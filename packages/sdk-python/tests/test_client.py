from __future__ import annotations

import asyncio
import base64
import hashlib
import hmac
import io
import json
import threading
import time
from typing import Any

import httpx
import pytest

import originalpictures


def test_client_configuration_rejects_embedded_credentials_and_invalid_bounds() -> None:
    with pytest.raises(originalpictures.ConfigurationError):
        originalpictures.Client(base_url="https://secret@example.test")
    with pytest.raises(originalpictures.ConfigurationError):
        originalpictures.Client(base_url="https://api.example", max_response_bytes=0)


@pytest.mark.parametrize("client_type", [originalpictures.Client, originalpictures.AsyncClient])
@pytest.mark.parametrize(
    "base_url",
    [
        "https://api.example?tenant=secret",
        "https://api.example#fragment",
        "https://api.example?",
        "https://api.example#",
    ],
)
def test_client_rejects_base_url_query_and_fragment_before_http(
    client_type: type[originalpictures.Client] | type[originalpictures.AsyncClient],
    base_url: str,
) -> None:
    calls = 0

    def handler(_request: httpx.Request) -> httpx.Response:
        nonlocal calls
        calls += 1
        return httpx.Response(200, json={})

    http: httpx.Client | httpx.AsyncClient
    if client_type is originalpictures.Client:
        http = httpx.Client(transport=httpx.MockTransport(handler))
    else:
        http = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    with pytest.raises(originalpictures.ConfigurationError, match="query or fragment"):
        client_type(base_url=base_url, api_key="must-not-send", http_client=http)  # type: ignore[arg-type]
    assert calls == 0


def test_client_preserves_base_url_path_prefix() -> None:
    seen: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(str(request.url))
        return httpx.Response(200, json={})

    client = originalpictures.Client(
        base_url="https://api.example/prefix/",
        api_key="test-key",
        http_client=httpx.Client(transport=httpx.MockTransport(handler)),
    )
    client.get_current_user()
    assert seen == ["https://api.example/prefix/v1/me"]


def test_generated_sync_operation_uses_authoritative_path_and_auth() -> None:
    seen: dict[str, Any] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["method"] = request.method
        seen["url"] = str(request.url)
        seen["auth"] = request.headers["authorization"]
        return httpx.Response(200, json={"job_id": "job_1", "state": "queued"})

    http = httpx.Client(transport=httpx.MockTransport(handler))
    client = originalpictures.Client(
        base_url="https://api.originalpictures.example", api_key="test-key", http_client=http
    )
    result = client.get_job(parameters={"job_id": "job_1"})
    assert result["job_id"] == "job_1"
    assert seen == {
        "method": "GET",
        "url": "https://api.originalpictures.example/v1/jobs/job_1",
        "auth": "Bearer test-key",
    }


@pytest.mark.asyncio
async def test_generated_async_operation_uses_typed_body_and_idempotency_header() -> None:
    async def handler(request: httpx.Request) -> httpx.Response:
        assert request.headers["idempotency-key"] == "verify-fixture"
        assert json.loads(request.content) == {"object_id": "obj_1"}
        return httpx.Response(202, json={"verification_id": "ver_1", "state": "queued"})

    http = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    client = originalpictures.AsyncClient(
        base_url="https://api.originalpictures.example", api_key="test-key", http_client=http
    )
    result = await client.create_verification(
        body={"object_id": "obj_1"}, headers={"Idempotency-Key": "verify-fixture"}
    )
    assert result["verification_id"] == "ver_1"
    await http.aclose()


def test_api_errors_are_typed_and_do_not_echo_secret_response_fields() -> None:
    def handler(_request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            403,
            headers={"x-request-id": "req_1"},
            json={
                "code": "SCOPE_REQUIRED",
                "detail": "opk_do-not-echo",
                "retryable": False,
                "field_details": {"scope": "assets:read"},
                "documentation_url": "https://docs.example/errors/SCOPE_REQUIRED",
                "job_reference": "job_fixture",
            },
        )

    client = originalpictures.Client(
        base_url="https://api.originalpictures.example",
        api_key="test-key",
        http_client=httpx.Client(transport=httpx.MockTransport(handler)),
    )
    with pytest.raises(originalpictures.PermissionDeniedError) as captured:
        client.get_current_user()
    assert captured.value.code == "SCOPE_REQUIRED"
    assert captured.value.request_id == "req_1"
    assert captured.value.retryable is False
    assert captured.value.field_details == {"scope": "assets:read"}
    assert captured.value.documentation_url == "https://docs.example/errors/SCOPE_REQUIRED"
    assert captured.value.job_reference == "job_fixture"
    assert "do-not-echo" not in str(captured.value)


