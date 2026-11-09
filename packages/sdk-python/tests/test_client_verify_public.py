"""Client.verify_public and AsyncClient.verify_public: the public check on an existing client."""

from __future__ import annotations

from pathlib import Path

import httpx
import pytest

import originalpictures
from originalpictures.errors import RateLimitError

SLUG = "studio-nova"
CHECK_ID = "pchk_abcdefghijklmnop"


def _completed(state: str = "completed") -> dict[str, object]:
    return {
        "schema_version": "op.public-check.v1",
        "check_id": CHECK_ID,
        "state": state,
        "page": {"slug": SLUG, "display_name": "Studio Nova"},
        "media_type": "image/jpeg",
        "content_credentials": None,
        "made_with": None,
        "statement": "It is not a judgement of whether the content is real.",
        "created_at": "2026-10-19T10:00:00Z",
        "completed_at": None,
        "failure_reason": None,
    }


def test_sends_one_multipart_file_without_a_key_or_the_local_name(tmp_path: Path) -> None:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json=_completed())

    source = tmp_path / "holiday-private-name.jpg"
    source.write_bytes(b"\xff\xd8 not really a jpeg")
    client = originalpictures.Client(
        base_url="https://api.example",
        api_key="never-sent",
        http_client=httpx.Client(transport=httpx.MockTransport(handler)),
    )

    result = client.verify_public(SLUG, source)

    assert result == _completed()
    (request,) = seen
    assert request.method == "POST"
    assert request.url.path == f"/v1/public/verify-pages/{SLUG}/checks"
    assert "authorization" not in request.headers
    assert request.headers["content-type"].startswith("multipart/form-data")
    body = request.read()
    assert b'name="file"' in body
    assert b"holiday-private-name" not in body


@pytest.mark.asyncio
async def test_async_polls_a_running_check_until_it_completes(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(originalpictures.client, "PUBLIC_CHECK_POLL_INTERVAL_SECONDS", 0.01)
    states = iter(["running", "completed"])
    seen: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(f"{request.method} {request.url.path}")
        if request.method == "POST":
            return httpx.Response(202, json=_completed("running"))
        return httpx.Response(200, json=_completed(next(states)))

    client = originalpictures.AsyncClient(
        base_url="https://api.example",
        http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler)),
    )

    result = await client.verify_public(SLUG, b"bytes", timeout=5.0)

    assert isinstance(result, dict) and result["state"] == "completed"
    assert seen[0] == f"POST /v1/public/verify-pages/{SLUG}/checks"
    assert seen[1:] == [f"GET /v1/public/verify-pages/{SLUG}/checks/{CHECK_ID}"] * 2


def test_refuses_bad_input_before_any_request(tmp_path: Path) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        raise AssertionError("no request expected")

    client = originalpictures.Client(
        base_url="https://api.example",
        http_client=httpx.Client(transport=httpx.MockTransport(handler)),
    )
    with pytest.raises(ValueError, match="slug"):
        client.verify_public("../admin", b"x")
    with pytest.raises(ValueError, match="empty"):
        client.verify_public(SLUG, b"")
    with pytest.raises(ValueError, match="25 MB"):
        client.verify_public(SLUG, b"x" * (originalpictures.MAX_PUBLIC_CHECK_BYTES + 1))
    target = tmp_path / "target.jpg"
    target.write_bytes(b"x")
    link = tmp_path / "link.jpg"
    link.symlink_to(target)
    with pytest.raises(ValueError, match="regular file"):
        client.verify_public(SLUG, link)
    with pytest.raises(ValueError, match="regular file"):
        client.verify_public(SLUG, tmp_path)


def test_rate_limit_is_typed() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            429,
            headers={"Retry-After": "30"},
            json={"code": "PUBLIC_CHECK_RATE_LIMITED", "retryable": True, "message": "slow down"},
        )

    client = originalpictures.Client(
        base_url="https://api.example",
        http_client=httpx.Client(transport=httpx.MockTransport(handler)),
    )
    with pytest.raises(RateLimitError) as raised:
        client.verify_public(SLUG, b"x")
    assert raised.value.code == "PUBLIC_CHECK_RATE_LIMITED"
