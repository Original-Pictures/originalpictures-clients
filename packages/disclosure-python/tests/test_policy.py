"""Policy resolution: the shared vectors, and the bundled copy stays the domain source."""

from __future__ import annotations

import json
from importlib import resources
from pathlib import Path
from typing import Any

import pytest

from originalpictures_disclosure import (
    JURISDICTION_IDS,
    detect_jurisdiction,
    load_policy,
    parse_accept_language,
    resolve,
    resolve_all,
)

_REPO = Path(__file__).resolve().parents[3]
_VECTORS = _REPO / "packages/disclosure/tests/fixtures/resolution-vectors.json"
_DOMAIN_SOURCE = (
    _REPO / "packages/domain/src/op_domain/resources/disclosure-policy"
) / "op.disclosure-policy.2026-10.v1.json"
_vectors: list[dict[str, Any]] = (
    json.loads(_VECTORS.read_text(encoding="utf-8"))["vectors"] if _VECTORS.exists() else []
)


@pytest.mark.skipif(not _VECTORS.exists(), reason="shared vectors live in the monorepo")
@pytest.mark.parametrize("vector", _vectors, ids=[v["name"] for v in _vectors])
def test_shared_resolution_vectors(vector: dict[str, Any]) -> None:
    resolved = resolve(**vector["options"])
    if vector["expect"] is None:
        assert resolved is None
        return
    assert resolved is not None
    actual = {
        "jurisdiction": resolved.jurisdiction,
        "basis": resolved.detected_by,
        "rule_id": resolved.rule_id,
        "locale": resolved.locale,
        "text": resolved.text,
        "timing": resolved.timing,
        "badge_set": resolved.badge_set,
    }
    for key, value in vector["expect"].items():
        assert actual[key] == value, key
    assert resolved.needs_legal_review is True


@pytest.mark.skipif(not _DOMAIN_SOURCE.exists(), reason="the domain source lives in the monorepo")
def test_bundled_policy_is_the_domain_source_byte_for_byte() -> None:
    bundled = (
        resources.files("originalpictures_disclosure")
        .joinpath("resources", "op.disclosure-policy.2026-10.v1.json")
        .read_bytes()
    )
    assert bundled == _DOMAIN_SOURCE.read_bytes()


def test_bundled_policy_covers_the_nine_jurisdictions() -> None:
    policy = load_policy()
    assert [j["id"] for j in policy["jurisdictions"]] == list(JURISDICTION_IDS)
    assert all(rule["needs_legal_review"] for j in policy["jurisdictions"] for rule in j["rules"])


def test_every_rule_resolves_by_id() -> None:
    for jurisdiction in load_policy()["jurisdictions"]:
        for rule in jurisdiction["rules"]:
            resolved = resolve(jurisdiction=jurisdiction["id"], rule_id=rule["id"])
            assert resolved is not None and resolved.rule_id == rule["id"]
            assert resolved.instrument["citation"]


def test_lists_all_rules_of_a_kind() -> None:
    ids = [r.rule_id for r in resolve_all(jurisdiction="CN", kind="visible_label")]
    assert ids == ["cn.labeling.explicit-label", "cn.labeling.platform-label"]


def test_hints() -> None:
    assert parse_accept_language("da, en-GB;q=0.8, en;q=0.7, *;q=0.5, fr;q=0") == [
        "da",
        "en-GB",
        "en",
    ]
    assert detect_jurisdiction(time_zone="America/Los_Angeles") is None
    assert detect_jurisdiction(accept_language="zh") is None
    assert detect_jurisdiction(region="de") == ("EU", "region")


def test_unknown_explicit_jurisdiction_is_refused() -> None:
    with pytest.raises(ValueError, match="unknown jurisdiction"):
        resolve(jurisdiction="US-TX")
