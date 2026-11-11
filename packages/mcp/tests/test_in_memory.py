from __future__ import annotations

import asyncio
import json
import time
from typing import Any

import anyio
import pytest
from conftest import FakeClient, factory
from fastmcp import Client
from fastmcp.exceptions import ToolError
from originalpictures.errors import ApiError

from originalpictures_mcp import Settings, create_server
from originalpictures_mcp.server import BILLING_META_KEY

EXPECTED_TOOLS = (
    "get_current_user",
    "list_assets",
    "get_asset",
    "list_jobs",
    "get_job",
    "list_receipts",
    "get_signing_receipt",
    "list_recipes",
    "get_recipe",
    "get_usage",
    "get_pricing",
    "list_verifications",
    "get_verification",
    "get_verification_history",
    "create_verification",
    "sign",
    "verify_public",
)
EXPECTED_RESOURCE_TEMPLATES = (
    "originalpictures://assets/{asset_id}",
    "originalpictures://jobs/{job_id}",
    "originalpictures://receipts/{receipt_id}",
    "originalpictures://recipes/{recipe_id}",
    "originalpictures://verifications/{verification_id}",
)


@pytest.mark.asyncio
async def test_server_info_reports_this_package_version(settings: Settings) -> None:
    import tomllib
    from pathlib import Path

    pyproject = Path(__file__).resolve().parents[1] / "pyproject.toml"
    expected = tomllib.loads(pyproject.read_text(encoding="utf-8"))["project"]["version"]
    server = create_server(settings, client_factory=factory(FakeClient()))
    async with Client(server) as client:
        info = client.initialize_result.serverInfo
    assert info.version == expected


@pytest.mark.asyncio
async def test_deterministic_bounded_component_schemas(settings: Settings) -> None:
    server = create_server(settings, client_factory=factory(FakeClient()))
    async with Client(server) as client:
        first = await client.list_tools()
        second = await client.list_tools()
        templates = await client.list_resource_templates()

    assert tuple(tool.name for tool in first) == EXPECTED_TOOLS
    assert [tool.model_dump(mode="json") for tool in first] == [
        tool.model_dump(mode="json") for tool in second
    ]
    assert tuple(str(template.uriTemplate) for template in templates) == EXPECTED_RESOURCE_TEMPLATES
    serialized = json.dumps([tool.inputSchema for tool in first], sort_keys=True)
    assert "route" not in serialized.lower()
    assert "media_bytes" not in serialized
    list_schema = next(tool.inputSchema for tool in first if tool.name == "list_assets")
    assert list_schema["properties"]["limit"]["maximum"] == 100
    assert list_schema["properties"]["cursor"]["anyOf"][0]["maxLength"] == 2048


@pytest.mark.asyncio
async def test_generated_sdk_method_and_grouped_mappings_are_the_only_boundary(
    settings: Settings,
) -> None:
    fake = FakeClient(response={"items": [], "next_cursor": None})
    server = create_server(settings, client_factory=factory(fake))
    async with Client(server) as client:
        result = await client.call_tool(
            "list_assets", {"limit": 3, "cursor": "next_1", "kind": "image"}
        )

    assert result.data == {"items": [], "next_cursor": None}
    assert fake.calls == [
        (
            "list_assets",
            {
                "parameters": {"limit": 3, "cursor": "next_1", "kind": "image"},
                "headers": {},
            },
        )
    ]


@pytest.mark.asyncio
async def test_empty_allowlist_lists_no_tool_and_no_resource_template() -> None:
    # The README promises that an empty ORIGINALPICTURES_MCP_SCOPES shows no tools.
    # 0.1.0 listed all of them over STDIO (package test kit, 2026-11-11).
    server = create_server(
        Settings(api_key="opk_lookup.secret", scopes=frozenset()),
        client_factory=factory(FakeClient()),
    )
    async with Client(server) as client:
        assert await client.list_tools() == []
        assert await client.list_resource_templates() == []


