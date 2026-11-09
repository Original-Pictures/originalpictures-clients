from __future__ import annotations

import json
from pathlib import Path

import pytest
from click.testing import CliRunner
from originalpictures.errors import AuthenticationError

from originalpictures_cli.cli import cli
from originalpictures_cli.exit_codes import ExitCode


def test_json_output_is_compact_sorted_and_stdout_only(runtime_factory, fake_client) -> None:
    fake_client.responses["get_job"] = {"z": 1, "a": {"two": 2, "one": 1}}

    result = CliRunner().invoke(
        cli,
        ["--json", "jobs", "get", "job_abcdefghijklmnop"],
        obj=runtime_factory(),
    )

    assert result.exit_code == ExitCode.SUCCESS
    assert result.stdout == '{"a":{"one":1,"two":2},"z":1}\n'
    assert result.stderr == ""
    assert fake_client.calls == [
        ("get_job", (), {"parameters": {"job_id": "job_abcdefghijklmnop"}})
    ]


def test_api_error_mapping_redacts_known_credential(runtime_factory, fake_client) -> None:
    fake_client.responses["get_current_user"] = AuthenticationError(
        "credential op_test_secret_value was rejected",
        status_code=401,
        code="AUTH_INVALID",
        request_id="req_123",
    )

    result = CliRunner().invoke(cli, ["--json", "user", "show"], obj=runtime_factory())

    assert result.exit_code == ExitCode.AUTHENTICATION
    assert result.stdout == ""
    assert "op_test_secret_value" not in result.stderr
    payload = json.loads(result.stderr)
    assert payload["error"]["exit_code"] == ExitCode.AUTHENTICATION
    assert payload["error"]["message"] == "credential [REDACTED] was rejected"
    assert payload["error"]["details"] == {
        "code": "AUTH_INVALID",
        "request_id": "req_123",
        "status_code": 401,
    }


def test_mutation_reads_body_from_file_and_generates_idempotency_key(
    tmp_path: Path, runtime_factory, fake_client
) -> None:
    body = tmp_path / "key.json"
    body.write_text('{"name":"automation","scopes":["assets:read"]}', encoding="utf-8")
    fake_client.responses["create_api_key"] = {"api_key_id": "key_1"}

    result = CliRunner().invoke(
        cli,
        ["--json", "keys", "create", "--input", str(body)],
        obj=runtime_factory(),
    )

    assert result.exit_code == ExitCode.SUCCESS
    name, _, kwargs = fake_client.calls[0]
    assert name == "create_api_key"
    assert kwargs["body"] == {"name": "automation", "scopes": ["assets:read"]}
    assert kwargs["headers"]["Idempotency-Key"].startswith("cli-")


def test_parameter_file_cannot_override_explicit_resource_id(
    tmp_path: Path, runtime_factory
) -> None:
    parameters = tmp_path / "params.json"
    parameters.write_text('{"job_id":"job_different"}', encoding="utf-8")

    result = CliRunner().invoke(
        cli,
        [
            "--json",
            "jobs",
            "get",
            "job_abcdefghijklmnop",
            "--parameters",
            str(parameters),
        ],
        obj=runtime_factory(),
    )

    assert result.exit_code == ExitCode.USAGE
    assert "conflicts with the explicit job_id argument" in result.stderr


def test_missing_credential_has_stable_configuration_exit(runtime_factory) -> None:
    result = CliRunner().invoke(
        cli,
        ["--json", "user", "show"],
        obj=runtime_factory(environ={}),
    )

    assert result.exit_code == ExitCode.CONFIGURATION
    assert result.stdout == ""
    assert json.loads(result.stderr)["error"]["kind"] == "configuration"


def test_no_raw_route_escape_hatch(runtime_factory) -> None:
    result = CliRunner().invoke(cli, ["--help"], obj=runtime_factory())

    assert result.exit_code == ExitCode.SUCCESS
    assert " raw " not in result.stdout.lower()
    assert "Root options must appear before the command group" in result.stdout


