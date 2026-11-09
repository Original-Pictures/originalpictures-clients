from __future__ import annotations

import hashlib
import json
from pathlib import Path

from click.testing import CliRunner

from originalpictures_cli.cli import cli
from originalpictures_cli.exit_codes import ExitCode


def _upload_grant() -> dict[str, object]:
    return {
        "asset_id": "ast_1",
        "expires_at": "2026-08-08T00:00:00Z",
        "mode": "single",
        "status": "initiated",
        "upload": {
            "headers": {"x-upload-capability": "secret-capability"},
            "method": "PUT",
            "url": "https://storage.invalid/upload-secret",
        },
        "upload_id": "upl_abcdefghijklmnop",
    }


def test_upload_uses_sdk_file_streaming_exact_facts_and_hides_capability(
    tmp_path: Path, runtime_factory, fake_client
) -> None:
    source = tmp_path / "asset.jpg"
    source.write_bytes(b"asset-bytes")
    fake_client.responses["create_upload"] = _upload_grant()
    fake_client.responses["complete_upload"] = {"status": "complete", "asset_id": "ast_1"}

    result = CliRunner().invoke(
        cli,
        ["--json", "uploads", "file", str(source), "--media-type", "image/jpeg"],
        obj=runtime_factory(),
    )

    assert result.exit_code == ExitCode.SUCCESS
    assert "upload-secret" not in result.stdout
    assert "secret-capability" not in result.stdout
    calls = {name: (args, kwargs) for name, args, kwargs in fake_client.calls}
    create_body = calls["create_upload"][1]["body"]
    assert create_body["byte_length"] == len(b"asset-bytes")
    assert create_body["sha256"] == hashlib.sha256(b"asset-bytes").hexdigest()
    upload_args, upload_kwargs = calls["upload_file"]
    assert upload_args == ("https://storage.invalid/upload-secret", source)
    assert "byte_length" not in upload_kwargs
    assert upload_kwargs["headers"] == {"x-upload-capability": "secret-capability"}
    assert calls["complete_upload"][1]["parameters"] == {"upload_id": "upl_abcdefghijklmnop"}


def test_upload_bound_fails_before_api_or_media_transfer(
    tmp_path: Path, runtime_factory, fake_client
) -> None:
    source = tmp_path / "large.bin"
    source.write_bytes(b"1234")

    result = CliRunner().invoke(
        cli,
        [
            "--json",
            "uploads",
            "file",
            str(source),
            "--media-type",
            "image/jpeg",
            "--max-bytes",
            "3",
        ],
        obj=runtime_factory(),
    )

    assert result.exit_code == ExitCode.TOO_LARGE
    assert fake_client.calls == []
    assert json.loads(result.stderr)["error"]["kind"] == "response_too_large"


def test_upload_keyboard_interrupt_aborts_grant_and_returns_130(
    tmp_path: Path, runtime_factory, fake_client
) -> None:
    source = tmp_path / "asset.jpg"
    source.write_bytes(b"asset-bytes")
    fake_client.responses["create_upload"] = _upload_grant()
    fake_client.responses["upload_file"] = KeyboardInterrupt()

    result = CliRunner().invoke(
        cli,
        ["--json", "uploads", "file", str(source), "--media-type", "image/jpeg"],
        obj=runtime_factory(),
    )

    assert result.exit_code == ExitCode.CANCELLED
    assert any(name == "abort_upload" for name, _, _ in fake_client.calls)
    assert "upload-secret" not in result.stderr


def test_download_uses_sdk_streaming_bound_and_exact_integrity(
    tmp_path: Path, runtime_factory, fake_client
) -> None:
    destination = tmp_path / "asset.jpg"
    body = b"downloaded"
    digest = hashlib.sha256(body).hexdigest()
    fake_client.responses["create_asset_download"] = {
        "byte_length": len(body),
        "headers": {"x-download": "capability"},
        "sha256": digest,
        "url": "https://storage.invalid/download-secret",
    }

    def download(_url, path, **_kwargs):
        Path(path).write_bytes(body)

    fake_client.responses["download_file"] = download
    result = CliRunner().invoke(
        cli,
        ["--json", "assets", "download", "ast_1", str(destination), "--max-bytes", "100"],
        obj=runtime_factory(),
    )

    assert result.exit_code == ExitCode.SUCCESS
    assert destination.read_bytes() == body
    assert "download-secret" not in result.stdout
    calls = {name: (args, kwargs) for name, args, kwargs in fake_client.calls}
    args, kwargs = calls["download_file"]
    assert args[0] == "https://storage.invalid/download-secret"
    assert Path(args[1]).name.startswith(f".{destination.name}.")
    assert kwargs["byte_length"] == len(body)
    assert kwargs["sha256"] == digest
    assert kwargs["max_bytes"] == 100


def test_download_bound_fails_before_sdk_transfer(
    tmp_path: Path, runtime_factory, fake_client
) -> None:
    fake_client.responses["create_asset_download"] = {
        "byte_length": 101,
        "headers": {},
        "sha256": "0" * 64,
        "url": "https://storage.invalid/download-secret",
    }

    result = CliRunner().invoke(
        cli,
        ["--json", "assets", "download", "ast_1", str(tmp_path / "output"), "--max-bytes", "100"],
        obj=runtime_factory(),
    )

    assert result.exit_code == ExitCode.TOO_LARGE
    assert not any(name == "download_file" for name, _, _ in fake_client.calls)


def test_job_wait_uses_sdk_polling_and_emits_one_json_document(
    runtime_factory, fake_client
) -> None:
    fake_client.responses["get_job"] = {
        "job_id": "job_abcdefghijklmnop",
        "progress": {"percent": 100},
        "state": "completed",
    }

    result = CliRunner().invoke(
        cli,
        ["--json", "jobs", "wait", "job_abcdefghijklmnop", "--poll-timeout", "1"],
        obj=runtime_factory(),
    )

    assert result.exit_code == ExitCode.SUCCESS
    assert json.loads(result.stdout)["state"] == "completed"
    assert result.stdout.count("\n") == 1
