"""One deterministic local HTTP fixture shared by SDK, CLI and MCP E2E tests."""

from __future__ import annotations

import base64
import copy
import json
import signal
import threading
import time
from collections.abc import Mapping
from contextlib import AbstractContextManager
from dataclasses import dataclass, field
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from types import TracebackType
from typing import Any, Self
from urllib.parse import urlsplit

FIXTURE_PATH = Path(__file__).with_name("developer-surfaces") / "v1.json"


def load_v1_fixture() -> dict[str, Any]:
    """Load an isolated copy of the checked-in V1 developer-surface facts."""

    value = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise TypeError("developer-surface fixture root must be an object")
    return value


@dataclass(slots=True)
class DeveloperSurfaceState:
    """Thread-safe observable state for subprocess and protocol assertions."""

    events: list[dict[str, Any]] = field(default_factory=list)
    uploaded_bytes: bytes = b""
    job_calls: int = 0
    next_user_delay: float = 0.0
    _condition: threading.Condition = field(default_factory=threading.Condition, repr=False)

    def record(self, event: dict[str, Any]) -> None:
        with self._condition:
            self.events.append(event)
            self._condition.notify_all()

    def wait_for(self, method: str, path: str, timeout: float = 5.0) -> dict[str, Any]:
        """Wait until an exact method/path event is observed."""

        deadline = time.monotonic() + timeout
        with self._condition:
            while True:
                for event in self.events:
                    if event.get("method") == method and event.get("path") == path:
                        return event
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise TimeoutError(f"fixture server did not observe {method} {path}")
                self._condition.wait(remaining)

    def delay_next_user_request(self, seconds: float) -> None:
        if seconds < 0:
            raise ValueError("delay must not be negative")
        with self._condition:
            self.next_user_delay = seconds

    def consume_user_delay(self) -> float:
        with self._condition:
            value = self.next_user_delay
            self.next_user_delay = 0.0
            return value


