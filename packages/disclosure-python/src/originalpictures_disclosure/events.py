"""Log disclosure evidence to ``POST /v1/disclosures/events``.

Use a publishable key (``POST /v1/api-keys`` with ``preset: publishable_disclosure``,
scope ``disclosure:write`` only) or any key holding that scope. The server appends
each event to the account's hash-chained, tamper-evident log; the log is not signed.
"""

from __future__ import annotations

import datetime as dt
import re
import time
import uuid
from dataclasses import dataclass
from typing import Any, Final, Literal

import httpx

from originalpictures_disclosure.policy import JURISDICTION_IDS, ResolvedDisclosure

DEFAULT_API_BASE: Final = "https://dev-api.originalpictures.com"
EventKind = Literal[
    "ai_interaction_notice", "visible_label_offered", "visible_label_applied", "user_acknowledged"
]
Surface = Literal["web", "app", "voice", "api", "other"]
EVENT_KINDS: Final = frozenset(
    {"ai_interaction_notice", "visible_label_offered", "visible_label_applied", "user_acknowledged"}
)
SURFACES: Final = frozenset({"web", "app", "voice", "api", "other"})
#: op_domain.disclosures.DISCLOSURE_REFERENCE_PATTERN: opaque, never an email or a name.
REFERENCE_PATTERN: Final = re.compile(r"^[A-Za-z0-9._:~-]{1,128}$")
_POLICY_VERSION: Final = re.compile(r"^\d{4}-\d{2}-\d{2}\.\d{1,3}$")
_RULE_ID: Final = re.compile(r"^[a-z0-9]+(?:[._-][a-z0-9]+)*$")
_LOCALE: Final = re.compile(r"^[A-Za-z]{2,3}(?:-[A-Za-z0-9]{2,8})*$")
_LOOPBACK: Final = frozenset({"localhost", "127.0.0.1", "::1"})


class DisclosureEventError(Exception):
    """An event was refused locally or by the API."""

    def __init__(self, code: str, message: str, status_code: int | None = None) -> None:
        super().__init__(message)
        self.code = code
        self.status_code = status_code


@dataclass(frozen=True, slots=True)
class DisclosureEventReceipt:
    event_id: str
    sequence: int
    prev_hash: str
    hash: str
    received_at: str


def build_event_payload(
    *,
    kind: str,
    jurisdiction: str,
    policy_version: str,
    subject_ref: str,
    rule_id: str | None = None,
    content_ref: str | None = None,
    locale: str | None = None,
    surface: str | None = None,
    client_time: dt.datetime | None = None,
) -> dict[str, Any]:
    """Validate one event and return the exact DisclosureEventRequest body."""

    def invalid(message: str) -> DisclosureEventError:
        return DisclosureEventError("DISCLOSURE_INVALID", message)

    if kind not in EVENT_KINDS:
        raise invalid("unknown event kind")
    if jurisdiction not in JURISDICTION_IDS:
        raise invalid("unknown jurisdiction")
    if not _POLICY_VERSION.fullmatch(policy_version):
        raise invalid("malformed policy version")
    if rule_id is not None and (len(rule_id) > 96 or not _RULE_ID.fullmatch(rule_id)):
        raise invalid("malformed rule id")
    if not REFERENCE_PATTERN.fullmatch(subject_ref):
        raise invalid("subject_ref must be an opaque reference (letters, digits and ._:~-)")
    if content_ref is not None and not REFERENCE_PATTERN.fullmatch(content_ref):
        raise invalid("content_ref must be an opaque reference (letters, digits and ._:~-)")
    if locale is not None and not _LOCALE.fullmatch(locale):
        raise invalid("malformed locale")
    if surface is not None and surface not in SURFACES:
        raise invalid("unknown surface")
    moment = client_time or dt.datetime.now(dt.UTC)
    if moment.tzinfo is None:
        raise invalid("client_time must be timezone-aware")
    utc = moment.astimezone(dt.UTC)
    return {
        "kind": kind,
        "jurisdiction": jurisdiction,
        "policy_version": policy_version,
        "rule_id": rule_id,
        "subject_ref": subject_ref,
        "content_ref": content_ref,
        "client_time": utc.strftime("%Y-%m-%dT%H:%M:%S.") + f"{utc.microsecond // 1000:03d}Z",
        "surface": surface,
        "locale": locale,
    }


