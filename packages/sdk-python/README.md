# originalpictures-sdk: Python SDK for C2PA Content Credentials, AI watermarking and verification

`originalpictures-sdk` is the official, typed Python client for the
[Original Pictures](https://originalpictures.com) API. Use it to sign images, audio, video and
documents with C2PA Content Credentials, add an invisible watermark and perceptual fingerprints,
and verify what a file declares about its origin.

It covers all 128 operations in the public API contract with generated types. Its synchronous and
asynchronous clients execute the 126 consumer operations; the two provider-ingress operations
(Clerk and Stripe callbacks) stay typed but are deliberately non-callable, because their signatures
cover exact raw bytes that a JSON client must not re-encode.

```python
from originalpictures import Client

with Client(base_url="https://dev-api.originalpictures.com", api_key="opk_...") as client:
    me = client.get_current_user()
    capabilities = client.get_capabilities()
```

## What it does

- **C2PA signing.** Every signing job writes a C2PA manifest (Content Credentials) into the file,
  or beside it for sidecar formats, following the C2PA Technical Specification 2.4. The manifest
  records the file's declared origin: who signed it, with which tool, and what actions were
  declared.
- **Invisible watermark.** Optionally embeds an invisible watermark before signing, so a copy
  whose metadata was stripped can still be matched to your record.
- **Perceptual fingerprinting.** Optionally keeps server-side fingerprints of the signed output
  for recovery by similarity.
- **AI-generation declaration.** Records that a generative model produced the file
  (`c2pa.created` with an IPTC digital source type such as `trainedAlgorithmicMedia`). This is
  the kind of machine-readable marking that EU AI Act Article 50(2) and the California AI
  Transparency Act (SB 942, as amended by AB 853) describe.
- **Verification.** Checks Content Credentials, the certificate chain and your account's records,
  and reports the file's declared origin with reason codes. It is never a judgement about the
  content itself.
- **Public verify pages.** `verify_public()` checks a file against an account's public verify
  page without an API key.
- **Webhooks.** `verify_webhook()` checks Standard Webhooks signatures on raw request bodies.

## Why use it

- Fully typed (`py.typed`): every request body, parameter and response is a `TypedDict`, so
  mypy and Pyright catch a misspelled field before the request is sent.
- Safe transfers: `upload_file` and `download_file` stream bytes and finish only after the
  expected length and SHA-256 match. API authorization is never forwarded to upload or download
  URLs.
- Bounded by default: response size limits, request timeouts, and polling helpers with a wall
  deadline and cooperative cancellation.
- Stable, typed errors (`AuthenticationError`, `RateLimitError`, `ConflictError` and others)
  carrying the API's reason `code` and `request_id`.
- One dependency: `httpx`.

## Install

```sh
pip install originalpictures-sdk
```

Or with uv:

```sh
uv add originalpictures-sdk
```

Requires Python 3.12 or later.

## Quickstart: sign a file

Get an API key from the [console](https://console.originalpictures.com/) (keys start with
`opk_`). Upload the bytes, then accept a signing job for the asset.

```python
import hashlib
import os
from pathlib import Path

from originalpictures import Client, idempotency_key, poll, sign_job_terminal

path = Path("photo.jpg")
digest = hashlib.sha256(path.read_bytes()).hexdigest()

with Client(
    base_url="https://dev-api.originalpictures.com",
    api_key=os.environ["ORIGINALPICTURES_API_KEY"],
) as client:
    upload = client.create_upload(
        body={
            "byte_length": path.stat().st_size,
            "declared_media_type": "image/jpeg",
            "mode": "single",
            "sha256": digest,
        }
    )
    target = upload.get("upload")
    if target is None:
        raise RuntimeError("a single-mode upload returns one presigned request")
    client.upload_file(target["url"], path, sha256=digest, headers=target["headers"])
    client.complete_upload(
        body={},
        parameters={"upload_id": upload["upload_id"]},
        headers={"Idempotency-Key": idempotency_key()},
    )

    # C2PA only: no watermark and no fingerprint.
    job = client.accept_signing_job(
        body={"asset_id": upload["asset_id"], "watermark": False, "fingerprint": False},
        headers={"Idempotency-Key": idempotency_key()},
    )
    signed = poll(
        lambda: client.get_job(parameters={"job_id": job["job_id"]}),
        sign_job_terminal,
        timeout=300,
    )
    print(signed["state"], signed["recipe_id"])
```

`sign_job_terminal` is the completion test for `job_...` Sign snapshots. It fails closed on
identifier or readiness drift: a completed Sign result must carry a ready `vfy_...` evidence ID.
Use `verification_job_terminal` for `vjob_...` public Verify jobs; a `vjob_...` is only a pollable
job and never immutable evidence.

## Choose what a signing job adds

Every job signs with C2PA. Two flags choose what else it does (an omitted flag means `false`):

| You want                                 | Request fields                         |
| ---------------------------------------- | -------------------------------------- |
| C2PA Content Credentials only            | `watermark: false, fingerprint: false` |
| An invisible watermark, then C2PA        | `watermark: true`                      |
| A watermark and a fingerprint, then C2PA | `watermark: true, fingerprint: true`   |
| A fingerprint, then C2PA                 | `fingerprint: true`                    |

Send both flags every time (only an older key with legacy defaults may leave them out). The job
reports the exact `recipe_id` it ran. Integrations that already send a `recipe_id` keep working; a
flag sent with it must agree with that recipe or the request is refused.

## Examples

### 1. Add an invisible watermark and fingerprints

```python
watermarked = client.accept_signing_job(
    body={"asset_id": asset_id, "watermark": True},
    headers={"Idempotency-Key": idempotency_key()},
)
fingerprinted = client.accept_signing_job(
    body={"asset_id": asset_id, "watermark": True, "fingerprint": True},
    headers={"Idempotency-Key": idempotency_key()},
)
```

Each job is a separate signing of the asset. A watermark request accepts only media types that
the deployment supports for watermarking; `client.get_capabilities()` lists them.

### 2. Declare AI generation (EU AI Act Article 50, SB 942)

To declare that a generative model produced the file, add `ai_declaration` and keep
`"watermark": False`. A watermark together with an AI declaration is refused with
`JOB_POLICY_REJECTED` and `detail_code` `AI_DECLARATION_REQUIRES_SIGN_ONLY`.

```python
job = client.accept_signing_job(
    body={
        "asset_id": asset_id,
        "watermark": False,
        "fingerprint": True,
        "ai_declaration": {
            "software_agent_name": "Studio Nova Imagine",
            "software_agent_version": "2.0",
            "digital_source_type": "trainedAlgorithmicMedia",
        },
    },
    headers={"Idempotency-Key": idempotency_key()},
)
```

### 3. Download the signed file with integrity checks

```python
result = signed["result"]
if result is None:
    raise RuntimeError("the job did not publish an asset")
grant = client.create_asset_download(parameters={"asset_id": result["asset_id"]})
client.download_file(
    grant["url"],
    Path("photo.signed.jpg"),
    byte_length=grant["byte_length"],
    sha256=grant["sha256"],
    headers=grant["headers"],
)
```

The download URL is a short-lived bearer capability: keep it out of logs. The file is written to a
temporary name and moved into place only after its length and SHA-256 match.

### 4. Check a file on a public verify page (no API key)

```python
from originalpictures import verify_public

result = verify_public("photo.jpg", page="studio-nova")
print(result["content_credentials"]["status"], result["made_with"]["answer"])
print(result["statement"])
```

`verify_public` states what the file declares about its origin and whether the page owner's
system has a record of it. Show the result's `statement` with it. A file may be at most 25 MB, and
a running check is polled every 2 seconds. `verify_public_async` is the asynchronous form,
`fetch_verify_page("studio-nova")` reads the page's public settings, and
`Client.verify_public(slug, file)` does the same on an existing client. Each check is billed to the
page owner.

### 5. Verify a webhook delivery

```python
from originalpictures import RequestValidationError, verify_webhook


def handle(raw_body: bytes, headers: dict[str, str], secret: str) -> bool:
    try:
        verify_webhook(
            raw_body,
            secret=secret,  # the whsec_... value shown once when the endpoint was created
            event_id=headers["webhook-id"],
            timestamp=headers["webhook-timestamp"],
            signature=headers["webhook-signature"],
        )
    except RequestValidationError:
        return False
    return True
```

Pass the exact raw request bytes: parsing and re-serializing the JSON first invalidates the HMAC.
Several space-delimited signatures are accepted during secret rotation.

### 6. Async client and error handling

```python
import asyncio

from originalpictures import AsyncClient, RateLimitError


async def recent_assets() -> None:
    async with AsyncClient(
        base_url="https://dev-api.originalpictures.com", api_key="opk_..."
    ) as client:
        try:
            page = await client.list_assets(parameters={"limit": 20})
        except RateLimitError as error:
            print("retry later", error.code, error.request_id)
            return
        for item in page["items"]:
            print(item["asset_id"])


asyncio.run(recent_assets())
```

## Configuration

| Setting             | Where                              | Default                                          |
| ------------------- | ---------------------------------- | ------------------------------------------------ |
| API origin          | `Client(base_url=...)`             | none; use `https://dev-api.originalpictures.com` |
| API key             | `Client(api_key=...)`              | none; read it from your secret store             |
| Request timeout     | `Client(timeout=...)` (seconds)    | `30.0`                                           |
| JSON response bound | `Client(max_response_bytes=...)`   | `DEFAULT_MAX_RESPONSE_BYTES` (16 MiB)            |
| Custom HTTP client  | `Client(http_client=httpx.Client)` | a private `httpx.Client`                         |
| Public check origin | `verify_public(..., api_base=...)` | `https://dev-api.originalpictures.com`           |

The SDK reads no environment variables itself; the examples use `ORIGINALPICTURES_API_KEY` by
convention, the same name the CLI and MCP server read. Do not put API keys in command arguments or
logs. API base URLs may include a path prefix, which is preserved; query strings and fragments are
rejected locally before any request or credential is sent.

`poll_async` cancels an in-flight coroutine at its wall deadline. `poll` runs each fetch in one of at
most eight daemon workers and never queues work; when all are busy, new polls fail with
`PollingCapacityError`. Give callbacks a finite I/O timeout no longer than the poll budget.

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
Files you upload are processed on Original Pictures' private servers, encrypted in transit and at
rest, in isolated processing. Published outputs are kept for the retention your API key selects
(`1h`, `24h`, `72h` or `retain`; new accounts default to 72 hours). Operator views show metadata
only, and emergency access is audited. This is private server processing, not end-to-end
encryption. See [Retention and pricing](https://docs.originalpictures.com/api/retention-pricing/).

**What formats are supported?**
Embedded C2PA for JPEG, PNG, WebP, TIFF, AVIF, WAV, MP3, AAC (`.m4a`) and MP4 (H.264/AAC).
Sign-only embedding for GIF, JPEG XL, SVG, DNG, HEIC/HEIF, QuickTime, AVI and FLAC. A sidecar
`.c2pa` manifest for PDF, EPUB, DOCX, text, fonts and ML model files. Watermarks and fingerprints
apply only to media types that can be decoded. `client.get_capabilities()` returns the live list;
see [Supported media](https://docs.originalpictures.com/introduction/).

**Does a watermark replace C2PA?**
No. C2PA records declared origin in metadata; the watermark and fingerprints help find your record
again when that metadata has been stripped. A file declared as AI-generated is signed without a
watermark.

**Does this make me meet the EU AI Act or SB 942?**
It produces machine-readable marking of the kind those laws describe. Whether your use meets an
obligation is a legal question for your counsel; using the SDK does not by itself satisfy any law.

**How much does it cost?**
See [pricing](https://originalpictures.com/pricing/). Signing jobs, watermarks, fingerprints and
verifications are billable operations.

**How do I get an API key?**
Sign in to the [console](https://console.originalpictures.com/) and create one under **API keys**.
Give each integration its own key with only the scopes it needs.

## Links

- Documentation: <https://docs.originalpictures.com/>
- Python SDK guide: <https://docs.originalpictures.com/sdk/python/>
- API reference: <https://docs.originalpictures.com/api/>
- Website: <https://originalpictures.com>
- Related packages: [`@originalpictures/sdk`](https://www.npmjs.com/package/@originalpictures/sdk)
  (TypeScript), [`originalpictures-cli`](https://pypi.org/project/originalpictures-cli/),
  [`originalpictures-mcp`](https://pypi.org/project/originalpictures-mcp/)
- Support: <hello@originalpictures.com>

## Licence

Licensed under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0); the
full text is in the `LICENSE` file shipped with this package. Copyright © 2026 Original Pictures
Technologies, Inc. The licence grants no rights to the Original Pictures name or logo.
