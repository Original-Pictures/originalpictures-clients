from __future__ import annotations

import inspect
import re
from pathlib import Path
from typing import get_args, get_type_hints

from originalpictures import PUBLIC_API_OPERATIONS, Client

from originalpictures_cli.operations import OPERATIONS


def test_cli_has_no_direct_http_internal_or_raw_operation_boundary() -> None:
    source_root = Path(__file__).parents[1] / "src" / "originalpictures_cli"
    combined = "\n".join(path.read_text(encoding="utf-8") for path in source_root.glob("*.py"))

    for forbidden in (
        "import httpx",
        "import requests",
        "boto3",
        "sqlalchemy",
        "psycopg",
        "_request_operation",
        'Command("raw"',
    ):
        assert forbidden not in combined
    assert all(not spec.method.startswith("receive_") for spec in OPERATIONS)
    assert all(spec.method != "request" for spec in OPERATIONS)


def test_reviewed_workflow_groups_are_present() -> None:
    groups = {spec.group for spec in OPERATIONS}
    assert {
        "assets",
        "billing",
        "capture",
        "governance",
        "history",
        "jobs",
        "keys",
        "shares",
        "sign",
        "uploads",
        "usage",
        "verifications",
        "webhooks",
    } <= groups


def test_explicit_commands_match_generated_sdk_methods_and_path_parameters() -> None:
    contracts = {contract.operation_id: contract for contract in PUBLIC_API_OPERATIONS}
    for spec in OPERATIONS:
        operation_id = re.sub(r"_([a-z])", lambda match: match.group(1).upper(), spec.method)
        contract = contracts[operation_id]
        assert hasattr(Client, spec.method)
        signature = inspect.signature(getattr(Client, spec.method))
        assert ("body" in signature.parameters) is spec.accepts_body
        if spec.accepts_body:
            body_default = signature.parameters["body"].default
            assert (body_default is inspect.Parameter.empty) is spec.body_required
        path_parameters = set(re.findall(r"{([^{}]+)}", contract.path))
        assert {field.api_name for field in spec.id_fields} == path_parameters


def test_idempotency_commands_match_required_public_contract_headers() -> None:
    # Derived from the generated contract rather than a hand-kept list, so a
    # contract that starts requiring Idempotency-Key fails here until the CLI
    # sends one.
    expected_methods = set()
    for spec in OPERATIONS:
        headers = get_type_hints(getattr(Client, spec.method)).get("headers")
        header_types = [arg for arg in get_args(headers) if arg is not type(None)]
        if any("Idempotency-Key" in getattr(arg, "__required_keys__", ()) for arg in header_types):
            expected_methods.add(spec.method)
    assert "create_verification" in expected_methods
    assert {spec.method for spec in OPERATIONS if spec.idempotent} == expected_methods