class DisclosureEventLogger:
    """Sends disclosure events; one retry with the same Idempotency-Key on 5xx or network error."""

    def __init__(
        self,
        api_key: str,
        *,
        api_base: str = DEFAULT_API_BASE,
        timeout: float = 10.0,
        retry_delay: float = 1.0,
        http_client: httpx.Client | None = None,
    ) -> None:
        if not api_key.startswith("opk_"):
            raise DisclosureEventError("DISCLOSURE_INVALID", "an opk_ API key is required")
        base = httpx.URL(api_base)
        if base.scheme != "https" and not (base.scheme == "http" and base.host in _LOOPBACK):
            raise DisclosureEventError("DISCLOSURE_INVALID", "the API base must use https")
        self._key = api_key
        self._url = f"{str(base).rstrip('/')}/v1/disclosures/events"
        self._retry_delay = retry_delay
        self._owns_client = http_client is None
        self._client = http_client or httpx.Client(timeout=timeout)

    def __enter__(self) -> DisclosureEventLogger:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def close(self) -> None:
        if self._owns_client:
            self._client.close()

    def log(self, **event: Any) -> DisclosureEventReceipt:
        """Record one event (the keyword arguments of :func:`build_event_payload`)."""

        body = build_event_payload(**event)
        headers = {
            "Authorization": f"Bearer {self._key}",
            "Accept": "application/json",
            "Idempotency-Key": f"dse-{uuid.uuid4()}",
        }
        for attempt in (0, 1):
            try:
                response = self._client.post(self._url, json=body, headers=headers)
            except httpx.HTTPError as error:
                if attempt == 0:
                    time.sleep(self._retry_delay)
                    continue
                raise DisclosureEventError(
                    "NETWORK_ERROR", "the disclosure log could not be reached"
                ) from error
            if response.status_code >= 500 and attempt == 0:
                time.sleep(self._retry_delay)
                continue
            payload: Any
            try:
                payload = response.json()
            except ValueError:
                payload = None
            if response.status_code == 201 and isinstance(payload, dict):
                return DisclosureEventReceipt(
                    event_id=payload["event_id"],
                    sequence=payload["sequence"],
                    prev_hash=payload["prev_hash"],
                    hash=payload["hash"],
                    received_at=payload["received_at"],
                )
            code = payload.get("code") if isinstance(payload, dict) else None
            raise DisclosureEventError(
                code if isinstance(code, str) else f"HTTP_{response.status_code}",
                "the event was not recorded",
                response.status_code,
            )
        raise AssertionError("unreachable")  # pragma: no cover

    def log_resolved(
        self,
        resolved: ResolvedDisclosure,
        kind: EventKind,
        *,
        subject_ref: str,
        content_ref: str | None = None,
        surface: Surface = "app",
    ) -> DisclosureEventReceipt:
        """Record that a resolved disclosure was shown, offered, applied or acknowledged."""

        return self.log(
            kind=kind,
            jurisdiction=resolved.jurisdiction,
            policy_version=resolved.policy_version,
            rule_id=resolved.rule_id,
            subject_ref=subject_ref,
            content_ref=content_ref,
            locale=resolved.locale,
            surface=surface,
        )


__all__ = [
    "DEFAULT_API_BASE",
    "EVENT_KINDS",
    "REFERENCE_PATTERN",
    "DisclosureEventError",
    "DisclosureEventLogger",
    "DisclosureEventReceipt",
    "EventKind",
    "Surface",
    "build_event_payload",
]
