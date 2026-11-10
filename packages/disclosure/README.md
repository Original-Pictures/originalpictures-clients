# @originalpictures/disclosure: AI disclosure labels and notices for the EU AI Act, SB 942 and more

`@originalpictures/disclosure` helps you show AI disclosures with the text, form and timing a
jurisdiction's rule asks for, and keep evidence that you showed them. It bundles a jurisdiction
policy engine, the `<op-ai-notice>` and `<op-ai-label>` web components, an AI badge set, and an
evidence logger for your [Original Pictures](https://originalpictures.com) account.

```html
<script
  src="https://cdn.jsdelivr.net/npm/@originalpictures/disclosure@0.1.0/dist/disclosure.iife.js"
  defer
></script>
<op-ai-notice jurisdiction="auto" publishable-key="opk_…"></op-ai-notice>
```

**Draft text.** Every rule is drafted from the statute and flagged `needs_legal_review: true` until
the owner's legal review clears it. Showing a notice does not by itself satisfy any law. The badges
are Original Pictures designs, not an official EU mark.

## What it does

- **Policy engine** bundling `op.disclosure-policy.2026-10.v1`: EU AI Act Article 50(1), (2), (4)
  and (5); the California AI Transparency Act (SB 942, as amended by AB 853) and the BOT Act
  (SB 1001); Maine LD 1727; New Hampshire HB 1596; New York GBL Art. 47 and synthetic-performer
  ads; Utah SB 149 and SB 226; India; China; Korea.
- **`<op-ai-notice>`**: the first-interaction notice for a chatbot or AI assistant.
- **`<op-ai-label>`**: a visible AI label on generated or manipulated media, or an offer to add
  one.
- **AI badge set** (AI-generated, AI-manipulated, AI interaction, AI-assisted) in brand light,
  brand dark and neutral, as SVG files and as components.
- **`badge()`**: overlays a label on an image in the browser.
- **Evidence log**: every shown notice, offered or applied label and acknowledgement can be logged
  to `POST /v1/disclosures/events` with a publishable key. The log is hash-chained and
  tamper-evident; it is not signed and not externally anchored, so keep the receipts
  (`op-disclosure-logged`) you are given.

Visible labels complement machine-readable marking. For the C2PA Content Credentials, invisible
watermark and fingerprinting side of AI transparency, see
[`@originalpictures/sdk`](https://www.npmjs.com/package/@originalpictures/sdk).

## Why use it

- One place for the rule text, citation, form (notice or label) and timing per jurisdiction.
- Detects a likely jurisdiction from a server region hint, time zone and Accept-Language, and lets
  you override it.
- Accessible, themeable web components with no framework dependency.
- An evidence trail of what you showed, to whom (by opaque reference) and when.
- A Python mirror with the same policy:
  [`originalpictures-disclosure`](https://pypi.org/project/originalpictures-disclosure/).

## Install

```sh
npm install @originalpictures/disclosure
```

Or load the IIFE bundle from a CDN with the script tag above.

## Quickstart: resolve a rule

```js
import { resolve, browserHints } from "@originalpictures/disclosure/core";

const notice = resolve({ ...browserHints(), region: "US-CA" }); // jurisdiction "auto"
notice.text; // "You are interacting with a bot, an automated AI system, not a person."
notice.rule.id; // "us-ca.sb1001.bot-disclosure"
notice.instrument.citation; // "Bus. & Prof. Code §§ 17940-17943"
notice.needsLegalReview; // true
```

`jurisdiction: "auto"` uses, in order, a server `region` hint (ISO 3166-1 or 3166-2, for example
from your CDN's geolocation header), the time zone, then Accept-Language, then `fallback` (default
`"EU"`). A US time zone spans many states, so it never selects a state: pass `region` for state
rules. A hint is not a legal determination of where someone is.

## Examples

### 1. Chatbot notice (EU AI Act Article 50(1))

```html
<op-ai-notice jurisdiction="auto" publishable-key="opk_…" remember="session"></op-ai-notice>
```

`<op-ai-notice>` also takes `remember` (`session`, `local` or `none`), `repeat-after` (minutes, for
example `180` for New York's three-hour reminder) and `acknowledge-label`. A rule whose timing is
`on_request` (Utah) stays hidden until you call `element.show()`.

### 2. Label AI-generated or manipulated media (Article 50(4))

```html
<img src="/render.jpg" alt="Harbour at dusk" />
<op-ai-label kind="deepfake_label" content-ref="ast_…" publishable-key="opk_…"></op-ai-label>
```

### 3. Offer a label (California SB 942)

```html
<op-ai-label mode="offer" jurisdiction="US-CA" publishable-key="opk_…"></op-ai-label>
```

`<op-ai-label>` also takes `badge`, `variant` (`brand-light`, `brand-dark`, `neutral`, or omitted to
follow the theme), `kind` (`visible_label` or `deepfake_label`), `mode="offer"`, `show-text` and
`size`.

### 4. Draw a badge onto an image

```js
import { badge } from "@originalpictures/disclosure/core";

const handle = await badge(imgElement, { badge: "ai-generated", position: "bottom-right" });
handle.remove();

const labelled = await badge(blob); // a new PNG/JPEG/WebP with the badge drawn in
```

A labelled Blob is a new encoding, so Content Credentials in the original are not carried over:
label first, then sign the labelled copy if you publish it.

### 5. Log evidence from your own code

```js
import { DisclosureClient, resolve } from "@originalpictures/disclosure/core";

const client = new DisclosureClient({ publishableKey: "opk_…" });
const notice = resolve({ jurisdiction: "EU" });
const receipt = await client.logResolved(notice, "ai_interaction_notice", {
  subjectRef: "session:8c1f",
});
receipt.sequence; // position in your hash-chained log
receipt.hash;
```

Event kinds: `ai_interaction_notice`, `visible_label_offered`, `visible_label_applied`,
`user_acknowledged`.

## Components: attributes and events

Shared attributes: `jurisdiction`, `rule`, `locale`, `region`, `publishable-key`, `api-base`,
`subject-ref` (defaults to a random `visitor:` id kept in localStorage), `content-ref`, `theme`.

Events: `op-disclosure-event` (always, with the exact request body), `op-disclosure-logged` (the
receipt) and `op-disclosure-error` (`kind`, `code`, `message` and `status`, the HTTP status or
`null` when no response arrived). Without a publishable key nothing is sent.

A `401` means the key was revoked, rotated away or has expired: no event from the page is being
recorded. The components then dispatch `op-disclosure-error` with `status: 401` for every event and
log one `console.warn` per page.

## Publishable keys

Create one in the [console](https://console.originalpictures.com/), or with `POST /v1/api-keys` and
`{"preset": "publishable_disclosure"}`. Its only scope is `disclosure:write`, so it can only append
events. Give it a rate limit. `subject_ref` and `content_ref` must be opaque references, never an
email address or a name.

A `publishable_disclosure` key issued without `expires_at` never expires, so embedded components
keep logging until you revoke it. A key you issue with an `expires_at`, or one issued while the
default was 90 days, stops working at that time; replace it before then. Anyone who views your page
can copy the key and append events to your log, so give it a rate limit and revoke and replace it if
you see events you did not send. An allowed-origins restriction is not available yet.

## Configuration

| Setting         | Where                                                     | Default                            |
| --------------- | --------------------------------------------------------- | ---------------------------------- |
| API origin      | `api-base` attribute, `DisclosureClient({ apiBase })`     | `https://api.originalpictures.com` |
| Publishable key | `publishable-key`, `DisclosureClient({ publishableKey })` | none: nothing is sent              |
| Jurisdiction    | `jurisdiction` attribute, `resolve({ jurisdiction })`     | `auto`, falling back to `EU`       |
| Policy document | `resolve({ policy })` with `fetchPolicy()`                | the bundled `2026-10.v1` policy    |

Badge files: `@originalpictures/disclosure/badges/ai-generated-brand-light.svg` and the other eleven
combinations. `badgeSvg(id, variant)` returns the same markup. The policy JSON is exported as
`@originalpictures/disclosure/policy.json`.

## Use with React, Next.js or Vue

The components are standard custom elements; import the package once on the client:

```jsx
// React or Next.js (client component)
import "@originalpictures/disclosure";

export function ChatNotice({ region }) {
  return (
    <op-ai-notice
      jurisdiction="auto"
      region={region}
      publishable-key={process.env.NEXT_PUBLIC_OP_DISCLOSURE_KEY}
    ></op-ai-notice>
  );
}
```

Pass `region` from the server (for example a CDN geolocation header) when state rules matter. To
pick the rule on the server instead, use `resolve()` from `@originalpictures/disclosure/core` in
Node, or the Python mirror
[`originalpictures-disclosure`](https://pypi.org/project/originalpictures-disclosure/).

## How it works

1. `resolve()` picks a jurisdiction (explicit, or detected from region, time zone and language).
2. It selects the rule of the kind you asked for (`ai_interaction_notice`, `visible_label`,
   `deepfake_label` or `machine_readable_marking`) and the best text for the locale.
3. The component shows the text with the rule's form and timing, and dispatches
   `op-disclosure-event` with the exact request body.
4. With a publishable key, the event is appended to your hash-chained log and the receipt arrives
   as `op-disclosure-logged`.

## Troubleshooting

| Symptom                                  | Likely cause and fix                                                  |
| ---------------------------------------- | --------------------------------------------------------------------- |
| The notice never appears                 | The rule's timing is `on_request` (Utah); call `element.show()`.      |
| A US visitor gets the EU text            | No `region` was passed; a US time zone never selects a state.         |
| `op-disclosure-error` with `status: 401` | The publishable key was revoked, rotated or expired; issue a new one. |
| Events are not recorded                  | No `publishable-key` is set; without one nothing is sent.             |

## FAQ

**Does this make my site meet the EU AI Act or SB 942?**
No library can do that by itself. It shows draft disclosure text for each rule and records that you
showed it; whether your use meets an obligation is a legal question for your counsel. Every rule is
flagged `needs_legal_review` until reviewed.

**Is this C2PA?**
The labels are visible disclosures, not C2PA manifests. For C2PA Content Credentials use
[`@originalpictures/sdk`](https://www.npmjs.com/package/@originalpictures/sdk). Original Pictures is
listed on the C2PA Conforming Products List as a generator product under the C2PA Conformance
Program 0.2.

**Is Original Pictures audited?**
Original Pictures Technologies, Inc. holds ISO/IEC 27001:2022 certification for its information
security management system (GCAI, certificate GCAI-ISMS-PD91) and ISO/IEC 42001:2023 certification
for its AI management system (TNV). It has a SOC 2 Type I report from Percilchofe CPA LLC as of
19 October 2026, and runs a GDPR compliance program. The certifications cover management systems,
not this package. See [Security and compliance](https://originalpictures.com/security/).

**Does it store my media or my visitors' data?**
No media is sent. Logged events carry only the rule, jurisdiction, locale and the opaque
references you choose; never put an email address or a name in them.

**Does a label keep the image's Content Credentials?**
No. `badge()` on a Blob produces a new encoding. Label first, then sign the labelled copy.

**How much does it cost?**
See [pricing](https://originalpictures.com/pricing/).

**How do I get a publishable key?**
In the [console](https://console.originalpictures.com/), under **API keys**, with the publishable
disclosure preset.

## Links

- Documentation: <https://docs.originalpictures.com/>
- Disclosures API: <https://docs.originalpictures.com/api/disclosures/>
- Website: <https://originalpictures.com>
- Support: <hello@originalpictures.com>

## Licence

Licensed under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0); the
full text is in the `LICENSE` file shipped with this package. Copyright © 2026 Original Pictures
Technologies, Inc. The licence grants no rights to the Original Pictures name or logo.