class DeveloperSurfaceServer(AbstractContextManager["DeveloperSurfaceServer"]):
    """Loopback-only fixture server with explicit auth and transfer-capability checks."""

    def __init__(self) -> None:
        self.state = DeveloperSurfaceState()
        self.fixture = load_v1_fixture()
        self._httpd: ThreadingHTTPServer | None = None
        self._thread: threading.Thread | None = None
        self.base_url = ""

    def __enter__(self) -> Self:
        fixture_server = self

        class Handler(BaseHTTPRequestHandler):
            protocol_version = "HTTP/1.1"

            def do_GET(self) -> None:  # noqa: N802
                fixture_server._handle(self)

            def do_POST(self) -> None:  # noqa: N802
                fixture_server._handle(self)

            def do_PUT(self) -> None:  # noqa: N802
                fixture_server._handle(self)

            def log_message(self, _format: str, *_args: object) -> None:
                return

        self._httpd = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        host, port = self._httpd.server_address[:2]
        host_text = host.decode("ascii") if isinstance(host, bytes) else host
        self.base_url = f"http://{host_text}:{port}"
        self.fixture = _replace_base_url(load_v1_fixture(), self.base_url)
        self._thread = threading.Thread(target=self._httpd.serve_forever, daemon=True)
        self._thread.start()
        return self

    def __exit__(
        self,
        _exc_type: type[BaseException] | None,
        _exc_value: BaseException | None,
        _traceback: TracebackType | None,
    ) -> None:
        if self._httpd is not None:
            self._httpd.shutdown()
            self._httpd.server_close()
        if self._thread is not None:
            self._thread.join(timeout=5)

    def _handle(self, request: BaseHTTPRequestHandler) -> None:
        parsed = urlsplit(request.path)
        path = parsed.path
        length = int(request.headers.get("content-length", "0"))
        body = request.rfile.read(length) if length else b""
        event = {
            "method": request.command,
            "path": path,
            "authorization": request.headers.get("authorization"),
            "idempotency_key": request.headers.get("idempotency-key"),
            "headers": {name.lower(): value for name, value in request.headers.items()},
            "body": body,
        }
        self.state.record(event)
        try:
            self._route(request, path, body)
        except (BrokenPipeError, ConnectionResetError):
            return

    def _route(self, request: BaseHTTPRequestHandler, path: str, body: bytes) -> None:
        fixture = self.fixture
        cli = _mapping(fixture["cli"])
        mcp = _mapping(fixture["mcp"])
        sdk = _mapping(fixture["sdk"])
        authorization = request.headers.get("authorization")

        if request.command == "GET" and path == "/healthz":
            self._send_json(
                request, 200, {"status": "ok", "service": "fixture", "source_revision": "v1"}
            )
            return
        if request.command == "GET" and path.startswith("/v1/shared-verifications/"):
            if authorization is not None:
                self._send_json(request, 400, {"detail": "anonymous route received bearer"})
            else:
                self._send_json(request, 200, sdk["anonymous_response"])
            return
        if path in {"/webhooks/clerk", "/webhooks/stripe"}:
            self._send_json(request, 500, {"detail": "provider ingress must be non-callable"})
            return

        valid_keys = {
            str(cli["valid_api_key"]),
            str(mcp["valid_api_key"]),
            str(sdk["valid_api_key"]),
        }
        bearer = authorization.removeprefix("Bearer ") if authorization else None

        if request.command == "GET" and path == "/v1/me":
            if bearer not in valid_keys:
                self._send_json(request, 401, {"detail": "authentication required"})
                return
            delay = self.state.consume_user_delay()
            if delay:
                time.sleep(delay)
            self._send_json(request, 200, cli["user_response"])
            return
        if request.command == "GET" and path == "/v1/assets":
            if bearer in {str(cli["scope_denied_api_key"]), str(mcp["forbidden_api_key"])}:
                error = (
                    cli["scope_error"]
                    if bearer == cli["scope_denied_api_key"]
                    else mcp["scope_error"]
                )
                self._send_json(
                    request,
                    int(error["status"]),
                    error,
                    headers={"x-request-id": str(error["request_id"])},
                )
                return
            if bearer not in valid_keys:
                self._send_json(request, 401, {"detail": "authentication required"})
                return
            self._send_json(
                request, 200, {"items": [mcp["asset"]["response"]], "next_cursor": None}
            )
            return
        if (
            request.command == "GET"
            and path.startswith("/v1/assets/")
            and not path.endswith("/download")
        ):
            if bearer not in valid_keys:
                self._send_json(request, 401, {"detail": "authentication required"})
                return
            asset_id = path.rsplit("/", 1)[-1]
            if asset_id == mcp["slow_asset"]["id"]:
                time.sleep(float(mcp["slow_asset"]["delay_seconds"]))
                self._send_json(request, 200, mcp["slow_asset"]["response"])
                return
            if asset_id == mcp["large_asset"]["id"]:
                self._send_json(
                    request,
                    200,
                    {
                        "asset_id": asset_id,
                        "padding": "x" * int(mcp["large_asset"]["payload_size"]),
                    },
                )
                return
            self._send_json(request, 200, mcp["asset"]["response"])
            return
        if request.command == "POST" and path == "/v1/verifications":
            if bearer not in valid_keys:
                self._send_json(request, 401, {"detail": "authentication required"})
                return
            expected = _mapping(mcp["verification"])
            if _json_body(body) != {"object_id": expected["object_id"]}:
                self._send_json(request, 422, {"detail": "fixture verification body mismatch"})
                return
            if request.headers.get("idempotency-key") != expected["idempotency_key"]:
                self._send_json(request, 422, {"detail": "fixture idempotency mismatch"})
                return
            self._send_json(request, 202, expected["response"])
            return
        if request.command == "POST" and path == "/v1/api-keys":
            expected = _mapping(cli["api_key_create"])
            if bearer != cli["valid_api_key"] or not request.headers.get("idempotency-key"):
                self._send_json(request, 403, {"detail": "fixture API-key request rejected"})
                return
            if _json_body(body) != expected["body"]:
                self._send_json(request, 422, {"detail": "fixture API-key body mismatch"})
                return
            self._send_json(request, 201, expected["response"])
            return
        if request.command == "GET" and path.startswith("/v1/jobs/"):
            if bearer not in valid_keys:
                self._send_json(request, 401, {"detail": "authentication required"})
                return
            self.state.job_calls += 1
            job = _mapping(cli["job"])
            response = (
                job["queued_response"] if self.state.job_calls == 1 else job["completed_response"]
            )
            self._send_json(request, 200, response)
            return
        if request.command == "POST" and path == "/v1/uploads":
            if bearer != cli["valid_api_key"]:
                self._send_json(request, 403, {"detail": "fixture upload auth rejected"})
                return
            upload = _mapping(cli["upload"])
            received = _json_body(body)
            if (
                received.get("byte_length") != upload["byte_length"]
                or received.get("sha256") != upload["sha256"]
            ):
                self._send_json(request, 422, {"detail": "fixture upload facts mismatch"})
                return
            self._send_json(request, 201, upload["create_response"])
            return
        if request.command == "PUT" and path == "/storage/upload":
            upload = _mapping(cli["upload"])
            capability = _mapping(upload["capability_header"])
            if (
                authorization is not None
                or request.headers.get(str(capability["name"])) != capability["value"]
            ):
                self._send_json(request, 403, {"detail": "fixture upload capability rejected"})
                return
            self.state.uploaded_bytes = body
            self._send_empty(request, 200)
            return
        if request.command == "POST" and path == "/v1/uploads/upl_fixture/complete":
            upload = _mapping(cli["upload"])
            expected_upload_bytes = base64.b64decode(str(upload["bytes_base64"]), validate=True)
            if bearer != cli["valid_api_key"] or not request.headers.get("idempotency-key"):
                self._send_json(request, 403, {"detail": "fixture completion rejected"})
                return
            if self.state.uploaded_bytes != expected_upload_bytes:
                self._send_json(request, 409, {"detail": "fixture upload bytes mismatch"})
                return
            self._send_json(request, 200, upload["complete_response"])
            return
        if request.command == "POST" and path == "/v1/uploads/upl_fixture/abort":
            self._send_json(request, 200, {"upload_id": "upl_fixture", "status": "aborted"})
            return
        download = _mapping(cli["download"])
        if request.command == "POST" and path == f"/v1/assets/{download['asset_id']}/download":
            if bearer != cli["valid_api_key"]:
                self._send_json(request, 403, {"detail": "fixture download auth rejected"})
                return
            self._send_json(request, 200, download["grant_response"])
            return
        if request.command == "GET" and path == "/storage/download":
            capability = _mapping(download["capability_header"])
            if (
                authorization is not None
                or request.headers.get(str(capability["name"])) != capability["value"]
            ):
                self._send_json(request, 403, {"detail": "fixture download capability rejected"})
                return
            payload = base64.b64decode(str(download["bytes_base64"]), validate=True)
            self._send_bytes(request, 200, payload)
            return
        if request.command == "GET" and path == "/storage/redirect":
            host_port = self.base_url.removeprefix("http://127.0.0.1")
            self._send_empty(
                request,
                302,
                headers={"location": f"http://localhost{host_port}/storage/redirect-target"},
            )
            return
        if request.command == "GET" and path == "/storage/redirect-target":
            self._send_empty(request, 200)
            return
        self._send_json(request, HTTPStatus.NOT_FOUND, {"detail": "fixture route not found"})

    @staticmethod
    def _send_json(
        request: BaseHTTPRequestHandler,
        status: int,
        value: object,
        *,
        headers: Mapping[str, str] | None = None,
    ) -> None:
        payload = json.dumps(value, separators=(",", ":"), sort_keys=True).encode("utf-8")
        DeveloperSurfaceServer._send_bytes(
            request,
            status,
            payload,
            headers={"content-type": "application/json", **dict(headers or {})},
        )

    @staticmethod
    def _send_empty(
        request: BaseHTTPRequestHandler,
        status: int,
        *,
        headers: Mapping[str, str] | None = None,
    ) -> None:
        DeveloperSurfaceServer._send_bytes(request, status, b"", headers=headers)

    @staticmethod
    def _send_bytes(
        request: BaseHTTPRequestHandler,
        status: int,
        payload: bytes,
        *,
        headers: Mapping[str, str] | None = None,
    ) -> None:
        request.send_response(status)
        for name, value in (headers or {}).items():
            request.send_header(name, value)
        request.send_header("content-length", str(len(payload)))
        request.end_headers()
        if payload:
            request.wfile.write(payload)


def _mapping(value: object) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise TypeError("fixture value must be an object")
    return value


def _json_body(value: bytes) -> dict[str, Any]:
    decoded = json.loads(value or b"{}")
    return _mapping(decoded)


def _replace_base_url(value: Any, base_url: str) -> Any:
    if isinstance(value, str):
        return value.replace("$BASE_URL", base_url)
    if isinstance(value, list):
        return [_replace_base_url(item, base_url) for item in value]
    if isinstance(value, dict):
        return {name: _replace_base_url(item, base_url) for name, item in value.items()}
    return copy.deepcopy(value)


def _serve_until_signalled() -> None:
    stopped = threading.Event()

    def stop(_signum: int, _frame: object) -> None:
        stopped.set()

    signal.signal(signal.SIGINT, stop)
    signal.signal(signal.SIGTERM, stop)
    with DeveloperSurfaceServer() as server:
        print(server.base_url, flush=True)
        stopped.wait()


if __name__ == "__main__":
    _serve_until_signalled()


__all__ = ["DeveloperSurfaceServer", "DeveloperSurfaceState", "load_v1_fixture"]
