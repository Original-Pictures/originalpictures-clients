# @originalpictures/sdk: TypeScript SDK for C2PA Content Credentials, AI watermarking and verification

`@originalpictures/sdk` is the official, typed TypeScript and JavaScript client for the
[Original Pictures](https://originalpictures.com) API. Use it from Node.js or the browser to sign
images, audio, video and documents with C2PA Content Credentials, add an invisible watermark and
perceptual fingerprints, and verify what a file declares about its origin.

It provides generated types for all 128 operations in the public API contract. The client executes
the 126 consumer operations; the two provider-ingress operations (Clerk and Stripe callbacks) stay
typed but are deliberately non-callable, because their signatures cover exact raw bytes that a JSON
client must not re-encode.

```ts
import { OriginalPicturesClient } from "@originalpictures/sdk";

const client = new OriginalPicturesClient({
  baseUrl: "https://api.originalpictures.com",
  apiKey: process.env.ORIGINALPICTURES_API_KEY,
});
const me = await client.operations.getCurrentUser();
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
- **AI-generation declaration.** Records that a generative model produced the file, the kind of
  machine-readable marking described by EU AI Act Article 50(2) and the California AI
  Transparency Act (SB 942, as amended by AB 853).
- **Verification.** Checks Content Credentials, the certificate chain and your account's records,
  and reports the declared origin with reason codes. It is never a judgement about the content
  itself.
- **Webhooks.** `verifyWebhook()` checks Standard Webhooks signatures on raw request bodies.

## Why use it

- Every operation is typed from the OpenAPI contract: `client.operations.<operationId>()` with
  typed `body`, `parameters`, `headers` and response.
- Safe transfers: `uploadBlob` (browsers) and `uploadNodeStream` (Node streaming) hash the bytes
  first; `download` writes to a staged sink whose `commit()` runs only after the exact length and
  SHA-256 match, and `abort()` runs on any failure.
- Cancellation everywhere: `poll` passes an `AbortSignal` to each fetch, and deadlines or caller
  cancellation settle the poll immediately.
- Stable, typed errors (`AuthenticationError`, `RateLimitError`, `ConflictError` and others)
  carrying the API's reason `code` and `requestId`.
- ESM, ships its own `.d.ts`, one small dependency (`@noble/hashes`).

## Install

```sh
npm install @originalpictures/sdk
```

```sh
pnpm add @originalpictures/sdk
```

The package is ESM-only (`import`, not `require`).

## Quickstart: sign a file (Node.js)

Get an API key from the [console](https://console.originalpictures.com/) (keys start with
`opk_`). Upload the bytes, then accept a signing job for the asset.

```ts
import { createHash } from "node:crypto";
import { readFile } from "node:fs/promises";

import {
  OriginalPicturesClient,
  idempotencyKey,
  poll,
  signJobTerminal,
} from "@originalpictures/sdk";

const client = new OriginalPicturesClient({
  baseUrl: "https://api.originalpictures.com",
  apiKey: process.env.ORIGINALPICTURES_API_KEY,
});

const bytes = await readFile("photo.jpg");
const sha256 = createHash("sha256").update(bytes).digest("hex");
const upload = await client.operations.createUpload({
  body: { byte_length: bytes.length, declared_media_type: "image/jpeg", mode: "single", sha256 },
});
if (!upload.upload) throw new Error("a single-mode upload returns one presigned request");
await client.uploadBlob(upload.upload.url, new Blob([bytes]), {
  byteLength: bytes.length,
  sha256,
  headers: upload.upload.headers,
});
await client.operations.completeUpload({
  body: {},
  parameters: { upload_id: upload.upload_id },
  headers: { "Idempotency-Key": idempotencyKey() },
});

// C2PA only: no watermark and no fingerprint.
const job = await client.operations.acceptSigningJob({
  body: { asset_id: upload.asset_id, watermark: false, fingerprint: false },
  headers: { "Idempotency-Key": idempotencyKey() },
});
const signed = await poll(
  (signal) => client.operations.getJob({ parameters: { job_id: job.job_id }, signal }),
  (snapshot) => signJobTerminal({ ...snapshot }),
  { timeoutMs: 300_000 },
);
console.log(signed.state, signed.recipe_id);
```

Use `signJobTerminal` for `job_...` Sign snapshots and `verificationJobTerminal` for pollable
`vjob_...` Verify snapshots. They fail closed on readiness drift: a completed Sign result must
carry ready immutable `vfy_...` evidence, and a `vjob_...` is never evidence.

## Choose what a signing job adds

Every job signs with C2PA. Two flags choose what else it does (an omitted flag means `false`):

| You want                                 | Request fields                         |
| ---------------------------------------- | -------------------------------------- |
| C2PA Content Credentials only            | `watermark: false, fingerprint: false` |
| An invisible watermark, then C2PA        | `watermark: true`                      |
| A watermark and a fingerprint, then C2PA | `watermark: true, fingerprint: true`   |
| A fingerprint, then C2PA                 | `fingerprint: true`                    |

The flags may be left out when the API key's signing profile names a default; send them when you
are not sure what that default is. The job reports the exact `recipe_id` it ran. A flag sent with a
`recipe_id` must agree with that recipe or the request is refused.

## Examples

### 1. Add an invisible watermark and fingerprints

```ts
await client.operations.acceptSigningJob({
  body: { asset_id: upload.asset_id, watermark: true },
  headers: { "Idempotency-Key": idempotencyKey() },
});
await client.operations.acceptSigningJob({
  body: { asset_id: upload.asset_id, watermark: true, fingerprint: true },
  headers: { "Idempotency-Key": idempotencyKey() },
});
```

Each job is a separate signing of the asset. A watermark request accepts only media types that
the deployment supports for watermarking; `client.operations.getCapabilities()` lists them.

### 2. Declare AI generation (EU AI Act Article 50, SB 942)

```ts
await client.operations.acceptSigningJob({
  body: {
    asset_id: upload.asset_id,
    watermark: false,
    fingerprint: true,
    ai_declaration: {
      software_agent_name: "Studio Nova Imagine",
      software_agent_version: "2.0",
      digital_source_type: "trainedAlgorithmicMedia",
    },
  },
  headers: { "Idempotency-Key": idempotencyKey() },
});
```

An AI declaration is accepted only on a sign-only request: `watermark: true` with
`ai_declaration` is refused with `JOB_POLICY_REJECTED` (`AI_DECLARATION_REQUIRES_SIGN_ONLY`).

### 3. Download the signed file with integrity checks

```ts
import { writeFile } from "node:fs/promises";

const assetId = signed.result?.asset_id;
if (!assetId) throw new Error("the job did not publish an asset");
const grant = await client.operations.createAssetDownload({ parameters: { asset_id: assetId } });
const chunks: Uint8Array[] = [];
await client.download(grant.url, {
  byteLength: grant.byte_length,
  sha256: grant.sha256,
  headers: grant.headers,
  sink: {
    write: (chunk) => {
      chunks.push(chunk);
    },
    commit: () => writeFile("photo.signed.jpg", Buffer.concat(chunks)),
    abort: () => {
      chunks.length = 0;
    },
  },
});
```

The download URL is a short-lived bearer capability: keep it out of logs.

### 4. Upload from a browser file input

```ts
const file = input.files![0];
const digest = await crypto.subtle.digest("SHA-256", await file.arrayBuffer());
const sha256 = [...new Uint8Array(digest)].map((b) => b.toString(16).padStart(2, "0")).join("");
const upload = await client.operations.createUpload({
  body: { byte_length: file.size, declared_media_type: file.type, mode: "single", sha256 },
});
await client.uploadBlob(upload.upload!.url, file, {
  byteLength: file.size,
  sha256,
  headers: upload.upload!.headers,
});
```

Never ship a secret API key to a browser. Run signing from your server, or give the browser a
key restricted to the scopes it needs.

### 5. Verify a webhook delivery and handle errors

```ts
import { ApiError, RateLimitError, ValidationError, verifyWebhook } from "@originalpictures/sdk";

export function isGenuineDelivery(raw: Uint8Array, headers: Headers, secret: string): boolean {
  try {
    verifyWebhook(raw, {
      secret, // the whsec_... value shown once when the endpoint was created
      eventId: headers.get("webhook-id") ?? "",
      timestamp: Number(headers.get("webhook-timestamp")),
      signature: headers.get("webhook-signature") ?? "",
    });
    return true;
  } catch (error) {
    if (error instanceof ValidationError) return false;
    throw error;
  }
}

try {
  await client.operations.listAssets({ parameters: { limit: 20 } });
} catch (error) {
  if (error instanceof RateLimitError) console.warn("retry later", error.requestId);
  else if (error instanceof ApiError) console.error(error.statusCode, error.code);
  else throw error;
}
```

Pass the exact raw body bytes to `verifyWebhook`; re-serialized JSON fails the HMAC.

## Configuration

| Option             | Meaning                                  | Default                                      |
| ------------------ | ---------------------------------------- | -------------------------------------------- |
| `baseUrl`          | API origin (may include a path prefix)   | required: `https://api.originalpictures.com` |
| `apiKey`           | API key, sent as `Authorization: Bearer` | none (anonymous operations only)             |
| `timeoutMs`        | Per-request timeout                      | `30000`                                      |
| `maxResponseBytes` | Hard bound on a JSON response            | `DEFAULT_MAX_RESPONSE_BYTES` (16 MiB)        |
| `fetch`            | A custom `fetch` implementation          | `globalThis.fetch`                           |

The SDK reads no environment variables itself; the examples use `ORIGINALPICTURES_API_KEY` by
convention. Query strings and fragments in `baseUrl` are rejected locally before any request or
credential is sent.

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
apply only to media types that can be decoded. `client.operations.getCapabilities()` returns the
live list; see [Supported media](https://docs.originalpictures.com/introduction/).

**Does this make me meet the EU AI Act or SB 942?**
It produces machine-readable marking of the kind those laws describe. Whether your use meets an
obligation is a legal question for your counsel; using the SDK does not by itself satisfy any law.

**Does it run in the browser?**
Yes, with standard `fetch`, `Blob` and `AbortSignal`. Keep secret keys on a server.

**How much does it cost?**
See [pricing](https://originalpictures.com/pricing/).

**How do I get an API key?**
Sign in to the [console](https://console.originalpictures.com/) and create one under **API keys**.

## Links

- Documentation: <https://docs.originalpictures.com/>
- TypeScript SDK guide: <https://docs.originalpictures.com/sdk/typescript/>
- API reference: <https://docs.originalpictures.com/api/>
- Website: <https://originalpictures.com>
- Related packages: [`originalpictures-sdk`](https://pypi.org/project/originalpictures-sdk/)
  (Python), [`@originalpictures/verify`](https://www.npmjs.com/package/@originalpictures/verify)
  (verify widget), [`@originalpictures/disclosure`](https://www.npmjs.com/package/@originalpictures/disclosure)
  (AI disclosure labels)
- Support: <hello@originalpictures.com>

## Licence

Licensed under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0); the
full text is in the `LICENSE` file shipped with this package. Copyright © 2026 Original Pictures
Technologies, Inc. The licence grants no rights to the Original Pictures name or logo.
