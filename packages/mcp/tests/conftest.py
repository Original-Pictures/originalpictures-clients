from __future__ import annotations

from collections.abc import Callable
from typing import Any

import pytest

from originalpictures_mcp.config import SUPPORTED_SCOPES, Settings


class FakeClient:
    def __init__(
        self,
        *,
        response: Any | Callable[[str, dict[str, Any]], Any] = None,
        error: BaseException | None = None,
    ) -> None:
        self.response = {"ok": True} if response is None else response
        self.error = error
        self.calls: list[tuple[str, dict[str, Any]]] = []

    async def __aenter__(self) -> FakeClient:
        return self

    async def __aexit__(self, *_args: Any) -> None:
        return None

    def __getattr__(self, name: str) -> Callable[..., Any]:
        async def call(**kwargs: Any) -> Any:
            self.calls.append((name, kwargs))
            if self.error is not None:
                raise self.error
            if callable(self.response):
                result = self.response(name, kwargs)
                if hasattr(result, "__await__"):
                    return await result
                return result
            return self.response

        return call


@pytest.fixture
def settings() -> Settings:
    return Settings(
        api_key="opk_lookup.secret-material",
        scopes=SUPPORTED_SCOPES,
        max_output_bytes=4096,
    )


def factory(client: FakeClient) -> Callable[[], FakeClient]:
    return lambda: client
