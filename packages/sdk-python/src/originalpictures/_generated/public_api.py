"""GENERATED FILE — do not edit by hand.

Source: packages/contracts/openapi/openapi.yaml
Regenerate with: pnpm contracts:generate
"""
# ruff: noqa: S105, UP013

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Final, Literal, NotRequired, Required, TypedDict, cast


@dataclass(frozen=True)
class PublicApiResponseContract:
    status_code: str
    content_types: tuple[str, ...]


@dataclass(frozen=True)
class PublicApiOperationContract:
    operation_id: str
    method: str
    path: str
    audience: str
    security_alternatives: tuple[tuple[str, ...], ...]
    executable: bool
    request_content_types: tuple[str, ...]
    responses: tuple[PublicApiResponseContract, ...]


PUBLIC_API_OPENAPI_SHA256: Final = (
    "dae3f9e07fda334eaeb7de8e2769869fd4074f4594501fc5b0eeab91b0bf9609"
)
PUBLIC_API_VERSION: Final = "1.0.0"
PUBLIC_API_OPERATIONS: Final[tuple[PublicApiOperationContract, ...]] = (
    PublicApiOperationContract(
        operation_id="getHealthz",
        method="GET",
        path="/healthz",
        audience="public-system",
        executable=True,
        security_alternatives=(),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getDatabaseHealth",
        method="GET",
        path="/healthz/db",
        audience="public-system",
        executable=True,
        security_alternatives=(),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getReadyz",
        method="GET",
        path="/readyz",
        audience="public-system",
        executable=True,
        security_alternatives=(),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getGovernanceReadyz",
        method="GET",
        path="/readyz/governance",
        audience="public-system",
        executable=True,
        security_alternatives=(),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="listApiKeys",
        method="GET",
        path="/v1/api-keys",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="createApiKey",
        method="POST",
        path="/v1/api-keys",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="201",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="revokeApiKey",
        method="DELETE",
        path="/v1/api-keys/{api_key_id}",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getApiKey",
        method="GET",
        path="/v1/api-keys/{api_key_id}",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getApiKeyRestrictions",
        method="GET",
        path="/v1/api-keys/{api_key_id}/restrictions",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="setApiKeyRestrictions",
        method="PUT",
        path="/v1/api-keys/{api_key_id}/restrictions",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getApiKeyRetention",
        method="GET",
        path="/v1/api-keys/{api_key_id}/retention",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="setApiKeyRetention",
        method="PUT",
        path="/v1/api-keys/{api_key_id}/retention",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="rotateApiKey",
        method="POST",
        path="/v1/api-keys/{api_key_id}/rotate",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="201",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="cancelApiKeyRotation",
        method="POST",
        path="/v1/api-keys/{api_key_id}/rotation/cancel",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="completeApiKeyRotation",
        method="POST",
        path="/v1/api-keys/{api_key_id}/rotation/complete",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getApiKeySigningProfile",
        method="GET",
        path="/v1/api-keys/{api_key_id}/signing-profile",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="setApiKeySigningProfile",
        method="PUT",
        path="/v1/api-keys/{api_key_id}/signing-profile",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="listApiKeyScopes",
        method="GET",
        path="/v1/api-keys/scopes",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="listApiRequestLogs",
        method="GET",
        path="/v1/api-request-logs",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="summarizeApiRequestLogs",
        method="GET",
        path="/v1/api-request-logs/summary",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="listAssets",
        method="GET",
        path="/v1/assets",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getAsset",
        method="GET",
        path="/v1/assets/{asset_id}",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getAssetDetail",
        method="GET",
        path="/v1/assets/{asset_id}/detail",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="createAssetDownload",
        method="POST",
        path="/v1/assets/{asset_id}/download",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="createAssetPreview",
        method="POST",
        path="/v1/assets/{asset_id}/preview",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="redeemAssetPreview",
        method="GET",
        path="/v1/assets/{asset_id}/preview/{capability}",
        audience="tenant",
        executable=True,
        security_alternatives=(),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("image/jpeg",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getBillingAccount",
        method="GET",
        path="/v1/billing/account",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="listBillingCharges",
        method="GET",
        path="/v1/billing/charges",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="createBillingCheckoutIntent",
        method="POST",
        path="/v1/billing/checkout-intents",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="201",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="502",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="listBillingInvoices",
        method="GET",
        path="/v1/billing/invoices",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getBillingPlans",
        method="GET",
        path="/v1/billing/plans",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="createBillingPortalIntent",
        method="POST",
        path="/v1/billing/portal-intents",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="201",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="502",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getBillingPricing",
        method="GET",
        path="/v1/billing/pricing",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="createBillingQuote",
        method="POST",
        path="/v1/billing/quotes",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getBillingWallet",
        method="GET",
        path="/v1/billing/wallet",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="setBillingWalletSettings",
        method="PUT",
        path="/v1/billing/wallet/settings",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getCapabilities",
        method="GET",
        path="/v1/capabilities",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="createCaptureAdmissionChallenge",
        method="POST",
        path="/v1/capture-admission-challenges",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="201",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="listCaptureAdmissions",
        method="GET",
        path="/v1/capture-admissions",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="createCaptureAdmission",
        method="POST",
        path="/v1/capture-admissions",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="201",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getCaptureAdmission",
        method="GET",
        path="/v1/capture-admissions/{capture_admission_id}",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="304",
                content_types=(),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="listCaptureIdentities",
        method="GET",
        path="/v1/capture-identities",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="createCaptureIdentity",
        method="POST",
        path="/v1/capture-identities",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="201",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getCaptureIdentity",
        method="GET",
        path="/v1/capture-identities/{capture_identity_id}",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="304",
                content_types=(),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="revokeCaptureIdentity",
        method="POST",
        path="/v1/capture-identities/{capture_identity_id}/revoke",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="createCaptureIdentityEnrollment",
        method="POST",
        path="/v1/capture-identity-enrollments",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="201",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getConnectCatalog",
        method="GET",
        path="/v1/connect-catalog",
        audience="public-system",
        executable=True,
        security_alternatives=(),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getCreatorDisclosurePolicy",
        method="GET",
        path="/v1/creator-disclosure-policy",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="updateCreatorDisclosurePolicy",
        method="PUT",
        path="/v1/creator-disclosure-policy",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="listCreatorIdentities",
        method="GET",
        path="/v1/creator-identities",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="createCreatorIdentity",
        method="POST",
        path="/v1/creator-identities",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="201",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getCreatorIdentity",
        method="GET",
        path="/v1/creator-identities/{creator_identity_id}",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="discloseCreatorIdentity",
        method="GET",
        path="/v1/creator-identities/{creator_identity_id}/disclosure",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="withdrawCreatorIdentity",
        method="POST",
        path="/v1/creator-identities/{creator_identity_id}/withdraw",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getDeveloperOnboarding",
        method="GET",
        path="/v1/developer-onboarding",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="listDisclosureEvents",
        method="GET",
        path="/v1/disclosures/events",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="createDisclosureEvent",
        method="POST",
        path="/v1/disclosures/events",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="201",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getDisclosurePolicies",
        method="GET",
        path="/v1/disclosures/policies",
        audience="public-system",
        executable=True,
        security_alternatives=(),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="submitFeedback",
        method="POST",
        path="/v1/feedback",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="201",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="queryGovernanceAudit",
        method="GET",
        path="/v1/governance/audit",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="listGovernanceDeletions",
        method="GET",
        path="/v1/governance/deletions",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="createGovernanceDeletion",
        method="POST",
        path="/v1/governance/deletions",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="202",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getGovernanceDeletion",
        method="GET",
        path="/v1/governance/deletions/{deletion_id}",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="listGovernanceExports",
        method="GET",
        path="/v1/governance/exports",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="createGovernanceExport",
        method="POST",
        path="/v1/governance/exports",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="202",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getGovernanceExport",
        method="GET",
        path="/v1/governance/exports/{export_id}",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="listGovernanceLegalHolds",
        method="GET",
        path="/v1/governance/legal-holds",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="releaseHistorySnapshot",
        method="DELETE",
        path="/v1/history/snapshots",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="204",
                content_types=(),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="listIdentityCredentials",
        method="GET",
        path="/v1/identity-credentials",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="listImageProfiles",
        method="GET",
        path="/v1/image-profiles",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="listJobs",
        method="GET",
        path="/v1/jobs",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getJob",
        method="GET",
        path="/v1/jobs/{job_id}",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="cancelJob",
        method="POST",
        path="/v1/jobs/{job_id}/cancel",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="createMarkingCheck",
        method="POST",
        path="/v1/marking-checks",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="202",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getMarkingCheck",
        method="GET",
        path="/v1/marking-checks/{marking_check_id}",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getCurrentUser",
        method="GET",
        path="/v1/me",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getOverview",
        method="GET",
        path="/v1/overview",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getPublicVerifyPage",
        method="GET",
        path="/v1/public/verify-pages/{slug}",
        audience="public-system",
        executable=True,
        security_alternatives=(),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="createPublicCheck",
        method="POST",
        path="/v1/public/verify-pages/{slug}/checks",
        audience="public-system",
        executable=True,
        security_alternatives=(),
        request_content_types=("multipart/form-data",),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="202",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="413",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="415",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getPublicCheck",
        method="GET",
        path="/v1/public/verify-pages/{slug}/checks/{check_id}",
        audience="public-system",
        executable=True,
        security_alternatives=(),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getPublicVerifyPageLogo",
        method="GET",
        path="/v1/public/verify-pages/{slug}/logo",
        audience="public-system",
        executable=True,
        security_alternatives=(),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=(
                    "image/jpeg",
                    "image/png",
                    "image/webp",
                ),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="listReceipts",
        method="GET",
        path="/v1/receipts",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getSigningReceipt",
        method="GET",
        path="/v1/receipts/{receipt_id}",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="listRecipes",
        method="GET",
        path="/v1/recipes",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getRecipe",
        method="GET",
        path="/v1/recipes/{recipe_id}",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getSharedVerification",
        method="GET",
        path="/v1/shared-verifications/{token}",
        audience="public-system",
        executable=True,
        security_alternatives=(),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="acceptSigningJob",
        method="POST",
        path="/v1/sign",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="202",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="402",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="acceptSigningJobBatch",
        method="POST",
        path="/v1/sign/batch",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="202",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="createUpload",
        method="POST",
        path="/v1/uploads",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="201",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="abortUpload",
        method="POST",
        path="/v1/uploads/{upload_id}/abort",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="completeUpload",
        method="POST",
        path="/v1/uploads/{upload_id}/complete",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="410",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getUsage",
        method="GET",
        path="/v1/usage",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getVerificationEvidence",
        method="GET",
        path="/v1/verification-evidence/{verification_id}",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="createVerificationReport",
        method="POST",
        path="/v1/verification-evidence/{verification_id}/reports",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="202",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="listVerificationShares",
        method="GET",
        path="/v1/verification-evidence/{verification_id}/shares",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="createVerificationShare",
        method="POST",
        path="/v1/verification-evidence/{verification_id}/shares",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="201",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getVerificationHistory",
        method="GET",
        path="/v1/verification-history/{verification_id}",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getVerificationReport",
        method="GET",
        path="/v1/verification-reports/{report_id}",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="closeVerificationShare",
        method="POST",
        path="/v1/verification-shares/{share_id}/close",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="listVerifications",
        method="GET",
        path="/v1/verifications",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="createVerification",
        method="POST",
        path="/v1/verifications",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="202",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getVerification",
        method="GET",
        path="/v1/verifications/{verification_id}",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="createVerificationBatch",
        method="POST",
        path="/v1/verifications/batch",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="202",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getVerifyPage",
        method="GET",
        path="/v1/verify-pages",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="putVerifyPage",
        method="PUT",
        path="/v1/verify-pages",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="listWebhookEndpoints",
        method="GET",
        path="/v1/webhook-endpoints",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="createWebhookEndpoint",
        method="POST",
        path="/v1/webhook-endpoints",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="201",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="deleteWebhookEndpoint",
        method="DELETE",
        path="/v1/webhook-endpoints/{endpoint_id}",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="204",
                content_types=(),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getWebhookEndpoint",
        method="GET",
        path="/v1/webhook-endpoints/{endpoint_id}",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="updateWebhookEndpoint",
        method="PATCH",
        path="/v1/webhook-endpoints/{endpoint_id}",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="listWebhookDeliveries",
        method="GET",
        path="/v1/webhook-endpoints/{endpoint_id}/deliveries",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="disableWebhookEndpoint",
        method="POST",
        path="/v1/webhook-endpoints/{endpoint_id}/disable",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="204",
                content_types=(),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="enableWebhookEndpoint",
        method="POST",
        path="/v1/webhook-endpoints/{endpoint_id}/enable",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="rotateWebhookEndpointSecret",
        method="POST",
        path="/v1/webhook-endpoints/{endpoint_id}/rotate-secret",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="completeWebhookEndpointSecretOverlap",
        method="POST",
        path="/v1/webhook-endpoints/{endpoint_id}/secret-overlap/complete",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="sendWebhookTestEvent",
        method="POST",
        path="/v1/webhook-endpoints/{endpoint_id}/test",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="202",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getWebhookDelivery",
        method="GET",
        path="/v1/webhook-endpoints/deliveries/{delivery_id}",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="listWebhookDeliveryAttempts",
        method="GET",
        path="/v1/webhook-endpoints/deliveries/{delivery_id}/attempts",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="replayWebhookDelivery",
        method="POST",
        path="/v1/webhook-endpoints/deliveries/{delivery_id}/replay",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getWebhookEventCatalog",
        method="GET",
        path="/v1/webhook-endpoints/event-catalog",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="replayWebhookEvent",
        method="POST",
        path="/v1/webhook-events/{event_id}/replay",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="listWorkflowTemplates",
        method="GET",
        path="/v1/workflow-templates",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="createWorkflowTemplate",
        method="POST",
        path="/v1/workflow-templates",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="201",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="deleteWorkflowTemplate",
        method="DELETE",
        path="/v1/workflow-templates/{template_id}",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="204",
                content_types=(),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="getWorkflowTemplate",
        method="GET",
        path="/v1/workflow-templates/{template_id}",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=(),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="replaceWorkflowTemplate",
        method="PUT",
        path="/v1/workflow-templates/{template_id}",
        audience="tenant",
        executable=True,
        security_alternatives=(("bearerAuth",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="401",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="403",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="404",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="429",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="receiveClerkWebhook",
        method="POST",
        path="/webhooks/clerk",
        audience="provider-webhook",
        executable=False,
        security_alternatives=(("clerkWebhookSignature",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="200",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="400",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="413",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="422",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
    PublicApiOperationContract(
        operation_id="receiveStripeWebhook",
        method="POST",
        path="/webhooks/stripe",
        audience="provider-webhook",
        executable=False,
        security_alternatives=(("stripeWebhookSignature",),),
        request_content_types=("application/json",),
        responses=(
            PublicApiResponseContract(
                status_code="202",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="400",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="409",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="413",
                content_types=("application/json",),
            ),
            PublicApiResponseContract(
                status_code="503",
                content_types=("application/json",),
            ),
        ),
    ),
)


# Complete generated schema and operation model surface.
class AbortUploadResponse(TypedDict):
    status: Required[UploadStatus]
    upload_id: Required[str]


class AiActionResponse(TypedDict):
    description: Required[str]
    id: Required[str]
    kind: Required[Literal["copy"] | Literal["deep_link"]]
    label: Required[str]
    maximum_prompt_characters: Required[int | None]
    over_limit_fallback_action_id: Required[str | None]
    target: Required[
        Literal["clipboard"] | Literal["cursor"] | Literal["claude"] | Literal["chatgpt"]
    ]
    url_template: Required[str | None]


class AiDeclarationRequest(TypedDict):
    digital_source_type: Required[
        Literal["trainedAlgorithmicMedia"]
        | Literal["compositeWithTrainedAlgorithmicMedia"]
        | Literal["compositeSynthetic"]
    ]
    human_oversight_level: NotRequired[
        Literal["human-in-the-loop"]
        | Literal["human-on-the-loop"]
        | Literal["human-out-of-the-loop"]
        | None
    ]
    models: NotRequired[list[AiModelDisclosureRequest]]
    software_agent_name: Required[str]
    software_agent_version: NotRequired[str | None]


class AiDeclaredSigningReceiptEvidenceResponse(TypedDict):
    ai_declaration: Required[ReceiptAiDeclarationResponse]
    asset_id: Required[str]
    bindings: Required[ReceiptBindingSetResponse | SidecarReceiptBindingSetResponse]
    job_id: Required[str]
    manifest: Required[ReceiptManifestResponse]
    output: Required[ReceiptOutputResponse]
    product: Required[ReceiptProductResponse]
    published_at: Required[str]
    schema_version: Required[Literal["op.signing-receipt.ai-declared.v1"]]
    signing: Required[ReceiptSigningResponse]
    validation: Required[ReceiptValidationResponse]


class AiMarkBlock(TypedDict):
    declaration: Required[AiDeclarationRequest]
    type: Required[Literal["ai_mark"]]


class AiModelDisclosureRequest(TypedDict):
    name: Required[str]
    scientific_domain: NotRequired[str | None]
    version: NotRequired[str | None]


class AiPromptResponse(TypedDict):
    credential_environment_variable: Required[str]
    id: Required[str]
    secret_substitution_allowed: Required[bool]
    section_order: Required[list[str]]
    template_id: Required[str]
    title: Required[str]


class ApiKeyCreateRequest(TypedDict):
    expires_at: NotRequired[str | None]
    name: NotRequired[str | None]
    preset: NotRequired[ApiKeyPreset | None]
    restrictions: NotRequired[ApiKeyRestrictionsRequest | None]
    retention_mode: NotRequired[
        Literal["1h"] | Literal["24h"] | Literal["72h"] | Literal["retain"] | None
    ]
    scopes: NotRequired[list[str] | None]
    signing_profile: NotRequired[ApiKeySigningProfileDocument | None]


class ApiKeyListResponse(TypedDict):
    data: Required[list[ApiKeyMetadataResponse]]


class ApiKeyMetadataResponse(TypedDict):
    created_at: Required[str]
    display_hint: Required[str]
    expires_at: Required[str | None]
    id: Required[str]
    last_used_at: Required[str | None]
    name: Required[str | None]
    restrictions: NotRequired[ApiKeyRestrictionsView | None]
    revoked_at: Required[str | None]
    rotated_from_id: Required[str | None]
    rotation: NotRequired[ApiKeyRotationResponse | None]
    scopes: Required[list[str]]
    status: Required[ApiKeyStatus]


type ApiKeyPreset = Literal["full_access"] | Literal["publishable_disclosure"]


class ApiKeyRestrictionsRequest(TypedDict):
    allowed_ip_cidrs: NotRequired[list[str] | None]
    allowed_origins: NotRequired[list[str] | None]
    rate_limit_per_minute: NotRequired[int | None]


class ApiKeyRestrictionsResponse(TypedDict):
    allowed_ip_cidrs: Required[list[str] | None]
    allowed_origins: NotRequired[list[str] | None]
    api_key_id: Required[str]
    ip_allowlist_available: Required[bool]
    rate_limit_per_minute: Required[int | None]
    version: Required[int]


class ApiKeyRestrictionsUpdateRequest(TypedDict):
    allowed_ip_cidrs: Required[list[str] | None]
    allowed_origins: NotRequired[list[str] | None]
    expected_version: Required[int]
    rate_limit_per_minute: Required[int | None]


class ApiKeyRestrictionsView(TypedDict):
    allowed_ip_cidrs: Required[list[str] | None]
    allowed_origins: NotRequired[list[str] | None]
    rate_limit_per_minute: Required[int | None]
    version: Required[int]


class ApiKeyRetentionRequest(TypedDict):
    expected_version: Required[int]
    retention_mode: Required[Literal["1h"] | Literal["24h"] | Literal["72h"] | Literal["retain"]]


class ApiKeyRetentionResponse(TypedDict):
    api_key_id: Required[str]
    clock_starts_at: Required[Literal["validated_publication"]]
    effective_for: Required[Literal["future_job_admissions"]]
    retention_mode: Required[
        Literal["legacy"] | Literal["1h"] | Literal["24h"] | Literal["72h"] | Literal["retain"]
    ]
    version: Required[int]


class ApiKeyRotateRequest(TypedDict):
    expires_at: NotRequired[str | None]
    overlap_seconds: NotRequired[int]


class ApiKeyRotationResponse(TypedDict):
    deadline_at: Required[str]
    peer_id: Required[str]
    role: Required[ApiKeyRotationRole]
    started_at: Required[str]


type ApiKeyRotationRole = Literal["outgoing"] | Literal["successor"]


class ApiKeyScopeCatalogResponse(TypedDict):
    catalog_version: Required[str]
    groups: Required[list[ApiKeyScopeGroupResponse]]
    scopes: Required[list[ApiKeyScopeDescriptorResponse]]
    wildcard_supported: NotRequired[Literal[False]]


class ApiKeyScopeDescriptorResponse(TypedDict):
    description: Required[str]
    group: Required[str]
    label: Required[str]
    scope: Required[str]


class ApiKeyScopeGroupResponse(TypedDict):
    description: Required[str]
    id: Required[str]
    label: Required[str]


class ApiKeySigningProfileDocument(TypedDict):
    allowed_fingerprint_algorithms: NotRequired[list[str] | None]
    allowed_media_types: NotRequired[list[str] | None]
    allowed_recipes: NotRequired[list[str] | None]
    allowed_watermark_algorithms: NotRequired[list[str] | None]
    allowed_watermark_strengths: NotRequired[
        list[Literal["subtle"] | Literal["balanced"] | Literal["robust"]] | None
    ]
    default_fingerprint_algorithms: NotRequired[list[str] | None]
    default_recipe: NotRequired[str | None]
    default_watermark_algorithm: NotRequired[str | None]
    default_watermark_strength: NotRequired[
        Literal["subtle"] | Literal["balanced"] | Literal["robust"] | None
    ]


class ApiKeySigningProfileResponse(TypedDict):
    api_key_id: Required[str]
    profile: Required[ApiKeySigningProfileDocument]
    version: Required[int]


class ApiKeySigningProfileUpdateRequest(TypedDict):
    expected_version: Required[int]
    profile: Required[ApiKeySigningProfileDocument]


type ApiKeyStatus = Literal["active"] | Literal["expired"] | Literal["revoked"] | Literal["rotated"]


class ApiRequestLogItem(TypedDict):
    api_key_id: Required[str | None]
    client_ip: Required[str | None]
    client_network: Required[str | None]
    duration_ms: Required[int]
    method: Required[str]
    occurred_at: Required[str]
    reason_code: Required[str | None]
    request_id: Required[str | None]
    route: Required[str]
    status: Required[int]


class ApiRequestLogPageResponse(TypedDict):
    best_effort: NotRequired[Literal[True]]
    data: Required[list[ApiRequestLogItem]]
    next_cursor: Required[str | None]


class ApiRequestLogStatusClasses(TypedDict):
    client_error: Required[int]
    redirect: Required[int]
    server_error: Required[int]
    success: Required[int]


class ApiRequestLogSummaryResponse(TypedDict):
    best_effort: NotRequired[Literal[True]]
    p50_duration_ms: Required[int | None]
    p95_duration_ms: Required[int | None]
    refused: Required[int]
    since: Required[str]
    status_classes: Required[ApiRequestLogStatusClasses]
    total: Required[int]
    window: Required[SummaryWindow]


type AssetAction = (
    Literal["download"]
    | Literal["preview"]
    | Literal["verify_again"]
    | Literal["request_deletion"]
    | Literal["request_account_export"]
)

type AssetActionReason = (
    Literal["not_published"]
    | Literal["restricted"]
    | Literal["already_deleted"]
    | Literal["deletion_in_progress"]
    | Literal["legal_hold"]
    | Literal["preview_pending"]
    | Literal["preview_unavailable"]
    | Literal["still_processing"]
)


class AssetActionResponse(TypedDict):
    action: Required[AssetAction]
    available: Required[bool]
    reason: Required[AssetActionReason | None]


class AssetActivityEventResponse(TypedDict):
    kind: Required[AssetActivityKind]
    occurred_at: Required[str]
    related_id: Required[str | None]
    related_url: Required[str | None]


type AssetActivityKind = (
    Literal["upload_completed"]
    | Literal["job_started"]
    | Literal["job_completed"]
    | Literal["job_failed"]
    | Literal["published"]
    | Literal["receipt_issued"]
    | Literal["verification_completed"]
    | Literal["preview_derived"]
    | Literal["deletion_requested"]
    | Literal["deletion_completed"]
    | Literal["deletion_failed"]
    | Literal["legal_hold_placed"]
    | Literal["legal_hold_released"]
)


class AssetActivityResponse(TypedDict):
    items: Required[list[AssetActivityEventResponse]]
    next_cursor: Required[str | None]


type AssetDeletionState = (
    Literal["requested"]
    | Literal["processing"]
    | Literal["retry_wait"]
    | Literal["blocked_legal_hold"]
    | Literal["completed"]
    | Literal["failed"]
)


class AssetDetailResponse(TypedDict):
    actions: Required[list[AssetActionResponse]]
    activity: Required[AssetActivityResponse]
    as_of: Required[str]
    asset: Required[AssetHistoryResponse]
    verification_history: Required[AssetVerificationHistoryResponse]
    workspace_governance: Required[WorkspaceGovernanceResponse]


class AssetGovernanceResponse(TypedDict):
    deletion_state: Required[AssetDeletionState | None]
    legal_hold_active: Required[bool]
    retention: NotRequired[AssetRetentionResponse | None]


type AssetHistoryKind = (
    Literal["uninspected"]
    | Literal["image"]
    | Literal["audio"]
    | Literal["video"]
    | Literal["text"]
    | Literal["fonts"]
    | Literal["mlModel"]
    | Literal["documents"]
    | Literal["imageSidecar"]
    | Literal["audioSidecar"]
    | Literal["videoSidecar"]
)

type AssetHistoryOrigin = Literal["upload"] | Literal["capture"] | Literal["derived"]


class AssetHistoryPageResponse(TypedDict):
    items: Required[list[AssetHistoryResponse]]
    next_cursor: Required[str | None]
    total_count: Required[int]
    workspace_governance: Required[WorkspaceGovernanceResponse]


class AssetHistoryResponse(TypedDict):
    asset_id: Required[str]
    asset_url: Required[str]
    byte_length: Required[int | None]
    created_at: Required[str]
    display_name: Required[str]
    download_url: Required[str | None]
    governance: Required[AssetGovernanceResponse]
    job: Required[AssetJobResponse | None]
    kind: Required[AssetHistoryKind]
    media: Required[AssetMediaResponse]
    media_type: Required[HistoryMediaType | None]
    origin: Required[AssetHistoryOrigin]
    preview_state: Required[AssetPreviewState]
    publication_id: Required[str | None]
    receipt_id: Required[str | None]
    sha256: Required[str | None]
    status: Required[AssetHistoryStatus]
    verification: Required[AssetVerificationResponse]
    verification_id: Required[str | None]


type AssetHistoryStatus = (
    Literal["pending"]
    | Literal["ready"]
    | Literal["processing"]
    | Literal["signed"]
    | Literal["watermarked"]
    | Literal["failed"]
    | Literal["deleted"]
)


class AssetJobResponse(TypedDict):
    created_at: Required[str]
    error_code: Required[str | None]
    failed_steps: Required[int]
    job_id: Required[str]
    job_url: Required[str]
    kind: Required[JobKind]
    recipe_id: Required[str]
    recipe_version: Required[int]
    state: Required[JobState]
    succeeded_steps: Required[int]
    total_steps: Required[int]
    updated_at: Required[str]


type AssetMediaFamily = Literal["image"] | Literal["audio"] | Literal["video"] | Literal["text"]


class AssetMediaResponse(TypedDict):
    byte_length: Required[int | None]
    codec_label: Required[str | None]
    duration_microseconds: Required[int | None]
    family: Required[AssetMediaFamily | None]
    frame_rate_denominator: Required[int | None]
    frame_rate_numerator: Required[int | None]
    height: Required[int | None]
    inspected: Required[bool]
    media_type: Required[HistoryMediaType | None]
    width: Required[int | None]


type AssetPreviewState = (
    Literal["available"] | Literal["pending"] | Literal["unavailable"] | Literal["restricted"]
)


class AssetResponse(TypedDict):
    asset_id: Required[str]
    created_at: Required[str]
    kind: Required[str]
    media_type: Required[str | None]
    publication: Required[PublicationResponse | None]
    status: Required[str]


class AssetRetentionClassResponse(TypedDict):
    data_class: Required[str]
    delete_after: NotRequired[str | None]
    is_indefinite: Required[bool]
    object_count: Required[int]


class AssetRetentionResponse(TypedDict):
    classes: Required[list[AssetRetentionClassResponse]]
    indefinite_object_count: Required[int]
    latest_delete_after: NotRequired[str | None]
    object_count: Required[int]
    soonest_delete_after: NotRequired[str | None]


class AssetVerificationEntryResponse(TypedDict):
    created_at: Required[str]
    evidence_url: Required[str]
    overall: Required[VerificationOverall]
    validated_at: Required[str]
    validation_path: Required[str | None]
    verification_id: Required[str]
    verification_url: Required[str]


class AssetVerificationHistoryResponse(TypedDict):
    items: Required[list[AssetVerificationEntryResponse]]
    next_cursor: Required[str | None]


class AssetVerificationResponse(TypedDict):
    count: Required[int]
    latest_overall: Required[VerificationOverall | None]
    latest_validated_at: Required[str | None]
    latest_validation_path: Required[ValidationPath | None]
    latest_verification_id: Required[str | None]


type AttestationKind = (
    Literal["app_attest"] | Literal["play_integrity"] | Literal["hardware_key_attestation"]
)

type AudioCodec = (
    Literal["pcm_u8"]
    | Literal["pcm_s16le"]
    | Literal["pcm_s24le"]
    | Literal["pcm_s32le"]
    | Literal["mp3"]
    | Literal["aac_lc"]
)


class AudioTrackFacts(TypedDict):
    bits_per_sample: Required[int]
    channel_layout: Required[str]
    channels: Required[int]
    codec: Required[AudioCodec]
    codec_profile: Required[str]
    decoded_byte_length: Required[int]
    duration_microseconds: Required[int]
    frame_count: Required[int]
    sample_count: Required[int]
    sample_rate_hz: Required[int]
    stream_index: Required[int]
    time_base_denominator: Required[int]
    time_base_numerator: Required[int]


class AuditEventResponse(TypedDict):
    action: Required[str]
    actor_id: Required[str | None]
    actor_type: Required[str]
    data_sha256: Required[str | None]
    event_id: Required[str]
    occurred_at: Required[str]
    request_id: Required[str | None]
    resource_id: Required[str | None]
    resource_type: Required[str | None]


class BillingAccountResponse(TypedDict):
    cancel_at_period_end: Required[bool]
    caps: Required[dict[str, Any]]
    current_period_end: Required[str | None]
    current_service_period_end: Required[str | None]
    current_service_period_start: Required[str | None]
    id: Required[str]
    plan: Required[str]
    plan_display_name: Required[str | None]
    portal_available: Required[bool]
    provider_customer_provisioned: Required[bool]
    renewal_at: Required[str | None]
    status: Required[str]


class BillingIntentResponse(TypedDict):
    actionable: Required[bool]
    expires_at: Required[str]
    id: Required[str]
    mode: Required[Literal["simulation"] | Literal["sandbox"] | Literal["provider"]]
    url: Required[str | None]


class BillingInvoiceResponse(TypedDict):
    amount_due: Required[str | None]
    created_at: Required[str]
    currency: Required[str | None]
    hosted_invoice_url: Required[str | None]
    id: Required[str]
    number: Required[str | None]
    period: Required[str]
    service_period_end: Required[str | None]
    service_period_start: Required[str | None]
    status: Required[str | None]


class BillingInvoicesResponse(TypedDict):
    items: Required[list[BillingInvoiceResponse]]
    next_before: Required[str | None]


type BillingPlanId = (
    Literal["plan_10k"]
    | Literal["plan_50k"]
    | Literal["plan_150k"]
    | Literal["plan_500k"]
    | Literal["payg"]
    | Literal["platform"]
    | Literal["cawg_identity_individual"]
    | Literal["cawg_identity_organisation"]
)


class BillingPlanResponse(TypedDict):
    availability: NotRequired[
        Literal["available"] | Literal["on_request"] | Literal["on_enrolment"]
    ]
    availability_note: NotRequired[str | None]
    billing_model: Required[Literal["subscription"] | Literal["metered"]]
    checkout_available: Required[bool]
    display_name: Required[str]
    id: Required[BillingPlanId]
    interval: NotRequired[Literal["month"] | Literal["year"]]
    monthly_assets: Required[int | None]
    monthly_usd: Required[str]


class BillingPlansResponse(TypedDict):
    currency: NotRequired[Literal["USD"]]
    plans: Required[list[BillingPlanResponse]]
    pricing_version: Required[str]
    provider_mode: Required[Literal["simulation"] | Literal["sandbox"] | Literal["provider"] | None]


class BindingReceiptEvidenceResponse(TypedDict):
    asset_id: Required[str]
    bindings: Required[ReceiptBindingSetResponse]
    job_id: Required[str]
    output: Required[ReceiptOutputResponse]
    product: Required[ReceiptProductResponse]
    published_at: Required[str]
    schema_version: Required[Literal["op.binding-receipt.v1"]]
    validation: Required[ReceiptValidationResponse]


class ByteRange(TypedDict):
    length: Required[int]
    offset: Required[int]


type C2PAStatusVocabularyVersion = Literal["op.c2pa-status.v1"] | Literal["op.c2pa-status.v2"]


class CancelJobRequest(TypedDict):
    reason: NotRequired[str | None]


class CanonicalCallResponse(TypedDict):
    id: Required[str]
    method: Required[str]
    path: Required[str]
    purpose: Required[str]
    required_scope: Required[str]


class CapabilityAvailabilityResponse(TypedDict):
    available: Required[bool]
    configured: Required[bool]
    state: Required[CapabilityAvailabilityState]


type CapabilityAvailabilityState = (
    Literal["available"] | Literal["temporarily_unavailable"] | Literal["unavailable"]
)


class CapabilityDiscoveryResponse(TypedDict):
    capture: Required[CaptureCapabilityResponse]
    contract: Required[ContractCapabilityResponse]
    media: Required[list[MediaCapabilityResponse]]
    recipes: Required[list[ReviewedRecipeAvailabilityResponse]]
    schema_version: Required[Literal["op.capability-discovery.v1"]]


class CapabilityRecipeResponse(TypedDict):
    capabilities: Required[list[PublicRecipeCapability]]
    display_name: Required[str]
    recipe_id: Required[str]
    summary: Required[str]
    supported_media_types: Required[
        list[
            Literal["application/epub+zip"]
            | Literal["application/onnx"]
            | Literal["application/oxps"]
            | Literal["application/pdf"]
            | Literal["application/vnd.oasis.opendocument.text"]
            | Literal["application/vnd.openxmlformats-officedocument.wordprocessingml.document"]
            | Literal["application/x-jax"]
            | Literal["application/x-keras"]
            | Literal["application/x-mlnet"]
            | Literal["application/x-mxnet"]
            | Literal["application/x-npy"]
            | Literal["application/x-openvino-ir+xml"]
            | Literal["application/x-openvino-weights"]
            | Literal["application/x-pickle"]
            | Literal["application/x-protobuf"]
            | Literal["application/x-pytorch"]
            | Literal["application/x-tensorflow"]
            | Literal["application/x-tensorflow-savedmodel"]
            | Literal["application/x-zip-based"]
            | Literal["application/xhtml+xml"]
            | Literal["application/xml"]
            | Literal["audio/MPA"]
            | Literal["audio/aac"]
            | Literal["audio/flac"]
            | Literal["audio/mp4"]
            | Literal["audio/mpeg"]
            | Literal["audio/wav"]
            | Literal["audio/x-riff-based"]
            | Literal["font/otf"]
            | Literal["image/avif"]
            | Literal["image/gif"]
            | Literal["image/heic"]
            | Literal["image/heic-sequence"]
            | Literal["image/heif"]
            | Literal["image/heif-sequence"]
            | Literal["image/jpeg"]
            | Literal["image/jxl"]
            | Literal["image/png"]
            | Literal["image/svg+xml"]
            | Literal["image/tiff"]
            | Literal["image/webp"]
            | Literal["image/x-adobe-dng"]
            | Literal["image/x-riff-based"]
            | Literal["image/x-tiff-based"]
            | Literal["text/html"]
            | Literal["text/plain"]
            | Literal["text/xml"]
            | Literal["video/mp4"]
            | Literal["video/quicktime"]
            | Literal["video/x-bmff-based"]
            | Literal["video/x-msvideo"]
            | Literal["video/x-riff-based"]
        ]
    ]
    version: Required[int]


class CaptureAdmissionChallengeRequest(TypedDict):
    capture_identity_id: Required[str]


class CaptureAdmissionChallengeResponse(TypedDict):
    capture_identity_id: Required[str]
    challenge_id: Required[str]
    challenge_secret: Required[str]
    expires_at: Required[str]


type CaptureAdmissionDecision = Literal["pass"] | Literal["reject"]


class CaptureAdmissionDetail(TypedDict):
    admission_policy_version: Required[str]
    asset_id: Required[str | None]
    capture_admission_id: Required[str]
    capture_identity_id: Required[str]
    capture_policy_id: Required[str]
    capture_policy_version: Required[str]
    decided_at: Required[str]
    decision: Required[CaptureAdmissionDecision]
    evidence_schema_version: Required[str]
    failed_gates: Required[list[PublicCaptureAdmissionReason]]
    governance_policy_version: Required[str]
    identity_version_id: Required[str]
    job_id: Required[str | None]
    provider_class: Required[CaptureProviderClass]
    reason: Required[PublicCaptureAdmissionReason]
    revocation_snapshot_version: Required[str]
    trust_snapshot_version: Required[str]
    upload_object_id: Required[str]
    verifier_version: Required[str]


class CaptureAdmissionListResponse(TypedDict):
    items: Required[list[CaptureAdmissionSummary]]
    next_cursor: Required[str | None]


class CaptureAdmissionSubmissionRequest(TypedDict):
    attestation_kind: Required[AttestationKind]
    capture_identity_id: Required[str]
    challenge_id: Required[str]
    challenge_secret: Required[str]
    installation_id_sha256: Required[str]
    sensor_evidence: NotRequired[dict[str, Any] | None]
    sensor_schema_version: NotRequired[str | None]
    statement: Required[str]
    upload_object_id: Required[str]


class CaptureAdmissionSubmissionResponse(TypedDict):
    capture_admission_id: Required[str]
    decision: Required[CaptureAdmissionDecision]
    failed_gates: Required[list[PublicCaptureAdmissionReason]]
    job_id: Required[str | None]
    reason: Required[PublicCaptureAdmissionReason]


class CaptureAdmissionSummary(TypedDict):
    asset_id: Required[str | None]
    capture_admission_id: Required[str]
    capture_identity_id: Required[str]
    decided_at: Required[str]
    decision: Required[CaptureAdmissionDecision]
    failed_gates: Required[list[PublicCaptureAdmissionReason]]
    job_id: Required[str | None]
    reason: Required[PublicCaptureAdmissionReason]
    upload_object_id: Required[str]


class CaptureCapabilityResponse(TypedDict):
    availability: Required[CapabilityAvailabilityResponse]


class CaptureIdentityCreationRequest(TypedDict):
    attestation_kind: Required[AttestationKind]
    capture_identity_enrollment_id: Required[str]
    challenge_secret: Required[str]
    statement: Required[str]


class CaptureIdentityDetail(TypedDict):
    capture_identity_id: Required[str]
    capture_policy_id: Required[str]
    capture_policy_version: Required[str]
    enrolled_at: Required[str]
    evidence_schema_version: Required[str]
    identity_version: Required[int]
    identity_version_id: Required[str]
    last_capture_at: Required[str | None]
    last_verified_at: Required[str | None]
    platform: Required[CaptureIdentityPlatform]
    provider_class: Required[CaptureProviderClass]
    revocation_snapshot_version: Required[str]
    revoked_at: Required[str | None]
    state: Required[CaptureIdentityState]
    trust_snapshot_version: Required[str]
    verifier_version: Required[str]


class CaptureIdentityEnrollmentRequest(TypedDict):
    platform: Required[CaptureIdentityPlatform]


class CaptureIdentityEnrollmentResponse(TypedDict):
    capture_identity_enrollment_id: Required[str]
    challenge_secret: Required[str]
    expires_at: Required[str]


class CaptureIdentityEnrollmentResult(TypedDict):
    capture_identity_id: Required[str]
    enrolled_at: Required[str]
    identity_version: Required[int]
    identity_version_id: Required[str]


type CaptureIdentityFilterState = Literal["active"] | Literal["revoked"]


class CaptureIdentityListResponse(TypedDict):
    items: Required[list[CaptureIdentitySummary]]
    next_cursor: Required[str | None]


type CaptureIdentityPlatform = Literal["ios"] | Literal["android"]


class CaptureIdentityRevocationResponse(TypedDict):
    capture_identity_id: Required[str]
    revocation_id: Required[str]
    revoked_at: Required[str]
    schema_version: NotRequired[Literal["op.capture-identity-revocation.v1"]]
    state: NotRequired[Literal["revoked"]]


type CaptureIdentityState = Literal["active"] | Literal["revoked"]


class CaptureIdentitySummary(TypedDict):
    capture_identity_id: Required[str]
    enrolled_at: Required[str]
    last_capture_at: Required[str | None]
    last_verified_at: Required[str | None]
    platform: Required[CaptureIdentityPlatform]
    provider_class: Required[CaptureProviderClass]
    revoked_at: Required[str | None]
    state: Required[CaptureIdentityState]


type CaptureManagementErrorCode = (
    Literal["CAPTURE_ENROLLMENT_NOT_FOUND"]
    | Literal["CAPTURE_CHALLENGE_NOT_FOUND"]
    | Literal["CAPTURE_IDENTITY_NOT_FOUND"]
    | Literal["CAPTURE_ADMISSION_NOT_FOUND"]
    | Literal["CAPTURE_ENROLLMENT_EXPIRED"]
    | Literal["CAPTURE_CHALLENGE_EXPIRED"]
    | Literal["CAPTURE_IDEMPOTENCY_IN_PROGRESS"]
    | Literal["CAPTURE_IDEMPOTENCY_CONFLICT"]
    | Literal["CAPTURE_ENROLLMENT_SECRET_ALREADY_ISSUED"]
    | Literal["CAPTURE_CHALLENGE_SECRET_ALREADY_ISSUED"]
    | Literal["CAPTURE_ENROLLMENT_REPLAY_CONFLICT"]
    | Literal["CAPTURE_ADMISSION_REPLAY_CONFLICT"]
    | Literal["CAPTURE_ENROLLMENT_REJECTED"]
    | Literal["CAPTURE_AUTHORITY_UNAVAILABLE"]
    | Literal["CAPTURE_CURSOR_INVALID"]
    | Literal["CAPTURE_VALIDATION_FAILED"]
)


class CaptureManagementErrorResponse(TypedDict):
    code: Required[CaptureManagementErrorCode]
    message: Required[str]
    request_id: Required[str]
    retryable: Required[bool]


type CaptureProviderClass = (
    Literal["apple_app_attest"]
    | Literal["google_play_integrity"]
    | Literal["android_key_attestation"]
    | Literal["other"]
)


class CawgIdentityBlock(TypedDict):
    credential_id: Required[str]
    type: Required[Literal["cawg_identity"]]


class CheckoutIntentRequest(TypedDict):
    amount_usd: NotRequired[float | str | None]
    cancel_url: Required[str]
    plan: NotRequired[BillingPlanId | None]
    purpose: NotRequired[Literal["subscription"] | Literal["wallet_top_up"]]
    success_url: Required[str]


class CloseShareRequest(TypedDict):
    state: Required[Literal["revoked"] | Literal["unpublished"]]


class CloseShareResponse(TypedDict):
    share_id: Required[str]
    state: Required[Literal["revoked"] | Literal["unpublished"]]


class ColorProfileFacts(TypedDict):
    byte_length: Required[int]
    sha256: Required[str]
    validated: NotRequired[Literal[True]]


class CommonErrorMeaningResponse(TypedDict):
    meaning: Required[str]
    retryable: Required[bool]
    status: Required[int]


class CompletePartRequest(TypedDict):
    etag: Required[str]
    part_number: Required[int]


class CompleteUploadRequest(TypedDict):
    parts: NotRequired[list[CompletePartRequest]]


class CompleteUploadResponse(TypedDict):
    asset_id: Required[str]
    asset_object_id: Required[str]
    byte_length: Required[int]
    sha256: Required[str]
    status: Required[UploadStatus]
    upload_id: Required[str]


class ComponentVersion(TypedDict):
    name: Required[str]
    version: Required[str]


class ConnectCatalogResponse(TypedDict):
    ai_actions: Required[list[AiActionResponse]]
    ai_prompt: Required[AiPromptResponse]
    api_reference_url: Required[str]
    authorization_header: Required[str]
    canonical_calls: Required[list[CanonicalCallResponse]]
    clients: Required[list[ConnectClientResponse]]
    common_errors: Required[list[CommonErrorMeaningResponse]]
    connection_modes: Required[list[ConnectModeResponse]]
    documentation_url: Required[str]
    environment_variables: Required[list[ConnectEnvironmentVariableResponse]]
    limits_and_cost: Required[LimitsCostGuidanceResponse]
    mcp_clients: Required[list[McpClientResponse]]
    mcp_feature_groups: Required[list[McpFeatureGroupResponse]]
    processing_modes: Required[list[str]]
    public_api_origin: Required[str]
    safety: Required[list[SafetyStatementResponse]]
    templates: Required[list[ConnectTemplateResponse]]
    version: Required[str]


class ConnectClientResponse(TypedDict):
    filename: Required[str]
    id: Required[str]
    install_template_id: Required[str]
    label: Required[str]
    language: Required[str | None]
    mode: Required[str]
    quickstart_template_id: Required[str]


class ConnectEnvironmentVariableResponse(TypedDict):
    default: Required[str | None]
    description: Required[str]
    name: Required[str]
    required: Required[bool]
    secret: Required[bool]


class ConnectModeResponse(TypedDict):
    description: Required[str]
    id: Required[str]
    label: Required[str]


type ConnectTemplatePartKind = Literal["literal"] | Literal["environment_variable"]


class ConnectTemplatePartResponse(TypedDict):
    kind: Required[ConnectTemplatePartKind]
    value: Required[str]


class ConnectTemplateResponse(TypedDict):
    id: Required[str]
    kind: Required[
        Literal["install_command"] | Literal["code"] | Literal["configuration"] | Literal["prompt"]
    ]
    media_type: Required[str]
    parts: Required[list[ConnectTemplatePartResponse]]


class ContractCapabilityResponse(TypedDict):
    api_version: Required[str]
    digest: Required[str]
    digest_algorithm: Required[Literal["sha256"]]


class CreateReportRequest(TypedDict):
    format: Required[ReportFormat]
    include_creator: NotRequired[bool]


class CreateShareRequest(TypedDict):
    expires_at: NotRequired[str | None]
    include_attribution: NotRequired[bool]


class CreateShareResponse(TypedDict):
    share_id: Required[str]
    token: Required[str | None]


class CreateUploadRequest(TypedDict):
    byte_length: Required[int]
    declared_media_type: Required[str]
    filename: NotRequired[str | None]
    mode: Required[UploadMode]
    parts: NotRequired[list[MultipartPartRequest]]
    sha256: Required[str]


class CreateUploadResponse(TypedDict):
    asset_id: Required[str]
    expires_at: Required[str]
    mode: Required[UploadMode]
    parts: NotRequired[list[PresignedPartResponse]]
    status: Required[UploadStatus]
    upload: NotRequired[PresignedRequestResponse | None]
    upload_id: Required[str]


class CreateVerificationRequest(TypedDict):
    manifest_object_id: NotRequired[str | None]
    object_id: Required[str]


class CreateWebhookEndpointRequest(TypedDict):
    auto_disable_after_failures: NotRequired[int]
    event_catalog_version: Required[CustomerEventCatalogVersion]
    events: Required[list[CustomerEventType]]
    max_concurrency: NotRequired[int]
    rate_limit_per_minute: NotRequired[int]
    url: Required[str]


class CreatorConsentRequest(TypedDict):
    captured_at: Required[str]
    captured_by: NotRequired[str | None]
    notice_version: Required[str]


class CreatorDisclosurePolicyRequest(TypedDict):
    brand_name: Required[str]
    console_disclosure: NotRequired[
        Literal["none"] | Literal["attributed"] | Literal["name"] | Literal["name_and_email"]
    ]
    notice_version: NotRequired[str | None]
    share_disclosure: NotRequired[Literal["none"] | Literal["attributed"] | Literal["name"]]


class CreatorDisclosurePolicyResponse(TypedDict):
    brand_name: Required[str]
    console_disclosure: Required[
        Literal["none"] | Literal["attributed"] | Literal["name"] | Literal["name_and_email"]
    ]
    notice_version: NotRequired[str | None]
    share_disclosure: Required[Literal["none"] | Literal["attributed"] | Literal["name"]]


class CreatorDisclosureResponse(TypedDict):
    assurance_level: Required[Literal["self_asserted"] | Literal["verified"]]
    assurance_statement: Required[str]
    audience: Required[Literal["operator"] | Literal["owning_tenant"] | Literal["public"]]
    commitment: NotRequired[dict[str, str] | None]
    creator_ref: NotRequired[str | None]
    disclosure_state: Required[
        Literal["disclosed"]
        | Literal["withheld"]
        | Literal["withdrawn"]
        | Literal["erased"]
        | Literal["unavailable"]
    ]
    end_user: NotRequired[dict[str, Any] | None]
    schema_version: Required[Literal["op.creator-disclosure.v1"]]
    tenant: Required[dict[str, Any]]


class CreatorIdentityCreateRequest(TypedDict):
    consent: Required[CreatorConsentRequest]
    email: Required[str]
    name: NotRequired[str | None]


class CreatorIdentityListResponse(TypedDict):
    items: Required[list[CreatorIdentityResponse]]
    next_cursor: NotRequired[str | None]


class CreatorIdentityResponse(TypedDict):
    assurance_level: Required[Literal["self_asserted"] | Literal["verified"]]
    created_at: Required[str]
    creator_id: Required[str]
    display_name_present: Required[bool]
    erased_at: NotRequired[str | None]
    status: Required[Literal["active"] | Literal["withdrawn"] | Literal["erased"]]
    withdrawn_at: NotRequired[str | None]


class CustomerEventCatalogResponse(TypedDict):
    catalog_version: Required[CustomerEventCatalogVersion]
    events: Required[list[CustomerEventDescriptorResponse]]
    wildcard_supported: NotRequired[Literal[False]]


type CustomerEventCatalogVersion = Literal["op.customer-events.v1"]


class CustomerEventDescriptorResponse(TypedDict):
    description: Required[str]
    event_type: Required[CustomerEventType]
    label: Required[str]


type CustomerEventType = Literal["asset.signed"] | Literal["asset.watermarked"]


class DbHealthResponse(TypedDict):
    status: Required[str]


type DeclaredCredentialsStatus = (
    Literal["valid"] | Literal["valid_untrusted"] | Literal["invalid"] | Literal["absent"]
)


class DeclaredOrigin(TypedDict):
    actions: Required[list[str]]
    ai_generated: Required[bool]
    claim_generator: Required[str | None]
    digital_source_type: Required[str | None]
    signed_at: Required[str | None]
    signed_by: Required[str | None]
    software_agent: Required[str | None]


class DeletionPageResponse(TypedDict):
    items: Required[list[DeletionResponse]]
    next_cursor: Required[str | None]


class DeletionRequestBody(TypedDict):
    asset_id: NotRequired[str | None]
    creator_id: NotRequired[str | None]
    scope: Required[Literal["asset"] | Literal["user_data"] | Literal["creator_identity"]]


class DeletionResponse(TypedDict):
    asset_id: NotRequired[str | None]
    completed_at: NotRequired[str | None]
    created_at: NotRequired[str | None]
    deletion_request_id: Required[str]
    scope: NotRequired[str | None]
    status: NotRequired[str | None]


class DeveloperOnboardingResponse(TypedDict):
    api_keys: Required[OnboardingApiKeysResponse]


type DigitalSourceType = (
    Literal["http://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia"]
    | Literal["http://cv.iptc.org/newscodes/digitalsourcetype/compositeWithTrainedAlgorithmicMedia"]
    | Literal["http://cv.iptc.org/newscodes/digitalsourcetype/compositeSynthetic"]
    | Literal["http://cv.iptc.org/newscodes/digitalsourcetype/humanEdits"]
    | Literal["http://c2pa.org/digitalsourcetype/empty"]
)


class DisclosureActor(TypedDict):
    id: Required[str]
    type: Required[Literal["api_key"] | Literal["user"]]


class DisclosureBadgeSet(TypedDict):
    id: Required[
        Literal["ai-generated"]
        | Literal["ai-manipulated"]
        | Literal["ai-interaction"]
        | Literal["ai-assisted"]
    ]
    label: Required[str]
    meaning: Required[str]
    variants: Required[list[Literal["brand-light"] | Literal["brand-dark"] | Literal["neutral"]]]


class DisclosureChainHead(TypedDict):
    hash: Required[str]
    sequence: Required[int]


class DisclosureEventBlock(TypedDict):
    jurisdiction: Required[
        Literal["EU"]
        | Literal["US-CA"]
        | Literal["US-ME"]
        | Literal["US-NH"]
        | Literal["US-NY"]
        | Literal["US-UT"]
        | Literal["IN"]
        | Literal["CN"]
        | Literal["KR"]
    ]
    kind: Required[DisclosureEventKind]
    type: Required[Literal["disclosure_event"]]


type DisclosureEventKind = (
    Literal["ai_interaction_notice"]
    | Literal["visible_label_offered"]
    | Literal["visible_label_applied"]
    | Literal["user_acknowledged"]
)


class DisclosureEventPage(TypedDict):
    chain_head: Required[DisclosureChainHead | None]
    data: Required[list[DisclosureEventRecord]]
    next_cursor: Required[str | None]


class DisclosureEventReceipt(TypedDict):
    event_id: Required[str]
    hash: Required[str]
    prev_hash: Required[str]
    received_at: Required[str]
    sequence: Required[int]


class DisclosureEventRecord(TypedDict):
    account_id: Required[str]
    actor: Required[DisclosureActor]
    client_time: Required[str]
    content_ref: Required[str | None]
    event_id: Required[str]
    hash: Required[str]
    jurisdiction: Required[
        Literal["EU"]
        | Literal["US-CA"]
        | Literal["US-ME"]
        | Literal["US-NH"]
        | Literal["US-NY"]
        | Literal["US-UT"]
        | Literal["IN"]
        | Literal["CN"]
        | Literal["KR"]
    ]
    kind: Required[DisclosureEventKind]
    locale: Required[str | None]
    origin: NotRequired[str | None]
    policy_version: Required[str]
    prev_hash: Required[str]
    received_at: Required[str]
    rule_id: Required[str | None]
    schema_version: Required[Literal["op.disclosure-event.v1"] | Literal["op.disclosure-event.v2"]]
    sequence: Required[int]
    subject_ref: Required[str]
    surface: Required[str | None]


class DisclosureEventRequest(TypedDict):
    client_time: Required[str]
    content_ref: NotRequired[str | None]
    jurisdiction: Required[
        Literal["EU"]
        | Literal["US-CA"]
        | Literal["US-ME"]
        | Literal["US-NH"]
        | Literal["US-NY"]
        | Literal["US-UT"]
        | Literal["IN"]
        | Literal["CN"]
        | Literal["KR"]
    ]
    kind: Required[DisclosureEventKind]
    locale: NotRequired[str | None]
    policy_version: Required[str]
    rule_id: NotRequired[str | None]
    subject_ref: Required[str]
    surface: NotRequired[
        Literal["web"]
        | Literal["app"]
        | Literal["voice"]
        | Literal["api"]
        | Literal["other"]
        | None
    ]


class DisclosureInstrument(TypedDict):
    applies_from: Required[str | None]
    citation: Required[str]
    id: Required[str]
    status: Required[
        Literal["in_force"]
        | Literal["enacted_not_in_force"]
        | Literal["amended"]
        | Literal["proposed"]
    ]
    title: Required[str]
    url: Required[str | None]


class DisclosureJurisdictionPolicy(TypedDict):
    id: Required[
        Literal["EU"]
        | Literal["US-CA"]
        | Literal["US-ME"]
        | Literal["US-NH"]
        | Literal["US-NY"]
        | Literal["US-UT"]
        | Literal["IN"]
        | Literal["CN"]
        | Literal["KR"]
    ]
    instruments: Required[list[DisclosureInstrument]]
    name: Required[str]
    rules: Required[list[DisclosureRule]]


class DisclosurePolicyDocument(TypedDict):
    badge_sets: Required[list[DisclosureBadgeSet]]
    disclaimer: Required[str]
    jurisdictions: Required[list[DisclosureJurisdictionPolicy]]
    needs_legal_review: Required[bool]
    policy_version: Required[str]
    published_at: Required[str]
    schema_version: Required[Literal["op.disclosure-policy.2026-10.v1"]]


class DisclosureRule(TypedDict):
    badge_set: Required[str | None]
    exceptions: Required[list[str]]
    form: Required[str]
    id: Required[str]
    instrument: Required[str]
    kind: Required[
        Literal["ai_interaction_notice"]
        | Literal["visible_label"]
        | Literal["deepfake_label"]
        | Literal["machine_readable_marking"]
    ]
    needs_legal_review: Required[bool]
    obligated_party: Required[
        Literal["provider"] | Literal["deployer"] | Literal["operator"] | Literal["platform"]
    ]
    provision: Required[str]
    texts: Required[list[DisclosureText]]
    timing: Required[
        Literal["before_first_interaction"]
        | Literal["at_first_interaction"]
        | Literal["on_display"]
        | Literal["on_publication"]
        | Literal["on_request"]
    ]
    trigger: Required[str]


class DisclosureText(TypedDict):
    locale: Required[str]
    text: Required[str]


class DownloadResponse(TypedDict):
    byte_length: Required[int]
    expires_at: Required[str]
    filename: Required[str]
    headers: Required[dict[str, str]]
    media_type: Required[
        Literal["application/epub+zip"]
        | Literal["application/onnx"]
        | Literal["application/oxps"]
        | Literal["application/pdf"]
        | Literal["application/vnd.oasis.opendocument.text"]
        | Literal["application/vnd.openxmlformats-officedocument.wordprocessingml.document"]
        | Literal["application/x-jax"]
        | Literal["application/x-keras"]
        | Literal["application/x-mlnet"]
        | Literal["application/x-mxnet"]
        | Literal["application/x-npy"]
        | Literal["application/x-openvino-ir+xml"]
        | Literal["application/x-openvino-weights"]
        | Literal["application/x-pickle"]
        | Literal["application/x-protobuf"]
        | Literal["application/x-pytorch"]
        | Literal["application/x-tensorflow"]
        | Literal["application/x-tensorflow-savedmodel"]
        | Literal["application/x-zip-based"]
        | Literal["application/xhtml+xml"]
        | Literal["application/xml"]
        | Literal["audio/MPA"]
        | Literal["audio/aac"]
        | Literal["audio/flac"]
        | Literal["audio/mp4"]
        | Literal["audio/mpeg"]
        | Literal["audio/wav"]
        | Literal["audio/x-riff-based"]
        | Literal["font/otf"]
        | Literal["image/avif"]
        | Literal["image/gif"]
        | Literal["image/heic"]
        | Literal["image/heic-sequence"]
        | Literal["image/heif"]
        | Literal["image/heif-sequence"]
        | Literal["image/jpeg"]
        | Literal["image/jxl"]
        | Literal["image/png"]
        | Literal["image/svg+xml"]
        | Literal["image/tiff"]
        | Literal["image/webp"]
        | Literal["image/x-adobe-dng"]
        | Literal["image/x-riff-based"]
        | Literal["image/x-tiff-based"]
        | Literal["text/html"]
        | Literal["text/plain"]
        | Literal["text/xml"]
        | Literal["video/mp4"]
        | Literal["video/quicktime"]
        | Literal["video/x-bmff-based"]
        | Literal["video/x-msvideo"]
        | Literal["video/x-riff-based"]
    ]
    method: Required[Literal["GET"]]
    sha256: Required[str]
    sidecar_manifest: NotRequired[SidecarManifestResponse | None]
    storage_version_sha256: Required[str]
    url: Required[str]


type EmbeddingPlacement = (
    Literal["jpeg_after_last_app0"]
    | Literal["png_before_first_idat"]
    | Literal["webp_riff_end"]
    | Literal["tiff_terminal_ifd"]
    | Literal["wav_riff_end"]
    | Literal["mp3_id3v2_geob"]
    | Literal["bmff_top_level_uuid"]
    | Literal["markdown_front_matter"]
    | Literal["gif_application_extension_after_color_table"]
    | Literal["jxl_container_top_level_jumb"]
    | Literal["svg_root_metadata"]
    | Literal["avi_riff_end"]
    | Literal["flac_leading_id3v2_geob"]
)


class EmbeddingPlan(TypedDict):
    maximum_fragments: Required[int]
    maximum_manifest_store_bytes: Required[int]
    placement: Required[EmbeddingPlacement]
    post_write_validation_required: NotRequired[Literal[True]]
    replace_existing_manifest: NotRequired[Literal[True]]
    source_remains_immutable: NotRequired[Literal[True]]
    write_new_output_object: NotRequired[Literal[True]]


class ErrorResponse(TypedDict):
    code: Required[ReasonCode]
    detail_code: NotRequired[ReasonCode | None]
    documentation_url: Required[str]
    field_details: Required[dict[str, str]]
    job_reference: NotRequired[str | None]
    message: Required[str]
    request_id: Required[str]
    retryable: Required[bool]


class ExportItemResponse(TypedDict):
    byte_length: Required[int | None]
    download_expires_at: NotRequired[str | None]
    download_url: NotRequired[str | None]
    resource_id: Required[str]
    resource_type: Required[str]
    sha256: Required[str | None]


class ExportMetadataResponse(TypedDict):
    expires_at: Required[str]
    export_id: Required[str]
    item_count: Required[int]
    kind: Required[str]
    manifest_sha256: Required[str | None]
    ready_at: Required[str | None]
    requested_at: Required[str]
    status: Required[str]
    total_bytes: Required[int]


class ExportPageResponse(TypedDict):
    items: Required[list[ExportMetadataResponse]]
    next_cursor: Required[str | None]


class ExportResponse(TypedDict):
    expires_at: Required[str]
    export_id: Required[str]
    filters: NotRequired[dict[str, Any] | None]
    item_count: Required[int]
    items: NotRequired[list[ExportItemResponse]]
    kind: Required[str]
    manifest: NotRequired[dict[str, Any] | None]
    manifest_sha256: Required[str | None]
    status: Required[str]
    total_bytes: Required[int]


class ExpressSignResponse(TypedDict):
    active_plan_revision: Required[int]
    asset_id: Required[str]
    cancel_requested_at: Required[str | None]
    download: Required[DownloadResponse | None]
    error_code: Required[str | None]
    fingerprint: NotRequired[bool | None]
    job_id: Required[str]
    media_inspection: Required[NormalizedInspectionFacts | None]
    policy_version: Required[str]
    progress: Required[JobProgressResponse]
    recipe_id: Required[str]
    recipe_version: Required[int]
    result: Required[JobResultResponse | None]
    state: Required[JobState]
    steps: Required[list[JobStepResponse]]
    terminal_at: Required[str | None]
    watermark: NotRequired[bool | None]


class FeedbackBody(TypedDict):
    category: NotRequired[str | None]
    contact_consented: NotRequired[bool]
    contexts: NotRequired[list[FeedbackContextBody]]
    message: Required[str]


class FeedbackContextBody(TypedDict):
    diagnostic_code: NotRequired[str | None]
    diagnostic_version: NotRequired[str | None]
    resource_id: Required[str]
    resource_type: Required[
        Literal["asset"]
        | Literal["job"]
        | Literal["publication"]
        | Literal["receipt"]
        | Literal["upload"]
    ]


class FeedbackResponse(TypedDict):
    feedback_id: Required[str]


class FingerprintAlgorithmResponse(TypedDict):
    algorithm_id: Required[str]
    default: Required[bool]
    display_name: Required[str]
    locked: Required[bool]
    soft_binding_registry_id: NotRequired[int | None]
    strength_note: Required[str]


class FingerprintBlock(TypedDict):
    algorithms: NotRequired[
        list[
            Literal["audfprint"]
            | Literal["chromaprint"]
            | Literal["dinov2"]
            | Literal["dinov2-lsh256"]
            | Literal["iscc-audio"]
            | Literal["iscc-image"]
            | Literal["pdq"]
            | Literal["tmk-pdqf"]
            | Literal["vpdq"]
        ]
        | None
    ]
    type: Required[Literal["fingerprint"]]


class GovernanceErrorResponse(TypedDict):
    code: Required[str]
    documentation_url: Required[str]
    field_details: Required[dict[str, str]]
    message: Required[str]
    request_id: Required[str]
    retryable: Required[bool]


class GovernanceReadinessResponse(TypedDict):
    capture_authority: Required[bool]
    commercial_authority: Required[bool]
    derived_index_reconciler: Required[bool]
    status: Required[str]


type HardBindingExclusionTarget = (
    Literal["jpeg_c2pa_app11"]
    | Literal["png_c2pa_cabx"]
    | Literal["webp_c2pa_chunk"]
    | Literal["tiff_c2pa_tag"]
    | Literal["wav_c2pa_chunk"]
    | Literal["mp3_c2pa_geob"]
    | Literal["bmff_c2pa_uuid"]
    | Literal["markdown_front_matter"]
    | Literal["gif_c2pa_application_extension"]
    | Literal["jxl_c2pa_jumb_box"]
    | Literal["svg_c2pa_manifest_text"]
    | Literal["avi_c2pa_chunk"]
    | Literal["flac_c2pa_geob"]
)


class HardBindingPlan(TypedDict):
    adapter_owns_exclusion_layout: NotRequired[Literal[True]]
    algorithm: NotRequired[Literal["sha256"]]
    assertion_label: NotRequired[Literal["c2pa.hash.data"] | Literal["c2pa.hash.bmff"]]
    compute_after_last_byte_change: NotRequired[Literal[True]]
    exclusion_target: Required[HardBindingExclusionTarget]
    existing_exclusion_ranges: NotRequired[list[ByteRange]]


class HealthResponse(TypedDict):
    service: Required[str]
    source_revision: Required[str]
    status: Required[str]


type HistoryMediaType = (
    Literal["image/jpeg"]
    | Literal["image/png"]
    | Literal["image/webp"]
    | Literal["image/tiff"]
    | Literal["image/avif"]
    | Literal["image/gif"]
    | Literal["image/jxl"]
    | Literal["image/svg+xml"]
    | Literal["image/x-adobe-dng"]
    | Literal["image/heic"]
    | Literal["image/heif"]
    | Literal["image/heic-sequence"]
    | Literal["image/heif-sequence"]
    | Literal["audio/wav"]
    | Literal["audio/mpeg"]
    | Literal["audio/mp4"]
    | Literal["audio/flac"]
    | Literal["video/mp4"]
    | Literal["video/quicktime"]
    | Literal["video/x-msvideo"]
    | Literal["text/markdown"]
    | Literal["font/otf"]
    | Literal["application/x-npy"]
    | Literal["application/onnx"]
    | Literal["application/x-pytorch"]
    | Literal["application/x-pickle"]
    | Literal["application/x-tensorflow"]
    | Literal["application/x-tensorflow-savedmodel"]
    | Literal["application/x-protobuf"]
    | Literal["application/x-keras"]
    | Literal["application/x-jax"]
    | Literal["application/x-mxnet"]
    | Literal["application/x-mlnet"]
    | Literal["application/x-openvino-ir+xml"]
    | Literal["application/x-openvino-weights"]
    | Literal["application/pdf"]
    | Literal["application/epub+zip"]
    | Literal["application/vnd.openxmlformats-officedocument.wordprocessingml.document"]
    | Literal["application/vnd.oasis.opendocument.text"]
    | Literal["application/oxps"]
    | Literal["application/x-zip-based"]
    | Literal["text/plain"]
    | Literal["text/html"]
    | Literal["text/xml"]
    | Literal["application/xml"]
    | Literal["application/xhtml+xml"]
    | Literal["audio/aac"]
    | Literal["audio/MPA"]
    | Literal["audio/x-riff-based"]
    | Literal["image/x-tiff-based"]
    | Literal["image/x-riff-based"]
    | Literal["video/x-bmff-based"]
    | Literal["video/x-riff-based"]
    | Literal["application/c2pa"]
)


class HttpErrorResponse(TypedDict):
    detail: Required[str]


class HTTPValidationError(TypedDict):
    detail: NotRequired[list[ValidationError]]


type IdentityCredentialKind = Literal["individual"] | Literal["organisation"]


class IdentityCredentialListResponse(TypedDict):
    cawg_available: Required[bool]
    data: Required[list[IdentityCredentialResponse]]
    unavailable_reason: Required[str | None]


class IdentityCredentialResponse(TypedDict):
    credential_id: Required[str]
    enrolled_at: Required[str]
    kind: Required[IdentityCredentialKind]
    not_after: Required[str]
    not_before: Required[str]
    status: Required[IdentityCredentialStatus]
    subject_name: Required[str]


type IdentityCredentialStatus = (
    Literal["pending"]
    | Literal["active"]
    | Literal["suspended"]
    | Literal["revoked"]
    | Literal["expired"]
)


class ImageProfileListResponse(TypedDict):
    profiles: Required[list[ImageProfileResponse]]


class ImageProfileResponse(TypedDict):
    accepted_auxiliaries: Required[list[str]]
    accepted_bit_depths: Required[list[int]]
    availability: Required[
        Literal["unreviewed"] | Literal["reviewed_unavailable"] | Literal["available"]
    ]
    color_class: Required[Literal["sdr"] | Literal["hdr"]]
    limits_are_provisional: Required[bool]
    max_compressed_bytes: Required[int]
    max_height: Required[int]
    max_pixels: Required[int]
    max_width: Required[int]
    media_format: Required[str]
    planned_auxiliaries: Required[list[str]]
    planned_bit_depths: Required[list[int]]
    profile_id: Required[str]
    profile_version: Required[str]
    recipes: Required[list[str]]
    unavailable_reason: Required[str]


class IssuedApiKeyResponse(TypedDict):
    created_at: Required[str]
    display_hint: Required[str]
    expires_at: Required[str | None]
    id: Required[str]
    last_used_at: Required[str | None]
    name: Required[str | None]
    restrictions: NotRequired[ApiKeyRestrictionsView | None]
    revoked_at: Required[str | None]
    rotated_from_id: Required[str | None]
    rotation: NotRequired[ApiKeyRotationResponse | None]
    scopes: Required[list[str]]
    secret: Required[str]
    status: Required[ApiKeyStatus]


class IssuedWebhookEndpointResponse(TypedDict):
    endpoint: Required[WebhookEndpointResponse]
    secret: Required[str]


class JobHistoryPageResponse(TypedDict):
    items: Required[list[JobHistoryResponse]]
    next_cursor: Required[str | None]


class JobHistoryResponse(TypedDict):
    asset_id: Required[str]
    attempt_count: Required[int]
    canceled_steps: Required[int]
    created_at: Required[str]
    error_code: Required[str | None]
    failed_steps: Required[int]
    job_id: Required[str]
    job_url: Required[str]
    kind: Required[JobKind]
    progress_percent: Required[int]
    receipt_url: Required[str | None]
    recipe_id: Required[str]
    recipe_version: Required[int]
    state: Required[JobState]
    succeeded_steps: Required[int]
    total_steps: Required[int]
    updated_at: Required[str]
    verification_url: Required[str | None]


type JobKind = (
    Literal["sign"] | Literal["watermark"] | Literal["watermark_then_sign"] | Literal["capture"]
)


class JobProgressResponse(TypedDict):
    canceled_steps: Required[int]
    failed_steps: Required[int]
    percent: Required[int]
    succeeded_steps: Required[int]
    total_steps: Required[int]


class JobResponse(TypedDict):
    active_plan_revision: Required[int]
    asset_id: Required[str]
    cancel_requested_at: Required[str | None]
    error_code: Required[str | None]
    fingerprint: NotRequired[bool | None]
    job_id: Required[str]
    media_inspection: Required[NormalizedInspectionFacts | None]
    policy_version: Required[str]
    progress: Required[JobProgressResponse]
    recipe_id: Required[str]
    recipe_version: Required[int]
    result: Required[JobResultResponse | None]
    state: Required[JobState]
    steps: Required[list[JobStepResponse]]
    terminal_at: Required[str | None]
    watermark: NotRequired[bool | None]


class JobResultResponse(TypedDict):
    asset_id: Required[str]
    publication_id: Required[str]
    receipt_id: Required[str]
    verification_id: Required[str]


type JobState = (
    Literal["accepted"]
    | Literal["queued"]
    | Literal["running"]
    | Literal["cancel_requested"]
    | Literal["completed"]
    | Literal["canceled"]
    | Literal["expired"]
    | Literal["rejected"]
    | Literal["failed"]
)


class JobStepResponse(TypedDict):
    attempt_count: Required[int]
    last_error_code: Required[str | None]
    max_attempts: Required[int]
    next_attempt_at: Required[str | None]
    plan_revision: Required[int]
    reconciliation_required: NotRequired[bool]
    state: Required[JobStepState]
    step_id: Required[str]
    step_key: Required[str]
    step_type: Required[str]


type JobStepState = (
    Literal["pending"]
    | Literal["ready"]
    | Literal["leased"]
    | Literal["running"]
    | Literal["succeeded"]
    | Literal["retry_wait"]
    | Literal["reconcile_wait"]
    | Literal["canceled"]
    | Literal["failed"]
)


class LegacyReceiptValidationResponse(TypedDict):
    outcome: Required[Literal["valid"]]
    request_sha256: Required[str]
    result_sha256: Required[str]
    revocation_snapshot_id: Required[str]
    trust_snapshot_id: Required[str]
    validated_at: Required[str]
    verification_id: Required[str]


class LegacySigningReceiptEvidenceResponse(TypedDict):
    asset_id: Required[str]
    job_id: Required[str]
    manifest: Required[ReceiptManifestResponse]
    output: Required[ReceiptOutputResponse]
    prior_provenance: Required[ReceiptPriorProvenanceResponse]
    product: Required[ReceiptProductResponse]
    published_at: Required[str]
    schema_version: Required[Literal["op.signing-receipt.v1"]]
    signing: Required[ReceiptSigningResponse]
    validation: Required[LegacyReceiptValidationResponse]


class LegalHoldResponse(TypedDict):
    created_at: Required[str]
    legal_hold_id: Required[str]
    reason: Required[str | None]
    released_at: Required[str | None]
    scope: Required[str]
    status: Required[str]
    target_id: Required[str | None]


class LimitsCostGuidanceResponse(TypedDict):
    text: Required[str]
    usage_path: Required[str]


class MadeWith(TypedDict):
    answer: Required[MadeWithAnswer]
    method: Required[MadeWithMethod | None]
    provider_name: Required[str]
    recovery_checked: Required[bool]


type MadeWithAnswer = Literal["yes"] | Literal["no_record"]

type MadeWithMethod = Literal["c2pa_manifest"] | Literal["watermark"] | Literal["fingerprint"]

type ManifestContainer = (
    Literal["jpeg_app11"]
    | Literal["png_cabx"]
    | Literal["riff_c2pa_chunk"]
    | Literal["tiff_tag_52545"]
    | Literal["wav_c2pa_chunk"]
    | Literal["mp3_id3_geob"]
    | Literal["bmff_c2pa_uuid"]
    | Literal["markdown_front_matter"]
    | Literal["gif_c2pa_application_extension"]
    | Literal["jxl_jumb_box"]
    | Literal["svg_c2pa_metadata"]
    | Literal["avi_riff_c2pa_chunk"]
    | Literal["flac_id3_geob"]
)

type ManifestStoreState = Literal["absent"] | Literal["present"]


class MarkingCheckItemRequest(TypedDict):
    asset_id: NotRequired[str | None]
    object_id: NotRequired[str | None]


class MarkingCheckItemResult(TypedDict):
    asset_id: Required[str | None]
    failure_reason: Required[ReasonCode | None]
    index: Required[int]
    object_id: Required[str | None]
    outcome: Required[Literal["pass"] | Literal["fail"] | Literal["pending"] | Literal["error"]]
    requirements: Required[list[MarkingRequirementResult]]
    verification_id: Required[str | None]


class MarkingCheckRequest(TypedDict):
    items: Required[list[MarkingCheckItemRequest]]
    preset: Required[
        Literal["c2pa_baseline"]
        | Literal["eu_ai_act_art50"]
        | Literal["us_ca_sb942"]
        | Literal["cn_labeling_measures"]
        | Literal["kr_ai_framework_act"]
        | Literal["in_synthetic_information"]
    ]


class MarkingCheckResponse(TypedDict):
    completed_at: Required[str | None]
    created_at: Required[str]
    items: Required[list[MarkingCheckItemResult]]
    marking_check_id: Required[str]
    preset: Required[
        Literal["c2pa_baseline"]
        | Literal["eu_ai_act_art50"]
        | Literal["us_ca_sb942"]
        | Literal["cn_labeling_measures"]
        | Literal["kr_ai_framework_act"]
        | Literal["in_synthetic_information"]
    ]
    state: Required[
        Literal["accepted"] | Literal["running"] | Literal["completed"] | Literal["failed"]
    ]
    statement: Required[str]
    summary: Required[MarkingCheckSummary]


class MarkingCheckSummary(TypedDict):
    errored: Required[int]
    failed: Required[int]
    passed: Required[int]
    pending: Required[int]


type MarkingRequirement = (
    Literal["c2pa_manifest"]
    | Literal["ai_declaration"]
    | Literal["recoverable_watermark"]
    | Literal["recoverable_fingerprint"]
    | Literal["machine_readable_ai_marking"]
)


class MarkingRequirementResult(TypedDict):
    detail: Required[str]
    evidence: NotRequired[Literal["recovered"] | Literal["recorded"] | None]
    level: Required[RequirementLevel]
    outcome: Required[
        Literal["pass"] | Literal["fail"] | Literal["pending"] | Literal["not_checked"]
    ]
    requirement: Required[MarkingRequirement]


class McpClientResponse(TypedDict):
    configuration_template_id: Required[str]
    filename: Required[str]
    id: Required[str]
    label: Required[str]


class McpFeatureGroupResponse(TypedDict):
    id: Required[str]
    label: Required[str]
    read_only_scopes: Required[list[str]]
    scopes: Required[list[str]]


class MediaAdapterPin(TypedDict):
    contract_version: Required[int]
    name: Required[str]
    version: Required[str]


class MediaCapabilityResponse(TypedDict):
    availability: Required[CapabilityAvailabilityResponse]
    codec: Required[str]
    container: Required[str]
    fingerprint_algorithms: NotRequired[list[FingerprintAlgorithmResponse]]
    media_type: Required[
        Literal["application/epub+zip"]
        | Literal["application/onnx"]
        | Literal["application/oxps"]
        | Literal["application/pdf"]
        | Literal["application/vnd.oasis.opendocument.text"]
        | Literal["application/vnd.openxmlformats-officedocument.wordprocessingml.document"]
        | Literal["application/x-jax"]
        | Literal["application/x-keras"]
        | Literal["application/x-mlnet"]
        | Literal["application/x-mxnet"]
        | Literal["application/x-npy"]
        | Literal["application/x-openvino-ir+xml"]
        | Literal["application/x-openvino-weights"]
        | Literal["application/x-pickle"]
        | Literal["application/x-protobuf"]
        | Literal["application/x-pytorch"]
        | Literal["application/x-tensorflow"]
        | Literal["application/x-tensorflow-savedmodel"]
        | Literal["application/x-zip-based"]
        | Literal["application/xhtml+xml"]
        | Literal["application/xml"]
        | Literal["audio/MPA"]
        | Literal["audio/aac"]
        | Literal["audio/flac"]
        | Literal["audio/mp4"]
        | Literal["audio/mpeg"]
        | Literal["audio/wav"]
        | Literal["audio/x-riff-based"]
        | Literal["font/otf"]
        | Literal["image/avif"]
        | Literal["image/gif"]
        | Literal["image/heic"]
        | Literal["image/heic-sequence"]
        | Literal["image/heif"]
        | Literal["image/heif-sequence"]
        | Literal["image/jpeg"]
        | Literal["image/jxl"]
        | Literal["image/png"]
        | Literal["image/svg+xml"]
        | Literal["image/tiff"]
        | Literal["image/webp"]
        | Literal["image/x-adobe-dng"]
        | Literal["image/x-riff-based"]
        | Literal["image/x-tiff-based"]
        | Literal["text/html"]
        | Literal["text/plain"]
        | Literal["text/xml"]
        | Literal["video/mp4"]
        | Literal["video/quicktime"]
        | Literal["video/x-bmff-based"]
        | Literal["video/x-msvideo"]
        | Literal["video/x-riff-based"]
    ]
    processing: Required[ProcessingLimitsResponse]
    upload: Required[UploadLimitsResponse]
    watermark_algorithms: NotRequired[list[WatermarkAlgorithmResponse]]


class MeResponse(TypedDict):
    email: Required[str]
    public_id: Required[str]


class MetadataFact(TypedDict):
    byte_length: Required[int]
    count: Required[int]
    kind: Required[MetadataKind]


type MetadataKind = (
    Literal["exif"]
    | Literal["xmp"]
    | Literal["icc"]
    | Literal["text"]
    | Literal["comment"]
    | Literal["riff"]
    | Literal["id3"]
    | Literal["bmff"]
    | Literal["other"]
)


class MeterQuotaResponse(TypedDict):
    available: Required[str]
    carried_reserved: Required[str]
    hard_limit: Required[str]
    meter_type: Required[str]
    meter_version: Required[int]
    period_reserved: Required[str]
    reserved: Required[str]
    used: Required[str]


class MultipartPartRequest(TypedDict):
    byte_length: Required[int]
    part_number: Required[int]
    sha256: Required[str]


class NormalizedAudioFacts(TypedDict):
    adapter: Required[MediaAdapterPin]
    audio: Required[AudioTrackFacts]
    byte_length: Required[int]
    container_element_count: Required[int]
    decoder_components: Required[list[ComponentVersion]]
    duration_microseconds: Required[int]
    embedding: Required[EmbeddingPlan]
    encrypted: NotRequired[Literal[False]]
    full_decode_succeeded: NotRequired[Literal[True]]
    hard_binding: Required[HardBindingPlan]
    manifest_store: Required[OpaqueManifestStoreFacts]
    maximum_box_depth: NotRequired[int | None]
    media_format: Required[Literal["audio/mp4"] | Literal["audio/mpeg"] | Literal["audio/wav"]]
    metadata: NotRequired[list[MetadataFact]]
    metadata_total_bytes: Required[int]
    schema_version: NotRequired[Literal["op.media-inspection.audio.v1"]]
    sha256: Required[str]
    source_reference: Required[str]
    track_count: NotRequired[Literal[1]]


type NormalizedInspectionFacts = NormalizedMediaFacts | NormalizedAudioFacts | NormalizedVideoFacts


class NormalizedMediaFacts(TypedDict):
    adapter: Required[MediaAdapterPin]
    bits_per_channel: Required[int]
    byte_length: Required[int]
    channels: Required[int]
    color_mode: Required[str]
    color_profile: NotRequired[ColorProfileFacts | None]
    container_element_count: Required[int]
    decoded_byte_length: Required[int]
    decoder: Required[ComponentVersion]
    embedding: Required[EmbeddingPlan]
    frame_count: Required[int]
    full_decode_succeeded: NotRequired[Literal[True]]
    hard_binding: Required[HardBindingPlan]
    height: Required[int]
    manifest_store: Required[OpaqueManifestStoreFacts]
    media_format: Required[
        Literal["image/avif"]
        | Literal["image/jpeg"]
        | Literal["image/png"]
        | Literal["image/tiff"]
        | Literal["image/webp"]
    ]
    metadata: NotRequired[list[MetadataFact]]
    metadata_total_bytes: Required[int]
    pixel_count: Required[int]
    schema_version: NotRequired[Literal["op.media-inspection.v1"]]
    sha256: Required[str]
    source_reference: Required[str]
    width: Required[int]


class NormalizedVideoFacts(TypedDict):
    adapter: Required[MediaAdapterPin]
    audio: NotRequired[AudioTrackFacts | None]
    byte_length: Required[int]
    container_element_count: Required[int]
    decoder_components: Required[list[ComponentVersion]]
    duration_microseconds: Required[int]
    embedding: Required[EmbeddingPlan]
    encrypted: NotRequired[Literal[False]]
    fragmented: NotRequired[Literal[False]]
    full_decode_succeeded: NotRequired[Literal[True]]
    hard_binding: Required[HardBindingPlan]
    manifest_store: Required[OpaqueManifestStoreFacts]
    maximum_box_depth: Required[int]
    media_format: NotRequired[Literal["video/mp4"]]
    metadata: NotRequired[list[MetadataFact]]
    metadata_total_bytes: Required[int]
    schema_version: NotRequired[Literal["op.media-inspection.video.v1"]]
    sha256: Required[str]
    source_reference: Required[str]
    track_count: Required[int]
    video: Required[VideoTrackFacts]


class OnboardingApiKeysResponse(TypedDict):
    active_count: Required[int]
    request_observation: Required[RequestObservationResponse]


class OpaqueManifestStoreFacts(TypedDict):
    byte_length: NotRequired[int]
    container: NotRequired[ManifestContainer | None]
    fragment_count: NotRequired[int]
    jumbf_box_count: NotRequired[int]
    maximum_depth: NotRequired[int]
    ranges: NotRequired[list[ByteRange]]
    sha256: NotRequired[str | None]
    state: Required[ManifestStoreState]
    trust_evaluated: NotRequired[Literal[False]]


class OverviewActivityBucketResponse(TypedDict):
    bucket_end: Required[str]
    bucket_start: Required[str]
    signing: Required[int]
    verifications: Required[int]


class OverviewAttentionResponse(TypedDict):
    count: Required[int]
    kind: Required[
        Literal["governance_deletions_active"]
        | Literal["governance_deletions_blocked"]
        | Literal["governance_exports_active"]
        | Literal["jobs_failed"]
        | Literal["jobs_rejected"]
        | Literal["queue_backlog_aging"]
        | Literal["quota_exhausted"]
        | Literal["webhook_deliveries_failing"]
    ]
    oldest_at: NotRequired[str | None]
    severity: Required[Literal["critical"] | Literal["warning"] | Literal["info"]]
    target_filters: Required[dict[str, str]]
    target_resource: Required[
        Literal["governance_deletions"]
        | Literal["governance_exports"]
        | Literal["jobs"]
        | Literal["quota"]
        | Literal["webhook_endpoints"]
    ]


class OverviewComparisonResponse(TypedDict):
    failed_jobs: Required[int]
    jobs_total: Required[int]
    range_end: Required[str]
    range_start: Required[str]
    signing: Required[int]
    terminal_latency_average_ms: NotRequired[int | None]
    verifications: Required[int]


class OverviewFreshnessResponse(TypedDict):
    historical_rollups_as_of: Required[str | None]
    pending_rebuild_bucket_count: Required[int]
    recent_authoritative_as_of: Required[str]


class OverviewGovernanceResponse(TypedDict):
    current_deletion_requests: Required[dict[str, int]]
    current_exports: Required[dict[str, int]]
    range_deletion_requests: Required[dict[str, int]]
    range_exports: Required[dict[str, int]]


class OverviewHealthResponse(TypedDict):
    failed_jobs: Required[int]
    oldest_queued_at: Required[str | None]
    queue_by_state: Required[dict[str, int]]
    terminal_latency_average_ms: Required[int | None]
    terminal_latency_max_ms: Required[int | None]


class OverviewJobMetricsResponse(TypedDict):
    by_kind: Required[dict[str, int]]
    by_state: Required[dict[str, int]]
    signing: Required[int]
    total: Required[int]


class OverviewQuotaMeterResponse(TypedDict):
    available: Required[str]
    hard_limit: Required[str]
    meter_type: Required[str]
    meter_version: Required[int]
    reserved: Required[str]
    used: Required[str]


class OverviewQuotaResponse(TypedDict):
    meters: Required[list[OverviewQuotaMeterResponse]]
    period: Required[str | None]


class OverviewResponse(TypedDict):
    activity: Required[list[OverviewActivityBucketResponse]]
    as_of: Required[str]
    attention: Required[list[OverviewAttentionResponse]]
    comparison: Required[OverviewComparisonResponse | None]
    freshness: Required[OverviewFreshnessResponse]
    governance: Required[OverviewGovernanceResponse]
    health: Required[OverviewHealthResponse]
    jobs: Required[OverviewJobMetricsResponse]
    media_kinds: Required[dict[str, int]]
    quota: Required[OverviewQuotaResponse]
    range: Required[Literal["7d"] | Literal["30d"] | Literal["12m"]]
    range_end: Required[str]
    range_start: Required[str]
    unavailable: Required[list[OverviewUnavailableResponse]]
    verification_outcomes: Required[dict[str, int]]
    webhooks: Required[OverviewWebhookResponse]


class OverviewUnavailableResponse(TypedDict):
    affected_from: NotRequired[str | None]
    affected_to: NotRequired[str | None]
    component: Required[Literal["historical_rollups"] | Literal["comparison"] | Literal["quota"]]
    reason: Required[Literal["pending_rebuild"] | Literal["not_provisioned"]]
    retryable: Required[bool]


class OverviewWebhookResponse(TypedDict):
    deliveries_by_state: Required[dict[str, int]]
    endpoints_by_state: Required[dict[str, int]]


class PortalIntentRequest(TypedDict):
    return_url: Required[str]


class PresignedPartResponse(TypedDict):
    headers: Required[dict[str, str]]
    method: Required[Literal["PUT"]]
    part_number: Required[int]
    url: Required[str]


class PresignedRequestResponse(TypedDict):
    headers: Required[dict[str, str]]
    method: Required[Literal["PUT"]]
    url: Required[str]


class PreviewResponse(TypedDict):
    byte_length: Required[int]
    expires_at: Required[str]
    headers: Required[dict[str, str]]
    height: Required[int]
    media_type: Required[Literal["image/jpeg"]]
    method: Required[Literal["GET"]]
    sha256: Required[str]
    url: Required[str]
    width: Required[int]


class PricingLineResponse(TypedDict):
    action: Required[str]
    amount_usd: Required[str]
    quantity: Required[str]
    unit: Required[str]
    unit_price_usd: Required[str]


class PricingQuoteRequest(TypedDict):
    duration_seconds: NotRequired[float | str | None]
    fingerprint: NotRequired[bool | None]
    frames_per_second: NotRequired[float | str | None]
    height: NotRequired[int | None]
    media_family: Required[
        Literal["image"]
        | Literal["audio"]
        | Literal["video"]
        | Literal["document"]
        | Literal["text"]
        | Literal["model"]
        | Literal["live"]
    ]
    operation: Required[Literal["sign"] | Literal["watermark"] | Literal["watermark_then_sign"]]
    width: NotRequired[int | None]


class PricingQuoteResponse(TypedDict):
    currency: NotRequired[Literal["USD"]]
    estimate_only: NotRequired[Literal[True]]
    excludes: NotRequired[list[str]]
    final_facts_source: NotRequired[Literal["server_validated_media_inspection"]]
    lines: Required[list[PricingLineResponse]]
    pricing_version: Required[str]
    total_usd: Required[str]


class PricingResponse(TypedDict):
    activation: NotRequired[Literal["requires_explicit_tenant_enrollment"]]
    currency: NotRequired[Literal["USD"]]
    pricing_version: Required[str]
    processing_credits_included: NotRequired[Literal[False]]
    rates: Required[dict[str, Any]]


class ProcessingChargeResponse(TypedDict):
    action: Required[str]
    amount_usd: Required[str]
    api_key_id: Required[str | None]
    created_at: Required[str]
    id: Required[str]
    job_id: Required[str]
    pricing_version: Required[str]
    quantity: Required[str]
    service_period_end: Required[str]
    service_period_start: Required[str]
    unit: Required[str]
    unit_price_usd: Required[str]


class ProcessingChargesResponse(TypedDict):
    currency: NotRequired[Literal["USD"]]
    items: Required[list[ProcessingChargeResponse]]
    next_before: Required[str | None]
    provider_charge_created: NotRequired[Literal[False]]


class ProcessingLimitsResponse(TypedDict):
    maximum_duration_seconds: NotRequired[int | None]
    maximum_height: NotRequired[int | None]
    maximum_pixels: NotRequired[int | None]
    maximum_width: NotRequired[int | None]


class PublicationResponse(TypedDict):
    byte_length: Required[int]
    job_id: Required[str]
    media_type: Required[
        Literal["application/epub+zip"]
        | Literal["application/onnx"]
        | Literal["application/oxps"]
        | Literal["application/pdf"]
        | Literal["application/vnd.oasis.opendocument.text"]
        | Literal["application/vnd.openxmlformats-officedocument.wordprocessingml.document"]
        | Literal["application/x-jax"]
        | Literal["application/x-keras"]
        | Literal["application/x-mlnet"]
        | Literal["application/x-mxnet"]
        | Literal["application/x-npy"]
        | Literal["application/x-openvino-ir+xml"]
        | Literal["application/x-openvino-weights"]
        | Literal["application/x-pickle"]
        | Literal["application/x-protobuf"]
        | Literal["application/x-pytorch"]
        | Literal["application/x-tensorflow"]
        | Literal["application/x-tensorflow-savedmodel"]
        | Literal["application/x-zip-based"]
        | Literal["application/xhtml+xml"]
        | Literal["application/xml"]
        | Literal["audio/MPA"]
        | Literal["audio/aac"]
        | Literal["audio/flac"]
        | Literal["audio/mp4"]
        | Literal["audio/mpeg"]
        | Literal["audio/wav"]
        | Literal["audio/x-riff-based"]
        | Literal["font/otf"]
        | Literal["image/avif"]
        | Literal["image/gif"]
        | Literal["image/heic"]
        | Literal["image/heic-sequence"]
        | Literal["image/heif"]
        | Literal["image/heif-sequence"]
        | Literal["image/jpeg"]
        | Literal["image/jxl"]
        | Literal["image/png"]
        | Literal["image/svg+xml"]
        | Literal["image/tiff"]
        | Literal["image/webp"]
        | Literal["image/x-adobe-dng"]
        | Literal["image/x-riff-based"]
        | Literal["image/x-tiff-based"]
        | Literal["text/html"]
        | Literal["text/plain"]
        | Literal["text/xml"]
        | Literal["video/mp4"]
        | Literal["video/quicktime"]
        | Literal["video/x-bmff-based"]
        | Literal["video/x-msvideo"]
        | Literal["video/x-riff-based"]
    ]
    publication_id: Required[str]
    published_at: Required[str]
    receipt_id: Required[str]
    sha256: Required[str]
    verification_id: Required[str]


type PublicCaptureAdmissionReason = (
    Literal["passed"]
    | Literal["capture_identity_revoked"]
    | Literal["capture_identity_conflict"]
    | Literal["evidence_unavailable"]
    | Literal["evidence_invalid"]
    | Literal["app_identity_mismatch"]
    | Literal["app_downgrade"]
    | Literal["os_downgrade"]
    | Literal["security_level"]
    | Literal["boot_state"]
    | Literal["counter_replay"]
    | Literal["clock_rollback"]
    | Literal["reinstall_restore"]
    | Literal["request_mismatch"]
    | Literal["media_substitution"]
    | Literal["governance_rejected"]
    | Literal["asset_closed"]
    | Literal["commercial_rejected"]
    | Literal["capture_work_conflict"]
    | Literal["capture_work_unavailable"]
)


class PublicCheckPage(TypedDict):
    display_name: Required[str]
    slug: Required[str]


class PublicCheckResponse(TypedDict):
    check_id: Required[str]
    completed_at: Required[str | None]
    content_credentials: Required[PublicContentCredentials | None]
    created_at: Required[str]
    failure_reason: Required[ReasonCode | None]
    made_with: Required[MadeWith | None]
    media_type: Required[str | None]
    page: Required[PublicCheckPage]
    schema_version: Required[Literal["op.public-check.v1"]]
    state: Required[Literal["running"] | Literal["completed"] | Literal["failed"]]
    statement: Required[str]


class PublicContentCredentials(TypedDict):
    declared_origin: Required[DeclaredOrigin | None]
    status: Required[DeclaredCredentialsStatus]


type PublicRecipeCapability = (
    Literal["watermark"] | Literal["fingerprint"] | Literal["c2pa_signing"]
)


class PublicVerifyPageResponse(TypedDict):
    accepted_media_types: NotRequired[list[str] | None]
    check_url: Required[str]
    colours: Required[VerifyPageColours]
    display_name: Required[str]
    logo_url: Required[str | None]
    max_upload_bytes: Required[int]
    recover_own_assets: Required[bool]
    schema_version: Required[Literal["op.public-verify-page.v1"]]
    slug: Required[str]
    statement: Required[str]


class ReadinessResponse(TypedDict):
    status: Required[str]


type ReasonCode = (
    Literal["AI_DECLARATION_REQUIRES_SIGN_ONLY"]
    | Literal["API_KEY_IP_ALLOWLIST_UNAVAILABLE"]
    | Literal["API_KEY_IP_NOT_ALLOWED"]
    | Literal["API_KEY_ORIGIN_NOT_ALLOWED"]
    | Literal["API_KEY_PROFILE_FORBIDS"]
    | Literal["API_KEY_RATE_LIMITED"]
    | Literal["ASSET_DETAIL_UNAVAILABLE"]
    | Literal["ASSET_DOWNLOAD_UNAVAILABLE"]
    | Literal["ASSET_NOT_FOUND"]
    | Literal["ASSET_NOT_PUBLISHED"]
    | Literal["ASSET_PREVIEW_DERIVATIVE_MISSING"]
    | Literal["ASSET_PREVIEW_GENERATION_FAILED"]
    | Literal["ASSET_PREVIEW_PENDING"]
    | Literal["ASSET_PREVIEW_REDEMPTION_REFUSED"]
    | Literal["ASSET_PREVIEW_RESTRICTED"]
    | Literal["ASSET_PREVIEW_STORAGE_UNAVAILABLE"]
    | Literal["ASSET_PREVIEW_UNSUPPORTED_MEDIA"]
    | Literal["BILLING_ACCOUNT_SUSPENDED"]
    | Literal["BILLING_ACCOUNT_UNAVAILABLE"]
    | Literal["BILLING_INTENT_RATE_LIMITED"]
    | Literal["BILLING_QUOTA_EXCEEDED"]
    | Literal["BINDING_ACTIVATION_FAILED"]
    | Literal["BINDING_EVIDENCE_CONFLICT"]
    | Literal["BINDING_LOOKUP_AMBIGUOUS"]
    | Literal["BINDING_LOOKUP_FORBIDDEN"]
    | Literal["BINDING_LOOKUP_INDETERMINATE"]
    | Literal["BINDING_NOT_ACTIVE"]
    | Literal["CAPABILITY_COMPONENT_INCOMPATIBLE"]
    | Literal["CAPABILITY_COMPONENT_NOT_APPROVED"]
    | Literal["CAPABILITY_COMPONENT_NOT_REGISTERED"]
    | Literal["CAPABILITY_COMPONENT_RUNTIME_UNAVAILABLE"]
    | Literal["CAPABILITY_DETECTION_FAILED"]
    | Literal["CAPABILITY_FORMAT_AMBIGUOUS"]
    | Literal["CAPABILITY_FORMAT_UNDETECTED"]
    | Literal["CAPABILITY_RECIPE_INVALID"]
    | Literal["CAPABILITY_REGISTRATION_COLLISION"]
    | Literal["CAPABILITY_REGISTRY_NOT_SEALED"]
    | Literal["CAPABILITY_REGISTRY_SEALED"]
    | Literal["CREATOR_ASSERTION_REJECTED"]
    | Literal["CREATOR_BINDING_CONFLICT"]
    | Literal["CREATOR_DISCLOSURE_ERASED"]
    | Literal["CREATOR_DISCLOSURE_FORBIDDEN"]
    | Literal["CREATOR_IDENTITY_CONFLICT"]
    | Literal["CREATOR_IDENTITY_INVALID"]
    | Literal["CREATOR_IDENTITY_KEY_UNAVAILABLE"]
    | Literal["CREATOR_IDENTITY_NOT_FOUND"]
    | Literal["CREATOR_IDENTITY_REVOKED"]
    | Literal["DISCLOSURE_INVALID"]
    | Literal["DISCLOSURE_POLICY_NOT_FOUND"]
    | Literal["FINGERPRINT_ALGORITHM_UNSUPPORTED"]
    | Literal["FINGERPRINT_OUTPUT_INVALID"]
    | Literal["FINGERPRINT_RUNTIME_UNAVAILABLE"]
    | Literal["FOUNDATION_CANARY_OK"]
    | Literal["FOUNDATION_CANARY_UNCORRELATED"]
    | Literal["FOUNDATION_CONFIG_REJECTED"]
    | Literal["GENERATOR_ASSERTION_REJECTED"]
    | Literal["GENERATOR_CLAIM_CONFLICT"]
    | Literal["GENERATOR_ENGINE_UNAVAILABLE"]
    | Literal["GENERATOR_INGREDIENT_INVALID"]
    | Literal["GENERATOR_OUTPUT_INVALID"]
    | Literal["GENERATOR_SIGNING_FAILED"]
    | Literal["HISTORY_CURSOR_INVALID"]
    | Literal["HISTORY_QUERY_INVALID"]
    | Literal["HISTORY_READ_FORBIDDEN"]
    | Literal["HISTORY_RESOURCE_NOT_FOUND"]
    | Literal["IDENTITY_CREDENTIAL_NOT_ENROLLED"]
    | Literal["JOB_ASSET_NOT_READY"]
    | Literal["JOB_CANCEL_CONFLICT"]
    | Literal["JOB_CANCELED"]
    | Literal["JOB_COMPILE_CONFLICT"]
    | Literal["JOB_EFFECT_CONFLICT"]
    | Literal["JOB_IDEMPOTENCY_CONFLICT"]
    | Literal["JOB_LEASE_EXPIRED"]
    | Literal["JOB_LEASE_LOST"]
    | Literal["JOB_MESSAGE_INVALID"]
    | Literal["JOB_NOT_FOUND"]
    | Literal["JOB_OUTBOX_FAILED"]
    | Literal["JOB_PERMANENT_FAILURE"]
    | Literal["JOB_POLICY_REJECTED"]
    | Literal["JOB_RECIPE_INVALID"]
    | Literal["JOB_RECIPE_NOT_FOUND"]
    | Literal["JOB_REPLAY_FORBIDDEN"]
    | Literal["JOB_REPLAY_INVALID"]
    | Literal["JOB_RETRY_EXHAUSTED"]
    | Literal["JOB_RUNTIME_UNAVAILABLE"]
    | Literal["JOB_STEP_NOT_READY"]
    | Literal["JOB_TERMINAL"]
    | Literal["MARKING_CHECK_INVALID"]
    | Literal["MARKING_CHECK_NOT_FOUND"]
    | Literal["MEDIA_CODEC_UNSUPPORTED"]
    | Literal["MEDIA_COMPRESSED_SIZE_LIMIT"]
    | Literal["MEDIA_CONTAINER_LIMIT_EXCEEDED"]
    | Literal["MEDIA_CONTAINER_MALFORMED"]
    | Literal["MEDIA_DECODE_FAILED"]
    | Literal["MEDIA_DECODED_SIZE_LIMIT"]
    | Literal["MEDIA_DIMENSION_LIMIT_EXCEEDED"]
    | Literal["MEDIA_DURATION_LIMIT_EXCEEDED"]
    | Literal["MEDIA_ENCRYPTION_REJECTED"]
    | Literal["MEDIA_FORMAT_AMBIGUOUS"]
    | Literal["MEDIA_FORMAT_UNDETECTED"]
    | Literal["MEDIA_MANIFEST_LIMIT_EXCEEDED"]
    | Literal["MEDIA_MANIFEST_MALFORMED"]
    | Literal["MEDIA_METADATA_LIMIT_EXCEEDED"]
    | Literal["MEDIA_METADATA_MALFORMED"]
    | Literal["MEDIA_OUTPUT_CONTRACT_VIOLATION"]
    | Literal["MEDIA_PARSER_DIFFERENTIAL"]
    | Literal["MEDIA_POLYGLOT_REJECTED"]
    | Literal["MEDIA_PREVIEW_LIMIT_EXCEEDED"]
    | Literal["MEDIA_PREVIEW_UNSUPPORTED"]
    | Literal["MEDIA_PROFILE_INVALID"]
    | Literal["MEDIA_PROTOCOL_VERSION_UNSUPPORTED"]
    | Literal["MEDIA_RESOURCE_EXHAUSTED"]
    | Literal["MEDIA_SANDBOX_UNAVAILABLE"]
    | Literal["MEDIA_TIMEOUT"]
    | Literal["MEDIA_TIMESTAMP_LIMIT_EXCEEDED"]
    | Literal["MEDIA_TRACK_LIMIT_EXCEEDED"]
    | Literal["MODEL_ARTIFACT_INVALID"]
    | Literal["PUBLIC_CHECK_MEDIA_UNSUPPORTED"]
    | Literal["PUBLIC_CHECK_MONTHLY_LIMIT_REACHED"]
    | Literal["PUBLIC_CHECK_NOT_FOUND"]
    | Literal["PUBLIC_CHECK_RATE_LIMITED"]
    | Literal["PUBLICATION_EVIDENCE_INVALID"]
    | Literal["PUBLICATION_REQUEST_INVALID"]
    | Literal["SIGNING_ALGORITHM_REJECTED"]
    | Literal["SIGNING_AUDIT_UNAVAILABLE"]
    | Literal["SIGNING_AUTHORIZATION_EXPIRED"]
    | Literal["SIGNING_AUTHORIZATION_INVALID"]
    | Literal["SIGNING_AUTHORIZATION_REPLAYED"]
    | Literal["SIGNING_CERTIFICATE_MISMATCH"]
    | Literal["SIGNING_DIGEST_MISMATCH"]
    | Literal["SIGNING_FENCE_MISMATCH"]
    | Literal["SIGNING_KMS_DENIED"]
    | Literal["SIGNING_KMS_KEY_MISMATCH"]
    | Literal["SIGNING_PROFILE_UNAVAILABLE"]
    | Literal["SIGNING_SIGNATURE_INVALID"]
    | Literal["SIGNING_TIMESTAMP_FAILED"]
    | Literal["SIGNING_TIMESTAMP_REPLAYED"]
    | Literal["STORAGE_IMMUTABILITY_VIOLATION"]
    | Literal["STORAGE_OPERATION_FAILED"]
    | Literal["TENANT_WRITE_CONTENDED"]
    | Literal["UPLOAD_ABORTED"]
    | Literal["UPLOAD_ALREADY_COMPLETED"]
    | Literal["UPLOAD_CHECKSUM_MISMATCH"]
    | Literal["UPLOAD_EXPIRED"]
    | Literal["UPLOAD_IDEMPOTENCY_CONFLICT"]
    | Literal["UPLOAD_INCOMPLETE"]
    | Literal["UPLOAD_INVALID_PARTS"]
    | Literal["UPLOAD_NOT_FOUND"]
    | Literal["UPLOAD_POLICY_REJECTED"]
    | Literal["UPLOAD_SIZE_MISMATCH"]
    | Literal["VALIDATION_ACTIVE_MANIFEST_INVALID"]
    | Literal["VALIDATION_CERTIFICATE_EXPIRED"]
    | Literal["VALIDATION_CERTIFICATE_INVALID"]
    | Literal["VALIDATION_CERTIFICATE_NOT_YET_VALID"]
    | Literal["VALIDATION_CONFORMANCE_LIST_UNAVAILABLE"]
    | Literal["VALIDATION_CONFORMANCE_PRODUCT_NOT_LISTED"]
    | Literal["VALIDATION_EVIDENCE_UNAVAILABLE"]
    | Literal["VALIDATION_HARD_BINDING_MISMATCH"]
    | Literal["VALIDATION_INGREDIENT_CYCLE"]
    | Literal["VALIDATION_INGREDIENT_INVALID"]
    | Literal["VALIDATION_INGREDIENT_LIMIT_EXCEEDED"]
    | Literal["VALIDATION_INTEGRITY_MISMATCH"]
    | Literal["VALIDATION_LIMIT_EXCEEDED"]
    | Literal["VALIDATION_MANIFEST_ABSENT"]
    | Literal["VALIDATION_MANIFEST_MALFORMED"]
    | Literal["VALIDATION_MANIFEST_UNSUPPORTED"]
    | Literal["VALIDATION_OUTPUT_INVALID"]
    | Literal["VALIDATION_POLICY_INVALID"]
    | Literal["VALIDATION_RECOVERY_ONLY"]
    | Literal["VALIDATION_REVOCATION_MALFORMED"]
    | Literal["VALIDATION_REVOCATION_REVOKED"]
    | Literal["VALIDATION_REVOCATION_UNAVAILABLE"]
    | Literal["VALIDATION_REVOCATION_UNKNOWN"]
    | Literal["VALIDATION_RUNTIME_UNAVAILABLE"]
    | Literal["VALIDATION_SIGNATURE_ALGORITHM_UNSUPPORTED"]
    | Literal["VALIDATION_SIGNATURE_INVALID"]
    | Literal["VALIDATION_SIGNER_UNTRUSTED"]
    | Literal["VALIDATION_SOURCE_MISMATCH"]
    | Literal["VALIDATION_STATUS_UNRECOGNIZED"]
    | Literal["VALIDATION_STRUCTURE_INVALID"]
    | Literal["VALIDATION_TIMESTAMP_INVALID"]
    | Literal["VALIDATION_TIMESTAMP_MISSING"]
    | Literal["VALIDATION_TIMESTAMP_UNTRUSTED"]
    | Literal["VALIDATION_TRUST_SNAPSHOT_EXPIRED"]
    | Literal["VALIDATION_TRUST_SNAPSHOT_INVALID"]
    | Literal["VERIFY_EXECUTION_CONTRACT_VIOLATION"]
    | Literal["VERIFY_IDEMPOTENCY_CONFLICT"]
    | Literal["VERIFY_MANIFEST_INVALID"]
    | Literal["VERIFY_MANIFEST_NOT_APPLICABLE"]
    | Literal["VERIFY_NOT_FOUND"]
    | Literal["VERIFY_NOT_READY"]
    | Literal["VERIFY_PAGE_CONFLICT"]
    | Literal["VERIFY_PAGE_INVALID"]
    | Literal["VERIFY_PAGE_NOT_FOUND"]
    | Literal["VERIFY_REPORT_NOT_FOUND"]
    | Literal["VERIFY_SHARE_NOT_FOUND"]
    | Literal["WATERMARK_DETECTION_FAILED"]
    | Literal["WATERMARK_EMBED_FAILED"]
    | Literal["WATERMARK_MODEL_INVALID"]
    | Literal["WATERMARK_PAYLOAD_MISMATCH"]
    | Literal["WATERMARK_RUNTIME_UNAVAILABLE"]
    | Literal["WEBHOOK_DELIVERY_UNAVAILABLE"]
    | Literal["WEBHOOK_NOT_FOUND"]
    | Literal["WEBHOOK_REPLAY_FORBIDDEN"]
    | Literal["WEBHOOK_TEST_RATE_LIMITED"]
    | Literal["WORKFLOW_TEMPLATE_CONFLICT"]
    | Literal["WORKFLOW_TEMPLATE_INVALID"]
    | Literal["WORKFLOW_TEMPLATE_NOT_FOUND"]
)


class ReceiptAiDeclarationResponse(TypedDict):
    declaration_sha256: Required[str]
    digital_source_type: Required[DigitalSourceType]
    inception_action: Required[Literal["c2pa.created"]]


class ReceiptBindingSetResponse(TypedDict):
    binding_set_sha256: Required[str]
    candidate_count: Required[int]
    schema_version: Required[Literal["op.publication-binding-set.v1"]]
    types: Required[
        list[
            Literal["hard_hash"]
            | Literal["iscc_fingerprint"]
            | Literal["sscd_descriptor"]
            | Literal["dinov2_descriptor"]
            | Literal["pdq_fingerprint"]
            | Literal["dinov2_lsh_fingerprint"]
            | Literal["audio_fingerprint"]
            | Literal["audfprint_fingerprint"]
            | Literal["iscc_audio_fingerprint"]
            | Literal["video_fingerprint"]
            | Literal["vpdq_fingerprint"]
            | Literal["watermark"]
        ]
    ]


class ReceiptHistoryPageResponse(TypedDict):
    items: Required[list[ReceiptHistoryResponse]]
    next_cursor: Required[str | None]


class ReceiptHistoryResponse(TypedDict):
    asset_id: Required[str]
    byte_length: Required[int | None]
    created_at: Required[str]
    job_id: Required[str]
    media_type: Required[HistoryMediaType | None]
    receipt_id: Required[str]
    receipt_url: Required[str]
    schema_version: Required[str]
    sha256: Required[str | None]


class ReceiptManifestResponse(TypedDict):
    active_label_sha256: Required[str]
    claim_plan_sha256: Required[str]
    manifest_id: Required[str]
    manifest_store_sha256: Required[str]


class ReceiptOutputResponse(TypedDict):
    byte_length: Required[int]
    media_type: Required[
        Literal["application/epub+zip"]
        | Literal["application/onnx"]
        | Literal["application/oxps"]
        | Literal["application/pdf"]
        | Literal["application/vnd.oasis.opendocument.text"]
        | Literal["application/vnd.openxmlformats-officedocument.wordprocessingml.document"]
        | Literal["application/x-jax"]
        | Literal["application/x-keras"]
        | Literal["application/x-mlnet"]
        | Literal["application/x-mxnet"]
        | Literal["application/x-npy"]
        | Literal["application/x-openvino-ir+xml"]
        | Literal["application/x-openvino-weights"]
        | Literal["application/x-pickle"]
        | Literal["application/x-protobuf"]
        | Literal["application/x-pytorch"]
        | Literal["application/x-tensorflow"]
        | Literal["application/x-tensorflow-savedmodel"]
        | Literal["application/x-zip-based"]
        | Literal["application/xhtml+xml"]
        | Literal["application/xml"]
        | Literal["audio/MPA"]
        | Literal["audio/aac"]
        | Literal["audio/flac"]
        | Literal["audio/mp4"]
        | Literal["audio/mpeg"]
        | Literal["audio/wav"]
        | Literal["audio/x-riff-based"]
        | Literal["font/otf"]
        | Literal["image/avif"]
        | Literal["image/gif"]
        | Literal["image/heic"]
        | Literal["image/heic-sequence"]
        | Literal["image/heif"]
        | Literal["image/heif-sequence"]
        | Literal["image/jpeg"]
        | Literal["image/jxl"]
        | Literal["image/png"]
        | Literal["image/svg+xml"]
        | Literal["image/tiff"]
        | Literal["image/webp"]
        | Literal["image/x-adobe-dng"]
        | Literal["image/x-riff-based"]
        | Literal["image/x-tiff-based"]
        | Literal["text/html"]
        | Literal["text/plain"]
        | Literal["text/xml"]
        | Literal["video/mp4"]
        | Literal["video/quicktime"]
        | Literal["video/x-bmff-based"]
        | Literal["video/x-msvideo"]
        | Literal["video/x-riff-based"]
    ]
    object_id: Required[str]
    sha256: Required[str]
    storage_version_sha256: Required[str]


class ReceiptPriorProvenanceResponse(TypedDict):
    disposition: Required[
        Literal["absent"]
        | Literal["valid_parent"]
        | Literal["untrusted_parent"]
        | Literal["invalid_parent"]
    ]
    validation_result_sha256: NotRequired[str | None]
    warning: NotRequired[ReceiptPriorProvenanceWarningResponse | None]


class ReceiptPriorProvenanceWarningResponse(TypedDict):
    c2pa_failure_codes: Required[list[str]]
    code: Required[Literal["prior_credential_untrusted"] | Literal["prior_credential_invalid"]]
    message: Required[str]
    reason_codes: Required[list[str]]


class ReceiptProductResponse(TypedDict):
    id: Required[str]
    name: Required[str]
    release_id: Required[str]


class ReceiptRecoveryResponse(TypedDict):
    accepted_at: Required[str]
    observation_policy_sha256: Required[str]
    observation_sha256: Required[str]
    recovery_id: Required[str]
    result_sha256: Required[str]


class ReceiptResponse(TypedDict):
    asset_id: Required[str]
    created_at: Required[str]
    evidence: Required[
        LegacySigningReceiptEvidenceResponse
        | SigningReceiptEvidenceResponse
        | SidecarSigningReceiptEvidenceResponse
        | AiDeclaredSigningReceiptEvidenceResponse
        | RecoveredSigningReceiptEvidenceResponse
        | BindingReceiptEvidenceResponse
    ]
    job_id: Required[str]
    receipt_id: Required[str]


class ReceiptSigningResponse(TypedDict):
    evidence_id: Required[str]
    evidence_sha256: Required[str]
    signature_sha256: Required[str]
    timestamp_evidence_sha256: Required[str | None]
    timestamp_omission_sha256: NotRequired[str | None]


class ReceiptValidationResponse(TypedDict):
    outcome: Required[Literal["valid"] | Literal["recovered"]]
    recovery_only: Required[bool]
    request_sha256: Required[str]
    result_sha256: Required[str]
    revocation_snapshot_id: Required[str | None]
    trust_snapshot_id: Required[str | None]
    validated_at: Required[str]
    validation_path: Required[Literal["direct"] | Literal["recovery"]]
    verification_id: Required[str]


type RecipeCatalogKind = (
    Literal["sign_only"] | Literal["watermark_only"] | Literal["watermark_then_sign"]
)


class RecipeCatalogResponse(TypedDict):
    available: Required[bool]
    catalog_version: NotRequired[Literal["op.recipe-catalog.v1"]]
    definition_sha256: Required[str]
    kind: Required[RecipeCatalogKind]
    name: Required[str]
    recipe_id: Required[str]
    recipe_url: Required[str]
    required_capabilities: Required[list[str]]
    required_steps: Required[list[str]]
    schema_version: Required[str]
    supported_media_types: Required[
        list[
            Literal["audio/mp4"]
            | Literal["audio/mpeg"]
            | Literal["audio/wav"]
            | Literal["image/avif"]
            | Literal["image/jpeg"]
            | Literal["image/png"]
            | Literal["image/tiff"]
            | Literal["image/webp"]
            | Literal["video/mp4"]
        ]
    ]
    unavailable_reason: Required[RecipeUnavailableReason | None]
    version: Required[int]


class RecipeListResponse(TypedDict):
    recipes: Required[list[RecipeResponse]]


class RecipeResponse(TypedDict):
    capabilities: Required[list[PublicRecipeCapability]]
    display_name: Required[str]
    recipe_id: Required[str]
    summary: Required[str]
    supported_media_types: Required[
        list[
            Literal["audio/flac"]
            | Literal["audio/mp4"]
            | Literal["audio/mpeg"]
            | Literal["audio/wav"]
            | Literal["image/avif"]
            | Literal["image/gif"]
            | Literal["image/heic"]
            | Literal["image/heic-sequence"]
            | Literal["image/heif"]
            | Literal["image/heif-sequence"]
            | Literal["image/jpeg"]
            | Literal["image/jxl"]
            | Literal["image/png"]
            | Literal["image/svg+xml"]
            | Literal["image/tiff"]
            | Literal["image/webp"]
            | Literal["image/x-adobe-dng"]
            | Literal["video/mp4"]
            | Literal["video/quicktime"]
            | Literal["video/x-msvideo"]
        ]
    ]
    version: Required[int]


type RecipeUnavailableReason = (
    Literal["definition_shape_invalid"]
    | Literal["definition_hash_mismatch"]
    | Literal["step_contract_mismatch"]
    | Literal["no_enabled_media_format"]
    | Literal["runtime_unavailable"]
)


class RecoveredReceiptSigningResponse(TypedDict):
    evidence_id: Required[str]
    evidence_sha256: Required[str]
    signature_sha256: Required[str]
    timestamp_evidence_sha256: Required[str | None]
    timestamp_omission_sha256: Required[None]
    timestamp_policy_observation_sha256: Required[str | None]


class RecoveredSigningReceiptEvidenceResponse(TypedDict):
    asset_id: Required[str]
    bindings: Required[ReceiptBindingSetResponse]
    job_id: Required[str]
    manifest: Required[ReceiptManifestResponse]
    output: Required[ReceiptOutputResponse]
    prior_provenance: Required[ReceiptPriorProvenanceResponse]
    product: Required[ReceiptProductResponse]
    published_at: Required[str]
    recovery: Required[ReceiptRecoveryResponse]
    schema_version: Required[Literal["op.signing-receipt.v3"]]
    signing: Required[RecoveredReceiptSigningResponse]
    validation: Required[ReceiptValidationResponse]


class ReplayWebhookDeliveryResponse(TypedDict):
    event_id: Required[str]


class ReportContentResponse(TypedDict):
    content_base64: Required[str]
    content_sha256: Required[str]
    content_type: Required[str]


type ReportFormat = Literal["machine_json"] | Literal["human_pdf"]


class ReportResponse(TypedDict):
    byte_length: NotRequired[int | None]
    content_sha256: NotRequired[str | None]
    content_type: NotRequired[str | None]
    format: Required[str]
    payload: NotRequired[dict[str, Any] | None]
    report_id: Required[str]
    state: Required[str]


class RequestObservationResponse(TypedDict):
    ever_used: Required[bool | None]
    last_request_at: Required[str | None]
    retry_after_seconds: Required[int | None]
    retryable: Required[bool]
    state: Required[RequestObservationState]


type RequestObservationState = Literal["available"] | Literal["temporarily_unavailable"]

type RequirementLevel = Literal["required"] | Literal["recommended"]


class ReviewedRecipeAvailabilityResponse(TypedDict):
    active: Required[CapabilityRecipeResponse | None]
    availability: Required[CapabilityAvailabilityResponse]
    recipe_id: Required[str]


class RotatedWebhookSecretResponse(TypedDict):
    endpoint: Required[WebhookEndpointResponse]
    secret: Required[str]


class RotateWebhookSecretRequest(TypedDict):
    overlap_seconds: NotRequired[int]


class SafetyStatementResponse(TypedDict):
    id: Required[str]
    text: Required[str]


class SecretNotReplayableResponse(TypedDict):
    detail: Required[Literal["secret_not_replayable"]]


class SharedVerificationResponse(TypedDict):
    creator: NotRequired[CreatorDisclosureResponse | None]
    result: Required[dict[str, Any]]
    schema_version: Required[str]
    verification_id: Required[str]


class SidecarManifestResponse(TypedDict):
    byte_length: Required[int]
    expires_at: Required[str]
    filename: Required[str]
    headers: Required[dict[str, str]]
    media_type: Required[Literal["application/c2pa"]]
    method: Required[Literal["GET"]]
    sha256: Required[str]
    storage_version_sha256: Required[str]
    url: Required[str]


class SidecarReceiptBindingSetResponse(TypedDict):
    binding_set_sha256: Required[str]
    candidate_count: Required[Literal[1]]
    schema_version: Required[Literal["op.publication-binding-set.v1"]]
    types: Required[list[Literal["hard_hash"]]]


class SidecarReceiptManifestResponse(TypedDict):
    claim_plan_sha256: Required[str]
    manifest_id: Required[str]
    manifest_store_sha256: Required[str]
    sidecar_object_id: Required[str]
    sidecar_sha256: Required[str]


class SidecarSigningReceiptEvidenceResponse(TypedDict):
    asset_id: Required[str]
    bindings: Required[SidecarReceiptBindingSetResponse]
    job_id: Required[str]
    manifest: Required[SidecarReceiptManifestResponse]
    output: Required[ReceiptOutputResponse]
    prior_provenance: NotRequired[ReceiptPriorProvenanceResponse | None]
    product: Required[ReceiptProductResponse]
    published_at: Required[str]
    schema_version: Required[Literal["op.signing-receipt.sidecar.v1"]]
    signing: Required[ReceiptSigningResponse]
    validation: Required[ReceiptValidationResponse]


class SignBatchItemResponse(TypedDict):
    error: Required[ErrorResponse | None]
    index: Required[int]
    job: Required[JobResponse | None]
    status: Required[int]


class SignBatchRequest(TypedDict):
    items: Required[list[SignRequest]]


class SignBatchResponse(TypedDict):
    items: Required[list[SignBatchItemResponse]]


class SignBlock(TypedDict):
    creator_id: NotRequired[str | None]
    mode: NotRequired[Literal["standard"] | Literal["express"] | None]
    type: Required[Literal["sign"]]


class SignIdentityRequest(TypedDict):
    credential_id: Required[str]


class SigningReceiptEvidenceResponse(TypedDict):
    asset_id: Required[str]
    bindings: Required[ReceiptBindingSetResponse | SidecarReceiptBindingSetResponse]
    job_id: Required[str]
    manifest: Required[ReceiptManifestResponse]
    output: Required[ReceiptOutputResponse]
    prior_provenance: Required[ReceiptPriorProvenanceResponse]
    product: Required[ReceiptProductResponse]
    published_at: Required[str]
    schema_version: Required[Literal["op.signing-receipt.v2"]]
    signing: Required[ReceiptSigningResponse]
    validation: Required[ReceiptValidationResponse]


class SignRequest(TypedDict):
    ai_declaration: NotRequired[AiDeclarationRequest | None]
    asset_id: Required[str]
    creator_id: NotRequired[str | None]
    fingerprint: NotRequired[bool | None]
    fingerprint_algorithms: NotRequired[
        list[
            Literal["audfprint"]
            | Literal["chromaprint"]
            | Literal["dinov2"]
            | Literal["dinov2-lsh256"]
            | Literal["iscc-audio"]
            | Literal["iscc-image"]
            | Literal["pdq"]
            | Literal["tmk-pdqf"]
            | Literal["vpdq"]
        ]
        | None
    ]
    identity: NotRequired[SignIdentityRequest | None]
    mode: NotRequired[Literal["standard"] | Literal["express"] | None]
    recipe_id: NotRequired[str | None]
    template_id: NotRequired[str | None]
    watermark: NotRequired[bool | None]
    watermark_algorithm: NotRequired[
        Literal["audioseal"]
        | Literal["audioseal-mm02-4"]
        | Literal["pixelseal"]
        | Literal["pixelseal-video"]
        | Literal["trustmark-b"]
        | Literal["trustmark-c"]
        | Literal["trustmark-p"]
        | Literal["trustmark-q"]
        | Literal["videoseal"]
        | Literal["videoseal-image"]
        | None
    ]
    watermark_strength: NotRequired[
        Literal["subtle"] | Literal["balanced"] | Literal["robust"] | None
    ]


type StatusClass = Literal["2xx"] | Literal["3xx"] | Literal["4xx"] | Literal["5xx"]


class StripeInboxResponse(TypedDict):
    duplicate: Required[bool]
    event_id: Required[str]
    state: Required[str]


type SummaryWindow = Literal["1h"] | Literal["24h"] | Literal["7d"]


class UpdateWebhookEndpointAutoDisableRequest(TypedDict):
    auto_disable_after_failures: Required[int]
    event_catalog_version: NotRequired[None]
    events: NotRequired[None]
    max_concurrency: NotRequired[int | None]
    rate_limit_per_minute: NotRequired[int | None]
    url: NotRequired[str | None]


type UpdateWebhookEndpointCommand = (
    UpdateWebhookEndpointEventsRequest
    | UpdateWebhookEndpointUrlRequest
    | UpdateWebhookEndpointConcurrencyRequest
    | UpdateWebhookEndpointRateRequest
    | UpdateWebhookEndpointAutoDisableRequest
)


class UpdateWebhookEndpointConcurrencyRequest(TypedDict):
    auto_disable_after_failures: NotRequired[int | None]
    event_catalog_version: NotRequired[None]
    events: NotRequired[None]
    max_concurrency: Required[int]
    rate_limit_per_minute: NotRequired[int | None]
    url: NotRequired[str | None]


class UpdateWebhookEndpointEventsRequest(TypedDict):
    auto_disable_after_failures: NotRequired[int | None]
    event_catalog_version: NotRequired[CustomerEventCatalogVersion | None]
    events: Required[list[CustomerEventType]]
    max_concurrency: NotRequired[int | None]
    rate_limit_per_minute: NotRequired[int | None]
    url: NotRequired[str | None]


class UpdateWebhookEndpointRateRequest(TypedDict):
    auto_disable_after_failures: NotRequired[int | None]
    event_catalog_version: NotRequired[None]
    events: NotRequired[None]
    max_concurrency: NotRequired[int | None]
    rate_limit_per_minute: Required[int]
    url: NotRequired[str | None]


type UpdateWebhookEndpointRequest = UpdateWebhookEndpointCommand


class UpdateWebhookEndpointUrlRequest(TypedDict):
    auto_disable_after_failures: NotRequired[int | None]
    event_catalog_version: NotRequired[None]
    events: NotRequired[None]
    max_concurrency: NotRequired[int | None]
    rate_limit_per_minute: NotRequired[int | None]
    url: Required[str]


class UploadBlock(TypedDict):
    type: Required[Literal["upload"]]


class UploadLimitsResponse(TypedDict):
    maximum_bytes: Required[int]
    modes: Required[list[Literal["single"] | Literal["multipart"]]]
    multipart_maximum_parts: Required[int]
    multipart_minimum_nonfinal_part_bytes: Required[int]
    multipart_minimum_parts: Required[int]


type UploadMode = Literal["single"] | Literal["multipart"]

type UploadStatus = (
    Literal["initiated"] | Literal["completed"] | Literal["aborted"] | Literal["expired"]
)


class UsageItemResponse(TypedDict):
    meter_type: Required[str]
    meter_version: Required[int]
    metering_id: Required[str]
    occurred_at: Required[str]
    quantity: Required[str]


class UsageResponse(TypedDict):
    cost_estimate: NotRequired[None]
    items: Required[list[UsageItemResponse]]
    meters: Required[list[MeterQuotaResponse]]
    period: Required[str]
    pricing_version: NotRequired[None]


class ValidationError(TypedDict):
    ctx: NotRequired[dict[str, Any]]
    input: NotRequired[str]
    loc: Required[list[str | int]]
    msg: Required[str]
    type: Required[str]


type ValidationPath = Literal["direct"] | Literal["recovery"] | Literal["none"]


class VerificationBatchItemResponse(TypedDict):
    error: Required[ErrorResponse | None]
    index: Required[int]
    status: Required[int]
    verification: Required[VerificationResponse | None]


class VerificationBatchRequest(TypedDict):
    items: Required[list[CreateVerificationRequest]]


class VerificationBatchResponse(TypedDict):
    items: Required[list[VerificationBatchItemResponse]]


class VerificationEvidenceResponse(TypedDict):
    asset_id: Required[str | None]
    created_at: Required[str]
    creator: NotRequired[CreatorDisclosureResponse | None]
    evidence_id: Required[str]
    object_sha256: Required[str]
    overall: Required[str]
    policy_version: Required[str | None]
    publication_id: Required[str | None]
    receipt_id: Required[str | None]
    report_eligible: Required[bool]
    result: Required[dict[str, Any]]
    share_eligible: Required[bool]
    signing_job_id: Required[str | None]
    storage_version_sha256: Required[str]
    subject_id: Required[str]
    subject_type: Required[str]
    trust_list_version: Required[str | None]
    validated_at: Required[str]
    validation_path: Required[str | None]
    verification_job_id: Required[str | None]


class VerificationHistoryPageResponse(TypedDict):
    items: Required[list[VerificationHistoryResponse]]
    next_cursor: Required[str | None]


class VerificationHistoryResponse(TypedDict):
    created_at: Required[str]
    job_id: Required[str | None]
    overall: Required[VerificationOverall]
    policy_version: Required[str | None]
    source_byte_length: Required[int | None]
    source_media_type: Required[HistoryMediaType | None]
    status_vocabulary_version: Required[C2PAStatusVocabularyVersion | None]
    subject_type: Required[VerificationSubjectType]
    validated_at: Required[str]
    validation_path: Required[ValidationPath | None]
    verification_id: Required[str]
    verification_url: Required[str]


type VerificationOverall = (
    Literal["valid"] | Literal["invalid"] | Literal["indeterminate"] | Literal["recovered"]
)


class VerificationResponse(TypedDict):
    completed_at: NotRequired[str | None]
    created_at: Required[str]
    evidence_id: NotRequired[str | None]
    failure_reason: NotRequired[ReasonCode | None]
    result: NotRequired[dict[str, Any] | None]
    state: Required[VerifyState]
    verification_id: Required[str]


class VerificationShareMetadataResponse(TypedDict):
    closed_at: Required[str | None]
    created_at: Required[str]
    expires_at: Required[str | None]
    share_id: Required[str]
    state: Required[Literal["active"] | Literal["revoked"] | Literal["unpublished"]]


class VerificationSharePageResponse(TypedDict):
    items: Required[list[VerificationShareMetadataResponse]]
    next_cursor: Required[str | None]


type VerificationSubjectType = (
    Literal["uploaded_object"]
    | Literal["stored_object"]
    | Literal["public_url"]
    | Literal["asset"]
    | Literal["manifest"]
    | Literal["receipt"]
)


class VerifyBlock(TypedDict):
    type: Required[Literal["verify"]]


class VerifyPageCheckUsage(TypedDict):
    checks: Required[int]
    limit: Required[int]
    period_end: Required[str]
    period_start: Required[str]


class VerifyPageColours(TypedDict):
    accent: NotRequired[str | None]
    background: NotRequired[str | None]
    text: NotRequired[str | None]


class VerifyPageResponse(TypedDict):
    check_usage: NotRequired[VerifyPageCheckUsage | None]
    colours: Required[VerifyPageColours]
    created_at: Required[str]
    display_name: Required[str]
    enabled: Required[bool]
    hosted_url: Required[str]
    logo_asset_id: Required[str | None]
    monthly_check_limit: NotRequired[int | None]
    recover_own_assets: Required[bool]
    slug: Required[str]
    updated_at: Required[str]
    version: Required[int]


class VerifyPageUpdateRequest(TypedDict):
    colours: NotRequired[VerifyPageColours | None]
    display_name: Required[str]
    enabled: NotRequired[bool]
    expected_version: Required[int]
    logo_asset_id: NotRequired[str | None]
    monthly_check_limit: NotRequired[int | None]
    recover_own_assets: NotRequired[bool]
    slug: Required[str]


type VerifyState = (
    Literal["accepted"] | Literal["running"] | Literal["completed"] | Literal["failed"]
)


class VideoTrackFacts(TypedDict):
    codec: NotRequired[Literal["h264"]]
    codec_profile: Required[str]
    decoded_byte_length: Required[int]
    duration_microseconds: Required[int]
    fps_denominator: Required[int]
    fps_numerator: Required[int]
    frame_count: Required[int]
    height: Required[int]
    pixel_format: Required[str]
    stream_index: Required[int]
    time_base_denominator: Required[int]
    time_base_numerator: Required[int]
    width: Required[int]


class WalletAutoRecharge(TypedDict):
    amount_usd: Required[str | None]
    enabled: Required[bool]
    threshold_usd: Required[str | None]


class WalletAutoRechargeRequest(TypedDict):
    amount_usd: NotRequired[float | str | None]
    enabled: Required[bool]
    threshold_usd: NotRequired[float | str | None]


class WalletResponse(TypedDict):
    auto_recharge: Required[WalletAutoRecharge]
    balance_usd: Required[str]
    currency: NotRequired[Literal["USD"]]
    enabled: Required[bool]
    month_to_date_spend_usd: Required[str]
    monthly_spend_limit_usd: Required[str | None]
    recharge_pending: Required[bool]
    reserved_usd: Required[str]
    top_up_max_usd: Required[str]
    top_up_min_usd: Required[str]
    transactions: Required[list[WalletTransactionResponse]]
    version: Required[int]


class WalletSettingsRequest(TypedDict):
    auto_recharge: Required[WalletAutoRechargeRequest]
    enabled: NotRequired[bool]
    expected_version: Required[int]
    monthly_spend_limit_usd: NotRequired[float | str | None]


class WalletTransactionResponse(TypedDict):
    amount_usd: Required[str]
    balance_after_usd: Required[str]
    created_at: Required[str]
    id: Required[str]
    kind: Required[
        Literal["top_up"] | Literal["charge"] | Literal["refund"] | Literal["adjustment"]
    ]


class WatermarkAlgorithmResponse(TypedDict):
    algorithm_id: Required[str]
    default: Required[bool]
    display_name: Required[str]
    false_match_rate_upper_bound: NotRequired[float | None]
    payload_bits: Required[int]
    quality: Required[dict[str, float]]
    recommended: Required[bool]
    robustness_attack: NotRequired[str | None]
    robustness_bit_accuracy: NotRequired[float | None]
    soft_binding: Required[Literal["registered"] | Literal["unregistered"]]
    soft_binding_registry_id: NotRequired[int | None]
    strength_levels: Required[WatermarkStrengthLevelsResponse]
    strengths: Required[list[float]]


class WatermarkBlock(TypedDict):
    algorithm: NotRequired[
        Literal["audioseal"]
        | Literal["audioseal-mm02-4"]
        | Literal["pixelseal"]
        | Literal["pixelseal-video"]
        | Literal["trustmark-b"]
        | Literal["trustmark-c"]
        | Literal["trustmark-p"]
        | Literal["trustmark-q"]
        | Literal["videoseal"]
        | Literal["videoseal-image"]
        | None
    ]
    strength: NotRequired[Literal["subtle"] | Literal["balanced"] | Literal["robust"] | None]
    type: Required[Literal["watermark"]]


class WatermarkStrengthLevelsResponse(TypedDict):
    balanced: Required[list[float]]
    robust: Required[list[float]]
    subtle: Required[list[float]]


class WebhookAck(TypedDict):
    duplicate: NotRequired[bool]
    result: Required[str]
    status: Required[str]


class WebhookAttemptPageResponse(TypedDict):
    data: Required[list[WebhookAttemptResponse]]
    next_cursor: NotRequired[str | None]


class WebhookAttemptResponse(TypedDict):
    attempt_no: Required[int]
    failure_class: Required[str | None]
    fencing_token: Required[int]
    occurred_at: Required[str]
    outcome: Required[
        Literal["dispatch_started"]
        | Literal["delivered"]
        | Literal["retrying"]
        | Literal["dead"]
        | Literal["stale_delivered"]
        | Literal["stale_failed"]
    ]
    phase: Required[Literal["dispatch_started"] | Literal["result"]]
    replay_generation: Required[int | None]
    response_body_sha256: Required[str | None]
    response_code: Required[int | None]


class WebhookBlock(TypedDict):
    endpoint_id: NotRequired[str | None]
    type: Required[Literal["webhook"]]


class WebhookDeliveryPageResponse(TypedDict):
    data: Required[list[WebhookDeliveryResponse]]
    next_cursor: NotRequired[str | None]


class WebhookDeliveryResponse(TypedDict):
    attempt_count: Required[int]
    created_at: Required[str]
    delivery_id: Required[str]
    event_id: Required[str]
    event_type: Required[CustomerEventType | Literal["webhook.test"]]
    next_attempt_at: Required[str | None]
    replay_count: Required[int]
    response_body_sha256: Required[str | None]
    response_code: Required[int | None]
    status: Required[
        Literal["pending"]
        | Literal["delivering"]
        | Literal["delivered"]
        | Literal["failed"]
        | Literal["dead"]
    ]
    terminal_reason: Required[WebhookDeliveryTerminalReason | None]


type WebhookDeliveryTerminalReason = (
    Literal["automatic_failure_threshold"]
    | Literal["customer_deleted"]
    | Literal["customer_disabled"]
    | Literal["payload_invalid"]
    | Literal["retryable_http"]
    | Literal["secret_invalid"]
    | Literal["terminal_http"]
    | Literal["transport_rejected"]
    | Literal["transport_unavailable"]
)

type WebhookDisabledReason = Literal["manual"] | Literal["consecutive_failures"]


class WebhookEndpointPageResponse(TypedDict):
    data: Required[list[WebhookEndpointResponse]]
    next_cursor: NotRequired[str | None]


class WebhookEndpointResponse(TypedDict):
    auto_disable_after_failures: Required[int]
    consecutive_failures: NotRequired[int]
    created_at: Required[str]
    deleted_at: NotRequired[str | None]
    disabled_at: NotRequired[str | None]
    disabled_reason: NotRequired[WebhookDisabledReason | None]
    endpoint_id: Required[str]
    event_catalog_version: Required[CustomerEventCatalogVersion]
    events: Required[list[CustomerEventType]]
    max_concurrency: Required[int]
    rate_limit_per_minute: Required[int]
    signing_secrets: NotRequired[list[WebhookSecretLifecycleResponse]]
    status: Required[Literal["active"] | Literal["disabled"] | Literal["deleted"]]
    triggering_delivery_id: NotRequired[str | None]
    updated_at: Required[str]
    url: Required[str]


class WebhookReplayResponse(TypedDict):
    delivery_count: Required[int]
    event_id: Required[str]


class WebhookSecretLifecycleResponse(TypedDict):
    created_at: Required[str]
    retire_at: NotRequired[str | None]
    status: Required[WebhookSecretLifecycleStatus]
    version: Required[int]


type WebhookSecretLifecycleStatus = Literal["active"] | Literal["retiring"]


class WebhookTestEventResponse(TypedDict):
    delivery_id: Required[str]
    event_id: Required[str]
    event_type: Required[Literal["webhook.test"]]


class WorkflowSignRequestFields(TypedDict):
    ai_declaration: NotRequired[AiDeclarationRequest | None]
    creator_id: NotRequired[str | None]
    fingerprint: Required[bool]
    fingerprint_algorithms: NotRequired[list[str] | None]
    identity: NotRequired[SignIdentityRequest | None]
    mode: NotRequired[Literal["standard"] | Literal["express"] | None]
    watermark: Required[bool]
    watermark_algorithm: NotRequired[str | None]
    watermark_strength: NotRequired[
        Literal["subtle"] | Literal["balanced"] | Literal["robust"] | None
    ]


class WorkflowTemplateListResponse(TypedDict):
    data: Required[list[WorkflowTemplateResponse]]


class WorkflowTemplateReplaceRequest(TypedDict):
    blocks: Required[
        list[
            UploadBlock
            | WatermarkBlock
            | FingerprintBlock
            | AiMarkBlock
            | CawgIdentityBlock
            | SignBlock
            | VerifyBlock
            | WebhookBlock
            | DisclosureEventBlock
        ]
    ]
    description: NotRequired[str | None]
    expected_version: Required[int]
    name: Required[str]


class WorkflowTemplateRequest(TypedDict):
    blocks: Required[
        list[
            UploadBlock
            | WatermarkBlock
            | FingerprintBlock
            | AiMarkBlock
            | CawgIdentityBlock
            | SignBlock
            | VerifyBlock
            | WebhookBlock
            | DisclosureEventBlock
        ]
    ]
    description: NotRequired[str | None]
    name: Required[str]


class WorkflowTemplateResponse(TypedDict):
    blocks: Required[
        list[
            UploadBlock
            | WatermarkBlock
            | FingerprintBlock
            | AiMarkBlock
            | CawgIdentityBlock
            | SignBlock
            | VerifyBlock
            | WebhookBlock
            | DisclosureEventBlock
        ]
    ]
    created_at: Required[str]
    description: Required[str | None]
    name: Required[str]
    schema_version: Required[Literal["op.workflow-template.v1"]]
    sign_request: Required[WorkflowSignRequestFields]
    template_id: Required[str]
    updated_at: Required[str]
    version: Required[int]


class WorkspaceGovernanceResponse(TypedDict):
    deletion_state: Required[AssetDeletionState | None]
    legal_hold_active: Required[bool]


GetHealthzParameters = TypedDict("GetHealthzParameters", {}, total=False)

GetHealthzHeaders = TypedDict("GetHealthzHeaders", {}, total=False)

type GetHealthzRequestBody = None
type GetHealthzSuccessResponse = HealthResponse
GetHealthzResponses = TypedDict("GetHealthzResponses", {"200": HealthResponse})
GetHealthzSuccessResponses = TypedDict("GetHealthzSuccessResponses", {"200": HealthResponse})
GetHealthzErrorResponses = TypedDict("GetHealthzErrorResponses", {})


class GetHealthzOperation(TypedDict):
    request: GetHealthzRequestBody
    response: GetHealthzSuccessResponse
    responses: GetHealthzResponses
    successes: GetHealthzSuccessResponses
    errors: GetHealthzErrorResponses
    parameters: GetHealthzParameters
    headers: GetHealthzHeaders


GetDatabaseHealthParameters = TypedDict("GetDatabaseHealthParameters", {}, total=False)

GetDatabaseHealthHeaders = TypedDict("GetDatabaseHealthHeaders", {}, total=False)

type GetDatabaseHealthRequestBody = None
type GetDatabaseHealthSuccessResponse = DbHealthResponse
GetDatabaseHealthResponses = TypedDict("GetDatabaseHealthResponses", {"200": DbHealthResponse})
GetDatabaseHealthSuccessResponses = TypedDict(
    "GetDatabaseHealthSuccessResponses", {"200": DbHealthResponse}
)
GetDatabaseHealthErrorResponses = TypedDict("GetDatabaseHealthErrorResponses", {})


class GetDatabaseHealthOperation(TypedDict):
    request: GetDatabaseHealthRequestBody
    response: GetDatabaseHealthSuccessResponse
    responses: GetDatabaseHealthResponses
    successes: GetDatabaseHealthSuccessResponses
    errors: GetDatabaseHealthErrorResponses
    parameters: GetDatabaseHealthParameters
    headers: GetDatabaseHealthHeaders


GetReadyzParameters = TypedDict("GetReadyzParameters", {}, total=False)

GetReadyzHeaders = TypedDict("GetReadyzHeaders", {}, total=False)

type GetReadyzRequestBody = None
type GetReadyzSuccessResponse = ReadinessResponse
GetReadyzResponses = TypedDict(
    "GetReadyzResponses", {"200": ReadinessResponse, "503": ReadinessResponse}
)
GetReadyzSuccessResponses = TypedDict("GetReadyzSuccessResponses", {"200": ReadinessResponse})
GetReadyzErrorResponses = TypedDict("GetReadyzErrorResponses", {"503": ReadinessResponse})


class GetReadyzOperation(TypedDict):
    request: GetReadyzRequestBody
    response: GetReadyzSuccessResponse
    responses: GetReadyzResponses
    successes: GetReadyzSuccessResponses
    errors: GetReadyzErrorResponses
    parameters: GetReadyzParameters
    headers: GetReadyzHeaders


GetGovernanceReadyzParameters = TypedDict("GetGovernanceReadyzParameters", {}, total=False)

GetGovernanceReadyzHeaders = TypedDict("GetGovernanceReadyzHeaders", {}, total=False)

type GetGovernanceReadyzRequestBody = None
type GetGovernanceReadyzSuccessResponse = GovernanceReadinessResponse
GetGovernanceReadyzResponses = TypedDict(
    "GetGovernanceReadyzResponses",
    {"200": GovernanceReadinessResponse, "503": GovernanceReadinessResponse},
)
GetGovernanceReadyzSuccessResponses = TypedDict(
    "GetGovernanceReadyzSuccessResponses", {"200": GovernanceReadinessResponse}
)
GetGovernanceReadyzErrorResponses = TypedDict(
    "GetGovernanceReadyzErrorResponses", {"503": GovernanceReadinessResponse}
)


class GetGovernanceReadyzOperation(TypedDict):
    request: GetGovernanceReadyzRequestBody
    response: GetGovernanceReadyzSuccessResponse
    responses: GetGovernanceReadyzResponses
    successes: GetGovernanceReadyzSuccessResponses
    errors: GetGovernanceReadyzErrorResponses
    parameters: GetGovernanceReadyzParameters
    headers: GetGovernanceReadyzHeaders


ListApiKeysParameters = TypedDict("ListApiKeysParameters", {}, total=False)

ListApiKeysHeaders = TypedDict("ListApiKeysHeaders", {}, total=False)

type ListApiKeysRequestBody = None
type ListApiKeysSuccessResponse = ApiKeyListResponse
ListApiKeysResponses = TypedDict(
    "ListApiKeysResponses",
    {
        "200": ApiKeyListResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
ListApiKeysSuccessResponses = TypedDict("ListApiKeysSuccessResponses", {"200": ApiKeyListResponse})
ListApiKeysErrorResponses = TypedDict(
    "ListApiKeysErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class ListApiKeysOperation(TypedDict):
    request: ListApiKeysRequestBody
    response: ListApiKeysSuccessResponse
    responses: ListApiKeysResponses
    successes: ListApiKeysSuccessResponses
    errors: ListApiKeysErrorResponses
    parameters: ListApiKeysParameters
    headers: ListApiKeysHeaders


CreateApiKeyParameters = TypedDict("CreateApiKeyParameters", {}, total=False)

CreateApiKeyHeaders = TypedDict(
    "CreateApiKeyHeaders", {"Idempotency-Key": Required[str]}, total=False
)

type CreateApiKeyRequestBody = ApiKeyCreateRequest
type CreateApiKeySuccessResponse = IssuedApiKeyResponse
CreateApiKeyResponses = TypedDict(
    "CreateApiKeyResponses",
    {
        "201": IssuedApiKeyResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
CreateApiKeySuccessResponses = TypedDict(
    "CreateApiKeySuccessResponses", {"201": IssuedApiKeyResponse}
)
CreateApiKeyErrorResponses = TypedDict(
    "CreateApiKeyErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class CreateApiKeyOperation(TypedDict):
    request: CreateApiKeyRequestBody
    response: CreateApiKeySuccessResponse
    responses: CreateApiKeyResponses
    successes: CreateApiKeySuccessResponses
    errors: CreateApiKeyErrorResponses
    parameters: CreateApiKeyParameters
    headers: CreateApiKeyHeaders


RevokeApiKeyParameters = TypedDict(
    "RevokeApiKeyParameters", {"api_key_id": Required[str]}, total=False
)

RevokeApiKeyHeaders = TypedDict(
    "RevokeApiKeyHeaders", {"Idempotency-Key": Required[str]}, total=False
)

type RevokeApiKeyRequestBody = None
type RevokeApiKeySuccessResponse = ApiKeyMetadataResponse
RevokeApiKeyResponses = TypedDict(
    "RevokeApiKeyResponses",
    {
        "200": ApiKeyMetadataResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
RevokeApiKeySuccessResponses = TypedDict(
    "RevokeApiKeySuccessResponses", {"200": ApiKeyMetadataResponse}
)
RevokeApiKeyErrorResponses = TypedDict(
    "RevokeApiKeyErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class RevokeApiKeyOperation(TypedDict):
    request: RevokeApiKeyRequestBody
    response: RevokeApiKeySuccessResponse
    responses: RevokeApiKeyResponses
    successes: RevokeApiKeySuccessResponses
    errors: RevokeApiKeyErrorResponses
    parameters: RevokeApiKeyParameters
    headers: RevokeApiKeyHeaders


GetApiKeyParameters = TypedDict("GetApiKeyParameters", {"api_key_id": Required[str]}, total=False)

GetApiKeyHeaders = TypedDict("GetApiKeyHeaders", {}, total=False)

type GetApiKeyRequestBody = None
type GetApiKeySuccessResponse = ApiKeyMetadataResponse
GetApiKeyResponses = TypedDict(
    "GetApiKeyResponses",
    {
        "200": ApiKeyMetadataResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
GetApiKeySuccessResponses = TypedDict("GetApiKeySuccessResponses", {"200": ApiKeyMetadataResponse})
GetApiKeyErrorResponses = TypedDict(
    "GetApiKeyErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class GetApiKeyOperation(TypedDict):
    request: GetApiKeyRequestBody
    response: GetApiKeySuccessResponse
    responses: GetApiKeyResponses
    successes: GetApiKeySuccessResponses
    errors: GetApiKeyErrorResponses
    parameters: GetApiKeyParameters
    headers: GetApiKeyHeaders


GetApiKeyRestrictionsParameters = TypedDict(
    "GetApiKeyRestrictionsParameters", {"api_key_id": Required[str]}, total=False
)

GetApiKeyRestrictionsHeaders = TypedDict("GetApiKeyRestrictionsHeaders", {}, total=False)

type GetApiKeyRestrictionsRequestBody = None
type GetApiKeyRestrictionsSuccessResponse = ApiKeyRestrictionsResponse
GetApiKeyRestrictionsResponses = TypedDict(
    "GetApiKeyRestrictionsResponses",
    {
        "200": ApiKeyRestrictionsResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
GetApiKeyRestrictionsSuccessResponses = TypedDict(
    "GetApiKeyRestrictionsSuccessResponses", {"200": ApiKeyRestrictionsResponse}
)
GetApiKeyRestrictionsErrorResponses = TypedDict(
    "GetApiKeyRestrictionsErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class GetApiKeyRestrictionsOperation(TypedDict):
    request: GetApiKeyRestrictionsRequestBody
    response: GetApiKeyRestrictionsSuccessResponse
    responses: GetApiKeyRestrictionsResponses
    successes: GetApiKeyRestrictionsSuccessResponses
    errors: GetApiKeyRestrictionsErrorResponses
    parameters: GetApiKeyRestrictionsParameters
    headers: GetApiKeyRestrictionsHeaders


SetApiKeyRestrictionsParameters = TypedDict(
    "SetApiKeyRestrictionsParameters", {"api_key_id": Required[str]}, total=False
)

SetApiKeyRestrictionsHeaders = TypedDict("SetApiKeyRestrictionsHeaders", {}, total=False)

type SetApiKeyRestrictionsRequestBody = ApiKeyRestrictionsUpdateRequest
type SetApiKeyRestrictionsSuccessResponse = ApiKeyRestrictionsResponse
SetApiKeyRestrictionsResponses = TypedDict(
    "SetApiKeyRestrictionsResponses",
    {
        "200": ApiKeyRestrictionsResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
SetApiKeyRestrictionsSuccessResponses = TypedDict(
    "SetApiKeyRestrictionsSuccessResponses", {"200": ApiKeyRestrictionsResponse}
)
SetApiKeyRestrictionsErrorResponses = TypedDict(
    "SetApiKeyRestrictionsErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class SetApiKeyRestrictionsOperation(TypedDict):
    request: SetApiKeyRestrictionsRequestBody
    response: SetApiKeyRestrictionsSuccessResponse
    responses: SetApiKeyRestrictionsResponses
    successes: SetApiKeyRestrictionsSuccessResponses
    errors: SetApiKeyRestrictionsErrorResponses
    parameters: SetApiKeyRestrictionsParameters
    headers: SetApiKeyRestrictionsHeaders


GetApiKeyRetentionParameters = TypedDict(
    "GetApiKeyRetentionParameters", {"api_key_id": Required[str]}, total=False
)

GetApiKeyRetentionHeaders = TypedDict("GetApiKeyRetentionHeaders", {}, total=False)

type GetApiKeyRetentionRequestBody = None
type GetApiKeyRetentionSuccessResponse = ApiKeyRetentionResponse
GetApiKeyRetentionResponses = TypedDict(
    "GetApiKeyRetentionResponses",
    {
        "200": ApiKeyRetentionResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
GetApiKeyRetentionSuccessResponses = TypedDict(
    "GetApiKeyRetentionSuccessResponses", {"200": ApiKeyRetentionResponse}
)
GetApiKeyRetentionErrorResponses = TypedDict(
    "GetApiKeyRetentionErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class GetApiKeyRetentionOperation(TypedDict):
    request: GetApiKeyRetentionRequestBody
    response: GetApiKeyRetentionSuccessResponse
    responses: GetApiKeyRetentionResponses
    successes: GetApiKeyRetentionSuccessResponses
    errors: GetApiKeyRetentionErrorResponses
    parameters: GetApiKeyRetentionParameters
    headers: GetApiKeyRetentionHeaders


SetApiKeyRetentionParameters = TypedDict(
    "SetApiKeyRetentionParameters", {"api_key_id": Required[str]}, total=False
)

SetApiKeyRetentionHeaders = TypedDict("SetApiKeyRetentionHeaders", {}, total=False)

type SetApiKeyRetentionRequestBody = ApiKeyRetentionRequest
type SetApiKeyRetentionSuccessResponse = ApiKeyRetentionResponse
SetApiKeyRetentionResponses = TypedDict(
    "SetApiKeyRetentionResponses",
    {
        "200": ApiKeyRetentionResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
SetApiKeyRetentionSuccessResponses = TypedDict(
    "SetApiKeyRetentionSuccessResponses", {"200": ApiKeyRetentionResponse}
)
SetApiKeyRetentionErrorResponses = TypedDict(
    "SetApiKeyRetentionErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class SetApiKeyRetentionOperation(TypedDict):
    request: SetApiKeyRetentionRequestBody
    response: SetApiKeyRetentionSuccessResponse
    responses: SetApiKeyRetentionResponses
    successes: SetApiKeyRetentionSuccessResponses
    errors: SetApiKeyRetentionErrorResponses
    parameters: SetApiKeyRetentionParameters
    headers: SetApiKeyRetentionHeaders


RotateApiKeyParameters = TypedDict(
    "RotateApiKeyParameters", {"api_key_id": Required[str]}, total=False
)

RotateApiKeyHeaders = TypedDict(
    "RotateApiKeyHeaders", {"Idempotency-Key": Required[str]}, total=False
)

type RotateApiKeyRequestBody = ApiKeyRotateRequest
type RotateApiKeySuccessResponse = IssuedApiKeyResponse
RotateApiKeyResponses = TypedDict(
    "RotateApiKeyResponses",
    {
        "201": IssuedApiKeyResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
RotateApiKeySuccessResponses = TypedDict(
    "RotateApiKeySuccessResponses", {"201": IssuedApiKeyResponse}
)
RotateApiKeyErrorResponses = TypedDict(
    "RotateApiKeyErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class RotateApiKeyOperation(TypedDict):
    request: RotateApiKeyRequestBody
    response: RotateApiKeySuccessResponse
    responses: RotateApiKeyResponses
    successes: RotateApiKeySuccessResponses
    errors: RotateApiKeyErrorResponses
    parameters: RotateApiKeyParameters
    headers: RotateApiKeyHeaders


CancelApiKeyRotationParameters = TypedDict(
    "CancelApiKeyRotationParameters", {"api_key_id": Required[str]}, total=False
)

CancelApiKeyRotationHeaders = TypedDict(
    "CancelApiKeyRotationHeaders", {"Idempotency-Key": Required[str]}, total=False
)

type CancelApiKeyRotationRequestBody = None
type CancelApiKeyRotationSuccessResponse = ApiKeyMetadataResponse
CancelApiKeyRotationResponses = TypedDict(
    "CancelApiKeyRotationResponses",
    {
        "200": ApiKeyMetadataResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
CancelApiKeyRotationSuccessResponses = TypedDict(
    "CancelApiKeyRotationSuccessResponses", {"200": ApiKeyMetadataResponse}
)
CancelApiKeyRotationErrorResponses = TypedDict(
    "CancelApiKeyRotationErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class CancelApiKeyRotationOperation(TypedDict):
    request: CancelApiKeyRotationRequestBody
    response: CancelApiKeyRotationSuccessResponse
    responses: CancelApiKeyRotationResponses
    successes: CancelApiKeyRotationSuccessResponses
    errors: CancelApiKeyRotationErrorResponses
    parameters: CancelApiKeyRotationParameters
    headers: CancelApiKeyRotationHeaders


CompleteApiKeyRotationParameters = TypedDict(
    "CompleteApiKeyRotationParameters", {"api_key_id": Required[str]}, total=False
)

CompleteApiKeyRotationHeaders = TypedDict(
    "CompleteApiKeyRotationHeaders", {"Idempotency-Key": Required[str]}, total=False
)

type CompleteApiKeyRotationRequestBody = None
type CompleteApiKeyRotationSuccessResponse = ApiKeyMetadataResponse
CompleteApiKeyRotationResponses = TypedDict(
    "CompleteApiKeyRotationResponses",
    {
        "200": ApiKeyMetadataResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
CompleteApiKeyRotationSuccessResponses = TypedDict(
    "CompleteApiKeyRotationSuccessResponses", {"200": ApiKeyMetadataResponse}
)
CompleteApiKeyRotationErrorResponses = TypedDict(
    "CompleteApiKeyRotationErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class CompleteApiKeyRotationOperation(TypedDict):
    request: CompleteApiKeyRotationRequestBody
    response: CompleteApiKeyRotationSuccessResponse
    responses: CompleteApiKeyRotationResponses
    successes: CompleteApiKeyRotationSuccessResponses
    errors: CompleteApiKeyRotationErrorResponses
    parameters: CompleteApiKeyRotationParameters
    headers: CompleteApiKeyRotationHeaders


GetApiKeySigningProfileParameters = TypedDict(
    "GetApiKeySigningProfileParameters", {"api_key_id": Required[str]}, total=False
)

GetApiKeySigningProfileHeaders = TypedDict("GetApiKeySigningProfileHeaders", {}, total=False)

type GetApiKeySigningProfileRequestBody = None
type GetApiKeySigningProfileSuccessResponse = ApiKeySigningProfileResponse
GetApiKeySigningProfileResponses = TypedDict(
    "GetApiKeySigningProfileResponses",
    {
        "200": ApiKeySigningProfileResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
GetApiKeySigningProfileSuccessResponses = TypedDict(
    "GetApiKeySigningProfileSuccessResponses", {"200": ApiKeySigningProfileResponse}
)
GetApiKeySigningProfileErrorResponses = TypedDict(
    "GetApiKeySigningProfileErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class GetApiKeySigningProfileOperation(TypedDict):
    request: GetApiKeySigningProfileRequestBody
    response: GetApiKeySigningProfileSuccessResponse
    responses: GetApiKeySigningProfileResponses
    successes: GetApiKeySigningProfileSuccessResponses
    errors: GetApiKeySigningProfileErrorResponses
    parameters: GetApiKeySigningProfileParameters
    headers: GetApiKeySigningProfileHeaders


SetApiKeySigningProfileParameters = TypedDict(
    "SetApiKeySigningProfileParameters", {"api_key_id": Required[str]}, total=False
)

SetApiKeySigningProfileHeaders = TypedDict("SetApiKeySigningProfileHeaders", {}, total=False)

type SetApiKeySigningProfileRequestBody = ApiKeySigningProfileUpdateRequest
type SetApiKeySigningProfileSuccessResponse = ApiKeySigningProfileResponse
SetApiKeySigningProfileResponses = TypedDict(
    "SetApiKeySigningProfileResponses",
    {
        "200": ApiKeySigningProfileResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
SetApiKeySigningProfileSuccessResponses = TypedDict(
    "SetApiKeySigningProfileSuccessResponses", {"200": ApiKeySigningProfileResponse}
)
SetApiKeySigningProfileErrorResponses = TypedDict(
    "SetApiKeySigningProfileErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class SetApiKeySigningProfileOperation(TypedDict):
    request: SetApiKeySigningProfileRequestBody
    response: SetApiKeySigningProfileSuccessResponse
    responses: SetApiKeySigningProfileResponses
    successes: SetApiKeySigningProfileSuccessResponses
    errors: SetApiKeySigningProfileErrorResponses
    parameters: SetApiKeySigningProfileParameters
    headers: SetApiKeySigningProfileHeaders


ListApiKeyScopesParameters = TypedDict("ListApiKeyScopesParameters", {}, total=False)

ListApiKeyScopesHeaders = TypedDict("ListApiKeyScopesHeaders", {}, total=False)

type ListApiKeyScopesRequestBody = None
type ListApiKeyScopesSuccessResponse = ApiKeyScopeCatalogResponse
ListApiKeyScopesResponses = TypedDict(
    "ListApiKeyScopesResponses",
    {
        "200": ApiKeyScopeCatalogResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
ListApiKeyScopesSuccessResponses = TypedDict(
    "ListApiKeyScopesSuccessResponses", {"200": ApiKeyScopeCatalogResponse}
)
ListApiKeyScopesErrorResponses = TypedDict(
    "ListApiKeyScopesErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class ListApiKeyScopesOperation(TypedDict):
    request: ListApiKeyScopesRequestBody
    response: ListApiKeyScopesSuccessResponse
    responses: ListApiKeyScopesResponses
    successes: ListApiKeyScopesSuccessResponses
    errors: ListApiKeyScopesErrorResponses
    parameters: ListApiKeyScopesParameters
    headers: ListApiKeyScopesHeaders


ListApiRequestLogsParameters = TypedDict(
    "ListApiRequestLogsParameters",
    {
        "api_key_id": NotRequired[str | None],
        "status_class": NotRequired[StatusClass | None],
        "route": NotRequired[str | None],
        "cursor": NotRequired[str | None],
        "limit": NotRequired[int],
    },
    total=False,
)

ListApiRequestLogsHeaders = TypedDict("ListApiRequestLogsHeaders", {}, total=False)

type ListApiRequestLogsRequestBody = None
type ListApiRequestLogsSuccessResponse = ApiRequestLogPageResponse
ListApiRequestLogsResponses = TypedDict(
    "ListApiRequestLogsResponses",
    {
        "200": ApiRequestLogPageResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
ListApiRequestLogsSuccessResponses = TypedDict(
    "ListApiRequestLogsSuccessResponses", {"200": ApiRequestLogPageResponse}
)
ListApiRequestLogsErrorResponses = TypedDict(
    "ListApiRequestLogsErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class ListApiRequestLogsOperation(TypedDict):
    request: ListApiRequestLogsRequestBody
    response: ListApiRequestLogsSuccessResponse
    responses: ListApiRequestLogsResponses
    successes: ListApiRequestLogsSuccessResponses
    errors: ListApiRequestLogsErrorResponses
    parameters: ListApiRequestLogsParameters
    headers: ListApiRequestLogsHeaders


SummarizeApiRequestLogsParameters = TypedDict(
    "SummarizeApiRequestLogsParameters", {"window": NotRequired[SummaryWindow]}, total=False
)

SummarizeApiRequestLogsHeaders = TypedDict("SummarizeApiRequestLogsHeaders", {}, total=False)

type SummarizeApiRequestLogsRequestBody = None
type SummarizeApiRequestLogsSuccessResponse = ApiRequestLogSummaryResponse
SummarizeApiRequestLogsResponses = TypedDict(
    "SummarizeApiRequestLogsResponses",
    {
        "200": ApiRequestLogSummaryResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
SummarizeApiRequestLogsSuccessResponses = TypedDict(
    "SummarizeApiRequestLogsSuccessResponses", {"200": ApiRequestLogSummaryResponse}
)
SummarizeApiRequestLogsErrorResponses = TypedDict(
    "SummarizeApiRequestLogsErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class SummarizeApiRequestLogsOperation(TypedDict):
    request: SummarizeApiRequestLogsRequestBody
    response: SummarizeApiRequestLogsSuccessResponse
    responses: SummarizeApiRequestLogsResponses
    successes: SummarizeApiRequestLogsSuccessResponses
    errors: SummarizeApiRequestLogsErrorResponses
    parameters: SummarizeApiRequestLogsParameters
    headers: SummarizeApiRequestLogsHeaders


ListAssetsParameters = TypedDict(
    "ListAssetsParameters",
    {
        "kind": NotRequired[AssetHistoryKind | None],
        "status": NotRequired[AssetHistoryStatus | None],
        "media": NotRequired[AssetMediaFamily | None],
        "from": NotRequired[str | None],
        "recipe_id": NotRequired[str | None],
        "verification_outcome": NotRequired[VerificationOverall | None],
        "cursor": NotRequired[str | None],
        "limit": NotRequired[int],
    },
    total=False,
)

ListAssetsHeaders = TypedDict("ListAssetsHeaders", {}, total=False)

type ListAssetsRequestBody = None
type ListAssetsSuccessResponse = AssetHistoryPageResponse
ListAssetsResponses = TypedDict(
    "ListAssetsResponses",
    {
        "200": AssetHistoryPageResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
ListAssetsSuccessResponses = TypedDict(
    "ListAssetsSuccessResponses", {"200": AssetHistoryPageResponse}
)
ListAssetsErrorResponses = TypedDict(
    "ListAssetsErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class ListAssetsOperation(TypedDict):
    request: ListAssetsRequestBody
    response: ListAssetsSuccessResponse
    responses: ListAssetsResponses
    successes: ListAssetsSuccessResponses
    errors: ListAssetsErrorResponses
    parameters: ListAssetsParameters
    headers: ListAssetsHeaders


GetAssetParameters = TypedDict("GetAssetParameters", {"asset_id": Required[str]}, total=False)

GetAssetHeaders = TypedDict("GetAssetHeaders", {}, total=False)

type GetAssetRequestBody = None
type GetAssetSuccessResponse = AssetResponse
GetAssetResponses = TypedDict(
    "GetAssetResponses",
    {
        "200": AssetResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
GetAssetSuccessResponses = TypedDict("GetAssetSuccessResponses", {"200": AssetResponse})
GetAssetErrorResponses = TypedDict(
    "GetAssetErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class GetAssetOperation(TypedDict):
    request: GetAssetRequestBody
    response: GetAssetSuccessResponse
    responses: GetAssetResponses
    successes: GetAssetSuccessResponses
    errors: GetAssetErrorResponses
    parameters: GetAssetParameters
    headers: GetAssetHeaders


GetAssetDetailParameters = TypedDict(
    "GetAssetDetailParameters",
    {
        "asset_id": Required[str],
        "verification_cursor": NotRequired[str | None],
        "activity_cursor": NotRequired[str | None],
        "limit": NotRequired[int],
    },
    total=False,
)

GetAssetDetailHeaders = TypedDict("GetAssetDetailHeaders", {}, total=False)

type GetAssetDetailRequestBody = None
type GetAssetDetailSuccessResponse = AssetDetailResponse
GetAssetDetailResponses = TypedDict(
    "GetAssetDetailResponses",
    {
        "200": AssetDetailResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
GetAssetDetailSuccessResponses = TypedDict(
    "GetAssetDetailSuccessResponses", {"200": AssetDetailResponse}
)
GetAssetDetailErrorResponses = TypedDict(
    "GetAssetDetailErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class GetAssetDetailOperation(TypedDict):
    request: GetAssetDetailRequestBody
    response: GetAssetDetailSuccessResponse
    responses: GetAssetDetailResponses
    successes: GetAssetDetailSuccessResponses
    errors: GetAssetDetailErrorResponses
    parameters: GetAssetDetailParameters
    headers: GetAssetDetailHeaders


CreateAssetDownloadParameters = TypedDict(
    "CreateAssetDownloadParameters", {"asset_id": Required[str]}, total=False
)

CreateAssetDownloadHeaders = TypedDict("CreateAssetDownloadHeaders", {}, total=False)

type CreateAssetDownloadRequestBody = None
type CreateAssetDownloadSuccessResponse = DownloadResponse
CreateAssetDownloadResponses = TypedDict(
    "CreateAssetDownloadResponses",
    {
        "200": DownloadResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
CreateAssetDownloadSuccessResponses = TypedDict(
    "CreateAssetDownloadSuccessResponses", {"200": DownloadResponse}
)
CreateAssetDownloadErrorResponses = TypedDict(
    "CreateAssetDownloadErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class CreateAssetDownloadOperation(TypedDict):
    request: CreateAssetDownloadRequestBody
    response: CreateAssetDownloadSuccessResponse
    responses: CreateAssetDownloadResponses
    successes: CreateAssetDownloadSuccessResponses
    errors: CreateAssetDownloadErrorResponses
    parameters: CreateAssetDownloadParameters
    headers: CreateAssetDownloadHeaders


CreateAssetPreviewParameters = TypedDict(
    "CreateAssetPreviewParameters", {"asset_id": Required[str]}, total=False
)

CreateAssetPreviewHeaders = TypedDict("CreateAssetPreviewHeaders", {}, total=False)

type CreateAssetPreviewRequestBody = None
type CreateAssetPreviewSuccessResponse = PreviewResponse
CreateAssetPreviewResponses = TypedDict(
    "CreateAssetPreviewResponses",
    {
        "200": PreviewResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
CreateAssetPreviewSuccessResponses = TypedDict(
    "CreateAssetPreviewSuccessResponses", {"200": PreviewResponse}
)
CreateAssetPreviewErrorResponses = TypedDict(
    "CreateAssetPreviewErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class CreateAssetPreviewOperation(TypedDict):
    request: CreateAssetPreviewRequestBody
    response: CreateAssetPreviewSuccessResponse
    responses: CreateAssetPreviewResponses
    successes: CreateAssetPreviewSuccessResponses
    errors: CreateAssetPreviewErrorResponses
    parameters: CreateAssetPreviewParameters
    headers: CreateAssetPreviewHeaders


RedeemAssetPreviewParameters = TypedDict(
    "RedeemAssetPreviewParameters",
    {"asset_id": Required[str], "capability": Required[str]},
    total=False,
)

RedeemAssetPreviewHeaders = TypedDict("RedeemAssetPreviewHeaders", {}, total=False)

type RedeemAssetPreviewRequestBody = None
type RedeemAssetPreviewSuccessResponse = None
RedeemAssetPreviewResponses = TypedDict(
    "RedeemAssetPreviewResponses", {"200": None, "404": ErrorResponse}
)
RedeemAssetPreviewSuccessResponses = TypedDict("RedeemAssetPreviewSuccessResponses", {"200": None})
RedeemAssetPreviewErrorResponses = TypedDict(
    "RedeemAssetPreviewErrorResponses", {"404": ErrorResponse}
)


class RedeemAssetPreviewOperation(TypedDict):
    request: RedeemAssetPreviewRequestBody
    response: RedeemAssetPreviewSuccessResponse
    responses: RedeemAssetPreviewResponses
    successes: RedeemAssetPreviewSuccessResponses
    errors: RedeemAssetPreviewErrorResponses
    parameters: RedeemAssetPreviewParameters
    headers: RedeemAssetPreviewHeaders


GetBillingAccountParameters = TypedDict("GetBillingAccountParameters", {}, total=False)

GetBillingAccountHeaders = TypedDict("GetBillingAccountHeaders", {}, total=False)

type GetBillingAccountRequestBody = None
type GetBillingAccountSuccessResponse = BillingAccountResponse
GetBillingAccountResponses = TypedDict(
    "GetBillingAccountResponses",
    {
        "200": BillingAccountResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
GetBillingAccountSuccessResponses = TypedDict(
    "GetBillingAccountSuccessResponses", {"200": BillingAccountResponse}
)
GetBillingAccountErrorResponses = TypedDict(
    "GetBillingAccountErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class GetBillingAccountOperation(TypedDict):
    request: GetBillingAccountRequestBody
    response: GetBillingAccountSuccessResponse
    responses: GetBillingAccountResponses
    successes: GetBillingAccountSuccessResponses
    errors: GetBillingAccountErrorResponses
    parameters: GetBillingAccountParameters
    headers: GetBillingAccountHeaders


ListBillingChargesParameters = TypedDict(
    "ListBillingChargesParameters",
    {"limit": NotRequired[int], "before": NotRequired[str | None]},
    total=False,
)

ListBillingChargesHeaders = TypedDict("ListBillingChargesHeaders", {}, total=False)

type ListBillingChargesRequestBody = None
type ListBillingChargesSuccessResponse = ProcessingChargesResponse
ListBillingChargesResponses = TypedDict(
    "ListBillingChargesResponses",
    {
        "200": ProcessingChargesResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
ListBillingChargesSuccessResponses = TypedDict(
    "ListBillingChargesSuccessResponses", {"200": ProcessingChargesResponse}
)
ListBillingChargesErrorResponses = TypedDict(
    "ListBillingChargesErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class ListBillingChargesOperation(TypedDict):
    request: ListBillingChargesRequestBody
    response: ListBillingChargesSuccessResponse
    responses: ListBillingChargesResponses
    successes: ListBillingChargesSuccessResponses
    errors: ListBillingChargesErrorResponses
    parameters: ListBillingChargesParameters
    headers: ListBillingChargesHeaders


CreateBillingCheckoutIntentParameters = TypedDict(
    "CreateBillingCheckoutIntentParameters", {}, total=False
)

CreateBillingCheckoutIntentHeaders = TypedDict(
    "CreateBillingCheckoutIntentHeaders", {}, total=False
)

type CreateBillingCheckoutIntentRequestBody = CheckoutIntentRequest
type CreateBillingCheckoutIntentSuccessResponse = BillingIntentResponse
CreateBillingCheckoutIntentResponses = TypedDict(
    "CreateBillingCheckoutIntentResponses",
    {
        "201": BillingIntentResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "502": HttpErrorResponse,
        "503": HttpErrorResponse,
    },
)
CreateBillingCheckoutIntentSuccessResponses = TypedDict(
    "CreateBillingCheckoutIntentSuccessResponses", {"201": BillingIntentResponse}
)
CreateBillingCheckoutIntentErrorResponses = TypedDict(
    "CreateBillingCheckoutIntentErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "502": HttpErrorResponse,
        "503": HttpErrorResponse,
    },
)


class CreateBillingCheckoutIntentOperation(TypedDict):
    request: CreateBillingCheckoutIntentRequestBody
    response: CreateBillingCheckoutIntentSuccessResponse
    responses: CreateBillingCheckoutIntentResponses
    successes: CreateBillingCheckoutIntentSuccessResponses
    errors: CreateBillingCheckoutIntentErrorResponses
    parameters: CreateBillingCheckoutIntentParameters
    headers: CreateBillingCheckoutIntentHeaders


ListBillingInvoicesParameters = TypedDict(
    "ListBillingInvoicesParameters",
    {"limit": NotRequired[int], "before": NotRequired[str | None]},
    total=False,
)

ListBillingInvoicesHeaders = TypedDict("ListBillingInvoicesHeaders", {}, total=False)

type ListBillingInvoicesRequestBody = None
type ListBillingInvoicesSuccessResponse = BillingInvoicesResponse
ListBillingInvoicesResponses = TypedDict(
    "ListBillingInvoicesResponses",
    {
        "200": BillingInvoicesResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
ListBillingInvoicesSuccessResponses = TypedDict(
    "ListBillingInvoicesSuccessResponses", {"200": BillingInvoicesResponse}
)
ListBillingInvoicesErrorResponses = TypedDict(
    "ListBillingInvoicesErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class ListBillingInvoicesOperation(TypedDict):
    request: ListBillingInvoicesRequestBody
    response: ListBillingInvoicesSuccessResponse
    responses: ListBillingInvoicesResponses
    successes: ListBillingInvoicesSuccessResponses
    errors: ListBillingInvoicesErrorResponses
    parameters: ListBillingInvoicesParameters
    headers: ListBillingInvoicesHeaders


GetBillingPlansParameters = TypedDict("GetBillingPlansParameters", {}, total=False)

GetBillingPlansHeaders = TypedDict("GetBillingPlansHeaders", {}, total=False)

type GetBillingPlansRequestBody = None
type GetBillingPlansSuccessResponse = BillingPlansResponse
GetBillingPlansResponses = TypedDict(
    "GetBillingPlansResponses",
    {
        "200": BillingPlansResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
GetBillingPlansSuccessResponses = TypedDict(
    "GetBillingPlansSuccessResponses", {"200": BillingPlansResponse}
)
GetBillingPlansErrorResponses = TypedDict(
    "GetBillingPlansErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class GetBillingPlansOperation(TypedDict):
    request: GetBillingPlansRequestBody
    response: GetBillingPlansSuccessResponse
    responses: GetBillingPlansResponses
    successes: GetBillingPlansSuccessResponses
    errors: GetBillingPlansErrorResponses
    parameters: GetBillingPlansParameters
    headers: GetBillingPlansHeaders


CreateBillingPortalIntentParameters = TypedDict(
    "CreateBillingPortalIntentParameters", {}, total=False
)

CreateBillingPortalIntentHeaders = TypedDict("CreateBillingPortalIntentHeaders", {}, total=False)

type CreateBillingPortalIntentRequestBody = PortalIntentRequest
type CreateBillingPortalIntentSuccessResponse = BillingIntentResponse
CreateBillingPortalIntentResponses = TypedDict(
    "CreateBillingPortalIntentResponses",
    {
        "201": BillingIntentResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "502": HttpErrorResponse,
        "503": HttpErrorResponse,
    },
)
CreateBillingPortalIntentSuccessResponses = TypedDict(
    "CreateBillingPortalIntentSuccessResponses", {"201": BillingIntentResponse}
)
CreateBillingPortalIntentErrorResponses = TypedDict(
    "CreateBillingPortalIntentErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "502": HttpErrorResponse,
        "503": HttpErrorResponse,
    },
)


class CreateBillingPortalIntentOperation(TypedDict):
    request: CreateBillingPortalIntentRequestBody
    response: CreateBillingPortalIntentSuccessResponse
    responses: CreateBillingPortalIntentResponses
    successes: CreateBillingPortalIntentSuccessResponses
    errors: CreateBillingPortalIntentErrorResponses
    parameters: CreateBillingPortalIntentParameters
    headers: CreateBillingPortalIntentHeaders


GetBillingPricingParameters = TypedDict("GetBillingPricingParameters", {}, total=False)

GetBillingPricingHeaders = TypedDict("GetBillingPricingHeaders", {}, total=False)

type GetBillingPricingRequestBody = None
type GetBillingPricingSuccessResponse = PricingResponse
GetBillingPricingResponses = TypedDict(
    "GetBillingPricingResponses",
    {
        "200": PricingResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
GetBillingPricingSuccessResponses = TypedDict(
    "GetBillingPricingSuccessResponses", {"200": PricingResponse}
)
GetBillingPricingErrorResponses = TypedDict(
    "GetBillingPricingErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class GetBillingPricingOperation(TypedDict):
    request: GetBillingPricingRequestBody
    response: GetBillingPricingSuccessResponse
    responses: GetBillingPricingResponses
    successes: GetBillingPricingSuccessResponses
    errors: GetBillingPricingErrorResponses
    parameters: GetBillingPricingParameters
    headers: GetBillingPricingHeaders


CreateBillingQuoteParameters = TypedDict("CreateBillingQuoteParameters", {}, total=False)

CreateBillingQuoteHeaders = TypedDict("CreateBillingQuoteHeaders", {}, total=False)

type CreateBillingQuoteRequestBody = PricingQuoteRequest
type CreateBillingQuoteSuccessResponse = PricingQuoteResponse
CreateBillingQuoteResponses = TypedDict(
    "CreateBillingQuoteResponses",
    {
        "200": PricingQuoteResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
CreateBillingQuoteSuccessResponses = TypedDict(
    "CreateBillingQuoteSuccessResponses", {"200": PricingQuoteResponse}
)
CreateBillingQuoteErrorResponses = TypedDict(
    "CreateBillingQuoteErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class CreateBillingQuoteOperation(TypedDict):
    request: CreateBillingQuoteRequestBody
    response: CreateBillingQuoteSuccessResponse
    responses: CreateBillingQuoteResponses
    successes: CreateBillingQuoteSuccessResponses
    errors: CreateBillingQuoteErrorResponses
    parameters: CreateBillingQuoteParameters
    headers: CreateBillingQuoteHeaders


GetBillingWalletParameters = TypedDict("GetBillingWalletParameters", {}, total=False)

GetBillingWalletHeaders = TypedDict("GetBillingWalletHeaders", {}, total=False)

type GetBillingWalletRequestBody = None
type GetBillingWalletSuccessResponse = WalletResponse
GetBillingWalletResponses = TypedDict(
    "GetBillingWalletResponses",
    {
        "200": WalletResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
GetBillingWalletSuccessResponses = TypedDict(
    "GetBillingWalletSuccessResponses", {"200": WalletResponse}
)
GetBillingWalletErrorResponses = TypedDict(
    "GetBillingWalletErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class GetBillingWalletOperation(TypedDict):
    request: GetBillingWalletRequestBody
    response: GetBillingWalletSuccessResponse
    responses: GetBillingWalletResponses
    successes: GetBillingWalletSuccessResponses
    errors: GetBillingWalletErrorResponses
    parameters: GetBillingWalletParameters
    headers: GetBillingWalletHeaders


SetBillingWalletSettingsParameters = TypedDict(
    "SetBillingWalletSettingsParameters", {}, total=False
)

SetBillingWalletSettingsHeaders = TypedDict("SetBillingWalletSettingsHeaders", {}, total=False)

type SetBillingWalletSettingsRequestBody = WalletSettingsRequest
type SetBillingWalletSettingsSuccessResponse = WalletResponse
SetBillingWalletSettingsResponses = TypedDict(
    "SetBillingWalletSettingsResponses",
    {
        "200": WalletResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
SetBillingWalletSettingsSuccessResponses = TypedDict(
    "SetBillingWalletSettingsSuccessResponses", {"200": WalletResponse}
)
SetBillingWalletSettingsErrorResponses = TypedDict(
    "SetBillingWalletSettingsErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class SetBillingWalletSettingsOperation(TypedDict):
    request: SetBillingWalletSettingsRequestBody
    response: SetBillingWalletSettingsSuccessResponse
    responses: SetBillingWalletSettingsResponses
    successes: SetBillingWalletSettingsSuccessResponses
    errors: SetBillingWalletSettingsErrorResponses
    parameters: SetBillingWalletSettingsParameters
    headers: SetBillingWalletSettingsHeaders


GetCapabilitiesParameters = TypedDict("GetCapabilitiesParameters", {}, total=False)

GetCapabilitiesHeaders = TypedDict("GetCapabilitiesHeaders", {}, total=False)

type GetCapabilitiesRequestBody = None
type GetCapabilitiesSuccessResponse = CapabilityDiscoveryResponse
GetCapabilitiesResponses = TypedDict(
    "GetCapabilitiesResponses",
    {
        "200": CapabilityDiscoveryResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
GetCapabilitiesSuccessResponses = TypedDict(
    "GetCapabilitiesSuccessResponses", {"200": CapabilityDiscoveryResponse}
)
GetCapabilitiesErrorResponses = TypedDict(
    "GetCapabilitiesErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class GetCapabilitiesOperation(TypedDict):
    request: GetCapabilitiesRequestBody
    response: GetCapabilitiesSuccessResponse
    responses: GetCapabilitiesResponses
    successes: GetCapabilitiesSuccessResponses
    errors: GetCapabilitiesErrorResponses
    parameters: GetCapabilitiesParameters
    headers: GetCapabilitiesHeaders


CreateCaptureAdmissionChallengeParameters = TypedDict(
    "CreateCaptureAdmissionChallengeParameters", {}, total=False
)

CreateCaptureAdmissionChallengeHeaders = TypedDict(
    "CreateCaptureAdmissionChallengeHeaders", {"Idempotency-Key": Required[str]}, total=False
)

type CreateCaptureAdmissionChallengeRequestBody = CaptureAdmissionChallengeRequest
type CreateCaptureAdmissionChallengeSuccessResponse = CaptureAdmissionChallengeResponse
CreateCaptureAdmissionChallengeResponses = TypedDict(
    "CreateCaptureAdmissionChallengeResponses",
    {
        "201": CaptureAdmissionChallengeResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": CaptureManagementErrorResponse,
        "409": HttpErrorResponse | CaptureManagementErrorResponse,
        "422": HttpErrorResponse | CaptureManagementErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | CaptureManagementErrorResponse,
    },
)
CreateCaptureAdmissionChallengeSuccessResponses = TypedDict(
    "CreateCaptureAdmissionChallengeSuccessResponses", {"201": CaptureAdmissionChallengeResponse}
)
CreateCaptureAdmissionChallengeErrorResponses = TypedDict(
    "CreateCaptureAdmissionChallengeErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": CaptureManagementErrorResponse,
        "409": HttpErrorResponse | CaptureManagementErrorResponse,
        "422": HttpErrorResponse | CaptureManagementErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | CaptureManagementErrorResponse,
    },
)


class CreateCaptureAdmissionChallengeOperation(TypedDict):
    request: CreateCaptureAdmissionChallengeRequestBody
    response: CreateCaptureAdmissionChallengeSuccessResponse
    responses: CreateCaptureAdmissionChallengeResponses
    successes: CreateCaptureAdmissionChallengeSuccessResponses
    errors: CreateCaptureAdmissionChallengeErrorResponses
    parameters: CreateCaptureAdmissionChallengeParameters
    headers: CreateCaptureAdmissionChallengeHeaders


ListCaptureAdmissionsParameters = TypedDict(
    "ListCaptureAdmissionsParameters",
    {
        "decision": NotRequired[CaptureAdmissionDecision | None],
        "capture_identity_id": NotRequired[str | None],
        "decided_from": NotRequired[str | None],
        "decided_through": NotRequired[str | None],
        "cursor": NotRequired[str | None],
        "limit": NotRequired[int | None],
    },
    total=False,
)

ListCaptureAdmissionsHeaders = TypedDict("ListCaptureAdmissionsHeaders", {}, total=False)

type ListCaptureAdmissionsRequestBody = None
type ListCaptureAdmissionsSuccessResponse = CaptureAdmissionListResponse
ListCaptureAdmissionsResponses = TypedDict(
    "ListCaptureAdmissionsResponses",
    {
        "200": CaptureAdmissionListResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": CaptureManagementErrorResponse,
        "409": HttpErrorResponse | CaptureManagementErrorResponse,
        "422": HttpErrorResponse | CaptureManagementErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | CaptureManagementErrorResponse,
    },
)
ListCaptureAdmissionsSuccessResponses = TypedDict(
    "ListCaptureAdmissionsSuccessResponses", {"200": CaptureAdmissionListResponse}
)
ListCaptureAdmissionsErrorResponses = TypedDict(
    "ListCaptureAdmissionsErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": CaptureManagementErrorResponse,
        "409": HttpErrorResponse | CaptureManagementErrorResponse,
        "422": HttpErrorResponse | CaptureManagementErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | CaptureManagementErrorResponse,
    },
)


class ListCaptureAdmissionsOperation(TypedDict):
    request: ListCaptureAdmissionsRequestBody
    response: ListCaptureAdmissionsSuccessResponse
    responses: ListCaptureAdmissionsResponses
    successes: ListCaptureAdmissionsSuccessResponses
    errors: ListCaptureAdmissionsErrorResponses
    parameters: ListCaptureAdmissionsParameters
    headers: ListCaptureAdmissionsHeaders


CreateCaptureAdmissionParameters = TypedDict("CreateCaptureAdmissionParameters", {}, total=False)

CreateCaptureAdmissionHeaders = TypedDict("CreateCaptureAdmissionHeaders", {}, total=False)

type CreateCaptureAdmissionRequestBody = CaptureAdmissionSubmissionRequest
type CreateCaptureAdmissionSuccessResponse = CaptureAdmissionSubmissionResponse
CreateCaptureAdmissionResponses = TypedDict(
    "CreateCaptureAdmissionResponses",
    {
        "200": CaptureAdmissionSubmissionResponse,
        "201": CaptureAdmissionSubmissionResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": CaptureManagementErrorResponse,
        "409": HttpErrorResponse | CaptureManagementErrorResponse,
        "422": HttpErrorResponse | CaptureManagementErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | CaptureManagementErrorResponse,
    },
)
CreateCaptureAdmissionSuccessResponses = TypedDict(
    "CreateCaptureAdmissionSuccessResponses",
    {"200": CaptureAdmissionSubmissionResponse, "201": CaptureAdmissionSubmissionResponse},
)
CreateCaptureAdmissionErrorResponses = TypedDict(
    "CreateCaptureAdmissionErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": CaptureManagementErrorResponse,
        "409": HttpErrorResponse | CaptureManagementErrorResponse,
        "422": HttpErrorResponse | CaptureManagementErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | CaptureManagementErrorResponse,
    },
)


class CreateCaptureAdmissionOperation(TypedDict):
    request: CreateCaptureAdmissionRequestBody
    response: CreateCaptureAdmissionSuccessResponse
    responses: CreateCaptureAdmissionResponses
    successes: CreateCaptureAdmissionSuccessResponses
    errors: CreateCaptureAdmissionErrorResponses
    parameters: CreateCaptureAdmissionParameters
    headers: CreateCaptureAdmissionHeaders


GetCaptureAdmissionParameters = TypedDict(
    "GetCaptureAdmissionParameters", {"capture_admission_id": Required[str]}, total=False
)

GetCaptureAdmissionHeaders = TypedDict(
    "GetCaptureAdmissionHeaders", {"If-None-Match": NotRequired[str | None]}, total=False
)

type GetCaptureAdmissionRequestBody = None
type GetCaptureAdmissionSuccessResponse = CaptureAdmissionDetail
GetCaptureAdmissionResponses = TypedDict(
    "GetCaptureAdmissionResponses",
    {
        "200": CaptureAdmissionDetail,
        "304": None,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": CaptureManagementErrorResponse,
        "409": HttpErrorResponse | CaptureManagementErrorResponse,
        "422": HttpErrorResponse | CaptureManagementErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | CaptureManagementErrorResponse,
    },
)
GetCaptureAdmissionSuccessResponses = TypedDict(
    "GetCaptureAdmissionSuccessResponses", {"200": CaptureAdmissionDetail}
)
GetCaptureAdmissionErrorResponses = TypedDict(
    "GetCaptureAdmissionErrorResponses",
    {
        "304": None,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": CaptureManagementErrorResponse,
        "409": HttpErrorResponse | CaptureManagementErrorResponse,
        "422": HttpErrorResponse | CaptureManagementErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | CaptureManagementErrorResponse,
    },
)


class GetCaptureAdmissionOperation(TypedDict):
    request: GetCaptureAdmissionRequestBody
    response: GetCaptureAdmissionSuccessResponse
    responses: GetCaptureAdmissionResponses
    successes: GetCaptureAdmissionSuccessResponses
    errors: GetCaptureAdmissionErrorResponses
    parameters: GetCaptureAdmissionParameters
    headers: GetCaptureAdmissionHeaders


ListCaptureIdentitiesParameters = TypedDict(
    "ListCaptureIdentitiesParameters",
    {
        "state": NotRequired[CaptureIdentityFilterState | None],
        "platform": NotRequired[CaptureIdentityPlatform | None],
        "provider_class": NotRequired[CaptureProviderClass | None],
        "cursor": NotRequired[str | None],
        "limit": NotRequired[int | None],
    },
    total=False,
)

ListCaptureIdentitiesHeaders = TypedDict("ListCaptureIdentitiesHeaders", {}, total=False)

type ListCaptureIdentitiesRequestBody = None
type ListCaptureIdentitiesSuccessResponse = CaptureIdentityListResponse
ListCaptureIdentitiesResponses = TypedDict(
    "ListCaptureIdentitiesResponses",
    {
        "200": CaptureIdentityListResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": CaptureManagementErrorResponse,
        "409": HttpErrorResponse | CaptureManagementErrorResponse,
        "422": HttpErrorResponse | CaptureManagementErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | CaptureManagementErrorResponse,
    },
)
ListCaptureIdentitiesSuccessResponses = TypedDict(
    "ListCaptureIdentitiesSuccessResponses", {"200": CaptureIdentityListResponse}
)
ListCaptureIdentitiesErrorResponses = TypedDict(
    "ListCaptureIdentitiesErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": CaptureManagementErrorResponse,
        "409": HttpErrorResponse | CaptureManagementErrorResponse,
        "422": HttpErrorResponse | CaptureManagementErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | CaptureManagementErrorResponse,
    },
)


class ListCaptureIdentitiesOperation(TypedDict):
    request: ListCaptureIdentitiesRequestBody
    response: ListCaptureIdentitiesSuccessResponse
    responses: ListCaptureIdentitiesResponses
    successes: ListCaptureIdentitiesSuccessResponses
    errors: ListCaptureIdentitiesErrorResponses
    parameters: ListCaptureIdentitiesParameters
    headers: ListCaptureIdentitiesHeaders


CreateCaptureIdentityParameters = TypedDict("CreateCaptureIdentityParameters", {}, total=False)

CreateCaptureIdentityHeaders = TypedDict("CreateCaptureIdentityHeaders", {}, total=False)

type CreateCaptureIdentityRequestBody = CaptureIdentityCreationRequest
type CreateCaptureIdentitySuccessResponse = CaptureIdentityEnrollmentResult
CreateCaptureIdentityResponses = TypedDict(
    "CreateCaptureIdentityResponses",
    {
        "200": CaptureIdentityEnrollmentResult,
        "201": CaptureIdentityEnrollmentResult,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": CaptureManagementErrorResponse,
        "409": HttpErrorResponse | CaptureManagementErrorResponse,
        "422": HttpErrorResponse | CaptureManagementErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | CaptureManagementErrorResponse,
    },
)
CreateCaptureIdentitySuccessResponses = TypedDict(
    "CreateCaptureIdentitySuccessResponses",
    {"200": CaptureIdentityEnrollmentResult, "201": CaptureIdentityEnrollmentResult},
)
CreateCaptureIdentityErrorResponses = TypedDict(
    "CreateCaptureIdentityErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": CaptureManagementErrorResponse,
        "409": HttpErrorResponse | CaptureManagementErrorResponse,
        "422": HttpErrorResponse | CaptureManagementErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | CaptureManagementErrorResponse,
    },
)


class CreateCaptureIdentityOperation(TypedDict):
    request: CreateCaptureIdentityRequestBody
    response: CreateCaptureIdentitySuccessResponse
    responses: CreateCaptureIdentityResponses
    successes: CreateCaptureIdentitySuccessResponses
    errors: CreateCaptureIdentityErrorResponses
    parameters: CreateCaptureIdentityParameters
    headers: CreateCaptureIdentityHeaders


GetCaptureIdentityParameters = TypedDict(
    "GetCaptureIdentityParameters", {"capture_identity_id": Required[str]}, total=False
)

GetCaptureIdentityHeaders = TypedDict(
    "GetCaptureIdentityHeaders", {"If-None-Match": NotRequired[str | None]}, total=False
)

type GetCaptureIdentityRequestBody = None
type GetCaptureIdentitySuccessResponse = CaptureIdentityDetail
GetCaptureIdentityResponses = TypedDict(
    "GetCaptureIdentityResponses",
    {
        "200": CaptureIdentityDetail,
        "304": None,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": CaptureManagementErrorResponse,
        "409": HttpErrorResponse | CaptureManagementErrorResponse,
        "422": HttpErrorResponse | CaptureManagementErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | CaptureManagementErrorResponse,
    },
)
GetCaptureIdentitySuccessResponses = TypedDict(
    "GetCaptureIdentitySuccessResponses", {"200": CaptureIdentityDetail}
)
GetCaptureIdentityErrorResponses = TypedDict(
    "GetCaptureIdentityErrorResponses",
    {
        "304": None,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": CaptureManagementErrorResponse,
        "409": HttpErrorResponse | CaptureManagementErrorResponse,
        "422": HttpErrorResponse | CaptureManagementErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | CaptureManagementErrorResponse,
    },
)


class GetCaptureIdentityOperation(TypedDict):
    request: GetCaptureIdentityRequestBody
    response: GetCaptureIdentitySuccessResponse
    responses: GetCaptureIdentityResponses
    successes: GetCaptureIdentitySuccessResponses
    errors: GetCaptureIdentityErrorResponses
    parameters: GetCaptureIdentityParameters
    headers: GetCaptureIdentityHeaders


RevokeCaptureIdentityParameters = TypedDict(
    "RevokeCaptureIdentityParameters", {"capture_identity_id": Required[str]}, total=False
)

RevokeCaptureIdentityHeaders = TypedDict("RevokeCaptureIdentityHeaders", {}, total=False)

type RevokeCaptureIdentityRequestBody = None
type RevokeCaptureIdentitySuccessResponse = CaptureIdentityRevocationResponse
RevokeCaptureIdentityResponses = TypedDict(
    "RevokeCaptureIdentityResponses",
    {
        "200": CaptureIdentityRevocationResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": CaptureManagementErrorResponse,
        "409": HttpErrorResponse | CaptureManagementErrorResponse,
        "422": HttpErrorResponse | CaptureManagementErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | CaptureManagementErrorResponse,
    },
)
RevokeCaptureIdentitySuccessResponses = TypedDict(
    "RevokeCaptureIdentitySuccessResponses", {"200": CaptureIdentityRevocationResponse}
)
RevokeCaptureIdentityErrorResponses = TypedDict(
    "RevokeCaptureIdentityErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": CaptureManagementErrorResponse,
        "409": HttpErrorResponse | CaptureManagementErrorResponse,
        "422": HttpErrorResponse | CaptureManagementErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | CaptureManagementErrorResponse,
    },
)


class RevokeCaptureIdentityOperation(TypedDict):
    request: RevokeCaptureIdentityRequestBody
    response: RevokeCaptureIdentitySuccessResponse
    responses: RevokeCaptureIdentityResponses
    successes: RevokeCaptureIdentitySuccessResponses
    errors: RevokeCaptureIdentityErrorResponses
    parameters: RevokeCaptureIdentityParameters
    headers: RevokeCaptureIdentityHeaders


CreateCaptureIdentityEnrollmentParameters = TypedDict(
    "CreateCaptureIdentityEnrollmentParameters", {}, total=False
)

CreateCaptureIdentityEnrollmentHeaders = TypedDict(
    "CreateCaptureIdentityEnrollmentHeaders", {"Idempotency-Key": Required[str]}, total=False
)

type CreateCaptureIdentityEnrollmentRequestBody = CaptureIdentityEnrollmentRequest
type CreateCaptureIdentityEnrollmentSuccessResponse = CaptureIdentityEnrollmentResponse
CreateCaptureIdentityEnrollmentResponses = TypedDict(
    "CreateCaptureIdentityEnrollmentResponses",
    {
        "201": CaptureIdentityEnrollmentResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": CaptureManagementErrorResponse,
        "409": HttpErrorResponse | CaptureManagementErrorResponse,
        "422": HttpErrorResponse | CaptureManagementErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | CaptureManagementErrorResponse,
    },
)
CreateCaptureIdentityEnrollmentSuccessResponses = TypedDict(
    "CreateCaptureIdentityEnrollmentSuccessResponses", {"201": CaptureIdentityEnrollmentResponse}
)
CreateCaptureIdentityEnrollmentErrorResponses = TypedDict(
    "CreateCaptureIdentityEnrollmentErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": CaptureManagementErrorResponse,
        "409": HttpErrorResponse | CaptureManagementErrorResponse,
        "422": HttpErrorResponse | CaptureManagementErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | CaptureManagementErrorResponse,
    },
)


class CreateCaptureIdentityEnrollmentOperation(TypedDict):
    request: CreateCaptureIdentityEnrollmentRequestBody
    response: CreateCaptureIdentityEnrollmentSuccessResponse
    responses: CreateCaptureIdentityEnrollmentResponses
    successes: CreateCaptureIdentityEnrollmentSuccessResponses
    errors: CreateCaptureIdentityEnrollmentErrorResponses
    parameters: CreateCaptureIdentityEnrollmentParameters
    headers: CreateCaptureIdentityEnrollmentHeaders


GetConnectCatalogParameters = TypedDict("GetConnectCatalogParameters", {}, total=False)

GetConnectCatalogHeaders = TypedDict("GetConnectCatalogHeaders", {}, total=False)

type GetConnectCatalogRequestBody = None
type GetConnectCatalogSuccessResponse = ConnectCatalogResponse
GetConnectCatalogResponses = TypedDict(
    "GetConnectCatalogResponses", {"200": ConnectCatalogResponse}
)
GetConnectCatalogSuccessResponses = TypedDict(
    "GetConnectCatalogSuccessResponses", {"200": ConnectCatalogResponse}
)
GetConnectCatalogErrorResponses = TypedDict("GetConnectCatalogErrorResponses", {})


class GetConnectCatalogOperation(TypedDict):
    request: GetConnectCatalogRequestBody
    response: GetConnectCatalogSuccessResponse
    responses: GetConnectCatalogResponses
    successes: GetConnectCatalogSuccessResponses
    errors: GetConnectCatalogErrorResponses
    parameters: GetConnectCatalogParameters
    headers: GetConnectCatalogHeaders


GetCreatorDisclosurePolicyParameters = TypedDict(
    "GetCreatorDisclosurePolicyParameters", {}, total=False
)

GetCreatorDisclosurePolicyHeaders = TypedDict("GetCreatorDisclosurePolicyHeaders", {}, total=False)

type GetCreatorDisclosurePolicyRequestBody = None
type GetCreatorDisclosurePolicySuccessResponse = CreatorDisclosurePolicyResponse
GetCreatorDisclosurePolicyResponses = TypedDict(
    "GetCreatorDisclosurePolicyResponses",
    {
        "200": CreatorDisclosurePolicyResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
GetCreatorDisclosurePolicySuccessResponses = TypedDict(
    "GetCreatorDisclosurePolicySuccessResponses", {"200": CreatorDisclosurePolicyResponse}
)
GetCreatorDisclosurePolicyErrorResponses = TypedDict(
    "GetCreatorDisclosurePolicyErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class GetCreatorDisclosurePolicyOperation(TypedDict):
    request: GetCreatorDisclosurePolicyRequestBody
    response: GetCreatorDisclosurePolicySuccessResponse
    responses: GetCreatorDisclosurePolicyResponses
    successes: GetCreatorDisclosurePolicySuccessResponses
    errors: GetCreatorDisclosurePolicyErrorResponses
    parameters: GetCreatorDisclosurePolicyParameters
    headers: GetCreatorDisclosurePolicyHeaders


UpdateCreatorDisclosurePolicyParameters = TypedDict(
    "UpdateCreatorDisclosurePolicyParameters", {}, total=False
)

UpdateCreatorDisclosurePolicyHeaders = TypedDict(
    "UpdateCreatorDisclosurePolicyHeaders", {}, total=False
)

type UpdateCreatorDisclosurePolicyRequestBody = CreatorDisclosurePolicyRequest
type UpdateCreatorDisclosurePolicySuccessResponse = CreatorDisclosurePolicyResponse
UpdateCreatorDisclosurePolicyResponses = TypedDict(
    "UpdateCreatorDisclosurePolicyResponses",
    {
        "200": CreatorDisclosurePolicyResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
UpdateCreatorDisclosurePolicySuccessResponses = TypedDict(
    "UpdateCreatorDisclosurePolicySuccessResponses", {"200": CreatorDisclosurePolicyResponse}
)
UpdateCreatorDisclosurePolicyErrorResponses = TypedDict(
    "UpdateCreatorDisclosurePolicyErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class UpdateCreatorDisclosurePolicyOperation(TypedDict):
    request: UpdateCreatorDisclosurePolicyRequestBody
    response: UpdateCreatorDisclosurePolicySuccessResponse
    responses: UpdateCreatorDisclosurePolicyResponses
    successes: UpdateCreatorDisclosurePolicySuccessResponses
    errors: UpdateCreatorDisclosurePolicyErrorResponses
    parameters: UpdateCreatorDisclosurePolicyParameters
    headers: UpdateCreatorDisclosurePolicyHeaders


ListCreatorIdentitiesParameters = TypedDict(
    "ListCreatorIdentitiesParameters",
    {
        "state": NotRequired[Literal["active"] | Literal["withdrawn"] | Literal["erased"] | None],
        "cursor": NotRequired[str | None],
        "limit": NotRequired[int | None],
    },
    total=False,
)

ListCreatorIdentitiesHeaders = TypedDict("ListCreatorIdentitiesHeaders", {}, total=False)

type ListCreatorIdentitiesRequestBody = None
type ListCreatorIdentitiesSuccessResponse = CreatorIdentityListResponse
ListCreatorIdentitiesResponses = TypedDict(
    "ListCreatorIdentitiesResponses",
    {
        "200": CreatorIdentityListResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
ListCreatorIdentitiesSuccessResponses = TypedDict(
    "ListCreatorIdentitiesSuccessResponses", {"200": CreatorIdentityListResponse}
)
ListCreatorIdentitiesErrorResponses = TypedDict(
    "ListCreatorIdentitiesErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class ListCreatorIdentitiesOperation(TypedDict):
    request: ListCreatorIdentitiesRequestBody
    response: ListCreatorIdentitiesSuccessResponse
    responses: ListCreatorIdentitiesResponses
    successes: ListCreatorIdentitiesSuccessResponses
    errors: ListCreatorIdentitiesErrorResponses
    parameters: ListCreatorIdentitiesParameters
    headers: ListCreatorIdentitiesHeaders


CreateCreatorIdentityParameters = TypedDict("CreateCreatorIdentityParameters", {}, total=False)

CreateCreatorIdentityHeaders = TypedDict(
    "CreateCreatorIdentityHeaders", {"Idempotency-Key": Required[str]}, total=False
)

type CreateCreatorIdentityRequestBody = CreatorIdentityCreateRequest
type CreateCreatorIdentitySuccessResponse = CreatorIdentityResponse
CreateCreatorIdentityResponses = TypedDict(
    "CreateCreatorIdentityResponses",
    {
        "201": CreatorIdentityResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
CreateCreatorIdentitySuccessResponses = TypedDict(
    "CreateCreatorIdentitySuccessResponses", {"201": CreatorIdentityResponse}
)
CreateCreatorIdentityErrorResponses = TypedDict(
    "CreateCreatorIdentityErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class CreateCreatorIdentityOperation(TypedDict):
    request: CreateCreatorIdentityRequestBody
    response: CreateCreatorIdentitySuccessResponse
    responses: CreateCreatorIdentityResponses
    successes: CreateCreatorIdentitySuccessResponses
    errors: CreateCreatorIdentityErrorResponses
    parameters: CreateCreatorIdentityParameters
    headers: CreateCreatorIdentityHeaders


GetCreatorIdentityParameters = TypedDict(
    "GetCreatorIdentityParameters", {"creator_identity_id": Required[str]}, total=False
)

GetCreatorIdentityHeaders = TypedDict("GetCreatorIdentityHeaders", {}, total=False)

type GetCreatorIdentityRequestBody = None
type GetCreatorIdentitySuccessResponse = CreatorIdentityResponse
GetCreatorIdentityResponses = TypedDict(
    "GetCreatorIdentityResponses",
    {
        "200": CreatorIdentityResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
GetCreatorIdentitySuccessResponses = TypedDict(
    "GetCreatorIdentitySuccessResponses", {"200": CreatorIdentityResponse}
)
GetCreatorIdentityErrorResponses = TypedDict(
    "GetCreatorIdentityErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class GetCreatorIdentityOperation(TypedDict):
    request: GetCreatorIdentityRequestBody
    response: GetCreatorIdentitySuccessResponse
    responses: GetCreatorIdentityResponses
    successes: GetCreatorIdentitySuccessResponses
    errors: GetCreatorIdentityErrorResponses
    parameters: GetCreatorIdentityParameters
    headers: GetCreatorIdentityHeaders


DiscloseCreatorIdentityParameters = TypedDict(
    "DiscloseCreatorIdentityParameters", {"creator_identity_id": Required[str]}, total=False
)

DiscloseCreatorIdentityHeaders = TypedDict("DiscloseCreatorIdentityHeaders", {}, total=False)

type DiscloseCreatorIdentityRequestBody = None
type DiscloseCreatorIdentitySuccessResponse = CreatorDisclosureResponse
DiscloseCreatorIdentityResponses = TypedDict(
    "DiscloseCreatorIdentityResponses",
    {
        "200": CreatorDisclosureResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
DiscloseCreatorIdentitySuccessResponses = TypedDict(
    "DiscloseCreatorIdentitySuccessResponses", {"200": CreatorDisclosureResponse}
)
DiscloseCreatorIdentityErrorResponses = TypedDict(
    "DiscloseCreatorIdentityErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class DiscloseCreatorIdentityOperation(TypedDict):
    request: DiscloseCreatorIdentityRequestBody
    response: DiscloseCreatorIdentitySuccessResponse
    responses: DiscloseCreatorIdentityResponses
    successes: DiscloseCreatorIdentitySuccessResponses
    errors: DiscloseCreatorIdentityErrorResponses
    parameters: DiscloseCreatorIdentityParameters
    headers: DiscloseCreatorIdentityHeaders


WithdrawCreatorIdentityParameters = TypedDict(
    "WithdrawCreatorIdentityParameters", {"creator_identity_id": Required[str]}, total=False
)

WithdrawCreatorIdentityHeaders = TypedDict("WithdrawCreatorIdentityHeaders", {}, total=False)

type WithdrawCreatorIdentityRequestBody = None
type WithdrawCreatorIdentitySuccessResponse = CreatorIdentityResponse
WithdrawCreatorIdentityResponses = TypedDict(
    "WithdrawCreatorIdentityResponses",
    {
        "200": CreatorIdentityResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
WithdrawCreatorIdentitySuccessResponses = TypedDict(
    "WithdrawCreatorIdentitySuccessResponses", {"200": CreatorIdentityResponse}
)
WithdrawCreatorIdentityErrorResponses = TypedDict(
    "WithdrawCreatorIdentityErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class WithdrawCreatorIdentityOperation(TypedDict):
    request: WithdrawCreatorIdentityRequestBody
    response: WithdrawCreatorIdentitySuccessResponse
    responses: WithdrawCreatorIdentityResponses
    successes: WithdrawCreatorIdentitySuccessResponses
    errors: WithdrawCreatorIdentityErrorResponses
    parameters: WithdrawCreatorIdentityParameters
    headers: WithdrawCreatorIdentityHeaders


GetDeveloperOnboardingParameters = TypedDict("GetDeveloperOnboardingParameters", {}, total=False)

GetDeveloperOnboardingHeaders = TypedDict("GetDeveloperOnboardingHeaders", {}, total=False)

type GetDeveloperOnboardingRequestBody = None
type GetDeveloperOnboardingSuccessResponse = DeveloperOnboardingResponse
GetDeveloperOnboardingResponses = TypedDict(
    "GetDeveloperOnboardingResponses",
    {
        "200": DeveloperOnboardingResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
GetDeveloperOnboardingSuccessResponses = TypedDict(
    "GetDeveloperOnboardingSuccessResponses", {"200": DeveloperOnboardingResponse}
)
GetDeveloperOnboardingErrorResponses = TypedDict(
    "GetDeveloperOnboardingErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class GetDeveloperOnboardingOperation(TypedDict):
    request: GetDeveloperOnboardingRequestBody
    response: GetDeveloperOnboardingSuccessResponse
    responses: GetDeveloperOnboardingResponses
    successes: GetDeveloperOnboardingSuccessResponses
    errors: GetDeveloperOnboardingErrorResponses
    parameters: GetDeveloperOnboardingParameters
    headers: GetDeveloperOnboardingHeaders


ListDisclosureEventsParameters = TypedDict(
    "ListDisclosureEventsParameters",
    {
        "cursor": NotRequired[str | None],
        "limit": NotRequired[int],
        "kind": NotRequired[DisclosureEventKind | None],
        "jurisdiction": NotRequired[str | None],
        "received_after": NotRequired[str | None],
        "received_before": NotRequired[str | None],
    },
    total=False,
)

ListDisclosureEventsHeaders = TypedDict("ListDisclosureEventsHeaders", {}, total=False)

type ListDisclosureEventsRequestBody = None
type ListDisclosureEventsSuccessResponse = DisclosureEventPage
ListDisclosureEventsResponses = TypedDict(
    "ListDisclosureEventsResponses",
    {
        "200": DisclosureEventPage,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
ListDisclosureEventsSuccessResponses = TypedDict(
    "ListDisclosureEventsSuccessResponses", {"200": DisclosureEventPage}
)
ListDisclosureEventsErrorResponses = TypedDict(
    "ListDisclosureEventsErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class ListDisclosureEventsOperation(TypedDict):
    request: ListDisclosureEventsRequestBody
    response: ListDisclosureEventsSuccessResponse
    responses: ListDisclosureEventsResponses
    successes: ListDisclosureEventsSuccessResponses
    errors: ListDisclosureEventsErrorResponses
    parameters: ListDisclosureEventsParameters
    headers: ListDisclosureEventsHeaders


CreateDisclosureEventParameters = TypedDict("CreateDisclosureEventParameters", {}, total=False)

CreateDisclosureEventHeaders = TypedDict(
    "CreateDisclosureEventHeaders", {"Idempotency-Key": Required[str]}, total=False
)

type CreateDisclosureEventRequestBody = DisclosureEventRequest
type CreateDisclosureEventSuccessResponse = DisclosureEventReceipt
CreateDisclosureEventResponses = TypedDict(
    "CreateDisclosureEventResponses",
    {
        "201": DisclosureEventReceipt,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
CreateDisclosureEventSuccessResponses = TypedDict(
    "CreateDisclosureEventSuccessResponses", {"201": DisclosureEventReceipt}
)
CreateDisclosureEventErrorResponses = TypedDict(
    "CreateDisclosureEventErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class CreateDisclosureEventOperation(TypedDict):
    request: CreateDisclosureEventRequestBody
    response: CreateDisclosureEventSuccessResponse
    responses: CreateDisclosureEventResponses
    successes: CreateDisclosureEventSuccessResponses
    errors: CreateDisclosureEventErrorResponses
    parameters: CreateDisclosureEventParameters
    headers: CreateDisclosureEventHeaders


GetDisclosurePoliciesParameters = TypedDict(
    "GetDisclosurePoliciesParameters", {"version": NotRequired[str | None]}, total=False
)

GetDisclosurePoliciesHeaders = TypedDict("GetDisclosurePoliciesHeaders", {}, total=False)

type GetDisclosurePoliciesRequestBody = None
type GetDisclosurePoliciesSuccessResponse = DisclosurePolicyDocument
GetDisclosurePoliciesResponses = TypedDict(
    "GetDisclosurePoliciesResponses",
    {"200": DisclosurePolicyDocument, "404": ErrorResponse, "422": ErrorResponse},
)
GetDisclosurePoliciesSuccessResponses = TypedDict(
    "GetDisclosurePoliciesSuccessResponses", {"200": DisclosurePolicyDocument}
)
GetDisclosurePoliciesErrorResponses = TypedDict(
    "GetDisclosurePoliciesErrorResponses", {"404": ErrorResponse, "422": ErrorResponse}
)


class GetDisclosurePoliciesOperation(TypedDict):
    request: GetDisclosurePoliciesRequestBody
    response: GetDisclosurePoliciesSuccessResponse
    responses: GetDisclosurePoliciesResponses
    successes: GetDisclosurePoliciesSuccessResponses
    errors: GetDisclosurePoliciesErrorResponses
    parameters: GetDisclosurePoliciesParameters
    headers: GetDisclosurePoliciesHeaders


SubmitFeedbackParameters = TypedDict("SubmitFeedbackParameters", {}, total=False)

SubmitFeedbackHeaders = TypedDict("SubmitFeedbackHeaders", {}, total=False)

type SubmitFeedbackRequestBody = FeedbackBody
type SubmitFeedbackSuccessResponse = FeedbackResponse
SubmitFeedbackResponses = TypedDict(
    "SubmitFeedbackResponses",
    {
        "201": FeedbackResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse,
        "404": GovernanceErrorResponse,
        "409": HttpErrorResponse | GovernanceErrorResponse,
        "422": HttpErrorResponse | GovernanceErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | GovernanceErrorResponse,
    },
)
SubmitFeedbackSuccessResponses = TypedDict(
    "SubmitFeedbackSuccessResponses", {"201": FeedbackResponse}
)
SubmitFeedbackErrorResponses = TypedDict(
    "SubmitFeedbackErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse,
        "404": GovernanceErrorResponse,
        "409": HttpErrorResponse | GovernanceErrorResponse,
        "422": HttpErrorResponse | GovernanceErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | GovernanceErrorResponse,
    },
)


class SubmitFeedbackOperation(TypedDict):
    request: SubmitFeedbackRequestBody
    response: SubmitFeedbackSuccessResponse
    responses: SubmitFeedbackResponses
    successes: SubmitFeedbackSuccessResponses
    errors: SubmitFeedbackErrorResponses
    parameters: SubmitFeedbackParameters
    headers: SubmitFeedbackHeaders


QueryGovernanceAuditParameters = TypedDict(
    "QueryGovernanceAuditParameters",
    {
        "actor_id": NotRequired[str | None],
        "resource_type": NotRequired[str | None],
        "resource_id": NotRequired[str | None],
        "action": NotRequired[str | None],
        "request_id": NotRequired[str | None],
        "occurred_from": NotRequired[str | None],
        "occurred_to": NotRequired[str | None],
        "limit": NotRequired[int],
    },
    total=False,
)

QueryGovernanceAuditHeaders = TypedDict("QueryGovernanceAuditHeaders", {}, total=False)

type QueryGovernanceAuditRequestBody = None
type QueryGovernanceAuditSuccessResponse = list[AuditEventResponse]
QueryGovernanceAuditResponses = TypedDict(
    "QueryGovernanceAuditResponses",
    {
        "200": list[AuditEventResponse],
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse,
        "404": GovernanceErrorResponse,
        "409": HttpErrorResponse | GovernanceErrorResponse,
        "422": HttpErrorResponse | GovernanceErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | GovernanceErrorResponse,
    },
)
QueryGovernanceAuditSuccessResponses = TypedDict(
    "QueryGovernanceAuditSuccessResponses", {"200": list[AuditEventResponse]}
)
QueryGovernanceAuditErrorResponses = TypedDict(
    "QueryGovernanceAuditErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse,
        "404": GovernanceErrorResponse,
        "409": HttpErrorResponse | GovernanceErrorResponse,
        "422": HttpErrorResponse | GovernanceErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | GovernanceErrorResponse,
    },
)


class QueryGovernanceAuditOperation(TypedDict):
    request: QueryGovernanceAuditRequestBody
    response: QueryGovernanceAuditSuccessResponse
    responses: QueryGovernanceAuditResponses
    successes: QueryGovernanceAuditSuccessResponses
    errors: QueryGovernanceAuditErrorResponses
    parameters: QueryGovernanceAuditParameters
    headers: QueryGovernanceAuditHeaders


ListGovernanceDeletionsParameters = TypedDict(
    "ListGovernanceDeletionsParameters",
    {
        "status": NotRequired[
            Literal["requested"]
            | Literal["processing"]
            | Literal["completed"]
            | Literal["blocked_legal_hold"]
            | Literal["retry_wait"]
            | Literal["failed"]
            | None
        ],
        "cursor": NotRequired[str | None],
        "limit": NotRequired[int],
    },
    total=False,
)

ListGovernanceDeletionsHeaders = TypedDict("ListGovernanceDeletionsHeaders", {}, total=False)

type ListGovernanceDeletionsRequestBody = None
type ListGovernanceDeletionsSuccessResponse = DeletionPageResponse
ListGovernanceDeletionsResponses = TypedDict(
    "ListGovernanceDeletionsResponses",
    {
        "200": DeletionPageResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse,
        "404": GovernanceErrorResponse,
        "409": HttpErrorResponse | GovernanceErrorResponse,
        "422": HttpErrorResponse | GovernanceErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | GovernanceErrorResponse,
    },
)
ListGovernanceDeletionsSuccessResponses = TypedDict(
    "ListGovernanceDeletionsSuccessResponses", {"200": DeletionPageResponse}
)
ListGovernanceDeletionsErrorResponses = TypedDict(
    "ListGovernanceDeletionsErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse,
        "404": GovernanceErrorResponse,
        "409": HttpErrorResponse | GovernanceErrorResponse,
        "422": HttpErrorResponse | GovernanceErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | GovernanceErrorResponse,
    },
)


class ListGovernanceDeletionsOperation(TypedDict):
    request: ListGovernanceDeletionsRequestBody
    response: ListGovernanceDeletionsSuccessResponse
    responses: ListGovernanceDeletionsResponses
    successes: ListGovernanceDeletionsSuccessResponses
    errors: ListGovernanceDeletionsErrorResponses
    parameters: ListGovernanceDeletionsParameters
    headers: ListGovernanceDeletionsHeaders


CreateGovernanceDeletionParameters = TypedDict(
    "CreateGovernanceDeletionParameters", {}, total=False
)

CreateGovernanceDeletionHeaders = TypedDict(
    "CreateGovernanceDeletionHeaders", {"Idempotency-Key": Required[str]}, total=False
)

type CreateGovernanceDeletionRequestBody = DeletionRequestBody
type CreateGovernanceDeletionSuccessResponse = DeletionResponse
CreateGovernanceDeletionResponses = TypedDict(
    "CreateGovernanceDeletionResponses",
    {
        "202": DeletionResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse,
        "404": GovernanceErrorResponse,
        "409": HttpErrorResponse | GovernanceErrorResponse,
        "422": HttpErrorResponse | GovernanceErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | GovernanceErrorResponse,
    },
)
CreateGovernanceDeletionSuccessResponses = TypedDict(
    "CreateGovernanceDeletionSuccessResponses", {"202": DeletionResponse}
)
CreateGovernanceDeletionErrorResponses = TypedDict(
    "CreateGovernanceDeletionErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse,
        "404": GovernanceErrorResponse,
        "409": HttpErrorResponse | GovernanceErrorResponse,
        "422": HttpErrorResponse | GovernanceErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | GovernanceErrorResponse,
    },
)


class CreateGovernanceDeletionOperation(TypedDict):
    request: CreateGovernanceDeletionRequestBody
    response: CreateGovernanceDeletionSuccessResponse
    responses: CreateGovernanceDeletionResponses
    successes: CreateGovernanceDeletionSuccessResponses
    errors: CreateGovernanceDeletionErrorResponses
    parameters: CreateGovernanceDeletionParameters
    headers: CreateGovernanceDeletionHeaders


GetGovernanceDeletionParameters = TypedDict(
    "GetGovernanceDeletionParameters", {"deletion_id": Required[str]}, total=False
)

GetGovernanceDeletionHeaders = TypedDict("GetGovernanceDeletionHeaders", {}, total=False)

type GetGovernanceDeletionRequestBody = None
type GetGovernanceDeletionSuccessResponse = DeletionResponse
GetGovernanceDeletionResponses = TypedDict(
    "GetGovernanceDeletionResponses",
    {
        "200": DeletionResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse,
        "404": GovernanceErrorResponse,
        "409": HttpErrorResponse | GovernanceErrorResponse,
        "422": HttpErrorResponse | GovernanceErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | GovernanceErrorResponse,
    },
)
GetGovernanceDeletionSuccessResponses = TypedDict(
    "GetGovernanceDeletionSuccessResponses", {"200": DeletionResponse}
)
GetGovernanceDeletionErrorResponses = TypedDict(
    "GetGovernanceDeletionErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse,
        "404": GovernanceErrorResponse,
        "409": HttpErrorResponse | GovernanceErrorResponse,
        "422": HttpErrorResponse | GovernanceErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | GovernanceErrorResponse,
    },
)


class GetGovernanceDeletionOperation(TypedDict):
    request: GetGovernanceDeletionRequestBody
    response: GetGovernanceDeletionSuccessResponse
    responses: GetGovernanceDeletionResponses
    successes: GetGovernanceDeletionSuccessResponses
    errors: GetGovernanceDeletionErrorResponses
    parameters: GetGovernanceDeletionParameters
    headers: GetGovernanceDeletionHeaders


ListGovernanceExportsParameters = TypedDict(
    "ListGovernanceExportsParameters",
    {
        "status": NotRequired[
            Literal["requested"]
            | Literal["processing"]
            | Literal["ready"]
            | Literal["retry_wait"]
            | Literal["expired"]
            | Literal["failed"]
            | None
        ],
        "cursor": NotRequired[str | None],
        "limit": NotRequired[int],
    },
    total=False,
)

ListGovernanceExportsHeaders = TypedDict("ListGovernanceExportsHeaders", {}, total=False)

type ListGovernanceExportsRequestBody = None
type ListGovernanceExportsSuccessResponse = ExportPageResponse
ListGovernanceExportsResponses = TypedDict(
    "ListGovernanceExportsResponses",
    {
        "200": ExportPageResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse,
        "404": GovernanceErrorResponse,
        "409": HttpErrorResponse | GovernanceErrorResponse,
        "422": HttpErrorResponse | GovernanceErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | GovernanceErrorResponse,
    },
)
ListGovernanceExportsSuccessResponses = TypedDict(
    "ListGovernanceExportsSuccessResponses", {"200": ExportPageResponse}
)
ListGovernanceExportsErrorResponses = TypedDict(
    "ListGovernanceExportsErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse,
        "404": GovernanceErrorResponse,
        "409": HttpErrorResponse | GovernanceErrorResponse,
        "422": HttpErrorResponse | GovernanceErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | GovernanceErrorResponse,
    },
)


class ListGovernanceExportsOperation(TypedDict):
    request: ListGovernanceExportsRequestBody
    response: ListGovernanceExportsSuccessResponse
    responses: ListGovernanceExportsResponses
    successes: ListGovernanceExportsSuccessResponses
    errors: ListGovernanceExportsErrorResponses
    parameters: ListGovernanceExportsParameters
    headers: ListGovernanceExportsHeaders


CreateGovernanceExportParameters = TypedDict("CreateGovernanceExportParameters", {}, total=False)

CreateGovernanceExportHeaders = TypedDict(
    "CreateGovernanceExportHeaders", {"Idempotency-Key": Required[str]}, total=False
)

type CreateGovernanceExportRequestBody = None
type CreateGovernanceExportSuccessResponse = ExportResponse
CreateGovernanceExportResponses = TypedDict(
    "CreateGovernanceExportResponses",
    {
        "202": ExportResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse,
        "404": GovernanceErrorResponse,
        "409": HttpErrorResponse | GovernanceErrorResponse,
        "422": HttpErrorResponse | GovernanceErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | GovernanceErrorResponse,
    },
)
CreateGovernanceExportSuccessResponses = TypedDict(
    "CreateGovernanceExportSuccessResponses", {"202": ExportResponse}
)
CreateGovernanceExportErrorResponses = TypedDict(
    "CreateGovernanceExportErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse,
        "404": GovernanceErrorResponse,
        "409": HttpErrorResponse | GovernanceErrorResponse,
        "422": HttpErrorResponse | GovernanceErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | GovernanceErrorResponse,
    },
)


class CreateGovernanceExportOperation(TypedDict):
    request: CreateGovernanceExportRequestBody
    response: CreateGovernanceExportSuccessResponse
    responses: CreateGovernanceExportResponses
    successes: CreateGovernanceExportSuccessResponses
    errors: CreateGovernanceExportErrorResponses
    parameters: CreateGovernanceExportParameters
    headers: CreateGovernanceExportHeaders


GetGovernanceExportParameters = TypedDict(
    "GetGovernanceExportParameters", {"export_id": Required[str]}, total=False
)

GetGovernanceExportHeaders = TypedDict("GetGovernanceExportHeaders", {}, total=False)

type GetGovernanceExportRequestBody = None
type GetGovernanceExportSuccessResponse = ExportResponse
GetGovernanceExportResponses = TypedDict(
    "GetGovernanceExportResponses",
    {
        "200": ExportResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse,
        "404": GovernanceErrorResponse,
        "409": HttpErrorResponse | GovernanceErrorResponse,
        "422": HttpErrorResponse | GovernanceErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | GovernanceErrorResponse,
    },
)
GetGovernanceExportSuccessResponses = TypedDict(
    "GetGovernanceExportSuccessResponses", {"200": ExportResponse}
)
GetGovernanceExportErrorResponses = TypedDict(
    "GetGovernanceExportErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse,
        "404": GovernanceErrorResponse,
        "409": HttpErrorResponse | GovernanceErrorResponse,
        "422": HttpErrorResponse | GovernanceErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | GovernanceErrorResponse,
    },
)


class GetGovernanceExportOperation(TypedDict):
    request: GetGovernanceExportRequestBody
    response: GetGovernanceExportSuccessResponse
    responses: GetGovernanceExportResponses
    successes: GetGovernanceExportSuccessResponses
    errors: GetGovernanceExportErrorResponses
    parameters: GetGovernanceExportParameters
    headers: GetGovernanceExportHeaders


ListGovernanceLegalHoldsParameters = TypedDict(
    "ListGovernanceLegalHoldsParameters", {}, total=False
)

ListGovernanceLegalHoldsHeaders = TypedDict("ListGovernanceLegalHoldsHeaders", {}, total=False)

type ListGovernanceLegalHoldsRequestBody = None
type ListGovernanceLegalHoldsSuccessResponse = list[LegalHoldResponse]
ListGovernanceLegalHoldsResponses = TypedDict(
    "ListGovernanceLegalHoldsResponses",
    {
        "200": list[LegalHoldResponse],
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse,
        "404": GovernanceErrorResponse,
        "409": HttpErrorResponse | GovernanceErrorResponse,
        "422": HttpErrorResponse | GovernanceErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | GovernanceErrorResponse,
    },
)
ListGovernanceLegalHoldsSuccessResponses = TypedDict(
    "ListGovernanceLegalHoldsSuccessResponses", {"200": list[LegalHoldResponse]}
)
ListGovernanceLegalHoldsErrorResponses = TypedDict(
    "ListGovernanceLegalHoldsErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | GovernanceErrorResponse | ErrorResponse,
        "404": GovernanceErrorResponse,
        "409": HttpErrorResponse | GovernanceErrorResponse,
        "422": HttpErrorResponse | GovernanceErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | GovernanceErrorResponse,
    },
)


class ListGovernanceLegalHoldsOperation(TypedDict):
    request: ListGovernanceLegalHoldsRequestBody
    response: ListGovernanceLegalHoldsSuccessResponse
    responses: ListGovernanceLegalHoldsResponses
    successes: ListGovernanceLegalHoldsSuccessResponses
    errors: ListGovernanceLegalHoldsErrorResponses
    parameters: ListGovernanceLegalHoldsParameters
    headers: ListGovernanceLegalHoldsHeaders


ReleaseHistorySnapshotParameters = TypedDict(
    "ReleaseHistorySnapshotParameters", {"cursor": Required[str]}, total=False
)

ReleaseHistorySnapshotHeaders = TypedDict("ReleaseHistorySnapshotHeaders", {}, total=False)

type ReleaseHistorySnapshotRequestBody = None
type ReleaseHistorySnapshotSuccessResponse = None
ReleaseHistorySnapshotResponses = TypedDict(
    "ReleaseHistorySnapshotResponses",
    {
        "204": None,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
ReleaseHistorySnapshotSuccessResponses = TypedDict(
    "ReleaseHistorySnapshotSuccessResponses", {"204": None}
)
ReleaseHistorySnapshotErrorResponses = TypedDict(
    "ReleaseHistorySnapshotErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class ReleaseHistorySnapshotOperation(TypedDict):
    request: ReleaseHistorySnapshotRequestBody
    response: ReleaseHistorySnapshotSuccessResponse
    responses: ReleaseHistorySnapshotResponses
    successes: ReleaseHistorySnapshotSuccessResponses
    errors: ReleaseHistorySnapshotErrorResponses
    parameters: ReleaseHistorySnapshotParameters
    headers: ReleaseHistorySnapshotHeaders


ListIdentityCredentialsParameters = TypedDict("ListIdentityCredentialsParameters", {}, total=False)

ListIdentityCredentialsHeaders = TypedDict("ListIdentityCredentialsHeaders", {}, total=False)

type ListIdentityCredentialsRequestBody = None
type ListIdentityCredentialsSuccessResponse = IdentityCredentialListResponse
ListIdentityCredentialsResponses = TypedDict(
    "ListIdentityCredentialsResponses",
    {
        "200": IdentityCredentialListResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
ListIdentityCredentialsSuccessResponses = TypedDict(
    "ListIdentityCredentialsSuccessResponses", {"200": IdentityCredentialListResponse}
)
ListIdentityCredentialsErrorResponses = TypedDict(
    "ListIdentityCredentialsErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class ListIdentityCredentialsOperation(TypedDict):
    request: ListIdentityCredentialsRequestBody
    response: ListIdentityCredentialsSuccessResponse
    responses: ListIdentityCredentialsResponses
    successes: ListIdentityCredentialsSuccessResponses
    errors: ListIdentityCredentialsErrorResponses
    parameters: ListIdentityCredentialsParameters
    headers: ListIdentityCredentialsHeaders


ListImageProfilesParameters = TypedDict("ListImageProfilesParameters", {}, total=False)

ListImageProfilesHeaders = TypedDict("ListImageProfilesHeaders", {}, total=False)

type ListImageProfilesRequestBody = None
type ListImageProfilesSuccessResponse = ImageProfileListResponse
ListImageProfilesResponses = TypedDict(
    "ListImageProfilesResponses",
    {
        "200": ImageProfileListResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
ListImageProfilesSuccessResponses = TypedDict(
    "ListImageProfilesSuccessResponses", {"200": ImageProfileListResponse}
)
ListImageProfilesErrorResponses = TypedDict(
    "ListImageProfilesErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class ListImageProfilesOperation(TypedDict):
    request: ListImageProfilesRequestBody
    response: ListImageProfilesSuccessResponse
    responses: ListImageProfilesResponses
    successes: ListImageProfilesSuccessResponses
    errors: ListImageProfilesErrorResponses
    parameters: ListImageProfilesParameters
    headers: ListImageProfilesHeaders


ListJobsParameters = TypedDict(
    "ListJobsParameters",
    {
        "kind": NotRequired[JobKind | None],
        "state": NotRequired[JobState | None],
        "cursor": NotRequired[str | None],
        "limit": NotRequired[int],
    },
    total=False,
)

ListJobsHeaders = TypedDict("ListJobsHeaders", {}, total=False)

type ListJobsRequestBody = None
type ListJobsSuccessResponse = JobHistoryPageResponse
ListJobsResponses = TypedDict(
    "ListJobsResponses",
    {
        "200": JobHistoryPageResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
ListJobsSuccessResponses = TypedDict("ListJobsSuccessResponses", {"200": JobHistoryPageResponse})
ListJobsErrorResponses = TypedDict(
    "ListJobsErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class ListJobsOperation(TypedDict):
    request: ListJobsRequestBody
    response: ListJobsSuccessResponse
    responses: ListJobsResponses
    successes: ListJobsSuccessResponses
    errors: ListJobsErrorResponses
    parameters: ListJobsParameters
    headers: ListJobsHeaders


GetJobParameters = TypedDict("GetJobParameters", {"job_id": Required[str]}, total=False)

GetJobHeaders = TypedDict("GetJobHeaders", {}, total=False)

type GetJobRequestBody = None
type GetJobSuccessResponse = JobResponse
GetJobResponses = TypedDict(
    "GetJobResponses",
    {
        "200": JobResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
GetJobSuccessResponses = TypedDict("GetJobSuccessResponses", {"200": JobResponse})
GetJobErrorResponses = TypedDict(
    "GetJobErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class GetJobOperation(TypedDict):
    request: GetJobRequestBody
    response: GetJobSuccessResponse
    responses: GetJobResponses
    successes: GetJobSuccessResponses
    errors: GetJobErrorResponses
    parameters: GetJobParameters
    headers: GetJobHeaders


CancelJobParameters = TypedDict("CancelJobParameters", {"job_id": Required[str]}, total=False)

CancelJobHeaders = TypedDict("CancelJobHeaders", {"Idempotency-Key": Required[str]}, total=False)

type CancelJobRequestBody = CancelJobRequest
type CancelJobSuccessResponse = JobResponse
CancelJobResponses = TypedDict(
    "CancelJobResponses",
    {
        "200": JobResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
CancelJobSuccessResponses = TypedDict("CancelJobSuccessResponses", {"200": JobResponse})
CancelJobErrorResponses = TypedDict(
    "CancelJobErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class CancelJobOperation(TypedDict):
    request: CancelJobRequestBody
    response: CancelJobSuccessResponse
    responses: CancelJobResponses
    successes: CancelJobSuccessResponses
    errors: CancelJobErrorResponses
    parameters: CancelJobParameters
    headers: CancelJobHeaders


CreateMarkingCheckParameters = TypedDict("CreateMarkingCheckParameters", {}, total=False)

CreateMarkingCheckHeaders = TypedDict(
    "CreateMarkingCheckHeaders", {"Idempotency-Key": Required[str]}, total=False
)

type CreateMarkingCheckRequestBody = MarkingCheckRequest
type CreateMarkingCheckSuccessResponse = MarkingCheckResponse
CreateMarkingCheckResponses = TypedDict(
    "CreateMarkingCheckResponses",
    {
        "202": MarkingCheckResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
CreateMarkingCheckSuccessResponses = TypedDict(
    "CreateMarkingCheckSuccessResponses", {"202": MarkingCheckResponse}
)
CreateMarkingCheckErrorResponses = TypedDict(
    "CreateMarkingCheckErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class CreateMarkingCheckOperation(TypedDict):
    request: CreateMarkingCheckRequestBody
    response: CreateMarkingCheckSuccessResponse
    responses: CreateMarkingCheckResponses
    successes: CreateMarkingCheckSuccessResponses
    errors: CreateMarkingCheckErrorResponses
    parameters: CreateMarkingCheckParameters
    headers: CreateMarkingCheckHeaders


GetMarkingCheckParameters = TypedDict(
    "GetMarkingCheckParameters", {"marking_check_id": Required[str]}, total=False
)

GetMarkingCheckHeaders = TypedDict("GetMarkingCheckHeaders", {}, total=False)

type GetMarkingCheckRequestBody = None
type GetMarkingCheckSuccessResponse = MarkingCheckResponse
GetMarkingCheckResponses = TypedDict(
    "GetMarkingCheckResponses",
    {
        "200": MarkingCheckResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
GetMarkingCheckSuccessResponses = TypedDict(
    "GetMarkingCheckSuccessResponses", {"200": MarkingCheckResponse}
)
GetMarkingCheckErrorResponses = TypedDict(
    "GetMarkingCheckErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class GetMarkingCheckOperation(TypedDict):
    request: GetMarkingCheckRequestBody
    response: GetMarkingCheckSuccessResponse
    responses: GetMarkingCheckResponses
    successes: GetMarkingCheckSuccessResponses
    errors: GetMarkingCheckErrorResponses
    parameters: GetMarkingCheckParameters
    headers: GetMarkingCheckHeaders


GetCurrentUserParameters = TypedDict("GetCurrentUserParameters", {}, total=False)

GetCurrentUserHeaders = TypedDict("GetCurrentUserHeaders", {}, total=False)

type GetCurrentUserRequestBody = None
type GetCurrentUserSuccessResponse = MeResponse
GetCurrentUserResponses = TypedDict(
    "GetCurrentUserResponses",
    {
        "200": MeResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
GetCurrentUserSuccessResponses = TypedDict("GetCurrentUserSuccessResponses", {"200": MeResponse})
GetCurrentUserErrorResponses = TypedDict(
    "GetCurrentUserErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class GetCurrentUserOperation(TypedDict):
    request: GetCurrentUserRequestBody
    response: GetCurrentUserSuccessResponse
    responses: GetCurrentUserResponses
    successes: GetCurrentUserSuccessResponses
    errors: GetCurrentUserErrorResponses
    parameters: GetCurrentUserParameters
    headers: GetCurrentUserHeaders


GetOverviewParameters = TypedDict(
    "GetOverviewParameters",
    {"range": NotRequired[Literal["7d"] | Literal["30d"] | Literal["12m"]]},
    total=False,
)

GetOverviewHeaders = TypedDict("GetOverviewHeaders", {}, total=False)

type GetOverviewRequestBody = None
type GetOverviewSuccessResponse = OverviewResponse
GetOverviewResponses = TypedDict(
    "GetOverviewResponses",
    {
        "200": OverviewResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
GetOverviewSuccessResponses = TypedDict("GetOverviewSuccessResponses", {"200": OverviewResponse})
GetOverviewErrorResponses = TypedDict(
    "GetOverviewErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class GetOverviewOperation(TypedDict):
    request: GetOverviewRequestBody
    response: GetOverviewSuccessResponse
    responses: GetOverviewResponses
    successes: GetOverviewSuccessResponses
    errors: GetOverviewErrorResponses
    parameters: GetOverviewParameters
    headers: GetOverviewHeaders


GetPublicVerifyPageParameters = TypedDict(
    "GetPublicVerifyPageParameters", {"slug": Required[str]}, total=False
)

GetPublicVerifyPageHeaders = TypedDict("GetPublicVerifyPageHeaders", {}, total=False)

type GetPublicVerifyPageRequestBody = None
type GetPublicVerifyPageSuccessResponse = PublicVerifyPageResponse
GetPublicVerifyPageResponses = TypedDict(
    "GetPublicVerifyPageResponses",
    {
        "200": PublicVerifyPageResponse,
        "404": ErrorResponse,
        "422": ErrorResponse,
        "503": ErrorResponse,
    },
)
GetPublicVerifyPageSuccessResponses = TypedDict(
    "GetPublicVerifyPageSuccessResponses", {"200": PublicVerifyPageResponse}
)
GetPublicVerifyPageErrorResponses = TypedDict(
    "GetPublicVerifyPageErrorResponses",
    {"404": ErrorResponse, "422": ErrorResponse, "503": ErrorResponse},
)


class GetPublicVerifyPageOperation(TypedDict):
    request: GetPublicVerifyPageRequestBody
    response: GetPublicVerifyPageSuccessResponse
    responses: GetPublicVerifyPageResponses
    successes: GetPublicVerifyPageSuccessResponses
    errors: GetPublicVerifyPageErrorResponses
    parameters: GetPublicVerifyPageParameters
    headers: GetPublicVerifyPageHeaders


CreatePublicCheckParameters = TypedDict(
    "CreatePublicCheckParameters", {"slug": Required[str]}, total=False
)

CreatePublicCheckHeaders = TypedDict("CreatePublicCheckHeaders", {}, total=False)

type CreatePublicCheckRequestBody = None
type CreatePublicCheckSuccessResponse = PublicCheckResponse
CreatePublicCheckResponses = TypedDict(
    "CreatePublicCheckResponses",
    {
        "200": PublicCheckResponse,
        "202": PublicCheckResponse,
        "404": ErrorResponse,
        "413": ErrorResponse,
        "415": ErrorResponse,
        "422": ErrorResponse,
        "429": ErrorResponse,
        "503": ErrorResponse,
    },
)
CreatePublicCheckSuccessResponses = TypedDict(
    "CreatePublicCheckSuccessResponses", {"200": PublicCheckResponse, "202": PublicCheckResponse}
)
CreatePublicCheckErrorResponses = TypedDict(
    "CreatePublicCheckErrorResponses",
    {
        "404": ErrorResponse,
        "413": ErrorResponse,
        "415": ErrorResponse,
        "422": ErrorResponse,
        "429": ErrorResponse,
        "503": ErrorResponse,
    },
)


class CreatePublicCheckOperation(TypedDict):
    request: CreatePublicCheckRequestBody
    response: CreatePublicCheckSuccessResponse
    responses: CreatePublicCheckResponses
    successes: CreatePublicCheckSuccessResponses
    errors: CreatePublicCheckErrorResponses
    parameters: CreatePublicCheckParameters
    headers: CreatePublicCheckHeaders


GetPublicCheckParameters = TypedDict(
    "GetPublicCheckParameters", {"slug": Required[str], "check_id": Required[str]}, total=False
)

GetPublicCheckHeaders = TypedDict("GetPublicCheckHeaders", {}, total=False)

type GetPublicCheckRequestBody = None
type GetPublicCheckSuccessResponse = PublicCheckResponse
GetPublicCheckResponses = TypedDict(
    "GetPublicCheckResponses",
    {"200": PublicCheckResponse, "404": ErrorResponse, "422": ErrorResponse, "503": ErrorResponse},
)
GetPublicCheckSuccessResponses = TypedDict(
    "GetPublicCheckSuccessResponses", {"200": PublicCheckResponse}
)
GetPublicCheckErrorResponses = TypedDict(
    "GetPublicCheckErrorResponses",
    {"404": ErrorResponse, "422": ErrorResponse, "503": ErrorResponse},
)


class GetPublicCheckOperation(TypedDict):
    request: GetPublicCheckRequestBody
    response: GetPublicCheckSuccessResponse
    responses: GetPublicCheckResponses
    successes: GetPublicCheckSuccessResponses
    errors: GetPublicCheckErrorResponses
    parameters: GetPublicCheckParameters
    headers: GetPublicCheckHeaders


GetPublicVerifyPageLogoParameters = TypedDict(
    "GetPublicVerifyPageLogoParameters", {"slug": Required[str]}, total=False
)

GetPublicVerifyPageLogoHeaders = TypedDict("GetPublicVerifyPageLogoHeaders", {}, total=False)

type GetPublicVerifyPageLogoRequestBody = None
type GetPublicVerifyPageLogoSuccessResponse = None
GetPublicVerifyPageLogoResponses = TypedDict(
    "GetPublicVerifyPageLogoResponses",
    {"200": str, "404": ErrorResponse, "422": ErrorResponse, "503": ErrorResponse},
)
GetPublicVerifyPageLogoSuccessResponses = TypedDict(
    "GetPublicVerifyPageLogoSuccessResponses", {"200": str}
)
GetPublicVerifyPageLogoErrorResponses = TypedDict(
    "GetPublicVerifyPageLogoErrorResponses",
    {"404": ErrorResponse, "422": ErrorResponse, "503": ErrorResponse},
)


class GetPublicVerifyPageLogoOperation(TypedDict):
    request: GetPublicVerifyPageLogoRequestBody
    response: GetPublicVerifyPageLogoSuccessResponse
    responses: GetPublicVerifyPageLogoResponses
    successes: GetPublicVerifyPageLogoSuccessResponses
    errors: GetPublicVerifyPageLogoErrorResponses
    parameters: GetPublicVerifyPageLogoParameters
    headers: GetPublicVerifyPageLogoHeaders


ListReceiptsParameters = TypedDict(
    "ListReceiptsParameters",
    {
        "asset_id": NotRequired[str | None],
        "job_id": NotRequired[str | None],
        "cursor": NotRequired[str | None],
        "limit": NotRequired[int],
    },
    total=False,
)

ListReceiptsHeaders = TypedDict("ListReceiptsHeaders", {}, total=False)

type ListReceiptsRequestBody = None
type ListReceiptsSuccessResponse = ReceiptHistoryPageResponse
ListReceiptsResponses = TypedDict(
    "ListReceiptsResponses",
    {
        "200": ReceiptHistoryPageResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
ListReceiptsSuccessResponses = TypedDict(
    "ListReceiptsSuccessResponses", {"200": ReceiptHistoryPageResponse}
)
ListReceiptsErrorResponses = TypedDict(
    "ListReceiptsErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class ListReceiptsOperation(TypedDict):
    request: ListReceiptsRequestBody
    response: ListReceiptsSuccessResponse
    responses: ListReceiptsResponses
    successes: ListReceiptsSuccessResponses
    errors: ListReceiptsErrorResponses
    parameters: ListReceiptsParameters
    headers: ListReceiptsHeaders


GetSigningReceiptParameters = TypedDict(
    "GetSigningReceiptParameters", {"receipt_id": Required[str]}, total=False
)

GetSigningReceiptHeaders = TypedDict("GetSigningReceiptHeaders", {}, total=False)

type GetSigningReceiptRequestBody = None
type GetSigningReceiptSuccessResponse = ReceiptResponse
GetSigningReceiptResponses = TypedDict(
    "GetSigningReceiptResponses",
    {
        "200": ReceiptResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
GetSigningReceiptSuccessResponses = TypedDict(
    "GetSigningReceiptSuccessResponses", {"200": ReceiptResponse}
)
GetSigningReceiptErrorResponses = TypedDict(
    "GetSigningReceiptErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class GetSigningReceiptOperation(TypedDict):
    request: GetSigningReceiptRequestBody
    response: GetSigningReceiptSuccessResponse
    responses: GetSigningReceiptResponses
    successes: GetSigningReceiptSuccessResponses
    errors: GetSigningReceiptErrorResponses
    parameters: GetSigningReceiptParameters
    headers: GetSigningReceiptHeaders


ListRecipesParameters = TypedDict("ListRecipesParameters", {}, total=False)

ListRecipesHeaders = TypedDict("ListRecipesHeaders", {}, total=False)

type ListRecipesRequestBody = None
type ListRecipesSuccessResponse = RecipeListResponse
ListRecipesResponses = TypedDict(
    "ListRecipesResponses",
    {
        "200": RecipeListResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
ListRecipesSuccessResponses = TypedDict("ListRecipesSuccessResponses", {"200": RecipeListResponse})
ListRecipesErrorResponses = TypedDict(
    "ListRecipesErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class ListRecipesOperation(TypedDict):
    request: ListRecipesRequestBody
    response: ListRecipesSuccessResponse
    responses: ListRecipesResponses
    successes: ListRecipesSuccessResponses
    errors: ListRecipesErrorResponses
    parameters: ListRecipesParameters
    headers: ListRecipesHeaders


GetRecipeParameters = TypedDict("GetRecipeParameters", {"recipe_id": Required[str]}, total=False)

GetRecipeHeaders = TypedDict("GetRecipeHeaders", {}, total=False)

type GetRecipeRequestBody = None
type GetRecipeSuccessResponse = RecipeCatalogResponse
GetRecipeResponses = TypedDict(
    "GetRecipeResponses",
    {
        "200": RecipeCatalogResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
GetRecipeSuccessResponses = TypedDict("GetRecipeSuccessResponses", {"200": RecipeCatalogResponse})
GetRecipeErrorResponses = TypedDict(
    "GetRecipeErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class GetRecipeOperation(TypedDict):
    request: GetRecipeRequestBody
    response: GetRecipeSuccessResponse
    responses: GetRecipeResponses
    successes: GetRecipeSuccessResponses
    errors: GetRecipeErrorResponses
    parameters: GetRecipeParameters
    headers: GetRecipeHeaders


GetSharedVerificationParameters = TypedDict(
    "GetSharedVerificationParameters", {"token": Required[str]}, total=False
)

GetSharedVerificationHeaders = TypedDict("GetSharedVerificationHeaders", {}, total=False)

type GetSharedVerificationRequestBody = None
type GetSharedVerificationSuccessResponse = SharedVerificationResponse
GetSharedVerificationResponses = TypedDict(
    "GetSharedVerificationResponses",
    {"200": SharedVerificationResponse, "404": ErrorResponse, "422": HTTPValidationError},
)
GetSharedVerificationSuccessResponses = TypedDict(
    "GetSharedVerificationSuccessResponses", {"200": SharedVerificationResponse}
)
GetSharedVerificationErrorResponses = TypedDict(
    "GetSharedVerificationErrorResponses", {"404": ErrorResponse, "422": HTTPValidationError}
)


class GetSharedVerificationOperation(TypedDict):
    request: GetSharedVerificationRequestBody
    response: GetSharedVerificationSuccessResponse
    responses: GetSharedVerificationResponses
    successes: GetSharedVerificationSuccessResponses
    errors: GetSharedVerificationErrorResponses
    parameters: GetSharedVerificationParameters
    headers: GetSharedVerificationHeaders


AcceptSigningJobParameters = TypedDict("AcceptSigningJobParameters", {}, total=False)

AcceptSigningJobHeaders = TypedDict(
    "AcceptSigningJobHeaders", {"Idempotency-Key": Required[str]}, total=False
)

type AcceptSigningJobRequestBody = SignRequest
type AcceptSigningJobSuccessResponse = ExpressSignResponse
AcceptSigningJobResponses = TypedDict(
    "AcceptSigningJobResponses",
    {
        "200": ExpressSignResponse,
        "202": JobResponse,
        "401": HttpErrorResponse,
        "402": ErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
AcceptSigningJobSuccessResponses = TypedDict(
    "AcceptSigningJobSuccessResponses", {"200": ExpressSignResponse, "202": JobResponse}
)
AcceptSigningJobErrorResponses = TypedDict(
    "AcceptSigningJobErrorResponses",
    {
        "401": HttpErrorResponse,
        "402": ErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class AcceptSigningJobOperation(TypedDict):
    request: AcceptSigningJobRequestBody
    response: AcceptSigningJobSuccessResponse
    responses: AcceptSigningJobResponses
    successes: AcceptSigningJobSuccessResponses
    errors: AcceptSigningJobErrorResponses
    parameters: AcceptSigningJobParameters
    headers: AcceptSigningJobHeaders


AcceptSigningJobBatchParameters = TypedDict("AcceptSigningJobBatchParameters", {}, total=False)

AcceptSigningJobBatchHeaders = TypedDict(
    "AcceptSigningJobBatchHeaders", {"Idempotency-Key": Required[str]}, total=False
)

type AcceptSigningJobBatchRequestBody = SignBatchRequest
type AcceptSigningJobBatchSuccessResponse = SignBatchResponse
AcceptSigningJobBatchResponses = TypedDict(
    "AcceptSigningJobBatchResponses",
    {
        "202": SignBatchResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
AcceptSigningJobBatchSuccessResponses = TypedDict(
    "AcceptSigningJobBatchSuccessResponses", {"202": SignBatchResponse}
)
AcceptSigningJobBatchErrorResponses = TypedDict(
    "AcceptSigningJobBatchErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class AcceptSigningJobBatchOperation(TypedDict):
    request: AcceptSigningJobBatchRequestBody
    response: AcceptSigningJobBatchSuccessResponse
    responses: AcceptSigningJobBatchResponses
    successes: AcceptSigningJobBatchSuccessResponses
    errors: AcceptSigningJobBatchErrorResponses
    parameters: AcceptSigningJobBatchParameters
    headers: AcceptSigningJobBatchHeaders


CreateUploadParameters = TypedDict("CreateUploadParameters", {}, total=False)

CreateUploadHeaders = TypedDict("CreateUploadHeaders", {}, total=False)

type CreateUploadRequestBody = CreateUploadRequest
type CreateUploadSuccessResponse = CreateUploadResponse
CreateUploadResponses = TypedDict(
    "CreateUploadResponses",
    {
        "201": CreateUploadResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
CreateUploadSuccessResponses = TypedDict(
    "CreateUploadSuccessResponses", {"201": CreateUploadResponse}
)
CreateUploadErrorResponses = TypedDict(
    "CreateUploadErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class CreateUploadOperation(TypedDict):
    request: CreateUploadRequestBody
    response: CreateUploadSuccessResponse
    responses: CreateUploadResponses
    successes: CreateUploadSuccessResponses
    errors: CreateUploadErrorResponses
    parameters: CreateUploadParameters
    headers: CreateUploadHeaders


AbortUploadParameters = TypedDict(
    "AbortUploadParameters", {"upload_id": Required[str]}, total=False
)

AbortUploadHeaders = TypedDict("AbortUploadHeaders", {}, total=False)

type AbortUploadRequestBody = None
type AbortUploadSuccessResponse = AbortUploadResponse
AbortUploadResponses = TypedDict(
    "AbortUploadResponses",
    {
        "200": AbortUploadResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
AbortUploadSuccessResponses = TypedDict("AbortUploadSuccessResponses", {"200": AbortUploadResponse})
AbortUploadErrorResponses = TypedDict(
    "AbortUploadErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class AbortUploadOperation(TypedDict):
    request: AbortUploadRequestBody
    response: AbortUploadSuccessResponse
    responses: AbortUploadResponses
    successes: AbortUploadSuccessResponses
    errors: AbortUploadErrorResponses
    parameters: AbortUploadParameters
    headers: AbortUploadHeaders


CompleteUploadParameters = TypedDict(
    "CompleteUploadParameters", {"upload_id": Required[str]}, total=False
)

CompleteUploadHeaders = TypedDict(
    "CompleteUploadHeaders", {"Idempotency-Key": Required[str]}, total=False
)

type CompleteUploadRequestBody = CompleteUploadRequest
type CompleteUploadSuccessResponse = CompleteUploadResponse
CompleteUploadResponses = TypedDict(
    "CompleteUploadResponses",
    {
        "200": CompleteUploadResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "410": ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
CompleteUploadSuccessResponses = TypedDict(
    "CompleteUploadSuccessResponses", {"200": CompleteUploadResponse}
)
CompleteUploadErrorResponses = TypedDict(
    "CompleteUploadErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "410": ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class CompleteUploadOperation(TypedDict):
    request: CompleteUploadRequestBody
    response: CompleteUploadSuccessResponse
    responses: CompleteUploadResponses
    successes: CompleteUploadSuccessResponses
    errors: CompleteUploadErrorResponses
    parameters: CompleteUploadParameters
    headers: CompleteUploadHeaders


GetUsageParameters = TypedDict(
    "GetUsageParameters",
    {"period": NotRequired[str | None], "item_limit": NotRequired[int]},
    total=False,
)

GetUsageHeaders = TypedDict("GetUsageHeaders", {}, total=False)

type GetUsageRequestBody = None
type GetUsageSuccessResponse = UsageResponse
GetUsageResponses = TypedDict(
    "GetUsageResponses",
    {
        "200": UsageResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
GetUsageSuccessResponses = TypedDict("GetUsageSuccessResponses", {"200": UsageResponse})
GetUsageErrorResponses = TypedDict(
    "GetUsageErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class GetUsageOperation(TypedDict):
    request: GetUsageRequestBody
    response: GetUsageSuccessResponse
    responses: GetUsageResponses
    successes: GetUsageSuccessResponses
    errors: GetUsageErrorResponses
    parameters: GetUsageParameters
    headers: GetUsageHeaders


GetVerificationEvidenceParameters = TypedDict(
    "GetVerificationEvidenceParameters", {"verification_id": Required[str]}, total=False
)

GetVerificationEvidenceHeaders = TypedDict("GetVerificationEvidenceHeaders", {}, total=False)

type GetVerificationEvidenceRequestBody = None
type GetVerificationEvidenceSuccessResponse = VerificationEvidenceResponse
GetVerificationEvidenceResponses = TypedDict(
    "GetVerificationEvidenceResponses",
    {
        "200": VerificationEvidenceResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
GetVerificationEvidenceSuccessResponses = TypedDict(
    "GetVerificationEvidenceSuccessResponses", {"200": VerificationEvidenceResponse}
)
GetVerificationEvidenceErrorResponses = TypedDict(
    "GetVerificationEvidenceErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class GetVerificationEvidenceOperation(TypedDict):
    request: GetVerificationEvidenceRequestBody
    response: GetVerificationEvidenceSuccessResponse
    responses: GetVerificationEvidenceResponses
    successes: GetVerificationEvidenceSuccessResponses
    errors: GetVerificationEvidenceErrorResponses
    parameters: GetVerificationEvidenceParameters
    headers: GetVerificationEvidenceHeaders


CreateVerificationReportParameters = TypedDict(
    "CreateVerificationReportParameters", {"verification_id": Required[str]}, total=False
)

CreateVerificationReportHeaders = TypedDict("CreateVerificationReportHeaders", {}, total=False)

type CreateVerificationReportRequestBody = CreateReportRequest
type CreateVerificationReportSuccessResponse = ReportResponse
CreateVerificationReportResponses = TypedDict(
    "CreateVerificationReportResponses",
    {
        "202": ReportResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
CreateVerificationReportSuccessResponses = TypedDict(
    "CreateVerificationReportSuccessResponses", {"202": ReportResponse}
)
CreateVerificationReportErrorResponses = TypedDict(
    "CreateVerificationReportErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class CreateVerificationReportOperation(TypedDict):
    request: CreateVerificationReportRequestBody
    response: CreateVerificationReportSuccessResponse
    responses: CreateVerificationReportResponses
    successes: CreateVerificationReportSuccessResponses
    errors: CreateVerificationReportErrorResponses
    parameters: CreateVerificationReportParameters
    headers: CreateVerificationReportHeaders


ListVerificationSharesParameters = TypedDict(
    "ListVerificationSharesParameters",
    {
        "verification_id": Required[str],
        "cursor": NotRequired[str | None],
        "limit": NotRequired[int],
    },
    total=False,
)

ListVerificationSharesHeaders = TypedDict("ListVerificationSharesHeaders", {}, total=False)

type ListVerificationSharesRequestBody = None
type ListVerificationSharesSuccessResponse = VerificationSharePageResponse
ListVerificationSharesResponses = TypedDict(
    "ListVerificationSharesResponses",
    {
        "200": VerificationSharePageResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
ListVerificationSharesSuccessResponses = TypedDict(
    "ListVerificationSharesSuccessResponses", {"200": VerificationSharePageResponse}
)
ListVerificationSharesErrorResponses = TypedDict(
    "ListVerificationSharesErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class ListVerificationSharesOperation(TypedDict):
    request: ListVerificationSharesRequestBody
    response: ListVerificationSharesSuccessResponse
    responses: ListVerificationSharesResponses
    successes: ListVerificationSharesSuccessResponses
    errors: ListVerificationSharesErrorResponses
    parameters: ListVerificationSharesParameters
    headers: ListVerificationSharesHeaders


CreateVerificationShareParameters = TypedDict(
    "CreateVerificationShareParameters", {"verification_id": Required[str]}, total=False
)

CreateVerificationShareHeaders = TypedDict(
    "CreateVerificationShareHeaders", {"Idempotency-Key": Required[str]}, total=False
)

type CreateVerificationShareRequestBody = CreateShareRequest
type CreateVerificationShareSuccessResponse = CreateShareResponse
CreateVerificationShareResponses = TypedDict(
    "CreateVerificationShareResponses",
    {
        "201": CreateShareResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
CreateVerificationShareSuccessResponses = TypedDict(
    "CreateVerificationShareSuccessResponses", {"201": CreateShareResponse}
)
CreateVerificationShareErrorResponses = TypedDict(
    "CreateVerificationShareErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class CreateVerificationShareOperation(TypedDict):
    request: CreateVerificationShareRequestBody
    response: CreateVerificationShareSuccessResponse
    responses: CreateVerificationShareResponses
    successes: CreateVerificationShareSuccessResponses
    errors: CreateVerificationShareErrorResponses
    parameters: CreateVerificationShareParameters
    headers: CreateVerificationShareHeaders


GetVerificationHistoryParameters = TypedDict(
    "GetVerificationHistoryParameters", {"verification_id": Required[str]}, total=False
)

GetVerificationHistoryHeaders = TypedDict("GetVerificationHistoryHeaders", {}, total=False)

type GetVerificationHistoryRequestBody = None
type GetVerificationHistorySuccessResponse = VerificationHistoryResponse
GetVerificationHistoryResponses = TypedDict(
    "GetVerificationHistoryResponses",
    {
        "200": VerificationHistoryResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
GetVerificationHistorySuccessResponses = TypedDict(
    "GetVerificationHistorySuccessResponses", {"200": VerificationHistoryResponse}
)
GetVerificationHistoryErrorResponses = TypedDict(
    "GetVerificationHistoryErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class GetVerificationHistoryOperation(TypedDict):
    request: GetVerificationHistoryRequestBody
    response: GetVerificationHistorySuccessResponse
    responses: GetVerificationHistoryResponses
    successes: GetVerificationHistorySuccessResponses
    errors: GetVerificationHistoryErrorResponses
    parameters: GetVerificationHistoryParameters
    headers: GetVerificationHistoryHeaders


GetVerificationReportParameters = TypedDict(
    "GetVerificationReportParameters", {"report_id": Required[str]}, total=False
)

GetVerificationReportHeaders = TypedDict("GetVerificationReportHeaders", {}, total=False)

type GetVerificationReportRequestBody = None
type GetVerificationReportSuccessResponse = ReportContentResponse
GetVerificationReportResponses = TypedDict(
    "GetVerificationReportResponses",
    {
        "200": ReportContentResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
GetVerificationReportSuccessResponses = TypedDict(
    "GetVerificationReportSuccessResponses", {"200": ReportContentResponse}
)
GetVerificationReportErrorResponses = TypedDict(
    "GetVerificationReportErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class GetVerificationReportOperation(TypedDict):
    request: GetVerificationReportRequestBody
    response: GetVerificationReportSuccessResponse
    responses: GetVerificationReportResponses
    successes: GetVerificationReportSuccessResponses
    errors: GetVerificationReportErrorResponses
    parameters: GetVerificationReportParameters
    headers: GetVerificationReportHeaders


CloseVerificationShareParameters = TypedDict(
    "CloseVerificationShareParameters", {"share_id": Required[str]}, total=False
)

CloseVerificationShareHeaders = TypedDict("CloseVerificationShareHeaders", {}, total=False)

type CloseVerificationShareRequestBody = CloseShareRequest
type CloseVerificationShareSuccessResponse = CloseShareResponse
CloseVerificationShareResponses = TypedDict(
    "CloseVerificationShareResponses",
    {
        "200": CloseShareResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
CloseVerificationShareSuccessResponses = TypedDict(
    "CloseVerificationShareSuccessResponses", {"200": CloseShareResponse}
)
CloseVerificationShareErrorResponses = TypedDict(
    "CloseVerificationShareErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class CloseVerificationShareOperation(TypedDict):
    request: CloseVerificationShareRequestBody
    response: CloseVerificationShareSuccessResponse
    responses: CloseVerificationShareResponses
    successes: CloseVerificationShareSuccessResponses
    errors: CloseVerificationShareErrorResponses
    parameters: CloseVerificationShareParameters
    headers: CloseVerificationShareHeaders


ListVerificationsParameters = TypedDict(
    "ListVerificationsParameters",
    {
        "overall": NotRequired[VerificationOverall | None],
        "subject_type": NotRequired[VerificationSubjectType | None],
        "cursor": NotRequired[str | None],
        "limit": NotRequired[int],
    },
    total=False,
)

ListVerificationsHeaders = TypedDict("ListVerificationsHeaders", {}, total=False)

type ListVerificationsRequestBody = None
type ListVerificationsSuccessResponse = VerificationHistoryPageResponse
ListVerificationsResponses = TypedDict(
    "ListVerificationsResponses",
    {
        "200": VerificationHistoryPageResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
ListVerificationsSuccessResponses = TypedDict(
    "ListVerificationsSuccessResponses", {"200": VerificationHistoryPageResponse}
)
ListVerificationsErrorResponses = TypedDict(
    "ListVerificationsErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class ListVerificationsOperation(TypedDict):
    request: ListVerificationsRequestBody
    response: ListVerificationsSuccessResponse
    responses: ListVerificationsResponses
    successes: ListVerificationsSuccessResponses
    errors: ListVerificationsErrorResponses
    parameters: ListVerificationsParameters
    headers: ListVerificationsHeaders


CreateVerificationParameters = TypedDict("CreateVerificationParameters", {}, total=False)

CreateVerificationHeaders = TypedDict(
    "CreateVerificationHeaders", {"Idempotency-Key": Required[str]}, total=False
)

type CreateVerificationRequestBody = CreateVerificationRequest
type CreateVerificationSuccessResponse = VerificationResponse
CreateVerificationResponses = TypedDict(
    "CreateVerificationResponses",
    {
        "202": VerificationResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
CreateVerificationSuccessResponses = TypedDict(
    "CreateVerificationSuccessResponses", {"202": VerificationResponse}
)
CreateVerificationErrorResponses = TypedDict(
    "CreateVerificationErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class CreateVerificationOperation(TypedDict):
    request: CreateVerificationRequestBody
    response: CreateVerificationSuccessResponse
    responses: CreateVerificationResponses
    successes: CreateVerificationSuccessResponses
    errors: CreateVerificationErrorResponses
    parameters: CreateVerificationParameters
    headers: CreateVerificationHeaders


GetVerificationParameters = TypedDict(
    "GetVerificationParameters", {"verification_id": Required[str]}, total=False
)

GetVerificationHeaders = TypedDict("GetVerificationHeaders", {}, total=False)

type GetVerificationRequestBody = None
type GetVerificationSuccessResponse = VerificationResponse
GetVerificationResponses = TypedDict(
    "GetVerificationResponses",
    {
        "200": VerificationResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
GetVerificationSuccessResponses = TypedDict(
    "GetVerificationSuccessResponses", {"200": VerificationResponse}
)
GetVerificationErrorResponses = TypedDict(
    "GetVerificationErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class GetVerificationOperation(TypedDict):
    request: GetVerificationRequestBody
    response: GetVerificationSuccessResponse
    responses: GetVerificationResponses
    successes: GetVerificationSuccessResponses
    errors: GetVerificationErrorResponses
    parameters: GetVerificationParameters
    headers: GetVerificationHeaders


CreateVerificationBatchParameters = TypedDict("CreateVerificationBatchParameters", {}, total=False)

CreateVerificationBatchHeaders = TypedDict(
    "CreateVerificationBatchHeaders", {"Idempotency-Key": Required[str]}, total=False
)

type CreateVerificationBatchRequestBody = VerificationBatchRequest
type CreateVerificationBatchSuccessResponse = VerificationBatchResponse
CreateVerificationBatchResponses = TypedDict(
    "CreateVerificationBatchResponses",
    {
        "202": VerificationBatchResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
CreateVerificationBatchSuccessResponses = TypedDict(
    "CreateVerificationBatchSuccessResponses", {"202": VerificationBatchResponse}
)
CreateVerificationBatchErrorResponses = TypedDict(
    "CreateVerificationBatchErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class CreateVerificationBatchOperation(TypedDict):
    request: CreateVerificationBatchRequestBody
    response: CreateVerificationBatchSuccessResponse
    responses: CreateVerificationBatchResponses
    successes: CreateVerificationBatchSuccessResponses
    errors: CreateVerificationBatchErrorResponses
    parameters: CreateVerificationBatchParameters
    headers: CreateVerificationBatchHeaders


GetVerifyPageParameters = TypedDict("GetVerifyPageParameters", {}, total=False)

GetVerifyPageHeaders = TypedDict("GetVerifyPageHeaders", {}, total=False)

type GetVerifyPageRequestBody = None
type GetVerifyPageSuccessResponse = VerifyPageResponse
GetVerifyPageResponses = TypedDict(
    "GetVerifyPageResponses",
    {
        "200": VerifyPageResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
GetVerifyPageSuccessResponses = TypedDict(
    "GetVerifyPageSuccessResponses", {"200": VerifyPageResponse}
)
GetVerifyPageErrorResponses = TypedDict(
    "GetVerifyPageErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class GetVerifyPageOperation(TypedDict):
    request: GetVerifyPageRequestBody
    response: GetVerifyPageSuccessResponse
    responses: GetVerifyPageResponses
    successes: GetVerifyPageSuccessResponses
    errors: GetVerifyPageErrorResponses
    parameters: GetVerifyPageParameters
    headers: GetVerifyPageHeaders


PutVerifyPageParameters = TypedDict("PutVerifyPageParameters", {}, total=False)

PutVerifyPageHeaders = TypedDict("PutVerifyPageHeaders", {}, total=False)

type PutVerifyPageRequestBody = VerifyPageUpdateRequest
type PutVerifyPageSuccessResponse = VerifyPageResponse
PutVerifyPageResponses = TypedDict(
    "PutVerifyPageResponses",
    {
        "200": VerifyPageResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
PutVerifyPageSuccessResponses = TypedDict(
    "PutVerifyPageSuccessResponses", {"200": VerifyPageResponse}
)
PutVerifyPageErrorResponses = TypedDict(
    "PutVerifyPageErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class PutVerifyPageOperation(TypedDict):
    request: PutVerifyPageRequestBody
    response: PutVerifyPageSuccessResponse
    responses: PutVerifyPageResponses
    successes: PutVerifyPageSuccessResponses
    errors: PutVerifyPageErrorResponses
    parameters: PutVerifyPageParameters
    headers: PutVerifyPageHeaders


ListWebhookEndpointsParameters = TypedDict(
    "ListWebhookEndpointsParameters",
    {
        "limit": NotRequired[int],
        "cursor": NotRequired[str | None],
        "include_deleted": NotRequired[bool],
    },
    total=False,
)

ListWebhookEndpointsHeaders = TypedDict("ListWebhookEndpointsHeaders", {}, total=False)

type ListWebhookEndpointsRequestBody = None
type ListWebhookEndpointsSuccessResponse = WebhookEndpointPageResponse
ListWebhookEndpointsResponses = TypedDict(
    "ListWebhookEndpointsResponses",
    {
        "200": WebhookEndpointPageResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
ListWebhookEndpointsSuccessResponses = TypedDict(
    "ListWebhookEndpointsSuccessResponses", {"200": WebhookEndpointPageResponse}
)
ListWebhookEndpointsErrorResponses = TypedDict(
    "ListWebhookEndpointsErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class ListWebhookEndpointsOperation(TypedDict):
    request: ListWebhookEndpointsRequestBody
    response: ListWebhookEndpointsSuccessResponse
    responses: ListWebhookEndpointsResponses
    successes: ListWebhookEndpointsSuccessResponses
    errors: ListWebhookEndpointsErrorResponses
    parameters: ListWebhookEndpointsParameters
    headers: ListWebhookEndpointsHeaders


CreateWebhookEndpointParameters = TypedDict("CreateWebhookEndpointParameters", {}, total=False)

CreateWebhookEndpointHeaders = TypedDict(
    "CreateWebhookEndpointHeaders", {"Idempotency-Key": Required[str]}, total=False
)

type CreateWebhookEndpointRequestBody = CreateWebhookEndpointRequest
type CreateWebhookEndpointSuccessResponse = IssuedWebhookEndpointResponse
CreateWebhookEndpointResponses = TypedDict(
    "CreateWebhookEndpointResponses",
    {
        "201": IssuedWebhookEndpointResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse | SecretNotReplayableResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
CreateWebhookEndpointSuccessResponses = TypedDict(
    "CreateWebhookEndpointSuccessResponses", {"201": IssuedWebhookEndpointResponse}
)
CreateWebhookEndpointErrorResponses = TypedDict(
    "CreateWebhookEndpointErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse | SecretNotReplayableResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class CreateWebhookEndpointOperation(TypedDict):
    request: CreateWebhookEndpointRequestBody
    response: CreateWebhookEndpointSuccessResponse
    responses: CreateWebhookEndpointResponses
    successes: CreateWebhookEndpointSuccessResponses
    errors: CreateWebhookEndpointErrorResponses
    parameters: CreateWebhookEndpointParameters
    headers: CreateWebhookEndpointHeaders


DeleteWebhookEndpointParameters = TypedDict(
    "DeleteWebhookEndpointParameters", {"endpoint_id": Required[str]}, total=False
)

DeleteWebhookEndpointHeaders = TypedDict("DeleteWebhookEndpointHeaders", {}, total=False)

type DeleteWebhookEndpointRequestBody = None
type DeleteWebhookEndpointSuccessResponse = None
DeleteWebhookEndpointResponses = TypedDict(
    "DeleteWebhookEndpointResponses",
    {
        "204": None,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
DeleteWebhookEndpointSuccessResponses = TypedDict(
    "DeleteWebhookEndpointSuccessResponses", {"204": None}
)
DeleteWebhookEndpointErrorResponses = TypedDict(
    "DeleteWebhookEndpointErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class DeleteWebhookEndpointOperation(TypedDict):
    request: DeleteWebhookEndpointRequestBody
    response: DeleteWebhookEndpointSuccessResponse
    responses: DeleteWebhookEndpointResponses
    successes: DeleteWebhookEndpointSuccessResponses
    errors: DeleteWebhookEndpointErrorResponses
    parameters: DeleteWebhookEndpointParameters
    headers: DeleteWebhookEndpointHeaders


GetWebhookEndpointParameters = TypedDict(
    "GetWebhookEndpointParameters", {"endpoint_id": Required[str]}, total=False
)

GetWebhookEndpointHeaders = TypedDict("GetWebhookEndpointHeaders", {}, total=False)

type GetWebhookEndpointRequestBody = None
type GetWebhookEndpointSuccessResponse = WebhookEndpointResponse
GetWebhookEndpointResponses = TypedDict(
    "GetWebhookEndpointResponses",
    {
        "200": WebhookEndpointResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
GetWebhookEndpointSuccessResponses = TypedDict(
    "GetWebhookEndpointSuccessResponses", {"200": WebhookEndpointResponse}
)
GetWebhookEndpointErrorResponses = TypedDict(
    "GetWebhookEndpointErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class GetWebhookEndpointOperation(TypedDict):
    request: GetWebhookEndpointRequestBody
    response: GetWebhookEndpointSuccessResponse
    responses: GetWebhookEndpointResponses
    successes: GetWebhookEndpointSuccessResponses
    errors: GetWebhookEndpointErrorResponses
    parameters: GetWebhookEndpointParameters
    headers: GetWebhookEndpointHeaders


UpdateWebhookEndpointParameters = TypedDict(
    "UpdateWebhookEndpointParameters", {"endpoint_id": Required[str]}, total=False
)

UpdateWebhookEndpointHeaders = TypedDict("UpdateWebhookEndpointHeaders", {}, total=False)

type UpdateWebhookEndpointRequestBody = UpdateWebhookEndpointRequest
type UpdateWebhookEndpointSuccessResponse = WebhookEndpointResponse
UpdateWebhookEndpointResponses = TypedDict(
    "UpdateWebhookEndpointResponses",
    {
        "200": WebhookEndpointResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
UpdateWebhookEndpointSuccessResponses = TypedDict(
    "UpdateWebhookEndpointSuccessResponses", {"200": WebhookEndpointResponse}
)
UpdateWebhookEndpointErrorResponses = TypedDict(
    "UpdateWebhookEndpointErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class UpdateWebhookEndpointOperation(TypedDict):
    request: UpdateWebhookEndpointRequestBody
    response: UpdateWebhookEndpointSuccessResponse
    responses: UpdateWebhookEndpointResponses
    successes: UpdateWebhookEndpointSuccessResponses
    errors: UpdateWebhookEndpointErrorResponses
    parameters: UpdateWebhookEndpointParameters
    headers: UpdateWebhookEndpointHeaders


ListWebhookDeliveriesParameters = TypedDict(
    "ListWebhookDeliveriesParameters",
    {"endpoint_id": Required[str], "limit": NotRequired[int], "cursor": NotRequired[str | None]},
    total=False,
)

ListWebhookDeliveriesHeaders = TypedDict("ListWebhookDeliveriesHeaders", {}, total=False)

type ListWebhookDeliveriesRequestBody = None
type ListWebhookDeliveriesSuccessResponse = WebhookDeliveryPageResponse
ListWebhookDeliveriesResponses = TypedDict(
    "ListWebhookDeliveriesResponses",
    {
        "200": WebhookDeliveryPageResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
ListWebhookDeliveriesSuccessResponses = TypedDict(
    "ListWebhookDeliveriesSuccessResponses", {"200": WebhookDeliveryPageResponse}
)
ListWebhookDeliveriesErrorResponses = TypedDict(
    "ListWebhookDeliveriesErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class ListWebhookDeliveriesOperation(TypedDict):
    request: ListWebhookDeliveriesRequestBody
    response: ListWebhookDeliveriesSuccessResponse
    responses: ListWebhookDeliveriesResponses
    successes: ListWebhookDeliveriesSuccessResponses
    errors: ListWebhookDeliveriesErrorResponses
    parameters: ListWebhookDeliveriesParameters
    headers: ListWebhookDeliveriesHeaders


DisableWebhookEndpointParameters = TypedDict(
    "DisableWebhookEndpointParameters", {"endpoint_id": Required[str]}, total=False
)

DisableWebhookEndpointHeaders = TypedDict("DisableWebhookEndpointHeaders", {}, total=False)

type DisableWebhookEndpointRequestBody = None
type DisableWebhookEndpointSuccessResponse = None
DisableWebhookEndpointResponses = TypedDict(
    "DisableWebhookEndpointResponses",
    {
        "204": None,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
DisableWebhookEndpointSuccessResponses = TypedDict(
    "DisableWebhookEndpointSuccessResponses", {"204": None}
)
DisableWebhookEndpointErrorResponses = TypedDict(
    "DisableWebhookEndpointErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class DisableWebhookEndpointOperation(TypedDict):
    request: DisableWebhookEndpointRequestBody
    response: DisableWebhookEndpointSuccessResponse
    responses: DisableWebhookEndpointResponses
    successes: DisableWebhookEndpointSuccessResponses
    errors: DisableWebhookEndpointErrorResponses
    parameters: DisableWebhookEndpointParameters
    headers: DisableWebhookEndpointHeaders


EnableWebhookEndpointParameters = TypedDict(
    "EnableWebhookEndpointParameters", {"endpoint_id": Required[str]}, total=False
)

EnableWebhookEndpointHeaders = TypedDict("EnableWebhookEndpointHeaders", {}, total=False)

type EnableWebhookEndpointRequestBody = None
type EnableWebhookEndpointSuccessResponse = WebhookEndpointResponse
EnableWebhookEndpointResponses = TypedDict(
    "EnableWebhookEndpointResponses",
    {
        "200": WebhookEndpointResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
EnableWebhookEndpointSuccessResponses = TypedDict(
    "EnableWebhookEndpointSuccessResponses", {"200": WebhookEndpointResponse}
)
EnableWebhookEndpointErrorResponses = TypedDict(
    "EnableWebhookEndpointErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class EnableWebhookEndpointOperation(TypedDict):
    request: EnableWebhookEndpointRequestBody
    response: EnableWebhookEndpointSuccessResponse
    responses: EnableWebhookEndpointResponses
    successes: EnableWebhookEndpointSuccessResponses
    errors: EnableWebhookEndpointErrorResponses
    parameters: EnableWebhookEndpointParameters
    headers: EnableWebhookEndpointHeaders


RotateWebhookEndpointSecretParameters = TypedDict(
    "RotateWebhookEndpointSecretParameters", {"endpoint_id": Required[str]}, total=False
)

RotateWebhookEndpointSecretHeaders = TypedDict(
    "RotateWebhookEndpointSecretHeaders", {"Idempotency-Key": Required[str]}, total=False
)

type RotateWebhookEndpointSecretRequestBody = RotateWebhookSecretRequest | None
type RotateWebhookEndpointSecretSuccessResponse = RotatedWebhookSecretResponse
RotateWebhookEndpointSecretResponses = TypedDict(
    "RotateWebhookEndpointSecretResponses",
    {
        "200": RotatedWebhookSecretResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse | SecretNotReplayableResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
RotateWebhookEndpointSecretSuccessResponses = TypedDict(
    "RotateWebhookEndpointSecretSuccessResponses", {"200": RotatedWebhookSecretResponse}
)
RotateWebhookEndpointSecretErrorResponses = TypedDict(
    "RotateWebhookEndpointSecretErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse | SecretNotReplayableResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class RotateWebhookEndpointSecretOperation(TypedDict):
    request: RotateWebhookEndpointSecretRequestBody
    response: RotateWebhookEndpointSecretSuccessResponse
    responses: RotateWebhookEndpointSecretResponses
    successes: RotateWebhookEndpointSecretSuccessResponses
    errors: RotateWebhookEndpointSecretErrorResponses
    parameters: RotateWebhookEndpointSecretParameters
    headers: RotateWebhookEndpointSecretHeaders


CompleteWebhookEndpointSecretOverlapParameters = TypedDict(
    "CompleteWebhookEndpointSecretOverlapParameters", {"endpoint_id": Required[str]}, total=False
)

CompleteWebhookEndpointSecretOverlapHeaders = TypedDict(
    "CompleteWebhookEndpointSecretOverlapHeaders", {}, total=False
)

type CompleteWebhookEndpointSecretOverlapRequestBody = None
type CompleteWebhookEndpointSecretOverlapSuccessResponse = WebhookEndpointResponse
CompleteWebhookEndpointSecretOverlapResponses = TypedDict(
    "CompleteWebhookEndpointSecretOverlapResponses",
    {
        "200": WebhookEndpointResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
CompleteWebhookEndpointSecretOverlapSuccessResponses = TypedDict(
    "CompleteWebhookEndpointSecretOverlapSuccessResponses", {"200": WebhookEndpointResponse}
)
CompleteWebhookEndpointSecretOverlapErrorResponses = TypedDict(
    "CompleteWebhookEndpointSecretOverlapErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class CompleteWebhookEndpointSecretOverlapOperation(TypedDict):
    request: CompleteWebhookEndpointSecretOverlapRequestBody
    response: CompleteWebhookEndpointSecretOverlapSuccessResponse
    responses: CompleteWebhookEndpointSecretOverlapResponses
    successes: CompleteWebhookEndpointSecretOverlapSuccessResponses
    errors: CompleteWebhookEndpointSecretOverlapErrorResponses
    parameters: CompleteWebhookEndpointSecretOverlapParameters
    headers: CompleteWebhookEndpointSecretOverlapHeaders


SendWebhookTestEventParameters = TypedDict(
    "SendWebhookTestEventParameters", {"endpoint_id": Required[str]}, total=False
)

SendWebhookTestEventHeaders = TypedDict("SendWebhookTestEventHeaders", {}, total=False)

type SendWebhookTestEventRequestBody = None
type SendWebhookTestEventSuccessResponse = WebhookTestEventResponse
SendWebhookTestEventResponses = TypedDict(
    "SendWebhookTestEventResponses",
    {
        "202": WebhookTestEventResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
SendWebhookTestEventSuccessResponses = TypedDict(
    "SendWebhookTestEventSuccessResponses", {"202": WebhookTestEventResponse}
)
SendWebhookTestEventErrorResponses = TypedDict(
    "SendWebhookTestEventErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class SendWebhookTestEventOperation(TypedDict):
    request: SendWebhookTestEventRequestBody
    response: SendWebhookTestEventSuccessResponse
    responses: SendWebhookTestEventResponses
    successes: SendWebhookTestEventSuccessResponses
    errors: SendWebhookTestEventErrorResponses
    parameters: SendWebhookTestEventParameters
    headers: SendWebhookTestEventHeaders


GetWebhookDeliveryParameters = TypedDict(
    "GetWebhookDeliveryParameters", {"delivery_id": Required[str]}, total=False
)

GetWebhookDeliveryHeaders = TypedDict("GetWebhookDeliveryHeaders", {}, total=False)

type GetWebhookDeliveryRequestBody = None
type GetWebhookDeliverySuccessResponse = WebhookDeliveryResponse
GetWebhookDeliveryResponses = TypedDict(
    "GetWebhookDeliveryResponses",
    {
        "200": WebhookDeliveryResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
GetWebhookDeliverySuccessResponses = TypedDict(
    "GetWebhookDeliverySuccessResponses", {"200": WebhookDeliveryResponse}
)
GetWebhookDeliveryErrorResponses = TypedDict(
    "GetWebhookDeliveryErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class GetWebhookDeliveryOperation(TypedDict):
    request: GetWebhookDeliveryRequestBody
    response: GetWebhookDeliverySuccessResponse
    responses: GetWebhookDeliveryResponses
    successes: GetWebhookDeliverySuccessResponses
    errors: GetWebhookDeliveryErrorResponses
    parameters: GetWebhookDeliveryParameters
    headers: GetWebhookDeliveryHeaders


ListWebhookDeliveryAttemptsParameters = TypedDict(
    "ListWebhookDeliveryAttemptsParameters",
    {"delivery_id": Required[str], "limit": NotRequired[int], "cursor": NotRequired[str | None]},
    total=False,
)

ListWebhookDeliveryAttemptsHeaders = TypedDict(
    "ListWebhookDeliveryAttemptsHeaders", {}, total=False
)

type ListWebhookDeliveryAttemptsRequestBody = None
type ListWebhookDeliveryAttemptsSuccessResponse = WebhookAttemptPageResponse
ListWebhookDeliveryAttemptsResponses = TypedDict(
    "ListWebhookDeliveryAttemptsResponses",
    {
        "200": WebhookAttemptPageResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
ListWebhookDeliveryAttemptsSuccessResponses = TypedDict(
    "ListWebhookDeliveryAttemptsSuccessResponses", {"200": WebhookAttemptPageResponse}
)
ListWebhookDeliveryAttemptsErrorResponses = TypedDict(
    "ListWebhookDeliveryAttemptsErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class ListWebhookDeliveryAttemptsOperation(TypedDict):
    request: ListWebhookDeliveryAttemptsRequestBody
    response: ListWebhookDeliveryAttemptsSuccessResponse
    responses: ListWebhookDeliveryAttemptsResponses
    successes: ListWebhookDeliveryAttemptsSuccessResponses
    errors: ListWebhookDeliveryAttemptsErrorResponses
    parameters: ListWebhookDeliveryAttemptsParameters
    headers: ListWebhookDeliveryAttemptsHeaders


ReplayWebhookDeliveryParameters = TypedDict(
    "ReplayWebhookDeliveryParameters", {"delivery_id": Required[str]}, total=False
)

ReplayWebhookDeliveryHeaders = TypedDict(
    "ReplayWebhookDeliveryHeaders", {"Idempotency-Key": Required[str]}, total=False
)

type ReplayWebhookDeliveryRequestBody = None
type ReplayWebhookDeliverySuccessResponse = ReplayWebhookDeliveryResponse
ReplayWebhookDeliveryResponses = TypedDict(
    "ReplayWebhookDeliveryResponses",
    {
        "200": ReplayWebhookDeliveryResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
ReplayWebhookDeliverySuccessResponses = TypedDict(
    "ReplayWebhookDeliverySuccessResponses", {"200": ReplayWebhookDeliveryResponse}
)
ReplayWebhookDeliveryErrorResponses = TypedDict(
    "ReplayWebhookDeliveryErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": HttpErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class ReplayWebhookDeliveryOperation(TypedDict):
    request: ReplayWebhookDeliveryRequestBody
    response: ReplayWebhookDeliverySuccessResponse
    responses: ReplayWebhookDeliveryResponses
    successes: ReplayWebhookDeliverySuccessResponses
    errors: ReplayWebhookDeliveryErrorResponses
    parameters: ReplayWebhookDeliveryParameters
    headers: ReplayWebhookDeliveryHeaders


GetWebhookEventCatalogParameters = TypedDict("GetWebhookEventCatalogParameters", {}, total=False)

GetWebhookEventCatalogHeaders = TypedDict("GetWebhookEventCatalogHeaders", {}, total=False)

type GetWebhookEventCatalogRequestBody = None
type GetWebhookEventCatalogSuccessResponse = CustomerEventCatalogResponse
GetWebhookEventCatalogResponses = TypedDict(
    "GetWebhookEventCatalogResponses",
    {
        "200": CustomerEventCatalogResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)
GetWebhookEventCatalogSuccessResponses = TypedDict(
    "GetWebhookEventCatalogSuccessResponses", {"200": CustomerEventCatalogResponse}
)
GetWebhookEventCatalogErrorResponses = TypedDict(
    "GetWebhookEventCatalogErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse,
    },
)


class GetWebhookEventCatalogOperation(TypedDict):
    request: GetWebhookEventCatalogRequestBody
    response: GetWebhookEventCatalogSuccessResponse
    responses: GetWebhookEventCatalogResponses
    successes: GetWebhookEventCatalogSuccessResponses
    errors: GetWebhookEventCatalogErrorResponses
    parameters: GetWebhookEventCatalogParameters
    headers: GetWebhookEventCatalogHeaders


ReplayWebhookEventParameters = TypedDict(
    "ReplayWebhookEventParameters", {"event_id": Required[str]}, total=False
)

ReplayWebhookEventHeaders = TypedDict(
    "ReplayWebhookEventHeaders", {"Idempotency-Key": Required[str]}, total=False
)

type ReplayWebhookEventRequestBody = None
type ReplayWebhookEventSuccessResponse = WebhookReplayResponse
ReplayWebhookEventResponses = TypedDict(
    "ReplayWebhookEventResponses",
    {
        "200": WebhookReplayResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
ReplayWebhookEventSuccessResponses = TypedDict(
    "ReplayWebhookEventSuccessResponses", {"200": WebhookReplayResponse}
)
ReplayWebhookEventErrorResponses = TypedDict(
    "ReplayWebhookEventErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class ReplayWebhookEventOperation(TypedDict):
    request: ReplayWebhookEventRequestBody
    response: ReplayWebhookEventSuccessResponse
    responses: ReplayWebhookEventResponses
    successes: ReplayWebhookEventSuccessResponses
    errors: ReplayWebhookEventErrorResponses
    parameters: ReplayWebhookEventParameters
    headers: ReplayWebhookEventHeaders


ListWorkflowTemplatesParameters = TypedDict("ListWorkflowTemplatesParameters", {}, total=False)

ListWorkflowTemplatesHeaders = TypedDict("ListWorkflowTemplatesHeaders", {}, total=False)

type ListWorkflowTemplatesRequestBody = None
type ListWorkflowTemplatesSuccessResponse = WorkflowTemplateListResponse
ListWorkflowTemplatesResponses = TypedDict(
    "ListWorkflowTemplatesResponses",
    {
        "200": WorkflowTemplateListResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
ListWorkflowTemplatesSuccessResponses = TypedDict(
    "ListWorkflowTemplatesSuccessResponses", {"200": WorkflowTemplateListResponse}
)
ListWorkflowTemplatesErrorResponses = TypedDict(
    "ListWorkflowTemplatesErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "409": HttpErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class ListWorkflowTemplatesOperation(TypedDict):
    request: ListWorkflowTemplatesRequestBody
    response: ListWorkflowTemplatesSuccessResponse
    responses: ListWorkflowTemplatesResponses
    successes: ListWorkflowTemplatesSuccessResponses
    errors: ListWorkflowTemplatesErrorResponses
    parameters: ListWorkflowTemplatesParameters
    headers: ListWorkflowTemplatesHeaders


CreateWorkflowTemplateParameters = TypedDict("CreateWorkflowTemplateParameters", {}, total=False)

CreateWorkflowTemplateHeaders = TypedDict(
    "CreateWorkflowTemplateHeaders", {"Idempotency-Key": Required[str]}, total=False
)

type CreateWorkflowTemplateRequestBody = WorkflowTemplateRequest
type CreateWorkflowTemplateSuccessResponse = WorkflowTemplateResponse
CreateWorkflowTemplateResponses = TypedDict(
    "CreateWorkflowTemplateResponses",
    {
        "201": WorkflowTemplateResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
CreateWorkflowTemplateSuccessResponses = TypedDict(
    "CreateWorkflowTemplateSuccessResponses", {"201": WorkflowTemplateResponse}
)
CreateWorkflowTemplateErrorResponses = TypedDict(
    "CreateWorkflowTemplateErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class CreateWorkflowTemplateOperation(TypedDict):
    request: CreateWorkflowTemplateRequestBody
    response: CreateWorkflowTemplateSuccessResponse
    responses: CreateWorkflowTemplateResponses
    successes: CreateWorkflowTemplateSuccessResponses
    errors: CreateWorkflowTemplateErrorResponses
    parameters: CreateWorkflowTemplateParameters
    headers: CreateWorkflowTemplateHeaders


DeleteWorkflowTemplateParameters = TypedDict(
    "DeleteWorkflowTemplateParameters", {"template_id": Required[str]}, total=False
)

DeleteWorkflowTemplateHeaders = TypedDict("DeleteWorkflowTemplateHeaders", {}, total=False)

type DeleteWorkflowTemplateRequestBody = None
type DeleteWorkflowTemplateSuccessResponse = None
DeleteWorkflowTemplateResponses = TypedDict(
    "DeleteWorkflowTemplateResponses",
    {
        "204": None,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
DeleteWorkflowTemplateSuccessResponses = TypedDict(
    "DeleteWorkflowTemplateSuccessResponses", {"204": None}
)
DeleteWorkflowTemplateErrorResponses = TypedDict(
    "DeleteWorkflowTemplateErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class DeleteWorkflowTemplateOperation(TypedDict):
    request: DeleteWorkflowTemplateRequestBody
    response: DeleteWorkflowTemplateSuccessResponse
    responses: DeleteWorkflowTemplateResponses
    successes: DeleteWorkflowTemplateSuccessResponses
    errors: DeleteWorkflowTemplateErrorResponses
    parameters: DeleteWorkflowTemplateParameters
    headers: DeleteWorkflowTemplateHeaders


GetWorkflowTemplateParameters = TypedDict(
    "GetWorkflowTemplateParameters", {"template_id": Required[str]}, total=False
)

GetWorkflowTemplateHeaders = TypedDict("GetWorkflowTemplateHeaders", {}, total=False)

type GetWorkflowTemplateRequestBody = None
type GetWorkflowTemplateSuccessResponse = WorkflowTemplateResponse
GetWorkflowTemplateResponses = TypedDict(
    "GetWorkflowTemplateResponses",
    {
        "200": WorkflowTemplateResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
GetWorkflowTemplateSuccessResponses = TypedDict(
    "GetWorkflowTemplateSuccessResponses", {"200": WorkflowTemplateResponse}
)
GetWorkflowTemplateErrorResponses = TypedDict(
    "GetWorkflowTemplateErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class GetWorkflowTemplateOperation(TypedDict):
    request: GetWorkflowTemplateRequestBody
    response: GetWorkflowTemplateSuccessResponse
    responses: GetWorkflowTemplateResponses
    successes: GetWorkflowTemplateSuccessResponses
    errors: GetWorkflowTemplateErrorResponses
    parameters: GetWorkflowTemplateParameters
    headers: GetWorkflowTemplateHeaders


ReplaceWorkflowTemplateParameters = TypedDict(
    "ReplaceWorkflowTemplateParameters", {"template_id": Required[str]}, total=False
)

ReplaceWorkflowTemplateHeaders = TypedDict("ReplaceWorkflowTemplateHeaders", {}, total=False)

type ReplaceWorkflowTemplateRequestBody = WorkflowTemplateReplaceRequest
type ReplaceWorkflowTemplateSuccessResponse = WorkflowTemplateResponse
ReplaceWorkflowTemplateResponses = TypedDict(
    "ReplaceWorkflowTemplateResponses",
    {
        "200": WorkflowTemplateResponse,
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)
ReplaceWorkflowTemplateSuccessResponses = TypedDict(
    "ReplaceWorkflowTemplateSuccessResponses", {"200": WorkflowTemplateResponse}
)
ReplaceWorkflowTemplateErrorResponses = TypedDict(
    "ReplaceWorkflowTemplateErrorResponses",
    {
        "401": HttpErrorResponse,
        "403": HttpErrorResponse | ErrorResponse,
        "404": ErrorResponse,
        "409": HttpErrorResponse | ErrorResponse,
        "422": HttpErrorResponse | ErrorResponse,
        "429": ErrorResponse,
        "503": HttpErrorResponse | ErrorResponse,
    },
)


class ReplaceWorkflowTemplateOperation(TypedDict):
    request: ReplaceWorkflowTemplateRequestBody
    response: ReplaceWorkflowTemplateSuccessResponse
    responses: ReplaceWorkflowTemplateResponses
    successes: ReplaceWorkflowTemplateSuccessResponses
    errors: ReplaceWorkflowTemplateErrorResponses
    parameters: ReplaceWorkflowTemplateParameters
    headers: ReplaceWorkflowTemplateHeaders


ReceiveClerkWebhookParameters = TypedDict("ReceiveClerkWebhookParameters", {}, total=False)

ReceiveClerkWebhookHeaders = TypedDict(
    "ReceiveClerkWebhookHeaders",
    {"svix-id": Required[str], "svix-timestamp": Required[str]},
    total=False,
)

type ReceiveClerkWebhookRequestBody = dict[str, Any]
type ReceiveClerkWebhookSuccessResponse = WebhookAck
ReceiveClerkWebhookResponses = TypedDict(
    "ReceiveClerkWebhookResponses",
    {
        "200": WebhookAck,
        "400": HttpErrorResponse,
        "409": HttpErrorResponse,
        "413": HttpErrorResponse,
        "422": HTTPValidationError,
        "503": HttpErrorResponse,
    },
)
ReceiveClerkWebhookSuccessResponses = TypedDict(
    "ReceiveClerkWebhookSuccessResponses", {"200": WebhookAck}
)
ReceiveClerkWebhookErrorResponses = TypedDict(
    "ReceiveClerkWebhookErrorResponses",
    {
        "400": HttpErrorResponse,
        "409": HttpErrorResponse,
        "413": HttpErrorResponse,
        "422": HTTPValidationError,
        "503": HttpErrorResponse,
    },
)


class ReceiveClerkWebhookOperation(TypedDict):
    request: ReceiveClerkWebhookRequestBody
    response: ReceiveClerkWebhookSuccessResponse
    responses: ReceiveClerkWebhookResponses
    successes: ReceiveClerkWebhookSuccessResponses
    errors: ReceiveClerkWebhookErrorResponses
    parameters: ReceiveClerkWebhookParameters
    headers: ReceiveClerkWebhookHeaders


ReceiveStripeWebhookParameters = TypedDict("ReceiveStripeWebhookParameters", {}, total=False)

ReceiveStripeWebhookHeaders = TypedDict("ReceiveStripeWebhookHeaders", {}, total=False)

type ReceiveStripeWebhookRequestBody = dict[str, Any]
type ReceiveStripeWebhookSuccessResponse = StripeInboxResponse
ReceiveStripeWebhookResponses = TypedDict(
    "ReceiveStripeWebhookResponses",
    {
        "202": StripeInboxResponse,
        "400": HttpErrorResponse,
        "409": HttpErrorResponse,
        "413": HttpErrorResponse,
        "503": HttpErrorResponse,
    },
)
ReceiveStripeWebhookSuccessResponses = TypedDict(
    "ReceiveStripeWebhookSuccessResponses", {"202": StripeInboxResponse}
)
ReceiveStripeWebhookErrorResponses = TypedDict(
    "ReceiveStripeWebhookErrorResponses",
    {
        "400": HttpErrorResponse,
        "409": HttpErrorResponse,
        "413": HttpErrorResponse,
        "503": HttpErrorResponse,
    },
)


class ReceiveStripeWebhookOperation(TypedDict):
    request: ReceiveStripeWebhookRequestBody
    response: ReceiveStripeWebhookSuccessResponse
    responses: ReceiveStripeWebhookResponses
    successes: ReceiveStripeWebhookSuccessResponses
    errors: ReceiveStripeWebhookErrorResponses
    parameters: ReceiveStripeWebhookParameters
    headers: ReceiveStripeWebhookHeaders


type PublicApiOperationModels = (
    GetHealthzOperation
    | GetDatabaseHealthOperation
    | GetReadyzOperation
    | GetGovernanceReadyzOperation
    | ListApiKeysOperation
    | CreateApiKeyOperation
    | RevokeApiKeyOperation
    | GetApiKeyOperation
    | GetApiKeyRestrictionsOperation
    | SetApiKeyRestrictionsOperation
    | GetApiKeyRetentionOperation
    | SetApiKeyRetentionOperation
    | RotateApiKeyOperation
    | CancelApiKeyRotationOperation
    | CompleteApiKeyRotationOperation
    | GetApiKeySigningProfileOperation
    | SetApiKeySigningProfileOperation
    | ListApiKeyScopesOperation
    | ListApiRequestLogsOperation
    | SummarizeApiRequestLogsOperation
    | ListAssetsOperation
    | GetAssetOperation
    | GetAssetDetailOperation
    | CreateAssetDownloadOperation
    | CreateAssetPreviewOperation
    | RedeemAssetPreviewOperation
    | GetBillingAccountOperation
    | ListBillingChargesOperation
    | CreateBillingCheckoutIntentOperation
    | ListBillingInvoicesOperation
    | GetBillingPlansOperation
    | CreateBillingPortalIntentOperation
    | GetBillingPricingOperation
    | CreateBillingQuoteOperation
    | GetBillingWalletOperation
    | SetBillingWalletSettingsOperation
    | GetCapabilitiesOperation
    | CreateCaptureAdmissionChallengeOperation
    | ListCaptureAdmissionsOperation
    | CreateCaptureAdmissionOperation
    | GetCaptureAdmissionOperation
    | ListCaptureIdentitiesOperation
    | CreateCaptureIdentityOperation
    | GetCaptureIdentityOperation
    | RevokeCaptureIdentityOperation
    | CreateCaptureIdentityEnrollmentOperation
    | GetConnectCatalogOperation
    | GetCreatorDisclosurePolicyOperation
    | UpdateCreatorDisclosurePolicyOperation
    | ListCreatorIdentitiesOperation
    | CreateCreatorIdentityOperation
    | GetCreatorIdentityOperation
    | DiscloseCreatorIdentityOperation
    | WithdrawCreatorIdentityOperation
    | GetDeveloperOnboardingOperation
    | ListDisclosureEventsOperation
    | CreateDisclosureEventOperation
    | GetDisclosurePoliciesOperation
    | SubmitFeedbackOperation
    | QueryGovernanceAuditOperation
    | ListGovernanceDeletionsOperation
    | CreateGovernanceDeletionOperation
    | GetGovernanceDeletionOperation
    | ListGovernanceExportsOperation
    | CreateGovernanceExportOperation
    | GetGovernanceExportOperation
    | ListGovernanceLegalHoldsOperation
    | ReleaseHistorySnapshotOperation
    | ListIdentityCredentialsOperation
    | ListImageProfilesOperation
    | ListJobsOperation
    | GetJobOperation
    | CancelJobOperation
    | CreateMarkingCheckOperation
    | GetMarkingCheckOperation
    | GetCurrentUserOperation
    | GetOverviewOperation
    | GetPublicVerifyPageOperation
    | CreatePublicCheckOperation
    | GetPublicCheckOperation
    | GetPublicVerifyPageLogoOperation
    | ListReceiptsOperation
    | GetSigningReceiptOperation
    | ListRecipesOperation
    | GetRecipeOperation
    | GetSharedVerificationOperation
    | AcceptSigningJobOperation
    | AcceptSigningJobBatchOperation
    | CreateUploadOperation
    | AbortUploadOperation
    | CompleteUploadOperation
    | GetUsageOperation
    | GetVerificationEvidenceOperation
    | CreateVerificationReportOperation
    | ListVerificationSharesOperation
    | CreateVerificationShareOperation
    | GetVerificationHistoryOperation
    | GetVerificationReportOperation
    | CloseVerificationShareOperation
    | ListVerificationsOperation
    | CreateVerificationOperation
    | GetVerificationOperation
    | CreateVerificationBatchOperation
    | GetVerifyPageOperation
    | PutVerifyPageOperation
    | ListWebhookEndpointsOperation
    | CreateWebhookEndpointOperation
    | DeleteWebhookEndpointOperation
    | GetWebhookEndpointOperation
    | UpdateWebhookEndpointOperation
    | ListWebhookDeliveriesOperation
    | DisableWebhookEndpointOperation
    | EnableWebhookEndpointOperation
    | RotateWebhookEndpointSecretOperation
    | CompleteWebhookEndpointSecretOverlapOperation
    | SendWebhookTestEventOperation
    | GetWebhookDeliveryOperation
    | ListWebhookDeliveryAttemptsOperation
    | ReplayWebhookDeliveryOperation
    | GetWebhookEventCatalogOperation
    | ReplayWebhookEventOperation
    | ListWorkflowTemplatesOperation
    | CreateWorkflowTemplateOperation
    | DeleteWorkflowTemplateOperation
    | GetWorkflowTemplateOperation
    | ReplaceWorkflowTemplateOperation
    | ReceiveClerkWebhookOperation
    | ReceiveStripeWebhookOperation
)


class GeneratedClientMixin:
    _request_operation: Any

    def get_healthz(
        self,
        *,
        parameters: GetHealthzParameters | None = None,
        headers: GetHealthzHeaders | None = None,
    ) -> GetHealthzSuccessResponse:
        return cast(
            GetHealthzSuccessResponse,
            self._request_operation(
                "getHealthz",
                parameters=parameters,
                headers=headers,
            ),
        )

    def get_database_health(
        self,
        *,
        parameters: GetDatabaseHealthParameters | None = None,
        headers: GetDatabaseHealthHeaders | None = None,
    ) -> GetDatabaseHealthSuccessResponse:
        return cast(
            GetDatabaseHealthSuccessResponse,
            self._request_operation(
                "getDatabaseHealth",
                parameters=parameters,
                headers=headers,
            ),
        )

    def get_readyz(
        self,
        *,
        parameters: GetReadyzParameters | None = None,
        headers: GetReadyzHeaders | None = None,
    ) -> GetReadyzSuccessResponse:
        return cast(
            GetReadyzSuccessResponse,
            self._request_operation(
                "getReadyz",
                parameters=parameters,
                headers=headers,
            ),
        )

    def get_governance_readyz(
        self,
        *,
        parameters: GetGovernanceReadyzParameters | None = None,
        headers: GetGovernanceReadyzHeaders | None = None,
    ) -> GetGovernanceReadyzSuccessResponse:
        return cast(
            GetGovernanceReadyzSuccessResponse,
            self._request_operation(
                "getGovernanceReadyz",
                parameters=parameters,
                headers=headers,
            ),
        )

    def list_api_keys(
        self,
        *,
        parameters: ListApiKeysParameters | None = None,
        headers: ListApiKeysHeaders | None = None,
    ) -> ListApiKeysSuccessResponse:
        return cast(
            ListApiKeysSuccessResponse,
            self._request_operation(
                "listApiKeys",
                parameters=parameters,
                headers=headers,
            ),
        )

    def create_api_key(
        self,
        *,
        body: CreateApiKeyRequestBody,
        parameters: CreateApiKeyParameters | None = None,
        headers: CreateApiKeyHeaders | None = None,
    ) -> CreateApiKeySuccessResponse:
        return cast(
            CreateApiKeySuccessResponse,
            self._request_operation(
                "createApiKey", parameters=parameters, headers=headers, body=body
            ),
        )

    def revoke_api_key(
        self,
        *,
        parameters: RevokeApiKeyParameters | None = None,
        headers: RevokeApiKeyHeaders | None = None,
    ) -> RevokeApiKeySuccessResponse:
        return cast(
            RevokeApiKeySuccessResponse,
            self._request_operation(
                "revokeApiKey",
                parameters=parameters,
                headers=headers,
            ),
        )

    def get_api_key(
        self,
        *,
        parameters: GetApiKeyParameters | None = None,
        headers: GetApiKeyHeaders | None = None,
    ) -> GetApiKeySuccessResponse:
        return cast(
            GetApiKeySuccessResponse,
            self._request_operation(
                "getApiKey",
                parameters=parameters,
                headers=headers,
            ),
        )

    def get_api_key_restrictions(
        self,
        *,
        parameters: GetApiKeyRestrictionsParameters | None = None,
        headers: GetApiKeyRestrictionsHeaders | None = None,
    ) -> GetApiKeyRestrictionsSuccessResponse:
        return cast(
            GetApiKeyRestrictionsSuccessResponse,
            self._request_operation(
                "getApiKeyRestrictions",
                parameters=parameters,
                headers=headers,
            ),
        )

    def set_api_key_restrictions(
        self,
        *,
        body: SetApiKeyRestrictionsRequestBody,
        parameters: SetApiKeyRestrictionsParameters | None = None,
        headers: SetApiKeyRestrictionsHeaders | None = None,
    ) -> SetApiKeyRestrictionsSuccessResponse:
        return cast(
            SetApiKeyRestrictionsSuccessResponse,
            self._request_operation(
                "setApiKeyRestrictions", parameters=parameters, headers=headers, body=body
            ),
        )

    def get_api_key_retention(
        self,
        *,
        parameters: GetApiKeyRetentionParameters | None = None,
        headers: GetApiKeyRetentionHeaders | None = None,
    ) -> GetApiKeyRetentionSuccessResponse:
        return cast(
            GetApiKeyRetentionSuccessResponse,
            self._request_operation(
                "getApiKeyRetention",
                parameters=parameters,
                headers=headers,
            ),
        )

    def set_api_key_retention(
        self,
        *,
        body: SetApiKeyRetentionRequestBody,
        parameters: SetApiKeyRetentionParameters | None = None,
        headers: SetApiKeyRetentionHeaders | None = None,
    ) -> SetApiKeyRetentionSuccessResponse:
        return cast(
            SetApiKeyRetentionSuccessResponse,
            self._request_operation(
                "setApiKeyRetention", parameters=parameters, headers=headers, body=body
            ),
        )

    def rotate_api_key(
        self,
        *,
        body: RotateApiKeyRequestBody,
        parameters: RotateApiKeyParameters | None = None,
        headers: RotateApiKeyHeaders | None = None,
    ) -> RotateApiKeySuccessResponse:
        return cast(
            RotateApiKeySuccessResponse,
            self._request_operation(
                "rotateApiKey", parameters=parameters, headers=headers, body=body
            ),
        )

    def cancel_api_key_rotation(
        self,
        *,
        parameters: CancelApiKeyRotationParameters | None = None,
        headers: CancelApiKeyRotationHeaders | None = None,
    ) -> CancelApiKeyRotationSuccessResponse:
        return cast(
            CancelApiKeyRotationSuccessResponse,
            self._request_operation(
                "cancelApiKeyRotation",
                parameters=parameters,
                headers=headers,
            ),
        )

    def complete_api_key_rotation(
        self,
        *,
        parameters: CompleteApiKeyRotationParameters | None = None,
        headers: CompleteApiKeyRotationHeaders | None = None,
    ) -> CompleteApiKeyRotationSuccessResponse:
        return cast(
            CompleteApiKeyRotationSuccessResponse,
            self._request_operation(
                "completeApiKeyRotation",
                parameters=parameters,
                headers=headers,
            ),
        )

    def get_api_key_signing_profile(
        self,
        *,
        parameters: GetApiKeySigningProfileParameters | None = None,
        headers: GetApiKeySigningProfileHeaders | None = None,
    ) -> GetApiKeySigningProfileSuccessResponse:
        return cast(
            GetApiKeySigningProfileSuccessResponse,
            self._request_operation(
                "getApiKeySigningProfile",
                parameters=parameters,
                headers=headers,
            ),
        )

    def set_api_key_signing_profile(
        self,
        *,
        body: SetApiKeySigningProfileRequestBody,
        parameters: SetApiKeySigningProfileParameters | None = None,
        headers: SetApiKeySigningProfileHeaders | None = None,
    ) -> SetApiKeySigningProfileSuccessResponse:
        return cast(
            SetApiKeySigningProfileSuccessResponse,
            self._request_operation(
                "setApiKeySigningProfile", parameters=parameters, headers=headers, body=body
            ),
        )

    def list_api_key_scopes(
        self,
        *,
        parameters: ListApiKeyScopesParameters | None = None,
        headers: ListApiKeyScopesHeaders | None = None,
    ) -> ListApiKeyScopesSuccessResponse:
        return cast(
            ListApiKeyScopesSuccessResponse,
            self._request_operation(
                "listApiKeyScopes",
                parameters=parameters,
                headers=headers,
            ),
        )

    def list_api_request_logs(
        self,
        *,
        parameters: ListApiRequestLogsParameters | None = None,
        headers: ListApiRequestLogsHeaders | None = None,
    ) -> ListApiRequestLogsSuccessResponse:
        return cast(
            ListApiRequestLogsSuccessResponse,
            self._request_operation(
                "listApiRequestLogs",
                parameters=parameters,
                headers=headers,
            ),
        )

    def summarize_api_request_logs(
        self,
        *,
        parameters: SummarizeApiRequestLogsParameters | None = None,
        headers: SummarizeApiRequestLogsHeaders | None = None,
    ) -> SummarizeApiRequestLogsSuccessResponse:
        return cast(
            SummarizeApiRequestLogsSuccessResponse,
            self._request_operation(
                "summarizeApiRequestLogs",
                parameters=parameters,
                headers=headers,
            ),
        )

    def list_assets(
        self,
        *,
        parameters: ListAssetsParameters | None = None,
        headers: ListAssetsHeaders | None = None,
    ) -> ListAssetsSuccessResponse:
        return cast(
            ListAssetsSuccessResponse,
            self._request_operation(
                "listAssets",
                parameters=parameters,
                headers=headers,
            ),
        )

    def get_asset(
        self,
        *,
        parameters: GetAssetParameters | None = None,
        headers: GetAssetHeaders | None = None,
    ) -> GetAssetSuccessResponse:
        return cast(
            GetAssetSuccessResponse,
            self._request_operation(
                "getAsset",
                parameters=parameters,
                headers=headers,
            ),
        )

    def get_asset_detail(
        self,
        *,
        parameters: GetAssetDetailParameters | None = None,
        headers: GetAssetDetailHeaders | None = None,
    ) -> GetAssetDetailSuccessResponse:
        return cast(
            GetAssetDetailSuccessResponse,
            self._request_operation(
                "getAssetDetail",
                parameters=parameters,
                headers=headers,
            ),
        )

    def create_asset_download(
        self,
        *,
        parameters: CreateAssetDownloadParameters | None = None,
        headers: CreateAssetDownloadHeaders | None = None,
    ) -> CreateAssetDownloadSuccessResponse:
        return cast(
            CreateAssetDownloadSuccessResponse,
            self._request_operation(
                "createAssetDownload",
                parameters=parameters,
                headers=headers,
            ),
        )

    def create_asset_preview(
        self,
        *,
        parameters: CreateAssetPreviewParameters | None = None,
        headers: CreateAssetPreviewHeaders | None = None,
    ) -> CreateAssetPreviewSuccessResponse:
        return cast(
            CreateAssetPreviewSuccessResponse,
            self._request_operation(
                "createAssetPreview",
                parameters=parameters,
                headers=headers,
            ),
        )

    def redeem_asset_preview(
        self,
        *,
        parameters: RedeemAssetPreviewParameters | None = None,
        headers: RedeemAssetPreviewHeaders | None = None,
    ) -> RedeemAssetPreviewSuccessResponse:
        return cast(
            RedeemAssetPreviewSuccessResponse,
            self._request_operation(
                "redeemAssetPreview",
                parameters=parameters,
                headers=headers,
            ),
        )

    def get_billing_account(
        self,
        *,
        parameters: GetBillingAccountParameters | None = None,
        headers: GetBillingAccountHeaders | None = None,
    ) -> GetBillingAccountSuccessResponse:
        return cast(
            GetBillingAccountSuccessResponse,
            self._request_operation(
                "getBillingAccount",
                parameters=parameters,
                headers=headers,
            ),
        )

    def list_billing_charges(
        self,
        *,
        parameters: ListBillingChargesParameters | None = None,
        headers: ListBillingChargesHeaders | None = None,
    ) -> ListBillingChargesSuccessResponse:
        return cast(
            ListBillingChargesSuccessResponse,
            self._request_operation(
                "listBillingCharges",
                parameters=parameters,
                headers=headers,
            ),
        )

    def create_billing_checkout_intent(
        self,
        *,
        body: CreateBillingCheckoutIntentRequestBody,
        parameters: CreateBillingCheckoutIntentParameters | None = None,
        headers: CreateBillingCheckoutIntentHeaders | None = None,
    ) -> CreateBillingCheckoutIntentSuccessResponse:
        return cast(
            CreateBillingCheckoutIntentSuccessResponse,
            self._request_operation(
                "createBillingCheckoutIntent", parameters=parameters, headers=headers, body=body
            ),
        )

    def list_billing_invoices(
        self,
        *,
        parameters: ListBillingInvoicesParameters | None = None,
        headers: ListBillingInvoicesHeaders | None = None,
    ) -> ListBillingInvoicesSuccessResponse:
        return cast(
            ListBillingInvoicesSuccessResponse,
            self._request_operation(
                "listBillingInvoices",
                parameters=parameters,
                headers=headers,
            ),
        )

    def get_billing_plans(
        self,
        *,
        parameters: GetBillingPlansParameters | None = None,
        headers: GetBillingPlansHeaders | None = None,
    ) -> GetBillingPlansSuccessResponse:
        return cast(
            GetBillingPlansSuccessResponse,
            self._request_operation(
                "getBillingPlans",
                parameters=parameters,
                headers=headers,
            ),
        )

    def create_billing_portal_intent(
        self,
        *,
        body: CreateBillingPortalIntentRequestBody,
        parameters: CreateBillingPortalIntentParameters | None = None,
        headers: CreateBillingPortalIntentHeaders | None = None,
    ) -> CreateBillingPortalIntentSuccessResponse:
        return cast(
            CreateBillingPortalIntentSuccessResponse,
            self._request_operation(
                "createBillingPortalIntent", parameters=parameters, headers=headers, body=body
            ),
        )

    def get_billing_pricing(
        self,
        *,
        parameters: GetBillingPricingParameters | None = None,
        headers: GetBillingPricingHeaders | None = None,
    ) -> GetBillingPricingSuccessResponse:
        return cast(
            GetBillingPricingSuccessResponse,
            self._request_operation(
                "getBillingPricing",
                parameters=parameters,
                headers=headers,
            ),
        )

    def create_billing_quote(
        self,
        *,
        body: CreateBillingQuoteRequestBody,
        parameters: CreateBillingQuoteParameters | None = None,
        headers: CreateBillingQuoteHeaders | None = None,
    ) -> CreateBillingQuoteSuccessResponse:
        return cast(
            CreateBillingQuoteSuccessResponse,
            self._request_operation(
                "createBillingQuote", parameters=parameters, headers=headers, body=body
            ),
        )

    def get_billing_wallet(
        self,
        *,
        parameters: GetBillingWalletParameters | None = None,
        headers: GetBillingWalletHeaders | None = None,
    ) -> GetBillingWalletSuccessResponse:
        return cast(
            GetBillingWalletSuccessResponse,
            self._request_operation(
                "getBillingWallet",
                parameters=parameters,
                headers=headers,
            ),
        )

    def set_billing_wallet_settings(
        self,
        *,
        body: SetBillingWalletSettingsRequestBody,
        parameters: SetBillingWalletSettingsParameters | None = None,
        headers: SetBillingWalletSettingsHeaders | None = None,
    ) -> SetBillingWalletSettingsSuccessResponse:
        return cast(
            SetBillingWalletSettingsSuccessResponse,
            self._request_operation(
                "setBillingWalletSettings", parameters=parameters, headers=headers, body=body
            ),
        )

    def get_capabilities(
        self,
        *,
        parameters: GetCapabilitiesParameters | None = None,
        headers: GetCapabilitiesHeaders | None = None,
    ) -> GetCapabilitiesSuccessResponse:
        return cast(
            GetCapabilitiesSuccessResponse,
            self._request_operation(
                "getCapabilities",
                parameters=parameters,
                headers=headers,
            ),
        )

    def create_capture_admission_challenge(
        self,
        *,
        body: CreateCaptureAdmissionChallengeRequestBody,
        parameters: CreateCaptureAdmissionChallengeParameters | None = None,
        headers: CreateCaptureAdmissionChallengeHeaders | None = None,
    ) -> CreateCaptureAdmissionChallengeSuccessResponse:
        return cast(
            CreateCaptureAdmissionChallengeSuccessResponse,
            self._request_operation(
                "createCaptureAdmissionChallenge", parameters=parameters, headers=headers, body=body
            ),
        )

    def list_capture_admissions(
        self,
        *,
        parameters: ListCaptureAdmissionsParameters | None = None,
        headers: ListCaptureAdmissionsHeaders | None = None,
    ) -> ListCaptureAdmissionsSuccessResponse:
        return cast(
            ListCaptureAdmissionsSuccessResponse,
            self._request_operation(
                "listCaptureAdmissions",
                parameters=parameters,
                headers=headers,
            ),
        )

    def create_capture_admission(
        self,
        *,
        body: CreateCaptureAdmissionRequestBody,
        parameters: CreateCaptureAdmissionParameters | None = None,
        headers: CreateCaptureAdmissionHeaders | None = None,
    ) -> CreateCaptureAdmissionSuccessResponse:
        return cast(
            CreateCaptureAdmissionSuccessResponse,
            self._request_operation(
                "createCaptureAdmission", parameters=parameters, headers=headers, body=body
            ),
        )

    def get_capture_admission(
        self,
        *,
        parameters: GetCaptureAdmissionParameters | None = None,
        headers: GetCaptureAdmissionHeaders | None = None,
    ) -> GetCaptureAdmissionSuccessResponse:
        return cast(
            GetCaptureAdmissionSuccessResponse,
            self._request_operation(
                "getCaptureAdmission",
                parameters=parameters,
                headers=headers,
            ),
        )

    def list_capture_identities(
        self,
        *,
        parameters: ListCaptureIdentitiesParameters | None = None,
        headers: ListCaptureIdentitiesHeaders | None = None,
    ) -> ListCaptureIdentitiesSuccessResponse:
        return cast(
            ListCaptureIdentitiesSuccessResponse,
            self._request_operation(
                "listCaptureIdentities",
                parameters=parameters,
                headers=headers,
            ),
        )

    def create_capture_identity(
        self,
        *,
        body: CreateCaptureIdentityRequestBody,
        parameters: CreateCaptureIdentityParameters | None = None,
        headers: CreateCaptureIdentityHeaders | None = None,
    ) -> CreateCaptureIdentitySuccessResponse:
        return cast(
            CreateCaptureIdentitySuccessResponse,
            self._request_operation(
                "createCaptureIdentity", parameters=parameters, headers=headers, body=body
            ),
        )

    def get_capture_identity(
        self,
        *,
        parameters: GetCaptureIdentityParameters | None = None,
        headers: GetCaptureIdentityHeaders | None = None,
    ) -> GetCaptureIdentitySuccessResponse:
        return cast(
            GetCaptureIdentitySuccessResponse,
            self._request_operation(
                "getCaptureIdentity",
                parameters=parameters,
                headers=headers,
            ),
        )

    def revoke_capture_identity(
        self,
        *,
        parameters: RevokeCaptureIdentityParameters | None = None,
        headers: RevokeCaptureIdentityHeaders | None = None,
    ) -> RevokeCaptureIdentitySuccessResponse:
        return cast(
            RevokeCaptureIdentitySuccessResponse,
            self._request_operation(
                "revokeCaptureIdentity",
                parameters=parameters,
                headers=headers,
            ),
        )

    def create_capture_identity_enrollment(
        self,
        *,
        body: CreateCaptureIdentityEnrollmentRequestBody,
        parameters: CreateCaptureIdentityEnrollmentParameters | None = None,
        headers: CreateCaptureIdentityEnrollmentHeaders | None = None,
    ) -> CreateCaptureIdentityEnrollmentSuccessResponse:
        return cast(
            CreateCaptureIdentityEnrollmentSuccessResponse,
            self._request_operation(
                "createCaptureIdentityEnrollment", parameters=parameters, headers=headers, body=body
            ),
        )

    def get_connect_catalog(
        self,
        *,
        parameters: GetConnectCatalogParameters | None = None,
        headers: GetConnectCatalogHeaders | None = None,
    ) -> GetConnectCatalogSuccessResponse:
        return cast(
            GetConnectCatalogSuccessResponse,
            self._request_operation(
                "getConnectCatalog",
                parameters=parameters,
                headers=headers,
            ),
        )

    def get_creator_disclosure_policy(
        self,
        *,
        parameters: GetCreatorDisclosurePolicyParameters | None = None,
        headers: GetCreatorDisclosurePolicyHeaders | None = None,
    ) -> GetCreatorDisclosurePolicySuccessResponse:
        return cast(
            GetCreatorDisclosurePolicySuccessResponse,
            self._request_operation(
                "getCreatorDisclosurePolicy",
                parameters=parameters,
                headers=headers,
            ),
        )

    def update_creator_disclosure_policy(
        self,
        *,
        body: UpdateCreatorDisclosurePolicyRequestBody,
        parameters: UpdateCreatorDisclosurePolicyParameters | None = None,
        headers: UpdateCreatorDisclosurePolicyHeaders | None = None,
    ) -> UpdateCreatorDisclosurePolicySuccessResponse:
        return cast(
            UpdateCreatorDisclosurePolicySuccessResponse,
            self._request_operation(
                "updateCreatorDisclosurePolicy", parameters=parameters, headers=headers, body=body
            ),
        )

    def list_creator_identities(
        self,
        *,
        parameters: ListCreatorIdentitiesParameters | None = None,
        headers: ListCreatorIdentitiesHeaders | None = None,
    ) -> ListCreatorIdentitiesSuccessResponse:
        return cast(
            ListCreatorIdentitiesSuccessResponse,
            self._request_operation(
                "listCreatorIdentities",
                parameters=parameters,
                headers=headers,
            ),
        )

    def create_creator_identity(
        self,
        *,
        body: CreateCreatorIdentityRequestBody,
        parameters: CreateCreatorIdentityParameters | None = None,
        headers: CreateCreatorIdentityHeaders | None = None,
    ) -> CreateCreatorIdentitySuccessResponse:
        return cast(
            CreateCreatorIdentitySuccessResponse,
            self._request_operation(
                "createCreatorIdentity", parameters=parameters, headers=headers, body=body
            ),
        )

    def get_creator_identity(
        self,
        *,
        parameters: GetCreatorIdentityParameters | None = None,
        headers: GetCreatorIdentityHeaders | None = None,
    ) -> GetCreatorIdentitySuccessResponse:
        return cast(
            GetCreatorIdentitySuccessResponse,
            self._request_operation(
                "getCreatorIdentity",
                parameters=parameters,
                headers=headers,
            ),
        )

    def disclose_creator_identity(
        self,
        *,
        parameters: DiscloseCreatorIdentityParameters | None = None,
        headers: DiscloseCreatorIdentityHeaders | None = None,
    ) -> DiscloseCreatorIdentitySuccessResponse:
        return cast(
            DiscloseCreatorIdentitySuccessResponse,
            self._request_operation(
                "discloseCreatorIdentity",
                parameters=parameters,
                headers=headers,
            ),
        )

    def withdraw_creator_identity(
        self,
        *,
        parameters: WithdrawCreatorIdentityParameters | None = None,
        headers: WithdrawCreatorIdentityHeaders | None = None,
    ) -> WithdrawCreatorIdentitySuccessResponse:
        return cast(
            WithdrawCreatorIdentitySuccessResponse,
            self._request_operation(
                "withdrawCreatorIdentity",
                parameters=parameters,
                headers=headers,
            ),
        )

    def get_developer_onboarding(
        self,
        *,
        parameters: GetDeveloperOnboardingParameters | None = None,
        headers: GetDeveloperOnboardingHeaders | None = None,
    ) -> GetDeveloperOnboardingSuccessResponse:
        return cast(
            GetDeveloperOnboardingSuccessResponse,
            self._request_operation(
                "getDeveloperOnboarding",
                parameters=parameters,
                headers=headers,
            ),
        )

    def list_disclosure_events(
        self,
        *,
        parameters: ListDisclosureEventsParameters | None = None,
        headers: ListDisclosureEventsHeaders | None = None,
    ) -> ListDisclosureEventsSuccessResponse:
        return cast(
            ListDisclosureEventsSuccessResponse,
            self._request_operation(
                "listDisclosureEvents",
                parameters=parameters,
                headers=headers,
            ),
        )

    def create_disclosure_event(
        self,
        *,
        body: CreateDisclosureEventRequestBody,
        parameters: CreateDisclosureEventParameters | None = None,
        headers: CreateDisclosureEventHeaders | None = None,
    ) -> CreateDisclosureEventSuccessResponse:
        return cast(
            CreateDisclosureEventSuccessResponse,
            self._request_operation(
                "createDisclosureEvent", parameters=parameters, headers=headers, body=body
            ),
        )

    def get_disclosure_policies(
        self,
        *,
        parameters: GetDisclosurePoliciesParameters | None = None,
        headers: GetDisclosurePoliciesHeaders | None = None,
    ) -> GetDisclosurePoliciesSuccessResponse:
        return cast(
            GetDisclosurePoliciesSuccessResponse,
            self._request_operation(
                "getDisclosurePolicies",
                parameters=parameters,
                headers=headers,
            ),
        )

    def submit_feedback(
        self,
        *,
        body: SubmitFeedbackRequestBody,
        parameters: SubmitFeedbackParameters | None = None,
        headers: SubmitFeedbackHeaders | None = None,
    ) -> SubmitFeedbackSuccessResponse:
        return cast(
            SubmitFeedbackSuccessResponse,
            self._request_operation(
                "submitFeedback", parameters=parameters, headers=headers, body=body
            ),
        )

    def query_governance_audit(
        self,
        *,
        parameters: QueryGovernanceAuditParameters | None = None,
        headers: QueryGovernanceAuditHeaders | None = None,
    ) -> QueryGovernanceAuditSuccessResponse:
        return cast(
            QueryGovernanceAuditSuccessResponse,
            self._request_operation(
                "queryGovernanceAudit",
                parameters=parameters,
                headers=headers,
            ),
        )

    def list_governance_deletions(
        self,
        *,
        parameters: ListGovernanceDeletionsParameters | None = None,
        headers: ListGovernanceDeletionsHeaders | None = None,
    ) -> ListGovernanceDeletionsSuccessResponse:
        return cast(
            ListGovernanceDeletionsSuccessResponse,
            self._request_operation(
                "listGovernanceDeletions",
                parameters=parameters,
                headers=headers,
            ),
        )

    def create_governance_deletion(
        self,
        *,
        body: CreateGovernanceDeletionRequestBody,
        parameters: CreateGovernanceDeletionParameters | None = None,
        headers: CreateGovernanceDeletionHeaders | None = None,
    ) -> CreateGovernanceDeletionSuccessResponse:
        return cast(
            CreateGovernanceDeletionSuccessResponse,
            self._request_operation(
                "createGovernanceDeletion", parameters=parameters, headers=headers, body=body
            ),
        )

    def get_governance_deletion(
        self,
        *,
        parameters: GetGovernanceDeletionParameters | None = None,
        headers: GetGovernanceDeletionHeaders | None = None,
    ) -> GetGovernanceDeletionSuccessResponse:
        return cast(
            GetGovernanceDeletionSuccessResponse,
            self._request_operation(
                "getGovernanceDeletion",
                parameters=parameters,
                headers=headers,
            ),
        )

    def list_governance_exports(
        self,
        *,
        parameters: ListGovernanceExportsParameters | None = None,
        headers: ListGovernanceExportsHeaders | None = None,
    ) -> ListGovernanceExportsSuccessResponse:
        return cast(
            ListGovernanceExportsSuccessResponse,
            self._request_operation(
                "listGovernanceExports",
                parameters=parameters,
                headers=headers,
            ),
        )

    def create_governance_export(
        self,
        *,
        parameters: CreateGovernanceExportParameters | None = None,
        headers: CreateGovernanceExportHeaders | None = None,
    ) -> CreateGovernanceExportSuccessResponse:
        return cast(
            CreateGovernanceExportSuccessResponse,
            self._request_operation(
                "createGovernanceExport",
                parameters=parameters,
                headers=headers,
            ),
        )

    def get_governance_export(
        self,
        *,
        parameters: GetGovernanceExportParameters | None = None,
        headers: GetGovernanceExportHeaders | None = None,
    ) -> GetGovernanceExportSuccessResponse:
        return cast(
            GetGovernanceExportSuccessResponse,
            self._request_operation(
                "getGovernanceExport",
                parameters=parameters,
                headers=headers,
            ),
        )

    def list_governance_legal_holds(
        self,
        *,
        parameters: ListGovernanceLegalHoldsParameters | None = None,
        headers: ListGovernanceLegalHoldsHeaders | None = None,
    ) -> ListGovernanceLegalHoldsSuccessResponse:
        return cast(
            ListGovernanceLegalHoldsSuccessResponse,
            self._request_operation(
                "listGovernanceLegalHolds",
                parameters=parameters,
                headers=headers,
            ),
        )

    def release_history_snapshot(
        self,
        *,
        parameters: ReleaseHistorySnapshotParameters | None = None,
        headers: ReleaseHistorySnapshotHeaders | None = None,
    ) -> ReleaseHistorySnapshotSuccessResponse:
        return cast(
            ReleaseHistorySnapshotSuccessResponse,
            self._request_operation(
                "releaseHistorySnapshot",
                parameters=parameters,
                headers=headers,
            ),
        )

    def list_identity_credentials(
        self,
        *,
        parameters: ListIdentityCredentialsParameters | None = None,
        headers: ListIdentityCredentialsHeaders | None = None,
    ) -> ListIdentityCredentialsSuccessResponse:
        return cast(
            ListIdentityCredentialsSuccessResponse,
            self._request_operation(
                "listIdentityCredentials",
                parameters=parameters,
                headers=headers,
            ),
        )

    def list_image_profiles(
        self,
        *,
        parameters: ListImageProfilesParameters | None = None,
        headers: ListImageProfilesHeaders | None = None,
    ) -> ListImageProfilesSuccessResponse:
        return cast(
            ListImageProfilesSuccessResponse,
            self._request_operation(
                "listImageProfiles",
                parameters=parameters,
                headers=headers,
            ),
        )

    def list_jobs(
        self,
        *,
        parameters: ListJobsParameters | None = None,
        headers: ListJobsHeaders | None = None,
    ) -> ListJobsSuccessResponse:
        return cast(
            ListJobsSuccessResponse,
            self._request_operation(
                "listJobs",
                parameters=parameters,
                headers=headers,
            ),
        )

    def get_job(
        self,
        *,
        parameters: GetJobParameters | None = None,
        headers: GetJobHeaders | None = None,
    ) -> GetJobSuccessResponse:
        return cast(
            GetJobSuccessResponse,
            self._request_operation(
                "getJob",
                parameters=parameters,
                headers=headers,
            ),
        )

    def cancel_job(
        self,
        *,
        body: CancelJobRequestBody,
        parameters: CancelJobParameters | None = None,
        headers: CancelJobHeaders | None = None,
    ) -> CancelJobSuccessResponse:
        return cast(
            CancelJobSuccessResponse,
            self._request_operation("cancelJob", parameters=parameters, headers=headers, body=body),
        )

    def create_marking_check(
        self,
        *,
        body: CreateMarkingCheckRequestBody,
        parameters: CreateMarkingCheckParameters | None = None,
        headers: CreateMarkingCheckHeaders | None = None,
    ) -> CreateMarkingCheckSuccessResponse:
        return cast(
            CreateMarkingCheckSuccessResponse,
            self._request_operation(
                "createMarkingCheck", parameters=parameters, headers=headers, body=body
            ),
        )

    def get_marking_check(
        self,
        *,
        parameters: GetMarkingCheckParameters | None = None,
        headers: GetMarkingCheckHeaders | None = None,
    ) -> GetMarkingCheckSuccessResponse:
        return cast(
            GetMarkingCheckSuccessResponse,
            self._request_operation(
                "getMarkingCheck",
                parameters=parameters,
                headers=headers,
            ),
        )

    def get_current_user(
        self,
        *,
        parameters: GetCurrentUserParameters | None = None,
        headers: GetCurrentUserHeaders | None = None,
    ) -> GetCurrentUserSuccessResponse:
        return cast(
            GetCurrentUserSuccessResponse,
            self._request_operation(
                "getCurrentUser",
                parameters=parameters,
                headers=headers,
            ),
        )

    def get_overview(
        self,
        *,
        parameters: GetOverviewParameters | None = None,
        headers: GetOverviewHeaders | None = None,
    ) -> GetOverviewSuccessResponse:
        return cast(
            GetOverviewSuccessResponse,
            self._request_operation(
                "getOverview",
                parameters=parameters,
                headers=headers,
            ),
        )

    def get_public_verify_page(
        self,
        *,
        parameters: GetPublicVerifyPageParameters | None = None,
        headers: GetPublicVerifyPageHeaders | None = None,
    ) -> GetPublicVerifyPageSuccessResponse:
        return cast(
            GetPublicVerifyPageSuccessResponse,
            self._request_operation(
                "getPublicVerifyPage",
                parameters=parameters,
                headers=headers,
            ),
        )

    def create_public_check(
        self,
        *,
        parameters: CreatePublicCheckParameters | None = None,
        headers: CreatePublicCheckHeaders | None = None,
    ) -> CreatePublicCheckSuccessResponse:
        return cast(
            CreatePublicCheckSuccessResponse,
            self._request_operation(
                "createPublicCheck",
                parameters=parameters,
                headers=headers,
            ),
        )

    def get_public_check(
        self,
        *,
        parameters: GetPublicCheckParameters | None = None,
        headers: GetPublicCheckHeaders | None = None,
    ) -> GetPublicCheckSuccessResponse:
        return cast(
            GetPublicCheckSuccessResponse,
            self._request_operation(
                "getPublicCheck",
                parameters=parameters,
                headers=headers,
            ),
        )

    def get_public_verify_page_logo(
        self,
        *,
        parameters: GetPublicVerifyPageLogoParameters | None = None,
        headers: GetPublicVerifyPageLogoHeaders | None = None,
    ) -> GetPublicVerifyPageLogoSuccessResponse:
        return cast(
            GetPublicVerifyPageLogoSuccessResponse,
            self._request_operation(
                "getPublicVerifyPageLogo",
                parameters=parameters,
                headers=headers,
            ),
        )

    def list_receipts(
        self,
        *,
        parameters: ListReceiptsParameters | None = None,
        headers: ListReceiptsHeaders | None = None,
    ) -> ListReceiptsSuccessResponse:
        return cast(
            ListReceiptsSuccessResponse,
            self._request_operation(
                "listReceipts",
                parameters=parameters,
                headers=headers,
            ),
        )

    def get_signing_receipt(
        self,
        *,
        parameters: GetSigningReceiptParameters | None = None,
        headers: GetSigningReceiptHeaders | None = None,
    ) -> GetSigningReceiptSuccessResponse:
        return cast(
            GetSigningReceiptSuccessResponse,
            self._request_operation(
                "getSigningReceipt",
                parameters=parameters,
                headers=headers,
            ),
        )

    def list_recipes(
        self,
        *,
        parameters: ListRecipesParameters | None = None,
        headers: ListRecipesHeaders | None = None,
    ) -> ListRecipesSuccessResponse:
        return cast(
            ListRecipesSuccessResponse,
            self._request_operation(
                "listRecipes",
                parameters=parameters,
                headers=headers,
            ),
        )

    def get_recipe(
        self,
        *,
        parameters: GetRecipeParameters | None = None,
        headers: GetRecipeHeaders | None = None,
    ) -> GetRecipeSuccessResponse:
        return cast(
            GetRecipeSuccessResponse,
            self._request_operation(
                "getRecipe",
                parameters=parameters,
                headers=headers,
            ),
        )

    def get_shared_verification(
        self,
        *,
        parameters: GetSharedVerificationParameters | None = None,
        headers: GetSharedVerificationHeaders | None = None,
    ) -> GetSharedVerificationSuccessResponse:
        return cast(
            GetSharedVerificationSuccessResponse,
            self._request_operation(
                "getSharedVerification",
                parameters=parameters,
                headers=headers,
            ),
        )

    def accept_signing_job(
        self,
        *,
        body: AcceptSigningJobRequestBody,
        parameters: AcceptSigningJobParameters | None = None,
        headers: AcceptSigningJobHeaders | None = None,
    ) -> AcceptSigningJobSuccessResponse:
        return cast(
            AcceptSigningJobSuccessResponse,
            self._request_operation(
                "acceptSigningJob", parameters=parameters, headers=headers, body=body
            ),
        )

    def accept_signing_job_batch(
        self,
        *,
        body: AcceptSigningJobBatchRequestBody,
        parameters: AcceptSigningJobBatchParameters | None = None,
        headers: AcceptSigningJobBatchHeaders | None = None,
    ) -> AcceptSigningJobBatchSuccessResponse:
        return cast(
            AcceptSigningJobBatchSuccessResponse,
            self._request_operation(
                "acceptSigningJobBatch", parameters=parameters, headers=headers, body=body
            ),
        )

    def create_upload(
        self,
        *,
        body: CreateUploadRequestBody,
        parameters: CreateUploadParameters | None = None,
        headers: CreateUploadHeaders | None = None,
    ) -> CreateUploadSuccessResponse:
        return cast(
            CreateUploadSuccessResponse,
            self._request_operation(
                "createUpload", parameters=parameters, headers=headers, body=body
            ),
        )

    def abort_upload(
        self,
        *,
        parameters: AbortUploadParameters | None = None,
        headers: AbortUploadHeaders | None = None,
    ) -> AbortUploadSuccessResponse:
        return cast(
            AbortUploadSuccessResponse,
            self._request_operation(
                "abortUpload",
                parameters=parameters,
                headers=headers,
            ),
        )

    def complete_upload(
        self,
        *,
        body: CompleteUploadRequestBody,
        parameters: CompleteUploadParameters | None = None,
        headers: CompleteUploadHeaders | None = None,
    ) -> CompleteUploadSuccessResponse:
        return cast(
            CompleteUploadSuccessResponse,
            self._request_operation(
                "completeUpload", parameters=parameters, headers=headers, body=body
            ),
        )

    def get_usage(
        self,
        *,
        parameters: GetUsageParameters | None = None,
        headers: GetUsageHeaders | None = None,
    ) -> GetUsageSuccessResponse:
        return cast(
            GetUsageSuccessResponse,
            self._request_operation(
                "getUsage",
                parameters=parameters,
                headers=headers,
            ),
        )

    def get_verification_evidence(
        self,
        *,
        parameters: GetVerificationEvidenceParameters | None = None,
        headers: GetVerificationEvidenceHeaders | None = None,
    ) -> GetVerificationEvidenceSuccessResponse:
        return cast(
            GetVerificationEvidenceSuccessResponse,
            self._request_operation(
                "getVerificationEvidence",
                parameters=parameters,
                headers=headers,
            ),
        )

    def create_verification_report(
        self,
        *,
        body: CreateVerificationReportRequestBody,
        parameters: CreateVerificationReportParameters | None = None,
        headers: CreateVerificationReportHeaders | None = None,
    ) -> CreateVerificationReportSuccessResponse:
        return cast(
            CreateVerificationReportSuccessResponse,
            self._request_operation(
                "createVerificationReport", parameters=parameters, headers=headers, body=body
            ),
        )

    def list_verification_shares(
        self,
        *,
        parameters: ListVerificationSharesParameters | None = None,
        headers: ListVerificationSharesHeaders | None = None,
    ) -> ListVerificationSharesSuccessResponse:
        return cast(
            ListVerificationSharesSuccessResponse,
            self._request_operation(
                "listVerificationShares",
                parameters=parameters,
                headers=headers,
            ),
        )

    def create_verification_share(
        self,
        *,
        body: CreateVerificationShareRequestBody,
        parameters: CreateVerificationShareParameters | None = None,
        headers: CreateVerificationShareHeaders | None = None,
    ) -> CreateVerificationShareSuccessResponse:
        return cast(
            CreateVerificationShareSuccessResponse,
            self._request_operation(
                "createVerificationShare", parameters=parameters, headers=headers, body=body
            ),
        )

    def get_verification_history(
        self,
        *,
        parameters: GetVerificationHistoryParameters | None = None,
        headers: GetVerificationHistoryHeaders | None = None,
    ) -> GetVerificationHistorySuccessResponse:
        return cast(
            GetVerificationHistorySuccessResponse,
            self._request_operation(
                "getVerificationHistory",
                parameters=parameters,
                headers=headers,
            ),
        )

    def get_verification_report(
        self,
        *,
        parameters: GetVerificationReportParameters | None = None,
        headers: GetVerificationReportHeaders | None = None,
    ) -> GetVerificationReportSuccessResponse:
        return cast(
            GetVerificationReportSuccessResponse,
            self._request_operation(
                "getVerificationReport",
                parameters=parameters,
                headers=headers,
            ),
        )

    def close_verification_share(
        self,
        *,
        body: CloseVerificationShareRequestBody,
        parameters: CloseVerificationShareParameters | None = None,
        headers: CloseVerificationShareHeaders | None = None,
    ) -> CloseVerificationShareSuccessResponse:
        return cast(
            CloseVerificationShareSuccessResponse,
            self._request_operation(
                "closeVerificationShare", parameters=parameters, headers=headers, body=body
            ),
        )

    def list_verifications(
        self,
        *,
        parameters: ListVerificationsParameters | None = None,
        headers: ListVerificationsHeaders | None = None,
    ) -> ListVerificationsSuccessResponse:
        return cast(
            ListVerificationsSuccessResponse,
            self._request_operation(
                "listVerifications",
                parameters=parameters,
                headers=headers,
            ),
        )

    def create_verification(
        self,
        *,
        body: CreateVerificationRequestBody,
        parameters: CreateVerificationParameters | None = None,
        headers: CreateVerificationHeaders | None = None,
    ) -> CreateVerificationSuccessResponse:
        return cast(
            CreateVerificationSuccessResponse,
            self._request_operation(
                "createVerification", parameters=parameters, headers=headers, body=body
            ),
        )

    def get_verification(
        self,
        *,
        parameters: GetVerificationParameters | None = None,
        headers: GetVerificationHeaders | None = None,
    ) -> GetVerificationSuccessResponse:
        return cast(
            GetVerificationSuccessResponse,
            self._request_operation(
                "getVerification",
                parameters=parameters,
                headers=headers,
            ),
        )

    def create_verification_batch(
        self,
        *,
        body: CreateVerificationBatchRequestBody,
        parameters: CreateVerificationBatchParameters | None = None,
        headers: CreateVerificationBatchHeaders | None = None,
    ) -> CreateVerificationBatchSuccessResponse:
        return cast(
            CreateVerificationBatchSuccessResponse,
            self._request_operation(
                "createVerificationBatch", parameters=parameters, headers=headers, body=body
            ),
        )

    def get_verify_page(
        self,
        *,
        parameters: GetVerifyPageParameters | None = None,
        headers: GetVerifyPageHeaders | None = None,
    ) -> GetVerifyPageSuccessResponse:
        return cast(
            GetVerifyPageSuccessResponse,
            self._request_operation(
                "getVerifyPage",
                parameters=parameters,
                headers=headers,
            ),
        )

    def put_verify_page(
        self,
        *,
        body: PutVerifyPageRequestBody,
        parameters: PutVerifyPageParameters | None = None,
        headers: PutVerifyPageHeaders | None = None,
    ) -> PutVerifyPageSuccessResponse:
        return cast(
            PutVerifyPageSuccessResponse,
            self._request_operation(
                "putVerifyPage", parameters=parameters, headers=headers, body=body
            ),
        )

    def list_webhook_endpoints(
        self,
        *,
        parameters: ListWebhookEndpointsParameters | None = None,
        headers: ListWebhookEndpointsHeaders | None = None,
    ) -> ListWebhookEndpointsSuccessResponse:
        return cast(
            ListWebhookEndpointsSuccessResponse,
            self._request_operation(
                "listWebhookEndpoints",
                parameters=parameters,
                headers=headers,
            ),
        )

    def create_webhook_endpoint(
        self,
        *,
        body: CreateWebhookEndpointRequestBody,
        parameters: CreateWebhookEndpointParameters | None = None,
        headers: CreateWebhookEndpointHeaders | None = None,
    ) -> CreateWebhookEndpointSuccessResponse:
        return cast(
            CreateWebhookEndpointSuccessResponse,
            self._request_operation(
                "createWebhookEndpoint", parameters=parameters, headers=headers, body=body
            ),
        )

    def delete_webhook_endpoint(
        self,
        *,
        parameters: DeleteWebhookEndpointParameters | None = None,
        headers: DeleteWebhookEndpointHeaders | None = None,
    ) -> DeleteWebhookEndpointSuccessResponse:
        return cast(
            DeleteWebhookEndpointSuccessResponse,
            self._request_operation(
                "deleteWebhookEndpoint",
                parameters=parameters,
                headers=headers,
            ),
        )

    def get_webhook_endpoint(
        self,
        *,
        parameters: GetWebhookEndpointParameters | None = None,
        headers: GetWebhookEndpointHeaders | None = None,
    ) -> GetWebhookEndpointSuccessResponse:
        return cast(
            GetWebhookEndpointSuccessResponse,
            self._request_operation(
                "getWebhookEndpoint",
                parameters=parameters,
                headers=headers,
            ),
        )

    def update_webhook_endpoint(
        self,
        *,
        body: UpdateWebhookEndpointRequestBody,
        parameters: UpdateWebhookEndpointParameters | None = None,
        headers: UpdateWebhookEndpointHeaders | None = None,
    ) -> UpdateWebhookEndpointSuccessResponse:
        return cast(
            UpdateWebhookEndpointSuccessResponse,
            self._request_operation(
                "updateWebhookEndpoint", parameters=parameters, headers=headers, body=body
            ),
        )

    def list_webhook_deliveries(
        self,
        *,
        parameters: ListWebhookDeliveriesParameters | None = None,
        headers: ListWebhookDeliveriesHeaders | None = None,
    ) -> ListWebhookDeliveriesSuccessResponse:
        return cast(
            ListWebhookDeliveriesSuccessResponse,
            self._request_operation(
                "listWebhookDeliveries",
                parameters=parameters,
                headers=headers,
            ),
        )

    def disable_webhook_endpoint(
        self,
        *,
        parameters: DisableWebhookEndpointParameters | None = None,
        headers: DisableWebhookEndpointHeaders | None = None,
    ) -> DisableWebhookEndpointSuccessResponse:
        return cast(
            DisableWebhookEndpointSuccessResponse,
            self._request_operation(
                "disableWebhookEndpoint",
                parameters=parameters,
                headers=headers,
            ),
        )

    def enable_webhook_endpoint(
        self,
        *,
        parameters: EnableWebhookEndpointParameters | None = None,
        headers: EnableWebhookEndpointHeaders | None = None,
    ) -> EnableWebhookEndpointSuccessResponse:
        return cast(
            EnableWebhookEndpointSuccessResponse,
            self._request_operation(
                "enableWebhookEndpoint",
                parameters=parameters,
                headers=headers,
            ),
        )

    def rotate_webhook_endpoint_secret(
        self,
        *,
        body: RotateWebhookEndpointSecretRequestBody | None = None,
        parameters: RotateWebhookEndpointSecretParameters | None = None,
        headers: RotateWebhookEndpointSecretHeaders | None = None,
    ) -> RotateWebhookEndpointSecretSuccessResponse:
        return cast(
            RotateWebhookEndpointSecretSuccessResponse,
            self._request_operation(
                "rotateWebhookEndpointSecret", parameters=parameters, headers=headers, body=body
            ),
        )

    def complete_webhook_endpoint_secret_overlap(
        self,
        *,
        parameters: CompleteWebhookEndpointSecretOverlapParameters | None = None,
        headers: CompleteWebhookEndpointSecretOverlapHeaders | None = None,
    ) -> CompleteWebhookEndpointSecretOverlapSuccessResponse:
        return cast(
            CompleteWebhookEndpointSecretOverlapSuccessResponse,
            self._request_operation(
                "completeWebhookEndpointSecretOverlap",
                parameters=parameters,
                headers=headers,
            ),
        )

    def send_webhook_test_event(
        self,
        *,
        parameters: SendWebhookTestEventParameters | None = None,
        headers: SendWebhookTestEventHeaders | None = None,
    ) -> SendWebhookTestEventSuccessResponse:
        return cast(
            SendWebhookTestEventSuccessResponse,
            self._request_operation(
                "sendWebhookTestEvent",
                parameters=parameters,
                headers=headers,
            ),
        )

    def get_webhook_delivery(
        self,
        *,
        parameters: GetWebhookDeliveryParameters | None = None,
        headers: GetWebhookDeliveryHeaders | None = None,
    ) -> GetWebhookDeliverySuccessResponse:
        return cast(
            GetWebhookDeliverySuccessResponse,
            self._request_operation(
                "getWebhookDelivery",
                parameters=parameters,
                headers=headers,
            ),
        )

    def list_webhook_delivery_attempts(
        self,
        *,
        parameters: ListWebhookDeliveryAttemptsParameters | None = None,
        headers: ListWebhookDeliveryAttemptsHeaders | None = None,
    ) -> ListWebhookDeliveryAttemptsSuccessResponse:
        return cast(
            ListWebhookDeliveryAttemptsSuccessResponse,
            self._request_operation(
                "listWebhookDeliveryAttempts",
                parameters=parameters,
                headers=headers,
            ),
        )

    def replay_webhook_delivery(
        self,
        *,
        parameters: ReplayWebhookDeliveryParameters | None = None,
        headers: ReplayWebhookDeliveryHeaders | None = None,
    ) -> ReplayWebhookDeliverySuccessResponse:
        return cast(
            ReplayWebhookDeliverySuccessResponse,
            self._request_operation(
                "replayWebhookDelivery",
                parameters=parameters,
                headers=headers,
            ),
        )

    def get_webhook_event_catalog(
        self,
        *,
        parameters: GetWebhookEventCatalogParameters | None = None,
        headers: GetWebhookEventCatalogHeaders | None = None,
    ) -> GetWebhookEventCatalogSuccessResponse:
        return cast(
            GetWebhookEventCatalogSuccessResponse,
            self._request_operation(
                "getWebhookEventCatalog",
                parameters=parameters,
                headers=headers,
            ),
        )

    def replay_webhook_event(
        self,
        *,
        parameters: ReplayWebhookEventParameters | None = None,
        headers: ReplayWebhookEventHeaders | None = None,
    ) -> ReplayWebhookEventSuccessResponse:
        return cast(
            ReplayWebhookEventSuccessResponse,
            self._request_operation(
                "replayWebhookEvent",
                parameters=parameters,
                headers=headers,
            ),
        )

    def list_workflow_templates(
        self,
        *,
        parameters: ListWorkflowTemplatesParameters | None = None,
        headers: ListWorkflowTemplatesHeaders | None = None,
    ) -> ListWorkflowTemplatesSuccessResponse:
        return cast(
            ListWorkflowTemplatesSuccessResponse,
            self._request_operation(
                "listWorkflowTemplates",
                parameters=parameters,
                headers=headers,
            ),
        )

    def create_workflow_template(
        self,
        *,
        body: CreateWorkflowTemplateRequestBody,
        parameters: CreateWorkflowTemplateParameters | None = None,
        headers: CreateWorkflowTemplateHeaders | None = None,
    ) -> CreateWorkflowTemplateSuccessResponse:
        return cast(
            CreateWorkflowTemplateSuccessResponse,
            self._request_operation(
                "createWorkflowTemplate", parameters=parameters, headers=headers, body=body
            ),
        )

    def delete_workflow_template(
        self,
        *,
        parameters: DeleteWorkflowTemplateParameters | None = None,
        headers: DeleteWorkflowTemplateHeaders | None = None,
    ) -> DeleteWorkflowTemplateSuccessResponse:
        return cast(
            DeleteWorkflowTemplateSuccessResponse,
            self._request_operation(
                "deleteWorkflowTemplate",
                parameters=parameters,
                headers=headers,
            ),
        )

    def get_workflow_template(
        self,
        *,
        parameters: GetWorkflowTemplateParameters | None = None,
        headers: GetWorkflowTemplateHeaders | None = None,
    ) -> GetWorkflowTemplateSuccessResponse:
        return cast(
            GetWorkflowTemplateSuccessResponse,
            self._request_operation(
                "getWorkflowTemplate",
                parameters=parameters,
                headers=headers,
            ),
        )

    def replace_workflow_template(
        self,
        *,
        body: ReplaceWorkflowTemplateRequestBody,
        parameters: ReplaceWorkflowTemplateParameters | None = None,
        headers: ReplaceWorkflowTemplateHeaders | None = None,
    ) -> ReplaceWorkflowTemplateSuccessResponse:
        return cast(
            ReplaceWorkflowTemplateSuccessResponse,
            self._request_operation(
                "replaceWorkflowTemplate", parameters=parameters, headers=headers, body=body
            ),
        )


class GeneratedAsyncClientMixin:
    _request_operation_async: Any

    async def get_healthz(
        self,
        *,
        parameters: GetHealthzParameters | None = None,
        headers: GetHealthzHeaders | None = None,
    ) -> GetHealthzSuccessResponse:
        return cast(
            GetHealthzSuccessResponse,
            await self._request_operation_async(
                "getHealthz",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def get_database_health(
        self,
        *,
        parameters: GetDatabaseHealthParameters | None = None,
        headers: GetDatabaseHealthHeaders | None = None,
    ) -> GetDatabaseHealthSuccessResponse:
        return cast(
            GetDatabaseHealthSuccessResponse,
            await self._request_operation_async(
                "getDatabaseHealth",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def get_readyz(
        self,
        *,
        parameters: GetReadyzParameters | None = None,
        headers: GetReadyzHeaders | None = None,
    ) -> GetReadyzSuccessResponse:
        return cast(
            GetReadyzSuccessResponse,
            await self._request_operation_async(
                "getReadyz",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def get_governance_readyz(
        self,
        *,
        parameters: GetGovernanceReadyzParameters | None = None,
        headers: GetGovernanceReadyzHeaders | None = None,
    ) -> GetGovernanceReadyzSuccessResponse:
        return cast(
            GetGovernanceReadyzSuccessResponse,
            await self._request_operation_async(
                "getGovernanceReadyz",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def list_api_keys(
        self,
        *,
        parameters: ListApiKeysParameters | None = None,
        headers: ListApiKeysHeaders | None = None,
    ) -> ListApiKeysSuccessResponse:
        return cast(
            ListApiKeysSuccessResponse,
            await self._request_operation_async(
                "listApiKeys",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def create_api_key(
        self,
        *,
        body: CreateApiKeyRequestBody,
        parameters: CreateApiKeyParameters | None = None,
        headers: CreateApiKeyHeaders | None = None,
    ) -> CreateApiKeySuccessResponse:
        return cast(
            CreateApiKeySuccessResponse,
            await self._request_operation_async(
                "createApiKey", parameters=parameters, headers=headers, body=body
            ),
        )

    async def revoke_api_key(
        self,
        *,
        parameters: RevokeApiKeyParameters | None = None,
        headers: RevokeApiKeyHeaders | None = None,
    ) -> RevokeApiKeySuccessResponse:
        return cast(
            RevokeApiKeySuccessResponse,
            await self._request_operation_async(
                "revokeApiKey",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def get_api_key(
        self,
        *,
        parameters: GetApiKeyParameters | None = None,
        headers: GetApiKeyHeaders | None = None,
    ) -> GetApiKeySuccessResponse:
        return cast(
            GetApiKeySuccessResponse,
            await self._request_operation_async(
                "getApiKey",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def get_api_key_restrictions(
        self,
        *,
        parameters: GetApiKeyRestrictionsParameters | None = None,
        headers: GetApiKeyRestrictionsHeaders | None = None,
    ) -> GetApiKeyRestrictionsSuccessResponse:
        return cast(
            GetApiKeyRestrictionsSuccessResponse,
            await self._request_operation_async(
                "getApiKeyRestrictions",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def set_api_key_restrictions(
        self,
        *,
        body: SetApiKeyRestrictionsRequestBody,
        parameters: SetApiKeyRestrictionsParameters | None = None,
        headers: SetApiKeyRestrictionsHeaders | None = None,
    ) -> SetApiKeyRestrictionsSuccessResponse:
        return cast(
            SetApiKeyRestrictionsSuccessResponse,
            await self._request_operation_async(
                "setApiKeyRestrictions", parameters=parameters, headers=headers, body=body
            ),
        )

    async def get_api_key_retention(
        self,
        *,
        parameters: GetApiKeyRetentionParameters | None = None,
        headers: GetApiKeyRetentionHeaders | None = None,
    ) -> GetApiKeyRetentionSuccessResponse:
        return cast(
            GetApiKeyRetentionSuccessResponse,
            await self._request_operation_async(
                "getApiKeyRetention",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def set_api_key_retention(
        self,
        *,
        body: SetApiKeyRetentionRequestBody,
        parameters: SetApiKeyRetentionParameters | None = None,
        headers: SetApiKeyRetentionHeaders | None = None,
    ) -> SetApiKeyRetentionSuccessResponse:
        return cast(
            SetApiKeyRetentionSuccessResponse,
            await self._request_operation_async(
                "setApiKeyRetention", parameters=parameters, headers=headers, body=body
            ),
        )

    async def rotate_api_key(
        self,
        *,
        body: RotateApiKeyRequestBody,
        parameters: RotateApiKeyParameters | None = None,
        headers: RotateApiKeyHeaders | None = None,
    ) -> RotateApiKeySuccessResponse:
        return cast(
            RotateApiKeySuccessResponse,
            await self._request_operation_async(
                "rotateApiKey", parameters=parameters, headers=headers, body=body
            ),
        )

    async def cancel_api_key_rotation(
        self,
        *,
        parameters: CancelApiKeyRotationParameters | None = None,
        headers: CancelApiKeyRotationHeaders | None = None,
    ) -> CancelApiKeyRotationSuccessResponse:
        return cast(
            CancelApiKeyRotationSuccessResponse,
            await self._request_operation_async(
                "cancelApiKeyRotation",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def complete_api_key_rotation(
        self,
        *,
        parameters: CompleteApiKeyRotationParameters | None = None,
        headers: CompleteApiKeyRotationHeaders | None = None,
    ) -> CompleteApiKeyRotationSuccessResponse:
        return cast(
            CompleteApiKeyRotationSuccessResponse,
            await self._request_operation_async(
                "completeApiKeyRotation",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def get_api_key_signing_profile(
        self,
        *,
        parameters: GetApiKeySigningProfileParameters | None = None,
        headers: GetApiKeySigningProfileHeaders | None = None,
    ) -> GetApiKeySigningProfileSuccessResponse:
        return cast(
            GetApiKeySigningProfileSuccessResponse,
            await self._request_operation_async(
                "getApiKeySigningProfile",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def set_api_key_signing_profile(
        self,
        *,
        body: SetApiKeySigningProfileRequestBody,
        parameters: SetApiKeySigningProfileParameters | None = None,
        headers: SetApiKeySigningProfileHeaders | None = None,
    ) -> SetApiKeySigningProfileSuccessResponse:
        return cast(
            SetApiKeySigningProfileSuccessResponse,
            await self._request_operation_async(
                "setApiKeySigningProfile", parameters=parameters, headers=headers, body=body
            ),
        )

    async def list_api_key_scopes(
        self,
        *,
        parameters: ListApiKeyScopesParameters | None = None,
        headers: ListApiKeyScopesHeaders | None = None,
    ) -> ListApiKeyScopesSuccessResponse:
        return cast(
            ListApiKeyScopesSuccessResponse,
            await self._request_operation_async(
                "listApiKeyScopes",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def list_api_request_logs(
        self,
        *,
        parameters: ListApiRequestLogsParameters | None = None,
        headers: ListApiRequestLogsHeaders | None = None,
    ) -> ListApiRequestLogsSuccessResponse:
        return cast(
            ListApiRequestLogsSuccessResponse,
            await self._request_operation_async(
                "listApiRequestLogs",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def summarize_api_request_logs(
        self,
        *,
        parameters: SummarizeApiRequestLogsParameters | None = None,
        headers: SummarizeApiRequestLogsHeaders | None = None,
    ) -> SummarizeApiRequestLogsSuccessResponse:
        return cast(
            SummarizeApiRequestLogsSuccessResponse,
            await self._request_operation_async(
                "summarizeApiRequestLogs",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def list_assets(
        self,
        *,
        parameters: ListAssetsParameters | None = None,
        headers: ListAssetsHeaders | None = None,
    ) -> ListAssetsSuccessResponse:
        return cast(
            ListAssetsSuccessResponse,
            await self._request_operation_async(
                "listAssets",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def get_asset(
        self,
        *,
        parameters: GetAssetParameters | None = None,
        headers: GetAssetHeaders | None = None,
    ) -> GetAssetSuccessResponse:
        return cast(
            GetAssetSuccessResponse,
            await self._request_operation_async(
                "getAsset",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def get_asset_detail(
        self,
        *,
        parameters: GetAssetDetailParameters | None = None,
        headers: GetAssetDetailHeaders | None = None,
    ) -> GetAssetDetailSuccessResponse:
        return cast(
            GetAssetDetailSuccessResponse,
            await self._request_operation_async(
                "getAssetDetail",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def create_asset_download(
        self,
        *,
        parameters: CreateAssetDownloadParameters | None = None,
        headers: CreateAssetDownloadHeaders | None = None,
    ) -> CreateAssetDownloadSuccessResponse:
        return cast(
            CreateAssetDownloadSuccessResponse,
            await self._request_operation_async(
                "createAssetDownload",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def create_asset_preview(
        self,
        *,
        parameters: CreateAssetPreviewParameters | None = None,
        headers: CreateAssetPreviewHeaders | None = None,
    ) -> CreateAssetPreviewSuccessResponse:
        return cast(
            CreateAssetPreviewSuccessResponse,
            await self._request_operation_async(
                "createAssetPreview",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def redeem_asset_preview(
        self,
        *,
        parameters: RedeemAssetPreviewParameters | None = None,
        headers: RedeemAssetPreviewHeaders | None = None,
    ) -> RedeemAssetPreviewSuccessResponse:
        return cast(
            RedeemAssetPreviewSuccessResponse,
            await self._request_operation_async(
                "redeemAssetPreview",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def get_billing_account(
        self,
        *,
        parameters: GetBillingAccountParameters | None = None,
        headers: GetBillingAccountHeaders | None = None,
    ) -> GetBillingAccountSuccessResponse:
        return cast(
            GetBillingAccountSuccessResponse,
            await self._request_operation_async(
                "getBillingAccount",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def list_billing_charges(
        self,
        *,
        parameters: ListBillingChargesParameters | None = None,
        headers: ListBillingChargesHeaders | None = None,
    ) -> ListBillingChargesSuccessResponse:
        return cast(
            ListBillingChargesSuccessResponse,
            await self._request_operation_async(
                "listBillingCharges",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def create_billing_checkout_intent(
        self,
        *,
        body: CreateBillingCheckoutIntentRequestBody,
        parameters: CreateBillingCheckoutIntentParameters | None = None,
        headers: CreateBillingCheckoutIntentHeaders | None = None,
    ) -> CreateBillingCheckoutIntentSuccessResponse:
        return cast(
            CreateBillingCheckoutIntentSuccessResponse,
            await self._request_operation_async(
                "createBillingCheckoutIntent", parameters=parameters, headers=headers, body=body
            ),
        )

    async def list_billing_invoices(
        self,
        *,
        parameters: ListBillingInvoicesParameters | None = None,
        headers: ListBillingInvoicesHeaders | None = None,
    ) -> ListBillingInvoicesSuccessResponse:
        return cast(
            ListBillingInvoicesSuccessResponse,
            await self._request_operation_async(
                "listBillingInvoices",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def get_billing_plans(
        self,
        *,
        parameters: GetBillingPlansParameters | None = None,
        headers: GetBillingPlansHeaders | None = None,
    ) -> GetBillingPlansSuccessResponse:
        return cast(
            GetBillingPlansSuccessResponse,
            await self._request_operation_async(
                "getBillingPlans",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def create_billing_portal_intent(
        self,
        *,
        body: CreateBillingPortalIntentRequestBody,
        parameters: CreateBillingPortalIntentParameters | None = None,
        headers: CreateBillingPortalIntentHeaders | None = None,
    ) -> CreateBillingPortalIntentSuccessResponse:
        return cast(
            CreateBillingPortalIntentSuccessResponse,
            await self._request_operation_async(
                "createBillingPortalIntent", parameters=parameters, headers=headers, body=body
            ),
        )

    async def get_billing_pricing(
        self,
        *,
        parameters: GetBillingPricingParameters | None = None,
        headers: GetBillingPricingHeaders | None = None,
    ) -> GetBillingPricingSuccessResponse:
        return cast(
            GetBillingPricingSuccessResponse,
            await self._request_operation_async(
                "getBillingPricing",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def create_billing_quote(
        self,
        *,
        body: CreateBillingQuoteRequestBody,
        parameters: CreateBillingQuoteParameters | None = None,
        headers: CreateBillingQuoteHeaders | None = None,
    ) -> CreateBillingQuoteSuccessResponse:
        return cast(
            CreateBillingQuoteSuccessResponse,
            await self._request_operation_async(
                "createBillingQuote", parameters=parameters, headers=headers, body=body
            ),
        )

    async def get_billing_wallet(
        self,
        *,
        parameters: GetBillingWalletParameters | None = None,
        headers: GetBillingWalletHeaders | None = None,
    ) -> GetBillingWalletSuccessResponse:
        return cast(
            GetBillingWalletSuccessResponse,
            await self._request_operation_async(
                "getBillingWallet",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def set_billing_wallet_settings(
        self,
        *,
        body: SetBillingWalletSettingsRequestBody,
        parameters: SetBillingWalletSettingsParameters | None = None,
        headers: SetBillingWalletSettingsHeaders | None = None,
    ) -> SetBillingWalletSettingsSuccessResponse:
        return cast(
            SetBillingWalletSettingsSuccessResponse,
            await self._request_operation_async(
                "setBillingWalletSettings", parameters=parameters, headers=headers, body=body
            ),
        )

    async def get_capabilities(
        self,
        *,
        parameters: GetCapabilitiesParameters | None = None,
        headers: GetCapabilitiesHeaders | None = None,
    ) -> GetCapabilitiesSuccessResponse:
        return cast(
            GetCapabilitiesSuccessResponse,
            await self._request_operation_async(
                "getCapabilities",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def create_capture_admission_challenge(
        self,
        *,
        body: CreateCaptureAdmissionChallengeRequestBody,
        parameters: CreateCaptureAdmissionChallengeParameters | None = None,
        headers: CreateCaptureAdmissionChallengeHeaders | None = None,
    ) -> CreateCaptureAdmissionChallengeSuccessResponse:
        return cast(
            CreateCaptureAdmissionChallengeSuccessResponse,
            await self._request_operation_async(
                "createCaptureAdmissionChallenge", parameters=parameters, headers=headers, body=body
            ),
        )

    async def list_capture_admissions(
        self,
        *,
        parameters: ListCaptureAdmissionsParameters | None = None,
        headers: ListCaptureAdmissionsHeaders | None = None,
    ) -> ListCaptureAdmissionsSuccessResponse:
        return cast(
            ListCaptureAdmissionsSuccessResponse,
            await self._request_operation_async(
                "listCaptureAdmissions",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def create_capture_admission(
        self,
        *,
        body: CreateCaptureAdmissionRequestBody,
        parameters: CreateCaptureAdmissionParameters | None = None,
        headers: CreateCaptureAdmissionHeaders | None = None,
    ) -> CreateCaptureAdmissionSuccessResponse:
        return cast(
            CreateCaptureAdmissionSuccessResponse,
            await self._request_operation_async(
                "createCaptureAdmission", parameters=parameters, headers=headers, body=body
            ),
        )

    async def get_capture_admission(
        self,
        *,
        parameters: GetCaptureAdmissionParameters | None = None,
        headers: GetCaptureAdmissionHeaders | None = None,
    ) -> GetCaptureAdmissionSuccessResponse:
        return cast(
            GetCaptureAdmissionSuccessResponse,
            await self._request_operation_async(
                "getCaptureAdmission",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def list_capture_identities(
        self,
        *,
        parameters: ListCaptureIdentitiesParameters | None = None,
        headers: ListCaptureIdentitiesHeaders | None = None,
    ) -> ListCaptureIdentitiesSuccessResponse:
        return cast(
            ListCaptureIdentitiesSuccessResponse,
            await self._request_operation_async(
                "listCaptureIdentities",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def create_capture_identity(
        self,
        *,
        body: CreateCaptureIdentityRequestBody,
        parameters: CreateCaptureIdentityParameters | None = None,
        headers: CreateCaptureIdentityHeaders | None = None,
    ) -> CreateCaptureIdentitySuccessResponse:
        return cast(
            CreateCaptureIdentitySuccessResponse,
            await self._request_operation_async(
                "createCaptureIdentity", parameters=parameters, headers=headers, body=body
            ),
        )

    async def get_capture_identity(
        self,
        *,
        parameters: GetCaptureIdentityParameters | None = None,
        headers: GetCaptureIdentityHeaders | None = None,
    ) -> GetCaptureIdentitySuccessResponse:
        return cast(
            GetCaptureIdentitySuccessResponse,
            await self._request_operation_async(
                "getCaptureIdentity",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def revoke_capture_identity(
        self,
        *,
        parameters: RevokeCaptureIdentityParameters | None = None,
        headers: RevokeCaptureIdentityHeaders | None = None,
    ) -> RevokeCaptureIdentitySuccessResponse:
        return cast(
            RevokeCaptureIdentitySuccessResponse,
            await self._request_operation_async(
                "revokeCaptureIdentity",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def create_capture_identity_enrollment(
        self,
        *,
        body: CreateCaptureIdentityEnrollmentRequestBody,
        parameters: CreateCaptureIdentityEnrollmentParameters | None = None,
        headers: CreateCaptureIdentityEnrollmentHeaders | None = None,
    ) -> CreateCaptureIdentityEnrollmentSuccessResponse:
        return cast(
            CreateCaptureIdentityEnrollmentSuccessResponse,
            await self._request_operation_async(
                "createCaptureIdentityEnrollment", parameters=parameters, headers=headers, body=body
            ),
        )

    async def get_connect_catalog(
        self,
        *,
        parameters: GetConnectCatalogParameters | None = None,
        headers: GetConnectCatalogHeaders | None = None,
    ) -> GetConnectCatalogSuccessResponse:
        return cast(
            GetConnectCatalogSuccessResponse,
            await self._request_operation_async(
                "getConnectCatalog",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def get_creator_disclosure_policy(
        self,
        *,
        parameters: GetCreatorDisclosurePolicyParameters | None = None,
        headers: GetCreatorDisclosurePolicyHeaders | None = None,
    ) -> GetCreatorDisclosurePolicySuccessResponse:
        return cast(
            GetCreatorDisclosurePolicySuccessResponse,
            await self._request_operation_async(
                "getCreatorDisclosurePolicy",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def update_creator_disclosure_policy(
        self,
        *,
        body: UpdateCreatorDisclosurePolicyRequestBody,
        parameters: UpdateCreatorDisclosurePolicyParameters | None = None,
        headers: UpdateCreatorDisclosurePolicyHeaders | None = None,
    ) -> UpdateCreatorDisclosurePolicySuccessResponse:
        return cast(
            UpdateCreatorDisclosurePolicySuccessResponse,
            await self._request_operation_async(
                "updateCreatorDisclosurePolicy", parameters=parameters, headers=headers, body=body
            ),
        )

    async def list_creator_identities(
        self,
        *,
        parameters: ListCreatorIdentitiesParameters | None = None,
        headers: ListCreatorIdentitiesHeaders | None = None,
    ) -> ListCreatorIdentitiesSuccessResponse:
        return cast(
            ListCreatorIdentitiesSuccessResponse,
            await self._request_operation_async(
                "listCreatorIdentities",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def create_creator_identity(
        self,
        *,
        body: CreateCreatorIdentityRequestBody,
        parameters: CreateCreatorIdentityParameters | None = None,
        headers: CreateCreatorIdentityHeaders | None = None,
    ) -> CreateCreatorIdentitySuccessResponse:
        return cast(
            CreateCreatorIdentitySuccessResponse,
            await self._request_operation_async(
                "createCreatorIdentity", parameters=parameters, headers=headers, body=body
            ),
        )

    async def get_creator_identity(
        self,
        *,
        parameters: GetCreatorIdentityParameters | None = None,
        headers: GetCreatorIdentityHeaders | None = None,
    ) -> GetCreatorIdentitySuccessResponse:
        return cast(
            GetCreatorIdentitySuccessResponse,
            await self._request_operation_async(
                "getCreatorIdentity",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def disclose_creator_identity(
        self,
        *,
        parameters: DiscloseCreatorIdentityParameters | None = None,
        headers: DiscloseCreatorIdentityHeaders | None = None,
    ) -> DiscloseCreatorIdentitySuccessResponse:
        return cast(
            DiscloseCreatorIdentitySuccessResponse,
            await self._request_operation_async(
                "discloseCreatorIdentity",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def withdraw_creator_identity(
        self,
        *,
        parameters: WithdrawCreatorIdentityParameters | None = None,
        headers: WithdrawCreatorIdentityHeaders | None = None,
    ) -> WithdrawCreatorIdentitySuccessResponse:
        return cast(
            WithdrawCreatorIdentitySuccessResponse,
            await self._request_operation_async(
                "withdrawCreatorIdentity",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def get_developer_onboarding(
        self,
        *,
        parameters: GetDeveloperOnboardingParameters | None = None,
        headers: GetDeveloperOnboardingHeaders | None = None,
    ) -> GetDeveloperOnboardingSuccessResponse:
        return cast(
            GetDeveloperOnboardingSuccessResponse,
            await self._request_operation_async(
                "getDeveloperOnboarding",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def list_disclosure_events(
        self,
        *,
        parameters: ListDisclosureEventsParameters | None = None,
        headers: ListDisclosureEventsHeaders | None = None,
    ) -> ListDisclosureEventsSuccessResponse:
        return cast(
            ListDisclosureEventsSuccessResponse,
            await self._request_operation_async(
                "listDisclosureEvents",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def create_disclosure_event(
        self,
        *,
        body: CreateDisclosureEventRequestBody,
        parameters: CreateDisclosureEventParameters | None = None,
        headers: CreateDisclosureEventHeaders | None = None,
    ) -> CreateDisclosureEventSuccessResponse:
        return cast(
            CreateDisclosureEventSuccessResponse,
            await self._request_operation_async(
                "createDisclosureEvent", parameters=parameters, headers=headers, body=body
            ),
        )

    async def get_disclosure_policies(
        self,
        *,
        parameters: GetDisclosurePoliciesParameters | None = None,
        headers: GetDisclosurePoliciesHeaders | None = None,
    ) -> GetDisclosurePoliciesSuccessResponse:
        return cast(
            GetDisclosurePoliciesSuccessResponse,
            await self._request_operation_async(
                "getDisclosurePolicies",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def submit_feedback(
        self,
        *,
        body: SubmitFeedbackRequestBody,
        parameters: SubmitFeedbackParameters | None = None,
        headers: SubmitFeedbackHeaders | None = None,
    ) -> SubmitFeedbackSuccessResponse:
        return cast(
            SubmitFeedbackSuccessResponse,
            await self._request_operation_async(
                "submitFeedback", parameters=parameters, headers=headers, body=body
            ),
        )

    async def query_governance_audit(
        self,
        *,
        parameters: QueryGovernanceAuditParameters | None = None,
        headers: QueryGovernanceAuditHeaders | None = None,
    ) -> QueryGovernanceAuditSuccessResponse:
        return cast(
            QueryGovernanceAuditSuccessResponse,
            await self._request_operation_async(
                "queryGovernanceAudit",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def list_governance_deletions(
        self,
        *,
        parameters: ListGovernanceDeletionsParameters | None = None,
        headers: ListGovernanceDeletionsHeaders | None = None,
    ) -> ListGovernanceDeletionsSuccessResponse:
        return cast(
            ListGovernanceDeletionsSuccessResponse,
            await self._request_operation_async(
                "listGovernanceDeletions",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def create_governance_deletion(
        self,
        *,
        body: CreateGovernanceDeletionRequestBody,
        parameters: CreateGovernanceDeletionParameters | None = None,
        headers: CreateGovernanceDeletionHeaders | None = None,
    ) -> CreateGovernanceDeletionSuccessResponse:
        return cast(
            CreateGovernanceDeletionSuccessResponse,
            await self._request_operation_async(
                "createGovernanceDeletion", parameters=parameters, headers=headers, body=body
            ),
        )

    async def get_governance_deletion(
        self,
        *,
        parameters: GetGovernanceDeletionParameters | None = None,
        headers: GetGovernanceDeletionHeaders | None = None,
    ) -> GetGovernanceDeletionSuccessResponse:
        return cast(
            GetGovernanceDeletionSuccessResponse,
            await self._request_operation_async(
                "getGovernanceDeletion",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def list_governance_exports(
        self,
        *,
        parameters: ListGovernanceExportsParameters | None = None,
        headers: ListGovernanceExportsHeaders | None = None,
    ) -> ListGovernanceExportsSuccessResponse:
        return cast(
            ListGovernanceExportsSuccessResponse,
            await self._request_operation_async(
                "listGovernanceExports",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def create_governance_export(
        self,
        *,
        parameters: CreateGovernanceExportParameters | None = None,
        headers: CreateGovernanceExportHeaders | None = None,
    ) -> CreateGovernanceExportSuccessResponse:
        return cast(
            CreateGovernanceExportSuccessResponse,
            await self._request_operation_async(
                "createGovernanceExport",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def get_governance_export(
        self,
        *,
        parameters: GetGovernanceExportParameters | None = None,
        headers: GetGovernanceExportHeaders | None = None,
    ) -> GetGovernanceExportSuccessResponse:
        return cast(
            GetGovernanceExportSuccessResponse,
            await self._request_operation_async(
                "getGovernanceExport",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def list_governance_legal_holds(
        self,
        *,
        parameters: ListGovernanceLegalHoldsParameters | None = None,
        headers: ListGovernanceLegalHoldsHeaders | None = None,
    ) -> ListGovernanceLegalHoldsSuccessResponse:
        return cast(
            ListGovernanceLegalHoldsSuccessResponse,
            await self._request_operation_async(
                "listGovernanceLegalHolds",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def release_history_snapshot(
        self,
        *,
        parameters: ReleaseHistorySnapshotParameters | None = None,
        headers: ReleaseHistorySnapshotHeaders | None = None,
    ) -> ReleaseHistorySnapshotSuccessResponse:
        return cast(
            ReleaseHistorySnapshotSuccessResponse,
            await self._request_operation_async(
                "releaseHistorySnapshot",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def list_identity_credentials(
        self,
        *,
        parameters: ListIdentityCredentialsParameters | None = None,
        headers: ListIdentityCredentialsHeaders | None = None,
    ) -> ListIdentityCredentialsSuccessResponse:
        return cast(
            ListIdentityCredentialsSuccessResponse,
            await self._request_operation_async(
                "listIdentityCredentials",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def list_image_profiles(
        self,
        *,
        parameters: ListImageProfilesParameters | None = None,
        headers: ListImageProfilesHeaders | None = None,
    ) -> ListImageProfilesSuccessResponse:
        return cast(
            ListImageProfilesSuccessResponse,
            await self._request_operation_async(
                "listImageProfiles",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def list_jobs(
        self,
        *,
        parameters: ListJobsParameters | None = None,
        headers: ListJobsHeaders | None = None,
    ) -> ListJobsSuccessResponse:
        return cast(
            ListJobsSuccessResponse,
            await self._request_operation_async(
                "listJobs",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def get_job(
        self,
        *,
        parameters: GetJobParameters | None = None,
        headers: GetJobHeaders | None = None,
    ) -> GetJobSuccessResponse:
        return cast(
            GetJobSuccessResponse,
            await self._request_operation_async(
                "getJob",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def cancel_job(
        self,
        *,
        body: CancelJobRequestBody,
        parameters: CancelJobParameters | None = None,
        headers: CancelJobHeaders | None = None,
    ) -> CancelJobSuccessResponse:
        return cast(
            CancelJobSuccessResponse,
            await self._request_operation_async(
                "cancelJob", parameters=parameters, headers=headers, body=body
            ),
        )

    async def create_marking_check(
        self,
        *,
        body: CreateMarkingCheckRequestBody,
        parameters: CreateMarkingCheckParameters | None = None,
        headers: CreateMarkingCheckHeaders | None = None,
    ) -> CreateMarkingCheckSuccessResponse:
        return cast(
            CreateMarkingCheckSuccessResponse,
            await self._request_operation_async(
                "createMarkingCheck", parameters=parameters, headers=headers, body=body
            ),
        )

    async def get_marking_check(
        self,
        *,
        parameters: GetMarkingCheckParameters | None = None,
        headers: GetMarkingCheckHeaders | None = None,
    ) -> GetMarkingCheckSuccessResponse:
        return cast(
            GetMarkingCheckSuccessResponse,
            await self._request_operation_async(
                "getMarkingCheck",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def get_current_user(
        self,
        *,
        parameters: GetCurrentUserParameters | None = None,
        headers: GetCurrentUserHeaders | None = None,
    ) -> GetCurrentUserSuccessResponse:
        return cast(
            GetCurrentUserSuccessResponse,
            await self._request_operation_async(
                "getCurrentUser",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def get_overview(
        self,
        *,
        parameters: GetOverviewParameters | None = None,
        headers: GetOverviewHeaders | None = None,
    ) -> GetOverviewSuccessResponse:
        return cast(
            GetOverviewSuccessResponse,
            await self._request_operation_async(
                "getOverview",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def get_public_verify_page(
        self,
        *,
        parameters: GetPublicVerifyPageParameters | None = None,
        headers: GetPublicVerifyPageHeaders | None = None,
    ) -> GetPublicVerifyPageSuccessResponse:
        return cast(
            GetPublicVerifyPageSuccessResponse,
            await self._request_operation_async(
                "getPublicVerifyPage",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def create_public_check(
        self,
        *,
        parameters: CreatePublicCheckParameters | None = None,
        headers: CreatePublicCheckHeaders | None = None,
    ) -> CreatePublicCheckSuccessResponse:
        return cast(
            CreatePublicCheckSuccessResponse,
            await self._request_operation_async(
                "createPublicCheck",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def get_public_check(
        self,
        *,
        parameters: GetPublicCheckParameters | None = None,
        headers: GetPublicCheckHeaders | None = None,
    ) -> GetPublicCheckSuccessResponse:
        return cast(
            GetPublicCheckSuccessResponse,
            await self._request_operation_async(
                "getPublicCheck",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def get_public_verify_page_logo(
        self,
        *,
        parameters: GetPublicVerifyPageLogoParameters | None = None,
        headers: GetPublicVerifyPageLogoHeaders | None = None,
    ) -> GetPublicVerifyPageLogoSuccessResponse:
        return cast(
            GetPublicVerifyPageLogoSuccessResponse,
            await self._request_operation_async(
                "getPublicVerifyPageLogo",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def list_receipts(
        self,
        *,
        parameters: ListReceiptsParameters | None = None,
        headers: ListReceiptsHeaders | None = None,
    ) -> ListReceiptsSuccessResponse:
        return cast(
            ListReceiptsSuccessResponse,
            await self._request_operation_async(
                "listReceipts",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def get_signing_receipt(
        self,
        *,
        parameters: GetSigningReceiptParameters | None = None,
        headers: GetSigningReceiptHeaders | None = None,
    ) -> GetSigningReceiptSuccessResponse:
        return cast(
            GetSigningReceiptSuccessResponse,
            await self._request_operation_async(
                "getSigningReceipt",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def list_recipes(
        self,
        *,
        parameters: ListRecipesParameters | None = None,
        headers: ListRecipesHeaders | None = None,
    ) -> ListRecipesSuccessResponse:
        return cast(
            ListRecipesSuccessResponse,
            await self._request_operation_async(
                "listRecipes",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def get_recipe(
        self,
        *,
        parameters: GetRecipeParameters | None = None,
        headers: GetRecipeHeaders | None = None,
    ) -> GetRecipeSuccessResponse:
        return cast(
            GetRecipeSuccessResponse,
            await self._request_operation_async(
                "getRecipe",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def get_shared_verification(
        self,
        *,
        parameters: GetSharedVerificationParameters | None = None,
        headers: GetSharedVerificationHeaders | None = None,
    ) -> GetSharedVerificationSuccessResponse:
        return cast(
            GetSharedVerificationSuccessResponse,
            await self._request_operation_async(
                "getSharedVerification",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def accept_signing_job(
        self,
        *,
        body: AcceptSigningJobRequestBody,
        parameters: AcceptSigningJobParameters | None = None,
        headers: AcceptSigningJobHeaders | None = None,
    ) -> AcceptSigningJobSuccessResponse:
        return cast(
            AcceptSigningJobSuccessResponse,
            await self._request_operation_async(
                "acceptSigningJob", parameters=parameters, headers=headers, body=body
            ),
        )

    async def accept_signing_job_batch(
        self,
        *,
        body: AcceptSigningJobBatchRequestBody,
        parameters: AcceptSigningJobBatchParameters | None = None,
        headers: AcceptSigningJobBatchHeaders | None = None,
    ) -> AcceptSigningJobBatchSuccessResponse:
        return cast(
            AcceptSigningJobBatchSuccessResponse,
            await self._request_operation_async(
                "acceptSigningJobBatch", parameters=parameters, headers=headers, body=body
            ),
        )

    async def create_upload(
        self,
        *,
        body: CreateUploadRequestBody,
        parameters: CreateUploadParameters | None = None,
        headers: CreateUploadHeaders | None = None,
    ) -> CreateUploadSuccessResponse:
        return cast(
            CreateUploadSuccessResponse,
            await self._request_operation_async(
                "createUpload", parameters=parameters, headers=headers, body=body
            ),
        )

    async def abort_upload(
        self,
        *,
        parameters: AbortUploadParameters | None = None,
        headers: AbortUploadHeaders | None = None,
    ) -> AbortUploadSuccessResponse:
        return cast(
            AbortUploadSuccessResponse,
            await self._request_operation_async(
                "abortUpload",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def complete_upload(
        self,
        *,
        body: CompleteUploadRequestBody,
        parameters: CompleteUploadParameters | None = None,
        headers: CompleteUploadHeaders | None = None,
    ) -> CompleteUploadSuccessResponse:
        return cast(
            CompleteUploadSuccessResponse,
            await self._request_operation_async(
                "completeUpload", parameters=parameters, headers=headers, body=body
            ),
        )

    async def get_usage(
        self,
        *,
        parameters: GetUsageParameters | None = None,
        headers: GetUsageHeaders | None = None,
    ) -> GetUsageSuccessResponse:
        return cast(
            GetUsageSuccessResponse,
            await self._request_operation_async(
                "getUsage",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def get_verification_evidence(
        self,
        *,
        parameters: GetVerificationEvidenceParameters | None = None,
        headers: GetVerificationEvidenceHeaders | None = None,
    ) -> GetVerificationEvidenceSuccessResponse:
        return cast(
            GetVerificationEvidenceSuccessResponse,
            await self._request_operation_async(
                "getVerificationEvidence",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def create_verification_report(
        self,
        *,
        body: CreateVerificationReportRequestBody,
        parameters: CreateVerificationReportParameters | None = None,
        headers: CreateVerificationReportHeaders | None = None,
    ) -> CreateVerificationReportSuccessResponse:
        return cast(
            CreateVerificationReportSuccessResponse,
            await self._request_operation_async(
                "createVerificationReport", parameters=parameters, headers=headers, body=body
            ),
        )

    async def list_verification_shares(
        self,
        *,
        parameters: ListVerificationSharesParameters | None = None,
        headers: ListVerificationSharesHeaders | None = None,
    ) -> ListVerificationSharesSuccessResponse:
        return cast(
            ListVerificationSharesSuccessResponse,
            await self._request_operation_async(
                "listVerificationShares",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def create_verification_share(
        self,
        *,
        body: CreateVerificationShareRequestBody,
        parameters: CreateVerificationShareParameters | None = None,
        headers: CreateVerificationShareHeaders | None = None,
    ) -> CreateVerificationShareSuccessResponse:
        return cast(
            CreateVerificationShareSuccessResponse,
            await self._request_operation_async(
                "createVerificationShare", parameters=parameters, headers=headers, body=body
            ),
        )

    async def get_verification_history(
        self,
        *,
        parameters: GetVerificationHistoryParameters | None = None,
        headers: GetVerificationHistoryHeaders | None = None,
    ) -> GetVerificationHistorySuccessResponse:
        return cast(
            GetVerificationHistorySuccessResponse,
            await self._request_operation_async(
                "getVerificationHistory",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def get_verification_report(
        self,
        *,
        parameters: GetVerificationReportParameters | None = None,
        headers: GetVerificationReportHeaders | None = None,
    ) -> GetVerificationReportSuccessResponse:
        return cast(
            GetVerificationReportSuccessResponse,
            await self._request_operation_async(
                "getVerificationReport",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def close_verification_share(
        self,
        *,
        body: CloseVerificationShareRequestBody,
        parameters: CloseVerificationShareParameters | None = None,
        headers: CloseVerificationShareHeaders | None = None,
    ) -> CloseVerificationShareSuccessResponse:
        return cast(
            CloseVerificationShareSuccessResponse,
            await self._request_operation_async(
                "closeVerificationShare", parameters=parameters, headers=headers, body=body
            ),
        )

    async def list_verifications(
        self,
        *,
        parameters: ListVerificationsParameters | None = None,
        headers: ListVerificationsHeaders | None = None,
    ) -> ListVerificationsSuccessResponse:
        return cast(
            ListVerificationsSuccessResponse,
            await self._request_operation_async(
                "listVerifications",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def create_verification(
        self,
        *,
        body: CreateVerificationRequestBody,
        parameters: CreateVerificationParameters | None = None,
        headers: CreateVerificationHeaders | None = None,
    ) -> CreateVerificationSuccessResponse:
        return cast(
            CreateVerificationSuccessResponse,
            await self._request_operation_async(
                "createVerification", parameters=parameters, headers=headers, body=body
            ),
        )

    async def get_verification(
        self,
        *,
        parameters: GetVerificationParameters | None = None,
        headers: GetVerificationHeaders | None = None,
    ) -> GetVerificationSuccessResponse:
        return cast(
            GetVerificationSuccessResponse,
            await self._request_operation_async(
                "getVerification",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def create_verification_batch(
        self,
        *,
        body: CreateVerificationBatchRequestBody,
        parameters: CreateVerificationBatchParameters | None = None,
        headers: CreateVerificationBatchHeaders | None = None,
    ) -> CreateVerificationBatchSuccessResponse:
        return cast(
            CreateVerificationBatchSuccessResponse,
            await self._request_operation_async(
                "createVerificationBatch", parameters=parameters, headers=headers, body=body
            ),
        )

    async def get_verify_page(
        self,
        *,
        parameters: GetVerifyPageParameters | None = None,
        headers: GetVerifyPageHeaders | None = None,
    ) -> GetVerifyPageSuccessResponse:
        return cast(
            GetVerifyPageSuccessResponse,
            await self._request_operation_async(
                "getVerifyPage",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def put_verify_page(
        self,
        *,
        body: PutVerifyPageRequestBody,
        parameters: PutVerifyPageParameters | None = None,
        headers: PutVerifyPageHeaders | None = None,
    ) -> PutVerifyPageSuccessResponse:
        return cast(
            PutVerifyPageSuccessResponse,
            await self._request_operation_async(
                "putVerifyPage", parameters=parameters, headers=headers, body=body
            ),
        )

    async def list_webhook_endpoints(
        self,
        *,
        parameters: ListWebhookEndpointsParameters | None = None,
        headers: ListWebhookEndpointsHeaders | None = None,
    ) -> ListWebhookEndpointsSuccessResponse:
        return cast(
            ListWebhookEndpointsSuccessResponse,
            await self._request_operation_async(
                "listWebhookEndpoints",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def create_webhook_endpoint(
        self,
        *,
        body: CreateWebhookEndpointRequestBody,
        parameters: CreateWebhookEndpointParameters | None = None,
        headers: CreateWebhookEndpointHeaders | None = None,
    ) -> CreateWebhookEndpointSuccessResponse:
        return cast(
            CreateWebhookEndpointSuccessResponse,
            await self._request_operation_async(
                "createWebhookEndpoint", parameters=parameters, headers=headers, body=body
            ),
        )

    async def delete_webhook_endpoint(
        self,
        *,
        parameters: DeleteWebhookEndpointParameters | None = None,
        headers: DeleteWebhookEndpointHeaders | None = None,
    ) -> DeleteWebhookEndpointSuccessResponse:
        return cast(
            DeleteWebhookEndpointSuccessResponse,
            await self._request_operation_async(
                "deleteWebhookEndpoint",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def get_webhook_endpoint(
        self,
        *,
        parameters: GetWebhookEndpointParameters | None = None,
        headers: GetWebhookEndpointHeaders | None = None,
    ) -> GetWebhookEndpointSuccessResponse:
        return cast(
            GetWebhookEndpointSuccessResponse,
            await self._request_operation_async(
                "getWebhookEndpoint",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def update_webhook_endpoint(
        self,
        *,
        body: UpdateWebhookEndpointRequestBody,
        parameters: UpdateWebhookEndpointParameters | None = None,
        headers: UpdateWebhookEndpointHeaders | None = None,
    ) -> UpdateWebhookEndpointSuccessResponse:
        return cast(
            UpdateWebhookEndpointSuccessResponse,
            await self._request_operation_async(
                "updateWebhookEndpoint", parameters=parameters, headers=headers, body=body
            ),
        )

    async def list_webhook_deliveries(
        self,
        *,
        parameters: ListWebhookDeliveriesParameters | None = None,
        headers: ListWebhookDeliveriesHeaders | None = None,
    ) -> ListWebhookDeliveriesSuccessResponse:
        return cast(
            ListWebhookDeliveriesSuccessResponse,
            await self._request_operation_async(
                "listWebhookDeliveries",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def disable_webhook_endpoint(
        self,
        *,
        parameters: DisableWebhookEndpointParameters | None = None,
        headers: DisableWebhookEndpointHeaders | None = None,
    ) -> DisableWebhookEndpointSuccessResponse:
        return cast(
            DisableWebhookEndpointSuccessResponse,
            await self._request_operation_async(
                "disableWebhookEndpoint",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def enable_webhook_endpoint(
        self,
        *,
        parameters: EnableWebhookEndpointParameters | None = None,
        headers: EnableWebhookEndpointHeaders | None = None,
    ) -> EnableWebhookEndpointSuccessResponse:
        return cast(
            EnableWebhookEndpointSuccessResponse,
            await self._request_operation_async(
                "enableWebhookEndpoint",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def rotate_webhook_endpoint_secret(
        self,
        *,
        body: RotateWebhookEndpointSecretRequestBody | None = None,
        parameters: RotateWebhookEndpointSecretParameters | None = None,
        headers: RotateWebhookEndpointSecretHeaders | None = None,
    ) -> RotateWebhookEndpointSecretSuccessResponse:
        return cast(
            RotateWebhookEndpointSecretSuccessResponse,
            await self._request_operation_async(
                "rotateWebhookEndpointSecret", parameters=parameters, headers=headers, body=body
            ),
        )

    async def complete_webhook_endpoint_secret_overlap(
        self,
        *,
        parameters: CompleteWebhookEndpointSecretOverlapParameters | None = None,
        headers: CompleteWebhookEndpointSecretOverlapHeaders | None = None,
    ) -> CompleteWebhookEndpointSecretOverlapSuccessResponse:
        return cast(
            CompleteWebhookEndpointSecretOverlapSuccessResponse,
            await self._request_operation_async(
                "completeWebhookEndpointSecretOverlap",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def send_webhook_test_event(
        self,
        *,
        parameters: SendWebhookTestEventParameters | None = None,
        headers: SendWebhookTestEventHeaders | None = None,
    ) -> SendWebhookTestEventSuccessResponse:
        return cast(
            SendWebhookTestEventSuccessResponse,
            await self._request_operation_async(
                "sendWebhookTestEvent",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def get_webhook_delivery(
        self,
        *,
        parameters: GetWebhookDeliveryParameters | None = None,
        headers: GetWebhookDeliveryHeaders | None = None,
    ) -> GetWebhookDeliverySuccessResponse:
        return cast(
            GetWebhookDeliverySuccessResponse,
            await self._request_operation_async(
                "getWebhookDelivery",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def list_webhook_delivery_attempts(
        self,
        *,
        parameters: ListWebhookDeliveryAttemptsParameters | None = None,
        headers: ListWebhookDeliveryAttemptsHeaders | None = None,
    ) -> ListWebhookDeliveryAttemptsSuccessResponse:
        return cast(
            ListWebhookDeliveryAttemptsSuccessResponse,
            await self._request_operation_async(
                "listWebhookDeliveryAttempts",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def replay_webhook_delivery(
        self,
        *,
        parameters: ReplayWebhookDeliveryParameters | None = None,
        headers: ReplayWebhookDeliveryHeaders | None = None,
    ) -> ReplayWebhookDeliverySuccessResponse:
        return cast(
            ReplayWebhookDeliverySuccessResponse,
            await self._request_operation_async(
                "replayWebhookDelivery",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def get_webhook_event_catalog(
        self,
        *,
        parameters: GetWebhookEventCatalogParameters | None = None,
        headers: GetWebhookEventCatalogHeaders | None = None,
    ) -> GetWebhookEventCatalogSuccessResponse:
        return cast(
            GetWebhookEventCatalogSuccessResponse,
            await self._request_operation_async(
                "getWebhookEventCatalog",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def replay_webhook_event(
        self,
        *,
        parameters: ReplayWebhookEventParameters | None = None,
        headers: ReplayWebhookEventHeaders | None = None,
    ) -> ReplayWebhookEventSuccessResponse:
        return cast(
            ReplayWebhookEventSuccessResponse,
            await self._request_operation_async(
                "replayWebhookEvent",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def list_workflow_templates(
        self,
        *,
        parameters: ListWorkflowTemplatesParameters | None = None,
        headers: ListWorkflowTemplatesHeaders | None = None,
    ) -> ListWorkflowTemplatesSuccessResponse:
        return cast(
            ListWorkflowTemplatesSuccessResponse,
            await self._request_operation_async(
                "listWorkflowTemplates",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def create_workflow_template(
        self,
        *,
        body: CreateWorkflowTemplateRequestBody,
        parameters: CreateWorkflowTemplateParameters | None = None,
        headers: CreateWorkflowTemplateHeaders | None = None,
    ) -> CreateWorkflowTemplateSuccessResponse:
        return cast(
            CreateWorkflowTemplateSuccessResponse,
            await self._request_operation_async(
                "createWorkflowTemplate", parameters=parameters, headers=headers, body=body
            ),
        )

    async def delete_workflow_template(
        self,
        *,
        parameters: DeleteWorkflowTemplateParameters | None = None,
        headers: DeleteWorkflowTemplateHeaders | None = None,
    ) -> DeleteWorkflowTemplateSuccessResponse:
        return cast(
            DeleteWorkflowTemplateSuccessResponse,
            await self._request_operation_async(
                "deleteWorkflowTemplate",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def get_workflow_template(
        self,
        *,
        parameters: GetWorkflowTemplateParameters | None = None,
        headers: GetWorkflowTemplateHeaders | None = None,
    ) -> GetWorkflowTemplateSuccessResponse:
        return cast(
            GetWorkflowTemplateSuccessResponse,
            await self._request_operation_async(
                "getWorkflowTemplate",
                parameters=parameters,
                headers=headers,
            ),
        )

    async def replace_workflow_template(
        self,
        *,
        body: ReplaceWorkflowTemplateRequestBody,
        parameters: ReplaceWorkflowTemplateParameters | None = None,
        headers: ReplaceWorkflowTemplateHeaders | None = None,
    ) -> ReplaceWorkflowTemplateSuccessResponse:
        return cast(
            ReplaceWorkflowTemplateSuccessResponse,
            await self._request_operation_async(
                "replaceWorkflowTemplate", parameters=parameters, headers=headers, body=body
            ),
        )


__all__ = [
    "PUBLIC_API_OPENAPI_SHA256",
    "PUBLIC_API_OPERATIONS",
    "PUBLIC_API_VERSION",
    "PublicApiOperationContract",
    "PublicApiResponseContract",
    "AbortUploadErrorResponses",
    "AbortUploadHeaders",
    "AbortUploadOperation",
    "AbortUploadParameters",
    "AbortUploadRequestBody",
    "AbortUploadResponse",
    "AbortUploadResponses",
    "AbortUploadSuccessResponse",
    "AbortUploadSuccessResponses",
    "AcceptSigningJobBatchErrorResponses",
    "AcceptSigningJobBatchHeaders",
    "AcceptSigningJobBatchOperation",
    "AcceptSigningJobBatchParameters",
    "AcceptSigningJobBatchRequestBody",
    "AcceptSigningJobBatchResponses",
    "AcceptSigningJobBatchSuccessResponse",
    "AcceptSigningJobBatchSuccessResponses",
    "AcceptSigningJobErrorResponses",
    "AcceptSigningJobHeaders",
    "AcceptSigningJobOperation",
    "AcceptSigningJobParameters",
    "AcceptSigningJobRequestBody",
    "AcceptSigningJobResponses",
    "AcceptSigningJobSuccessResponse",
    "AcceptSigningJobSuccessResponses",
    "AiActionResponse",
    "AiDeclarationRequest",
    "AiDeclaredSigningReceiptEvidenceResponse",
    "AiMarkBlock",
    "AiModelDisclosureRequest",
    "AiPromptResponse",
    "ApiKeyCreateRequest",
    "ApiKeyListResponse",
    "ApiKeyMetadataResponse",
    "ApiKeyPreset",
    "ApiKeyRestrictionsRequest",
    "ApiKeyRestrictionsResponse",
    "ApiKeyRestrictionsUpdateRequest",
    "ApiKeyRestrictionsView",
    "ApiKeyRetentionRequest",
    "ApiKeyRetentionResponse",
    "ApiKeyRotateRequest",
    "ApiKeyRotationResponse",
    "ApiKeyRotationRole",
    "ApiKeyScopeCatalogResponse",
    "ApiKeyScopeDescriptorResponse",
    "ApiKeyScopeGroupResponse",
    "ApiKeySigningProfileDocument",
    "ApiKeySigningProfileResponse",
    "ApiKeySigningProfileUpdateRequest",
    "ApiKeyStatus",
    "ApiRequestLogItem",
    "ApiRequestLogPageResponse",
    "ApiRequestLogStatusClasses",
    "ApiRequestLogSummaryResponse",
    "AssetAction",
    "AssetActionReason",
    "AssetActionResponse",
    "AssetActivityEventResponse",
    "AssetActivityKind",
    "AssetActivityResponse",
    "AssetDeletionState",
    "AssetDetailResponse",
    "AssetGovernanceResponse",
    "AssetHistoryKind",
    "AssetHistoryOrigin",
    "AssetHistoryPageResponse",
    "AssetHistoryResponse",
    "AssetHistoryStatus",
    "AssetJobResponse",
    "AssetMediaFamily",
    "AssetMediaResponse",
    "AssetPreviewState",
    "AssetResponse",
    "AssetRetentionClassResponse",
    "AssetRetentionResponse",
    "AssetVerificationEntryResponse",
    "AssetVerificationHistoryResponse",
    "AssetVerificationResponse",
    "AttestationKind",
    "AudioCodec",
    "AudioTrackFacts",
    "AuditEventResponse",
    "BillingAccountResponse",
    "BillingIntentResponse",
    "BillingInvoiceResponse",
    "BillingInvoicesResponse",
    "BillingPlanId",
    "BillingPlanResponse",
    "BillingPlansResponse",
    "BindingReceiptEvidenceResponse",
    "ByteRange",
    "C2PAStatusVocabularyVersion",
    "CancelApiKeyRotationErrorResponses",
    "CancelApiKeyRotationHeaders",
    "CancelApiKeyRotationOperation",
    "CancelApiKeyRotationParameters",
    "CancelApiKeyRotationRequestBody",
    "CancelApiKeyRotationResponses",
    "CancelApiKeyRotationSuccessResponse",
    "CancelApiKeyRotationSuccessResponses",
    "CancelJobErrorResponses",
    "CancelJobHeaders",
    "CancelJobOperation",
    "CancelJobParameters",
    "CancelJobRequest",
    "CancelJobRequestBody",
    "CancelJobResponses",
    "CancelJobSuccessResponse",
    "CancelJobSuccessResponses",
    "CanonicalCallResponse",
    "CapabilityAvailabilityResponse",
    "CapabilityAvailabilityState",
    "CapabilityDiscoveryResponse",
    "CapabilityRecipeResponse",
    "CaptureAdmissionChallengeRequest",
    "CaptureAdmissionChallengeResponse",
    "CaptureAdmissionDecision",
    "CaptureAdmissionDetail",
    "CaptureAdmissionListResponse",
    "CaptureAdmissionSubmissionRequest",
    "CaptureAdmissionSubmissionResponse",
    "CaptureAdmissionSummary",
    "CaptureCapabilityResponse",
    "CaptureIdentityCreationRequest",
    "CaptureIdentityDetail",
    "CaptureIdentityEnrollmentRequest",
    "CaptureIdentityEnrollmentResponse",
    "CaptureIdentityEnrollmentResult",
    "CaptureIdentityFilterState",
    "CaptureIdentityListResponse",
    "CaptureIdentityPlatform",
    "CaptureIdentityRevocationResponse",
    "CaptureIdentityState",
    "CaptureIdentitySummary",
    "CaptureManagementErrorCode",
    "CaptureManagementErrorResponse",
    "CaptureProviderClass",
    "CawgIdentityBlock",
    "CheckoutIntentRequest",
    "CloseShareRequest",
    "CloseShareResponse",
    "CloseVerificationShareErrorResponses",
    "CloseVerificationShareHeaders",
    "CloseVerificationShareOperation",
    "CloseVerificationShareParameters",
    "CloseVerificationShareRequestBody",
    "CloseVerificationShareResponses",
    "CloseVerificationShareSuccessResponse",
    "CloseVerificationShareSuccessResponses",
    "ColorProfileFacts",
    "CommonErrorMeaningResponse",
    "CompleteApiKeyRotationErrorResponses",
    "CompleteApiKeyRotationHeaders",
    "CompleteApiKeyRotationOperation",
    "CompleteApiKeyRotationParameters",
    "CompleteApiKeyRotationRequestBody",
    "CompleteApiKeyRotationResponses",
    "CompleteApiKeyRotationSuccessResponse",
    "CompleteApiKeyRotationSuccessResponses",
    "CompletePartRequest",
    "CompleteUploadErrorResponses",
    "CompleteUploadHeaders",
    "CompleteUploadOperation",
    "CompleteUploadParameters",
    "CompleteUploadRequest",
    "CompleteUploadRequestBody",
    "CompleteUploadResponse",
    "CompleteUploadResponses",
    "CompleteUploadSuccessResponse",
    "CompleteUploadSuccessResponses",
    "CompleteWebhookEndpointSecretOverlapErrorResponses",
    "CompleteWebhookEndpointSecretOverlapHeaders",
    "CompleteWebhookEndpointSecretOverlapOperation",
    "CompleteWebhookEndpointSecretOverlapParameters",
    "CompleteWebhookEndpointSecretOverlapRequestBody",
    "CompleteWebhookEndpointSecretOverlapResponses",
    "CompleteWebhookEndpointSecretOverlapSuccessResponse",
    "CompleteWebhookEndpointSecretOverlapSuccessResponses",
    "ComponentVersion",
    "ConnectCatalogResponse",
    "ConnectClientResponse",
    "ConnectEnvironmentVariableResponse",
    "ConnectModeResponse",
    "ConnectTemplatePartKind",
    "ConnectTemplatePartResponse",
    "ConnectTemplateResponse",
    "ContractCapabilityResponse",
    "CreateApiKeyErrorResponses",
    "CreateApiKeyHeaders",
    "CreateApiKeyOperation",
    "CreateApiKeyParameters",
    "CreateApiKeyRequestBody",
    "CreateApiKeyResponses",
    "CreateApiKeySuccessResponse",
    "CreateApiKeySuccessResponses",
    "CreateAssetDownloadErrorResponses",
    "CreateAssetDownloadHeaders",
    "CreateAssetDownloadOperation",
    "CreateAssetDownloadParameters",
    "CreateAssetDownloadRequestBody",
    "CreateAssetDownloadResponses",
    "CreateAssetDownloadSuccessResponse",
    "CreateAssetDownloadSuccessResponses",
    "CreateAssetPreviewErrorResponses",
    "CreateAssetPreviewHeaders",
    "CreateAssetPreviewOperation",
    "CreateAssetPreviewParameters",
    "CreateAssetPreviewRequestBody",
    "CreateAssetPreviewResponses",
    "CreateAssetPreviewSuccessResponse",
    "CreateAssetPreviewSuccessResponses",
    "CreateBillingCheckoutIntentErrorResponses",
    "CreateBillingCheckoutIntentHeaders",
    "CreateBillingCheckoutIntentOperation",
    "CreateBillingCheckoutIntentParameters",
    "CreateBillingCheckoutIntentRequestBody",
    "CreateBillingCheckoutIntentResponses",
    "CreateBillingCheckoutIntentSuccessResponse",
    "CreateBillingCheckoutIntentSuccessResponses",
    "CreateBillingPortalIntentErrorResponses",
    "CreateBillingPortalIntentHeaders",
    "CreateBillingPortalIntentOperation",
    "CreateBillingPortalIntentParameters",
    "CreateBillingPortalIntentRequestBody",
    "CreateBillingPortalIntentResponses",
    "CreateBillingPortalIntentSuccessResponse",
    "CreateBillingPortalIntentSuccessResponses",
    "CreateBillingQuoteErrorResponses",
    "CreateBillingQuoteHeaders",
    "CreateBillingQuoteOperation",
    "CreateBillingQuoteParameters",
    "CreateBillingQuoteRequestBody",
    "CreateBillingQuoteResponses",
    "CreateBillingQuoteSuccessResponse",
    "CreateBillingQuoteSuccessResponses",
    "CreateCaptureAdmissionChallengeErrorResponses",
    "CreateCaptureAdmissionChallengeHeaders",
    "CreateCaptureAdmissionChallengeOperation",
    "CreateCaptureAdmissionChallengeParameters",
    "CreateCaptureAdmissionChallengeRequestBody",
    "CreateCaptureAdmissionChallengeResponses",
    "CreateCaptureAdmissionChallengeSuccessResponse",
    "CreateCaptureAdmissionChallengeSuccessResponses",
    "CreateCaptureAdmissionErrorResponses",
    "CreateCaptureAdmissionHeaders",
    "CreateCaptureAdmissionOperation",
    "CreateCaptureAdmissionParameters",
    "CreateCaptureAdmissionRequestBody",
    "CreateCaptureAdmissionResponses",
    "CreateCaptureAdmissionSuccessResponse",
    "CreateCaptureAdmissionSuccessResponses",
    "CreateCaptureIdentityEnrollmentErrorResponses",
    "CreateCaptureIdentityEnrollmentHeaders",
    "CreateCaptureIdentityEnrollmentOperation",
    "CreateCaptureIdentityEnrollmentParameters",
    "CreateCaptureIdentityEnrollmentRequestBody",
    "CreateCaptureIdentityEnrollmentResponses",
    "CreateCaptureIdentityEnrollmentSuccessResponse",
    "CreateCaptureIdentityEnrollmentSuccessResponses",
    "CreateCaptureIdentityErrorResponses",
    "CreateCaptureIdentityHeaders",
    "CreateCaptureIdentityOperation",
    "CreateCaptureIdentityParameters",
    "CreateCaptureIdentityRequestBody",
    "CreateCaptureIdentityResponses",
    "CreateCaptureIdentitySuccessResponse",
    "CreateCaptureIdentitySuccessResponses",
    "CreateCreatorIdentityErrorResponses",
    "CreateCreatorIdentityHeaders",
    "CreateCreatorIdentityOperation",
    "CreateCreatorIdentityParameters",
    "CreateCreatorIdentityRequestBody",
    "CreateCreatorIdentityResponses",
    "CreateCreatorIdentitySuccessResponse",
    "CreateCreatorIdentitySuccessResponses",
    "CreateDisclosureEventErrorResponses",
    "CreateDisclosureEventHeaders",
    "CreateDisclosureEventOperation",
    "CreateDisclosureEventParameters",
    "CreateDisclosureEventRequestBody",
    "CreateDisclosureEventResponses",
    "CreateDisclosureEventSuccessResponse",
    "CreateDisclosureEventSuccessResponses",
    "CreateGovernanceDeletionErrorResponses",
    "CreateGovernanceDeletionHeaders",
    "CreateGovernanceDeletionOperation",
    "CreateGovernanceDeletionParameters",
    "CreateGovernanceDeletionRequestBody",
    "CreateGovernanceDeletionResponses",
    "CreateGovernanceDeletionSuccessResponse",
    "CreateGovernanceDeletionSuccessResponses",
    "CreateGovernanceExportErrorResponses",
    "CreateGovernanceExportHeaders",
    "CreateGovernanceExportOperation",
    "CreateGovernanceExportParameters",
    "CreateGovernanceExportRequestBody",
    "CreateGovernanceExportResponses",
    "CreateGovernanceExportSuccessResponse",
    "CreateGovernanceExportSuccessResponses",
    "CreateMarkingCheckErrorResponses",
    "CreateMarkingCheckHeaders",
    "CreateMarkingCheckOperation",
    "CreateMarkingCheckParameters",
    "CreateMarkingCheckRequestBody",
    "CreateMarkingCheckResponses",
    "CreateMarkingCheckSuccessResponse",
    "CreateMarkingCheckSuccessResponses",
    "CreatePublicCheckErrorResponses",
    "CreatePublicCheckHeaders",
    "CreatePublicCheckOperation",
    "CreatePublicCheckParameters",
    "CreatePublicCheckRequestBody",
    "CreatePublicCheckResponses",
    "CreatePublicCheckSuccessResponse",
    "CreatePublicCheckSuccessResponses",
    "CreateReportRequest",
    "CreateShareRequest",
    "CreateShareResponse",
    "CreateUploadErrorResponses",
    "CreateUploadHeaders",
    "CreateUploadOperation",
    "CreateUploadParameters",
    "CreateUploadRequest",
    "CreateUploadRequestBody",
    "CreateUploadResponse",
    "CreateUploadResponses",
    "CreateUploadSuccessResponse",
    "CreateUploadSuccessResponses",
    "CreateVerificationBatchErrorResponses",
    "CreateVerificationBatchHeaders",
    "CreateVerificationBatchOperation",
    "CreateVerificationBatchParameters",
    "CreateVerificationBatchRequestBody",
    "CreateVerificationBatchResponses",
    "CreateVerificationBatchSuccessResponse",
    "CreateVerificationBatchSuccessResponses",
    "CreateVerificationErrorResponses",
    "CreateVerificationHeaders",
    "CreateVerificationOperation",
    "CreateVerificationParameters",
    "CreateVerificationReportErrorResponses",
    "CreateVerificationReportHeaders",
    "CreateVerificationReportOperation",
    "CreateVerificationReportParameters",
    "CreateVerificationReportRequestBody",
    "CreateVerificationReportResponses",
    "CreateVerificationReportSuccessResponse",
    "CreateVerificationReportSuccessResponses",
    "CreateVerificationRequest",
    "CreateVerificationRequestBody",
    "CreateVerificationResponses",
    "CreateVerificationShareErrorResponses",
    "CreateVerificationShareHeaders",
    "CreateVerificationShareOperation",
    "CreateVerificationShareParameters",
    "CreateVerificationShareRequestBody",
    "CreateVerificationShareResponses",
    "CreateVerificationShareSuccessResponse",
    "CreateVerificationShareSuccessResponses",
    "CreateVerificationSuccessResponse",
    "CreateVerificationSuccessResponses",
    "CreateWebhookEndpointErrorResponses",
    "CreateWebhookEndpointHeaders",
    "CreateWebhookEndpointOperation",
    "CreateWebhookEndpointParameters",
    "CreateWebhookEndpointRequest",
    "CreateWebhookEndpointRequestBody",
    "CreateWebhookEndpointResponses",
    "CreateWebhookEndpointSuccessResponse",
    "CreateWebhookEndpointSuccessResponses",
    "CreateWorkflowTemplateErrorResponses",
    "CreateWorkflowTemplateHeaders",
    "CreateWorkflowTemplateOperation",
    "CreateWorkflowTemplateParameters",
    "CreateWorkflowTemplateRequestBody",
    "CreateWorkflowTemplateResponses",
    "CreateWorkflowTemplateSuccessResponse",
    "CreateWorkflowTemplateSuccessResponses",
    "CreatorConsentRequest",
    "CreatorDisclosurePolicyRequest",
    "CreatorDisclosurePolicyResponse",
    "CreatorDisclosureResponse",
    "CreatorIdentityCreateRequest",
    "CreatorIdentityListResponse",
    "CreatorIdentityResponse",
    "CustomerEventCatalogResponse",
    "CustomerEventCatalogVersion",
    "CustomerEventDescriptorResponse",
    "CustomerEventType",
    "DbHealthResponse",
    "DeclaredCredentialsStatus",
    "DeclaredOrigin",
    "DeleteWebhookEndpointErrorResponses",
    "DeleteWebhookEndpointHeaders",
    "DeleteWebhookEndpointOperation",
    "DeleteWebhookEndpointParameters",
    "DeleteWebhookEndpointRequestBody",
    "DeleteWebhookEndpointResponses",
    "DeleteWebhookEndpointSuccessResponse",
    "DeleteWebhookEndpointSuccessResponses",
    "DeleteWorkflowTemplateErrorResponses",
    "DeleteWorkflowTemplateHeaders",
    "DeleteWorkflowTemplateOperation",
    "DeleteWorkflowTemplateParameters",
    "DeleteWorkflowTemplateRequestBody",
    "DeleteWorkflowTemplateResponses",
    "DeleteWorkflowTemplateSuccessResponse",
    "DeleteWorkflowTemplateSuccessResponses",
    "DeletionPageResponse",
    "DeletionRequestBody",
    "DeletionResponse",
    "DeveloperOnboardingResponse",
    "DigitalSourceType",
    "DisableWebhookEndpointErrorResponses",
    "DisableWebhookEndpointHeaders",
    "DisableWebhookEndpointOperation",
    "DisableWebhookEndpointParameters",
    "DisableWebhookEndpointRequestBody",
    "DisableWebhookEndpointResponses",
    "DisableWebhookEndpointSuccessResponse",
    "DisableWebhookEndpointSuccessResponses",
    "DiscloseCreatorIdentityErrorResponses",
    "DiscloseCreatorIdentityHeaders",
    "DiscloseCreatorIdentityOperation",
    "DiscloseCreatorIdentityParameters",
    "DiscloseCreatorIdentityRequestBody",
    "DiscloseCreatorIdentityResponses",
    "DiscloseCreatorIdentitySuccessResponse",
    "DiscloseCreatorIdentitySuccessResponses",
    "DisclosureActor",
    "DisclosureBadgeSet",
    "DisclosureChainHead",
    "DisclosureEventBlock",
    "DisclosureEventKind",
    "DisclosureEventPage",
    "DisclosureEventReceipt",
    "DisclosureEventRecord",
    "DisclosureEventRequest",
    "DisclosureInstrument",
    "DisclosureJurisdictionPolicy",
    "DisclosurePolicyDocument",
    "DisclosureRule",
    "DisclosureText",
    "DownloadResponse",
    "EmbeddingPlacement",
    "EmbeddingPlan",
    "EnableWebhookEndpointErrorResponses",
    "EnableWebhookEndpointHeaders",
    "EnableWebhookEndpointOperation",
    "EnableWebhookEndpointParameters",
    "EnableWebhookEndpointRequestBody",
    "EnableWebhookEndpointResponses",
    "EnableWebhookEndpointSuccessResponse",
    "EnableWebhookEndpointSuccessResponses",
    "ErrorResponse",
    "ExportItemResponse",
    "ExportMetadataResponse",
    "ExportPageResponse",
    "ExportResponse",
    "ExpressSignResponse",
    "FeedbackBody",
    "FeedbackContextBody",
    "FeedbackResponse",
    "FingerprintAlgorithmResponse",
    "FingerprintBlock",
    "GeneratedAsyncClientMixin",
    "GeneratedClientMixin",
    "GetApiKeyErrorResponses",
    "GetApiKeyHeaders",
    "GetApiKeyOperation",
    "GetApiKeyParameters",
    "GetApiKeyRequestBody",
    "GetApiKeyResponses",
    "GetApiKeyRestrictionsErrorResponses",
    "GetApiKeyRestrictionsHeaders",
    "GetApiKeyRestrictionsOperation",
    "GetApiKeyRestrictionsParameters",
    "GetApiKeyRestrictionsRequestBody",
    "GetApiKeyRestrictionsResponses",
    "GetApiKeyRestrictionsSuccessResponse",
    "GetApiKeyRestrictionsSuccessResponses",
    "GetApiKeyRetentionErrorResponses",
    "GetApiKeyRetentionHeaders",
    "GetApiKeyRetentionOperation",
    "GetApiKeyRetentionParameters",
    "GetApiKeyRetentionRequestBody",
    "GetApiKeyRetentionResponses",
    "GetApiKeyRetentionSuccessResponse",
    "GetApiKeyRetentionSuccessResponses",
    "GetApiKeySigningProfileErrorResponses",
    "GetApiKeySigningProfileHeaders",
    "GetApiKeySigningProfileOperation",
    "GetApiKeySigningProfileParameters",
    "GetApiKeySigningProfileRequestBody",
    "GetApiKeySigningProfileResponses",
    "GetApiKeySigningProfileSuccessResponse",
    "GetApiKeySigningProfileSuccessResponses",
    "GetApiKeySuccessResponse",
    "GetApiKeySuccessResponses",
    "GetAssetDetailErrorResponses",
    "GetAssetDetailHeaders",
    "GetAssetDetailOperation",
    "GetAssetDetailParameters",
    "GetAssetDetailRequestBody",
    "GetAssetDetailResponses",
    "GetAssetDetailSuccessResponse",
    "GetAssetDetailSuccessResponses",
    "GetAssetErrorResponses",
    "GetAssetHeaders",
    "GetAssetOperation",
    "GetAssetParameters",
    "GetAssetRequestBody",
    "GetAssetResponses",
    "GetAssetSuccessResponse",
    "GetAssetSuccessResponses",
    "GetBillingAccountErrorResponses",
    "GetBillingAccountHeaders",
    "GetBillingAccountOperation",
    "GetBillingAccountParameters",
    "GetBillingAccountRequestBody",
    "GetBillingAccountResponses",
    "GetBillingAccountSuccessResponse",
    "GetBillingAccountSuccessResponses",
    "GetBillingPlansErrorResponses",
    "GetBillingPlansHeaders",
    "GetBillingPlansOperation",
    "GetBillingPlansParameters",
    "GetBillingPlansRequestBody",
    "GetBillingPlansResponses",
    "GetBillingPlansSuccessResponse",
    "GetBillingPlansSuccessResponses",
    "GetBillingPricingErrorResponses",
    "GetBillingPricingHeaders",
    "GetBillingPricingOperation",
    "GetBillingPricingParameters",
    "GetBillingPricingRequestBody",
    "GetBillingPricingResponses",
    "GetBillingPricingSuccessResponse",
    "GetBillingPricingSuccessResponses",
    "GetBillingWalletErrorResponses",
    "GetBillingWalletHeaders",
    "GetBillingWalletOperation",
    "GetBillingWalletParameters",
    "GetBillingWalletRequestBody",
    "GetBillingWalletResponses",
    "GetBillingWalletSuccessResponse",
    "GetBillingWalletSuccessResponses",
    "GetCapabilitiesErrorResponses",
    "GetCapabilitiesHeaders",
    "GetCapabilitiesOperation",
    "GetCapabilitiesParameters",
    "GetCapabilitiesRequestBody",
    "GetCapabilitiesResponses",
    "GetCapabilitiesSuccessResponse",
    "GetCapabilitiesSuccessResponses",
    "GetCaptureAdmissionErrorResponses",
    "GetCaptureAdmissionHeaders",
    "GetCaptureAdmissionOperation",
    "GetCaptureAdmissionParameters",
    "GetCaptureAdmissionRequestBody",
    "GetCaptureAdmissionResponses",
    "GetCaptureAdmissionSuccessResponse",
    "GetCaptureAdmissionSuccessResponses",
    "GetCaptureIdentityErrorResponses",
    "GetCaptureIdentityHeaders",
    "GetCaptureIdentityOperation",
    "GetCaptureIdentityParameters",
    "GetCaptureIdentityRequestBody",
    "GetCaptureIdentityResponses",
    "GetCaptureIdentitySuccessResponse",
    "GetCaptureIdentitySuccessResponses",
    "GetConnectCatalogErrorResponses",
    "GetConnectCatalogHeaders",
    "GetConnectCatalogOperation",
    "GetConnectCatalogParameters",
    "GetConnectCatalogRequestBody",
    "GetConnectCatalogResponses",
    "GetConnectCatalogSuccessResponse",
    "GetConnectCatalogSuccessResponses",
    "GetCreatorDisclosurePolicyErrorResponses",
    "GetCreatorDisclosurePolicyHeaders",
    "GetCreatorDisclosurePolicyOperation",
    "GetCreatorDisclosurePolicyParameters",
    "GetCreatorDisclosurePolicyRequestBody",
    "GetCreatorDisclosurePolicyResponses",
    "GetCreatorDisclosurePolicySuccessResponse",
    "GetCreatorDisclosurePolicySuccessResponses",
    "GetCreatorIdentityErrorResponses",
    "GetCreatorIdentityHeaders",
    "GetCreatorIdentityOperation",
    "GetCreatorIdentityParameters",
    "GetCreatorIdentityRequestBody",
    "GetCreatorIdentityResponses",
    "GetCreatorIdentitySuccessResponse",
    "GetCreatorIdentitySuccessResponses",
    "GetCurrentUserErrorResponses",
    "GetCurrentUserHeaders",
    "GetCurrentUserOperation",
    "GetCurrentUserParameters",
    "GetCurrentUserRequestBody",
    "GetCurrentUserResponses",
    "GetCurrentUserSuccessResponse",
    "GetCurrentUserSuccessResponses",
    "GetDatabaseHealthErrorResponses",
    "GetDatabaseHealthHeaders",
    "GetDatabaseHealthOperation",
    "GetDatabaseHealthParameters",
    "GetDatabaseHealthRequestBody",
    "GetDatabaseHealthResponses",
    "GetDatabaseHealthSuccessResponse",
    "GetDatabaseHealthSuccessResponses",
    "GetDeveloperOnboardingErrorResponses",
    "GetDeveloperOnboardingHeaders",
    "GetDeveloperOnboardingOperation",
    "GetDeveloperOnboardingParameters",
    "GetDeveloperOnboardingRequestBody",
    "GetDeveloperOnboardingResponses",
    "GetDeveloperOnboardingSuccessResponse",
    "GetDeveloperOnboardingSuccessResponses",
    "GetDisclosurePoliciesErrorResponses",
    "GetDisclosurePoliciesHeaders",
    "GetDisclosurePoliciesOperation",
    "GetDisclosurePoliciesParameters",
    "GetDisclosurePoliciesRequestBody",
    "GetDisclosurePoliciesResponses",
    "GetDisclosurePoliciesSuccessResponse",
    "GetDisclosurePoliciesSuccessResponses",
    "GetGovernanceDeletionErrorResponses",
    "GetGovernanceDeletionHeaders",
    "GetGovernanceDeletionOperation",
    "GetGovernanceDeletionParameters",
    "GetGovernanceDeletionRequestBody",
    "GetGovernanceDeletionResponses",
    "GetGovernanceDeletionSuccessResponse",
    "GetGovernanceDeletionSuccessResponses",
    "GetGovernanceExportErrorResponses",
    "GetGovernanceExportHeaders",
    "GetGovernanceExportOperation",
    "GetGovernanceExportParameters",
    "GetGovernanceExportRequestBody",
    "GetGovernanceExportResponses",
    "GetGovernanceExportSuccessResponse",
    "GetGovernanceExportSuccessResponses",
    "GetGovernanceReadyzErrorResponses",
    "GetGovernanceReadyzHeaders",
    "GetGovernanceReadyzOperation",
    "GetGovernanceReadyzParameters",
    "GetGovernanceReadyzRequestBody",
    "GetGovernanceReadyzResponses",
    "GetGovernanceReadyzSuccessResponse",
    "GetGovernanceReadyzSuccessResponses",
    "GetHealthzErrorResponses",
    "GetHealthzHeaders",
    "GetHealthzOperation",
    "GetHealthzParameters",
    "GetHealthzRequestBody",
    "GetHealthzResponses",
    "GetHealthzSuccessResponse",
    "GetHealthzSuccessResponses",
    "GetJobErrorResponses",
    "GetJobHeaders",
    "GetJobOperation",
    "GetJobParameters",
    "GetJobRequestBody",
    "GetJobResponses",
    "GetJobSuccessResponse",
    "GetJobSuccessResponses",
    "GetMarkingCheckErrorResponses",
    "GetMarkingCheckHeaders",
    "GetMarkingCheckOperation",
    "GetMarkingCheckParameters",
    "GetMarkingCheckRequestBody",
    "GetMarkingCheckResponses",
    "GetMarkingCheckSuccessResponse",
    "GetMarkingCheckSuccessResponses",
    "GetOverviewErrorResponses",
    "GetOverviewHeaders",
    "GetOverviewOperation",
    "GetOverviewParameters",
    "GetOverviewRequestBody",
    "GetOverviewResponses",
    "GetOverviewSuccessResponse",
    "GetOverviewSuccessResponses",
    "GetPublicCheckErrorResponses",
    "GetPublicCheckHeaders",
    "GetPublicCheckOperation",
    "GetPublicCheckParameters",
    "GetPublicCheckRequestBody",
    "GetPublicCheckResponses",
    "GetPublicCheckSuccessResponse",
    "GetPublicCheckSuccessResponses",
    "GetPublicVerifyPageErrorResponses",
    "GetPublicVerifyPageHeaders",
    "GetPublicVerifyPageLogoErrorResponses",
    "GetPublicVerifyPageLogoHeaders",
    "GetPublicVerifyPageLogoOperation",
    "GetPublicVerifyPageLogoParameters",
    "GetPublicVerifyPageLogoRequestBody",
    "GetPublicVerifyPageLogoResponses",
    "GetPublicVerifyPageLogoSuccessResponse",
    "GetPublicVerifyPageLogoSuccessResponses",
    "GetPublicVerifyPageOperation",
    "GetPublicVerifyPageParameters",
    "GetPublicVerifyPageRequestBody",
    "GetPublicVerifyPageResponses",
    "GetPublicVerifyPageSuccessResponse",
    "GetPublicVerifyPageSuccessResponses",
    "GetReadyzErrorResponses",
    "GetReadyzHeaders",
    "GetReadyzOperation",
    "GetReadyzParameters",
    "GetReadyzRequestBody",
    "GetReadyzResponses",
    "GetReadyzSuccessResponse",
    "GetReadyzSuccessResponses",
    "GetRecipeErrorResponses",
    "GetRecipeHeaders",
    "GetRecipeOperation",
    "GetRecipeParameters",
    "GetRecipeRequestBody",
    "GetRecipeResponses",
    "GetRecipeSuccessResponse",
    "GetRecipeSuccessResponses",
    "GetSharedVerificationErrorResponses",
    "GetSharedVerificationHeaders",
    "GetSharedVerificationOperation",
    "GetSharedVerificationParameters",
    "GetSharedVerificationRequestBody",
    "GetSharedVerificationResponses",
    "GetSharedVerificationSuccessResponse",
    "GetSharedVerificationSuccessResponses",
    "GetSigningReceiptErrorResponses",
    "GetSigningReceiptHeaders",
    "GetSigningReceiptOperation",
    "GetSigningReceiptParameters",
    "GetSigningReceiptRequestBody",
    "GetSigningReceiptResponses",
    "GetSigningReceiptSuccessResponse",
    "GetSigningReceiptSuccessResponses",
    "GetUsageErrorResponses",
    "GetUsageHeaders",
    "GetUsageOperation",
    "GetUsageParameters",
    "GetUsageRequestBody",
    "GetUsageResponses",
    "GetUsageSuccessResponse",
    "GetUsageSuccessResponses",
    "GetVerificationErrorResponses",
    "GetVerificationEvidenceErrorResponses",
    "GetVerificationEvidenceHeaders",
    "GetVerificationEvidenceOperation",
    "GetVerificationEvidenceParameters",
    "GetVerificationEvidenceRequestBody",
    "GetVerificationEvidenceResponses",
    "GetVerificationEvidenceSuccessResponse",
    "GetVerificationEvidenceSuccessResponses",
    "GetVerificationHeaders",
    "GetVerificationHistoryErrorResponses",
    "GetVerificationHistoryHeaders",
    "GetVerificationHistoryOperation",
    "GetVerificationHistoryParameters",
    "GetVerificationHistoryRequestBody",
    "GetVerificationHistoryResponses",
    "GetVerificationHistorySuccessResponse",
    "GetVerificationHistorySuccessResponses",
    "GetVerificationOperation",
    "GetVerificationParameters",
    "GetVerificationReportErrorResponses",
    "GetVerificationReportHeaders",
    "GetVerificationReportOperation",
    "GetVerificationReportParameters",
    "GetVerificationReportRequestBody",
    "GetVerificationReportResponses",
    "GetVerificationReportSuccessResponse",
    "GetVerificationReportSuccessResponses",
    "GetVerificationRequestBody",
    "GetVerificationResponses",
    "GetVerificationSuccessResponse",
    "GetVerificationSuccessResponses",
    "GetVerifyPageErrorResponses",
    "GetVerifyPageHeaders",
    "GetVerifyPageOperation",
    "GetVerifyPageParameters",
    "GetVerifyPageRequestBody",
    "GetVerifyPageResponses",
    "GetVerifyPageSuccessResponse",
    "GetVerifyPageSuccessResponses",
    "GetWebhookDeliveryErrorResponses",
    "GetWebhookDeliveryHeaders",
    "GetWebhookDeliveryOperation",
    "GetWebhookDeliveryParameters",
    "GetWebhookDeliveryRequestBody",
    "GetWebhookDeliveryResponses",
    "GetWebhookDeliverySuccessResponse",
    "GetWebhookDeliverySuccessResponses",
    "GetWebhookEndpointErrorResponses",
    "GetWebhookEndpointHeaders",
    "GetWebhookEndpointOperation",
    "GetWebhookEndpointParameters",
    "GetWebhookEndpointRequestBody",
    "GetWebhookEndpointResponses",
    "GetWebhookEndpointSuccessResponse",
    "GetWebhookEndpointSuccessResponses",
    "GetWebhookEventCatalogErrorResponses",
    "GetWebhookEventCatalogHeaders",
    "GetWebhookEventCatalogOperation",
    "GetWebhookEventCatalogParameters",
    "GetWebhookEventCatalogRequestBody",
    "GetWebhookEventCatalogResponses",
    "GetWebhookEventCatalogSuccessResponse",
    "GetWebhookEventCatalogSuccessResponses",
    "GetWorkflowTemplateErrorResponses",
    "GetWorkflowTemplateHeaders",
    "GetWorkflowTemplateOperation",
    "GetWorkflowTemplateParameters",
    "GetWorkflowTemplateRequestBody",
    "GetWorkflowTemplateResponses",
    "GetWorkflowTemplateSuccessResponse",
    "GetWorkflowTemplateSuccessResponses",
    "GovernanceErrorResponse",
    "GovernanceReadinessResponse",
    "HardBindingExclusionTarget",
    "HardBindingPlan",
    "HealthResponse",
    "HistoryMediaType",
    "HttpErrorResponse",
    "HTTPValidationError",
    "IdentityCredentialKind",
    "IdentityCredentialListResponse",
    "IdentityCredentialResponse",
    "IdentityCredentialStatus",
    "ImageProfileListResponse",
    "ImageProfileResponse",
    "IssuedApiKeyResponse",
    "IssuedWebhookEndpointResponse",
    "JobHistoryPageResponse",
    "JobHistoryResponse",
    "JobKind",
    "JobProgressResponse",
    "JobResponse",
    "JobResultResponse",
    "JobState",
    "JobStepResponse",
    "JobStepState",
    "LegacyReceiptValidationResponse",
    "LegacySigningReceiptEvidenceResponse",
    "LegalHoldResponse",
    "LimitsCostGuidanceResponse",
    "ListApiKeyScopesErrorResponses",
    "ListApiKeyScopesHeaders",
    "ListApiKeyScopesOperation",
    "ListApiKeyScopesParameters",
    "ListApiKeyScopesRequestBody",
    "ListApiKeyScopesResponses",
    "ListApiKeyScopesSuccessResponse",
    "ListApiKeyScopesSuccessResponses",
    "ListApiKeysErrorResponses",
    "ListApiKeysHeaders",
    "ListApiKeysOperation",
    "ListApiKeysParameters",
    "ListApiKeysRequestBody",
    "ListApiKeysResponses",
    "ListApiKeysSuccessResponse",
    "ListApiKeysSuccessResponses",
    "ListApiRequestLogsErrorResponses",
    "ListApiRequestLogsHeaders",
    "ListApiRequestLogsOperation",
    "ListApiRequestLogsParameters",
    "ListApiRequestLogsRequestBody",
    "ListApiRequestLogsResponses",
    "ListApiRequestLogsSuccessResponse",
    "ListApiRequestLogsSuccessResponses",
    "ListAssetsErrorResponses",
    "ListAssetsHeaders",
    "ListAssetsOperation",
    "ListAssetsParameters",
    "ListAssetsRequestBody",
    "ListAssetsResponses",
    "ListAssetsSuccessResponse",
    "ListAssetsSuccessResponses",
    "ListBillingChargesErrorResponses",
    "ListBillingChargesHeaders",
    "ListBillingChargesOperation",
    "ListBillingChargesParameters",
    "ListBillingChargesRequestBody",
    "ListBillingChargesResponses",
    "ListBillingChargesSuccessResponse",
    "ListBillingChargesSuccessResponses",
    "ListBillingInvoicesErrorResponses",
    "ListBillingInvoicesHeaders",
    "ListBillingInvoicesOperation",
    "ListBillingInvoicesParameters",
    "ListBillingInvoicesRequestBody",
    "ListBillingInvoicesResponses",
    "ListBillingInvoicesSuccessResponse",
    "ListBillingInvoicesSuccessResponses",
    "ListCaptureAdmissionsErrorResponses",
    "ListCaptureAdmissionsHeaders",
    "ListCaptureAdmissionsOperation",
    "ListCaptureAdmissionsParameters",
    "ListCaptureAdmissionsRequestBody",
    "ListCaptureAdmissionsResponses",
    "ListCaptureAdmissionsSuccessResponse",
    "ListCaptureAdmissionsSuccessResponses",
    "ListCaptureIdentitiesErrorResponses",
    "ListCaptureIdentitiesHeaders",
    "ListCaptureIdentitiesOperation",
    "ListCaptureIdentitiesParameters",
    "ListCaptureIdentitiesRequestBody",
    "ListCaptureIdentitiesResponses",
    "ListCaptureIdentitiesSuccessResponse",
    "ListCaptureIdentitiesSuccessResponses",
    "ListCreatorIdentitiesErrorResponses",
    "ListCreatorIdentitiesHeaders",
    "ListCreatorIdentitiesOperation",
    "ListCreatorIdentitiesParameters",
    "ListCreatorIdentitiesRequestBody",
    "ListCreatorIdentitiesResponses",
    "ListCreatorIdentitiesSuccessResponse",
    "ListCreatorIdentitiesSuccessResponses",
    "ListDisclosureEventsErrorResponses",
    "ListDisclosureEventsHeaders",
    "ListDisclosureEventsOperation",
    "ListDisclosureEventsParameters",
    "ListDisclosureEventsRequestBody",
    "ListDisclosureEventsResponses",
    "ListDisclosureEventsSuccessResponse",
    "ListDisclosureEventsSuccessResponses",
    "ListGovernanceDeletionsErrorResponses",
    "ListGovernanceDeletionsHeaders",
    "ListGovernanceDeletionsOperation",
    "ListGovernanceDeletionsParameters",
    "ListGovernanceDeletionsRequestBody",
    "ListGovernanceDeletionsResponses",
    "ListGovernanceDeletionsSuccessResponse",
    "ListGovernanceDeletionsSuccessResponses",
    "ListGovernanceExportsErrorResponses",
    "ListGovernanceExportsHeaders",
    "ListGovernanceExportsOperation",
    "ListGovernanceExportsParameters",
    "ListGovernanceExportsRequestBody",
    "ListGovernanceExportsResponses",
    "ListGovernanceExportsSuccessResponse",
    "ListGovernanceExportsSuccessResponses",
    "ListGovernanceLegalHoldsErrorResponses",
    "ListGovernanceLegalHoldsHeaders",
    "ListGovernanceLegalHoldsOperation",
    "ListGovernanceLegalHoldsParameters",
    "ListGovernanceLegalHoldsRequestBody",
    "ListGovernanceLegalHoldsResponses",
    "ListGovernanceLegalHoldsSuccessResponse",
    "ListGovernanceLegalHoldsSuccessResponses",
    "ListIdentityCredentialsErrorResponses",
    "ListIdentityCredentialsHeaders",
    "ListIdentityCredentialsOperation",
    "ListIdentityCredentialsParameters",
    "ListIdentityCredentialsRequestBody",
    "ListIdentityCredentialsResponses",
    "ListIdentityCredentialsSuccessResponse",
    "ListIdentityCredentialsSuccessResponses",
    "ListImageProfilesErrorResponses",
    "ListImageProfilesHeaders",
    "ListImageProfilesOperation",
    "ListImageProfilesParameters",
    "ListImageProfilesRequestBody",
    "ListImageProfilesResponses",
    "ListImageProfilesSuccessResponse",
    "ListImageProfilesSuccessResponses",
    "ListJobsErrorResponses",
    "ListJobsHeaders",
    "ListJobsOperation",
    "ListJobsParameters",
    "ListJobsRequestBody",
    "ListJobsResponses",
    "ListJobsSuccessResponse",
    "ListJobsSuccessResponses",
    "ListReceiptsErrorResponses",
    "ListReceiptsHeaders",
    "ListReceiptsOperation",
    "ListReceiptsParameters",
    "ListReceiptsRequestBody",
    "ListReceiptsResponses",
    "ListReceiptsSuccessResponse",
    "ListReceiptsSuccessResponses",
    "ListRecipesErrorResponses",
    "ListRecipesHeaders",
    "ListRecipesOperation",
    "ListRecipesParameters",
    "ListRecipesRequestBody",
    "ListRecipesResponses",
    "ListRecipesSuccessResponse",
    "ListRecipesSuccessResponses",
    "ListVerificationsErrorResponses",
    "ListVerificationSharesErrorResponses",
    "ListVerificationSharesHeaders",
    "ListVerificationSharesOperation",
    "ListVerificationSharesParameters",
    "ListVerificationSharesRequestBody",
    "ListVerificationSharesResponses",
    "ListVerificationSharesSuccessResponse",
    "ListVerificationSharesSuccessResponses",
    "ListVerificationsHeaders",
    "ListVerificationsOperation",
    "ListVerificationsParameters",
    "ListVerificationsRequestBody",
    "ListVerificationsResponses",
    "ListVerificationsSuccessResponse",
    "ListVerificationsSuccessResponses",
    "ListWebhookDeliveriesErrorResponses",
    "ListWebhookDeliveriesHeaders",
    "ListWebhookDeliveriesOperation",
    "ListWebhookDeliveriesParameters",
    "ListWebhookDeliveriesRequestBody",
    "ListWebhookDeliveriesResponses",
    "ListWebhookDeliveriesSuccessResponse",
    "ListWebhookDeliveriesSuccessResponses",
    "ListWebhookDeliveryAttemptsErrorResponses",
    "ListWebhookDeliveryAttemptsHeaders",
    "ListWebhookDeliveryAttemptsOperation",
    "ListWebhookDeliveryAttemptsParameters",
    "ListWebhookDeliveryAttemptsRequestBody",
    "ListWebhookDeliveryAttemptsResponses",
    "ListWebhookDeliveryAttemptsSuccessResponse",
    "ListWebhookDeliveryAttemptsSuccessResponses",
    "ListWebhookEndpointsErrorResponses",
    "ListWebhookEndpointsHeaders",
    "ListWebhookEndpointsOperation",
    "ListWebhookEndpointsParameters",
    "ListWebhookEndpointsRequestBody",
    "ListWebhookEndpointsResponses",
    "ListWebhookEndpointsSuccessResponse",
    "ListWebhookEndpointsSuccessResponses",
    "ListWorkflowTemplatesErrorResponses",
    "ListWorkflowTemplatesHeaders",
    "ListWorkflowTemplatesOperation",
    "ListWorkflowTemplatesParameters",
    "ListWorkflowTemplatesRequestBody",
    "ListWorkflowTemplatesResponses",
    "ListWorkflowTemplatesSuccessResponse",
    "ListWorkflowTemplatesSuccessResponses",
    "MadeWith",
    "MadeWithAnswer",
    "MadeWithMethod",
    "ManifestContainer",
    "ManifestStoreState",
    "MarkingCheckItemRequest",
    "MarkingCheckItemResult",
    "MarkingCheckRequest",
    "MarkingCheckResponse",
    "MarkingCheckSummary",
    "MarkingRequirement",
    "MarkingRequirementResult",
    "McpClientResponse",
    "McpFeatureGroupResponse",
    "MediaAdapterPin",
    "MediaCapabilityResponse",
    "MeResponse",
    "MetadataFact",
    "MetadataKind",
    "MeterQuotaResponse",
    "MultipartPartRequest",
    "NormalizedAudioFacts",
    "NormalizedInspectionFacts",
    "NormalizedMediaFacts",
    "NormalizedVideoFacts",
    "OnboardingApiKeysResponse",
    "OpaqueManifestStoreFacts",
    "OverviewActivityBucketResponse",
    "OverviewAttentionResponse",
    "OverviewComparisonResponse",
    "OverviewFreshnessResponse",
    "OverviewGovernanceResponse",
    "OverviewHealthResponse",
    "OverviewJobMetricsResponse",
    "OverviewQuotaMeterResponse",
    "OverviewQuotaResponse",
    "OverviewResponse",
    "OverviewUnavailableResponse",
    "OverviewWebhookResponse",
    "PortalIntentRequest",
    "PresignedPartResponse",
    "PresignedRequestResponse",
    "PreviewResponse",
    "PricingLineResponse",
    "PricingQuoteRequest",
    "PricingQuoteResponse",
    "PricingResponse",
    "ProcessingChargeResponse",
    "ProcessingChargesResponse",
    "ProcessingLimitsResponse",
    "PublicApiOperationModels",
    "PublicationResponse",
    "PublicCaptureAdmissionReason",
    "PublicCheckPage",
    "PublicCheckResponse",
    "PublicContentCredentials",
    "PublicRecipeCapability",
    "PublicVerifyPageResponse",
    "PutVerifyPageErrorResponses",
    "PutVerifyPageHeaders",
    "PutVerifyPageOperation",
    "PutVerifyPageParameters",
    "PutVerifyPageRequestBody",
    "PutVerifyPageResponses",
    "PutVerifyPageSuccessResponse",
    "PutVerifyPageSuccessResponses",
    "QueryGovernanceAuditErrorResponses",
    "QueryGovernanceAuditHeaders",
    "QueryGovernanceAuditOperation",
    "QueryGovernanceAuditParameters",
    "QueryGovernanceAuditRequestBody",
    "QueryGovernanceAuditResponses",
    "QueryGovernanceAuditSuccessResponse",
    "QueryGovernanceAuditSuccessResponses",
    "ReadinessResponse",
    "ReasonCode",
    "ReceiptAiDeclarationResponse",
    "ReceiptBindingSetResponse",
    "ReceiptHistoryPageResponse",
    "ReceiptHistoryResponse",
    "ReceiptManifestResponse",
    "ReceiptOutputResponse",
    "ReceiptPriorProvenanceResponse",
    "ReceiptPriorProvenanceWarningResponse",
    "ReceiptProductResponse",
    "ReceiptRecoveryResponse",
    "ReceiptResponse",
    "ReceiptSigningResponse",
    "ReceiptValidationResponse",
    "ReceiveClerkWebhookErrorResponses",
    "ReceiveClerkWebhookHeaders",
    "ReceiveClerkWebhookOperation",
    "ReceiveClerkWebhookParameters",
    "ReceiveClerkWebhookRequestBody",
    "ReceiveClerkWebhookResponses",
    "ReceiveClerkWebhookSuccessResponse",
    "ReceiveClerkWebhookSuccessResponses",
    "ReceiveStripeWebhookErrorResponses",
    "ReceiveStripeWebhookHeaders",
    "ReceiveStripeWebhookOperation",
    "ReceiveStripeWebhookParameters",
    "ReceiveStripeWebhookRequestBody",
    "ReceiveStripeWebhookResponses",
    "ReceiveStripeWebhookSuccessResponse",
    "ReceiveStripeWebhookSuccessResponses",
    "RecipeCatalogKind",
    "RecipeCatalogResponse",
    "RecipeListResponse",
    "RecipeResponse",
    "RecipeUnavailableReason",
    "RecoveredReceiptSigningResponse",
    "RecoveredSigningReceiptEvidenceResponse",
    "RedeemAssetPreviewErrorResponses",
    "RedeemAssetPreviewHeaders",
    "RedeemAssetPreviewOperation",
    "RedeemAssetPreviewParameters",
    "RedeemAssetPreviewRequestBody",
    "RedeemAssetPreviewResponses",
    "RedeemAssetPreviewSuccessResponse",
    "RedeemAssetPreviewSuccessResponses",
    "ReleaseHistorySnapshotErrorResponses",
    "ReleaseHistorySnapshotHeaders",
    "ReleaseHistorySnapshotOperation",
    "ReleaseHistorySnapshotParameters",
    "ReleaseHistorySnapshotRequestBody",
    "ReleaseHistorySnapshotResponses",
    "ReleaseHistorySnapshotSuccessResponse",
    "ReleaseHistorySnapshotSuccessResponses",
    "ReplaceWorkflowTemplateErrorResponses",
    "ReplaceWorkflowTemplateHeaders",
    "ReplaceWorkflowTemplateOperation",
    "ReplaceWorkflowTemplateParameters",
    "ReplaceWorkflowTemplateRequestBody",
    "ReplaceWorkflowTemplateResponses",
    "ReplaceWorkflowTemplateSuccessResponse",
    "ReplaceWorkflowTemplateSuccessResponses",
    "ReplayWebhookDeliveryErrorResponses",
    "ReplayWebhookDeliveryHeaders",
    "ReplayWebhookDeliveryOperation",
    "ReplayWebhookDeliveryParameters",
    "ReplayWebhookDeliveryRequestBody",
    "ReplayWebhookDeliveryResponse",
    "ReplayWebhookDeliveryResponses",
    "ReplayWebhookDeliverySuccessResponse",
    "ReplayWebhookDeliverySuccessResponses",
    "ReplayWebhookEventErrorResponses",
    "ReplayWebhookEventHeaders",
    "ReplayWebhookEventOperation",
    "ReplayWebhookEventParameters",
    "ReplayWebhookEventRequestBody",
    "ReplayWebhookEventResponses",
    "ReplayWebhookEventSuccessResponse",
    "ReplayWebhookEventSuccessResponses",
    "ReportContentResponse",
    "ReportFormat",
    "ReportResponse",
    "RequestObservationResponse",
    "RequestObservationState",
    "RequirementLevel",
    "ReviewedRecipeAvailabilityResponse",
    "RevokeApiKeyErrorResponses",
    "RevokeApiKeyHeaders",
    "RevokeApiKeyOperation",
    "RevokeApiKeyParameters",
    "RevokeApiKeyRequestBody",
    "RevokeApiKeyResponses",
    "RevokeApiKeySuccessResponse",
    "RevokeApiKeySuccessResponses",
    "RevokeCaptureIdentityErrorResponses",
    "RevokeCaptureIdentityHeaders",
    "RevokeCaptureIdentityOperation",
    "RevokeCaptureIdentityParameters",
    "RevokeCaptureIdentityRequestBody",
    "RevokeCaptureIdentityResponses",
    "RevokeCaptureIdentitySuccessResponse",
    "RevokeCaptureIdentitySuccessResponses",
    "RotateApiKeyErrorResponses",
    "RotateApiKeyHeaders",
    "RotateApiKeyOperation",
    "RotateApiKeyParameters",
    "RotateApiKeyRequestBody",
    "RotateApiKeyResponses",
    "RotateApiKeySuccessResponse",
    "RotateApiKeySuccessResponses",
    "RotatedWebhookSecretResponse",
    "RotateWebhookEndpointSecretErrorResponses",
    "RotateWebhookEndpointSecretHeaders",
    "RotateWebhookEndpointSecretOperation",
    "RotateWebhookEndpointSecretParameters",
    "RotateWebhookEndpointSecretRequestBody",
    "RotateWebhookEndpointSecretResponses",
    "RotateWebhookEndpointSecretSuccessResponse",
    "RotateWebhookEndpointSecretSuccessResponses",
    "RotateWebhookSecretRequest",
    "SafetyStatementResponse",
    "SecretNotReplayableResponse",
    "SendWebhookTestEventErrorResponses",
    "SendWebhookTestEventHeaders",
    "SendWebhookTestEventOperation",
    "SendWebhookTestEventParameters",
    "SendWebhookTestEventRequestBody",
    "SendWebhookTestEventResponses",
    "SendWebhookTestEventSuccessResponse",
    "SendWebhookTestEventSuccessResponses",
    "SetApiKeyRestrictionsErrorResponses",
    "SetApiKeyRestrictionsHeaders",
    "SetApiKeyRestrictionsOperation",
    "SetApiKeyRestrictionsParameters",
    "SetApiKeyRestrictionsRequestBody",
    "SetApiKeyRestrictionsResponses",
    "SetApiKeyRestrictionsSuccessResponse",
    "SetApiKeyRestrictionsSuccessResponses",
    "SetApiKeyRetentionErrorResponses",
    "SetApiKeyRetentionHeaders",
    "SetApiKeyRetentionOperation",
    "SetApiKeyRetentionParameters",
    "SetApiKeyRetentionRequestBody",
    "SetApiKeyRetentionResponses",
    "SetApiKeyRetentionSuccessResponse",
    "SetApiKeyRetentionSuccessResponses",
    "SetApiKeySigningProfileErrorResponses",
    "SetApiKeySigningProfileHeaders",
    "SetApiKeySigningProfileOperation",
    "SetApiKeySigningProfileParameters",
    "SetApiKeySigningProfileRequestBody",
    "SetApiKeySigningProfileResponses",
    "SetApiKeySigningProfileSuccessResponse",
    "SetApiKeySigningProfileSuccessResponses",
    "SetBillingWalletSettingsErrorResponses",
    "SetBillingWalletSettingsHeaders",
    "SetBillingWalletSettingsOperation",
    "SetBillingWalletSettingsParameters",
    "SetBillingWalletSettingsRequestBody",
    "SetBillingWalletSettingsResponses",
    "SetBillingWalletSettingsSuccessResponse",
    "SetBillingWalletSettingsSuccessResponses",
    "SharedVerificationResponse",
    "SidecarManifestResponse",
    "SidecarReceiptBindingSetResponse",
    "SidecarReceiptManifestResponse",
    "SidecarSigningReceiptEvidenceResponse",
    "SignBatchItemResponse",
    "SignBatchRequest",
    "SignBatchResponse",
    "SignBlock",
    "SignIdentityRequest",
    "SigningReceiptEvidenceResponse",
    "SignRequest",
    "StatusClass",
    "StripeInboxResponse",
    "SubmitFeedbackErrorResponses",
    "SubmitFeedbackHeaders",
    "SubmitFeedbackOperation",
    "SubmitFeedbackParameters",
    "SubmitFeedbackRequestBody",
    "SubmitFeedbackResponses",
    "SubmitFeedbackSuccessResponse",
    "SubmitFeedbackSuccessResponses",
    "SummarizeApiRequestLogsErrorResponses",
    "SummarizeApiRequestLogsHeaders",
    "SummarizeApiRequestLogsOperation",
    "SummarizeApiRequestLogsParameters",
    "SummarizeApiRequestLogsRequestBody",
    "SummarizeApiRequestLogsResponses",
    "SummarizeApiRequestLogsSuccessResponse",
    "SummarizeApiRequestLogsSuccessResponses",
    "SummaryWindow",
    "UpdateCreatorDisclosurePolicyErrorResponses",
    "UpdateCreatorDisclosurePolicyHeaders",
    "UpdateCreatorDisclosurePolicyOperation",
    "UpdateCreatorDisclosurePolicyParameters",
    "UpdateCreatorDisclosurePolicyRequestBody",
    "UpdateCreatorDisclosurePolicyResponses",
    "UpdateCreatorDisclosurePolicySuccessResponse",
    "UpdateCreatorDisclosurePolicySuccessResponses",
    "UpdateWebhookEndpointAutoDisableRequest",
    "UpdateWebhookEndpointCommand",
    "UpdateWebhookEndpointConcurrencyRequest",
    "UpdateWebhookEndpointErrorResponses",
    "UpdateWebhookEndpointEventsRequest",
    "UpdateWebhookEndpointHeaders",
    "UpdateWebhookEndpointOperation",
    "UpdateWebhookEndpointParameters",
    "UpdateWebhookEndpointRateRequest",
    "UpdateWebhookEndpointRequest",
    "UpdateWebhookEndpointRequestBody",
    "UpdateWebhookEndpointResponses",
    "UpdateWebhookEndpointSuccessResponse",
    "UpdateWebhookEndpointSuccessResponses",
    "UpdateWebhookEndpointUrlRequest",
    "UploadBlock",
    "UploadLimitsResponse",
    "UploadMode",
    "UploadStatus",
    "UsageItemResponse",
    "UsageResponse",
    "ValidationError",
    "ValidationPath",
    "VerificationBatchItemResponse",
    "VerificationBatchRequest",
    "VerificationBatchResponse",
    "VerificationEvidenceResponse",
    "VerificationHistoryPageResponse",
    "VerificationHistoryResponse",
    "VerificationOverall",
    "VerificationResponse",
    "VerificationShareMetadataResponse",
    "VerificationSharePageResponse",
    "VerificationSubjectType",
    "VerifyBlock",
    "VerifyPageCheckUsage",
    "VerifyPageColours",
    "VerifyPageResponse",
    "VerifyPageUpdateRequest",
    "VerifyState",
    "VideoTrackFacts",
    "WalletAutoRecharge",
    "WalletAutoRechargeRequest",
    "WalletResponse",
    "WalletSettingsRequest",
    "WalletTransactionResponse",
    "WatermarkAlgorithmResponse",
    "WatermarkBlock",
    "WatermarkStrengthLevelsResponse",
    "WebhookAck",
    "WebhookAttemptPageResponse",
    "WebhookAttemptResponse",
    "WebhookBlock",
    "WebhookDeliveryPageResponse",
    "WebhookDeliveryResponse",
    "WebhookDeliveryTerminalReason",
    "WebhookDisabledReason",
    "WebhookEndpointPageResponse",
    "WebhookEndpointResponse",
    "WebhookReplayResponse",
    "WebhookSecretLifecycleResponse",
    "WebhookSecretLifecycleStatus",
    "WebhookTestEventResponse",
    "WithdrawCreatorIdentityErrorResponses",
    "WithdrawCreatorIdentityHeaders",
    "WithdrawCreatorIdentityOperation",
    "WithdrawCreatorIdentityParameters",
    "WithdrawCreatorIdentityRequestBody",
    "WithdrawCreatorIdentityResponses",
    "WithdrawCreatorIdentitySuccessResponse",
    "WithdrawCreatorIdentitySuccessResponses",
    "WorkflowSignRequestFields",
    "WorkflowTemplateListResponse",
    "WorkflowTemplateReplaceRequest",
    "WorkflowTemplateRequest",
    "WorkflowTemplateResponse",
    "WorkspaceGovernanceResponse",
]
