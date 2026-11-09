from __future__ import annotations

import asyncio
import contextvars
import threading
import time

import pytest

import originalpictures
import originalpictures.helpers as helpers


def test_sign_and_verify_readiness_helpers_enforce_identifier_meaning() -> None:
    assert not originalpictures.sign_job_terminal(
        {"job_id": "job_aaaaaaaaaaaaaaaa", "state": "running", "result": None}
    )
    assert originalpictures.sign_job_terminal(
        {
            "job_id": "job_aaaaaaaaaaaaaaaa",
            "state": "completed",
            "result": {"verification_id": "vfy_aaaaaaaaaaaaaaaa"},
        }
    )
    with pytest.raises(ValueError, match="ready vfy_"):
        originalpictures.sign_job_terminal(
            {
                "job_id": "job_aaaaaaaaaaaaaaaa",
                "state": "completed",
                "result": {"verification_id": "vjob_aaaaaaaaaaaaaaaa"},
            }
        )

    assert not originalpictures.verification_job_terminal(
        {
            "verification_id": "vjob_aaaaaaaaaaaaaaaa",
            "state": "accepted",
            "evidence_id": None,
        }
    )
    assert originalpictures.verification_job_terminal(
        {
            "verification_id": "vjob_aaaaaaaaaaaaaaaa",
            "state": "completed",
            "evidence_id": "vfy_aaaaaaaaaaaaaaaa",
        }
    )
    with pytest.raises(ValueError, match="vjob_"):
        originalpictures.verification_job_terminal(
            {
                "verification_id": "vfy_aaaaaaaaaaaaaaaa",
                "state": "completed",
                "evidence_id": "vfy_aaaaaaaaaaaaaaaa",
            }
        )


def _join_workers(workers: list[threading.Thread]) -> None:
    for worker in workers:
        worker.join(timeout=1)
        assert not worker.is_alive()


def test_sync_poll_preserves_context_and_immediate_callback_errors() -> None:
    marker: contextvars.ContextVar[str] = contextvars.ContextVar("poll-marker", default="missing")
    token = marker.set("present")
    try:
        assert originalpictures.poll(lambda: marker.get(), lambda value: value == "present") == (
            "present"
        )
    finally:
        marker.reset(token)

    failure = ValueError("callback failed")

    def fail() -> object:
        raise failure

    with pytest.raises(ValueError) as captured:
        originalpictures.poll(fail, lambda _value: False)
    assert captured.value is failure


def test_sync_poll_bounds_in_flight_fetch_with_daemon_worker() -> None:
    started = threading.Event()
    release = threading.Event()
    workers: list[threading.Thread] = []

    def fetch() -> object:
        workers.append(threading.current_thread())
        started.set()
        release.wait(timeout=2)
        return object()

    before = time.monotonic()
    try:
        with pytest.raises(originalpictures.DeadlineExceededError):
            originalpictures.poll(fetch, lambda _value: False, timeout=0.02, interval=0)
    finally:
        release.set()
    assert time.monotonic() - before < 0.2
    assert started.is_set()
    assert workers and workers[0].daemon is True
    _join_workers(workers)


def test_sync_poll_checks_cancellation_during_in_flight_fetch() -> None:
    cancelled = threading.Event()
    release = threading.Event()
    workers: list[threading.Thread] = []

    def fetch() -> object:
        workers.append(threading.current_thread())
        release.wait(timeout=2)
        return object()

    def cancel_later() -> None:
        time.sleep(0.02)
        cancelled.set()

    threading.Thread(target=cancel_later, daemon=True).start()
    before = time.monotonic()
    try:
        with pytest.raises(originalpictures.CancelledError):
            originalpictures.poll(
                fetch,
                lambda _value: False,
                timeout=1,
                interval=0,
                cancelled=cancelled.is_set,
            )
    finally:
        release.set()
    assert time.monotonic() - before < 0.2
    _join_workers(workers)


