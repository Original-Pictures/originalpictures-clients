# originalpictures-disclosure: AI disclosure rules and evidence logging for Python (EU AI Act, SB 942)

`originalpictures-disclosure` resolves the AI disclosure rule that applies in a jurisdiction (the
text, form and timing a law asks for) and logs evidence that you showed it to your
[Original Pictures](https://originalpictures.com) account. It is the Python mirror of
[`@originalpictures/disclosure`](https://www.npmjs.com/package/@originalpictures/disclosure) and
bundles the same policy, `op.disclosure-policy.2026-10.v1`.

```python
from originalpictures_disclosure import resolve

notice = resolve(region="US-CA")
print(notice.text)  # You are interacting with a bot, an automated AI system, not a person.
```

**Draft text.** Every rule is drafted from the statute and flagged `needs_legal_review` until the
owner's legal review clears it. Showing a notice does not by itself satisfy any law.

## What it does

- **Resolves disclosure rules** for the EU AI Act Article 50(1), (2), (4) and (5); the California
  AI Transparency Act (SB 942, as amended by AB 853) and the BOT Act (SB 1001); Maine LD 1727; New
  Hampshire HB 1596; New York GBL Art. 47; Utah SB 149 and SB 226; India; China; Korea.
- **Four rule kinds**: `ai_interaction_notice` (chatbots), `visible_label`, `deepfake_label` and
  `machine_readable_marking`.
- **Picks the text in the user's language** from the locale or an Accept-Language header, falling
  back to English.
- **Logs evidence** to `POST /v1/disclosures/events`: a hash-chained, tamper-evident record of each
  notice shown, label offered or applied, and acknowledgement. The log is not signed and not
  externally anchored, so keep the receipts.

For the machine-readable side (C2PA Content Credentials, invisible watermark, fingerprinting), use
[`originalpictures-sdk`](https://pypi.org/project/originalpictures-sdk/).

## Why use it

- Server-side rendering: choose the right notice before the page or chatbot reply is sent.
- The same policy document and rule ids as the browser components, so server and client agree.
- Typed (`py.typed`) and frozen dataclasses; one dependency (`httpx`).
- One retry with the same idempotency key on a 5xx or network error.

## Install

```sh
pip install originalpictures-disclosure
```

Requires Python 3.12 or later.

## Quickstart

```python
from originalpictures_disclosure import DisclosureEventLogger, resolve

notice = resolve(region="US-CA")  # or jurisdiction="EU", accept_language=..., time_zone=...
print(notice.text, notice.instrument["citation"], notice.needs_legal_review)

with DisclosureEventLogger("opk_…") as log:
    receipt = log.log_resolved(notice, "ai_interaction_notice", subject_ref="session:8c1f")
    print(receipt.sequence, receipt.hash)
```

`resolve()` returns `None` when no rule matches (for example `fallback=None` and no hint), so check
for it before use. `subject_ref` and `content_ref` must be opaque references, never an email
address or a name.

## Examples

### 1. EU chatbot notice in the visitor's language

```python
from originalpictures_disclosure import resolve

notice = resolve(jurisdiction="EU", accept_language="de-DE,de;q=0.9")
notice.rule_id  # "eu.art50.1.ai-interaction"
notice.text  # "Sie chatten mit einem KI-System."
notice.locale  # "de"
```

### 2. Label for AI-generated or manipulated media (Article 50(4))

```python
label = resolve(jurisdiction="EU", kind="deepfake_label")
label.rule_id  # "eu.art50.4.deep-fake"
label.text  # "This content has been artificially generated or manipulated."
```

### 3. Detect the jurisdiction from request hints

```python
from originalpictures_disclosure import detect_jurisdiction, resolve

hints = {
    "region": request.headers.get("cloudfront-viewer-country-region-code"),
    "time_zone": user_time_zone,
    "accept_language": request.headers.get("accept-language"),
}
print(detect_jurisdiction(**hints))  # for example ("EU", "timezone") or None
notice = resolve(**hints, fallback="EU")
```

Detection uses, in order, the region (ISO 3166-1 or 3166-2), the time zone, then the language. A
US time zone never selects a state; pass `region` for state rules. A hint is not a legal
determination of where someone is.

### 4. Every rule of a kind, for a review page

```python
from originalpictures_disclosure import JURISDICTION_IDS, resolve_all

for jurisdiction in JURISDICTION_IDS:
    for rule in resolve_all(jurisdiction=jurisdiction, kind="visible_label"):
        print(jurisdiction, rule.rule_id, rule.timing, rule.form)
```

### 5. Log that a label was applied

```python
from originalpictures_disclosure import DisclosureEventError, DisclosureEventLogger

with DisclosureEventLogger("opk_…") as log:
    try:
        log.log_resolved(
            label,
            "visible_label_applied",
            subject_ref="visitor:4f2a",
            content_ref=asset_id,  # an opaque reference such as an ast_ asset ID
            surface="web",
        )
    except DisclosureEventError as error:
        print(error.code, error.status_code)
```

Event kinds: `ai_interaction_notice`, `visible_label_offered`, `visible_label_applied`,
`user_acknowledged`. Surfaces: `web`, `app`, `voice`, `api`, `other`.

## Configuration

| Setting         | Where                                         | Default                            |
| --------------- | --------------------------------------------- | ---------------------------------- |
| API origin      | `DisclosureEventLogger(..., api_base=...)`    | `https://api.originalpictures.com` |
| Request timeout | `DisclosureEventLogger(..., timeout=...)`     | `10.0` seconds                     |
| Retry delay     | `DisclosureEventLogger(..., retry_delay=...)` | `1.0` second (one retry)           |
| HTTP client     | `DisclosureEventLogger(..., http_client=...)` | a private `httpx.Client`           |
| Fallback        | `resolve(..., fallback=...)`                  | `"EU"`; `None` resolves nothing    |
| Policy document | `resolve(..., policy=...)`                    | the bundled `2026-10.v1` policy    |

The API key must be an `opk_` key; a publishable key with only `disclosure:write` is enough. The API
origin must use HTTPS (plain HTTP only on loopback, for tests).

## Use in a web app

```python
from fastapi import FastAPI, Request

from originalpictures_disclosure import resolve

app = FastAPI()


@app.get("/chat/notice")
def chat_notice(request: Request) -> dict[str, str | None]:
    notice = resolve(
        region=request.headers.get("cloudfront-viewer-country-region-code"),
        accept_language=request.headers.get("accept-language"),
    )
    if notice is None:
        return {"text": None, "rule_id": None}
    return {"text": notice.text, "rule_id": notice.rule_id}
```

The same call works in Django, Flask or a chatbot worker. Log the event once the notice was
actually shown, not when it was resolved.

## How it works

1. `resolve()` picks a jurisdiction (explicit, or detected from region, time zone and language).
2. It selects the rule of the kind you asked for and the best text for the locale.
3. `DisclosureEventLogger.log_resolved()` sends the event with an idempotency key and returns the
   receipt (`event_id`, `sequence`, `prev_hash`, `hash`, `received_at`).

## Troubleshooting

| Symptom                                     | Likely cause and fix                                                            |
| ------------------------------------------- | ------------------------------------------------------------------------------- |
| `resolve()` returns `None`                  | No hint matched and `fallback=None`, or the kind has no rule there.             |
| `DISCLOSURE_INVALID: an opk_ API key...`    | Pass an `opk_` key.                                                             |
| `DisclosureEventError` with code `HTTP_401` | The key was revoked, rotated or expired.                                        |
| A reference is refused locally              | `subject_ref`/`content_ref` must match `REFERENCE_PATTERN` (no spaces, no `@`). |

## FAQ

**Does this make my product meet the EU AI Act or SB 942?**
No library can do that by itself. It gives you draft rule text and an evidence trail; whether your
use meets an obligation is a legal question for your counsel.

**Is this C2PA?**
This package handles visible disclosures. For C2PA Content Credentials use
[`originalpictures-sdk`](https://pypi.org/project/originalpictures-sdk/). Original Pictures is listed
on the C2PA Conforming Products List as a generator product under the C2PA Conformance Program 0.2.

**Is Original Pictures audited?**
Original Pictures Technologies, Inc. holds ISO/IEC 27001:2022 certification for its information
security management system (GCAI, certificate GCAI-ISMS-PD91) and ISO/IEC 42001:2023 certification
for its AI management system (TNV). It has a SOC 2 Type I report from Percilchofe CPA LLC as of
19 October 2026, and runs a GDPR compliance program. The certifications cover management systems,
not this package. See [Security and compliance](https://originalpictures.com/security/).

**Does it send my media or personal data?**
No media is sent. Events carry the rule, jurisdiction, policy version, locale, surface and the
opaque references you choose.

**What formats does it label?**
It resolves rule text; it does not edit files. Use the JavaScript package's `badge()` to draw a
visible label onto an image.

**How much does it cost?**
See [pricing](https://originalpictures.com/pricing/).

**How do I get an API key?**
In the [console](https://console.originalpictures.com/), under **API keys**.

## Links

- Documentation: <https://docs.originalpictures.com/>
- Disclosures API: <https://docs.originalpictures.com/api/disclosures/>
- Website: <https://originalpictures.com>
- Support: <hello@originalpictures.com>

## Licence

Licensed under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0); the
full text is in the `LICENSE` file shipped with this package. Copyright © 2026 Original Pictures
Technologies, Inc. The licence grants no rights to the Original Pictures name or logo.