@pytest.mark.parametrize(
    ("arguments", "message_fragment"),
    [
        (["--json", "jobs", "get"], "Missing argument 'JOB_ID'"),
        (["--json", "--timeout", "not-a-number", "user", "show"], "not-a-number"),
        (["--json", "not-a-command"], "No such command 'not-a-command'"),
        (
            ["--json", "jobs", "get", "job_abcdefghijklmnop", "--not-an-option"],
            "No such option '--not-an-option'",
        ),
        (["jobs", "--json"], "No such option '--json'"),
    ],
)
def test_json_covers_click_parsing_and_usage_errors(
    runtime_factory, arguments: list[str], message_fragment: str
) -> None:
    result = CliRunner().invoke(cli, arguments, obj=runtime_factory())

    assert result.exit_code == ExitCode.USAGE
    assert result.stdout == ""
    assert result.stderr.count("\n") == 1
    payload = json.loads(result.stderr)
    assert payload["error"]["exit_code"] == ExitCode.USAGE
    assert payload["error"]["kind"] == "usage"
    assert message_fragment in payload["error"]["message"]


def test_non_json_usage_error_keeps_click_human_output(runtime_factory) -> None:
    result = CliRunner().invoke(cli, ["jobs", "get"], obj=runtime_factory())

    assert result.exit_code == ExitCode.USAGE
    assert result.stdout == ""
    assert "Usage:" in result.stderr
    assert "Error: Missing argument 'JOB_ID'." in result.stderr
    with pytest.raises(json.JSONDecodeError):
        json.loads(result.stderr)


def test_fingerprint_algorithm_flags_fill_the_sign_request(
    tmp_path: Path, runtime_factory, fake_client
) -> None:
    body = tmp_path / "sign.json"
    body.write_text('{"asset_id":"ast_1","watermark":false}', encoding="utf-8")
    fake_client.responses["accept_signing_job"] = {"job_id": "job_1"}

    result = CliRunner().invoke(
        cli,
        ["--json", "sign", "accept", "--input", str(body), "--fingerprint"]
        + ["--fingerprint-algorithm", "pdq", "--fingerprint-algorithm", "dinov2"],
        obj=runtime_factory(),
    )

    assert result.exit_code == ExitCode.SUCCESS, result.stderr
    name, _, kwargs = fake_client.calls[0]
    assert name == "accept_signing_job"
    assert kwargs["body"] == {
        "asset_id": "ast_1",
        "watermark": False,
        "fingerprint": True,
        "fingerprint_algorithms": ["pdq", "dinov2"],
    }


def test_fingerprint_algorithm_flags_cannot_contradict_the_request_file(
    tmp_path: Path, runtime_factory
) -> None:
    body = tmp_path / "sign.json"
    body.write_text(
        '{"asset_id":"ast_1","fingerprint":true,"fingerprint_algorithms":["pdq"]}',
        encoding="utf-8",
    )

    result = CliRunner().invoke(
        cli,
        ["--json", "sign", "accept", "--input", str(body)] + ["--fingerprint-algorithm", "dinov2"],
        obj=runtime_factory(),
    )

    assert result.exit_code == ExitCode.USAGE
    assert "conflicts with the explicit --fingerprint-algorithm flags" in result.stderr


def test_flags_alone_build_the_whole_sign_request(runtime_factory, fake_client) -> None:
    fake_client.responses["accept_signing_job"] = {"job_id": "job_1"}

    result = CliRunner().invoke(
        cli,
        ["--json", "sign", "accept", "--asset", "ast_1", "--watermark", "--no-fingerprint"]
        + ["--watermark-algorithm", "pixelseal", "--watermark-strength", "subtle"],
        obj=runtime_factory(),
    )

    assert result.exit_code == ExitCode.SUCCESS, result.stderr
    _, _, kwargs = fake_client.calls[0]
    assert kwargs["body"] == {
        "asset_id": "ast_1",
        "watermark": True,
        "fingerprint": False,
        "watermark_algorithm": "pixelseal",
        "watermark_strength": "subtle",
    }
    assert "Idempotency-Key" in kwargs["headers"]


def test_sign_needs_a_body_from_a_file_or_flags(runtime_factory, fake_client) -> None:
    result = CliRunner().invoke(cli, ["--json", "sign", "accept"], obj=runtime_factory())

    assert result.exit_code == ExitCode.USAGE
    assert "pass --input FILE or the request flags" in result.stderr
    assert fake_client.calls == []