def test_security_is_per_operation_and_provider_ingress_is_non_callable() -> None:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={})

    client = originalpictures.Client(
        base_url="https://api.originalpictures.example",
        api_key="private-key",
        http_client=httpx.Client(transport=httpx.MockTransport(handler)),
    )
    client.get_shared_verification(parameters={"token": "share-token"})
    assert "authorization" not in seen[0].headers
    with pytest.raises(originalpictures.ConfigurationError, match="intentionally non-callable"):
        client.request("receiveClerkWebhook", body={}, headers={}, parameters={})
    assert len(seen) == 1


def test_injected_redirecting_client_cannot_forward_transfer_capability() -> None:
    seen: list[tuple[str, str | None]] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append((str(request.url), request.headers.get("x-storage-grant")))
        if request.url.host == "storage.example":
            return httpx.Response(302, headers={"location": "https://other.example/file"})
        return httpx.Response(200, content=b"x")

    http = httpx.Client(transport=httpx.MockTransport(handler), follow_redirects=True)
    client = originalpictures.Client(base_url="https://api.example", http_client=http)
    with pytest.raises(originalpictures.TransportError, match="status 302"):
        client.download_stream(
            "https://storage.example/file",
            io.BytesIO(),
            byte_length=1,
            sha256=hashlib.sha256(b"x").hexdigest(),
            headers={"x-storage-grant": "secret-grant"},
        )
    assert seen == [("https://storage.example/file", "secret-grant")]


@pytest.mark.asyncio
async def test_injected_async_redirecting_client_cannot_forward_transfer_capability() -> None:
    seen: list[tuple[str, str | None]] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append((str(request.url), request.headers.get("x-storage-grant")))
        if request.url.host == "storage.example":
            return httpx.Response(302, headers={"location": "https://other.example/file"})
        return httpx.Response(200, content=b"x")

    http = httpx.AsyncClient(transport=httpx.MockTransport(handler), follow_redirects=True)
    client = originalpictures.AsyncClient(base_url="https://api.example", http_client=http)
    try:
        with pytest.raises(originalpictures.TransportError, match="status 302"):
            await client.download_stream(
                "https://storage.example/file",
                io.BytesIO(),
                byte_length=1,
                sha256=hashlib.sha256(b"x").hexdigest(),
                headers={"x-storage-grant": "secret-grant"},
            )
    finally:
        await http.aclose()
    assert seen == [("https://storage.example/file", "secret-grant")]


def test_exact_transfer_helpers_verify_bytes_and_never_forward_api_auth() -> None:
    payload = b"Original Pictures exact bytes"
    expected = hashlib.sha256(payload).hexdigest()

    def handler(request: httpx.Request) -> httpx.Response:
        assert "authorization" not in request.headers
        if request.method == "PUT":
            assert request.content == payload
            assert request.headers["content-length"] == str(len(payload))
            return httpx.Response(200)
        return httpx.Response(200, headers={"content-length": str(len(payload))}, content=payload)

    http = httpx.Client(transport=httpx.MockTransport(handler))
    client = originalpictures.Client(
        base_url="https://api.originalpictures.example", api_key="secret", http_client=http
    )
    uploaded = client.upload_stream(
        "https://storage.example/upload",
        io.BytesIO(payload),
        byte_length=len(payload),
        sha256=expected,
    )
    sink = io.BytesIO()
    downloaded = client.download_stream(
        "https://storage.example/download",
        sink,
        byte_length=len(payload),
        sha256=expected,
    )
    assert uploaded == downloaded == {"byte_length": len(payload), "sha256": expected}
    assert sink.getvalue() == payload


