"""Deterministic output and secret-safe diagnostics."""

from __future__ import annotations

import dataclasses
import json
import re
from collections.abc import Mapping, Sequence
from datetime import date, datetime
from enum import Enum
from pathlib import Path
from typing import Any

import click
from rich.console import Console
from rich.json import JSON

_SECRET_KEY = re.compile(
    r"(^|[_-])(api[_-]?key|authorization|credential|password|secret|token)($|[_-])",
    re.IGNORECASE,
)
_REDACTED = "[REDACTED]"


def normalize(value: Any) -> Any:
    """Convert SDK response values into deterministic JSON-compatible data."""

    if dataclasses.is_dataclass(value) and not isinstance(value, type):
        return normalize(dataclasses.asdict(value))
    if hasattr(value, "model_dump") and callable(value.model_dump):
        return normalize(value.model_dump(mode="json"))
    if isinstance(value, Mapping):
        return {str(key): normalize(item) for key, item in value.items()}
    if isinstance(value, tuple | list):
        return [normalize(item) for item in value]
    if isinstance(value, set | frozenset):
        return sorted((normalize(item) for item in value), key=canonical_json)
    if isinstance(value, datetime | date):
        return value.isoformat()
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, Enum):
        return normalize(value.value)
    if isinstance(value, bytes | bytearray | memoryview):
        return {"byte_length": len(value), "value": "[BINARY OMITTED]"}
    if value is None or isinstance(value, str | int | float | bool):
        return value
    raise TypeError(f"unsupported output type: {type(value).__name__}")


def redact(value: Any, *, known_secrets: Sequence[str] = ()) -> Any:
    """Recursively remove credentials before displaying diagnostic data."""

    normalized = normalize(value)
    secrets = tuple(secret for secret in known_secrets if secret)

    def visit(item: Any) -> Any:
        if isinstance(item, dict):
            return {
                key: _REDACTED if _SECRET_KEY.search(key) else visit(child)
                for key, child in item.items()
            }
        if isinstance(item, list):
            return [visit(child) for child in item]
        if isinstance(item, str):
            result = item
            for secret in secrets:
                result = result.replace(secret, _REDACTED)
            return result
        return item

    return visit(normalized)


def canonical_json(value: Any) -> str:
    """Serialize one compact, key-sorted, newline-free JSON value."""

    return json.dumps(
        normalize(value),
        ensure_ascii=False,
        allow_nan=False,
        separators=(",", ":"),
        sort_keys=True,
    )


class Output:
    def __init__(self, *, json_mode: bool) -> None:
        self.json_mode = json_mode
        self.stdout = Console(file=click.get_text_stream("stdout"), highlight=False)
        self.stderr = Console(file=click.get_text_stream("stderr"), highlight=False)

    def success(self, value: Any) -> None:
        normalized = normalize(value)
        if self.json_mode:
            click.echo(canonical_json(normalized))
            return
        self.stdout.print(JSON.from_data(normalized, indent=2, sort_keys=True))

    def diagnostic(self, message: str) -> None:
        self.stderr.print(message)

    def error(
        self,
        *,
        code: int,
        kind: str,
        message: str,
        details: Any | None = None,
        known_secrets: Sequence[str] = (),
    ) -> None:
        payload: dict[str, Any] = {
            "error": {
                "exit_code": code,
                "kind": kind,
                "message": message,
            }
        }
        if details:
            payload["error"]["details"] = details
        safe = redact(payload, known_secrets=known_secrets)
        if self.json_mode:
            click.echo(canonical_json(safe), err=True)
            return
        self.stderr.print(f"[red]Error ({kind})[/red]: {safe['error']['message']}")


__all__ = ["Output", "canonical_json", "normalize", "redact"]
