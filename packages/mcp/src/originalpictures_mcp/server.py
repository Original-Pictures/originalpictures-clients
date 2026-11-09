"""Reviewed FastMCP tools and resources over the generated public SDK.

The tools are registered by :func:`register_tools`, which is transport-agnostic: the
packaged server (:func:`create_server`, STDIO or a single-tenant loopback HTTP server)
and the API's hosted ``/mcp`` endpoint (``op_api.mcp``) register the same reviewed
definitions. Only what differs between them is passed in: the client factory (the SDK
over HTTPS here, the same SDK over an in-process transport there), the bounds, and how
a tool is authorized.
"""

from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable
from contextlib import AbstractAsyncContextManager
from dataclasses import dataclass
from importlib import metadata
from pathlib import Path
from typing import Annotated, Any, Final, Literal, Protocol

import anyio
from fastmcp import FastMCP
from fastmcp.exceptions import ToolError
from fastmcp.server.auth import require_scopes as _require_scopes
from fastmcp.server.auth.providers.jwt import StaticTokenVerifier
from originalpictures.errors import ResponseTooLargeError
from pydantic import BaseModel, ConfigDict, Field

from originalpictures_mcp.bounds import bounded_output, checked_deadline, safe_error
from originalpictures_mcp.config import Settings
from originalpictures_mcp.sdk import ApiClient, sdk_client

type ClientFactory = Callable[[], AbstractAsyncContextManager[ApiClient]]
type Identifier = Annotated[
    str,
    Field(
        min_length=1,
        max_length=128,
        pattern=r"^[A-Za-z0-9][A-Za-z0-9._:-]*$",
        description="Exact opaque public identifier; never a path or URL.",
    ),
]
type Cursor = Annotated[
    str,
    Field(min_length=1, max_length=2048, description="Opaque cursor returned by the prior page."),
]
type Deadline = Annotated[
    float | None,
    Field(default=None, gt=0, le=120, description="Per-call wall-clock deadline in seconds."),
]
type IdempotencyKey = Annotated[
    str,
    Field(
        min_length=1,
        max_length=255,
        pattern=r"^[\x21-\x7e]+$",
        description="Printable ASCII idempotency key; safe to retry with the same request.",
    ),
]


type VerifyPageSlug = Annotated[
    str,
    Field(
        pattern=r"^[a-z0-9](?:[a-z0-9-]{1,46})[a-z0-9]$",
        description="The verify page's slug, as in originalpictures.com/verify/{slug}/.",
    ),
]

type MaxBillableOperations = Annotated[
    int | None,
    Field(
        default=None,
        ge=0,
        le=1000,
        description=(
            "Optional spend guard: refuse this call, before anything is sent, if it would "
            "start more billable operations than this."
        ),
    ),
]

#: The public check's upload ceiling; the API refuses a larger file with 413.
MAX_PUBLIC_CHECK_BYTES = 25 * 1024 * 1024
#: The console's text for the combination the C2PA claim plan refuses.
AI_MARK_REQUIRES_SIGN_ONLY = "AI-generated mark needs a sign-only call (C2PA claim plan)"
#: ``_meta`` key carrying a billable tool's machine-readable cost preview.
BILLING_META_KEY: Final = "com.originalpictures/billing"
#: Where a caller reads the rates that price a billable operation.
PRICING_REFERENCE: Final = "GET /v1/billing/pricing (the get_pricing tool)"

#: Directory reviewers (Claude, ChatGPT) want every hint explicit, not defaulted.
#: ``openWorldHint`` is false because every tool reads or writes only the caller's own
#: bounded Original Pictures account.
READ_ONLY_HINTS: Final = {
    "readOnlyHint": True,
    "destructiveHint": False,
    "idempotentHint": True,
    "openWorldHint": False,
}
#: A billable write starts work in the caller's account. It deletes nothing, and the
#: required idempotency key makes a retry return the first result.
BILLABLE_WRITE_HINTS: Final = {
    "readOnlyHint": False,
    "destructiveHint": False,
    "idempotentHint": True,
    "openWorldHint": False,
}


def tool_annotations(title: str, hints: dict[str, bool]) -> dict[str, Any]:
    """The tool's annotations; the title repeats here for clients on the 2025-03-26 spec."""

    return {"title": title, **hints}


