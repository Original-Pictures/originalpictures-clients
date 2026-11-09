"""Versioned, dependency-free authority for public MCP scope names."""

from typing import Final

#: v2 (2026-10-19) added ``sign:write`` for the MCP ``sign`` tool.
SCOPE_CATALOG_VERSION: Final = "op.mcp-scopes.v2"
SUPPORTED_SCOPES: Final = frozenset(
    {
        "assets:read",
        "billing:read",
        "identity:read",
        "jobs:read",
        "recipes:read",
        "recovery:read",
        "sign:write",
        "verifications:read",
        "verify:write",
    }
)
#: The scopes whose tools change state or start billable work. Every other scope is
#: read-only, which is what a "read-only" MCP configuration may hold.
WRITE_SCOPES: Final = frozenset({"sign:write", "verify:write"})

__all__ = ["SCOPE_CATALOG_VERSION", "SUPPORTED_SCOPES", "WRITE_SCOPES"]