@pytest.mark.asyncio
async def test_listing_follows_the_allowlist_and_hidden_calls_are_still_refused() -> None:
    read_scopes = frozenset(
        {"identity:read", "assets:read", "jobs:read", "recipes:read", "verifications:read"}
    )
    fake = FakeClient()
    server = create_server(
        Settings(api_key="opk_lookup.secret", scopes=read_scopes),
        client_factory=factory(fake),
    )
    async with Client(server) as client:
        tools = {tool.name for tool in await client.list_tools()}
        templates = {str(t.uriTemplate) for t in await client.list_resource_templates()}
        # A tool left out of the listing is still registered, so a client that calls it
        # anyway gets the explicit scope refusal, not an unknown-tool error.
        with pytest.raises(ToolError, match="not configured"):
            await client.call_tool("get_usage", {})

    assert tools == {
        "get_current_user",
        "list_assets",
        "get_asset",
        "list_jobs",
        "get_job",
        "list_receipts",
        "get_signing_receipt",
        "list_recipes",
        "get_recipe",
        "list_verifications",
        "get_verification_history",
    }
    assert not tools & {"sign", "create_verification", "verify_public", "get_pricing"}
    assert templates == {
        "originalpictures://assets/{asset_id}",
        "originalpictures://jobs/{job_id}",
        "originalpictures://receipts/{receipt_id}",
        "originalpictures://recipes/{recipe_id}",
    }
    assert fake.calls == []


@pytest.mark.asyncio
async def test_write_scopes_list_the_billable_tools() -> None:
    server = create_server(
        Settings(api_key="opk_lookup.secret", scopes=frozenset({"sign:write", "verify:write"})),
        client_factory=factory(FakeClient()),
    )
    async with Client(server) as client:
        tools = {tool.name for tool in await client.list_tools()}
    assert tools == {"sign", "create_verification", "verify_public"}


@pytest.mark.asyncio
async def test_default_deny_and_wrong_scope_never_reach_sdk() -> None:
    fake = FakeClient()
    server = create_server(
        Settings(api_key="opk_lookup.secret", scopes=frozenset()),
        client_factory=factory(fake),
    )
    async with Client(server) as client:
        with pytest.raises(ToolError, match="not configured"):
            await client.call_tool("get_asset", {"asset_id": "asset_1"})
    assert fake.calls == []

    wrong_scope = create_server(
        Settings(api_key="opk_lookup.secret", scopes=frozenset({"jobs:read"})),
        client_factory=factory(fake),
    )
    async with Client(wrong_scope) as client:
        with pytest.raises(ToolError, match="not configured"):
            await client.call_tool("list_assets", {})
    assert fake.calls == []


@pytest.mark.asyncio
async def test_page_and_runtime_deadline_bounds_reject_before_sdk(settings: Settings) -> None:
    fake = FakeClient()
    restricted = Settings(
        api_key=settings.api_key,
        scopes=frozenset({"assets:read"}),
        max_page_size=10,
        default_deadline_seconds=2,
        max_deadline_seconds=5,
    )
    server = create_server(restricted, client_factory=factory(fake))
    async with Client(server) as client:
        with pytest.raises(ToolError, match="page bound"):
            await client.call_tool("list_assets", {"limit": 11})
        with pytest.raises(ToolError, match="at most 5"):
            await client.call_tool("get_asset", {"asset_id": "asset_1", "deadline_seconds": 6})
    assert fake.calls == []


@pytest.mark.asyncio
async def test_exact_confirmation_and_idempotency_are_forwarded(settings: Settings) -> None:
    fake = FakeClient(response={"verification_id": "ver_1", "state": "accepted"})
    server = create_server(settings, client_factory=factory(fake))
    async with Client(server) as client:
        with pytest.raises(ToolError, match="exactly match"):
            await client.call_tool(
                "create_verification",
                {
                    "object_id": "object_1",
                    "idempotency_key": "verify-request-1",
                    "confirmation": "verify:other",
                },
            )
        result = await client.call_tool(
            "create_verification",
            {
                "object_id": "object_1",
                "idempotency_key": "verify-request-1",
                "confirmation": "verify:object_1",
            },
        )

    assert result.data == {"verification_id": "ver_1", "state": "accepted"}
    assert fake.calls == [
        (
            "create_verification",
            {
                "parameters": {},
                "headers": {"Idempotency-Key": "verify-request-1"},
                "body": {"object_id": "object_1"},
            },
        )
    ]


