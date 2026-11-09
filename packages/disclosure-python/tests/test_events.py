"""Event payloads and the logger, against a mocked API."""

from __future__ import annotations

import datetime as dt
import json

import httpx
import pytest

import originalpictures_disclosure.events as events
from originalpictures_disclosure import (
    DisclosureEventError,
    DisclosureEventLogger,
    build_event_payload,
    resolve,
)

KEY = "opk_AbCdEfGhIjKl.secret-part_123"
RECEIPT = {
    "event_id": "dse_abcdefghijklmnop",
    "sequence": 3,
    "prev_hash": "sha256:" + "a1" * 32,
    "hash": "sha256:" + "3f" * 32,
    "received_at": "2026-10-19T09:30:00.412345Z",
}
EVENT = {
    "kind": "ai_interaction_notice",
    "jurisdiction": "EU",
    "policy_version": "2026-10-19.1",
    "rule_id": "eu.art50.1.ai-interaction",
    "subject_ref": "visitor:7f3c2a91",
    "locale": "de-DE",
    "surface": "app",
    "client_time": dt.datetime(2026, 10, 19, 9, 30, 0, 120000, tzinfo=dt.UTC),
}


def test_payload_is_exactly_the_request_body() -> None:
    assert build_event_payload(**EVENT) == {
        "kind": "ai_interaction_notice",
        "jurisdiction": "EU",
        "policy_version": "2026-10-19.1",
        "rule_id": "eu.art50.1.ai-interaction",
        "subject_ref": "visitor:7f3c2a91",
        "content_ref": None,
        "client_time": "2026-10-19T09:30:00.120Z",
        "surface": "app",
        "locale": "de-DE",
    }


@pytest.mark.parametrize(
    "patch",
    [
        {"subject_ref": "person@example.com"},
        {"jurisdiction": "US-TX"},
        {"policy_version": "v1"},
        {"kind": "label_removed"},
        {"rule_id": "EU Art 50"},
        {"client_time": dt.datetime(2026, 10, 19, 9, 30)},  # noqa: DTZ001
    ],
)
def test_refuses_invalid_events(patch: dict[str, object]) -> None:
    with pytest.raises(DisclosureEventError) as caught:
        build_event_payload(**{**EVENT, **patch})  # type: ignore[arg-type]
    assert caught.value.code == "DISCLOSURE_INVALID"


def test_logs_with_bearer_key_and_idempotency_key() -> None:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(201, json=RECEIPT)

    client = httpx.Client(transport=httpx.MockTransport(handler))
    with DisclosureEventLogger(KEY, http_client=client) as logger:
        resolved = resolve(jurisdiction="KR", locale="ko")
        assert resolved is not None
        receipt = logger.log_resolved(resolved, "user_acknowledged", subject_ref="user:42")
    assert receipt.event_id == "dse_abcdefghijklmnop"
    request = seen[0]
    assert str(request.url) == "https://dev-api.originalpictures.com/v1/disclosures/events"
    assert request.headers["authorization"] == f"Bearer {KEY}"
    assert request.headers["idempotency-key"].startswith("dse-")
    body = json.loads(request.content)
    assert body["kind"] == "user_acknowledged"
    assert body["jurisdiction"] == "KR"
    assert body["rule_id"] == "kr.art31.1.advance-notice"
    assert body["locale"] == "ko"


def test_retries_a_5xx_once_with_the_same_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(events.time, "sleep", lambda _: None)
    answers = [httpx.Response(503, json={"code": "X"}), httpx.Response(201, json=RECEIPT)]
    keys: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        keys.append(request.headers["idempotency-key"])
        return answers.pop(0)

    logger = DisclosureEventLogger(
        KEY, http_client=httpx.Client(transport=httpx.MockTransport(handler))
    )
    assert logger.log(**EVENT).sequence == 3
    assert len(keys) == 2 and keys[0] == keys[1]


def test_surfaces_the_api_reason_code() -> None:
    handler = httpx.MockTransport(
        lambda _: httpx.Response(422, json={"code": "DISCLOSURE_INVALID", "message": "bad"})
    )
    logger = DisclosureEventLogger(KEY, http_client=httpx.Client(transport=handler))
    with pytest.raises(DisclosureEventError) as caught:
        logger.log(**EVENT)
    assert (caught.value.code, caught.value.status_code) == ("DISCLOSURE_INVALID", 422)


def test_refuses_non_opk_keys_and_plain_http() -> None:
    with pytest.raises(DisclosureEventError):
        DisclosureEventLogger("sk_live_123")
    with pytest.raises(DisclosureEventError):
        DisclosureEventLogger(KEY, api_base="http://api.example")
    DisclosureEventLogger(KEY, api_base="http://127.0.0.1:3122").close()
