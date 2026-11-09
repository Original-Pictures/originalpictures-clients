"""Typed Python SDK for the Original Pictures public API."""

from originalpictures._generated.public_api import *  # noqa: F403
from originalpictures._generated.public_api import PUBLIC_API_OPERATIONS as _PUBLIC_API_OPERATIONS
from originalpictures._generated.public_api import __all__ as _generated_all
from originalpictures.client import (
    DEFAULT_MAX_RESPONSE_BYTES,
    DEFAULT_MAX_TRANSFER_BYTES,
    DEFAULT_TRANSFER_CHUNK_BYTES,
    MAX_PUBLIC_CHECK_BYTES,
    MAX_TRANSFER_CHUNK_BYTES,
    AsyncClient,
    Client,
)
from originalpictures.errors import *  # noqa: F403
from originalpictures.errors import __all__ as _error_all
from originalpictures.helpers import (
    MAX_SYNC_POLL_WORKERS,
    idempotency_key,
    poll,
    poll_async,
    sign_job_terminal,
    validate_idempotency_key,
    verification_job_terminal,
)
from originalpictures.public_checks import (
    DEFAULT_PUBLIC_API_BASE,
    PUBLIC_CHECK_MAX_BYTES,
    fetch_verify_page,
    verify_public,
    verify_public_async,
)
from originalpictures.webhooks import MAX_WEBHOOK_BYTES, verify_webhook

SDK_STATUS = "complete"
SDK_TYPED_OPERATION_COUNT = len(_PUBLIC_API_OPERATIONS)
SDK_EXECUTABLE_OPERATION_COUNT = sum(operation.executable for operation in _PUBLIC_API_OPERATIONS)

__all__ = [
    *_generated_all,
    *_error_all,
    "AsyncClient",
    "Client",
    "DEFAULT_MAX_RESPONSE_BYTES",
    "DEFAULT_PUBLIC_API_BASE",
    "DEFAULT_MAX_TRANSFER_BYTES",
    "DEFAULT_TRANSFER_CHUNK_BYTES",
    "MAX_WEBHOOK_BYTES",
    "MAX_PUBLIC_CHECK_BYTES",
    "MAX_TRANSFER_CHUNK_BYTES",
    "MAX_SYNC_POLL_WORKERS",
    "PUBLIC_CHECK_MAX_BYTES",
    "SDK_STATUS",
    "SDK_EXECUTABLE_OPERATION_COUNT",
    "SDK_TYPED_OPERATION_COUNT",
    "idempotency_key",
    "poll",
    "poll_async",
    "sign_job_terminal",
    "validate_idempotency_key",
    "fetch_verify_page",
    "verification_job_terminal",
    "verify_public",
    "verify_public_async",
    "verify_webhook",
]
