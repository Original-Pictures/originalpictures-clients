"""Secret-safe runtime configuration for the MCP adapter."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Final
from urllib.parse import urlsplit

from originalpictures_mcp_scopes import SUPPORTED_SCOPES as _CONTRACT_SUPPORTED_SCOPES

# Public compatibility name for the adapter's closed local allowlist. The
# Connect catalog imports this same dependency-free leaf contract, so the two
# surfaces cannot drift without an import-time/test failure.
SUPPORTED_SCOPES: Final = _CONTRACT_SUPPORTED_SCOPES
if SUPPORTED_SCOPES is not _CONTRACT_SUPPORTED_SCOPES:
    raise RuntimeError("MCP scope contract import drifted")


#: The documented public API origin (docs.originalpictures.com/llms.txt). The retired
#: api.originalpictures.com host is never a default.
DEFAULT_API_BASE_URL: Final = "https://dev-api.originalpictures.com"


class ConfigurationError(ValueError):
    """Configuration is absent or would widen MCP authority."""


@dataclass(frozen=True, slots=True)
class Settings:
    """Closed configuration surface; secrets are excluded from representations."""

    api_key: str = field(repr=False)
    scopes: frozenset[str] = frozenset()
    api_base_url: str = DEFAULT_API_BASE_URL
    remote_token: str | None = field(default=None, repr=False)
    default_deadline_seconds: float = 20.0
    max_deadline_seconds: float = 120.0
    max_output_bytes: int = 256 * 1024
    max_page_size: int = 100

    def __post_init__(self) -> None:
        unknown = self.scopes - SUPPORTED_SCOPES
        if unknown:
            raise ConfigurationError("MCP scope allowlist contains unsupported scopes")
        if not self.api_key.strip() or len(self.api_key) > 1024:
            raise ConfigurationError("ORIGINALPICTURES_API_KEY is required and must be bounded")
        parsed_url = urlsplit(self.api_base_url)
        if (
            parsed_url.scheme not in {"http", "https"}
            or not parsed_url.netloc
            or parsed_url.username is not None
            or parsed_url.password is not None
            or parsed_url.query
            or parsed_url.fragment
            or len(self.api_base_url) > 2048
        ):
            raise ConfigurationError(
                "API base URL must be a bounded http(s) origin without credentials"
            )
        if not (0 < self.default_deadline_seconds <= self.max_deadline_seconds <= 120):
            raise ConfigurationError("deadline bounds are invalid")
        if not (1024 <= self.max_output_bytes <= 1024 * 1024):
            raise ConfigurationError("output bound must be between 1 KiB and 1 MiB")
        if not (1 <= self.max_page_size <= 100):
            raise ConfigurationError("page bound must be between 1 and 100")
        if self.remote_token is not None:
            if not (16 <= len(self.remote_token) <= 4096) or not self.remote_token.strip():
                raise ConfigurationError("remote bearer token must contain 16-4096 characters")
            if self.remote_token == self.api_key:
                raise ConfigurationError(
                    "remote bearer token must differ from the upstream API key"
                )

    @classmethod
    def from_env(cls) -> Settings:
        raw_scopes = os.environ.get("ORIGINALPICTURES_MCP_SCOPES", "")
        scopes = frozenset(value.strip() for value in raw_scopes.split(",") if value.strip())
        return cls(
            api_key=os.environ.get("ORIGINALPICTURES_API_KEY", ""),
            scopes=scopes,
            api_base_url=(
                os.environ.get("ORIGINALPICTURES_API_BASE_URL") or DEFAULT_API_BASE_URL
            ).rstrip("/"),
            remote_token=os.environ.get("ORIGINALPICTURES_MCP_REMOTE_TOKEN") or None,
            default_deadline_seconds=_float_env(
                "ORIGINALPICTURES_MCP_DEFAULT_DEADLINE_SECONDS", 20.0
            ),
            max_deadline_seconds=_float_env("ORIGINALPICTURES_MCP_MAX_DEADLINE_SECONDS", 120.0),
            max_output_bytes=_int_env("ORIGINALPICTURES_MCP_MAX_OUTPUT_BYTES", 256 * 1024),
            max_page_size=_int_env("ORIGINALPICTURES_MCP_MAX_PAGE_SIZE", 100),
        )


def _float_env(name: str, default: float) -> float:
    try:
        return float(os.environ.get(name, str(default)))
    except ValueError as error:
        raise ConfigurationError(f"{name} must be numeric") from error


def _int_env(name: str, default: int) -> int:
    try:
        return int(os.environ.get(name, str(default)))
    except ValueError as error:
        raise ConfigurationError(f"{name} must be an integer") from error


__all__ = ["DEFAULT_API_BASE_URL", "ConfigurationError", "SUPPORTED_SCOPES", "Settings"]
