from __future__ import annotations

import asyncio
import json
import os
import socket
from collections.abc import AsyncIterator, Iterable, Mapping
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any

import pytest
from fastmcp import Client
from fastmcp.client.auth import BearerAuth
from fastmcp.client.transports import StdioTransport, StreamableHttpTransport
from fastmcp.exceptions import ToolError
from httpx import HTTPStatusError
from tests.fixtures.developer_surfaces import DeveloperSurfaceServer


def _installed_entrypoint() -> Path:
    requested = Path(os.environ.get("ORIGINALPICTURES_MCP_TEST_EXECUTABLE", ""))
    executable = (
        requested
        if requested.is_file()
        else Path(os.sys.executable).with_name("originalpictures-mcp")
    )
    assert executable.is_file(), f"installed entrypoint not found: {executable}"
    return executable


def _server_env(
    *,
    base_url: str,
    api_key: str,
    scopes: Iterable[str],
    remote_bearer: str | None,
) -> dict[str, str]:
    env = {
        **os.environ,
        "ORIGINALPICTURES_API_BASE_URL": base_url,
        "ORIGINALPICTURES_API_KEY": api_key,
        "ORIGINALPICTURES_MCP_SCOPES": ",".join(sorted(scopes)),
        "ORIGINALPICTURES_MCP_DEFAULT_DEADLINE_SECONDS": "2",
        "ORIGINALPICTURES_MCP_MAX_DEADLINE_SECONDS": "5",
        "ORIGINALPICTURES_MCP_MAX_OUTPUT_BYTES": "1024",
    }
    if remote_bearer is None:
        env.pop("ORIGINALPICTURES_MCP_REMOTE_TOKEN", None)
    else:
        env["ORIGINALPICTURES_MCP_REMOTE_TOKEN"] = remote_bearer
    return env


def _stdio_client(*, base_url: str, api_key: str, scopes: Iterable[str]) -> Client[StdioTransport]:
    return Client(
        StdioTransport(
            command=str(_installed_entrypoint()),
            args=[],
            env=_server_env(
                base_url=base_url,
                api_key=api_key,
                scopes=scopes,
                remote_bearer=None,
            ),
        )
    )


def _unused_loopback_port() -> int:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])
    finally:
        sock.close()


@asynccontextmanager
async def _running_http_endpoint(
    *,
    base_url: str,
    api_key: str,
    scopes: Iterable[str],
    remote_bearer: str,
) -> AsyncIterator[str]:
    port = _unused_loopback_port()
    process = await asyncio.create_subprocess_exec(
        str(_installed_entrypoint()),
        "--transport",
        "http",
        "--host",
        "127.0.0.1",
        "--port",
        str(port),
        env=_server_env(
            base_url=base_url,
            api_key=api_key,
            scopes=scopes,
            remote_bearer=remote_bearer,
        ),
        stdout=asyncio.subprocess.DEVNULL,
        stderr=asyncio.subprocess.PIPE,
    )
    try:
        startup_deadline = asyncio.get_running_loop().time() + 60
        while asyncio.get_running_loop().time() < startup_deadline:
            if process.returncode is not None:
                raise AssertionError("installed MCP HTTP entrypoint exited during startup")
            try:
                _reader, writer = await asyncio.open_connection("127.0.0.1", port)
            except OSError:
                await asyncio.sleep(0.05)
            else:
                writer.close()
                await writer.wait_closed()
                break
        else:
            raise AssertionError("installed MCP HTTP entrypoint did not bind loopback in time")
        yield f"http://127.0.0.1:{port}/mcp"
    finally:
        if process.returncode is None:
            process.terminate()
            try:
                await asyncio.wait_for(process.wait(), timeout=5)
            except TimeoutError:
                process.kill()
                await process.wait()


def _mcp_fixture(server: DeveloperSurfaceServer) -> Mapping[str, Any]:
    fixture = server.fixture["mcp"]
    assert isinstance(fixture, dict)
    return fixture


async def _exercise_success_workflow(client: Client[Any], server: DeveloperSurfaceServer) -> None:
    fixture = _mcp_fixture(server)
    asset = fixture["asset"]
    slow_asset = fixture["slow_asset"]
    large_asset = fixture["large_asset"]
    verification = fixture["verification"]
    assert large_asset["payload_size"] > 1024

    result = await client.call_tool("get_asset", {"asset_id": asset["id"]})
    assert result.data == asset["response"]

    contents = await client.read_resource(f"originalpictures://assets/{asset['id']}")
    assert json.loads(contents[0].text) == asset["response"]

    before_confirmation = len(server.state.events)
    with pytest.raises(ToolError, match="exactly match"):
        await client.call_tool(
            "create_verification",
            {
                "object_id": verification["object_id"],
                "idempotency_key": verification["idempotency_key"],
                "confirmation": "verify:wrong-object",
            },
        )
    assert len(server.state.events) == before_confirmation

    request = {
        "object_id": verification["object_id"],
        "idempotency_key": verification["idempotency_key"],
        "confirmation": verification["confirmation"],
    }
    first = await client.call_tool("create_verification", request)
    second = await client.call_tool("create_verification", request)
    assert first.data == second.data == verification["response"]
    server.state.wait_for("POST", "/v1/verifications", timeout=2)

    slow_path = f"/v1/assets/{slow_asset['id']}"
    cancelled = asyncio.create_task(
        client.call_tool("get_asset", {"asset_id": slow_asset["id"], "deadline_seconds": 2})
    )
    await asyncio.to_thread(server.state.wait_for, "GET", slow_path, timeout=2)
    cancelled.cancel()
    with pytest.raises(asyncio.CancelledError):
        await cancelled

    with pytest.raises(ToolError, match="exceeded its deadline"):
        await client.call_tool(
            "get_asset",
            {"asset_id": slow_asset["id"], "deadline_seconds": 0.01},
        )

    with pytest.raises(ToolError, match="output bound"):
        await client.call_tool("get_asset", {"asset_id": large_asset["id"]})


