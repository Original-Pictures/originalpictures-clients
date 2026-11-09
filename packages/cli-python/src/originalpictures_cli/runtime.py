"""SDK lifecycle and stable error translation."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any, Protocol

import click

from originalpictures_cli.config import ConfigStore, ConfigurationFailure, ResolvedProfile
from originalpictures_cli.exit_codes import ExitCode
from originalpictures_cli.output import Output


class ClientLike(Protocol):
    def close(self) -> None: ...


class ClientFactory(Protocol):
    def __call__(
        self,
        *,
        base_url: str,
        api_key: str | None,
        timeout: float,
        max_response_bytes: int,
    ) -> ClientLike: ...


@dataclass(frozen=True)
class Failure:
    exit_code: ExitCode
    kind: str
    message: str
    details: Any | None = None


@dataclass
class Runtime:
    store: ConfigStore
    output: Output
    profile_name: str | None = None
    api_url: str | None = None
    timeout: float = 30.0
    max_response_bytes: int = 16 * 1024 * 1024
    client_factory: ClientFactory | None = None
    _profile: ResolvedProfile | None = field(default=None, init=False)
    _client: ClientLike | None = field(default=None, init=False)

    @property
    def profile(self) -> ResolvedProfile:
        if self._profile is None:
            self._profile = self.store.resolve(profile=self.profile_name, api_url=self.api_url)
        return self._profile

    @property
    def known_secrets(self) -> tuple[str, ...]:
        try:
            return (self.profile.api_key,) if self.profile.api_key else ()
        except ConfigurationFailure:
            return ()

    def client(self, *, authentication_required: bool = True) -> ClientLike:
        if authentication_required and self.profile.api_key is None:
            raise ConfigurationFailure(
                "no API credential is configured; use auth login or ORIGINALPICTURES_API_KEY"
            )
        if self._client is None:
            factory = self.client_factory or _default_client_factory
            self._client = factory(
                base_url=self.profile.api_url,
                api_key=self.profile.api_key,
                timeout=self.timeout,
                max_response_bytes=self.max_response_bytes,
            )
        return self._client

    def close(self) -> None:
        if self._client is not None:
            self._client.close()
            self._client = None


def _default_client_factory(**kwargs: Any) -> ClientLike:
    from originalpictures import Client

    return Client(**kwargs)


def invoke(runtime: Runtime, operation: Callable[[], Any]) -> Any:
    try:
        return operation()
    except (KeyboardInterrupt, click.Abort):
        fail(runtime, Failure(ExitCode.CANCELLED, "cancelled", "operation cancelled"))
    except Exception as error:
        fail(runtime, classify_exception(error))
    raise AssertionError("unreachable")


def fail(runtime: Runtime, failure: Failure) -> None:
    runtime.output.error(
        code=int(failure.exit_code),
        kind=failure.kind,
        message=failure.message,
        details=failure.details,
        known_secrets=runtime.known_secrets,
    )
    raise click.exceptions.Exit(int(failure.exit_code))


def classify_exception(error: Exception) -> Failure:
    if isinstance(error, ConfigurationFailure):
        return Failure(ExitCode.CONFIGURATION, "configuration", str(error))

    try:
        from originalpictures import errors as sdk_errors
    except ImportError:
        return Failure(
            ExitCode.CONFIGURATION,
            "configuration",
            "originalpictures-sdk is not installed correctly",
        )

    validation_error = getattr(sdk_errors, "RequestValidationError", None)
    mappings: tuple[tuple[type[Exception], ExitCode, str], ...] = (
        (sdk_errors.AuthenticationError, ExitCode.AUTHENTICATION, "authentication"),
        (sdk_errors.PermissionDeniedError, ExitCode.PERMISSION, "permission_denied"),
        (sdk_errors.NotFoundError, ExitCode.NOT_FOUND, "not_found"),
        (sdk_errors.ConflictError, ExitCode.CONFLICT, "conflict"),
        (sdk_errors.RateLimitError, ExitCode.RATE_LIMIT, "rate_limited"),
        (sdk_errors.DeadlineExceededError, ExitCode.DEADLINE, "deadline_exceeded"),
        (sdk_errors.CancelledError, ExitCode.CANCELLED, "cancelled"),
        (sdk_errors.ServiceUnavailableError, ExitCode.UNAVAILABLE, "service_unavailable"),
        (sdk_errors.TransportError, ExitCode.UNAVAILABLE, "transport"),
        (sdk_errors.IntegrityError, ExitCode.INTEGRITY, "integrity"),
        (sdk_errors.ResponseTooLargeError, ExitCode.TOO_LARGE, "response_too_large"),
        (sdk_errors.ConfigurationError, ExitCode.CONFIGURATION, "configuration"),
    )
    if isinstance(validation_error, type) and isinstance(error, validation_error):
        return Failure(ExitCode.VALIDATION, "validation", str(error), _api_details(error))
    for error_type, code, kind in mappings:
        if isinstance(error, error_type):
            return Failure(code, kind, str(error), _api_details(error))
    if isinstance(error, sdk_errors.ApiError):
        code, kind = _status_fallback(error.status_code)
        return Failure(code, kind, str(error), _api_details(error))
    if isinstance(error, (ValueError, TypeError)):
        return Failure(ExitCode.VALIDATION, "validation", str(error))
    return Failure(ExitCode.UNEXPECTED, "unexpected", "unexpected local failure")


def _api_details(error: Exception) -> dict[str, Any] | None:
    details: dict[str, Any] = {}
    for key in ("status_code", "code", "request_id"):
        value = getattr(error, key, None)
        if value is not None:
            details[key] = value
    return details or None


def _status_fallback(status_code: int) -> tuple[ExitCode, str]:
    return {
        400: (ExitCode.VALIDATION, "validation"),
        401: (ExitCode.AUTHENTICATION, "authentication"),
        403: (ExitCode.PERMISSION, "permission_denied"),
        404: (ExitCode.NOT_FOUND, "not_found"),
        409: (ExitCode.CONFLICT, "conflict"),
        422: (ExitCode.VALIDATION, "validation"),
        429: (ExitCode.RATE_LIMIT, "rate_limited"),
        503: (ExitCode.UNAVAILABLE, "service_unavailable"),
    }.get(status_code, (ExitCode.UNEXPECTED, "api_error"))


__all__ = ["Failure", "Runtime", "classify_exception", "fail", "invoke"]
