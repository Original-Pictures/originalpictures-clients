"""The generated SDK is the MCP server's sole Original Pictures API boundary."""

from __future__ import annotations

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Any, Protocol, cast

from originalpictures import AsyncClient

from originalpictures_mcp.config import Settings


class ApiClient(Protocol):
    """Only the generated method shape used by this bounded adapter."""

    def __getattr__(self, name: str) -> Any: ...


@asynccontextmanager
async def sdk_client(settings: Settings) -> AsyncIterator[ApiClient]:
    """Construct and close the official SDK without adding HTTP semantics here."""

    async with AsyncClient(
        base_url=settings.api_base_url,
        api_key=settings.api_key,
        timeout=settings.max_deadline_seconds,
        max_response_bytes=settings.max_output_bytes,
    ) as client:
        yield cast(ApiClient, client)


__all__ = ["ApiClient", "sdk_client"]
