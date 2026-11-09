"""Deterministic input, output, deadline, and redaction boundaries."""

from __future__ import annotations

import json
import re
from collections.abc import Mapping, Sequence
from dataclasses import asdict, is_dataclass
from typing import Any, Final

from fastmcp.exceptions import ToolError

_SAFE_DETAIL: Final = re.compile(r"^[A-Za-z0-9._:/-]{1,160}$")
_SENSITIVE_KEYS: Final = frozenset(
    {"api_key", "authorization", "challenge_secret", "secret", "signature", "token"}
)


def checked_deadline(value: float | None, *, default: float, maximum: float) -> float:
    deadline = default if value is None else value
    if deadline <= 0 or deadline > maximum:
        raise ToolError(f"deadline_seconds must be greater than zero and at most {maximum:g}")
    return deadline


def bounded_output(value: Any, *, max_bytes: int) -> Any:
    normalized = _normalize(value, depth=0)
    try:
        encoded = json.dumps(
            normalized, ensure_ascii=True, allow_nan=False, separators=(",", ":"), sort_keys=True
        ).encode("utf-8")
    except (TypeError, ValueError) as error:
        raise ToolError("Original Pictures API returned an unsupported result") from error
    if len(encoded) > max_bytes:
        raise ToolError("Original Pictures API result exceeded the configured output bound")
    return normalized


def safe_error(error: BaseException) -> ToolError:
    """Map SDK failures to bounded metadata without reflecting messages or secrets."""

    status = getattr(error, "status_code", None)
    code = _safe_detail(getattr(error, "code", None))
    request_id = _safe_detail(getattr(error, "request_id", None))
    facts = []
    if isinstance(status, int) and 100 <= status <= 599:
        facts.append(f"status={status}")
    if code:
        facts.append(f"code={code}")
    if request_id:
        facts.append(f"request_id={request_id}")
    suffix = f" ({', '.join(facts)})" if facts else ""
    return ToolError(f"Original Pictures API request failed{suffix}")


def _normalize(value: Any, *, depth: int) -> Any:
    if depth > 16:
        raise ToolError("Original Pictures API result exceeded the nesting bound")
    if value is None or isinstance(value, (bool, int, float, str)):
        return value
    if isinstance(value, bytes):
        raise ToolError("Binary media is not returned through MCP tools")
    if hasattr(value, "model_dump"):
        value = value.model_dump(mode="json")
    elif is_dataclass(value) and not isinstance(value, type):
        value = asdict(value)
    if isinstance(value, Mapping):
        result: dict[str, Any] = {}
        for key, item in value.items():
            name = str(key)
            if name.lower() in _SENSITIVE_KEYS:
                result[name] = "[REDACTED]"
            else:
                result[name] = _normalize(item, depth=depth + 1)
        return result
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        if len(value) > 500:
            raise ToolError("Original Pictures API result exceeded the item-count bound")
        return [_normalize(item, depth=depth + 1) for item in value]
    raise ToolError("Original Pictures API returned an unsupported result")


def _safe_detail(value: Any) -> str | None:
    if isinstance(value, str) and _SAFE_DETAIL.fullmatch(value):
        return value
    return None


__all__ = ["bounded_output", "checked_deadline", "safe_error"]
