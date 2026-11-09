"""Bounded idempotency and polling helpers shared by SDK consumers."""

from __future__ import annotations

import asyncio
import contextvars
import re
import threading
import time
import uuid
from collections.abc import Awaitable, Callable, Mapping
from contextlib import suppress

from originalpictures.errors import CancelledError, DeadlineExceededError, PollingCapacityError

_IDEMPOTENCY_RE = re.compile(r"^[\x21-\x7e]{1,255}$")
_POLL_CANCELLATION_GRANULARITY = 0.01
MAX_SYNC_POLL_WORKERS = 8
_SYNC_POLL_CAPACITY = threading.BoundedSemaphore(MAX_SYNC_POLL_WORKERS)
_SIGN_JOB_ID_RE = re.compile(r"^job_[a-z2-7]{16}$")
_VERIFY_JOB_ID_RE = re.compile(r"^vjob_[a-z2-7]{16}$")
_VERIFY_EVIDENCE_ID_RE = re.compile(r"^vfy_[a-z2-7]{16}$")
_SIGN_TERMINAL_STATES = frozenset({"completed", "failed", "rejected", "canceled", "expired"})
_SIGN_STATES = _SIGN_TERMINAL_STATES | frozenset(
    {"accepted", "queued", "running", "cancel_requested"}
)
_VERIFY_TERMINAL_STATES = frozenset({"completed", "failed"})
_VERIFY_STATES = _VERIFY_TERMINAL_STATES | frozenset({"accepted", "running"})


def idempotency_key(prefix: str = "sdk") -> str:
    """Create a printable, non-secret idempotency key."""

    key = f"{prefix}-{uuid.uuid4()}"
    return validate_idempotency_key(key)


def validate_idempotency_key(value: str) -> str:
    """Validate the public API's safe idempotency-key envelope."""

    if not _IDEMPOTENCY_RE.fullmatch(value):
        raise ValueError("idempotency key must be 1-255 printable ASCII characters")
    return value


def sign_job_terminal(snapshot: Mapping[str, object]) -> bool:
    """Validate one Sign snapshot and report whether its ``job_`` is terminal.

    A completed Sign snapshot must carry ready immutable ``vfy_`` evidence. It is
    a protocol error—not a polling state—when that identifier is absent or has
    the asynchronous public-Verify ``vjob_`` shape.
    """

    job_id = snapshot.get("job_id")
    state = snapshot.get("state")
    result = snapshot.get("result")
    if not isinstance(job_id, str) or _SIGN_JOB_ID_RE.fullmatch(job_id) is None:
        raise ValueError("Sign snapshot requires a job_ identifier")
    if not isinstance(state, str) or state not in _SIGN_STATES:
        raise ValueError("Sign snapshot has an unsupported lifecycle state")
    if state == "completed":
        if not isinstance(result, Mapping):
            raise ValueError("completed Sign snapshot requires a result")
        evidence_id = result.get("verification_id")
        if (
            not isinstance(evidence_id, str)
            or _VERIFY_EVIDENCE_ID_RE.fullmatch(evidence_id) is None
        ):
            raise ValueError("completed Sign result requires ready vfy_ evidence")
    elif result is not None:
        raise ValueError("non-completed Sign snapshot cannot expose a result")
    return state in _SIGN_TERMINAL_STATES


def verification_job_terminal(snapshot: Mapping[str, object]) -> bool:
    """Validate one pollable ``vjob_`` snapshot and report terminal readiness."""

    job_id = snapshot.get("verification_id")
    state = snapshot.get("state")
    evidence_id = snapshot.get("evidence_id")
    if not isinstance(job_id, str) or _VERIFY_JOB_ID_RE.fullmatch(job_id) is None:
        raise ValueError("public Verify snapshot requires a vjob_ identifier")
    if not isinstance(state, str) or state not in _VERIFY_STATES:
        raise ValueError("public Verify snapshot has an unsupported lifecycle state")
    if state == "completed":
        if (
            not isinstance(evidence_id, str)
            or _VERIFY_EVIDENCE_ID_RE.fullmatch(evidence_id) is None
        ):
            raise ValueError("completed public Verify job requires ready vfy_ evidence")
    elif evidence_id is not None:
        raise ValueError("non-completed public Verify job cannot expose vfy_ evidence")
    return state in _VERIFY_TERMINAL_STATES


