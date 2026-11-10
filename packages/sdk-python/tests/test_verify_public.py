"""verify_public(): anonymous public checks against a verify page, with a mocked API."""

from __future__ import annotations

import asyncio
import io
import json
from pathlib import Path
from typing import Any

import httpx
import pytest

import originalpictures
import originalpictures.public_checks as public_checks
from originalpictures import (
    DeadlineExceededError,
    NotFoundError,
    RateLimitError,
    RequestValidationError,
    TransportError,
    fetch_verify_page,
    verify_public,
    verify_public_async,
)

BASE = "https://api.originalpictures.com/v1/public/verify-pages/studio-nova"
STATEMENT = (
    "This describes what the file declares about its origin and whether this provider's "
    "system has a record of it. It is not a judgement of whether the content is real."
)


def _check(state: str = "completed") -> dict[str, Any]:
    done = state == "completed"
    return {
        "schema_version": "op.public-check.v1",
        "check_id": "pchk_abcdefghijklmnop",
        "state": state,
        "page": {"slug": "studio-nova", "display_name": "Studio Nova"},
        "media_type": "image/jpeg",
        "content_credentials": {"status": "valid", "declared_origin": None} if done else None,
        "made_with": {
            "answer": "yes",
            "provider_name": "Studio Nova",
            "method": "c2pa_manifest",
            "recovery_checked": True,
        }
        if done
        else None,
        "statement": STATEMENT,
        "created_at": "2026-10-19T09:20:00Z",
        "completed_at": "2026-10-19T09:20:02Z" if done else None,
        "failure_reason": None,
    }


class Recorder:
    def __init__(self, *answers: httpx.Response) -> None:
        self.answers = list(answers)
        self.requests: list[httpx.Request] = []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        return self.answers.pop(0)


def _client(recorder: Recorder) -> httpx.Client:
    return httpx.Client(transport=httpx.MockTransport(recorder))


@pytest.fixture(autouse=True)
def no_waiting(monkeypatch: pytest.MonkeyPatch) -> list[float]:
    waits: list[float] = []
    monkeypatch.setattr(public_checks, "_sleep", waits.append)
    return waits


def test_exported_from_the_package() -> None:
    assert originalpictures.verify_public is verify_public
    assert "verify_public" in originalpictures.__all__


def test_posts_only_the_bytes_anonymously(tmp_path: Path) -> None:
    recorder = Recorder(httpx.Response(200, json=_check()))
    image = tmp_path / "holiday-in-lisbon.jpg"
    image.write_bytes(b"\xff\xd8\xff")
    result = verify_public(image, page="studio-nova", http_client=_client(recorder))
    assert result["made_with"]["answer"] == "yes"
    assert result["statement"] == STATEMENT
    request = recorder.requests[0]
    assert request.method == "POST"
    assert str(request.url) == f"{BASE}/checks"
    assert "authorization" not in request.headers
    body = request.read()
    assert b'name="file"; filename="upload"' in body
    assert b"holiday-in-lisbon" not in body
    assert b"\xff\xd8\xff" in body


def test_polls_a_running_check_no_faster_than_two_seconds(no_waiting: list[float]) -> None:
    recorder = Recorder(
        httpx.Response(202, json=_check("running")),
        httpx.Response(200, json=_check("running")),
        httpx.Response(200, json=_check()),
    )
    result = verify_public(
        b"bytes", page="studio-nova", poll_interval=0.1, http_client=_client(recorder)
    )
    assert result["state"] == "completed"
    assert no_waiting == [2.0, 2.0]
    assert [str(r.url) for r in recorder.requests[1:]] == [
        f"{BASE}/checks/pchk_abcdefghijklmnop"
    ] * 2