async def _exercise_default_deny(client: Client[Any], server: DeveloperSurfaceServer) -> None:
    fixture = _mcp_fixture(server)
    before = len(server.state.events)
    # STDIO reaches the explicit local gate; remote component authorization hides
    # the tool entirely. Both fail closed before an upstream SDK request.
    with pytest.raises(ToolError, match="not configured|Unknown tool"):
        await client.call_tool("get_asset", {"asset_id": fixture["asset"]["id"]})
    await asyncio.sleep(0.02)
    assert len(server.state.events) == before


async def _exercise_scope_error_and_redaction(
    client: Client[Any], server: DeveloperSurfaceServer
) -> None:
    fixture = _mcp_fixture(server)
    expected = fixture["scope_error"]
    with pytest.raises(ToolError) as raised:
        await client.call_tool("list_assets", {"limit": 1})
    message = str(raised.value)
    assert f"status={expected['status']}" in message
    assert f"code={expected['code']}" in message
    assert f"request_id={expected['request_id']}" in message
    assert expected["detail"] not in message
    assert fixture["forbidden_api_key"] not in message
    assert fixture["remote_bearer"] not in message


@pytest.mark.asyncio
async def test_installed_stdio_executes_real_sdk_against_shared_v1_fixture() -> None:
    with DeveloperSurfaceServer() as upstream:
        fixture = _mcp_fixture(upstream)
        assert fixture["remote_bearer"] not in {
            fixture["valid_api_key"],
            fixture["forbidden_api_key"],
        }

        async with _stdio_client(
            base_url=upstream.base_url,
            api_key=fixture["valid_api_key"],
            scopes={"assets:read", "recovery:read", "verify:write"},
        ) as client:
            await _exercise_success_workflow(client, upstream)

        async with _stdio_client(
            base_url=upstream.base_url,
            api_key=fixture["valid_api_key"],
            scopes=set(),
        ) as client:
            await _exercise_default_deny(client, upstream)

        async with _stdio_client(
            base_url=upstream.base_url,
            api_key=fixture["forbidden_api_key"],
            scopes={"assets:read"},
        ) as client:
            await _exercise_scope_error_and_redaction(client, upstream)


@pytest.mark.asyncio
async def test_installed_authenticated_stateless_http_executes_real_sdk_fixture() -> None:
    with DeveloperSurfaceServer() as upstream:
        fixture = _mcp_fixture(upstream)
        bearer = fixture["remote_bearer"]
        assert bearer not in {fixture["valid_api_key"], fixture["forbidden_api_key"]}

        async with _running_http_endpoint(
            base_url=upstream.base_url,
            api_key=fixture["valid_api_key"],
            scopes={"assets:read", "recovery:read", "verify:write"},
            remote_bearer=bearer,
        ) as url:
            unauthorized = Client(StreamableHttpTransport(url=url))
            with pytest.raises(HTTPStatusError):
                async with unauthorized:
                    await unauthorized.ping()

            async with Client(StreamableHttpTransport(url=url, auth=BearerAuth(bearer))) as client:
                await _exercise_success_workflow(client, upstream)

            # A fresh connection executes a real tool without session affinity.
            async with Client(StreamableHttpTransport(url=url, auth=BearerAuth(bearer))) as client:
                result = await client.call_tool("get_asset", {"asset_id": fixture["asset"]["id"]})
            assert result.data == fixture["asset"]["response"]

        async with _running_http_endpoint(
            base_url=upstream.base_url,
            api_key=fixture["valid_api_key"],
            scopes=set(),
            remote_bearer=bearer,
        ) as url:
            async with Client(StreamableHttpTransport(url=url, auth=BearerAuth(bearer))) as client:
                await _exercise_default_deny(client, upstream)

        async with _running_http_endpoint(
            base_url=upstream.base_url,
            api_key=fixture["forbidden_api_key"],
            scopes={"assets:read"},
            remote_bearer=bearer,
        ) as url:
            async with Client(StreamableHttpTransport(url=url, auth=BearerAuth(bearer))) as client:
                await _exercise_scope_error_and_redaction(client, upstream)
