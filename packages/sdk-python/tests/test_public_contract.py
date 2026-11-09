"""The Python SDK seam consumes only the generated authoritative API binding."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import get_type_hints

import originalpictures


def test_python_operation_binding_matches_committed_openapi_bytes() -> None:
    repository_root = Path(__file__).resolve().parents[3]
    openapi = repository_root / "packages" / "contracts" / "openapi" / "openapi.yaml"

    assert (
        hashlib.sha256(openapi.read_bytes()).hexdigest()
        == originalpictures.PUBLIC_API_OPENAPI_SHA256
    )
    assert originalpictures.PUBLIC_API_VERSION == "1.0.0"
    assert len(originalpictures.PUBLIC_API_OPERATIONS) == 128
    assert (
        len({operation.operation_id for operation in originalpictures.PUBLIC_API_OPERATIONS}) == 128
    )
    assert {operation.path for operation in originalpictures.PUBLIC_API_OPERATIONS} >= {
        "/healthz/db",
        "/v1/me",
        "/v1/recipes",
        "/webhooks/clerk",
    }
    assert all(
        not operation.path.startswith("/internal/")
        for operation in originalpictures.PUBLIC_API_OPERATIONS
    )
    assert sum(operation.executable for operation in originalpictures.PUBLIC_API_OPERATIONS) == 126
    assert {
        operation.operation_id
        for operation in originalpictures.PUBLIC_API_OPERATIONS
        if not operation.executable
    } == {"receiveClerkWebhook", "receiveStripeWebhook"}
    assert {
        operation.operation_id
        for operation in originalpictures.PUBLIC_API_OPERATIONS
        if operation.path.startswith("/v1/capture-")
    } == {
        "createCaptureIdentityEnrollment",
        "createCaptureIdentity",
        "listCaptureIdentities",
        "getCaptureIdentity",
        "createCaptureAdmissionChallenge",
        "createCaptureAdmission",
        "listCaptureAdmissions",
        "getCaptureAdmission",
        "revokeCaptureIdentity",
    }


def test_retention_and_billing_operations_remain_callable_with_exact_routes() -> None:
    operations = {
        operation.operation_id: operation for operation in originalpictures.PUBLIC_API_OPERATIONS
    }
    for operation_id, method, path in (
        ("getApiKeyRetention", "GET", "/v1/api-keys/{api_key_id}/retention"),
        ("setApiKeyRetention", "PUT", "/v1/api-keys/{api_key_id}/retention"),
        ("listBillingCharges", "GET", "/v1/billing/charges"),
        ("getBillingPricing", "GET", "/v1/billing/pricing"),
        ("createBillingQuote", "POST", "/v1/billing/quotes"),
    ):
        operation = operations[operation_id]
        assert operation.method == method
        assert operation.path == path
        assert operation.executable is True


def test_generated_webhook_models_are_importable_and_typed() -> None:
    request = originalpictures.CreateWebhookEndpointRequest(
        url="https://receiver.example/webhook",
        event_catalog_version="op.customer-events.v1",
        events=["asset.signed"],
    )
    assert request["url"] == "https://receiver.example/webhook"
    assert originalpictures.CreateWebhookEndpointHeaders.__required_keys__ == {"Idempotency-Key"}
    assert originalpictures.CreateWebhookEndpointParameters.__optional_keys__ == set()
    attempt_fields = get_type_hints(originalpictures.WebhookAttemptResponse)
    assert attempt_fields["replay_generation"] == int | None
    assert attempt_fields["fencing_token"] is int
    assert callable(originalpictures.GeneratedClientMixin.create_upload)
    assert callable(originalpictures.GeneratedAsyncClientMixin.create_verification)
    assert callable(originalpictures.GeneratedClientMixin.create_capture_identity)
    assert callable(originalpictures.GeneratedClientMixin.list_capture_admissions)
    assert callable(originalpictures.GeneratedAsyncClientMixin.revoke_capture_identity)
    assert callable(originalpictures.GeneratedClientMixin.get_api_key)
    assert callable(originalpictures.GeneratedClientMixin.complete_api_key_rotation)
    assert callable(originalpictures.GeneratedAsyncClientMixin.cancel_api_key_rotation)
    assert callable(originalpictures.GeneratedAsyncClientMixin.get_webhook_delivery)
    assert callable(originalpictures.GeneratedClientMixin.complete_webhook_endpoint_secret_overlap)
    assert not hasattr(originalpictures.GeneratedClientMixin, "receive_clerk_webhook")
    assert originalpictures.GetJobResponses.__required_keys__ >= {"200", "403", "404"}
    assert originalpictures.GetJobErrorResponses.__required_keys__ >= {"403", "404", "503"}


def test_shared_v1_compatibility_fixture_matches_generated_operations() -> None:
    repository_root = Path(__file__).resolve().parents[3]
    fixture = json.loads(
        (repository_root / "tests/fixtures/developer-surfaces/v1.json").read_text()
    )
    operation_ids = {operation.operation_id for operation in originalpictures.PUBLIC_API_OPERATIONS}
    assert fixture["contract_version"] == originalpictures.PUBLIC_API_VERSION
    assert fixture["operation_count"] == len(operation_ids)
    assert set(fixture["required_workflow_operations"]) <= operation_ids
