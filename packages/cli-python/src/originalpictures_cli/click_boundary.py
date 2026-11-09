"""Root Click error boundary for deterministic machine-readable usage failures."""

from __future__ import annotations

import sys
from collections.abc import Sequence
from typing import Any

import click

from originalpictures_cli.exit_codes import ExitCode
from originalpictures_cli.output import canonical_json


class JsonUsageGroup(click.Group):
    """Preserve normal Click UX while making ``--json`` parsing errors canonical."""

    def main(
        self,
        args: Sequence[str] | None = None,
        prog_name: str | None = None,
        complete_var: str | None = None,
        standalone_mode: bool = True,
        windows_expand_args: bool = True,
        **extra: Any,
    ) -> Any:
        resolved_args = list(args) if args is not None else sys.argv[1:]
        json_requested = any(
            argument == "--json" or argument.startswith("--json=") for argument in resolved_args
        )
        try:
            result = super().main(
                args=resolved_args,
                prog_name=prog_name,
                complete_var=complete_var,
                standalone_mode=False,
                windows_expand_args=windows_expand_args,
                **extra,
            )
            if standalone_mode and isinstance(result, int):
                raise SystemExit(result)
            return result
        except click.ClickException as error:
            if json_requested:
                payload = {
                    "error": {
                        "exit_code": int(ExitCode.USAGE),
                        "kind": "usage",
                        "message": error.format_message(),
                    }
                }
                click.echo(canonical_json(payload), err=True)
            elif standalone_mode:
                error.show()
            if standalone_mode:
                raise SystemExit(int(ExitCode.USAGE)) from None
            raise
        except click.exceptions.Exit as error:
            if standalone_mode:
                raise SystemExit(error.exit_code) from None
            raise
        except click.Abort:
            if standalone_mode:
                click.echo("Aborted!", err=True)
                raise SystemExit(int(ExitCode.UNEXPECTED)) from None
            raise


__all__ = ["JsonUsageGroup"]