@pytest.mark.asyncio
async def test_deadline_holds_when_it_coalesces_with_a_transport_group_cancel(
    settings: Settings,
) -> None:
    """Regression: an anyio task-group cancel must not swallow the per-call deadline.

    httpx connects through anyio, whose happy-eyeballs task group is cancelled by
    the winning attempt. When that cancel and the deadline land in the same loop
    step, an edge-triggered asyncio.timeout() lost its cancel inside anyio's
    TaskGroup.__aexit__ and the tool returned the upstream result long after the
    deadline (the intermittent test_transports "DID NOT RAISE" failure).
    """

    deadline = 0.05

    async def coalescing(_name: str, _kwargs: dict[str, Any]) -> Any:
        loop = asyncio.get_running_loop()
        async with anyio.create_task_group() as group:
            group.start_soon(anyio.sleep_forever)  # a losing connection attempt
            # The winning attempt cancels the group, due just ahead of the deadline.
            loop.call_at(loop.time(), group.cancel_scope.cancel)
            time.sleep(deadline * 5)  # a stalled runner: both timers are now overdue
        await asyncio.sleep(deadline * 4)  # the upstream answers long after the deadline
        return {"late": True}

    server = create_server(settings, client_factory=factory(FakeClient(response=coalescing)))
    async with Client(server) as client:
        for _ in range(3):
            with pytest.raises(ToolError, match="exceeded its deadline"):
                await client.call_tool(
                    "get_asset", {"asset_id": "asset_1", "deadline_seconds": deadline}
                )


@pytest.mark.asyncio
async def test_deadline_cancellation_output_bound_and_redaction(settings: Settings) -> None:
    async def slow(_name: str, _kwargs: dict[str, Any]) -> Any:
        await asyncio.sleep(60)

    deadline_server = create_server(settings, client_factory=factory(FakeClient(response=slow)))
    async with Client(deadline_server) as client:
        with pytest.raises(ToolError, match="exceeded its deadline"):
            await client.call_tool("get_asset", {"asset_id": "asset_1", "deadline_seconds": 0.01})

    started = asyncio.Event()

    async def cancellable(_name: str, _kwargs: dict[str, Any]) -> Any:
        started.set()
        await asyncio.Event().wait()

    cancellation_server = create_server(
        settings, client_factory=factory(FakeClient(response=cancellable))
    )
    async with Client(cancellation_server) as client:
        task = asyncio.create_task(client.call_tool("get_asset", {"asset_id": "asset_1"}))
        await asyncio.wait_for(started.wait(), timeout=1)
        task.cancel()
        with pytest.raises(asyncio.CancelledError):
            await task

    tiny = Settings(
        api_key=settings.api_key,
        scopes=frozenset({"assets:read"}),
        max_output_bytes=1024,
    )
    output_server = create_server(
        tiny, client_factory=factory(FakeClient(response={"payload": "x" * 2048}))
    )
    async with Client(output_server) as client:
        with pytest.raises(ToolError, match="output bound"):
            await client.call_tool("get_asset", {"asset_id": "asset_1"})

    redaction_server = create_server(
        settings,
        client_factory=factory(
            FakeClient(response={"asset_id": "asset_1", "secret": "do-not-return", "token": "cap"})
        ),
    )
    async with Client(redaction_server) as client:
        result = await client.call_tool("get_asset", {"asset_id": "asset_1"})
    assert result.data == {
        "asset_id": "asset_1",
        "secret": "[REDACTED]",
        "token": "[REDACTED]",
    }


