from __future__ import annotations

import pytest

from originalpictures_mcp.cli import main, parser, validate_plaintext_http_host
from originalpictures_mcp.config import ConfigurationError, Settings


def test_scope_configuration_is_closed_and_secret_safe() -> None:
    settings = Settings(api_key="opk_lookup.secret", scopes=frozenset())
    assert "opk_lookup" not in repr(settings)
    with pytest.raises(ConfigurationError, match="unsupported scopes"):
        Settings(api_key="opk_lookup.secret", scopes=frozenset({"admin"}))
    with pytest.raises(ConfigurationError, match="must differ"):
        Settings(
            api_key="same-secret-material",
            remote_token="same-secret-material",
        )
    with pytest.raises(ConfigurationError, match="without credentials"):
        Settings(
            api_key="opk_lookup.secret",
            api_base_url="https://user:password@example.invalid/v1?key=secret",
        )


def test_cli_exposes_only_stdio_and_streamable_http() -> None:
    assert parser().parse_args([]).transport == "stdio"
    assert parser().parse_args(["--transport", "http"]).transport == "http"
    for legacy in ("sse", "websocket", "ws"):
        with pytest.raises(SystemExit):
            parser().parse_args(["--transport", legacy])


def test_http_refuses_to_start_without_authentication(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("ORIGINALPICTURES_API_KEY", "opk_lookup.secret")
    monkeypatch.delenv("ORIGINALPICTURES_MCP_REMOTE_TOKEN", raising=False)
    with pytest.raises(SystemExit):
        main(["--transport", "http"])


@pytest.mark.parametrize(
    "host",
    (
        "127.0.0.1",
        "127.255.255.254",
        "::1",
        "0:0:0:0:0:0:0:1",
        "localhost",
        "LOCALHOST",
    ),
)
def test_plaintext_http_accepts_only_explicit_loopback_forms(host: str) -> None:
    assert validate_plaintext_http_host(host) == host


@pytest.mark.parametrize(
    "host",
    (
        "0.0.0.0",
        "::",
        "192.168.1.10",
        "8.8.8.8",
        "::ffff:127.0.0.1",
        "::ffff:7f00:1",
        "example.com",
        "host.docker.internal",
        "localhost.example.com",
        "localhost.",
        "0177.0.0.1",
        "[::1]",
        "::1%lo",
        " localhost",
        "",
    ),
)
def test_plaintext_http_rejects_wildcard_nonloopback_and_ambiguous_hosts(host: str) -> None:
    with pytest.raises(ConfigurationError, match="must bind to a loopback host"):
        validate_plaintext_http_host(host)


@pytest.mark.parametrize("host", ("0.0.0.0", "::", "example.com"))
def test_http_entrypoint_fails_before_binding_nonloopback(
    host: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("ORIGINALPICTURES_API_KEY", "opk_lookup.secret")
    monkeypatch.setenv("ORIGINALPICTURES_MCP_REMOTE_TOKEN", "distinct-remote-token-material")
    with pytest.raises(SystemExit):
        main(["--transport", "http", "--host", host])
