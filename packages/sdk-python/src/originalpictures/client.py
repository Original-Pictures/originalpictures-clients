"""HTTPX transport for the generated Original Pictures public API surface."""

from __future__ import annotations

import asyncio
import hashlib
import json
import os
import re
import tempfile
from collections.abc import AsyncIterator, Iterator, Mapping
from contextlib import suppress
from pathlib import Path
from typing import Any, BinaryIO
from urllib.parse import quote, urlsplit

import httpx

from originalpictures._generated.public_api import (
    PUBLIC_API_OPERATIONS,
    GeneratedAsyncClientMixin,
    GeneratedClientMixin,
    PublicApiOperationContract,
)
from originalpictures.errors import (
    ApiError,
    AuthenticationError,
    ConfigurationError,
    ConflictError,
    DeadlineExceededError,
    IntegrityError,
    NotFoundError,
    PermissionDeniedError,
    RateLimitError,
    RequestValidationError,
    ResponseTooLargeError,
    ServiceUnavailableError,
    TransportError,
)

DEFAULT_MAX_RESPONSE_BYTES = 16 * 1024 * 1024
DEFAULT_MAX_TRANSFER_BYTES = 5 * 1024 * 1024 * 1024
DEFAULT_TRANSFER_CHUNK_BYTES = 1024 * 1024
MAX_TRANSFER_CHUNK_BYTES = 8 * 1024 * 1024
_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
_OPERATIONS = {operation.operation_id: operation for operation in PUBLIC_API_OPERATIONS}
_PATH_PARAMETER_RE = re.compile(r"\{([^{}]+)\}")
_FORBIDDEN_EXTERNAL_HEADERS = {"authorization", "proxy-authorization", "cookie"}
#: The public check's upload ceiling (POST /v1/public/verify-pages/{slug}/checks).
#: ``originalpictures.public_checks.PUBLIC_CHECK_MAX_BYTES`` is the same value.
MAX_PUBLIC_CHECK_BYTES = 25 * 1024 * 1024
#: The public check contract asks clients to poll a running check at most every 2 seconds.
PUBLIC_CHECK_POLL_INTERVAL_SECONDS = 2.0
_PUBLIC_SLUG_RE = re.compile(r"^[a-z0-9](?:[a-z0-9-]{1,46})[a-z0-9]$")


def _validate_client(base_url: str, api_key: str | None) -> str:
    parsed = urlsplit(base_url)
    if (
        not base_url
        or parsed.scheme not in {"http", "https"}
        or not parsed.hostname
        or parsed.username is not None
        or parsed.password is not None
        or bool(parsed.query)
        or bool(parsed.fragment)
        or "?" in base_url
        or "#" in base_url
    ):
        raise ConfigurationError(
            "base_url must be an absolute HTTP(S) URL without a query or fragment"
        )
    if api_key is not None and (not api_key.strip() or "\n" in api_key or "\r" in api_key):
        raise ConfigurationError("api_key is invalid")
    return base_url.rstrip("/")


def _operation(operation_id: str) -> PublicApiOperationContract:
    try:
        return _OPERATIONS[operation_id]
    except KeyError as error:
        raise ValueError(f"unknown generated operation: {operation_id}") from error


def _request_parts(
    operation: PublicApiOperationContract,
    parameters: Mapping[str, Any] | None,
    headers: Mapping[str, Any] | None,
) -> tuple[str, list[tuple[str, str | int | float | bool | None]], dict[str, str]]:
    remaining = dict(parameters or {})
    path = operation.path
    for name in _PATH_PARAMETER_RE.findall(path):
        if name not in remaining or remaining[name] is None:
            raise ValueError(f"missing required path parameter: {name}")
        value = quote(str(remaining.pop(name)), safe="")
        path = path.replace("{" + name + "}", value)
    query: list[tuple[str, str | int | float | bool | None]] = []
    for name, value in remaining.items():
        if value is None:
            continue
        if isinstance(value, (list, tuple)):
            query.extend((name, str(item)) for item in value)
        else:
            query.append((name, str(value)))
    resolved_headers = {str(name): str(value) for name, value in (headers or {}).items()}
    if any(
        name.lower() in {"authorization", "host", "content-length"} for name in resolved_headers
    ):
        raise ValueError("generated operation headers may not override transport authority")
    return path, query, resolved_headers


