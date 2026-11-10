"""Anonymous public checks against a verify page (Module C2/C5).

``verify_public(file, page="studio-nova")`` does what ``<op-verify>`` does in a
browser: it posts one file to ``POST /v1/public/verify-pages/{slug}/checks`` and,
when the check answers 202, polls it no faster than every 2 seconds until it is
``completed`` or ``failed``. No API key is used or sent.

The result (``op.public-check.v1``) describes what the file *declares* about its
origin and whether the page owner's system has a record of it. It is not a
judgement of whether the content is real; show its ``statement`` with it.

Hand-written: this module is not generated from the OpenAPI document, because
the public routes are anonymous multipart calls outside the typed client.
"""

from __future__ import annotations

import asyncio
import json
import os
import re
import time
from collections.abc import Callable, Mapping
from typing import IO, Any

import httpx

from originalpictures.client import MAX_PUBLIC_CHECK_BYTES, _raise_api_error
from originalpictures.errors import (
    ApiError,
    DeadlineExceededError,
    RateLimitError,
    RequestValidationError,
    TransportError,
)

DEFAULT_PUBLIC_API_BASE = "https://api.originalpictures.com"
#: op_domain.verify_pages.PUBLIC_CHECK_MAX_BYTES; one value with the client's
#: ``MAX_PUBLIC_CHECK_BYTES`` (``Client.verify_public``).
PUBLIC_CHECK_MAX_BYTES = MAX_PUBLIC_CHECK_BYTES
#: The contract asks clients to poll a running check at most every 2 seconds.
MIN_POLL_INTERVAL_SECONDS = 2.0
_SLUG_RE = re.compile(r"^[a-z0-9](?:[a-z0-9-]{1,46})[a-z0-9]$")
_CHECK_ID_RE = re.compile(r"^pchk_[a-z2-7]{16}$")
_STATES = frozenset({"running", "completed", "failed"})
_LOOPBACK = frozenset({"localhost", "127.0.0.1", "::1"})

FileInput = bytes | bytearray | str | os.PathLike[str] | IO[bytes]

# Indirection so tests can run polling without waiting.
_sleep: Callable[[float], None] = time.sleep


def _base_url(api_base: str) -> str:
    parsed = httpx.URL(api_base)
    host = parsed.host
    if parsed.scheme != "https" and not (parsed.scheme == "http" and host in _LOOPBACK):
        raise RequestValidationError(
            "api_base must use https", status_code=400, code="VERIFY_PAGE_INVALID"
        )
    if parsed.query or parsed.fragment or parsed.userinfo:
        raise RequestValidationError(
            "api_base must be a plain origin", status_code=400, code="VERIFY_PAGE_INVALID"
        )
    return str(parsed).rstrip("/")


def _page_url(api_base: str, page: str) -> str:
    if not _SLUG_RE.fullmatch(page):
        raise RequestValidationError(
            "the verify page name is not valid", status_code=400, code="VERIFY_PAGE_INVALID"
        )
    return f"{_base_url(api_base)}/v1/public/verify-pages/{page}"


def _read_file(file: FileInput, limit: int) -> bytes:
    if isinstance(file, bytes | bytearray):
        data = bytes(file)
    elif isinstance(file, str | os.PathLike):
        with open(file, "rb") as handle:
            data = handle.read(limit + 1)
    else:
        data = file.read(limit + 1)
    if not data:
        raise RequestValidationError(
            "the file is empty", status_code=400, code="VERIFY_PAGE_INVALID"
        )
    if len(data) > limit:
        raise RequestValidationError(
            f"the file is larger than {limit // (1024 * 1024)} MB",
            status_code=413,
            code="MEDIA_COMPRESSED_SIZE_LIMIT",
        )
    return data


def _decode(response: httpx.Response) -> object:
    payload: object | None = None
    if response.content:
        try:
            payload = json.loads(response.content)
        except (UnicodeDecodeError, json.JSONDecodeError):
            payload = None
    if not response.is_success:
        _raise_api_error(response, payload)
    return payload


def _check(payload: object, status_code: int) -> dict[str, Any]:
    if (
        not isinstance(payload, dict)
        or payload.get("schema_version") != "op.public-check.v1"
        or not isinstance(payload.get("check_id"), str)
        or not _CHECK_ID_RE.fullmatch(payload["check_id"])
        or payload.get("state") not in _STATES
    ):
        raise ApiError("unexpected public check response", status_code=status_code)
    return payload


def _page(payload: object, status_code: int) -> dict[str, Any]:
    if not isinstance(payload, dict) or payload.get("schema_version") != (
        "op.public-verify-page.v1"
    ):
        raise ApiError("unexpected verify page response", status_code=status_code)
    return payload


def _retry_after(headers: Mapping[str, str]) -> float:
    value = headers.get("retry-after")
    try:
        return max(float(value), 1.0) if value is not None else 5.0
    except ValueError:
        return 5.0


