from __future__ import annotations

import json
import stat

from click.testing import CliRunner

from originalpictures_cli.cli import cli
from originalpictures_cli.exit_codes import ExitCode


def test_login_reads_stdin_stores_only_in_keyring_and_never_echoes_secret(
    runtime_factory, credentials
) -> None:
    runtime = runtime_factory(environ={})
    secret = "op_live_extremely_sensitive"

    result = CliRunner().invoke(
        cli,
        ["--json", "auth", "login", "--token-stdin"],
        input=f"{secret}\n",
        obj=runtime,
    )

    assert result.exit_code == ExitCode.SUCCESS
    assert secret not in result.stdout
    assert secret not in result.stderr
    assert credentials.values[("originalpictures-cli", "default")] == secret
    assert not runtime.store.path.exists()


def test_config_file_is_deterministic_private_and_contains_no_credential(
    runtime_factory,
) -> None:
    runtime = runtime_factory(environ={"ORIGINALPICTURES_API_KEY": "op_env_secret"})

    result = CliRunner().invoke(
        cli,
        ["--json", "config", "set-api-url", "https://api.original.pictures"],
        obj=runtime,
    )

    assert result.exit_code == ExitCode.SUCCESS
    raw = runtime.store.path.read_text(encoding="utf-8")
    assert raw == '{"profiles":{"default":{"api_url":"https://api.original.pictures"}}}\n'
    assert "op_env_secret" not in raw
    assert stat.S_IMODE(runtime.store.path.stat().st_mode) == 0o600


def test_api_url_rejects_embedded_credentials(runtime_factory) -> None:
    result = CliRunner().invoke(
        cli,
        ["--json", "config", "set-api-url", "https://user:password@example.com"],
        obj=runtime_factory(),
    )

    assert result.exit_code == ExitCode.CONFIGURATION
    payload = json.loads(result.stderr)
    assert payload["error"]["kind"] == "configuration"
    assert "password" not in payload["error"]["message"]


def test_auth_status_never_returns_the_credential(runtime_factory) -> None:
    result = CliRunner().invoke(cli, ["--json", "auth", "status"], obj=runtime_factory())

    assert result.exit_code == ExitCode.SUCCESS
    assert "op_test_secret_value" not in result.stdout
    assert json.loads(result.stdout) == {
        "api_url": "https://api.originalpictures.com",
        "credential_configured": True,
        "credential_source": "environment",
        "profile": "default",
    }


def test_a_fresh_profile_defaults_to_the_public_api_over_https(tmp_path, credentials) -> None:
    # 0.1.0 defaulted to http://localhost:8000: with no configured URL a fresh install sent
    # its bearer key in plain text to whatever listened on that port (test kit, 2026-11-11).
    from originalpictures_cli.config import DEFAULT_API_URL, ConfigStore

    store = ConfigStore(config_dir=tmp_path / "fresh", credential_backend=credentials, environ={})

    assert DEFAULT_API_URL == "https://api.originalpictures.com"
    assert store.resolve().api_url == "https://api.originalpictures.com"