def test_transfer_integrity_and_authority_fail_closed() -> None:
    http = httpx.Client(transport=httpx.MockTransport(lambda _request: httpx.Response(200)))
    client = originalpictures.Client(base_url="https://api.example", http_client=http)
    with pytest.raises(ValueError, match="never be forwarded"):
        client.upload_stream(
            "https://storage.example/upload",
            io.BytesIO(b"x"),
            byte_length=1,
            sha256=hashlib.sha256(b"x").hexdigest(),
            headers={"Authorization": "Bearer forbidden"},
        )
    with pytest.raises(originalpictures.IntegrityError):
        client.download_stream(
            "https://storage.example/download",
            io.BytesIO(),
            byte_length=1,
            sha256=hashlib.sha256(b"x").hexdigest(),
        )


@pytest.mark.parametrize(
    "chunk_size", [-1, 0, originalpictures.MAX_TRANSFER_CHUNK_BYTES + 1, 1.5, True]
)
def test_sync_upload_rejects_unbounded_chunk_sizes_before_read(chunk_size: Any) -> None:
    class Source(io.BytesIO):
        reads = 0

        def read(self, size: int = -1) -> bytes:
            self.reads += 1
            return super().read(size)

    source = Source(b"x")
    client = originalpictures.Client(
        base_url="https://api.example",
        http_client=httpx.Client(transport=httpx.MockTransport(lambda _: httpx.Response(200))),
    )
    with pytest.raises(ValueError, match="chunk_size"):
        client.upload_stream(
            "https://storage.example/file",
            source,
            byte_length=1,
            sha256=hashlib.sha256(b"x").hexdigest(),
            chunk_size=chunk_size,
        )
    assert source.reads == 0


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "chunk_size", [-1, 0, originalpictures.MAX_TRANSFER_CHUNK_BYTES + 1, 1.5, True]
)
async def test_async_upload_rejects_unbounded_chunk_sizes_before_read(chunk_size: Any) -> None:
    class Source(io.BytesIO):
        reads = 0

        def read(self, size: int = -1) -> bytes:
            self.reads += 1
            return super().read(size)

    source = Source(b"x")
    http = httpx.AsyncClient(transport=httpx.MockTransport(lambda _: httpx.Response(200)))
    client = originalpictures.AsyncClient(base_url="https://api.example", http_client=http)
    try:
        with pytest.raises(ValueError, match="chunk_size"):
            await client.upload_stream(
                "https://storage.example/file",
                source,
                byte_length=1,
                sha256=hashlib.sha256(b"x").hexdigest(),
                chunk_size=chunk_size,
            )
    finally:
        await http.aclose()
    assert source.reads == 0


@pytest.mark.asyncio
async def test_async_upload_offloads_slow_reads_and_cleans_up_on_cancellation() -> None:
    started = threading.Event()
    release = threading.Event()

    class SlowSource:
        reads = 0

        def read(self, _size: int = -1) -> bytes:
            self.reads += 1
            started.set()
            release.wait(timeout=2)
            return b"x"

    async def handler(request: httpx.Request) -> httpx.Response:
        await request.aread()
        return httpx.Response(200)

    source = SlowSource()
    http = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    client = originalpictures.AsyncClient(base_url="https://api.example", http_client=http)
    task = asyncio.create_task(
        client.upload_stream(
            "https://storage.example/file",
            source,
            byte_length=1,
            sha256=hashlib.sha256(b"x").hexdigest(),
        )
    )
    assert await asyncio.to_thread(started.wait, 1)
    before = time.monotonic()
    await asyncio.sleep(0.01)
    assert time.monotonic() - before < 0.2
    task.cancel()
    try:
        with pytest.raises(asyncio.CancelledError):
            await task
    finally:
        release.set()
        await http.aclose()
    assert source.reads == 1


