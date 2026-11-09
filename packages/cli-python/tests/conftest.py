from __future__ import annotations

from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any

import pytest

from originalpictures_cli.config import ConfigStore
from originalpictures_cli.output import Output
from originalpictures_cli.runtime import Runtime


class MemoryCredentials:
    def __init__(self) -> None:
        self.values: dict[tuple[str, str], str] = {}

    def get_password(self, service_name: str, username: str) -> str | None:
        return self.values.get((service_name, username))

    def set_password(self, service_name: str, username: str, password: str) -> None:
        self.values[(service_name, username)] = password

    def delete_password(self, service_name: str, username: str) -> None:
        del self.values[(service_name, username)]


class FakeClient:
    def __init__(self) -> None:
        self.calls: list[tuple[str, tuple[Any, ...], dict[str, Any]]] = []
        self.responses: dict[str, Any] = {}
        self.closed = False

    def close(self) -> None:
        self.closed = True

    def __getattr__(self, name: str) -> Callable[..., Any]:
        def method(*args: Any, **kwargs: Any) -> Any:
            self.calls.append((name, args, kwargs))
            response = self.responses.get(name, {"operation": name})
            if isinstance(response, BaseException):
                raise response
            if callable(response):
                return response(*args, **kwargs)
            return response

        return method


@pytest.fixture
def credentials() -> MemoryCredentials:
    return MemoryCredentials()


@pytest.fixture
def fake_client() -> FakeClient:
    return FakeClient()


@pytest.fixture
def runtime_factory(
    tmp_path: Path,
    credentials: MemoryCredentials,
    fake_client: FakeClient,
) -> Callable[..., Runtime]:
    def build(*, environ: Mapping[str, str] | None = None) -> Runtime:
        environment = (
            environ if environ is not None else {"ORIGINALPICTURES_API_KEY": "op_test_secret_value"}
        )
        store = ConfigStore(
            config_dir=tmp_path / "config",
            credential_backend=credentials,
            environ=environment,
        )

        def client_factory(**_: Any) -> FakeClient:
            return fake_client

        return Runtime(
            store=store,
            output=Output(json_mode=False),
            client_factory=client_factory,
        )

    return build
