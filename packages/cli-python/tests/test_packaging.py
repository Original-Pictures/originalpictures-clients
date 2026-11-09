from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path


def test_local_wheel_install_and_single_entrypoint(tmp_path: Path) -> None:
    project = Path(__file__).parents[1]
    dist = tmp_path / "dist"
    sdk_dist = tmp_path / "sdk-dist"
    subprocess.run(
        ["uv", "build", "--project", str(project), "--out-dir", str(dist)],
        check=True,
        capture_output=True,
        text=True,
    )
    wheel = next(dist.glob("originalpictures_cli-*.whl"))
    subprocess.run(
        [
            "uv",
            "build",
            "--project",
            str(project.parent / "sdk-python"),
            "--out-dir",
            str(sdk_dist),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    sdk_wheel = next(sdk_dist.glob("originalpictures_sdk-*.whl"))

    environment = tmp_path / "venv"
    subprocess.run(
        ["uv", "venv", str(environment), "--python", "3.12"],
        check=True,
        capture_output=True,
        text=True,
    )
    scripts = environment / ("Scripts" if os.name == "nt" else "bin")
    python = scripts / ("python.exe" if os.name == "nt" else "python")
    subprocess.run(
        ["uv", "pip", "install", "--python", str(python), str(sdk_wheel), str(wheel)],
        check=True,
        capture_output=True,
        text=True,
    )
    # `op` was dropped before the first release (2026-11-07): it is the 1Password
    # CLI's command, and installing ours would shadow it on users' PATH.
    assert not (scripts / "op").exists()
    assert not (scripts / "op.exe").exists()
    executable = scripts / "originalpictures"
    completed = subprocess.run(
        [str(executable), "--help"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert "Reviewed Original Pictures public API workflows" in completed.stdout
    malformed = subprocess.run(
        [str(executable), "--json", "jobs", "get"],
        check=False,
        capture_output=True,
        text=True,
    )
    assert malformed.returncode == 2
    assert malformed.stdout == ""
    assert json.loads(malformed.stderr) == {
        "error": {
            "exit_code": 2,
            "kind": "usage",
            "message": "Missing argument 'JOB_ID'.",
        }
    }
    shutil.rmtree(environment)