def _safe_external_url(url: str) -> None:
    parsed = urlsplit(url)
    if parsed.username or parsed.password or not parsed.hostname:
        raise ValueError("transfer URL is invalid")
    if parsed.scheme == "https":
        return
    if parsed.scheme == "http" and parsed.hostname in {"127.0.0.1", "localhost", "::1"}:
        return
    raise ValueError("transfer URL must use HTTPS (except loopback tests)")


def _external_headers(headers: Mapping[str, str] | None) -> dict[str, str]:
    result = dict(headers or {})
    if any(name.lower() in _FORBIDDEN_EXTERNAL_HEADERS for name in result):
        raise ValueError("API credentials must never be forwarded to transfer URLs")
    return result


def _public_check_content(file: str | Path | bytes) -> bytes:
    """The bytes to check: a regular file (never a symlink) or bytes, at most 25 MB."""

    if isinstance(file, bytes):
        content = file
    else:
        path = Path(file)
        if path.is_symlink() or not path.is_file():
            raise ValueError("the file to check must be a regular file")
        if path.stat().st_size > MAX_PUBLIC_CHECK_BYTES:
            raise ValueError("the file to check is larger than 25 MB")
        content = path.read_bytes()
    if not content:
        raise ValueError("the file to check is empty")
    if len(content) > MAX_PUBLIC_CHECK_BYTES:
        raise ValueError("the file to check is larger than 25 MB")
    return content


def _public_check_path(slug: str) -> str:
    if _PUBLIC_SLUG_RE.fullmatch(slug) is None:
        raise ValueError("slug is not a verify page slug")
    return f"/v1/public/verify-pages/{slug}/checks"


def _public_check_files(content: bytes) -> dict[str, tuple[str, bytes, str]]:
    # A fixed part name: the local file name is not the API's business, and the public
    # check never records it anyway.
    return {"file": ("file", content, "application/octet-stream")}


def _public_check_running(result: object) -> bool:
    return isinstance(result, Mapping) and result.get("state") == "running"


def _public_check_id(result: object) -> str:
    check_id = result.get("check_id") if isinstance(result, Mapping) else None
    if not isinstance(check_id, str) or not check_id.startswith("pchk_"):
        raise TransportError("Original Pictures returned a running check without a check_id")
    return check_id


def _uses_bearer_auth(operation: PublicApiOperationContract) -> bool:
    if not operation.executable:
        schemes = sorted(
            {scheme for alternative in operation.security_alternatives for scheme in alternative}
        )
        joined = ", ".join(schemes) or "unknown"
        raise ConfigurationError(
            f"operation {operation.operation_id} is typed but intentionally non-callable; "
            f"it requires exact raw-body security scheme(s): {joined}"
        )
    if not operation.security_alternatives or any(
        not alternative for alternative in operation.security_alternatives
    ):
        return False
    if any(alternative == ("bearerAuth",) for alternative in operation.security_alternatives):
        return True
    raise ConfigurationError(
        f"operation {operation.operation_id} has no supported security alternative"
    )


def _validate_chunk_size(chunk_size: int) -> None:
    if (
        not isinstance(chunk_size, int)
        or isinstance(chunk_size, bool)
        or not 1 <= chunk_size <= MAX_TRANSFER_CHUNK_BYTES
    ):
        raise ValueError(f"chunk_size must be between 1 and {MAX_TRANSFER_CHUNK_BYTES} bytes")


def _validate_integrity(expected_length: int, expected_sha256: str, max_bytes: int) -> None:
    if expected_length < 0 or expected_length > max_bytes:
        raise ValueError("byte length is outside the configured transfer bound")
    if not _SHA256_RE.fullmatch(expected_sha256):
        raise ValueError("expected_sha256 must be lowercase hexadecimal SHA-256")


