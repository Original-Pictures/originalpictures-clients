"""AI disclosure policy resolution and evidence logging (Python mirror).

The rule text is a draft for owner and legal review (``needs_legal_review`` on
every rule). Showing a notice does not by itself satisfy any law.
"""

from originalpictures_disclosure.events import (
    DEFAULT_API_BASE,
    EVENT_KINDS,
    REFERENCE_PATTERN,
    DisclosureEventError,
    DisclosureEventLogger,
    DisclosureEventReceipt,
    EventKind,
    Surface,
    build_event_payload,
)
from originalpictures_disclosure.policy import (
    JURISDICTION_IDS,
    POLICY_SCHEMA,
    DetectionBasis,
    JurisdictionId,
    ResolvedDisclosure,
    RuleKind,
    detect_jurisdiction,
    load_policy,
    parse_accept_language,
    pick_text,
    resolve,
    resolve_all,
)

__all__ = [
    "DEFAULT_API_BASE",
    "EVENT_KINDS",
    "JURISDICTION_IDS",
    "POLICY_SCHEMA",
    "REFERENCE_PATTERN",
    "DetectionBasis",
    "DisclosureEventError",
    "DisclosureEventLogger",
    "DisclosureEventReceipt",
    "EventKind",
    "JurisdictionId",
    "ResolvedDisclosure",
    "RuleKind",
    "Surface",
    "build_event_payload",
    "detect_jurisdiction",
    "load_policy",
    "parse_accept_language",
    "pick_text",
    "resolve",
    "resolve_all",
]
