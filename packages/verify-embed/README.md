# @originalpictures/verify: Content Credentials (C2PA) verify widget and verify() function

`@originalpictures/verify` adds a C2PA Content Credentials checker to any web page. The
`<op-verify>` web component lets visitors drop or choose a file, or inspect media already on your
page, and see what the file declares about its origin and whether your
[Original Pictures](https://originalpictures.com) account has a record of it. The `verify()`
function does the same from your own code.

```html
<script
  src="https://cdn.jsdelivr.net/npm/@originalpictures/verify@0.1.0/dist/verify.iife.js"
  defer
></script>
<op-verify page="studio-nova"></op-verify>
```

It never judges the content itself; every result carries the sentence the API sends in
`statement`, and the card shows it.

## What it does

- **Checks Content Credentials (C2PA manifests)** in a file and reports their status: `valid`,
  `valid_untrusted`, `invalid` or `absent`.
- **Reports the declared origin**: the signer as the certificate names it, the claim generator,
  the declared actions, and whether an AI-generation source type is declared (the marking that EU
  AI Act Article 50 and the California AI Transparency Act, SB 942, describe).
- **Answers "made with us?"**: whether your account's records match the file, including recovery
  through an invisible watermark or perceptual fingerprint when the file's metadata was stripped
  and the page has recovery turned on (`made_with.answer`: `yes` or `no_record`; `made_with.method`:
  `c2pa_manifest`, `watermark` or `fingerprint`).
- **Inspects media on your page**: a compact "Check Content Credentials" button next to an
  `<img>`, `<video>` or `<audio>`.

## Why use it

- Zero runtime dependencies, shadow DOM, light and dark themes.
- Keyboard and screen-reader accessible (`aria-expanded`, plain-language errors).
- No API key in the page: checks are anonymous calls to your public verify page.
- Billing-aware: checks run on a press, not on page view, unless you opt in with `autocheck`.
- Works with a script tag, a bundler, or as plain functions from `/core` with no side effects.

## Install

```sh
npm install @originalpictures/verify
```

Or load it from a CDN with the script tag above. You need a verify page: create one in the
[console](https://console.originalpictures.com/) and use its slug as `page`.

## Quickstart

```js
import "@originalpictures/verify"; // defines <op-verify>
```

```html
<op-verify page="studio-nova"></op-verify>
```

Listen for results:

```js
document.querySelector("op-verify").addEventListener("op-verify-result", (event) => {
  const { result } = event.detail;
  console.log(result.content_credentials?.status, result.made_with?.answer, result.statement);
});
```

## Examples

### 1. Verify a file from your own code

```js
import { verify, VerifyError } from "@originalpictures/verify/core"; // no side effects

try {
  const result = await verify(file, { page: "studio-nova" });
  result.content_credentials?.status; // "valid" | "valid_untrusted" | "invalid" | "absent"
  result.made_with?.answer; // "yes" | "no_record"
  result.statement; // show this sentence with the result
} catch (error) {
  if (error instanceof VerifyError) console.warn(error.code, error.message);
}
```

`verify()` posts the file to `POST /v1/public/verify-pages/{slug}/checks` (anonymous, at most
25 MB, rate-limited per network) and polls a running check no faster than every 2 seconds. The
file's name is not sent. Errors are `VerifyError` with the API's reason `code`, for example
`PUBLIC_CHECK_RATE_LIMITED` with `retryAfterSeconds`.

### 2. Inspect an image already on your page

```html
<img id="hero" src="https://cdn.example.com/sunrise.jpg" alt="Sunrise" />
<op-verify page="studio-nova" for="hero"></op-verify>
<!-- or name the asset directly -->
<op-verify page="studio-nova" src="https://cdn.example.com/sunrise.jpg"></op-verify>
```

The button starts as "Check Content Credentials". Pressing it loads the asset in the visitor's
browser, sends it to the same public check, and shows "Content Credentials", "No Content
Credentials found" or "Content Credentials that do not validate"; it then expands into the full
card (with the statement) and collapses again on the next press. Pressing it again never runs a
second check. The same is available as `inspect(src, { page })` from
`@originalpictures/verify/core`, and `element.inspect()` on the element.

### 3. Read your page's settings first

```js
import { fetchVerifyPage } from "@originalpictures/verify/core";

const pageConfig = await fetchVerifyPage("studio-nova");
const element = document.querySelector("op-verify");
element.pageConfig = pageConfig; // skips the element's own page request
```

A page lists the media types it checks in `accepted_media_types`. `<op-verify>` sets its file
picker's `accept` from that list and refuses other types before uploading.

### 4. Dark theme and your brand colours

```html
<op-verify page="studio-nova" theme="dark"></op-verify>
<style>
  op-verify::part(button) {
    border-radius: 999px;
  }
</style>
```

Your page's accent colour styles the button (with a readable label colour); your background and
text colours apply in the light theme when they read at WCAG AA. Style hooks: `::part(root)`,
`::part(chip)`, `::part(panel)`, `::part(dropzone)`, `::part(button)`, `::part(logo)`.

### 5. Check automatically on load (billed per view)

```html
<op-verify page="studio-nova" for="hero" autocheck></op-verify>
```

## Attributes and events

| Attribute   | Meaning                                                                                     |
| ----------- | ------------------------------------------------------------------------------------------- |
| `page`      | Your verify page slug (required).                                                           |
| `api-base`  | API origin; defaults to `https://dev-api.originalpictures.com`.                             |
| `theme`     | `light`, `dark`, or omitted to follow the system.                                           |
| `src`       | Inspect mode: the URL of an asset on your page.                                             |
| `for`       | Inspect mode: the `id` of an `<img>`, `<video>` or `<audio>` on your page.                  |
| `autocheck` | Inspect mode: check when the element loads instead of on the first press (billed per view). |

The element dispatches `op-verify-result` (`detail.result`) and `op-verify-error` (`detail.code`,
`detail.message`). Set the `pageConfig` property to a configuration you already fetched to skip the
page request. `for` reads the element's `currentSrc` (the source the browser chose from `srcset` or
`<source>`), then its `src`.

## Limits and billing

- **Billing:** every check is billed to you, the page owner, as one verification. With
  `autocheck`, every page view that shows the element is a billed check.
- **Media types:** a type the page does not accept is refused before it is billed
  (`PUBLIC_CHECK_MEDIA_UNSUPPORTED`, 415, naming the accepted types). MP4 video is not checked on a
  verify page today.
- **Monthly allowance:** a page that has used it answers `PUBLIC_CHECK_MONTHLY_LIMIT_REACHED` (429,
  with `Retry-After` to the next UTC month).
- **CORS:** inspect mode loads the asset with a CORS request, so its server must allow your page's
  origin. When it does not, when the network fails, or when the asset is larger than 25 MB, nothing
  is checked: the element says so, offers the file drop instead, and dispatches `op-verify-error`
  with a `SOURCE_*` code (`SOURCE_UNREACHABLE`, `SOURCE_HTTP_ERROR`, `SOURCE_TOO_LARGE`,
  `SOURCE_EMPTY`, `SOURCE_INVALID`). Those failures happen before the check request and are not
  billed.

## Hosted page

`https://originalpictures.com/verify/{slug}/` shows the same component on the Original Pictures
site.

## Use with React, Vue, Svelte or plain HTML

`<op-verify>` is a standard custom element, so any framework can render it once the module is
imported on the client:

```jsx
// React or Next.js (client component)
import "@originalpictures/verify";

export function VerifyBox() {
  return <op-verify page="studio-nova" theme="light"></op-verify>;
}
```

```html
<!-- Vue or Svelte template -->
<op-verify page="studio-nova"></op-verify>
```

In Vue, tell the compiler that `op-verify` is a custom element (`compilerOptions.isCustomElement`).
Server-side rendering emits the tag as plain HTML; it upgrades when the module loads in the
browser.

## How it works

1. The element reads your verify page's public settings (`GET /v1/public/verify-pages/{slug}`):
   display name, colours, accepted media types and the statement.
2. A visitor drops or chooses a file, or presses the inspect button. The element checks the type
   and size locally and refuses what the page does not accept, before anything is billed.
3. The file's bytes (not its name) go to `POST /v1/public/verify-pages/{slug}/checks`. A running
   check is polled no faster than every 2 seconds.
4. The card shows the Content Credentials status, the declared origin, whether your records match,
   and the statement.

## Troubleshooting

| Symptom                                   | Likely cause and fix                                                          |
| ----------------------------------------- | ----------------------------------------------------------------------------- |
| The element renders nothing               | The module did not load; check the script URL or the import.                  |
| `NotFound` or a page error                | The `page` slug is wrong, or the verify page is not published.                |
| Inspect mode offers the file drop instead | The asset's server does not allow your origin (CORS), or the file is > 25 MB. |
| `PUBLIC_CHECK_RATE_LIMITED`               | Too many checks from one network; wait `retryAfterSeconds`.                   |
| `PUBLIC_CHECK_MEDIA_UNSUPPORTED`          | The page does not check that type; the message lists the accepted ones.       |

## FAQ

**Is this C2PA?**
Yes. It reads standard C2PA manifests (Content Credentials) and validates their certificate chain.
Original Pictures is listed on the C2PA Conforming Products List as a generator product under the
C2PA Conformance Program 0.2 (C2PA Technical Specification 2.4).

**Is Original Pictures audited?**
Original Pictures Technologies, Inc. holds ISO/IEC 27001:2022 certification for its information
security management system (GCAI, certificate GCAI-ISMS-PD91) and ISO/IEC 42001:2023 certification
for its AI management system (TNV). It has a SOC 2 Type I report from Percilchofe CPA LLC as of
19 October 2026, and runs a GDPR compliance program. The certifications cover management systems,
not this package. See [Security and compliance](https://originalpictures.com/security/).

**Does it store my visitors' files?**
The file is sent to Original Pictures' private servers for the check, encrypted in transit, and is
processed in isolation; its name is not sent. Operator views show metadata only. This is private
server processing, not end-to-end encryption.

**What formats can a visitor check?**
The types your verify page lists in `accepted_media_types`: JPEG, PNG, WebP, TIFF, AVIF, WAV,
M4A, MP3, FLAC and PDF where the deployment admits them. MP4 video is not checked on a verify page
today; verify a signed video through the API instead.

**Does it need an API key?**
No. Checks are anonymous calls to your public verify page and are billed to the page owner.

**How much does it cost?**
See [pricing](https://originalpictures.com/pricing/).

**How do I get a verify page?**
Sign in to the [console](https://console.originalpictures.com/) and create one.

## Links

- Documentation: <https://docs.originalpictures.com/>
- Verify pages: <https://docs.originalpictures.com/api/verify-pages/>
- Website: <https://originalpictures.com>
- Related packages: [`@originalpictures/sdk`](https://www.npmjs.com/package/@originalpictures/sdk),
  [`@originalpictures/disclosure`](https://www.npmjs.com/package/@originalpictures/disclosure)
- Support: <hello@originalpictures.com>

## Licence

Licensed under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0); the
full text is in the `LICENSE` file shipped with this package. Copyright © 2026 Original Pictures
Technologies, Inc. The licence grants no rights to the Original Pictures name or logo.
