"""Stable, secret-safe Original Pictures SDK errors."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any


class OriginalPicturesError(Exception):
    """Base error for every SDK failure."""


class ConfigurationError(OriginalPicturesError):
    """The client configuration is invalid or incomplete."""


class TransportError(OriginalPicturesError):
    """The API could not be reached safely."""


class DeadlineExceededError(TransportError):
    """A request or bounded polling operation exceeded its deadline."""


class CancelledError(OriginalPicturesError):
    """A bounded local SDK operation was cancelled."""


class PollingCapacityError(OriginalPicturesError):
    """No bounded synchronous polling worker is currently available."""


class IntegrityError(OriginalPicturesError):
    """Transferred bytes did not match authenticated integrity facts."""


class ResponseTooLargeError(OriginalPicturesError):
    """A response exceeded its configured byte bound."""


class ApiError(OriginalPicturesError):
    """A stable, typed non-success response from the public API."""

    def __init__(
        self,
        message: str,
        *,
        status_code: int,
        code: str | None = None,
        request_id: str | None = None,
        retryable: bool | None = None,
        field_details: Mapping[str, str] | None = None,
        documentation_url: str | None = None,
        job_reference: str | None = None,
        validation_errors: Sequence[Mapping[str, Any]] | None = None,
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.code = code
        self.request_id = request_id
        self.retryable = retryable
        self.field_details = dict(field_details or {})
        self.documentation_url = documentation_url
        self.job_reference = job_reference
        self.validation_errors = tuple(dict(item) for item in (validation_errors or ()))
        self.details = details or {}


class AuthenticationError(ApiError):
    """The API credential is absent or invalid."""


class PermissionDeniedError(ApiError):
    """The credential lacks the required scope or authority."""


class NotFoundError(ApiError):
    """The requested public resource does not exist."""


class ConflictError(ApiError):
    """The request conflicts with current state or idempotency history."""


class RequestValidationError(ApiError):
    """The public API rejected request validation."""


class RateLimitError(ApiError):
    """The public API rate limit was exceeded."""


class ServiceUnavailableError(ApiError):
    """The public API is temporarily unavailable."""


__all__ = [
    "ApiError",
    "AuthenticationError",
    "CancelledError",
    "ConfigurationError",
    "ConflictError",
    "DeadlineExceededError",
    "IntegrityError",
    "NotFoundError",
    "OriginalPicturesError",
    "PermissionDeniedError",
    "PollingCapacityError",
    "RateLimitError",
    "ResponseTooLargeError",
    "ServiceUnavailableError",
    "TransportError",
    "RequestValidationError",
]