@pytest.mark.asyncio
async def test_async_download_offloads_bounded_sink_writes_and_drains_on_cancellation() -> None:
    payload = b"async sink fixture"
    expected = hashlib.sha256(payload).hexdigest()
    started = threading.Event()
    release = threading.Event()
    sink_threads: list[int] = []

    class SlowSink(io.BytesIO):
        def write(self, data: bytes) -> int:
            sink_threads.append(threading.get_ident())
            started.set()
            release.wait(timeout=2)
            return super().write(data)

    async def handler(_request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200,
            headers={"content-length": str(len(payload))},
            content=payload,
        )

    loop_thread = threading.get_ident()
    sink = SlowSink()
    http = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    client = originalpictures.AsyncClient(base_url="https://api.example", http_client=http)
    task = asyncio.create_task(
        client.download_stream(
            "https://storage.example/file",
            sink,
            byte_length=len(payload),
            sha256=expected,
        )
    )
    assert await asyncio.to_thread(started.wait, 1)
    before = time.monotonic()
    await asyncio.sleep(0.01)
    assert time.monotonic() - before < 0.1
    assert sink_threads == [sink_threads[0]]
    assert sink_threads[0] != loop_thread
    for _ in range(3):
        task.cancel()
        await asyncio.sleep(0)
        assert not task.done()
    release.set()
    try:
        with pytest.raises(asyncio.CancelledError):
            await task
    finally:
        await http.aclose()
    assert sink.getvalue() == payload
    bytes_at_return = sink.getvalue()
    await asyncio.sleep(0.02)
    assert sink.getvalue() == bytes_at_return
    assert task.cancelled()
    assert task.cancelling() == 1
    assert not any(
        active.get_name() == "originalpictures-sink-write"
        for active in asyncio.all_tasks()
        if not active.done()
    )


@pytest.mark.asyncio
async def test_async_download_preserves_sink_write_failure_without_leaked_task() -> None:
    payload = b"failing sink fixture"

    class FailingSink(io.BytesIO):
        def write(self, _data: bytes) -> int:
            raise OSError("sink write failed")

    http = httpx.AsyncClient(
        transport=httpx.MockTransport(
            lambda _request: httpx.Response(
                200,
                headers={"content-length": str(len(payload))},
                content=payload,
            )
        )
    )
    client = originalpictures.AsyncClient(base_url="https://api.example", http_client=http)
    try:
        with pytest.raises(OSError, match="sink write failed"):
            await client.download_stream(
                "https://storage.example/file",
                FailingSink(),
                byte_length=len(payload),
                sha256=hashlib.sha256(payload).hexdigest(),
            )
    finally:
        await http.aclose()
    await asyncio.sleep(0)
    assert not any(
        active.get_name() == "originalpictures-sink-write"
        for active in asyncio.all_tasks()
        if not active.done()
    )


def test_webhook_verifier_uses_exact_raw_body_and_timestamp() -> None:
    body = b'{"event_id":"evt_1"}'
    secret = b"s" * 32
    timestamp = 1_700_000_000
    signature = (
        "v1=" + hmac.new(secret, f"{timestamp}.evt_1.".encode() + body, hashlib.sha256).hexdigest()
    )
    originalpictures.verify_webhook(
        body,
        secret=secret,
        event_id="evt_1",
        timestamp=timestamp,
        signature=signature,
        now=timestamp,
    )
    with pytest.raises(originalpictures.RequestValidationError):
        originalpictures.verify_webhook(
            body + b" ",
            secret=secret,
            event_id="evt_1",
            timestamp=timestamp,
            signature=signature,
            now=timestamp,
        )


def test_webhook_verifier_accepts_either_standard_signer_during_overlap() -> None:
    body = b'{"event_id":"evt_overlap","value":1}'
    timestamp = 1_700_000_000
    old_key = b"1" * 32
    new_key = b"2" * 32
    old_secret = "whsec_" + base64.b64encode(old_key).decode("ascii")
    new_secret = "whsec_" + base64.b64encode(new_key).decode("ascii")
    message = f"evt_overlap.{timestamp}.".encode("ascii") + body
    signature = " ".join(
        "v1," + base64.b64encode(hmac.new(key, message, hashlib.sha256).digest()).decode("ascii")
        for key in (old_key, new_key)
    )

    for secret in (old_secret, new_secret):
        originalpictures.verify_webhook(
            body,
            secret=secret,
            event_id="evt_overlap",
            timestamp=timestamp,
            signature=signature,
            now=timestamp,
        )
    with pytest.raises(originalpictures.RequestValidationError):
        originalpictures.verify_webhook(
            body,
            secret="whsec_" + base64.b64encode(b"3" * 32).decode("ascii"),
            event_id="evt_overlap",
            timestamp=timestamp,
            signature=signature,
            now=timestamp,
        )
    with pytest.raises(originalpictures.RequestValidationError):
        originalpictures.verify_webhook(
            body + b" ",
            secret=new_secret,
            event_id="evt_overlap",
            timestamp=timestamp,
            signature=signature,
            now=timestamp,
        )
