"""Verification helpers for exact Original Pictures customer webhook bodies."""

from __future__ import annotations

import base64
import binascii
import hashlib
import hmac
import time

from originalpictures.errors import RequestValidationError

MAX_WEBHOOK_BYTES = 256 * 1024


def verify_webhook(
    body: bytes,
    *,
    secret: bytes | str,
    event_id: str,
    timestamp: int | str,
    signature: str,
    tolerance_seconds: int = 300,
    now: int | None = None,
) -> None:
    """Verify a Standard Webhooks signature or the legacy compatibility form.

    ``signature`` may contain multiple space-delimited ``v1,<base64>`` values
    during zero-downtime secret rotation. The body must be the exact raw request
    bytes; parsing and reserializing JSON before this call invalidates the HMAC.
    """

    if len(body) > MAX_WEBHOOK_BYTES:
        raise RequestValidationError("webhook body exceeds 256 KiB", status_code=413)
    try:
        timestamp_int = int(timestamp)
    except (TypeError, ValueError) as error:
        raise RequestValidationError("invalid webhook timestamp", status_code=400) from error
    if not event_id or tolerance_seconds < 0:
        raise RequestValidationError("invalid webhook signature inputs", status_code=400)
    current = int(time.time()) if now is None else now
    if abs(current - timestamp_int) > tolerance_seconds:
        raise RequestValidationError(
            "webhook timestamp is outside the allowed tolerance", status_code=400
        )
    rendered_key = secret.encode("utf-8") if isinstance(secret, str) else secret
    if len(rendered_key) < 32:
        raise RequestValidationError("webhook secret is invalid", status_code=400)
    try:
        encoded_event_id = event_id.encode("ascii")
    except UnicodeEncodeError as error:
        raise RequestValidationError("webhook event ID is invalid", status_code=400) from error
    legacy_message = b".".join((str(timestamp_int).encode("ascii"), encoded_event_id, body))
    legacy_expected = "v1=" + hmac.new(rendered_key, legacy_message, hashlib.sha256).hexdigest()

    standard_key: bytes | None = None
    if rendered_key.startswith(b"whsec_"):
        encoded = rendered_key.removeprefix(b"whsec_")
        try:
            standard_key = base64.b64decode(encoded, validate=True)
        except (binascii.Error, ValueError):
            try:
                standard_key = base64.urlsafe_b64decode(encoded + b"=" * (-len(encoded) % 4))
            except (binascii.Error, ValueError):
                standard_key = None
    elif 24 <= len(rendered_key) <= 64:
        standard_key = rendered_key
    standard_expected: str | None = None
    if standard_key is not None and 24 <= len(standard_key) <= 64 and b"." not in encoded_event_id:
        standard_message = b".".join((encoded_event_id, str(timestamp_int).encode("ascii"), body))
        digest = hmac.new(standard_key, standard_message, hashlib.sha256).digest()
        standard_expected = "v1," + base64.b64encode(digest).decode("ascii")

    valid = False
    for candidate in signature.split():
        if candidate.startswith("v1,") and standard_expected is not None:
            valid |= hmac.compare_digest(standard_expected, candidate)
        elif candidate.startswith("v1="):
            valid |= hmac.compare_digest(legacy_expected, candidate)
    if not valid:
        raise RequestValidationError("webhook signature is invalid", status_code=400)


__all__ = ["MAX_WEBHOOK_BYTES", "verify_webhook"]
