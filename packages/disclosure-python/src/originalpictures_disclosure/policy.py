"""Resolve the disclosure rule, text, form and timing for a jurisdiction.

Mirrors ``resolve()`` in ``@originalpictures/disclosure``; both engines run the
same resolution vectors. The bundled document is op.disclosure-policy.2026-10.v1,
drafted from the statutes and flagged ``needs_legal_review`` on every rule:
resolving a rule says what to show, not that showing it satisfies a law.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from functools import cache
from importlib import resources
from typing import Any, Final, Literal

JurisdictionId = Literal["EU", "US-CA", "US-ME", "US-NH", "US-NY", "US-UT", "IN", "CN", "KR"]
RuleKind = Literal[
    "ai_interaction_notice", "visible_label", "deepfake_label", "machine_readable_marking"
]
DetectionBasis = Literal["explicit", "region", "timezone", "language", "fallback"]

POLICY_SCHEMA: Final = "op.disclosure-policy.2026-10.v1"
POLICY_RESOURCE: Final = "op.disclosure-policy.2026-10.v1.json"
JURISDICTION_IDS: Final[tuple[str, ...]] = (
    "EU",
    "US-CA",
    "US-ME",
    "US-NH",
    "US-NY",
    "US-UT",
    "IN",
    "CN",
    "KR",
)

_EU_MEMBER_STATES: Final = frozenset(
    [
        "AT",
        "BE",
        "BG",
        "HR",
        "CY",
        "CZ",
        "DK",
        "EE",
        "FI",
        "FR",
        "DE",
        "GR",
        "EL",
        "HU",
        "IE",
        "IT",
        "LV",
        "LT",
        "LU",
        "MT",
        "NL",
        "PL",
        "PT",
        "RO",
        "SK",
        "SI",
        "ES",
        "SE",
    ]
)
# Zones wholly inside one covered jurisdiction. A US zone spans many states, so
# none maps to a state: pass ``region`` from server geolocation instead.
_EU_ZONES: Final = [
    "Europe/Vienna",
    "Europe/Brussels",
    "Europe/Sofia",
    "Europe/Zagreb",
    "Asia/Nicosia",
    "Asia/Famagusta",
    "Europe/Nicosia",
    "Europe/Prague",
    "Europe/Copenhagen",
    "Europe/Tallinn",
    "Europe/Helsinki",
    "Europe/Mariehamn",
    "Europe/Paris",
    "Europe/Berlin",
    "Europe/Busingen",
    "Europe/Athens",
    "Europe/Budapest",
    "Europe/Dublin",
    "Europe/Rome",
    "Europe/Riga",
    "Europe/Vilnius",
    "Europe/Luxembourg",
    "Europe/Malta",
    "Europe/Amsterdam",
    "Europe/Warsaw",
    "Europe/Lisbon",
    "Atlantic/Madeira",
    "Atlantic/Azores",
    "Europe/Bucharest",
    "Europe/Bratislava",
    "Europe/Ljubljana",
    "Europe/Madrid",
    "Africa/Ceuta",
    "Atlantic/Canary",
    "Europe/Stockholm",
    "America/Guadeloupe",
    "America/Martinique",
    "America/Cayenne",
    "Indian/Reunion",
    "Indian/Mayotte",
]
_ZONE_JURISDICTIONS: Final[dict[str, str]] = {
    **dict.fromkeys(_EU_ZONES, "EU"),
    **dict.fromkeys(
        (
            "Asia/Shanghai",
            "Asia/Urumqi",
            "Asia/Chongqing",
            "Asia/Chungking",
            "Asia/Harbin",
            "Asia/Kashgar",
            "PRC",
        ),
        "CN",
    ),
    "Asia/Seoul": "KR",
    "ROK": "KR",
    "Asia/Kolkata": "IN",
    "Asia/Calcutta": "IN",
}
_COUNTRY_JURISDICTIONS: Final = {"CN": "CN", "KR": "KR", "IN": "IN"}
# A bare language is a weak hint: only languages spoken (almost) only there.
_LANGUAGE_JURISDICTIONS: Final = {"ko": "KR", "hi": "IN"}


@dataclass(frozen=True, slots=True)
class ResolvedDisclosure:
    policy_version: str
    jurisdiction: str
    jurisdiction_name: str
    detected_by: DetectionBasis
    rule_id: str
    kind: str
    provision: str
    obligated_party: str
    trigger: str
    exceptions: tuple[str, ...]
    instrument: dict[str, Any]
    #: The draft text to show, or None for machine-readable marking.
    text: str | None
    locale: str | None
    form: str
    timing: str
    badge_set: str | None
    #: True until the owner's legal review clears the text.
    needs_legal_review: bool
    disclaimer: str


@cache
def _bundled_text() -> str:
    path = resources.files("originalpictures_disclosure").joinpath("resources", POLICY_RESOURCE)
    return path.read_text(encoding="utf-8")


def load_policy() -> dict[str, Any]:
    """A fresh copy of the bundled policy document."""

    document = json.loads(_bundled_text())
    if not isinstance(document, dict) or document.get("schema_version") != POLICY_SCHEMA:
        raise ValueError("the bundled disclosure policy has an unexpected schema")
    return document


def parse_accept_language(header: str | None) -> list[str]:
    """Language tags from an Accept-Language value, most preferred first."""

    if not header:
        return []
    entries: list[tuple[float, int, str]] = []
    for index, part in enumerate(header.split(",")):
        tag, *params = (piece.strip() for piece in part.strip().split(";"))
        weight = 1.0
        for param in params:
            if param.startswith("q="):
                try:
                    weight = float(param[2:])
                except ValueError:
                    weight = 0.0
        if tag and tag != "*" and weight > 0:
            entries.append((-weight, index, tag))
    return [tag for _, _, tag in sorted(entries)]


def _from_region(region: str) -> str | None:
    code = region.strip().upper()
    if code in JURISDICTION_IDS:
        return code
    country = code.split("-")[0]
    if country in _EU_MEMBER_STATES:
        return "EU"
    return _COUNTRY_JURISDICTIONS.get(country)


def _from_language_tag(tag: str) -> str | None:
    subtags = tag.split("-")
    region = next((part for part in subtags[1:] if len(part) == 2 and part.isalpha()), None)
    if region:
        return _from_region(region)
    return _LANGUAGE_JURISDICTIONS.get(subtags[0].lower())


def detect_jurisdiction(
    *, region: str | None = None, time_zone: str | None = None, accept_language: str | None = None
) -> tuple[str, DetectionBasis] | None:
    """Best-effort jurisdiction from hints: region, then time zone, then language."""

    if region and (found := _from_region(region)):
        return found, "region"
    if time_zone and (found := _ZONE_JURISDICTIONS.get(time_zone)):
        return found, "timezone"
    for tag in parse_accept_language(accept_language):
        if found := _from_language_tag(tag):
            return found, "language"
    return None


def pick_text(texts: list[dict[str, str]], preferences: list[str]) -> dict[str, str] | None:
    """The text whose locale best matches the preferences; then English; then the first."""

    if not texts:
        return None
    for preference in preferences:
        wanted = preference.lower()
        for text in texts:
            if text["locale"].lower() == wanted:
                return text
        language = wanted.split("-")[0]
        for text in texts:
            if text["locale"].lower().split("-")[0] == language:
                return text
    return next((text for text in texts if text["locale"] == "en"), texts[0])


_UNSET: Final = object()


def resolve_all(
    *,
    jurisdiction: str = "auto",
    kind: RuleKind = "ai_interaction_notice",
    rule_id: str | None = None,
    locale: str | None = None,
    region: str | None = None,
    time_zone: str | None = None,
    accept_language: str | None = None,
    fallback: str | None | object = _UNSET,
    policy: dict[str, Any] | None = None,
) -> list[ResolvedDisclosure]:
    """Every rule of ``kind`` (or the rule ``rule_id``) in the chosen jurisdiction."""

    document = policy if policy is not None else load_policy()
    chosen: tuple[str, DetectionBasis] | None
    if jurisdiction != "auto":
        if jurisdiction not in JURISDICTION_IDS:
            raise ValueError(f"unknown jurisdiction {jurisdiction}")
        chosen = (jurisdiction, "explicit")
    else:
        chosen = detect_jurisdiction(
            region=region, time_zone=time_zone, accept_language=accept_language
        )
        if chosen is None:
            fallback_id = "EU" if fallback is _UNSET else fallback
            chosen = (str(fallback_id), "fallback") if fallback_id else None
    if chosen is None:
        return []
    entry = next((j for j in document["jurisdictions"] if j["id"] == chosen[0]), None)
    if entry is None:
        return []
    preferences = ([locale] if locale else []) + parse_accept_language(accept_language)
    rules = [
        rule
        for rule in entry["rules"]
        if (rule["id"] == rule_id if rule_id else rule["kind"] == kind)
    ]
    resolved: list[ResolvedDisclosure] = []
    for rule in rules:
        instrument = next(i for i in entry["instruments"] if i["id"] == rule["instrument"])
        text = pick_text(rule["texts"], preferences)
        resolved.append(
            ResolvedDisclosure(
                policy_version=document["policy_version"],
                jurisdiction=entry["id"],
                jurisdiction_name=entry["name"],
                detected_by=chosen[1],
                rule_id=rule["id"],
                kind=rule["kind"],
                provision=rule["provision"],
                obligated_party=rule["obligated_party"],
                trigger=rule["trigger"],
                exceptions=tuple(rule["exceptions"]),
                instrument=dict(instrument),
                text=text["text"] if text else None,
                locale=text["locale"] if text else None,
                form=rule["form"],
                timing=rule["timing"],
                badge_set=rule["badge_set"],
                needs_legal_review=bool(
                    rule["needs_legal_review"] or document["needs_legal_review"]
                ),
                disclaimer=document["disclaimer"],
            )
        )
    return resolved


def resolve(**options: Any) -> ResolvedDisclosure | None:
    """The first matching rule (see :func:`resolve_all`), or None when there is none."""

    found = resolve_all(**options)
    return found[0] if found else None


__all__ = [
    "JURISDICTION_IDS",
    "POLICY_SCHEMA",
    "DetectionBasis",
    "JurisdictionId",
    "ResolvedDisclosure",
    "RuleKind",
    "detect_jurisdiction",
    "load_policy",
    "parse_accept_language",
    "pick_text",
    "resolve",
    "resolve_all",
]