def _safe_error_fields(payload: object | None) -> dict[str, Any]:
    if not isinstance(payload, dict):
        return {}
    safe: dict[str, Any] = {}
    for name in ("code", "reason_code", "request_id", "documentation_url", "job_reference"):
        value = payload.get(name)
        if isinstance(value, str) and len(value) <= 2048:
            safe[name] = value
    retryable = payload.get("retryable")
    if isinstance(retryable, bool):
        safe["retryable"] = retryable
    field_details = payload.get("field_details")
    if isinstance(field_details, dict):
        safe["field_details"] = {
            str(name)[:128]: value[:512]
            for name, value in field_details.items()
            if isinstance(name, str) and isinstance(value, str)
        }
    validation = payload.get("detail")
    if isinstance(validation, list):
        safe["validation_errors"] = [
            {
                name: item[name]
                for name in ("loc", "type")
                if name in item and isinstance(item[name], (str, list))
            }
            for item in validation
            if isinstance(item, dict)
        ]
    return safe


def _raise_api_error(response: httpx.Response, payload: object | None = None) -> None:
    status = response.status_code
    error_type: type[ApiError]
    if status == 401:
        error_type = AuthenticationError
    elif status in {402, 403}:
        error_type = PermissionDeniedError
    elif status == 404:
        error_type = NotFoundError
    elif status in {409, 410}:
        error_type = ConflictError
    elif status in {400, 413, 422}:
        error_type = RequestValidationError
    elif status == 429:
        error_type = RateLimitError
    elif status >= 500:
        error_type = ServiceUnavailableError
    else:
        error_type = ApiError
    safe = _safe_error_fields(payload)
    candidate = safe.get("code") or safe.get("reason_code")
    code = candidate if isinstance(candidate, str) and len(candidate) <= 128 else None
    messages = {
        AuthenticationError: "Original Pictures authentication failed",
        PermissionDeniedError: "Original Pictures permission denied",
        NotFoundError: "Original Pictures resource not found",
        ConflictError: "Original Pictures request conflict",
        RequestValidationError: "Original Pictures request validation failed",
        RateLimitError: "Original Pictures rate limit exceeded",
        ServiceUnavailableError: "Original Pictures service unavailable",
        ApiError: "Original Pictures API request failed",
    }
    raise error_type(
        messages[error_type],
        status_code=status,
        code=code,
        request_id=response.headers.get("x-request-id")
        or (safe.get("request_id") if isinstance(safe.get("request_id"), str) else None),
        retryable=safe.get("retryable") if isinstance(safe.get("retryable"), bool) else None,
        field_details=safe.get("field_details")
        if isinstance(safe.get("field_details"), dict)
        else None,
        documentation_url=safe.get("documentation_url")
        if isinstance(safe.get("documentation_url"), str)
        else None,
        job_reference=safe.get("job_reference")
        if isinstance(safe.get("job_reference"), str)
        else None,
        validation_errors=safe.get("validation_errors")
        if isinstance(safe.get("validation_errors"), list)
        else None,
        details=safe,
    )


def _decode_response(response: httpx.Response, content: bytes) -> object:
    if not 200 <= response.status_code < 300:
        payload: object | None = None
        if content and "json" in response.headers.get("content-type", ""):
            with suppress(UnicodeDecodeError, json.JSONDecodeError):
                payload = json.loads(content)
        _raise_api_error(response, payload)
    if response.status_code == 204 or not content:
        return None
    try:
        return json.loads(content)
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise TransportError("Original Pictures returned an invalid JSON response") from error


def _read_response(response: httpx.Response, max_bytes: int) -> bytes:
    chunks: list[bytes] = []
    total = 0
    for chunk in response.iter_bytes():
        total += len(chunk)
        if total > max_bytes:
            raise ResponseTooLargeError("Original Pictures response exceeded the configured bound")
        chunks.append(chunk)
    return b"".join(chunks)


async def _read_response_async(response: httpx.Response, max_bytes: int) -> bytes:
    chunks: list[bytes] = []
    total = 0
    async for chunk in response.aiter_bytes():
        total += len(chunk)
        if total > max_bytes:
            raise ResponseTooLargeError("Original Pictures response exceeded the configured bound")
        chunks.append(chunk)
    return b"".join(chunks)


async def _write_sink_async(sink: BinaryIO, chunk: bytes) -> None:
    """Write one bounded chunk off-loop and drain it through repeated cancellation."""

    write = asyncio.create_task(
        asyncio.to_thread(sink.write, chunk), name="originalpictures-sink-write"
    )
    current = asyncio.current_task()
    cancellation_requested = False
    while not write.done():
        try:
            await asyncio.shield(write)
        except asyncio.CancelledError:
            cancellation_requested = True
            if current is not None:
                while current.cancelling():
                    current.uncancel()
        except Exception:
            if not cancellation_requested:
                raise
            break
    if cancellation_requested:
        with suppress(Exception):
            write.result()
        if current is None:
            raise asyncio.CancelledError
        current.cancel()
        await asyncio.sleep(0)
        raise AssertionError("task cancellation was not delivered")
    write.result()