def test_sync_poll_worker_capacity_is_hard_capped_without_queue_and_recovers() -> None:
    release = threading.Event()
    workers: list[threading.Thread] = []
    errors: list[type[BaseException]] = []

    def fetch() -> object:
        workers.append(threading.current_thread())
        release.wait(timeout=2)
        return object()

    try:
        for _ in range(originalpictures.MAX_SYNC_POLL_WORKERS + 3):
            try:
                originalpictures.poll(fetch, lambda _value: False, timeout=0.01, interval=0)
            except (
                originalpictures.DeadlineExceededError,
                originalpictures.PollingCapacityError,
            ) as error:
                errors.append(type(error))
        assert errors.count(originalpictures.DeadlineExceededError) == (
            originalpictures.MAX_SYNC_POLL_WORKERS
        )
        assert errors.count(originalpictures.PollingCapacityError) == 3
        assert len(workers) == originalpictures.MAX_SYNC_POLL_WORKERS
        assert all(worker.is_alive() and worker.daemon for worker in workers)
    finally:
        release.set()
        _join_workers(workers)

    time.sleep(0.01)
    assert len(workers) == originalpictures.MAX_SYNC_POLL_WORKERS
    assert originalpictures.poll(lambda: "recovered", lambda value: value == "recovered") == (
        "recovered"
    )


