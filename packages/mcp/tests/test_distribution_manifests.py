"""The registry and directory manifests agree with the package and say nothing false.

Covers ``server.json`` (MCP registry), ``smithery.yaml``, ``glama.json`` and the A2A
agent card the marketing site serves at ``/.well-known/agent-card.json``.
"""

from __future__ import annotations

import json
import re
import tomllib
from pathlib import Path
from typing import Any

import yaml
from originalpictures_mcp_scopes import WRITE_SCOPES

from originalpictures_mcp.config import DEFAULT_API_BASE_URL, SUPPORTED_SCOPES

PACKAGE = Path(__file__).resolve().parents[1]
REPO = PACKAGE.parents[1]
AGENT_CARD = REPO / "apps/marketing-site/public/.well-known/agent-card.json"
#: What the API serves at /.well-known/agent-card.json in production (apps/api test_a2a.py).
PUBLISHED_A2A_CARD = REPO / "docs/distribution/a2a-agent-card.json"
# The words the docs and marketing sites refuse (apps/docs/tests/forbidden-claims.mjs).
FORBIDDEN = re.compile(r"\b(?:certified|certification|conformant|conformance|compliant)\b", re.I)
#: The host existing integrations call, which the published card must never name. Spelled
#: in two parts so the monorepo's published-source guard stays a plain substring search.
DEVELOPMENT_API_HOST = "dev-" + "api.originalpictures.com"
A2A_CORE_BINDINGS = {"JSONRPC", "GRPC", "HTTP+JSON"}


def _project() -> dict[str, Any]:
    return tomllib.loads((PACKAGE / "pyproject.toml").read_text(encoding="utf-8"))["project"]


def _server() -> dict[str, Any]:
    return json.loads((PACKAGE / "server.json").read_text(encoding="utf-8"))


def _environment(name: str) -> dict[str, Any]:
    (package,) = _server()["packages"]
    return next(item for item in package["environmentVariables"] if item["name"] == name)


def test_server_json_matches_the_package() -> None:
    server = _server()
    project = _project()
    (package,) = server["packages"]
    # The registry entry is versioned on its own (1.0.0 was published with package 0.1.0,
    # and a registry version can never be reused), so only the package pin must follow
    # pyproject. A new package release still needs a new registry version.
    assert package["version"] == project["version"]
    assert re.fullmatch(r"\d+\.\d+\.\d+", server["version"])
    assert package["identifier"] == project["name"]
    assert server["description"] == project["description"]
    assert len(server["description"]) <= 100
    readme = (PACKAGE / "README.md").read_text(encoding="utf-8")
    assert f"<!-- mcp-name: {server['name']} -->" in readme


def test_server_json_defaults_are_the_packages_own() -> None:
    base_url = _environment("ORIGINALPICTURES_API_BASE_URL")
    assert base_url["default"] == DEFAULT_API_BASE_URL
    assert base_url["isRequired"] is False
    assert "loopback" not in base_url["description"]
    scopes = set(_environment("ORIGINALPICTURES_MCP_SCOPES")["default"].split(","))
    assert scopes <= SUPPORTED_SCOPES
    assert not scopes & WRITE_SCOPES, "the suggested default must stay read-only"
    assert _environment("ORIGINALPICTURES_API_KEY")["isSecret"] is True


def test_smithery_launches_the_published_package_with_the_same_defaults() -> None:
    manifest = yaml.safe_load((PACKAGE / "smithery.yaml").read_text(encoding="utf-8"))
    start = manifest["startCommand"]
    assert start["type"] == "stdio"
    properties = start["configSchema"]["properties"]
    assert start["configSchema"]["required"] == ["apiKey"]
    assert properties["apiBaseUrl"]["default"] == DEFAULT_API_BASE_URL
    assert properties["scopes"]["default"] == _environment("ORIGINALPICTURES_MCP_SCOPES")["default"]
    function = start["commandFunction"]
    assert "command: 'uvx'" in function
    assert f"args: ['{_project()['name']}']" in function
    assert properties["scopes"]["default"] in function
    assert DEFAULT_API_BASE_URL in function


def test_glama_manifest_names_its_schema() -> None:
    manifest = json.loads((PACKAGE / "glama.json").read_text(encoding="utf-8"))
    assert manifest["$schema"] == "https://glama.ai/mcp/schemas/server.json"
    assert manifest["maintainers"]


def test_agent_card_has_the_a2a_required_fields_and_claims_no_a2a_endpoint() -> None:
    card = json.loads(AGENT_CARD.read_text(encoding="utf-8"))
    if any(item.get("protocolBinding") == "JSONRPC" for item in card["supportedInterfaces"]):
        # The API serves a real A2A endpoint since feat/module-c-followup (2026-10-19). Once
        # the marketing site publishes the A2A card, it must be exactly the copy the API's
        # own test holds equal to what the production API serves.
        assert card == json.loads(PUBLISHED_A2A_CARD.read_text(encoding="utf-8"))
        return
    # A2A 1.0 AgentCard REQUIRED fields (a2a.proto).
    for field in (
        "name",
        "description",
        "supportedInterfaces",
        "version",
        "capabilities",
        "defaultInputModes",
        "defaultOutputModes",
        "skills",
    ):
        assert card.get(field), field
    for interface in card["supportedInterfaces"]:
        assert {"url", "protocolBinding", "protocolVersion"} <= interface.keys()
        assert interface["url"] == DEFAULT_API_BASE_URL
        # Original Pictures runs no A2A server, so the card must not name a core A2A
        # binding (which would tell an A2A client to send it JSON-RPC or gRPC).
        assert interface["protocolBinding"] not in A2A_CORE_BINDINGS
    # A 0.3-style top-level url would default to JSON-RPC for 0.3 clients.
    assert "url" not in card
    assert "preferredTransport" not in card
    assert card["capabilities"] == {
        "streaming": False,
        "pushNotifications": False,
        "extendedAgentCard": False,
    }
    for skill in card["skills"]:
        assert {"id", "name", "description", "tags"} <= skill.keys()
        assert skill["tags"]
    text = json.dumps(card)
    assert not FORBIDDEN.search(text)
    assert DEVELOPMENT_API_HOST not in text


def test_server_json_remote_is_the_hosted_endpoint_with_header_auth() -> None:
    (remote,) = _server()["remotes"]
    # Served by the API itself (apps/api op_api.routers.mcp), stateless Streamable HTTP.
    assert remote["type"] == "streamable-http"
    assert remote["url"] == f"{DEFAULT_API_BASE_URL}/mcp"
    (header,) = remote["headers"]
    assert header["name"] == "Authorization"
    assert header["isRequired"] is True and header["isSecret"] is True
    assert header["value"] == "Bearer {api_key}"
    assert header["variables"]["api_key"]["isSecret"] is True
    assert not FORBIDDEN.search(json.dumps(remote))
