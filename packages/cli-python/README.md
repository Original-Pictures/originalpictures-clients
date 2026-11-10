# originalpictures-cli: command-line tool for C2PA Content Credentials, AI watermarking and verification

`originalpictures-cli` installs the `originalpictures` command: a safe, scriptable command-line
interface to the [Original Pictures](https://originalpictures.com) API. Sign files with C2PA
Content Credentials, add an invisible watermark and perceptual fingerprints, declare AI generation,
verify what a file declares about its origin, and download signed outputs, from a terminal or a CI
job.

```sh
pipx install originalpictures-cli
export ORIGINALPICTURES_API_URL=https://api.originalpictures.com
originalpictures auth login            # paste the key at the hidden prompt
originalpictures capabilities show
```

It delegates every network operation to [`originalpictures-sdk`](https://pypi.org/project/originalpictures-sdk/);
it has no raw-route command and no internal-service access.

## What it does

- **C2PA signing** (`sign accept`): every job writes a C2PA manifest (Content Credentials) following
  the C2PA Technical Specification 2.4, recording the file's declared origin.
- **Invisible watermark and fingerprinting** (`--watermark`, `--fingerprint`): optional, so a copy
  whose metadata was stripped can still be matched to your record.
- **AI-generation declaration** (`--ai-generated`): the kind of machine-readable marking that EU AI
  Act Article 50(2) and the California AI Transparency Act (SB 942) describe.
- **Verification** (`verifications create`, `verifications get`): Content Credentials status,
  certificate chain and your account's records, reported as declared origin with reason codes.
- **Uploads and downloads** (`uploads file`, `assets download`) with streaming, size bounds and
  SHA-256 integrity checks.
- **Jobs** (`jobs wait`): polls with a bounded deadline and clean Ctrl-C cancellation.

## Why use it

- **No secrets on the command line.** Credentials come only from `ORIGINALPICTURES_API_KEY`, a
  hidden prompt, or standard input (`auth login --token-stdin`). The operating-system keyring
  stores them; the config file holds only non-secret profile settings.
- **Scriptable.** `--json` gives deterministic compact JSON on stdout and canonical JSON errors on
  stderr, with stable exit codes (below).
- **No hand-written JSON for signing.** `sign accept` builds the request from flags.
- **Safe by default.** Bounded timeouts and response sizes, fresh idempotency keys for operations
  that need them, and request bodies read from bounded files or stdin, never from argv.

## Install

```sh
pipx install originalpictures-cli
```

or

```sh
uv tool install originalpictures-cli
```

Requires Python 3.12 or later. The command is `originalpictures`. (Earlier pre-release builds also
installed an `op` alias; it was removed because `op` is the 1Password CLI's command.)

## Quickstart

1. Create an API key in the [console](https://console.originalpictures.com/) under **API keys**
   (keys start with `opk_`).
2. Point the CLI at the API and store the key:

   ```sh
   originalpictures config set-api-url https://api.originalpictures.com
   originalpictures auth login
   originalpictures auth status
   ```

   The CLI's built-in default API URL is a local development address, so set the URL once per
   profile as above, or export `ORIGINALPICTURES_API_URL` in each shell.

3. Upload, sign and wait:

   ```sh
   originalpictures --json uploads file photo.jpg --media-type image/jpeg > upload.json
   ASSET=$(jq -r .completion.asset_id upload.json)

   originalpictures --json sign accept --asset "$ASSET" --no-watermark --no-fingerprint > job.json
   originalpictures --json jobs wait "$(jq -r .job_id job.json)" --poll-timeout 300 > signed.json
   ```

4. Download the signed file (checked against the published length and SHA-256):

   ```sh
   originalpictures assets download "$(jq -r .result.asset_id signed.json)" photo.signed.jpg
   ```

Root options (`--json`, `--profile`, `--api-url`, `--timeout`, `--max-response-bytes`) must come
before the command group, for example `originalpictures --json jobs get job_...`.

## Signing flags

`sign accept` builds the whole request from flags. Every job signs with C2PA;
`--watermark/--no-watermark` and `--fingerprint/--no-fingerprint` choose what else it adds. Send
both every time.

| Flag                                 | Request field                                                            |
| ------------------------------------ | ------------------------------------------------------------------------ |
| `--asset ID`                         | `asset_id`                                                               |
| `--watermark` / `--no-watermark`     | `watermark`                                                              |
| `--fingerprint` / `--no-fingerprint` | `fingerprint`                                                            |
| `--watermark-algorithm ID`           | `watermark_algorithm` (needs `--watermark`)                              |
| `--watermark-strength LEVEL`         | `watermark_strength`: `subtle`, `balanced`, `robust`                     |
| `--fingerprint-algorithm ID`         | `fingerprint_algorithms` (repeatable)                                    |
| `--ai-generated`                     | `ai_declaration` (needs `--software-agent NAME`)                         |
| `--software-agent-version V`         | `ai_declaration.software_agent_version`                                  |
| `--digital-source-type T`            | `ai_declaration.digital_source_type` (default `trainedAlgorithmicMedia`) |
| `--creator ID`                       | `creator_id`                                                             |
| `--template ID`                      | `template_id` (a saved workflow template)                                |
| `--recipe ID`                        | `recipe_id` (advanced; needed only for a sidecar format)                 |

`--input FILE` (or `-` for standard input) still supplies a JSON body; a flag and the same field in
the body must agree. `--strength` is an alias of `--watermark-strength`.

## Examples

### 1. C2PA Content Credentials only

```sh
originalpictures sign accept --asset ast_… --no-watermark --no-fingerprint
```

### 2. Invisible watermark and fingerprints, then C2PA

```sh
originalpictures sign accept --asset ast_… --watermark --fingerprint \
  --watermark-algorithm pixelseal --watermark-strength subtle
```

`originalpictures capabilities show` lists the media types, recipes, watermark and fingerprint
algorithms your deployment offers.

### 3. Declare AI generation (sign-only)

```sh
originalpictures sign accept --asset ast_… --no-watermark --fingerprint \
  --ai-generated --software-agent "Studio Nova Imagine" --software-agent-version 2.0
```

`--ai-generated` with `--watermark` is refused before any request is sent: "AI-generated mark needs
a sign-only call (C2PA claim plan)".

### 4. Verify a file

```sh
originalpictures --json uploads file received.jpg --media-type image/jpeg > upload.json
jq '{object_id: .completion.asset_object_id}' upload.json \
  | originalpictures --json verifications create --input - > verification.json
originalpictures --json verifications get "$(jq -r .verification_id verification.json)"
```

The result reports what the file declares about its origin and whether your account has a record
of it. It is never a judgement about the content itself.

### 5. CI pipeline (GitHub Actions, GitLab, Jenkins)

```sh
# The key comes from the CI secret store as an environment variable, never as an argument.
export ORIGINALPICTURES_API_KEY="$OP_SIGNING_KEY"
export ORIGINALPICTURES_API_URL=https://api.originalpictures.com
for file in build/images/*.png; do
  asset=$(originalpictures --json uploads file "$file" --media-type image/png | jq -r .completion.asset_id)
  originalpictures --json sign accept --asset "$asset" --watermark --fingerprint | jq -r .job_id
done
```

### 6. Several accounts with profiles

```sh
originalpictures --profile staging config set-api-url https://api.originalpictures.com
originalpictures --profile staging auth login --token-stdin < staging-key.txt
originalpictures --profile staging --json user show
originalpictures config profiles
```

## Configuration

| Variable or option                       | Meaning                                                         |
| ---------------------------------------- | --------------------------------------------------------------- |
| `ORIGINALPICTURES_API_KEY`               | API key; takes precedence over the keyring credential           |
| `ORIGINALPICTURES_API_URL` / `--api-url` | API origin for one run; overrides the profile's URL             |
| `ORIGINALPICTURES_PROFILE` / `--profile` | Named local profile (default `default`)                         |
| `--timeout SECONDS`                      | Per-request timeout (default 30, at most 600)                   |
| `--max-response-bytes N`                 | Hard JSON response bound (default 16 MiB)                       |
| `--json`                                 | Deterministic JSON on stdout, canonical JSON errors on stderr   |
| `config set-api-url URL`                 | Store the profile's API URL (URLs carrying credentials refused) |

Mutation bodies use `--input FILE` and explicit operation parameters use `--parameters FILE`; `-`
reads the JSON object from standard input. Run `originalpictures --help` for every command group:
`assets`, `auth`, `billing`, `capabilities`, `capture`, `config`, `governance`, `history`, `jobs`,
`keys`, `shares`, `sign`, `uploads`, `usage`, `user`, `verifications`, `webhooks`.

## Stable exit codes

| Code | Meaning                                           |
| ---: | ------------------------------------------------- |
|    0 | Success                                           |
|    1 | Unexpected local failure                          |
|    2 | Command usage error                               |
|    3 | Missing or invalid local configuration/credential |
|    4 | API or local input validation failure             |
|    5 | Authentication failed                             |
|    6 | Permission denied                                 |
|    7 | Resource not found                                |
|    8 | State or idempotency conflict                     |
|    9 | Rate limited                                      |
|   10 | Deadline exceeded                                 |
|   11 | Transport or service unavailable                  |
|   12 | Transfer integrity failure                        |
|   13 | Configured response/transfer bound exceeded       |
|  130 | Cancelled by Ctrl-C                               |

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
Uploaded files are processed on Original Pictures' private servers, encrypted in transit and at
rest, in isolated processing. Published outputs are kept for the retention your API key selects
(new accounts default to 72 hours). Operator views show metadata only, and emergency access is
audited. This is private server processing, not end-to-end encryption.

**What formats are supported?**
Embedded C2PA for JPEG, PNG, WebP, TIFF, AVIF, WAV, MP3, AAC (`.m4a`) and MP4 (H.264/AAC);
sign-only embedding for GIF, JPEG XL, SVG, DNG, HEIC/HEIF, QuickTime, AVI and FLAC; a sidecar
`.c2pa` manifest for PDF, EPUB, DOCX, text, fonts and ML model files. Run
`originalpictures capabilities show` for the live list.

**Why was the `op` command removed?**
`op` is the 1Password CLI. Installing a second `op` would shadow it on your `PATH`.

**How much does it cost?**
See [pricing](https://originalpictures.com/pricing/).

**How do I get an API key?**
Sign in to the [console](https://console.originalpictures.com/) and create one under **API keys**.

## Links

- Documentation: <https://docs.originalpictures.com/>
- API reference: <https://docs.originalpictures.com/api/>
- Website: <https://originalpictures.com>
- Python SDK: <https://pypi.org/project/originalpictures-sdk/>
- Support: <hello@originalpictures.com>

## Licence

Licensed under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0); the
full text is in the `LICENSE` file shipped with this package. Copyright © 2026 Original Pictures
Technologies, Inc. The licence grants no rights to the Original Pictures name or logo.
