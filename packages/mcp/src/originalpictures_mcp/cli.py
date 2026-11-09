"""`originalpictures-mcp` transport entrypoint."""

from __future__ import annotations

import argparse
from collections.abc import Sequence
from ipaddress import ip_address

from originalpictures_mcp.config import ConfigurationError, Settings
from originalpictures_mcp.server import create_server


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(prog="originalpictures-mcp")
    result.add_argument(
        "--transport",
        choices=("stdio", "http"),
        default="stdio",
        help="STDIO (default) or authenticated stateless Streamable HTTP.",
    )
    result.add_argument(
        "--host",
        default="127.0.0.1",
        help="Plaintext HTTP bind host; explicit loopback forms only.",
    )
    result.add_argument("--port", type=int, default=8000)
    result.add_argument("--path", default="/mcp")
    return result


def validate_plaintext_http_host(host: str) -> str:
    """Accept only literal loopback addresses or the special-use localhost name."""

    if host.casefold() == "localhost":
        return host
    if not host or host != host.strip() or "%" in host:
        raise ConfigurationError("plaintext HTTP transport must bind to a loopback host")
    try:
        address = ip_address(host)
    except ValueError as error:
        raise ConfigurationError("plaintext HTTP transport must bind to a loopback host") from error
    if not address.is_loopback or getattr(address, "ipv4_mapped", None) is not None:
        raise ConfigurationError("plaintext HTTP transport must bind to a loopback host")
    return host


def main(argv: Sequence[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        settings = Settings.from_env()
        if args.transport == "http" and settings.remote_token is None:
            raise ConfigurationError(
                "ORIGINALPICTURES_MCP_REMOTE_TOKEN is required for HTTP transport"
            )
        if args.transport == "http":
            validate_plaintext_http_host(args.host)
        if not (1 <= args.port <= 65535):
            raise ConfigurationError("port must be between 1 and 65535")
        if not args.path.startswith("/") or len(args.path) > 128:
            raise ConfigurationError("path must be an absolute bounded URL path")
    except ConfigurationError as error:
        parser().error(str(error))

    mcp = create_server(settings)
    if args.transport == "stdio":
        mcp.run(transport="stdio", show_banner=False)
    else:
        mcp.run(
            transport="http",
            host=args.host,
            port=args.port,
            path=args.path,
            stateless_http=True,
            show_banner=False,
        )
    return 0


__all__ = ["main", "parser", "validate_plaintext_http_host"]
