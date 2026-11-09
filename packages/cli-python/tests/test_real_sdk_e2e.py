from __future__ import annotations

import base64
import importlib.util
import json
import os
import shutil
import signal
import subprocess
import sys
from collections.abc import Iterator, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pytest


def _load_shared_server() -> type[Any]:
    """Load the repo fixture without colliding with pytest's CLI-local ``tests`` package."""

    path = Path(__file__).parents[3] / "tests/fixtures/developer_surfaces.py"
    spec = importlib.util.spec_from_file_location("op_shared_developer_surfaces", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("shared developer-surface fixture could not be loaded")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module.DeveloperSurfaceServer


DeveloperSurfaceServer = _load_shared_server()


@dataclass(frozen=True)
class InstalledCli:
    python: Path
    originalpictures: Path
    environment: Mapping[str, str]

    def run(
        self,
        arguments: Sequence[str],
        *,
        api_key: str,
        timeout: float = 10.0,
    ) -> subprocess.CompletedProcess[str]:
        environment = dict(self.environment)
        environment["ORIGINALPICTURES_API_KEY"] = api_key
        return subprocess.run(
            [str(self.originalpictures), *arguments],
            check=False,
            capture_output=True,
            text=True,
            timeout=timeout,
            env=environment,
        )


@pytest.fixture(scope="module")
def installed_cli(tmp_path_factory: pytest.TempPathFactory) -> Iterator[InstalledCli]:
    repository = Path(__file__).parents[3]
    temporary = tmp_path_factory.mktemp("installed-cli-e2e")
    cli_dist = temporary / "cli-dist"
    sdk_dist = temporary / "sdk-dist"
    uv = shutil.which("uv")
    assert uv is not None, "uv is required for the local installation acceptance test"

    for project, output in (
        (repository / "packages/cli-python", cli_dist),
        (repository / "packages/sdk-python", sdk_dist),
    ):
        subprocess.run(
            [uv, "build", "--project", str(project), "--out-dir", str(output)],
            check=True,
            capture_output=True,
            text=True,
        )

    cli_wheel = next(cli_dist.glob("originalpictures_cli-*.whl"))
    sdk_wheel = next(sdk_dist.glob("originalpictures_sdk-*.whl"))
    environment_path = temporary / "venv"
    subprocess.run(
        [uv, "venv", str(environment_path), "--python", "3.12"],
        check=True,
        capture_output=True,
        text=True,
    )
    scripts = environment_path / ("Scripts" if os.name == "nt" else "bin")
    python = scripts / ("python.exe" if os.name == "nt" else "python")
    subprocess.run(
        [uv, "pip", "install", "--python", str(python), str(sdk_wheel), str(cli_wheel)],
        check=True,
        capture_output=True,
        text=True,
    )

    isolated_environment = dict(os.environ)
    for name in (
        "PYTHONPATH",
        "PYTHONHOME",
        "VIRTUAL_ENV",
        "ORIGINALPICTURES_API_KEY",
        "ORIGINALPICTURES_API_URL",
        "ORIGINALPICTURES_PROFILE",
    ):
        isolated_environment.pop(name, None)
    isolated_environment.update(
        {
            "HOME": str(temporary / "home"),
            "NO_PROXY": "127.0.0.1,localhost",
            "no_proxy": "127.0.0.1,localhost",
            "XDG_CACHE_HOME": str(temporary / "cache"),
            "XDG_CONFIG_HOME": str(temporary / "config"),
            "XDG_DATA_HOME": str(temporary / "data"),
        }
    )
    origin = subprocess.run(
        [
            str(python),
            "-c",
            "import originalpictures,originalpictures_cli;"
            "print(originalpictures.__file__);print(originalpictures_cli.__file__)",
        ],
        check=True,
        capture_output=True,
        text=True,
        env=isolated_environment,
    )
    assert str(environment_path) in origin.stdout
    assert str(repository) not in origin.stdout

    yield InstalledCli(
        python=python,
        originalpictures=scripts / "originalpictures",
        environment=isolated_environment,
    )


def test_installed_cli_real_sdk_success_and_typed_scope_error(installed_cli: InstalledCli) -> None:
    with DeveloperSurfaceServer() as server:
        cli = _mapping(server.fixture["cli"])
        success = installed_cli.run(
            ["--json", "--api-url", server.base_url, "user", "show"],
            api_key=str(cli["valid_api_key"]),
        )
        assert success.returncode == 0
        assert success.stderr == ""
        assert json.loads(success.stdout) == cli["user_response"]
        success_event = server.state.wait_for("GET", "/v1/me")
        assert success_event["authorization"] == f"Bearer {cli['valid_api_key']}"

        scope = _mapping(cli["scope_error"])
        denied = installed_cli.run(
            ["--json", "--api-url", server.base_url, "assets", "list"],
            api_key=str(cli["scope_denied_api_key"]),
        )
        assert denied.returncode == 6
        assert denied.stdout == ""
        error = _canonical_stderr(denied.stderr)
        assert error["error"]["kind"] == "permission_denied"
        assert error["error"]["details"]["status_code"] == scope["status"]
        assert error["error"]["details"]["code"] == scope["code"]
        assert error["error"]["details"]["request_id"] == scope["request_id"]
        assert str(scope["detail"]) not in denied.stderr
        assert str(cli["scope_denied_api_key"]) not in denied.stderr


def test_installed_cli_real_sdk_idempotency_and_polling(
    tmp_path: Path, installed_cli: InstalledCli
) -> None:
    with DeveloperSurfaceServer() as server:
        cli = _mapping(server.fixture["cli"])
        api_key_create = _mapping(cli["api_key_create"])
        input_path = tmp_path / "api-key.json"
        input_path.write_text(_canonical(api_key_create["body"]), encoding="utf-8")
        created = installed_cli.run(
            [
                "--json",
                "--api-url",
                server.base_url,
                "keys",
                "create",
                "--input",
                str(input_path),
            ],
            api_key=str(cli["valid_api_key"]),
        )
        assert created.returncode == 0
        assert json.loads(created.stdout) == api_key_create["response"]
        create_event = server.state.wait_for("POST", "/v1/api-keys")
        assert str(create_event["idempotency_key"]).startswith("cli-")
        assert str(cli["valid_api_key"]) not in created.stdout
        assert str(cli["valid_api_key"]) not in created.stderr

        job = _mapping(cli["job"])
        waited = installed_cli.run(
            [
                "--json",
                "--api-url",
                server.base_url,
                "jobs",
                "wait",
                str(job["id"]),
                "--poll-timeout",
                "2",
                "--interval",
                "0.1",
                "--max-attempts",
                "4",
            ],
            api_key=str(cli["valid_api_key"]),
        )
        assert waited.returncode == 0
        assert json.loads(waited.stdout) == job["completed_response"]
        job_events = _events(server, "GET", f"/v1/jobs/{job['id']}")
        assert len(job_events) == 2


def test_installed_cli_real_sdk_deadline_and_sigint_cancellation(
    installed_cli: InstalledCli,
) -> None:
    with DeveloperSurfaceServer() as server:
        cli = _mapping(server.fixture["cli"])
        slow = _mapping(cli["slow_user"])
        server.state.delay_next_user_request(float(slow["delay_seconds"]))
        timed_out = installed_cli.run(
            [
                "--json",
                "--api-url",
                server.base_url,
                "--timeout",
                "0.1",
                "user",
                "show",
            ],
            api_key=str(cli["valid_api_key"]),
        )
        assert timed_out.returncode == 10
        assert timed_out.stdout == ""
        timeout_error = _canonical_stderr(timed_out.stderr)
        assert timeout_error["error"]["kind"] == "deadline_exceeded"
        assert str(cli["valid_api_key"]) not in timed_out.stderr

    with DeveloperSurfaceServer() as server:
        cli = _mapping(server.fixture["cli"])
        slow = _mapping(cli["slow_user"])
        # The request must still be in flight when SIGINT lands. On a loaded
        # runner the fixture's short delay can elapse between the server
        # observing the request and the signal arriving, so hold it longer here;
        # SIGINT ends the wait either way.
        server.state.delay_next_user_request(max(float(slow["delay_seconds"]), 5.0))
        environment = dict(installed_cli.environment)
        environment["ORIGINALPICTURES_API_KEY"] = str(cli["valid_api_key"])
        process = subprocess.Popen(
            [
                str(installed_cli.originalpictures),
                "--json",
                "--api-url",
                server.base_url,
                "user",
                "show",
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=environment,
        )
        # Starting the installed CLI can take several seconds under the full
        # gate's load (the release rehearsal timed out at the 5 s default).
        server.state.wait_for("GET", "/v1/me", timeout=30.0)
        process.send_signal(signal.SIGINT)
        stdout, stderr = process.communicate(timeout=30)
        assert process.returncode == 130
        assert stdout == ""
        cancelled = _canonical_stderr(stderr)
        assert cancelled["error"]["kind"] == "cancelled"
        assert str(cli["valid_api_key"]) not in stderr


def test_installed_cli_real_sdk_verified_upload_and_download(
    tmp_path: Path, installed_cli: InstalledCli
) -> None:
    with DeveloperSurfaceServer() as server:
        cli = _mapping(server.fixture["cli"])
        upload = _mapping(cli["upload"])
        upload_bytes = base64.b64decode(str(upload["bytes_base64"]), validate=True)
        source = tmp_path / "fixture-upload.png"
        source.write_bytes(upload_bytes)
        uploaded = installed_cli.run(
            [
                "--json",
                "--api-url",
                server.base_url,
                "uploads",
                "file",
                str(source),
                "--media-type",
                str(upload["media_type"]),
                "--max-bytes",
                str(upload["max_bytes"]),
            ],
            api_key=str(cli["valid_api_key"]),
        )
        assert uploaded.returncode == 0, uploaded.stderr
        assert json.loads(uploaded.stdout)["completion"] == upload["complete_response"]
        upload_event = server.state.wait_for("PUT", "/storage/upload")
        capability = _mapping(upload["capability_header"])
        assert upload_event["authorization"] is None
        assert upload_event["headers"][str(capability["name"])] == capability["value"]
        assert upload_event["body"] == upload_bytes
        complete_event = server.state.wait_for("POST", "/v1/uploads/upl_fixture/complete")
        assert str(complete_event["idempotency_key"]).startswith("cli-")
        assert str(capability["value"]) not in uploaded.stdout
        assert "/storage/upload" not in uploaded.stdout

        download = _mapping(cli["download"])
        destination = tmp_path / "fixture-download.png"
        downloaded = installed_cli.run(
            [
                "--json",
                "--api-url",
                server.base_url,
                "assets",
                "download",
                str(download["asset_id"]),
                str(destination),
                "--max-bytes",
                str(download["max_bytes"]),
            ],
            api_key=str(cli["valid_api_key"]),
        )
        assert downloaded.returncode == 0, downloaded.stderr
        expected_download = base64.b64decode(str(download["bytes_base64"]), validate=True)
        assert destination.read_bytes() == expected_download
        assert json.loads(downloaded.stdout)["sha256"] == download["sha256"]
        download_event = server.state.wait_for("GET", "/storage/download")
        download_capability = _mapping(download["capability_header"])
        assert download_event["authorization"] is None
        assert (
            download_event["headers"][str(download_capability["name"])]
            == download_capability["value"]
        )
        assert str(download_capability["value"]) not in downloaded.stdout
        assert "/storage/download" not in downloaded.stdout


def _mapping(value: object) -> dict[str, Any]:
    assert isinstance(value, dict)
    return value


def _canonical(value: object) -> str:
    return json.dumps(
        value, ensure_ascii=False, allow_nan=False, separators=(",", ":"), sort_keys=True
    )


def _canonical_stderr(value: str) -> dict[str, Any]:
    assert value.count("\n") == 1
    decoded = json.loads(value)
    assert value == _canonical(decoded) + "\n"
    return _mapping(decoded)


def _events(server: Any, method: str, path: str) -> list[dict[str, Any]]:
    return [
        event
        for event in server.state.events
        if event.get("method") == method and event.get("path") == path
    ]