def test_waits_out_a_rate_limit_while_polling(no_waiting: list[float]) -> None:
    limited = httpx.Response(
        429, json={"code": "PUBLIC_CHECK_RATE_LIMITED"}, headers={"Retry-After": "7"}
    )
    recorder = Recorder(
        httpx.Response(202, json=_check("running")), limited, httpx.Response(200, json=_check())
    )
    verify_public(b"bytes", page="studio-nova", http_client=_client(recorder))
    assert no_waiting == [2.0, 7.0, 2.0]


def test_rate_limited_upload_raises_with_retry_after() -> None:
    recorder = Recorder(
        httpx.Response(
            429,
            json={"code": "PUBLIC_CHECK_RATE_LIMITED", "message": "slow down"},
            headers={"Retry-After": "42"},
        )
    )
    with pytest.raises(RateLimitError) as caught:
        verify_public(b"bytes", page="studio-nova", http_client=_client(recorder))
    assert caught.value.code == "PUBLIC_CHECK_RATE_LIMITED"
    assert caught.value.details["retry_after"] == "42"


def test_unknown_page_is_not_found() -> None:
    recorder = Recorder(httpx.Response(404, json={"code": "VERIFY_PAGE_NOT_FOUND"}))
    with pytest.raises(NotFoundError) as caught:
        fetch_verify_page("studio-nova", http_client=_client(recorder))
    assert caught.value.code == "VERIFY_PAGE_NOT_FOUND"


def test_reads_the_public_page_configuration() -> None:
    page = {"schema_version": "op.public-verify-page.v1", "slug": "studio-nova"}
    recorder = Recorder(httpx.Response(200, json=page))
    assert fetch_verify_page("studio-nova", http_client=_client(recorder)) == page
    assert str(recorder.requests[0].url) == BASE


@pytest.mark.parametrize(
    ("kwargs", "code"),
    [
        ({"page": "../admin"}, "VERIFY_PAGE_INVALID"),
        ({"page": "studio-nova", "api_base": "http://evil.example"}, "VERIFY_PAGE_INVALID"),
        ({"page": "studio-nova", "max_upload_bytes": 2}, "MEDIA_COMPRESSED_SIZE_LIMIT"),
    ],
)
def test_refuses_before_any_request(kwargs: dict[str, Any], code: str) -> None:
    recorder = Recorder()
    with pytest.raises(RequestValidationError) as caught:
        verify_public(io.BytesIO(b"bytes"), http_client=_client(recorder), **kwargs)
    assert caught.value.code == code
    assert recorder.requests == []


def test_refuses_an_unexpected_answer() -> None:
    recorder = Recorder(httpx.Response(200, json={**_check(), "check_id": "chk_1"}))
    with pytest.raises(originalpictures.ApiError):
        verify_public(b"bytes", page="studio-nova", http_client=_client(recorder))


def test_network_failure_is_a_transport_error() -> None:
    def fail(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("down", request=request)

    with pytest.raises(TransportError):
        verify_public(
            b"bytes",
            page="studio-nova",
            http_client=httpx.Client(transport=httpx.MockTransport(fail)),
        )


def test_gives_up_after_the_deadline() -> None:
    recorder = Recorder(httpx.Response(202, json=_check("running")))
    with pytest.raises(DeadlineExceededError):
        verify_public(b"bytes", page="studio-nova", timeout=1.0, http_client=_client(recorder))


def test_async_form(monkeypatch: pytest.MonkeyPatch) -> None:
    async def instant(_: float) -> None:
        return None

    monkeypatch.setattr(public_checks.asyncio, "sleep", instant)
    recorder = Recorder(
        httpx.Response(202, json=_check("running")), httpx.Response(200, json=_check())
    )

    async def run() -> dict[str, Any]:
        async with httpx.AsyncClient(transport=httpx.MockTransport(recorder)) as client:
            return await verify_public_async(b"bytes", page="studio-nova", http_client=client)

    assert asyncio.run(run())["state"] == "completed"
    assert json.loads(json.dumps(recorder.requests[0].method)) == "POST"