def test_sync_poll_publishes_capacity_before_waking_next_attempt(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    class PausingSemaphore:
        def __init__(self) -> None:
            self._semaphore = threading.BoundedSemaphore(1)
            self._lock = threading.Lock()
            self._release_count = 0
            self.first_release_entered = threading.Event()
            self.allow_first_release = threading.Event()

        def acquire(self, *, blocking: bool = True) -> bool:
            return self._semaphore.acquire(blocking=blocking)

        def release(self) -> None:
            with self._lock:
                self._release_count += 1
                release_count = self._release_count
            if release_count == 1:
                self.first_release_entered.set()
                assert self.allow_first_release.wait(timeout=1)
            self._semaphore.release()

    capacity = PausingSemaphore()
    monkeypatch.setattr(helpers, "_SYNC_POLL_CAPACITY", capacity)
    calls = 0
    result: list[bool] = []
    errors: list[BaseException] = []
    settled = threading.Event()

    def fetch() -> bool:
        nonlocal calls
        calls += 1
        return calls == 2

    def run_poll() -> None:
        try:
            result.append(
                originalpictures.poll(
                    fetch,
                    bool,
                    timeout=1,
                    interval=0,
                    max_interval=1,
                    max_attempts=2,
                )
            )
        except BaseException as error:
            errors.append(error)
        finally:
            settled.set()

    caller = threading.Thread(target=run_poll)
    caller.start()
    try:
        assert capacity.first_release_entered.wait(timeout=1)
        assert calls == 1
        assert not settled.wait(timeout=0.05)
        capacity.allow_first_release.set()
        caller.join(timeout=1)
        assert not caller.is_alive()
    finally:
        capacity.allow_first_release.set()
        caller.join(timeout=1)

    assert errors == []
    assert result == [True]
    assert calls == 2


def test_concurrent_sync_polls_never_start_or_queue_above_capacity() -> None:
    caller_count = originalpictures.MAX_SYNC_POLL_WORKERS + 4
    callers_ready = threading.Barrier(caller_count + 1)
    release = threading.Event()
    fetch_workers: list[threading.Thread] = []
    results: list[type[BaseException]] = []
    lock = threading.Lock()

    def fetch() -> object:
        with lock:
            fetch_workers.append(threading.current_thread())
        release.wait(timeout=2)
        return object()

    def call_poll() -> None:
        callers_ready.wait(timeout=1)
        try:
            originalpictures.poll(fetch, lambda _value: False, timeout=0.03, interval=0)
        except (
            originalpictures.DeadlineExceededError,
            originalpictures.PollingCapacityError,
        ) as error:
            with lock:
                results.append(type(error))

    callers = [threading.Thread(target=call_poll) for _ in range(caller_count)]
    for caller in callers:
        caller.start()
    callers_ready.wait(timeout=1)
    for caller in callers:
        caller.join(timeout=1)
        assert not caller.is_alive()
    try:
        assert results.count(originalpictures.DeadlineExceededError) == (
            originalpictures.MAX_SYNC_POLL_WORKERS
        )
        assert results.count(originalpictures.PollingCapacityError) == 4
        assert len(fetch_workers) == originalpictures.MAX_SYNC_POLL_WORKERS
    finally:
        release.set()
        _join_workers(fetch_workers)

    time.sleep(0.01)
    assert len(fetch_workers) == originalpictures.MAX_SYNC_POLL_WORKERS


def test_sync_poll_cancelled_predicate_interrupts_backoff_sleep() -> None:
    cancelled = threading.Event()

    def cancel_later() -> None:
        time.sleep(0.02)
        cancelled.set()

    threading.Thread(target=cancel_later, daemon=True).start()
    before = time.monotonic()
    with pytest.raises(originalpictures.CancelledError):
        originalpictures.poll(
            object,
            lambda _value: False,
            timeout=1,
            interval=0.5,
            cancelled=cancelled.is_set,
        )
    assert time.monotonic() - before < 0.1


@pytest.mark.asyncio
async def test_async_poll_bounds_and_cancels_never_resolving_fetch() -> None:
    fetch_cancelled = asyncio.Event()

    async def fetch() -> object:
        try:
            await asyncio.Future()
        finally:
            fetch_cancelled.set()

    before = time.monotonic()
    with pytest.raises(originalpictures.DeadlineExceededError):
        await originalpictures.poll_async(fetch, lambda _value: False, timeout=0.02, interval=0)
    assert time.monotonic() - before < 0.2
    await asyncio.wait_for(fetch_cancelled.wait(), timeout=0.2)


@pytest.mark.asyncio
async def test_async_poll_caller_cancellation_interrupts_fetch() -> None:
    fetch_cancelled = asyncio.Event()

    async def fetch() -> object:
        try:
            await asyncio.Future()
        finally:
            fetch_cancelled.set()

    task = asyncio.create_task(
        originalpictures.poll_async(fetch, lambda _value: False, timeout=1, interval=0)
    )
    await asyncio.sleep(0)
    task.cancel()
    with pytest.raises(asyncio.CancelledError):
        await task
    await asyncio.wait_for(fetch_cancelled.wait(), timeout=0.2)


@pytest.mark.asyncio
async def test_async_poll_cancelled_predicate_interrupts_backoff_sleep() -> None:
    cancelled = False

    async def fetch() -> object:
        return object()

    async def cancel_later() -> None:
        nonlocal cancelled
        await asyncio.sleep(0.02)
        cancelled = True

    cancel_task = asyncio.create_task(cancel_later())
    before = time.monotonic()
    with pytest.raises(originalpictures.CancelledError):
        await originalpictures.poll_async(
            fetch,
            lambda _value: False,
            timeout=1,
            interval=0.5,
            cancelled=lambda: cancelled,
        )
    assert time.monotonic() - before < 0.1
    await cancel_task


@pytest.mark.asyncio
async def test_native_async_cancellation_interrupts_backoff_without_leaked_task() -> None:
    fetched = asyncio.Event()

    async def fetch() -> object:
        fetched.set()
        return object()

    task = asyncio.create_task(
        originalpictures.poll_async(fetch, lambda _value: False, timeout=1, interval=0.5),
        name="poll-backoff-probe",
    )
    await asyncio.wait_for(fetched.wait(), timeout=0.2)
    await asyncio.sleep(0)
    before = time.monotonic()
    task.cancel()
    with pytest.raises(asyncio.CancelledError):
        await task
    assert time.monotonic() - before < 0.05
    assert task.done() and task.cancelled()
