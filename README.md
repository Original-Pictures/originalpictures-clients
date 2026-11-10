# Original Pictures client packages

Client libraries and tools for the [Original Pictures](https://originalpictures.com) API:
sign media with C2PA Content Credentials, add invisible watermarks, fingerprint and verify
media, and show AI disclosures.

Documentation: <https://docs.originalpictures.com>

## Packages

| Directory | Package | Registry | Install |
| --- | --- | --- | --- |
| [`packages/sdk-python`](packages/sdk-python) | `originalpictures-sdk` | PyPI | `pip install originalpictures-sdk` |
| [`packages/cli-python`](packages/cli-python) | `originalpictures-cli` | PyPI | `pipx install originalpictures-cli` |
| [`packages/mcp`](packages/mcp) | `originalpictures-mcp` | PyPI | `uvx originalpictures-mcp` |
| [`packages/mcp-scopes`](packages/mcp-scopes) | `originalpictures-mcp-scopes` | PyPI | `pip install originalpictures-mcp-scopes` |
| [`packages/disclosure-python`](packages/disclosure-python) | `originalpictures-disclosure` | PyPI | `pip install originalpictures-disclosure` |
| [`packages/sdk-typescript`](packages/sdk-typescript) | `@originalpictures/sdk` | npm | `npm install @originalpictures/sdk` |
| [`packages/verify-embed`](packages/verify-embed) | `@originalpictures/verify` | npm | `npm install @originalpictures/verify` |
| [`packages/disclosure`](packages/disclosure) | `@originalpictures/disclosure` | npm | `npm install @originalpictures/disclosure` |

Each package's own README covers usage. `packages/typescript-config` and
`packages/eslint-config` are private build and lint configuration; they are never
published.

## Source of truth

This repository is a public mirror. The packages are developed in a private repository
and exported here. Please report issues in this repository's issue tracker.

`packages/contracts/openapi/openapi.yaml` (the public API description the SDKs are
generated from) and the A2A agent card under `apps/marketing-site` and
`docs/distribution` are included because package tests check against them. One test,
`packages/verify-embed/tests/tokens.test.ts`, compares with design tokens that exist only
in the private repository; the release workflow excludes it by name and it runs in the
private repository's CI.

## Building and testing

Requirements: Python 3.12 with [uv](https://docs.astral.sh/uv/), and Node.js 24 with
pnpm 11 (via `corepack`).

```sh
uv sync --all-packages --all-groups --frozen
uv run --frozen --package originalpictures-sdk pytest packages/sdk-python
uv build --package originalpictures-sdk

corepack pnpm install --frozen-lockfile
corepack pnpm --filter @originalpictures/sdk test
```

## Releases

`.github/workflows/publish-sdk.yml` builds, checks and publishes one package per run.
It runs only when started by hand (a dry run unless `dry_run` is unticked) or on a
release tag such as `sdk-python-v1.0.0`. Each package publishes from its own job behind
a protected environment, using PyPI trusted publishing and npm provenance.

## Licence

The client packages are licensed under the [Apache License 2.0](LICENSE). The licence
grants no rights to the Original Pictures name or logos.
