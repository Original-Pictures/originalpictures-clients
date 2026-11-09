// Shared plumbing for <op-ai-notice> and <op-ai-label>: theme styles, policy
// resolution from attributes, and evidence logging that never breaks the page.

import {
  DisclosureClient,
  DisclosureEventError,
  buildEventPayload,
  eventFor,
  pseudonymousSubject,
  type DisclosureEventKind,
  type DisclosureEventReceipt,
  type DisclosureEventRequest,
} from "./events.ts";
import { browserHints, isJurisdictionId, resolve, type ResolvedDisclosure } from "./policy.ts";
import type { RuleKind } from "./policy-types.ts";
import { DARK, FONT_STACK, LIGHT, themeCss } from "./tokens.ts";

/** Server-side rendering imports these modules too; only a browser defines elements. */
export const ElementBase: typeof HTMLElement =
  typeof HTMLElement === "undefined" ? (class {} as unknown as typeof HTMLElement) : HTMLElement;

export const THEME_CSS = `
:host{font-family:${FONT_STACK};${themeCss(LIGHT)}color-scheme:light}
@media (prefers-color-scheme:dark){:host(:not([theme="light"])){${themeCss(DARK)}color-scheme:dark}}
:host([theme="dark"]){${themeCss(DARK)}color-scheme:dark}
:host([hidden]){display:none}
*{box-sizing:border-box}
button{font:inherit}
button:focus-visible{outline:3px solid var(--op-focus);outline-offset:2px}
@media (forced-colors:active){button{border:1px solid ButtonText}}
`;

export interface DisclosureEventDetail {
  kind: DisclosureEventKind;
  payload: DisclosureEventRequest;
}
export interface DisclosureLoggedDetail {
  kind: DisclosureEventKind;
  receipt: DisclosureEventReceipt;
}
export interface DisclosureErrorDetail {
  kind: DisclosureEventKind;
  code: string;
  message: string;
  /** The HTTP status the API answered, or null when no response arrived. */
  status: number | null;
}

let warnedUnauthorized = false;

/** Test hook: lets the next 401 warn again. */
export function resetUnauthorizedWarning(): void {
  warnedUnauthorized = false;
}

/**
 * A 401 means the publishable key was revoked, rotated away or has expired, so
 * every later event on this page will be refused too. Say so once per page in
 * the console, where a site owner will look, rather than failing silently.
 */
function warnUnauthorizedOnce(): void {
  if (warnedUnauthorized) return;
  warnedUnauthorized = true;
  console.warn(
    "[@originalpictures/disclosure] The publishable key was refused (401): it is revoked, " +
      "rotated or expired. Disclosure events are NOT being recorded in your evidence log. " +
      "Issue a new publishable_disclosure key and update the publishable-key attribute.",
  );
}

/** Resolves the policy rule an element's attributes ask for, falling back to the EU rule. */
export function resolveFromAttributes(
  host: HTMLElement,
  kind: RuleKind,
): ResolvedDisclosure | null {
  const requested = host.getAttribute("jurisdiction") ?? "auto";
  const jurisdiction = isJurisdictionId(requested) ? requested : "auto";
  const options = {
    ...browserHints(),
    region: host.getAttribute("region"),
    jurisdiction,
    kind,
    ruleId: host.getAttribute("rule") ?? undefined,
    locale: host.getAttribute("locale") ?? host.closest("[lang]")?.getAttribute("lang") ?? null,
  } as const;
  // A covered jurisdiction may have no rule of this kind (India has no
  // AI-interaction rule); the EU rule's text is then shown and logged as EU.
  return resolve(options) ?? resolve({ ...options, jurisdiction: "EU", ruleId: undefined });
}

function emit<T>(host: HTMLElement, type: string, detail: T): void {
  host.dispatchEvent(new CustomEvent<T>(type, { detail, bubbles: true, composed: true }));
}

/**
 * Records an event: always dispatches op-disclosure-event (so a host can keep
 * its own log), and with a publishable-key attribute also sends it to
 * /v1/disclosures/events, answering op-disclosure-logged or op-disclosure-error.
 */
export async function logDisclosure(
  host: HTMLElement,
  resolved: ResolvedDisclosure,
  kind: DisclosureEventKind,
): Promise<DisclosureEventReceipt | null> {
  let payload: DisclosureEventRequest;
  const input = eventFor(resolved, kind, {
    subjectRef: host.getAttribute("subject-ref") ?? pseudonymousSubject(),
    contentRef: host.getAttribute("content-ref"),
    surface: "web",
  });
  try {
    payload = buildEventPayload(input);
  } catch (error) {
    emit<DisclosureErrorDetail>(host, "op-disclosure-error", {
      kind,
      code: error instanceof DisclosureEventError ? error.code : "DISCLOSURE_INVALID",
      message: error instanceof Error ? error.message : "invalid event",
      status: null,
    });
    return null;
  }
  emit<DisclosureEventDetail>(host, "op-disclosure-event", { kind, payload });
  const key = host.getAttribute("publishable-key");
  if (!key) return null;
  try {
    const client = new DisclosureClient({
      publishableKey: key,
      apiBase: host.getAttribute("api-base") ?? undefined,
    });
    const receipt = await client.log({ ...input, clientTime: new Date(payload.client_time) });
    emit<DisclosureLoggedDetail>(host, "op-disclosure-logged", { kind, receipt });
    return receipt;
  } catch (error) {
    const status = error instanceof DisclosureEventError ? error.status : null;
    if (status === 401) warnUnauthorizedOnce();
    emit<DisclosureErrorDetail>(host, "op-disclosure-error", {
      kind,
      code: error instanceof DisclosureEventError ? error.code : "UNKNOWN",
      message: error instanceof Error ? error.message : "the event was not recorded",
      status,
    });
    return null;
  }
}

export function el(
  tag: string,
  attributes: Record<string, string> = {},
  text?: string,
): HTMLElement {
  const node = document.createElement(tag);
  for (const [name, value] of Object.entries(attributes)) node.setAttribute(name, value);
  if (text !== undefined) node.textContent = text;
  return node;
}
