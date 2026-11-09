"""Real sync/async SDK execution against the shared deterministic V1 server."""

from __future__ import annotations

import asyncio
import base64
import importlib.util
import io
import sys
from pathlib import Path
from typing import Any

import pytest

import originalpictures


def _load_shared_server() -> type[Any]:
    path = Path(__file__).parents[3] / "tests/fixtures/developer_surfaces.py"
    spec = importlib.util.spec_from_file_location("op_sdk_developer_surfaces", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("shared developer-surface fixture could not be loaded")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module.DeveloperSurfaceServer


DeveloperSurfaceServer = _load_shared_server()


def test_shared_v1_fixture_executes_through_real_sync_client() -> None:
    with DeveloperSurfaceServer() as server:
        fixture = server.fixture
        sdk = fixture["sdk"]
        cli = fixture["cli"]
        mcp = fixture["mcp"]

        with originalpictures.Client(
            base_url=server.base_url, api_key=sdk["valid_api_key"], timeout=1
        ) as client:
            assert (
                client.get_shared_verification(parameters={"token": sdk["anonymous_share_token"]})
                == sdk["anonymous_response"]
            )
            anonymous_event = server.state.wait_for(
                "GET", f"/v1/shared-verifications/{sdk['anonymous_share_token']}"
            )
            assert anonymous_event["authorization"] is None
            assert client.get_current_user() == cli["user_response"]
            with pytest.raises(
                originalpictures.ConfigurationError, match="intentionally non-callable"
            ):
                client.request("receiveClerkWebhook", body={}, headers={}, parameters={})
        assert not any(event["path"] == "/webhooks/clerk" for event in server.state.events)

        with (
            originalpictures.Client(
                base_url=server.base_url, api_key=cli["scope_denied_api_key"]
            ) as denied,
            pytest.raises(originalpictures.PermissionDeniedError) as captured,
        ):
            denied.list_assets()
        error = captured.value
        assert error.status_code == cli["scope_error"]["status"]
        assert error.code == cli["scope_error"]["code"]
        assert error.request_id == cli["scope_error"]["request_id"]
        assert error.retryable is False
        assert cli["scope_error"]["detail"] not in str(error)

        with originalpictures.Client(
            base_url=server.base_url, api_key=mcp["valid_api_key"]
        ) as client:
            kwargs = {
                "body": {"object_id": mcp["verification"]["object_id"]},
                "headers": {"Idempotency-Key": mcp["verification"]["idempotency_key"]},
            }
            assert client.create_verification(**kwargs) == mcp["verification"]["response"]
            assert client.create_verification(**kwargs) == mcp["verification"]["response"]

        with (
            originalpictures.Client(
                base_url=server.base_url, api_key=mcp["valid_api_key"], timeout=0.025
            ) as client,
            pytest.raises(originalpictures.DeadlineExceededError),
        ):
            client.get_asset(parameters={"asset_id": mcp["slow_asset"]["id"]})

        upload = cli["upload"]
        download = cli["download"]
        upload_bytes = base64.b64decode(upload["bytes_base64"], validate=True)
        download_bytes = base64.b64decode(download["bytes_base64"], validate=True)
        with originalpictures.Client(base_url=server.base_url) as transfers:
            assert transfers.upload_stream(
                upload["create_response"]["upload"]["url"],
                io.BytesIO(upload_bytes),
                byte_length=upload["byte_length"],
                sha256=upload["sha256"],
                headers=upload["create_response"]["upload"]["headers"],
            ) == {"byte_length": len(upload_bytes), "sha256": upload["sha256"]}
            sink = io.BytesIO()
            assert transfers.download_stream(
                download["grant_response"]["url"],
                sink,
                byte_length=download["byte_length"],
                sha256=download["sha256"],
                headers=download["grant_response"]["headers"],
            ) == {"byte_length": len(download_bytes), "sha256": download["sha256"]}
            assert sink.getvalue() == download_bytes


@pytest.mark.asyncio
async def test_shared_v1_fixture_executes_through_real_async_client() -> None:
    with DeveloperSurfaceServer() as server:
        fixture = server.fixture
        sdk = fixture["sdk"]
        cli = fixture["cli"]
        mcp = fixture["mcp"]
        async with originalpictures.AsyncClient(
            base_url=server.base_url, api_key=sdk["valid_api_key"], timeout=1
        ) as client:
            assert (
                await client.get_shared_verification(
                    parameters={"token": sdk["anonymous_share_token"]}
                )
                == sdk["anonymous_response"]
            )
            assert await client.get_current_user() == cli["user_response"]

        async with originalpictures.AsyncClient(
            base_url=server.base_url, api_key=mcp["valid_api_key"], timeout=1
        ) as client:
            kwargs = {
                "body": {"object_id": mcp["verification"]["object_id"]},
                "headers": {"Idempotency-Key": mcp["verification"]["idempotency_key"]},
            }
            assert await client.create_verification(**kwargs) == mcp["verification"]["response"]
            slow = asyncio.create_task(
                client.get_asset(parameters={"asset_id": mcp["slow_asset"]["id"]})
            )
            await asyncio.to_thread(
                server.state.wait_for, "GET", f"/v1/assets/{mcp['slow_asset']['id']}"
            )
            slow.cancel()
            with pytest.raises(asyncio.CancelledError):
                await slow

        upload = cli["upload"]
        download = cli["download"]
        upload_bytes = base64.b64decode(upload["bytes_base64"], validate=True)
        download_bytes = base64.b64decode(download["bytes_base64"], validate=True)
        async with originalpictures.AsyncClient(base_url=server.base_url) as transfers:
            assert await transfers.upload_stream(
                upload["create_response"]["upload"]["url"],
                io.BytesIO(upload_bytes),
                byte_length=upload["byte_length"],
                sha256=upload["sha256"],
                headers=upload["create_response"]["upload"]["headers"],
            ) == {"byte_length": len(upload_bytes), "sha256": upload["sha256"]}
            sink = io.BytesIO()
            assert await transfers.download_stream(
                download["grant_response"]["url"],
                sink,
                byte_length=download["byte_length"],
                sha256=download["sha256"],
                headers=download["grant_response"]["headers"],
            ) == {"byte_length": len(download_bytes), "sha256": download["sha256"]}
            assert sink.getvalue() == download_bytes
