# originalpictures-mcp: MCP server for C2PA Content Credentials, AI watermarking and verification

<!-- mcp-name: com.originalpictures/mcp -->

`originalpictures-mcp` is the official [Model Context Protocol](https://modelcontextprotocol.io)
server for [Original Pictures](https://originalpictures.com). It lets AI assistants and agents
(Claude Desktop, Claude Code, Cursor and other MCP clients) sign media with C2PA Content
Credentials, add an invisible watermark and fingerprints, and verify what a file declares about its
origin, through a narrow, scope-limited set of tools.

```sh
ORIGINALPICTURES_API_KEY=opk_... \
ORIGINALPICTURES_MCP_SCOPES=assets:read,jobs:read,recipes:read,verifications:read \
uvx originalpictures-mcp
```

It is an adapter over the typed [`originalpictures-sdk`](https://pypi.org/project/originalpictures-sdk/).
It exposes reviewed read workflows, two explicitly confirmed, idempotent writes (`sign` and
`create_verification`), and `verify_public`, the anonymous check of a local file against a public
verify page. It does not proxy arbitrary API routes and has no database, object-store, worker,
signer or infrastructure access.

## What it does

- **Sign with C2PA** (`sign`): starts a signing job for an uploaded asset. Every job writes a C2PA
  manifest (Content Credentials) following the C2PA Technical Specification 2.4; `watermark` and
  `fingerprint` choose whether an invisible watermark and perceptual fingerprints are added.
- **Declare AI generation**: `sign` accepts an `ai_declaration`, the kind of machine-readable
  marking described by EU AI Act Article 50(2) and the California AI Transparency Act (SB 942).
- **Verify** (`create_verification`, `get_verification`, `verify_public`): reports Content
  Credentials status, the declared origin and whether the account has a record of the file. It is
  never a judgement about the content itself.
- **Read your account** (`list_assets`, `list_jobs`, `get_usage`, `get_pricing` and more).

## Why use it

- **Least privilege.** No tool is enabled until its scope is in `ORIGINALPICTURES_MCP_SCOPES`. The
  API independently enforces the scopes granted to the key.
- **No surprise bills.** The two billable tools show a "Cost preview" in their description and in
  `_meta["com.originalpictures/billing"]`, require an exact `confirmation` string, and accept
  `max_billable_operations` to refuse a call that would start more billable work than you allow.
- **Clear tool hints.** Every tool sets `title`, `readOnlyHint`, `destructiveHint`,
  `idempotentHint` and `openWorldHint` explicitly.
- **No media in the conversation.** Media bytes never travel in a tool argument or result.

## Install

Run it without a separate install step:

```sh
uvx originalpictures-mcp
```

or install it:

```sh
pipx install originalpictures-mcp
```

Requires Python 3.12 or later.

## Quickstart

1. Create a dedicated API key in the [console](https://console.originalpictures.com/) under
   **API keys**, with only the scopes your assistant needs.
2. Add the server to your MCP client.

**Claude Desktop** (`claude_desktop_config.json`) and **Cursor** (`~/.cursor/mcp.json`) use the
same `mcpServers` entry:

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
      }
    }
  }
}
```

**Claude Code:**

```sh
claude mcp add originalpictures \
  -e ORIGINALPICTURES_API_KEY=opk_... \
  -e ORIGINALPICTURES_API_BASE_URL=https://api.originalpictures.com \
  -e ORIGINALPICTURES_MCP_SCOPES=assets:read,jobs:read \
  -- uvx originalpictures-mcp