def billing_meta(*, operations: str, max_operations: int) -> dict[str, Any]:
    """The machine-readable cost preview a billable tool lists in ``_meta``."""

    return {
        BILLING_META_KEY: {
            "billable": True,
            "operations": operations,
            "max_billable_operations_per_call": max_operations,
            "rates": PRICING_REFERENCE,
            "guard": "max_billable_operations",
        }
    }


def sign_operations(*, watermark: bool, fingerprint: bool) -> int:
    """Billable operations one sign call starts: the signature, plus each opted-in service.

    Each is metered separately; an audio or video watermark or fingerprint is then
    priced per second by the account's rate catalog.
    """

    return 1 + int(watermark) + int(fingerprint)


class ToolPolicy(Protocol):
    """The bounds a transport applies to every tool call (``Settings`` satisfies it)."""

    @property
    def scopes(self) -> frozenset[str]: ...

    @property
    def default_deadline_seconds(self) -> float: ...

    @property
    def max_deadline_seconds(self) -> float: ...

    @property
    def max_output_bytes(self) -> int: ...

    @property
    def max_page_size(self) -> int: ...


@dataclass(frozen=True, slots=True)
class ToolAccess:
    """How a transport authorizes the shared tools.

    ``scoped`` filters and gates each tool on the caller's OAuth-style scopes (HTTP
    transports, where FastMCP sees an access token). ``local_files`` offers the tools
    that read a file on the server's own host, which only a local STDIO server may.
    ``operation_ceiling`` returns the transport's per-request spend ceiling, if any.
    """

    scoped: bool
    local_files: bool
    operation_ceiling: Callable[[], int | None] | None = None


class AiDeclaration(BaseModel):
    """Declares that a generative model produced the file (sent as ``ai_declaration``)."""

    model_config = ConfigDict(extra="forbid")

    digital_source_type: Literal[
        "trainedAlgorithmicMedia", "compositeWithTrainedAlgorithmicMedia", "compositeSynthetic"
    ] = "trainedAlgorithmicMedia"
    software_agent_name: Annotated[str, Field(min_length=1, max_length=128)]
    software_agent_version: Annotated[str | None, Field(min_length=1, max_length=64)] = None


def _public_check_file(file_path: str) -> Path:
    """A local file the public check may read: absolute, regular, not a link, at most 25 MB."""

    path = Path(file_path)
    if not path.is_absolute():
        raise ToolError("file_path must be an absolute path")
    if path.is_symlink() or not path.is_file():
        raise ToolError("file_path must name a regular file")
    if path.stat().st_size > MAX_PUBLIC_CHECK_BYTES:
        raise ToolError("the file is larger than the public check's 25 MB limit")
    return path


class ToolRunner:
    """Runs one tool's SDK call under the allowlist, a deadline and the output bound.

    Every tool goes through it, so a transport that registers its own tools (the hosted
    endpoint's upload tools) gets the same bounds and the same secret-safe errors.
    """

    def __init__(self, policy: ToolPolicy, client_factory: ClientFactory) -> None:
        self._policy = policy
        self._factory = client_factory

    async def run(
        self,
        scope: str | None,
        deadline_seconds: float | None,
        call: Callable[[ApiClient, float], Awaitable[Any]],
    ) -> Any:
        """Run ``call``; ``scope`` ``None`` marks an operation the API serves anonymously."""

        settings = self._policy
        if scope is not None and scope not in settings.scopes:
            raise ToolError("This MCP server is not configured for the required API-key scope")
        deadline = checked_deadline(
            deadline_seconds,
            default=settings.default_deadline_seconds,
            maximum=settings.max_deadline_seconds,
        )
        try:
            # Level-triggered on purpose. The SDK's transport (httpx -> anyio) cancels
            # its own task groups, e.g. the losing happy-eyeballs connect attempts.
            # An edge-triggered asyncio.timeout() delivers exactly one cancel; when it
            # coalesces with such an anyio group cancel, anyio's scope swallows it as
            # its own and the call silently runs past its deadline. anyio.fail_after()
            # re-delivers until the scope is exited, so the deadline always holds.
            with anyio.fail_after(deadline):
                async with self._factory() as client:
                    result = await call(client, deadline)
        except TimeoutError as error:
            raise ToolError("Original Pictures API request exceeded its deadline") from error
        except asyncio.CancelledError:
            raise
        except ResponseTooLargeError as error:
            raise ToolError(
                "Original Pictures API result exceeded the configured output bound"
            ) from error
        except ToolError:
            raise
        except Exception as error:
            raise safe_error(error) from None
        return bounded_output(result, max_bytes=settings.max_output_bytes)

    async def invoke(
        self,
        operation: str,
        scope: str | None,
        *,
        parameters: dict[str, Any] | None = None,
        headers: dict[str, Any] | None = None,
        body: dict[str, Any] | None = None,
        deadline_seconds: float | None = None,
    ) -> Any:
        """Call one generated SDK operation by its method name."""

        kwargs: dict[str, Any] = {
            "parameters": parameters or {},
            "headers": headers or {},
        }
        if body is not None:
            kwargs["body"] = body

        async def call(client: ApiClient, _deadline: float) -> Any:
            method = getattr(client, operation)
            return await method(**kwargs)

        return await self.run(scope, deadline_seconds, call)


