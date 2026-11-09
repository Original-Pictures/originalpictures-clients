# originalpictures-mcp-scopes: scope vocabulary for the Original Pictures MCP server

`originalpictures-mcp-scopes` is the dependency-free, versioned list of API-key scopes that the
[Original Pictures](https://originalpictures.com) MCP server,
[`originalpictures-mcp`](https://pypi.org/project/originalpictures-mcp/), can be configured with.
The server and the Original Pictures Connect catalog import the same object, so the two cannot
drift.

```python
from originalpictures_mcp_scopes import SCOPE_CATALOG_VERSION, SUPPORTED_SCOPES, WRITE_SCOPES
```

Most people never install this package directly: `pip install originalpictures-mcp` or
`uvx originalpictures-mcp` pulls it in. Install it yourself when you build tooling that validates
an MCP configuration, generates a key request, or audits which tools an assistant can reach.

## What it does

Original Pictures signs media with C2PA Content Credentials, can add an invisible watermark and
perceptual fingerprints, and verifies what a file declares about its origin. Its MCP server lets AI
assistants use those features, but only through the scopes you allow. This package defines those
scopes:

| Scope                | Enables (in `originalpictures-mcp`)                                | Writes or bills |
| -------------------- | ------------------------------------------------------------------ | --------------- |
| `identity:read`      | `get_current_user`                                                 | no              |
| `assets:read`        | `list_assets`, `get_asset`, `list_receipts`, `get_signing_receipt` | no              |
| `jobs:read`          | `list_jobs`, `get_job`, `list_recipes`                             | no              |
| `recipes:read`       | `get_recipe`                                                       | no              |
| `billing:read`       | `get_usage`, `get_pricing`                                         | no              |
| `verifications:read` | `list_verifications`, `get_verification_history`                   | no              |
| `recovery:read`      | `get_verification`                                                 | no              |
| `sign:write`         | `sign` (C2PA signing, optional watermark and fingerprints)         | yes             |
| `verify:write`       | `create_verification`, `verify_public`                             | yes             |

- `SUPPORTED_SCOPES`: every scope an MCP tool can require (a `frozenset[str]`).
- `WRITE_SCOPES`: the scopes whose tools change state or start billable work (`sign:write`,
  `verify:write`). Every other scope is read-only.
- `SCOPE_CATALOG_VERSION`: `op.mcp-scopes.v2` since `sign:write` was added on 2026-10-19.

## Why use it

- One source of truth for scope names, shared by the server and the catalog.
- Versioned, so a change in the vocabulary is visible in `SCOPE_CATALOG_VERSION`.
- No runtime dependencies, typed (`py.typed`), safe to import anywhere.

## Install

```sh
pip install originalpictures-mcp-scopes
```

Requires Python 3.12 or later.

## Examples

### 1. Validate a configured allowlist

```python
from originalpictures_mcp_scopes import SUPPORTED_SCOPES

configured = {"assets:read", "jobs:read", "sign:wirte"}
unknown = configured - SUPPORTED_SCOPES
if unknown:
    raise SystemExit(f"unknown MCP scopes: {sorted(unknown)}")
```

### 2. Refuse a configuration that can spend money

```python
from originalpictures_mcp_scopes import WRITE_SCOPES

scopes = set("assets:read,jobs:read,recipes:read,verifications:read".split(","))
assert not scopes & WRITE_SCOPES, "this assistant must stay read-only"
```

### 3. Record which vocabulary a review covered

```python
from originalpictures_mcp_scopes import SCOPE_CATALOG_VERSION

print(f"reviewed against {SCOPE_CATALOG_VERSION}")  # reviewed against op.mcp-scopes.v2
```

## Configuration

None. The MCP server reads its allowlist from `ORIGINALPICTURES_MCP_SCOPES` (comma-separated); see
[`originalpictures-mcp`](https://pypi.org/project/originalpictures-mcp/).

## FAQ

**Is this C2PA?**
This package only names scopes. The MCP server it serves signs with standard C2PA Content
Credentials; Original Pictures is listed on the C2PA Conforming Products List as a generator
product under the C2PA Conformance Program 0.2.

**Is Original Pictures audited?**
Original Pictures Technologies, Inc. holds ISO/IEC 27001:2022 certification for its information
security management system (GCAI, certificate GCAI-ISMS-PD91) and ISO/IEC 42001:2023 certification
for its AI management system (TNV). It has a SOC 2 Type I report from Percilchofe CPA LLC as of
19 October 2026, and runs a GDPR compliance program. The certifications cover management systems,
not this package. See [Security and compliance](https://originalpictures.com/security/).

**Does it store or send anything?**
No. It is a few constants and makes no network calls.

**How do I get an API key with these scopes?**
In the [console](https://console.originalpictures.com/), under **API keys**. See
[pricing](https://originalpictures.com/pricing/) for what the billable tools cost.

## Links

- Documentation: <https://docs.originalpictures.com/>
- Hosted MCP server: <https://docs.originalpictures.com/integrations/mcp-remote/>
- Website: <https://originalpictures.com>
- Support: <hello@originalpictures.com>

## Licence

Licensed under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0); the
full text is in the `LICENSE` file shipped with this package. Copyright © 2026 Original Pictures
Technologies, Inc. The licence grants no rights to the Original Pictures name or logo.
