# Installing the Original Pictures MCP server

Instructions for an AI agent (for example Cline) installing this MCP server for a user.

The server is the Python package `originalpictures-mcp` (Python 3.12 or newer), run with `uvx`.
It exposes the Original Pictures API (C2PA signing, watermarking, fingerprinting and
verification of media) as MCP tools.

## 1. Ask the user for an API key

The user creates a dedicated key in the console at https://console.originalpictures.com/ under
**API keys**. Keys start with `opk_`. Never invent a key, and never print it back or write it
anywhere except the MCP client's configuration.

## 2. Choose the tool scopes

`ORIGINALPICTURES_MCP_SCOPES` is a comma-separated allowlist. With it empty, no tool is enabled.
Start read-only unless the user asks for signing:

```
assets:read,jobs:read,recipes:read,verifications:read
```

Add `sign:write` (billable signing) or `verify:write` (billable verification) only when the user
asks for them. `billing:read` enables usage and pricing; `identity:read` enables
`get_current_user`.

## 3. Add the server to the MCP settings

Check that `uvx` is available (`uvx --version`). If not, install uv:
https://docs.astral.sh/uv/getting-started/installation/

Add this entry to the client's MCP settings file (for Cline: `cline_mcp_settings.json`):

```json
{
  "mcpServers": {
    "originalpictures": {
      "command": "uvx",
      "args": ["originalpictures-mcp"],
      "env": {
        "ORIGINALPICTURES_API_KEY": "opk_...",
        "ORIGINALPICTURES_API_BASE_URL": "https://api.originalpictures.com",
        "ORIGINALPICTURES_MCP_SCOPES": "assets:read,jobs:read,recipes:read,verifications:read"
      },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

Leave `autoApprove` empty: `sign` and `create_verification` are billable and must be confirmed
by the user. Each billable call also requires a `confirmation` argument (`sign:<asset_id>` or
`verify:<object_id>`).

## 4. Check it works

Ask the server for something read-only, such as "List my five most recent signed assets"
(`list_assets`, needs `assets:read`). An authentication error means the key is wrong or revoked;
a tool missing from the list means its scope is not in `ORIGINALPICTURES_MCP_SCOPES`.

## No local install: hosted server

Clients that support remote Streamable HTTP servers can use
`https://api.originalpictures.com/mcp` with the header `Authorization: Bearer opk_...` instead of
the local package. See https://docs.originalpictures.com/integrations/mcp-remote/

## More

- Package README: [packages/mcp/README.md](packages/mcp/README.md) (all tools, scopes and settings)
- Documentation: https://docs.originalpictures.com/
