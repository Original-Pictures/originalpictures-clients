"""Explicit public operation commands backed only by generated SDK methods."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import click

from originalpictures_cli.runtime import Runtime, invoke

MAX_INPUT_BYTES = 1024 * 1024


@dataclass(frozen=True)
class IdField:
    cli_name: str
    api_name: str


@dataclass(frozen=True)
class BodyValueOption:
    """A single-valued flag that fills one scalar field of the request body."""

    flag: str
    body_field: str
    help: str
    choices: tuple[str, ...] | None = None
    aliases: tuple[str, ...] = ()

    @property
    def destination(self) -> str:
        return self.flag.lstrip("-").replace("-", "_") + "_value"


@dataclass(frozen=True)
class BodyListOption:
    """A repeatable flag that fills one list field of the request body."""

    flag: str
    body_field: str
    help: str

    @property
    def destination(self) -> str:
        return self.flag.lstrip("-").replace("-", "_") + "_values"


@dataclass(frozen=True)
class BodyFlagOption:
    """An on/off pair (``--x/--no-x``) that fills one boolean field of the request body.

    Neither form given leaves the field out, so the request file (or the API's own
    default) decides.
    """

    flag: str
    body_field: str
    help: str

    @property
    def destination(self) -> str:
        return self.flag.lstrip("-").replace("-", "_") + "_flag"

    @property
    def declaration(self) -> str:
        name = self.flag.lstrip("-")
        return f"--{name}/--no-{name}"


#: The digital source types an AI declaration may state (AiDeclarationRequest).
AI_DIGITAL_SOURCE_TYPES: tuple[str, ...] = (
    "trainedAlgorithmicMedia",
    "compositeWithTrainedAlgorithmicMedia",
    "compositeSynthetic",
)
#: The console's text for the one combination the C2PA claim plan refuses.
AI_MARK_REQUIRES_SIGN_ONLY = "AI-generated mark needs a sign-only call (C2PA claim plan)"


@dataclass(frozen=True)
class OperationSpec:
    group: str
    command: str
    method: str
    help: str
    body_required: bool = False
    id_fields: tuple[IdField, ...] = ()
    idempotent: bool = False
    authentication_required: bool = True
    # The contract accepts a body but does not require one (`anyOf: [schema, null]`).
    body_optional: bool = False
    body_list_options: tuple[BodyListOption, ...] = ()
    body_value_options: tuple[BodyValueOption, ...] = ()
    body_flag_options: tuple[BodyFlagOption, ...] = ()
    # `--ai-generated` and its companions build the request's `ai_declaration`.
    ai_declaration_options: bool = False

    @property
    def has_body_options(self) -> bool:
        return bool(
            self.body_list_options
            or self.body_value_options
            or self.body_flag_options
            or self.ai_declaration_options
        )

    @property
    def accepts_body(self) -> bool:
        return self.body_required or self.body_optional


def _id(cli_name: str, api_name: str | None = None) -> IdField:
    return IdField(cli_name, api_name or cli_name)


OPERATIONS = (
    OperationSpec("user", "show", "get_current_user", "Show the authenticated user."),
    OperationSpec("uploads", "create", "create_upload", "Create an upload grant.", True),
    OperationSpec(
        "uploads", "abort", "abort_upload", "Abort an upload.", id_fields=(_id("upload_id"),)
    ),
    OperationSpec(
        "uploads",
        "complete",
        "complete_upload",
        "Complete an uploaded object.",
        True,
        (_id("upload_id"),),
        True,
    ),
    OperationSpec(
        "sign",
        "accept",
        "accept_signing_job",
        "Accept a signing job. Every job signs with C2PA; send both --watermark/--no-watermark "
        "and --fingerprint/--no-fingerprint to choose what else it adds.",
        True,
        (),
        True,
        body_flag_options=(
            BodyFlagOption(
                "--watermark",
                "watermark",
                "Embed an invisible watermark before signing (--no-watermark: none).",
            ),
            BodyFlagOption(
                "--fingerprint",
                "fingerprint",
                "Also keep server-side fingerprints for recovery (--no-fingerprint: none).",
            ),
        ),
        body_list_options=(
            BodyListOption(
                "--fingerprint-algorithm",
                "fingerprint_algorithms",
                "A fingerprint to compute (repeatable); replaces the default set. Needs "
                "--fingerprint. See `capabilities show` for the ids offered per media type.",
            ),
        ),
        body_value_options=(
            BodyValueOption("--asset", "asset_id", "The ast_ asset to sign."),
            BodyValueOption(
                "--watermark-algorithm",
                "watermark_algorithm",
                "The watermark to embed. Needs --watermark. See `capabilities show` for the "
                "ids per media type.",
            ),
            BodyValueOption(
                "--watermark-strength",
                "watermark_strength",
                "How hard the watermark may be embedded. Needs --watermark.",
                choices=("subtle", "balanced", "robust"),
                aliases=("--strength",),
            ),
            BodyValueOption("--creator", "creator_id", "An enrolled crid_ creator to attribute."),
            BodyValueOption(
                "--template",
                "template_id",
                "A saved wft_ workflow template filling the fields this request omits.",
            ),
            BodyValueOption(
                "--recipe",
                "recipe_id",
                "Advanced: an exact recipe instead of the flags. Needed only for a sidecar format.",
            ),
        ),
        ai_declaration_options=True,
    ),
    OperationSpec(
        "capabilities",
        "show",
        "get_capabilities",
        "Show supported media types, recipes, watermarks and fingerprints.",
    ),
    OperationSpec("jobs", "list", "list_jobs", "List jobs."),
    OperationSpec("jobs", "get", "get_job", "Get a job.", id_fields=(_id("job_id"),)),
    OperationSpec("jobs", "cancel", "cancel_job", "Cancel a job.", True, (_id("job_id"),), True),
    OperationSpec("verifications", "list", "list_verifications", "List verifications."),
    OperationSpec(
        "verifications", "create", "create_verification", "Create a verification.", True, (), True
    ),
    OperationSpec(
        "verifications",
        "get",
        "get_verification",
        "Get a verification.",
        id_fields=(_id("verification_id"),),
    ),
    OperationSpec(
        "verifications",
        "history",
        "get_verification_history",
        "Get verification recovery history.",
        id_fields=(_id("verification_id"),),
    ),
    OperationSpec(
        "verifications",
        "report-create",
        "create_verification_report",
        "Create a verification report.",
        True,
        (_id("verification_id"),),
    ),
    OperationSpec(
        "verifications",
        "report-get",
        "get_verification_report",
        "Get a verification report.",
        id_fields=(_id("report_id"),),
    ),
    OperationSpec(
        "shares",
        "create",
        "create_verification_share",
        "Create a verification share.",
        True,
        (_id("verification_id"),),
        idempotent=True,
    ),
    OperationSpec(
        "shares",
        "get",
        "get_shared_verification",
        "Read a shared verification.",
        id_fields=(_id("token"),),
        authentication_required=False,
    ),
    OperationSpec(
        "shares",
        "close",
        "close_verification_share",
        "Close a verification share.",
        True,
        (_id("share_id"),),
    ),
    OperationSpec("assets", "list", "list_assets", "List assets."),
    OperationSpec("assets", "get", "get_asset", "Get an asset.", id_fields=(_id("asset_id"),)),
    OperationSpec("keys", "list", "list_api_keys", "List API keys."),
    OperationSpec("keys", "create", "create_api_key", "Create an API key.", True, (), True),
    OperationSpec(
        "keys",
        "revoke",
        "revoke_api_key",
        "Revoke an API key.",
        id_fields=(_id("api_key_id"),),
        idempotent=True,
    ),
    OperationSpec(
        "keys", "rotate", "rotate_api_key", "Rotate an API key.", True, (_id("api_key_id"),), True
    ),
    OperationSpec("history", "receipts", "list_receipts", "List signing receipts."),
    OperationSpec(
        "history",
        "receipt",
        "get_signing_receipt",
        "Get a signing receipt.",
        id_fields=(_id("receipt_id"),),
    ),
    OperationSpec("history", "recipes", "list_recipes", "List recovery recipes."),
    OperationSpec(
        "history", "recipe", "get_recipe", "Get a recovery recipe.", id_fields=(_id("recipe_id"),)
    ),
    OperationSpec(
        "history", "release-snapshot", "release_history_snapshot", "Release a history snapshot."
    ),
    OperationSpec("webhooks", "list", "list_webhook_endpoints", "List webhook endpoints."),
    OperationSpec(
        "webhooks",
        "create",
        "create_webhook_endpoint",
        "Create a webhook endpoint.",
        True,
        (),
        True,
    ),
    OperationSpec(
        "webhooks",
        "update",
        "update_webhook_endpoint",
        "Update a webhook endpoint.",
        True,
        (_id("endpoint_id"),),
    ),
    OperationSpec(
        "webhooks",
        "delete",
        "delete_webhook_endpoint",
        "Delete a webhook endpoint.",
        id_fields=(_id("endpoint_id"),),
    ),
    OperationSpec(
        "webhooks",
        "disable",
        "disable_webhook_endpoint",
        "Disable a webhook endpoint.",
        id_fields=(_id("endpoint_id"),),
    ),
    OperationSpec(
        "webhooks",
        "rotate-secret",
        "rotate_webhook_endpoint_secret",
        "Rotate a webhook signing secret.",
        id_fields=(_id("endpoint_id"),),
        idempotent=True,
        body_optional=True,
    ),
    OperationSpec(
        "webhooks",
        "deliveries",
        "list_webhook_deliveries",
        "List endpoint deliveries.",
        id_fields=(_id("endpoint_id"),),
    ),
    OperationSpec(
        "webhooks",
        "attempts",
        "list_webhook_delivery_attempts",
        "List delivery attempts.",
        id_fields=(_id("delivery_id"),),
    ),
    OperationSpec(
        "webhooks",
        "replay-delivery",
        "replay_webhook_delivery",
        "Replay a delivery.",
        id_fields=(_id("delivery_id"),),
        idempotent=True,
    ),
    OperationSpec(
        "webhooks",
        "replay-event",
        "replay_webhook_event",
        "Replay an event.",
        id_fields=(_id("event_id"),),
        idempotent=True,
    ),
    OperationSpec("usage", "show", "get_usage", "Show usage and quota."),
    OperationSpec("billing", "account", "get_billing_account", "Show the billing account."),
    OperationSpec(
        "billing", "checkout", "create_billing_checkout_intent", "Create a checkout intent.", True
    ),
    OperationSpec(
        "billing", "portal", "create_billing_portal_intent", "Create a billing portal intent.", True
    ),
    OperationSpec("governance", "audit", "query_governance_audit", "Query audit records."),
    OperationSpec(
        "governance",
        "deletion-create",
        "create_governance_deletion",
        "Create a deletion.",
        True,
        idempotent=True,
    ),
    OperationSpec(
        "governance",
        "deletion-get",
        "get_governance_deletion",
        "Get a deletion.",
        id_fields=(_id("deletion_id"),),
    ),
    OperationSpec(
        "governance",
        "export-create",
        "create_governance_export",
        "Create an export.",
        idempotent=True,
    ),
    OperationSpec(
        "governance",
        "export-get",
        "get_governance_export",
        "Get an export.",
        id_fields=(_id("export_id"),),
    ),
    OperationSpec("governance", "legal-holds", "list_governance_legal_holds", "List legal holds."),
    OperationSpec(
        "capture", "admit", "create_capture_admission", "Admit trusted capture evidence.", True
    ),
    OperationSpec(
        "capture",
        "challenge",
        "create_capture_admission_challenge",
        "Issue a capture challenge.",
        True,
        idempotent=True,
    ),
    OperationSpec(
        "capture",
        "get",
        "get_capture_admission",
        "Get capture admission evidence.",
        id_fields=(_id("capture_id", "capture_admission_id"),),
    ),
    OperationSpec(
        "capture",
        "enroll-start",
        "create_capture_identity_enrollment",
        "Start device enrollment.",
        True,
        idempotent=True,
    ),
    OperationSpec(
        "capture",
        "enroll-complete",
        "create_capture_identity",
        "Complete device enrollment.",
        True,
    ),
    OperationSpec(
        "capture",
        "device-revoke",
        "revoke_capture_identity",
        "Revoke a capture device.",
        id_fields=(_id("device_id", "capture_identity_id"),),
    ),
)


def register_operation_commands(root: click.Group) -> None:
    groups: dict[str, click.Group] = {}
    for spec in OPERATIONS:
        group = groups.get(spec.group)
        if group is None:
            group = click.Group(spec.group, help=f"{spec.group.title()} public API workflows.")
            root.add_command(group)
            groups[spec.group] = group
        group.add_command(_make_command(spec))


def _make_command(spec: OperationSpec) -> click.Command:
    parameters: list[click.Parameter] = [
        click.Argument([field.cli_name], required=True) for field in spec.id_fields
    ]
    if spec.accepts_body:
        parameters.append(
            click.Option(
                ["--input", "input_source"],
                # Flags can build the whole body, so a file is then optional.
                required=spec.body_required and not spec.has_body_options,
                metavar="FILE",
                help="Bounded JSON request body; use - for stdin."
                + ("" if spec.body_required and not spec.has_body_options else " Optional."),
            )
        )
    for option in spec.body_list_options:
        parameters.append(
            click.Option(
                [option.flag, option.destination],
                multiple=True,
                metavar="ID",
                help=option.help,
            )
        )
    for flag_option in spec.body_flag_options:
        parameters.append(
            click.Option(
                [flag_option.declaration, flag_option.destination],
                default=None,
                help=flag_option.help,
            )
        )
    if spec.ai_declaration_options:
        parameters.extend(_ai_declaration_parameters())
    for value_option in spec.body_value_options:
        parameters.append(
            click.Option(
                [value_option.flag, *value_option.aliases, value_option.destination],
                type=click.Choice(value_option.choices) if value_option.choices else None,
                metavar=None if value_option.choices else "ID",
                help=value_option.help,
            )
        )
    parameters.append(
        click.Option(
            ["--parameters", "parameter_source"],
            metavar="FILE",
            help="Bounded JSON path/query parameters; use - for stdin.",
        )
    )

    def callback(**kwargs: Any) -> None:
        runtime = _runtime()
        body = (
            _read_json_object(kwargs.pop("input_source"), "request body")
            if spec.accepts_body
            else None
        )
        for option in spec.body_list_options:
            values = list(kwargs.pop(option.destination))
            if not values:
                continue
            body = dict(body or {})
            existing = body.get(option.body_field)
            if existing is not None and existing != values:
                raise click.UsageError(
                    f"{option.body_field!r} conflicts with the explicit {option.flag} flags"
                )
            body[option.body_field] = values
        for value_option in spec.body_value_options:
            value = kwargs.pop(value_option.destination)
            if value is None:
                continue
            body = dict(body or {})
            current = body.get(value_option.body_field)
            if current is not None and current != value:
                raise click.UsageError(
                    f"{value_option.body_field!r} conflicts with the explicit "
                    f"{value_option.flag} flag"
                )
            body[value_option.body_field] = value
        for flag_option in spec.body_flag_options:
            flag = kwargs.pop(flag_option.destination)
            if flag is None:
                continue
            body = dict(body or {})
            current = body.get(flag_option.body_field)
            if current is not None and current != flag:
                raise click.UsageError(
                    f"{flag_option.body_field!r} conflicts with the explicit "
                    f"{flag_option.flag} flag"
                )
            body[flag_option.body_field] = flag
        if spec.ai_declaration_options:
            body = _apply_ai_declaration(body, kwargs)
        if spec.body_required and body is None:
            raise click.UsageError("pass --input FILE or the request flags")
        provided_parameters = _read_json_object(kwargs.pop("parameter_source"), "parameters")
        operation_parameters = dict(provided_parameters or {})
        for field in spec.id_fields:
            value = kwargs.pop(field.cli_name)
            existing = operation_parameters.get(field.api_name)
            if existing is not None and existing != value:
                raise click.UsageError(
                    f"{field.api_name!r} conflicts with the explicit {field.cli_name} argument"
                )
            operation_parameters[field.api_name] = value

        def run() -> Any:
            client = runtime.client(authentication_required=spec.authentication_required)
            method = getattr(client, spec.method)
            call_kwargs: dict[str, Any] = {}
            if operation_parameters:
                call_kwargs["parameters"] = operation_parameters
            if spec.body_required or body is not None:
                call_kwargs["body"] = body
            if spec.idempotent:
                from originalpictures import idempotency_key

                call_kwargs["headers"] = {"Idempotency-Key": idempotency_key("cli")}
            return method(**call_kwargs)

        result = invoke(runtime, run)
        runtime.output.success(result)

    return click.Command(spec.command, callback=callback, params=parameters, help=spec.help)


def _ai_declaration_parameters() -> list[click.Parameter]:
    return [
        click.Option(
            ["--ai-generated", "ai_generated"],
            is_flag=True,
            default=False,
            help="Declare that a generative model produced the file (sends ai_declaration). "
            "Needs --no-watermark and --software-agent.",
        ),
        click.Option(
            ["--software-agent", "software_agent_name"],
            metavar="NAME",
            help="With --ai-generated: the generating software.",
        ),
        click.Option(
            ["--software-agent-version", "software_agent_version"],
            metavar="VERSION",
            help="With --ai-generated: the generating software's version.",
        ),
        click.Option(
            ["--digital-source-type", "digital_source_type"],
            type=click.Choice(AI_DIGITAL_SOURCE_TYPES),
            default=None,
            help="With --ai-generated: the declared source type (default trainedAlgorithmicMedia).",
        ),
    ]


def _apply_ai_declaration(
    body: dict[str, Any] | None, kwargs: dict[str, Any]
) -> dict[str, Any] | None:
    """Build ``ai_declaration`` from ``--ai-generated`` and refuse what the API refuses.

    The API is the authority; this only turns the one refusal a flag user is most
    likely to hit (a watermark with an AI declaration) into a local usage error that
    says why, before any network call.
    """

    declared = kwargs.pop("ai_generated")
    companions = {
        "software_agent_name": kwargs.pop("software_agent_name"),
        "software_agent_version": kwargs.pop("software_agent_version"),
        "digital_source_type": kwargs.pop("digital_source_type"),
    }
    if not declared:
        flags = {
            "software_agent_name": "--software-agent",
            "software_agent_version": "--software-agent-version",
            "digital_source_type": "--digital-source-type",
        }
        named = [flags[key] for key, value in companions.items() if value is not None]
        if named:
            raise click.UsageError(f"{named[0]} needs --ai-generated")
        return body
    body = dict(body or {})
    if body.get("ai_declaration") is not None:
        raise click.UsageError("'ai_declaration' conflicts with the explicit --ai-generated flag")
    if not companions["software_agent_name"]:
        raise click.UsageError("--ai-generated needs --software-agent NAME")
    if body.get("watermark") is True:
        raise click.UsageError(
            f"{AI_MARK_REQUIRES_SIGN_ONLY}: use --no-watermark with --ai-generated"
        )
    declaration = {
        "digital_source_type": companions["digital_source_type"] or AI_DIGITAL_SOURCE_TYPES[0],
        "software_agent_name": companions["software_agent_name"],
    }
    if companions["software_agent_version"]:
        declaration["software_agent_version"] = companions["software_agent_version"]
    body["ai_declaration"] = declaration
    return body


def _runtime() -> Runtime:
    runtime = click.get_current_context().find_object(Runtime)
    if runtime is None:
        raise RuntimeError("CLI runtime was not initialized")
    return runtime


def read_json_object(source: str, label: str) -> dict[str, Any]:
    value = _read_json_object(source, label)
    if value is None:
        raise click.UsageError(f"{label} is required")
    return value


def _read_json_object(source: str | None, label: str) -> dict[str, Any] | None:
    if source is None:
        return None
    if source == "-":
        raw = click.get_text_stream("stdin").read(MAX_INPUT_BYTES + 1)
    else:
        path = Path(source)
        try:
            if not path.is_file():
                raise click.UsageError(f"{label} path is not a regular file")
            if path.stat().st_size > MAX_INPUT_BYTES:
                raise click.UsageError(f"{label} exceeds the 1 MiB limit")
            raw = path.read_text(encoding="utf-8")
        except OSError as error:
            raise click.UsageError(f"could not read {label}") from error
    if len(raw.encode("utf-8")) > MAX_INPUT_BYTES:
        raise click.UsageError(f"{label} exceeds the 1 MiB limit")
    try:
        value = json.loads(raw)
    except json.JSONDecodeError as error:
        raise click.UsageError(f"{label} must be valid JSON") from error
    if not isinstance(value, dict):
        raise click.UsageError(f"{label} must be a JSON object")
    return value


__all__ = [
    "AI_DIGITAL_SOURCE_TYPES",
    "AI_MARK_REQUIRES_SIGN_ONLY",
    "MAX_INPUT_BYTES",
    "OPERATIONS",
    "BodyFlagOption",
    "BodyListOption",
    "BodyValueOption",
    "register_operation_commands",
    "read_json_object",
]