def poll[T](
    fetch: Callable[[], T],
    done: Callable[[T], bool],
    *,
    timeout: float = 60.0,
    interval: float = 1.0,
    max_interval: float = 5.0,
    max_attempts: int = 120,
    cancelled: Callable[[], bool] | None = None,
) -> T:
    """Poll with a wall deadline, bounded attempts and cooperative cancellation.

    Each synchronous fetch runs with copied context in one of a fixed number of daemon
    worker slots. Python cannot stop an arbitrary synchronous callback; one that ignores
    its own I/O timeout may retain its slot after this function returns. Calls fail fast
    with :class:`PollingCapacityError` when every slot is still occupied.
    """

    _validate_polling(timeout, interval, max_interval, max_attempts)
    deadline = time.monotonic() + timeout
    delay = interval
    for attempt in range(max_attempts):
        if cancelled is not None and cancelled():
            raise CancelledError("polling cancelled")
        value = _fetch_sync(fetch, deadline, cancelled)
        if done(value):
            return value
        remaining = deadline - time.monotonic()
        if remaining <= 0 or attempt + 1 >= max_attempts:
            break
        _sleep_sync(min(delay, remaining), cancelled)
        delay = min(delay * 1.5, max_interval)
    raise DeadlineExceededError("polling deadline exceeded")


async def poll_async[T](
    fetch: Callable[[], Awaitable[T]],
    done: Callable[[T], bool],
    *,
    timeout: float = 60.0,
    interval: float = 1.0,
    max_interval: float = 5.0,
    max_attempts: int = 120,
    cancelled: Callable[[], bool] | None = None,
) -> T:
    """Async counterpart to :func:`poll`."""

    _validate_polling(timeout, interval, max_interval, max_attempts)
    deadline = time.monotonic() + timeout
    delay = interval
    for attempt in range(max_attempts):
        if cancelled is not None and cancelled():
            raise CancelledError("polling cancelled")
        value = await _fetch_async(fetch, deadline, cancelled)
        if done(value):
            return value
        remaining = deadline - time.monotonic()
        if remaining <= 0 or attempt + 1 >= max_attempts:
            break
        await _sleep_async(min(delay, remaining), cancelled)
        delay = min(delay * 1.5, max_interval)
    raise DeadlineExceededError("polling deadline exceeded")


def _validate_polling(timeout: float, interval: float, max_interval: float, attempts: int) -> None:
    if timeout <= 0 or interval < 0 or max_interval <= 0 or attempts <= 0:
        raise ValueError("polling bounds must be positive")


def _fetch_sync[T](
    fetch: Callable[[], T],
    deadline: float,
    cancelled: Callable[[], bool] | None,
) -> T:
    completed = threading.Event()
    values: list[T] = []
    failures: list[BaseException] = []
    context = contextvars.copy_context()

    if not _SYNC_POLL_CAPACITY.acquire(blocking=False):
        raise PollingCapacityError("synchronous polling worker capacity exhausted")

    def run() -> None:
        try:
            values.append(context.run(fetch))
        except BaseException as error:
            failures.append(error)
        finally:
            _SYNC_POLL_CAPACITY.release()
            completed.set()

    worker = threading.Thread(target=run, name="originalpictures-poll-fetch", daemon=True)
    try:
        worker.start()
    except BaseException:
        _SYNC_POLL_CAPACITY.release()
        raise
    while True:
        if cancelled is not None and cancelled():
            raise CancelledError("polling cancelled")
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise DeadlineExceededError("polling deadline exceeded")
        if completed.wait(min(remaining, _POLL_CANCELLATION_GRANULARITY)):
            break
    if failures:
        raise failures[0]
    return values[0]


async def _fetch_async[T](
    fetch: Callable[[], Awaitable[T]],
    deadline: float,
    cancelled: Callable[[], bool] | None,
) -> T:
    task: asyncio.Future[T] = asyncio.ensure_future(fetch())
    try:
        while True:
            if cancelled is not None and cancelled():
                task.cancel()
                _consume_task_result(task)
                raise CancelledError("polling cancelled")
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                task.cancel()
                _consume_task_result(task)
                raise DeadlineExceededError("polling deadline exceeded")
            done, _pending = await asyncio.wait(
                {task}, timeout=min(remaining, _POLL_CANCELLATION_GRANULARITY)
            )
            if done:
                return task.result()
    except asyncio.CancelledError:
        task.cancel()
        _consume_task_result(task)
        raise


def _consume_task_result[T](task: asyncio.Future[T]) -> None:
    def consume(done: asyncio.Future[T]) -> None:
        with suppress(asyncio.CancelledError, Exception):
            done.exception()

    task.add_done_callback(consume)


def _sleep_sync(duration: float, cancelled: Callable[[], bool] | None) -> None:
    deadline = time.monotonic() + duration
    while True:
        if cancelled is not None and cancelled():
            raise CancelledError("polling cancelled")
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            return
        time.sleep(min(remaining, _POLL_CANCELLATION_GRANULARITY))


async def _sleep_async(duration: float, cancelled: Callable[[], bool] | None) -> None:
    deadline = time.monotonic() + duration
    while True:
        if cancelled is not None and cancelled():
            raise CancelledError("polling cancelled")
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            return
        await asyncio.sleep(min(remaining, _POLL_CANCELLATION_GRANULARITY))


__all__ = [
    "MAX_SYNC_POLL_WORKERS",
    "idempotency_key",
    "poll",
    "poll_async",
    "sign_job_terminal",
    "validate_idempotency_key",
    "verification_job_terminal",
]