def fetch_verify_page(
    page: str,
    *,
    api_base: str = DEFAULT_PUBLIC_API_BASE,
    timeout: float = 30.0,
    http_client: httpx.Client | None = None,
) -> dict[str, Any]:
    """Read a verify page's public configuration (op.public-verify-page.v1)."""

    url = _page_url(api_base, page)
    client = http_client or httpx.Client(timeout=timeout)
    try:
        response = client.get(url, headers={"Accept": "application/json"})
    except httpx.HTTPError as error:
        raise TransportError("the verify service could not be reached") from error
    finally:
        if http_client is None:
            client.close()
    return _page(_decode(response), response.status_code)


def verify_public(
    file: FileInput,
    *,
    page: str,
    api_base: str = DEFAULT_PUBLIC_API_BASE,
    poll_interval: float = MIN_POLL_INTERVAL_SECONDS,
    timeout: float = 300.0,
    request_timeout: float = 60.0,
    max_upload_bytes: int = PUBLIC_CHECK_MAX_BYTES,
    http_client: httpx.Client | None = None,
) -> dict[str, Any]:
    """Check one file against a verify page and return the terminal result.

    ``file`` is bytes, a path, or a binary file object. Only the bytes are sent,
    under a neutral part name; the file name is not. The result's ``state`` is
    ``completed`` or ``failed``. Raises ``RateLimitError`` (with
    ``details['retry_after']``), ``NotFoundError`` for an unknown page,
    ``RequestValidationError`` for an unreadable or oversized file,
    ``DeadlineExceededError`` after ``timeout`` seconds of polling.
    """

    base = _page_url(api_base, page)
    data = _read_file(file, max_upload_bytes)
    interval = max(poll_interval, MIN_POLL_INTERVAL_SECONDS)
    deadline = time.monotonic() + timeout
    client = http_client or httpx.Client(timeout=request_timeout)
    try:
        response = _send(
            client,
            "POST",
            f"{base}/checks",
            files={"file": ("upload", data, "application/octet-stream")},
        )
        snapshot = _check(_decode_rate_limited(response), response.status_code)
        while snapshot["state"] == "running":
            if time.monotonic() + interval > deadline:
                raise DeadlineExceededError("the public check did not finish in time")
            _sleep(interval)
            response = _send(client, "GET", f"{base}/checks/{snapshot['check_id']}")
            try:
                snapshot = _check(_decode_rate_limited(response), response.status_code)
            except RateLimitError:
                _sleep(_retry_after(response.headers))
        return snapshot
    finally:
        if http_client is None:
            client.close()


def _send(client: httpx.Client, method: str, url: str, **kwargs: Any) -> httpx.Response:
    try:
        return client.request(method, url, headers={"Accept": "application/json"}, **kwargs)
    except httpx.HTTPError as error:
        raise TransportError("the verify service could not be reached") from error


def _decode_rate_limited(response: httpx.Response) -> object:
    try:
        return _decode(response)
    except RateLimitError as error:
        retry_after = response.headers.get("retry-after")
        if retry_after is not None:
            error.details["retry_after"] = retry_after
        raise


async def verify_public_async(
    file: FileInput,
    *,
    page: str,
    api_base: str = DEFAULT_PUBLIC_API_BASE,
    poll_interval: float = MIN_POLL_INTERVAL_SECONDS,
    timeout: float = 300.0,
    request_timeout: float = 60.0,
    max_upload_bytes: int = PUBLIC_CHECK_MAX_BYTES,
    http_client: httpx.AsyncClient | None = None,
) -> dict[str, Any]:
    """The asynchronous form of :func:`verify_public`."""

    base = _page_url(api_base, page)
    data = _read_file(file, max_upload_bytes)
    interval = max(poll_interval, MIN_POLL_INTERVAL_SECONDS)
    loop = asyncio.get_running_loop()
    deadline = loop.time() + timeout
    client = http_client or httpx.AsyncClient(timeout=request_timeout)
    try:

        async def send(method: str, url: str, **kwargs: Any) -> httpx.Response:
            try:
                return await client.request(
                    method, url, headers={"Accept": "application/json"}, **kwargs
                )
            except httpx.HTTPError as error:
                raise TransportError("the verify service could not be reached") from error

        response = await send(
            "POST", f"{base}/checks", files={"file": ("upload", data, "application/octet-stream")}
        )
        snapshot = _check(_decode_rate_limited(response), response.status_code)
        while snapshot["state"] == "running":
            if loop.time() + interval > deadline:
                raise DeadlineExceededError("the public check did not finish in time")
            await asyncio.sleep(interval)
            response = await send("GET", f"{base}/checks/{snapshot['check_id']}")
            try:
                snapshot = _check(_decode_rate_limited(response), response.status_code)
            except RateLimitError:
                await asyncio.sleep(_retry_after(response.headers))
        return snapshot
    finally:
        if http_client is None:
            await client.aclose()


__all__ = [
    "DEFAULT_PUBLIC_API_BASE",
    "MIN_POLL_INTERVAL_SECONDS",
    "PUBLIC_CHECK_MAX_BYTES",
    "fetch_verify_page",
    "verify_public",
    "verify_public_async",
]