def create_server(
    settings: Settings,
    *,
    client_factory: ClientFactory | None = None,
) -> FastMCP:
    """Build the packaged server: one deterministic, default-deny MCP component registry."""

    factory = client_factory or (lambda: sdk_client(settings))
    auth = None
    if settings.remote_token is not None:
        auth = StaticTokenVerifier(
            tokens={
                settings.remote_token: {
                    "client_id": "originalpictures-mcp-client",
                    "scopes": sorted(settings.scopes),
                }
            }
        )

    # Without an explicit version FastMCP reports its own release as serverInfo.version,
    # so a client saw "3.4.6" for this 0.1.0 server.
    mcp = FastMCP(
        name=SERVER_NAME,
        instructions=SERVER_INSTRUCTIONS,
        auth=auth,
        version=metadata.version("originalpictures-mcp"),
    )
    # FastMCP authorization checks rely on HTTP OAuth context. STDIO has no such
    # context, so the mandatory local allowlist in ``invoke`` remains authoritative
    # there. Remote components additionally use FastMCP scope filtering.
    remote = settings.remote_token is not None
    register_tools(
        mcp,
        policy=settings,
        client_factory=factory,
        access=ToolAccess(scoped=remote, local_files=not remote),
    )
    return mcp


SERVER_NAME: Final = "Original Pictures"
SERVER_INSTRUCTIONS: Final = (
    "Use only the reviewed bounded tools and resources. Never request or expose API keys, "
    "media bytes, direct storage locations, infrastructure, signer, database, or worker "
    "access."
)