class Client(GeneratedClientMixin):
    """Synchronous typed client covering every generated public operation."""

    def __init__(
        self,
        *,
        base_url: str,
        api_key: str | None = None,
        timeout: float | httpx.Timeout = 30.0,
        max_response_bytes: int = DEFAULT_MAX_RESPONSE_BYTES,
        http_client: httpx.Client | None = None,
    ) -> None:
        self.base_url = _validate_client(base_url, api_key)
        self.api_key = api_key
        if max_response_bytes <= 0:
            raise ConfigurationError("max_response_bytes must be positive")
        self.max_response_bytes = max_response_bytes
        self._owns_client = http_client is None
        self._http = http_client or httpx.Client(timeout=timeout, follow_redirects=False)

    def __enter__(self) -> Client:
        return self

    def __exit__(self, *_args: object) -> None:
        self.close()

    def close(self) -> None:
        if self._owns_client:
            self._http.close()

    def request(
        self,
        operation_id: str,
        *,
        parameters: Mapping[str, Any] | None = None,
        headers: Mapping[str, Any] | None = None,
        body: object | None = None,
    ) -> object:
        return self._request_operation(
            operation_id, parameters=parameters, headers=headers, body=body
        )

    def _request_operation(
        self,
        operation_id: str,
        *,
        parameters: Mapping[str, Any] | None = None,
        headers: Mapping[str, Any] | None = None,
        body: object | None = None,
    ) -> object:
        operation = _operation(operation_id)
        uses_bearer = _uses_bearer_auth(operation)
        if uses_bearer and self.api_key is None:
            raise ConfigurationError("this operation requires an Original Pictures API key")
        path, query, request_headers = _request_parts(operation, parameters, headers)
        if uses_bearer and self.api_key is not None:
            request_headers["Authorization"] = f"Bearer {self.api_key}"
        try:
            with self._http.stream(
                operation.method,
                self.base_url + path,
                params=httpx.QueryParams(query),
                headers=request_headers,
                json=body if operation.request_content_types else None,
                follow_redirects=False,
            ) as response:
                content = _read_response(response, self.max_response_bytes)
                return _decode_response(response, content)
        except httpx.TimeoutException as error:
            raise DeadlineExceededError("Original Pictures request deadline exceeded") from error
        except httpx.RequestError as error:
            raise TransportError("Original Pictures transport failed") from error

    def verify_public(
        self,
        slug: str,
        file: str | Path | bytes,
        *,
        timeout: float = 120.0,
    ) -> object:
        """Check one file against a public verify page, without an API key.

        Sends the file to ``POST /v1/public/verify-pages/{slug}/checks`` and, while the
        check is running, polls it every 2 seconds until ``timeout``. The result states
        the file's declared origin and whether the page owner's system has a record of
        it; show its ``statement`` with it. It is never a verdict on whether content is
        real.
        """

        path = _public_check_path(slug)
        content = _public_check_content(file)
        try:
            with self._http.stream(
                "POST",
                self.base_url + path,
                files=_public_check_files(content),
                follow_redirects=False,
            ) as response:
                result = _decode_response(
                    response, _read_response(response, self.max_response_bytes)
                )
        except httpx.TimeoutException as error:
            raise DeadlineExceededError("Original Pictures request deadline exceeded") from error
        except httpx.RequestError as error:
            raise TransportError("Original Pictures transport failed") from error
        if not _public_check_running(result):
            return result
        from originalpictures.helpers import poll

        check_id = _public_check_id(result)
        return poll(
            lambda: self._request_operation(
                "getPublicCheck", parameters={"slug": slug, "check_id": check_id}
            ),
            lambda value: not _public_check_running(value),
            timeout=timeout,
            interval=PUBLIC_CHECK_POLL_INTERVAL_SECONDS,
            max_interval=PUBLIC_CHECK_POLL_INTERVAL_SECONDS * 2,
            max_attempts=max(1, int(timeout / PUBLIC_CHECK_POLL_INTERVAL_SECONDS) + 1),
        )

    def upload_stream(
        self,
        url: str,
        source: BinaryIO,
        *,
        byte_length: int,
        sha256: str,
        headers: Mapping[str, str] | None = None,
        max_bytes: int = DEFAULT_MAX_TRANSFER_BYTES,
        chunk_size: int = DEFAULT_TRANSFER_CHUNK_BYTES,
    ) -> dict[str, int | str]:
        """PUT exact bytes to an API-issued URL without forwarding API auth."""

        _safe_external_url(url)
        _validate_integrity(byte_length, sha256, max_bytes)
        _validate_chunk_size(chunk_size)
        transfer_headers = _external_headers(headers)
        transfer_headers["Content-Length"] = str(byte_length)
        digest = hashlib.sha256()
        sent = 0

        def chunks() -> Iterator[bytes]:
            nonlocal sent
            while True:
                chunk = source.read(chunk_size)
                if not chunk:
                    break
                sent += len(chunk)
                if sent > byte_length:
                    raise IntegrityError("upload exceeded the authenticated byte length")
                digest.update(chunk)
                yield chunk

        try:
            with self._http.stream(
                "PUT", url, headers=transfer_headers, content=chunks(), follow_redirects=False
            ) as response:
                _read_response(response, min(self.max_response_bytes, 1024 * 1024))
                if not 200 <= response.status_code < 300:
                    raise TransportError(
                        f"transfer upload failed with status {response.status_code}"
                    )
        except httpx.TimeoutException as error:
            raise DeadlineExceededError("transfer upload deadline exceeded") from error
        except httpx.RequestError as error:
            raise TransportError("transfer upload failed") from error
        if sent != byte_length or digest.hexdigest() != sha256:
            raise IntegrityError("uploaded bytes failed length or SHA-256 verification")
        return {"byte_length": sent, "sha256": digest.hexdigest()}

    def download_stream(
        self,
        url: str,
        sink: BinaryIO,
        *,
        byte_length: int,
        sha256: str,
        headers: Mapping[str, str] | None = None,
        max_bytes: int = DEFAULT_MAX_TRANSFER_BYTES,
    ) -> dict[str, int | str]:
        """GET exact bytes and write only while authenticated bounds hold."""

        _safe_external_url(url)
        _validate_integrity(byte_length, sha256, max_bytes)
        digest = hashlib.sha256()
        received = 0
        try:
            with self._http.stream(
                "GET", url, headers=_external_headers(headers), follow_redirects=False
            ) as response:
                if not 200 <= response.status_code < 300:
                    raise TransportError(
                        f"transfer download failed with status {response.status_code}"
                    )
                declared = response.headers.get("content-length")
                if declared is not None:
                    try:
                        declared_length = int(declared)
                    except ValueError as error:
                        raise IntegrityError("download Content-Length is invalid") from error
                    if declared_length != byte_length:
                        raise IntegrityError(
                            "download Content-Length does not match authenticated length"
                        )
                for chunk in response.iter_bytes():
                    received += len(chunk)
                    if received > byte_length:
                        raise IntegrityError("download exceeded the authenticated byte length")
                    digest.update(chunk)
                    sink.write(chunk)
        except httpx.TimeoutException as error:
            raise DeadlineExceededError("transfer download deadline exceeded") from error
        except httpx.RequestError as error:
            raise TransportError("transfer download failed") from error
        if received != byte_length or digest.hexdigest() != sha256:
            raise IntegrityError("downloaded bytes failed length or SHA-256 verification")
        return {"byte_length": received, "sha256": digest.hexdigest()}

    def upload_file(self, url: str, path: str | Path, *, sha256: str, **kwargs: Any) -> object:
        resolved = Path(path)
        digest = hashlib.sha256()
        byte_length = 0
        with resolved.open("rb") as preflight:
            for chunk in iter(lambda: preflight.read(1024 * 1024), b""):
                byte_length += len(chunk)
                digest.update(chunk)
        if digest.hexdigest() != sha256:
            raise IntegrityError("upload file failed preflight SHA-256 verification")
        with resolved.open("rb") as source:
            return self.upload_stream(url, source, byte_length=byte_length, sha256=sha256, **kwargs)

    def download_file(
        self, url: str, path: str | Path, *, byte_length: int, sha256: str, **kwargs: Any
    ) -> object:
        destination = Path(path)
        destination.parent.mkdir(parents=True, exist_ok=True)
        descriptor, temporary_name = tempfile.mkstemp(
            prefix=f".{destination.name}.", suffix=".download", dir=destination.parent
        )
        temporary = Path(temporary_name)
        try:
            with os.fdopen(descriptor, "wb") as sink:
                result = self.download_stream(
                    url, sink, byte_length=byte_length, sha256=sha256, **kwargs
                )
                sink.flush()
                os.fsync(sink.fileno())
            os.replace(temporary, destination)
            return result
        except BaseException:
            temporary.unlink(missing_ok=True)
            raise