def test_the_strength_alias_and_the_recipe_still_work(
    tmp_path: Path, runtime_factory, fake_client
) -> None:
    body = tmp_path / "sign.json"
    body.write_text('{"asset_id":"ast_1"}', encoding="utf-8")
    fake_client.responses["accept_signing_job"] = {"job_id": "job_1"}

    result = CliRunner().invoke(
        cli,
        ["--json", "sign", "accept", "--input", str(body)]
        + ["--recipe", "rcp_system_watermark_then_sign_unfingerprinted", "--strength", "subtle"],
        obj=runtime_factory(),
    )

    assert result.exit_code == ExitCode.SUCCESS, result.stderr
    _, _, kwargs = fake_client.calls[0]
    assert kwargs["body"] == {
        "asset_id": "ast_1",
        "recipe_id": "rcp_system_watermark_then_sign_unfingerprinted",
        "watermark_strength": "subtle",
    }


def test_mode_flags_refuse_an_unknown_strength_and_a_contradiction(
    tmp_path: Path, runtime_factory
) -> None:
    body = tmp_path / "sign.json"
    body.write_text(
        '{"asset_id":"ast_1","recipe_id":"rcp_system_sign","watermark":false}', encoding="utf-8"
    )

    unknown = CliRunner().invoke(
        cli,
        ["sign", "accept", "--input", str(body), "--watermark-strength", "gentle"],
        obj=runtime_factory(),
    )
    assert unknown.exit_code == ExitCode.USAGE
    contradiction = CliRunner().invoke(
        cli,
        ["--json", "sign", "accept", "--input", str(body), "--recipe", "rcp_system_sign_only"],
        obj=runtime_factory(),
    )
    assert contradiction.exit_code == ExitCode.USAGE
    assert "conflicts with the explicit --recipe flag" in contradiction.stderr
    flag = CliRunner().invoke(
        cli,
        ["--json", "sign", "accept", "--input", str(body), "--watermark"],
        obj=runtime_factory(),
    )
    assert flag.exit_code == ExitCode.USAGE
    assert "'watermark' conflicts with the explicit --watermark flag" in flag.stderr


def test_ai_generated_builds_the_declaration(runtime_factory, fake_client) -> None:
    fake_client.responses["accept_signing_job"] = {"job_id": "job_1"}

    result = CliRunner().invoke(
        cli,
        ["--json", "sign", "accept", "--asset", "ast_1", "--no-watermark", "--fingerprint"]
        + ["--ai-generated", "--software-agent", "Studio Nova Imagine"]
        + ["--software-agent-version", "2.0"],
        obj=runtime_factory(),
    )

    assert result.exit_code == ExitCode.SUCCESS, result.stderr
    _, _, kwargs = fake_client.calls[0]
    assert kwargs["body"] == {
        "asset_id": "ast_1",
        "watermark": False,
        "fingerprint": True,
        "ai_declaration": {
            "digital_source_type": "trainedAlgorithmicMedia",
            "software_agent_name": "Studio Nova Imagine",
            "software_agent_version": "2.0",
        },
    }


def test_ai_generated_is_refused_locally_with_a_watermark(runtime_factory, fake_client) -> None:
    result = CliRunner().invoke(
        cli,
        ["--json", "sign", "accept", "--asset", "ast_1", "--watermark"]
        + ["--ai-generated", "--software-agent", "Imagine"],
        obj=runtime_factory(),
    )

    assert result.exit_code == ExitCode.USAGE
    assert "AI-generated mark needs a sign-only call (C2PA claim plan)" in result.stderr
    assert fake_client.calls == []


def test_ai_companions_need_ai_generated_and_a_software_agent(runtime_factory) -> None:
    orphan = CliRunner().invoke(
        cli,
        ["sign", "accept", "--asset", "ast_1", "--software-agent", "Imagine"],
        obj=runtime_factory(),
    )
    assert orphan.exit_code == ExitCode.USAGE
    assert "--software-agent needs --ai-generated" in orphan.stderr
    unnamed = CliRunner().invoke(
        cli,
        ["sign", "accept", "--asset", "ast_1", "--no-watermark", "--ai-generated"],
        obj=runtime_factory(),
    )
    assert unnamed.exit_code == ExitCode.USAGE
    assert "--ai-generated needs --software-agent NAME" in unnamed.stderr


def test_capabilities_show_calls_discovery(runtime_factory, fake_client) -> None:
    fake_client.responses["get_capabilities"] = {"media": []}

    result = CliRunner().invoke(cli, ["--json", "capabilities", "show"], obj=runtime_factory())

    assert result.exit_code == ExitCode.SUCCESS
    assert fake_client.calls == [("get_capabilities", (), {})]