```

3. Ask the assistant, for example: "List my five most recent signed assets."

## Tools

| Tool                                                               | Scope                | Notes                                                                                                                                       |
| ------------------------------------------------------------------ | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `get_current_user`                                                 | `identity:read`      |                                                                                                                                             |
| `list_assets`, `get_asset`, `list_receipts`, `get_signing_receipt` | `assets:read`        |                                                                                                                                             |
| `list_jobs`, `get_job`, `list_recipes`                             | `jobs:read`          |                                                                                                                                             |
| `get_recipe`                                                       | `recipes:read`       |                                                                                                                                             |
| `get_usage`                                                        | `billing:read`       |                                                                                                                                             |
| `get_pricing`                                                      | `billing:read`       | The versioned rates that price each billable operation.                                                                                     |
| `list_verifications`, `get_verification_history`                   | `verifications:read` |                                                                                                                                             |
| `get_verification`                                                 | `recovery:read`      |                                                                                                                                             |
| `create_verification`                                              | `verify:write`       | Billable. `confirmation` must be exactly `verify:<object_id>`.                                                                              |
| `sign`                                                             | `sign:write`         | Billable. Signs an uploaded `asset_id`; `watermark` and `fingerprint` are required flags. `confirmation` must be exactly `sign:<asset_id>`. |
| `verify_public`                                                    | `verify:write`       | STDIO only. Reads one absolute local file (at most 25 MB, no symlinks) and checks it against a verify page `slug`, without the API key.     |

`sign` refuses an `ai_declaration` together with `watermark: true` before calling the API:
"AI-generated mark needs a sign-only call (C2PA claim plan)". Media is uploaded with the SDKs, the
CLI or the REST API; `sign` starts one billable operation for the signature, plus one each for the
watermark and fingerprints when chosen.

## Examples

### 1. Read-only assistant (safe default)

```sh
ORIGINALPICTURES_API_KEY=opk_... \
ORIGINALPICTURES_MCP_SCOPES=assets:read,jobs:read,recipes:read,verifications:read \
uvx originalpictures-mcp
```

Prompts that work: "Which of my jobs failed this week and why?", "Show the signing receipt for
asset ast_…", "What does a watermark cost per image?" (with `billing:read`).

### 2. Signing assistant with a spend guard

Add `sign:write` to the scopes. When the assistant calls `sign`, it must pass
`confirmation: "sign:<asset_id>"`, and you can cap a call with `max_billable_operations`:

```json
{
  "asset_id": "ast_…",
  "watermark": true,
  "fingerprint": true,
  "idempotency_key": "mcp-sign-2026-11-07-001",
  "confirmation": "sign:ast_…",
  "max_billable_operations": 3
}
```

### 3. Check a local file against a public verify page

With `verify:write` in the scopes and the default STDIO transport, `verify_public` reads one
absolute local path and checks it against a page slug (for example `studio-nova`) without sending
the API key. The result states what the file declares about its origin and whether the page
owner's system has a record of it; show its `statement` with it. Each check is billed to the page
owner. It is not offered over HTTP, because a remote server must never read files on its own host.

### 4. Use the hosted server instead (no local install)

The same tools are served by the API at `https://api.originalpictures.com/mcp` (stateless
Streamable HTTP, `Authorization: Bearer opk_...`), with upload tools for agents that have no local
files. See [Hosted MCP server](https://docs.originalpictures.com/integrations/mcp-remote/).

### 5. Run your own HTTP endpoint on loopback

```sh
ORIGINALPICTURES_API_KEY=opk_... \
ORIGINALPICTURES_MCP_SCOPES=assets:read,jobs:read \
ORIGINALPICTURES_MCP_REMOTE_TOKEN='a-long-random-secret' \
originalpictures-mcp --transport http --host 127.0.0.1 --port 8000
```

The MCP bearer token is distinct from the upstream API key. Plaintext HTTP accepts only literal
IPv4/IPv6 loopback addresses or `localhost`; wildcard, LAN, public and other hostname bindings are
rejected before the server starts. Put a separately reviewed TLS terminator on the same host in
front of the loopback listener when remote access is required. Legacy SSE and WebSocket transports
are not supported.

## Configuration

| Variable                                        | Meaning                                                | Default                            |
| ----------------------------------------------- | ------------------------------------------------------ | ---------------------------------- |
| `ORIGINALPICTURES_API_KEY`                      | API key (required, server-side secret)                 | none                               |
| `ORIGINALPICTURES_MCP_SCOPES`                   | Comma-separated tool scope allowlist                   | empty: no tool enabled             |
| `ORIGINALPICTURES_API_BASE_URL`                 | API origin                                             | `https://api.originalpictures.com` |
| `ORIGINALPICTURES_MCP_REMOTE_TOKEN`             | Bearer token for `--transport http` (16 to 4096 chars) | none                               |
| `ORIGINALPICTURES_MCP_DEFAULT_DEADLINE_SECONDS` | Default per-call deadline                              | `20`                               |
| `ORIGINALPICTURES_MCP_MAX_DEADLINE_SECONDS`     | Largest deadline a call may ask for (at most 120)      | `120`                              |
| `ORIGINALPICTURES_MCP_MAX_OUTPUT_BYTES`         | Bound on one tool result (1 KiB to 1 MiB)              | `262144`                           |
| `ORIGINALPICTURES_MCP_MAX_PAGE_SIZE`            | Largest list page (1 to 100)                           | `100`                              |

Command-line options: `--transport` (`stdio`, the default, or `http`), `--host`, `--port` (default
`8000`) and `--path` (default `/mcp`).

## How it works

1. Your MCP client starts `originalpictures-mcp` (STDIO) or connects to it (HTTP).
2. The server lists only the tools whose scope is in `ORIGINALPICTURES_MCP_SCOPES`.
3. Each tool call is checked locally (scope, argument bounds, confirmation string, billable-operation
   cap), then sent through `originalpictures-sdk` to the API with your key.
4. The API enforces the key's own scopes, quotas and spend caps, and returns a bounded result
   (at most `ORIGINALPICTURES_MCP_MAX_OUTPUT_BYTES`).

## Troubleshooting

| Symptom                                     | Likely cause and fix                                                                            |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| The client shows no Original Pictures tools | `ORIGINALPICTURES_MCP_SCOPES` is empty or misspelled; list at least one scope.                  |
| `ORIGINALPICTURES_API_KEY is required`      | The key is missing from the client's `env` block.                                               |
| A tool answers with an authentication error | The key was revoked or expired; create a new one in the console.                                |
| A tool answers with a permission error      | The key lacks the scope the tool needs; the local allowlist does not grant scopes.              |
| `sign` is refused before any request        | `confirmation` is not exactly `sign:<asset_id>`, or the call exceeds `max_billable_operations`. |
| `--transport http` refuses to start         | The host is not loopback, or `ORIGINALPICTURES_MCP_REMOTE_TOKEN` is missing or short.           |
| `uvx` is not found                          | Install [uv](https://docs.astral.sh/uv/), or use `pipx install originalpictures-mcp`.           |

## FAQ

**Is this C2PA?**
Yes. Signing writes standard C2PA manifests (Content Credentials) that any C2PA-aware validator,
such as `c2patool`, can read. Original Pictures is listed on the C2PA Conforming Products List as a
generator product under the C2PA Conformance Program 0.2 (C2PA Technical Specification 2.4).

**Is Original Pictures audited?**
Original Pictures Technologies, Inc. holds ISO/IEC 27001:2022 certification for its information
security management system (GCAI, certificate GCAI-ISMS-PD91) and ISO/IEC 42001:2023 certification
for its AI management system (TNV). It has a SOC 2 Type I report from Percilchofe CPA LLC as of
19 October 2026, and runs a GDPR compliance program. The certifications cover management systems,
not this package. See [Security and compliance](https://originalpictures.com/security/).

**Does it store my media?**
The MCP server stores nothing itself. Files uploaded to Original Pictures are processed on private
servers, encrypted in transit and at rest, in isolated processing, and published outputs are kept
for the retention your API key selects. Operator views show metadata only, and emergency access is
audited. This is private server processing, not end-to-end encryption.

**What formats are supported?**
Embedded C2PA for JPEG, PNG, WebP, TIFF, AVIF, WAV, MP3, AAC (`.m4a`) and MP4 (H.264/AAC);
sign-only embedding for GIF, JPEG XL, SVG, DNG, HEIC/HEIF, QuickTime, AVI and FLAC; a sidecar
`.c2pa` manifest for PDF, EPUB, DOCX, text, fonts and ML model files. `list_recipes` shows what your
deployment offers.

**Can the assistant spend money without asking?**
Only if you add `sign:write` or `verify:write`, and even then each billable call needs the exact
confirmation string. Use `max_billable_operations` and a key with a spend cap.

**How much does it cost?**
See [pricing](https://originalpictures.com/pricing/), or ask the assistant to call `get_pricing`.

**How do I get an API key?**
Sign in to the [console](https://console.originalpictures.com/) and create one under **API keys**.

## Links

- Documentation: <https://docs.originalpictures.com/>
- Hosted MCP server: <https://docs.originalpictures.com/integrations/mcp-remote/>
- API reference: <https://docs.originalpictures.com/api/>
- Website: <https://originalpictures.com>
- Support: <hello@originalpictures.com>

## Licence

Licensed under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0); the
full text is in the `LICENSE` file shipped with this package. Copyright © 2026 Original Pictures
Technologies, Inc. The licence grants no rights to the Original Pictures name or logo.