class AsyncClient(GeneratedAsyncClientMixin):
    """Asynchronous typed client covering every generated public operation."""

    def __init__(
        self,
        *,
        base_url: str,
        api_key: str | None = None,
        timeout: float | httpx.Timeout = 30.0,
        max_response_bytes: int = DEFAULT_MAX_RESPONSE_BYTES,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        self.base_url = _validate_client(base_url, api_key)
        self.api_key = api_key
        if max_response_bytes <= 0:
            raise ConfigurationError("max_response_bytes must be positive")
        self.max_response_bytes = max_response_bytes
        self._owns_client = http_client is None
        self._http = http_client or httpx.AsyncClient(timeout=timeout, follow_redirects=False)

    async def __aenter__(self) -> AsyncClient:
        return self

    async def __aexit__(self, *_args: object) -> None:
        await self.aclose()

    async def aclose(self) -> None:
        if self._owns_client:
            await self._http.aclose()

    async def request(
        self,
        operation_id: str,
        *,
        parameters: Mapping[str, Any] | None = None,
        headers: Mapping[str, Any] | None = None,
        body: object | None = None,
    ) -> object:
        return await self._request_operation_async(
            operation_id, parameters=parameters, headers=headers, body=body
        )

    async def _request_operation_async(
        self,
        operation_id: str,
        *,
        parameters: Mapping[str, Any] | None = None,
        headers: Mapping[str, Any] | None = None,
        body: object | None = None,
    ) -> object:
        operation = _operation(operation_id)
        uses_bearer = _uses_bearer_auth(operation)
        if uses_bearer and self.api_key is None:
            raise ConfigurationError("this operation requires an Original Pictures API key")
        path, query, request_headers = _request_parts(operation, parameters, headers)
        if uses_bearer and self.api_key is not None:
            request_headers["Authorization"] = f"Bearer {self.api_key}"
        try:
            async with self._http.stream(
                operation.method,
                self.base_url + path,
                params=httpx.QueryParams(query),
                headers=request_headers,
                json=body if operation.request_content_types else None,
                follow_redirects=False,
            ) as response:
                content = await _read_response_async(response, self.max_response_bytes)
                return _decode_response(response, content)
        except httpx.TimeoutException as error:
            raise DeadlineExceededError("Original Pictures request deadline exceeded") from error
        except httpx.RequestError as error:
            raise TransportError("Original Pictures transport failed") from error

    async def verify_public(
        self,
        slug: str,
        file: str | Path | bytes,
        *,
        timeout: float = 120.0,
    ) -> object:
        """Async counterpart to :meth:`Client.verify_public`."""

        path = _public_check_path(slug)
        content = await asyncio.to_thread(_public_check_content, file)
        try:
            async with self._http.stream(
                "POST",
                self.base_url + path,
                files=_public_check_files(content),
                follow_redirects=False,
            ) as response:
                result = _decode_response(
                    response, await _read_response_async(response, self.max_response_bytes)
                )
        except httpx.TimeoutException as error:
            raise DeadlineExceededError("Original Pictures request deadline exceeded") from error
        except httpx.RequestError as error:
            raise TransportError("Original Pictures transport failed") from error
        if not _public_check_running(result):
            return result
        from originalpictures.helpers import poll_async

        check_id = _public_check_id(result)
        return await poll_async(
            lambda: self._request_operation_async(
                "getPublicCheck", parameters={"slug": slug, "check_id": check_id}
            ),
            lambda value: not _public_check_running(value),
            timeout=timeout,
            interval=PUBLIC_CHECK_POLL_INTERVAL_SECONDS,
            max_interval=PUBLIC_CHECK_POLL_INTERVAL_SECONDS * 2,
            max_attempts=max(1, int(timeout / PUBLIC_CHECK_POLL_INTERVAL_SECONDS) + 1),
        )

    async def upload_stream(
        self,
        url: str,
        source: BinaryIO,
        *,
        byte_length: int,
        sha256: str,
        headers: Mapping[str, str] | None = None,
        max_bytes: int = DEFAULT_MAX_TRANSFER_BYTES,
        chunk_size: int = DEFAULT_TRANSFER_CHUNK_BYTES,
    ) -> dict[str, int | str]:
        _safe_external_url(url)
        _validate_integrity(byte_length, sha256, max_bytes)
        _validate_chunk_size(chunk_size)
        transfer_headers = _external_headers(headers)
        transfer_headers["Content-Length"] = str(byte_length)
        digest = hashlib.sha256()
        sent = 0

        async def chunks() -> AsyncIterator[bytes]:
            nonlocal sent
            while True:
                chunk = await asyncio.to_thread(source.read, chunk_size)
                if not chunk:
                    break
                sent += len(chunk)
                if sent > byte_length:
                    raise IntegrityError("upload exceeded the authenticated byte length")
                digest.update(chunk)
                yield chunk

        try:
            async with self._http.stream(
                "PUT", url, headers=transfer_headers, content=chunks(), follow_redirects=False
            ) as response:
                await _read_response_async(response, min(self.max_response_bytes, 1024 * 1024))
                if not 200 <= response.status_code < 300:
                    raise TransportError(
                        f"transfer upload failed with status {response.status_code}"
                    )
        except httpx.TimeoutException as error:
            raise DeadlineExceededError("transfer upload deadline exceeded") from error
        except httpx.RequestError as error:
            raise TransportError("transfer upload failed") from error
        if sent != byte_length or digest.hexdigest() != sha256:
            raise IntegrityError("uploaded bytes failed length or SHA-256 verification")
        return {"byte_length": sent, "sha256": digest.hexdigest()}

    async def download_stream(
        self,
        url: str,
        sink: BinaryIO,
        *,
        byte_length: int,
        sha256: str,
        headers: Mapping[str, str] | None = None,
        max_bytes: int = DEFAULT_MAX_TRANSFER_BYTES,
    ) -> dict[str, int | str]:
        _safe_external_url(url)
        _validate_integrity(byte_length, sha256, max_bytes)
        digest = hashlib.sha256()
        received = 0
        try:
            async with self._http.stream(
                "GET", url, headers=_external_headers(headers), follow_redirects=False
            ) as response:
                if not 200 <= response.status_code < 300:
                    raise TransportError(
                        f"transfer download failed with status {response.status_code}"
                    )
                declared = response.headers.get("content-length")
                if declared is not None:
                    try:
                        declared_length = int(declared)
                    except ValueError as error:
                        raise IntegrityError("download Content-Length is invalid") from error
                    if declared_length != byte_length:
                        raise IntegrityError(
                            "download Content-Length does not match authenticated length"
                        )
                async for chunk in response.aiter_bytes(chunk_size=DEFAULT_TRANSFER_CHUNK_BYTES):
                    received += len(chunk)
                    if received > byte_length:
                        raise IntegrityError("download exceeded the authenticated byte length")
                    digest.update(chunk)
                    await _write_sink_async(sink, chunk)
        except httpx.TimeoutException as error:
            raise DeadlineExceededError("transfer download deadline exceeded") from error
        except httpx.RequestError as error:
            raise TransportError("transfer download failed") from error
        if received != byte_length or digest.hexdigest() != sha256:
            raise IntegrityError("downloaded bytes failed length or SHA-256 verification")
        return {"byte_length": received, "sha256": digest.hexdigest()}


__all__ = [
    "AsyncClient",
    "Client",
    "DEFAULT_MAX_RESPONSE_BYTES",
    "DEFAULT_MAX_TRANSFER_BYTES",
    "DEFAULT_TRANSFER_CHUNK_BYTES",
    "MAX_PUBLIC_CHECK_BYTES",
    "MAX_TRANSFER_CHUNK_BYTES",
    "PUBLIC_CHECK_POLL_INTERVAL_SECONDS",
]
