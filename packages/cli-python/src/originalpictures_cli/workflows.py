"""Bounded polling and streaming workflows composed from SDK primitives."""

from __future__ import annotations

import hashlib
import os
import tempfile
from collections.abc import Iterator, Mapping
from contextlib import contextmanager
from pathlib import Path
from typing import Any, cast

import click
from rich.progress import BarColumn, Progress, SpinnerColumn, TaskID, TaskProgressColumn, TextColumn

from originalpictures_cli.runtime import Runtime, invoke

MAX_TRANSFER_BYTES = 5 * 1024 * 1024 * 1024
HASH_CHUNK_BYTES = 1024 * 1024
TERMINAL_JOB_STATES = frozenset({"completed", "canceled", "expired", "rejected", "failed"})


def register_workflow_commands(root: click.Group) -> None:
    uploads = cast(click.Group, root.get_command(click.Context(root), "uploads"))
    assets = cast(click.Group, root.get_command(click.Context(root), "assets"))
    jobs = cast(click.Group, root.get_command(click.Context(root), "jobs"))
    uploads.add_command(upload_file)
    assets.add_command(download_asset)
    jobs.add_command(wait_for_job)


@click.command("file", help="Upload one file and complete its upload session.")
@click.argument(
    "source", type=click.Path(path_type=Path, exists=True, dir_okay=False, readable=True)
)
@click.option("--media-type", required=True, help="Declared IANA media type.")
@click.option(
    "--max-bytes",
    type=click.IntRange(1, MAX_TRANSFER_BYTES),
    default=MAX_TRANSFER_BYTES,
    show_default=True,
    help="Hard local and SDK upload bound.",
)
def upload_file(source: Path, media_type: str, max_bytes: int) -> None:
    runtime = _runtime()

    def run() -> Any:
        source_size = source.stat().st_size
        if source_size <= 0:
            raise ValueError("upload source must not be empty")
        if source_size > max_bytes:
            _raise_too_large(f"upload is {source_size} bytes; configured bound is {max_bytes}")
        digest = _sha256_file(runtime, source, source_size)
        client = cast(Any, runtime.client())
        create = client.create_upload(
            body={
                "byte_length": source_size,
                "declared_media_type": media_type,
                "filename": source.name,
                "mode": "single",
                "sha256": digest,
            }
        )
        create_response = _mapping(create, "upload grant")
        upload = _mapping(create_response.get("upload"), "single-part upload capability")
        upload_id = _string(create_response, "upload_id")
        try:
            with _spinner(runtime, "Streaming upload through the SDK"):
                client.upload_file(
                    _string(upload, "url"),
                    source,
                    sha256=digest,
                    headers=_headers(upload),
                    max_bytes=max_bytes,
                )
            from originalpictures import idempotency_key

            completion = client.complete_upload(
                body={"parts": []},
                parameters={"upload_id": upload_id},
                headers={"Idempotency-Key": idempotency_key("cli")},
            )
        except (Exception, KeyboardInterrupt):
            try:
                client.abort_upload(parameters={"upload_id": upload_id})
            except Exception:
                runtime.output.diagnostic("Upload cleanup could not be confirmed.")
            raise
        safe_grant = {
            key: value for key, value in create_response.items() if key not in {"upload", "parts"}
        }
        return {"completion": completion, "upload": safe_grant}

    runtime.output.success(invoke(runtime, run))


@click.command("download", help="Download an asset through the SDK with exact integrity facts.")
@click.argument("asset_id")
@click.argument("destination", type=click.Path(path_type=Path, dir_okay=False))
@click.option("--overwrite", is_flag=True, help="Replace an existing destination.")
@click.option(
    "--max-bytes",
    type=click.IntRange(1, MAX_TRANSFER_BYTES),
    default=MAX_TRANSFER_BYTES,
    show_default=True,
    help="Hard SDK download bound.",
)
def download_asset(asset_id: str, destination: Path, overwrite: bool, max_bytes: int) -> None:
    runtime = _runtime()

    def run() -> Any:
        if destination.exists() and not overwrite:
            raise ValueError("destination exists; pass --overwrite to replace it")
        if not destination.parent.is_dir():
            raise ValueError("destination parent directory does not exist")
        client = cast(Any, runtime.client())
        grant_value = client.create_asset_download(parameters={"asset_id": asset_id})
        grant = _mapping(grant_value, "download grant")
        byte_length = _integer(grant, "byte_length")
        if byte_length > max_bytes:
            _raise_too_large(f"download is {byte_length} bytes; configured bound is {max_bytes}")
        temporary_path: Path | None = None
        try:
            with tempfile.NamedTemporaryFile(
                dir=destination.parent,
                prefix=f".{destination.name}.",
                suffix=".partial",
                delete=False,
            ) as temporary:
                temporary_path = Path(temporary.name)
            with _spinner(runtime, "Streaming download through the SDK"):
                client.download_file(
                    _string(grant, "url"),
                    temporary_path,
                    byte_length=byte_length,
                    sha256=_string(grant, "sha256"),
                    headers=_headers(grant),
                    max_bytes=max_bytes,
                )
            os.replace(temporary_path, destination)
        except (Exception, KeyboardInterrupt):
            if temporary_path is not None:
                temporary_path.unlink(missing_ok=True)
            raise
        return {
            "asset_id": asset_id,
            "byte_length": byte_length,
            "destination": str(destination),
            "sha256": grant["sha256"],
        }

    runtime.output.success(invoke(runtime, run))


