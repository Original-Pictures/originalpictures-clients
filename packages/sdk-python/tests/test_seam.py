"""Labelled seam check for the Python SDK root (not behavioral coverage)."""

from __future__ import annotations

import pytest

import originalpictures


@pytest.mark.seam
def test_sdk_python_is_complete() -> None:
    assert originalpictures.SDK_STATUS == "complete"
    assert originalpictures.SDK_TYPED_OPERATION_COUNT == 128
    assert originalpictures.SDK_EXECUTABLE_OPERATION_COUNT == 126