@pytest.mark.asyncio
async def test_secret_safe_sdk_error_does_not_reflect_message_or_credential(
    settings: Settings,
) -> None:
    secret = settings.api_key
    error = ApiError(
        f"request with Authorization: Bearer {secret} failed",
        status_code=403,
        code="missing_scope",
        request_id="req_123",
        details={"api_key": secret},
    )
    server = create_server(settings, client_factory=factory(FakeClient(error=error)))
    async with Client(server) as client:
        with pytest.raises(ToolError) as raised:
            await client.call_tool("get_asset", {"asset_id": "asset_1"})
    message = str(raised.value)
    assert secret not in message
    assert "Authorization" not in message
    assert "status=403" in message
    assert "code=missing_scope" in message
    assert "request_id=req_123" in message


@pytest.mark.asyncio
async def test_resource_template_uses_same_scope_gate_and_sdk_boundary(settings: Settings) -> None:
    fake = FakeClient(response={"asset_id": "asset_1", "status": "ready"})
    server = create_server(settings, client_factory=factory(fake))
    async with Client(server) as client:
        contents = await client.read_resource("originalpictures://assets/asset_1")
    assert json.loads(contents[0].text) == {"asset_id": "asset_1", "status": "ready"}
    assert fake.calls == [
        (
            "get_asset",
            {"parameters": {"asset_id": "asset_1"}, "headers": {}},
        )
    ]


@pytest.mark.asyncio
async def test_sign_needs_confirmation_sends_flags_and_refuses_ai_with_watermark(
    settings: Settings,
) -> None:
    fake = FakeClient(response={"job_id": "job_1", "state": "accepted"})
    server = create_server(settings, client_factory=factory(fake))
    base = {"asset_id": "ast_1", "idempotency_key": "sign-1", "fingerprint": True}
    async with Client(server) as client:
        with pytest.raises(ToolError, match="exactly match sign:<asset_id>"):
            await client.call_tool(
                "sign", {**base, "watermark": False, "confirmation": "sign:other"}
            )
        with pytest.raises(ToolError, match=r"needs a sign-only call \(C2PA claim plan\)"):
            await client.call_tool(
                "sign",
                {
                    **base,
                    "watermark": True,
                    "confirmation": "sign:ast_1",
                    "ai_declaration": {"software_agent_name": "Imagine"},
                },
            )
        result = await client.call_tool(
            "sign",
            {
                **base,
                "watermark": False,
                "confirmation": "sign:ast_1",
                "fingerprint_algorithms": ["pdq"],
                "ai_declaration": {"software_agent_name": "Imagine"},
            },
        )

    assert result.data == {"job_id": "job_1", "state": "accepted"}
    assert fake.calls == [
        (
            "accept_signing_job",
            {
                "parameters": {},
                "headers": {"Idempotency-Key": "sign-1"},
                "body": {
                    "asset_id": "ast_1",
                    "watermark": False,
                    "fingerprint": True,
                    "fingerprint_algorithms": ["pdq"],
                    "ai_declaration": {
                        "digital_source_type": "trainedAlgorithmicMedia",
                        "software_agent_name": "Imagine",
                    },
                },
            },
        )
    ]


@pytest.mark.asyncio
async def test_sign_and_verify_public_are_default_deny(tmp_path: Any) -> None:
    fake = FakeClient()
    source = tmp_path / "photo.jpg"
    source.write_bytes(b"x")
    server = create_server(
        Settings(api_key="opk_lookup.secret", scopes=frozenset({"assets:read"})),
        client_factory=factory(fake),
    )
    async with Client(server) as client:
        with pytest.raises(ToolError, match="not configured"):
            await client.call_tool(
                "sign",
                {
                    "asset_id": "ast_1",
                    "watermark": False,
                    "fingerprint": False,
                    "idempotency_key": "sign-1",
                    "confirmation": "sign:ast_1",
                },
            )
        with pytest.raises(ToolError, match="not configured"):
            await client.call_tool(
                "verify_public", {"slug": "studio-nova", "file_path": str(source)}
            )
    assert fake.calls == []