@click.command("wait", help="Poll a job with a bounded deadline and Ctrl-C cancellation.")
@click.argument("job_id")
@click.option(
    "--poll-timeout",
    type=click.FloatRange(0.1, 3600.0),
    default=60.0,
    show_default=True,
)
@click.option(
    "--interval",
    type=click.FloatRange(0.1, 60.0),
    default=1.0,
    show_default=True,
)
@click.option(
    "--max-attempts",
    type=click.IntRange(1, 10_000),
    default=120,
    show_default=True,
)
def wait_for_job(job_id: str, poll_timeout: float, interval: float, max_attempts: int) -> None:
    runtime = _runtime()

    def run() -> Any:
        from originalpictures import poll

        client = cast(Any, runtime.client())
        with _spinner(runtime, "Waiting for job") as spinner:
            progress, task_id = spinner

            def fetch() -> Any:
                value = client.get_job(parameters={"job_id": job_id})
                if isinstance(value, Mapping):
                    state = value.get("state", "unknown")
                    progress.update(task_id, description=f"Job state: {state}")
                return value

            return poll(
                fetch,
                lambda value: (
                    isinstance(value, Mapping) and value.get("state") in TERMINAL_JOB_STATES
                ),
                timeout=poll_timeout,
                interval=interval,
                max_interval=min(max(interval, 0.1) * 5, 60.0),
                max_attempts=max_attempts,
            )

    runtime.output.success(invoke(runtime, run))


def _runtime() -> Runtime:
    runtime = click.get_current_context().find_object(Runtime)
    if runtime is None:
        raise RuntimeError("CLI runtime was not initialized")
    return runtime


def _sha256_file(runtime: Runtime, path: Path, size: int) -> str:
    digest = hashlib.sha256()
    progress = Progress(
        TextColumn("Hashing"),
        BarColumn(),
        TaskProgressColumn(),
        console=runtime.output.stderr,
        disable=runtime.output.json_mode or not runtime.output.stderr.is_terminal,
        transient=True,
    )
    with progress:
        task = progress.add_task("Hashing", total=size)
        with path.open("rb") as source:
            while chunk := source.read(HASH_CHUNK_BYTES):
                digest.update(chunk)
                progress.update(task, advance=len(chunk))
    return digest.hexdigest()


@contextmanager
def _spinner(runtime: Runtime, description: str) -> Iterator[tuple[Progress, TaskID]]:
    progress = Progress(
        SpinnerColumn(),
        TextColumn("{task.description}"),
        console=runtime.output.stderr,
        disable=runtime.output.json_mode or not runtime.output.stderr.is_terminal,
        transient=True,
    )
    with progress:
        task_id = progress.add_task(description, total=None)
        yield progress, task_id


def _mapping(value: Any, label: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ValueError(f"SDK {label} response is malformed")
    return value


def _string(value: Mapping[str, Any], key: str) -> str:
    item = value.get(key)
    if not isinstance(item, str) or not item:
        raise ValueError(f"SDK response is missing {key}")
    return item


def _integer(value: Mapping[str, Any], key: str) -> int:
    item = value.get(key)
    if not isinstance(item, int) or isinstance(item, bool) or item < 0:
        raise ValueError(f"SDK response is missing {key}")
    return item


def _headers(value: Mapping[str, Any]) -> dict[str, str]:
    headers = value.get("headers", {})
    if not isinstance(headers, Mapping):
        raise ValueError("SDK response headers are malformed")
    result: dict[str, str] = {}
    for key, item in headers.items():
        if not isinstance(key, str) or not isinstance(item, str):
            raise ValueError("SDK response headers are malformed")
        result[key] = item
    return result


def _raise_too_large(message: str) -> None:
    from originalpictures.errors import ResponseTooLargeError

    raise ResponseTooLargeError(message)


__all__ = [
    "HASH_CHUNK_BYTES",
    "MAX_TRANSFER_BYTES",
    "TERMINAL_JOB_STATES",
    "register_workflow_commands",
]
