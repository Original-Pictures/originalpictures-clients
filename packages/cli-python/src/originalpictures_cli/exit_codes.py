"""Documented process exit codes for scripts and operators."""

from enum import IntEnum


class ExitCode(IntEnum):
    SUCCESS = 0
    UNEXPECTED = 1
    USAGE = 2
    CONFIGURATION = 3
    VALIDATION = 4
    AUTHENTICATION = 5
    PERMISSION = 6
    NOT_FOUND = 7
    CONFLICT = 8
    RATE_LIMIT = 9
    DEADLINE = 10
    UNAVAILABLE = 11
    INTEGRITY = 12
    TOO_LARGE = 13
    CANCELLED = 130


__all__ = ["ExitCode"]