@pytest.mark.asyncio
async def test_verify_public_reads_only_a_bounded_regular_local_file(
    settings: Settings, tmp_path: Any
) -> None:
    fake = FakeClient(response={"state": "completed", "statement": "declared origin only"})
    server = create_server(settings, client_factory=factory(fake))
    source = tmp_path / "photo.jpg"
    source.write_bytes(b"x")
    link = tmp_path / "link.jpg"
    link.symlink_to(source)
    async with Client(server) as client:
        for path, reason in (
            ("photo.jpg", "absolute path"),
            (str(link), "regular file"),
            (str(tmp_path), "regular file"),
        ):
            with pytest.raises(ToolError, match=reason):
                await client.call_tool("verify_public", {"slug": "studio-nova", "file_path": path})
        result = await client.call_tool(
            "verify_public", {"slug": "studio-nova", "file_path": str(source)}
        )

    assert result.data == {"state": "completed", "statement": "declared origin only"}
    ((name, kwargs),) = fake.calls
    assert name == "verify_public"
    assert kwargs["slug"] == "studio-nova"
    assert kwargs["file"] == source


@pytest.mark.asyncio
async def test_verify_public_is_not_offered_over_remote_transport(settings: Settings) -> None:
    remote = Settings(
        api_key=settings.api_key,
        scopes=settings.scopes,
        remote_token="a-long-remote-bearer-token",
    )
    server = create_server(remote, client_factory=factory(FakeClient()))
    # Unfiltered registry: list_tools() would hide every scoped tool without an
    # authenticated HTTP context, which would make this assertion vacuous.
    tools = {tool.name for tool in await server._list_tools()}
    assert "verify_public" not in tools
    assert "sign" in tools


@pytest.mark.asyncio
async def test_every_tool_has_a_title_and_explicit_hints(settings: Settings) -> None:
    """Directory reviewers (Claude, ChatGPT) refuse a tool without a title and all four hints."""

    server = create_server(settings, client_factory=factory(FakeClient()))
    async with Client(server) as client:
        tools = await client.list_tools()
    for tool in tools:
        assert tool.title, tool.name
        hints = tool.annotations
        assert hints is not None, tool.name
        assert hints.title == tool.title
        for hint in ("readOnlyHint", "destructiveHint", "idempotentHint", "openWorldHint"):
            assert isinstance(getattr(hints, hint), bool), (tool.name, hint)
        billable = BILLING_META_KEY in (tool.meta or {})
        assert billable == (tool.name in {"sign", "create_verification"}), tool.name
        if billable:
            assert hints.readOnlyHint is False
            assert "Cost preview" in (tool.description or "")
            assert "max_billable_operations" in tool.inputSchema["properties"]
        elif tool.name != "verify_public":
            assert hints.readOnlyHint is True
            assert hints.openWorldHint is False
        assert hints.destructiveHint is False, tool.name


@pytest.mark.asyncio
async def test_spend_guard_refuses_before_anything_is_sent(settings: Settings) -> None:
    fake = FakeClient(response={"job_id": "job_1"})
    server = create_server(settings, client_factory=factory(fake))
    sign = {
        "asset_id": "ast_1",
        "idempotency_key": "sign-1",
        "confirmation": "sign:ast_1",
        "watermark": True,
        "fingerprint": True,
    }
    async with Client(server) as client:
        with pytest.raises(ToolError, match="start 3 billable operation"):
            await client.call_tool("sign", {**sign, "max_billable_operations": 2})
        with pytest.raises(ToolError, match="above the ceiling of 0"):
            await client.call_tool(
                "create_verification",
                {
                    "object_id": "object_1",
                    "idempotency_key": "verify-1",
                    "confirmation": "verify:object_1",
                    "max_billable_operations": 0,
                },
            )
        assert fake.calls == []
        await client.call_tool("sign", {**sign, "max_billable_operations": 3})
        await client.call_tool("get_pricing", {})
    assert [name for name, _ in fake.calls] == ["accept_signing_job", "get_billing_pricing"]