def register_tools(
    mcp: FastMCP,
    *,
    policy: ToolPolicy,
    client_factory: ClientFactory,
    access: ToolAccess,
) -> None:
    """Register the reviewed tools and resources on ``mcp``.

    ``policy.scopes`` is the local allowlist every call is checked against before the
    SDK is reached; with ``access.scoped`` each component also requires its scope from
    the caller's access token, so a caller lists only what it may call.
    """

    settings = policy

    def component_auth(scope: str) -> Any:
        return _require_scopes(scope) if access.scoped else None

    def check_spend(operations: int, requested: int | None) -> None:
        """Refuse before anything is sent when a call would start more than a ceiling."""

        ceilings = [requested]
        if access.operation_ceiling is not None:
            ceilings.append(access.operation_ceiling())
        bound = min((ceiling for ceiling in ceilings if ceiling is not None), default=None)
        if bound is not None and operations > bound:
            raise ToolError(
                f"this call would start {operations} billable operation(s), above the "
                f"ceiling of {bound}; nothing was sent"
            )

    runner = ToolRunner(policy, client_factory)
    guarded = runner.run
    invoke = runner.invoke

    def page(limit: int, cursor: str | None) -> dict[str, Any]:
        if limit > settings.max_page_size:
            raise ToolError(
                f"limit must not exceed the configured page bound ({settings.max_page_size})"
            )
        result: dict[str, Any] = {"limit": limit}
        if cursor is not None:
            result["cursor"] = cursor
        return result

    @mcp.tool(
        title="Read the API key's identity",
        auth=component_auth("identity:read"),
        annotations=tool_annotations("Read the API key's identity", READ_ONLY_HINTS),
    )
    async def get_current_user(deadline_seconds: Deadline = None) -> Any:
        """Read the provisioned public identity for the configured API credential."""

        return await invoke("get_current_user", "identity:read", deadline_seconds=deadline_seconds)

    @mcp.tool(
        title="List assets",
        auth=component_auth("assets:read"),
        annotations=tool_annotations("List assets", READ_ONLY_HINTS),
    )
    async def list_assets(
        limit: Annotated[int, Field(ge=1, le=100)] = 50,
        cursor: Cursor | None = None,
        kind: Literal["uninspected", "image", "audio", "video"] | None = None,
        status: Literal[
            "pending", "ready", "processing", "signed", "watermarked", "failed", "deleted"
        ]
        | None = None,
        deadline_seconds: Deadline = None,
    ) -> Any:
        """List one bounded, snapshot-consistent page of tenant assets."""

        parameters = page(limit, cursor)
        if kind is not None:
            parameters["kind"] = kind
        if status is not None:
            parameters["status"] = status
        return await invoke(
            "list_assets", "assets:read", parameters=parameters, deadline_seconds=deadline_seconds
        )

    @mcp.tool(
        title="Read an asset",
        auth=component_auth("assets:read"),
        annotations=tool_annotations("Read an asset", READ_ONLY_HINTS),
    )
    async def get_asset(asset_id: Identifier, deadline_seconds: Deadline = None) -> Any:
        """Read status and validated publication metadata for one exact asset."""

        return await invoke(
            "get_asset",
            "assets:read",
            parameters={"asset_id": asset_id},
            deadline_seconds=deadline_seconds,
        )

    @mcp.tool(
        title="List jobs",
        auth=component_auth("jobs:read"),
        annotations=tool_annotations("List jobs", READ_ONLY_HINTS),
    )
    async def list_jobs(
        limit: Annotated[int, Field(ge=1, le=100)] = 50,
        cursor: Cursor | None = None,
        kind: Literal["sign", "watermark", "watermark_then_sign", "capture"] | None = None,
        state: Literal[
            "accepted",
            "queued",
            "running",
            "cancel_requested",
            "completed",
            "canceled",
            "expired",
            "rejected",
            "failed",
        ]
        | None = None,
        deadline_seconds: Deadline = None,
    ) -> Any:
        """List one bounded, snapshot-consistent page of durable jobs."""

        parameters = page(limit, cursor)
        if kind is not None:
            parameters["kind"] = kind
        if state is not None:
            parameters["state"] = state
        return await invoke(
            "list_jobs", "jobs:read", parameters=parameters, deadline_seconds=deadline_seconds
        )

    @mcp.tool(
        title="Read a job",
        auth=component_auth("jobs:read"),
        annotations=tool_annotations("Read a job", READ_ONLY_HINTS),
    )
    async def get_job(job_id: Identifier, deadline_seconds: Deadline = None) -> Any:
        """Read durable state, progress, and bounded evidence for one exact job."""

        return await invoke(
            "get_job",
            "jobs:read",
            parameters={"job_id": job_id},
            deadline_seconds=deadline_seconds,
        )

    @mcp.tool(
        title="List signing receipts",
        auth=component_auth("assets:read"),
        annotations=tool_annotations("List signing receipts", READ_ONLY_HINTS),
    )
    async def list_receipts(
        limit: Annotated[int, Field(ge=1, le=100)] = 50,
        cursor: Cursor | None = None,
        asset_id: Identifier | None = None,
        job_id: Identifier | None = None,
        deadline_seconds: Deadline = None,
    ) -> Any:
        """List one bounded page of privacy-safe publication receipt summaries."""

        parameters = page(limit, cursor)
        if asset_id is not None:
            parameters["asset_id"] = asset_id
        if job_id is not None:
            parameters["job_id"] = job_id
        return await invoke(
            "list_receipts",
            "assets:read",
            parameters=parameters,
            deadline_seconds=deadline_seconds,
        )

    @mcp.tool(
        title="Read a signing receipt",
        auth=component_auth("assets:read"),
        annotations=tool_annotations("Read a signing receipt", READ_ONLY_HINTS),
    )
    async def get_signing_receipt(receipt_id: Identifier, deadline_seconds: Deadline = None) -> Any:
        """Read the immutable privacy-safe receipt for one publication."""

        return await invoke(
            "get_signing_receipt",
            "assets:read",
            parameters={"receipt_id": receipt_id},
            deadline_seconds=deadline_seconds,
        )

    @mcp.tool(
        title="List recipes",
        auth=component_auth("jobs:read"),
        annotations=tool_annotations("List recipes", READ_ONLY_HINTS),
    )
    async def list_recipes(deadline_seconds: Deadline = None) -> Any:
        """List the fixed catalog of approved recipes and supported media formats."""

        return await invoke("list_recipes", "jobs:read", deadline_seconds=deadline_seconds)

    @mcp.tool(
        title="Read a recipe",
        auth=component_auth("recipes:read"),
        annotations=tool_annotations("Read a recipe", READ_ONLY_HINTS),
    )
    async def get_recipe(recipe_id: Identifier, deadline_seconds: Deadline = None) -> Any:
        """Read one exact active recipe version from the immutable catalog."""

        return await invoke(
            "get_recipe",
            "recipes:read",
            parameters={"recipe_id": recipe_id},
            deadline_seconds=deadline_seconds,
        )

    @mcp.tool(
        title="Read usage and caps",
        auth=component_auth("billing:read"),
        annotations=tool_annotations("Read usage and caps", READ_ONLY_HINTS),
    )
    async def get_usage(
        period: Annotated[str | None, Field(default=None, max_length=32)] = None,
        item_limit: Annotated[int, Field(ge=1, le=100)] = 50,
        deadline_seconds: Deadline = None,
    ) -> Any:
        """Read a bounded authoritative usage and hard-cap projection."""

        if item_limit > settings.max_page_size:
            raise ToolError(
                f"item_limit must not exceed the configured page bound ({settings.max_page_size})"
            )
        parameters: dict[str, Any] = {"item_limit": item_limit}
        if period is not None:
            parameters["period"] = period
        return await invoke(
            "get_usage",
            "billing:read",
            parameters=parameters,
            deadline_seconds=deadline_seconds,
        )

    @mcp.tool(
        title="Read the price list",
        auth=component_auth("billing:read"),
        annotations=tool_annotations("Read the price list", READ_ONLY_HINTS),
    )
    async def get_pricing(deadline_seconds: Deadline = None) -> Any:
        """Read the versioned rates that price each billable operation for this account."""

        return await invoke(
            "get_billing_pricing", "billing:read", deadline_seconds=deadline_seconds
        )

    @mcp.tool(
        title="List verifications",
        auth=component_auth("verifications:read"),
        annotations=tool_annotations("List verifications", READ_ONLY_HINTS),
    )
    async def list_verifications(
        limit: Annotated[int, Field(ge=1, le=100)] = 50,
        cursor: Cursor | None = None,
        overall: Literal["valid", "invalid", "indeterminate", "recovered"] | None = None,
        subject_type: Literal[
            "uploaded_object", "stored_object", "public_url", "asset", "manifest", "receipt"
        ]
        | None = None,
        deadline_seconds: Deadline = None,
    ) -> Any:
        """List one bounded page of tenant verification observations."""

        parameters = page(limit, cursor)
        if overall is not None:
            parameters["overall"] = overall
        if subject_type is not None:
            parameters["subject_type"] = subject_type
        return await invoke(
            "list_verifications",
            "verifications:read",
            parameters=parameters,
            deadline_seconds=deadline_seconds,
        )

    @mcp.tool(
        title="Read a verification",
        auth=component_auth("recovery:read"),
        annotations=tool_annotations("Read a verification", READ_ONLY_HINTS),
    )
    async def get_verification(
        verification_id: Identifier, deadline_seconds: Deadline = None
    ) -> Any:
        """Read durable direct-validation and recovery status for one verification."""

        return await invoke(
            "get_verification",
            "recovery:read",
            parameters={"verification_id": verification_id},
            deadline_seconds=deadline_seconds,
        )

    @mcp.tool(
        title="Read a verification's history",
        auth=component_auth("verifications:read"),
        annotations=tool_annotations("Read a verification's history", READ_ONLY_HINTS),
    )
    async def get_verification_history(
        verification_id: Identifier, deadline_seconds: Deadline = None
    ) -> Any:
        """Read one historical verification summary and its validation path."""

        return await invoke(
            "get_verification_history",
            "verifications:read",
            parameters={"verification_id": verification_id},
            deadline_seconds=deadline_seconds,
        )

    @mcp.tool(
        title="Verify a stored file (billable)",
        auth=component_auth("verify:write"),
        annotations=tool_annotations("Verify a stored file (billable)", BILLABLE_WRITE_HINTS),
        meta=billing_meta(operations="one verification", max_operations=1),
    )
    async def create_verification(
        object_id: Identifier,
        idempotency_key: IdempotencyKey,
        confirmation: Annotated[
            str,
            Field(
                min_length=8,
                max_length=136,
                description="Must equal the exact string `verify:<object_id>`.",
            ),
        ],
        max_billable_operations: MaxBillableOperations = None,
        deadline_seconds: Deadline = None,
    ) -> Any:
        """Submit one stored object for verification after exact confirmation.

        Cost preview: 1 billable operation (one verification). Rates: get_pricing.
        The result states what the file's Content Credentials declare, not whether
        its content is true.
        """

        if confirmation != f"verify:{object_id}":
            raise ToolError("confirmation must exactly match verify:<object_id>")
        check_spend(1, max_billable_operations)
        return await invoke(
            "create_verification",
            "verify:write",
            headers={"Idempotency-Key": idempotency_key},
            body={"object_id": object_id},
            deadline_seconds=deadline_seconds,
        )

    @mcp.tool(
        title="Sign an asset (billable)",
        auth=component_auth("sign:write"),
        annotations=tool_annotations("Sign an asset (billable)", BILLABLE_WRITE_HINTS),
        meta=billing_meta(
            operations="the signature, plus the watermark and fingerprints when chosen",
            max_operations=3,
        ),
    )
    async def sign(
        asset_id: Identifier,
        watermark: Annotated[
            bool, Field(description="Embed an invisible watermark before signing.")
        ],
        fingerprint: Annotated[
            bool, Field(description="Also keep server-side fingerprints for recovery.")
        ],
        idempotency_key: IdempotencyKey,
        confirmation: Annotated[
            str,
            Field(
                min_length=6,
                max_length=133,
                description="Must equal the exact string `sign:<asset_id>`.",
            ),
        ],
        watermark_algorithm: Identifier | None = None,
        watermark_strength: Literal["subtle", "balanced", "robust"] | None = None,
        fingerprint_algorithms: Annotated[
            list[Identifier] | None, Field(default=None, min_length=1, max_length=9)
        ] = None,
        ai_declaration: AiDeclaration | None = None,
        creator_id: Identifier | None = None,
        template_id: Identifier | None = None,
        max_billable_operations: MaxBillableOperations = None,
        deadline_seconds: Deadline = None,
    ) -> Any:
        """Sign one uploaded asset with a C2PA manifest (billable), after exact confirmation.

        Every job signs with C2PA; watermark and fingerprint choose what else it adds.
        An AI declaration is accepted only with watermark false (C2PA claim plan).
        Cost preview: 1 to 3 billable operations on one file: the signature, plus the
        watermark when watermark is true, plus fingerprints when fingerprint is true
        (audio and video watermarks and fingerprints are priced per second). Rates:
        get_pricing. The job runs asynchronously: poll get_job with the returned job_id.
        """

        if confirmation != f"sign:{asset_id}":
            raise ToolError("confirmation must exactly match sign:<asset_id>")
        if ai_declaration is not None and watermark:
            raise ToolError(f"{AI_MARK_REQUIRES_SIGN_ONLY}: send watermark false")
        check_spend(
            sign_operations(watermark=watermark, fingerprint=fingerprint),
            max_billable_operations,
        )
        body: dict[str, Any] = {
            "asset_id": asset_id,
            "watermark": watermark,
            "fingerprint": fingerprint,
        }
        optional: dict[str, Any] = {
            "watermark_algorithm": watermark_algorithm,
            "watermark_strength": watermark_strength,
            "fingerprint_algorithms": fingerprint_algorithms,
            "ai_declaration": None
            if ai_declaration is None
            else ai_declaration.model_dump(exclude_none=True),
            "creator_id": creator_id,
            "template_id": template_id,
        }
        body.update({name: value for name, value in optional.items() if value is not None})
        return await invoke(
            "accept_signing_job",
            "sign:write",
            headers={"Idempotency-Key": idempotency_key},
            body=body,
            deadline_seconds=deadline_seconds,
        )

    # The public check reads a local file, so it exists only on the local STDIO
    # transport: a remote (HTTP) server must never read files on its own host.
    if access.local_files:

        @mcp.tool(
            title="Check a local file on a verify page",
            annotations=tool_annotations(
                "Check a local file on a verify page",
                # It starts a public check on a verify page another account owns (and
                # which that account pays for), so it is neither read-only nor closed.
                {
                    "readOnlyHint": False,
                    "destructiveHint": False,
                    "idempotentHint": False,
                    "openWorldHint": True,
                },
            ),
        )
        async def verify_public(
            slug: VerifyPageSlug,
            file_path: Annotated[
                str,
                Field(
                    min_length=2,
                    max_length=4096,
                    description="Absolute path of a local file of at most 25 MB.",
                ),
            ],
            deadline_seconds: Deadline = None,
        ) -> Any:
            """Check one local file against a public verify page: what the file declares
            about its origin, and whether the page owner's system has a record of it.

            Never a verdict on whether the content is real; show the result's statement.
            Uses no API key; each check is billed to the page owner. Needs verify:write
            in this server's allowlist.
            """

            path = _public_check_file(file_path)

            async def call(client: ApiClient, deadline: float) -> Any:
                return await client.verify_public(slug=slug, file=path, timeout=deadline)

            return await guarded("verify:write", deadline_seconds, call)

    # Resources intentionally mirror only exact, read-only public projections.
    @mcp.resource(
        "originalpictures://assets/{asset_id}",
        auth=component_auth("assets:read"),
        mime_type="application/json",
    )
    async def asset_resource(asset_id: Identifier) -> Any:
        """Exact tenant asset projection."""

        return await invoke("get_asset", "assets:read", parameters={"asset_id": asset_id})

    @mcp.resource(
        "originalpictures://jobs/{job_id}",
        auth=component_auth("jobs:read"),
        mime_type="application/json",
    )
    async def job_resource(job_id: Identifier) -> Any:
        """Exact durable job projection."""

        return await invoke("get_job", "jobs:read", parameters={"job_id": job_id})

    @mcp.resource(
        "originalpictures://receipts/{receipt_id}",
        auth=component_auth("assets:read"),
        mime_type="application/json",
    )
    async def receipt_resource(receipt_id: Identifier) -> Any:
        """Exact immutable signing receipt."""

        return await invoke(
            "get_signing_receipt", "assets:read", parameters={"receipt_id": receipt_id}
        )

    @mcp.resource(
        "originalpictures://recipes/{recipe_id}",
        auth=component_auth("recipes:read"),
        mime_type="application/json",
    )
    async def recipe_resource(recipe_id: Identifier) -> Any:
        """Exact active recipe catalog entry."""

        return await invoke("get_recipe", "recipes:read", parameters={"recipe_id": recipe_id})

    @mcp.resource(
        "originalpictures://verifications/{verification_id}",
        auth=component_auth("recovery:read"),
        mime_type="application/json",
    )
    async def verification_resource(verification_id: Identifier) -> Any:
        """Exact durable verification projection."""

        return await invoke(
            "get_verification",
            "recovery:read",
            parameters={"verification_id": verification_id},
        )


__all__ = [
    "AI_MARK_REQUIRES_SIGN_ONLY",
    "BILLABLE_WRITE_HINTS",
    "BILLING_META_KEY",
    "READ_ONLY_HINTS",
    "SERVER_INSTRUCTIONS",
    "SERVER_NAME",
    "AiDeclaration",
    "ClientFactory",
    "Identifier",
    "IdempotencyKey",
    "MaxBillableOperations",
    "ToolAccess",
    "ToolPolicy",
    "ToolRunner",
    "tool_annotations",
    "billing_meta",
    "create_server",
    "register_tools",
    "sign_operations",
]
