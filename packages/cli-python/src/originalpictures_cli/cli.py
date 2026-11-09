"""Click command tree for Original Pictures public workflows."""

from __future__ import annotations

import click

from originalpictures_cli import __version__
from originalpictures_cli.click_boundary import JsonUsageGroup
from originalpictures_cli.config import ConfigStore
from originalpictures_cli.operations import register_operation_commands
from originalpictures_cli.output import Output
from originalpictures_cli.runtime import Runtime, invoke
from originalpictures_cli.workflows import register_workflow_commands


@click.group(
    cls=JsonUsageGroup,
    context_settings={"help_option_names": ["-h", "--help"], "max_content_width": 100},
    help="Reviewed Original Pictures public API workflows.",
    epilog="Root options must appear before the command group (for example: --json jobs get).",
)
@click.version_option(__version__, prog_name="Original Pictures CLI")
@click.option("--json", "json_mode", is_flag=True, help="Emit deterministic JSON on stdout.")
@click.option("--profile", help="Named local profile (or ORIGINALPICTURES_PROFILE).")
@click.option("--api-url", help="One-run API URL override (or ORIGINALPICTURES_API_URL).")
@click.option(
    "--timeout",
    type=click.FloatRange(0.1, 600.0),
    default=30.0,
    show_default=True,
    help="Per-request SDK timeout in seconds.",
)
@click.option(
    "--max-response-bytes",
    type=click.IntRange(1024, 64 * 1024 * 1024),
    default=16 * 1024 * 1024,
    show_default=True,
    help="Hard SDK JSON response bound.",
)
@click.pass_context
def cli(
    ctx: click.Context,
    json_mode: bool,
    profile: str | None,
    api_url: str | None,
    timeout: float,
    max_response_bytes: int,
) -> None:
    """Initialize a lazy SDK runtime; no network call occurs for help/config commands."""

    output = Output(json_mode=json_mode)
    if isinstance(ctx.obj, Runtime):
        runtime = ctx.obj
        runtime.output = output
        runtime.profile_name = profile or runtime.profile_name
        runtime.api_url = api_url or runtime.api_url
        runtime.timeout = timeout
        runtime.max_response_bytes = max_response_bytes
    else:
        runtime = Runtime(
            store=ConfigStore(),
            output=output,
            profile_name=profile,
            api_url=api_url,
            timeout=timeout,
            max_response_bytes=max_response_bytes,
        )
    ctx.obj = runtime
    ctx.call_on_close(runtime.close)


@cli.group("auth", help="Store and inspect API credentials without argv secrets.")
def auth_group() -> None:
    pass


@auth_group.command("login", help="Store an API credential in the operating-system keyring.")
@click.option(
    "--token-stdin",
    is_flag=True,
    help="Read one credential line from stdin instead of hidden interactive input.",
)
@click.pass_obj
def auth_login(runtime: Runtime, token_stdin: bool) -> None:
    if token_stdin:
        token = click.get_text_stream("stdin").readline(4098)
        if len(token) > 4097 or (token and not token.endswith("\n")):
            raise click.UsageError("credential input exceeds the 4096-character limit")
        token = token.rstrip("\r\n")
    else:
        token = click.prompt("API credential", hide_input=True, confirmation_prompt=True)
    profile_name = runtime.profile_name or runtime.store.default_profile
    invoke(runtime, lambda: runtime.store.set_api_key(profile_name, token))
    runtime.output.success({"credential_stored": True, "profile": profile_name})


@auth_group.command("logout", help="Remove a profile credential from the keyring.")
@click.pass_obj
def auth_logout(runtime: Runtime) -> None:
    profile_name = runtime.profile_name or runtime.store.default_profile
    removed = invoke(runtime, lambda: runtime.store.delete_api_key(profile_name))
    runtime.output.success({"credential_removed": bool(removed), "profile": profile_name})


@auth_group.command("status", help="Show credential presence and source, never its value.")
@click.pass_obj
def auth_status(runtime: Runtime) -> None:
    profile = invoke(runtime, lambda: runtime.profile)
    runtime.output.success(
        {
            "api_url": profile.api_url,
            "credential_configured": profile.api_key is not None,
            "credential_source": profile.credential_source,
            "profile": profile.name,
        }
    )


@cli.group("config", help="Manage non-secret local profile configuration.")
def config_group() -> None:
    pass


@config_group.command("set-api-url", help="Set a profile API URL (credentials are rejected).")
@click.argument("url")
@click.pass_obj
def config_set_api_url(runtime: Runtime, url: str) -> None:
    profile_name = runtime.profile_name or runtime.store.default_profile
    profile = invoke(runtime, lambda: runtime.store.set_api_url(profile_name, url))
    runtime.output.success({"api_url": profile.api_url, "profile": profile.name})


@config_group.command("show", help="Show the selected non-secret profile configuration.")
@click.pass_obj
def config_show(runtime: Runtime) -> None:
    profile = invoke(runtime, lambda: runtime.profile)
    runtime.output.success(
        {
            "api_url": profile.api_url,
            "credential_configured": profile.api_key is not None,
            "profile": profile.name,
        }
    )


@config_group.command("profiles", help="List configured profiles without credential values.")
@click.pass_obj
def config_profiles(runtime: Runtime) -> None:
    profiles = invoke(runtime, runtime.store.list_profiles)
    runtime.output.success({"profiles": profiles})


def main() -> None:
    """Console script entry point."""

    cli()


register_operation_commands(cli)
register_workflow_commands(cli)

__all__ = ["cli", "main"]
