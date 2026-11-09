"""Mechanical smoke for the README's exact Python example and its stated contract facts."""

import re
from pathlib import Path

import originalpictures

README = Path(__file__).resolve().parents[1] / "README.md"


def test_readme_python_example_compiles() -> None:
    source = README.read_text(encoding="utf-8").split("```python\n", 1)[1].split("\n```", 1)[0]
    compile(source, str(README), "exec")


def test_readme_operation_counts_match_generated_contract() -> None:
    prose = README.read_text(encoding="utf-8")
    stated_total = re.search(r"all\s+(\d+)\s+operations", prose)
    stated_consumer = re.search(r"the\s+(\d+)\s+consumer\s+operations", prose)
    assert stated_total is not None, "README no longer states the total operation count"
    assert stated_consumer is not None, "README no longer states the consumer operation count"
    assert int(stated_total.group(1)) == originalpictures.SDK_TYPED_OPERATION_COUNT
    assert int(stated_consumer.group(1)) == originalpictures.SDK_EXECUTABLE_OPERATION_COUNT
