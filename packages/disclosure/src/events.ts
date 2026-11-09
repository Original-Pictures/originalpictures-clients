// Evidence logging: POST /v1/disclosures/events with a publishable key (an
// opk_ key whose only scope is disclosure:write). The server appends each
// event to the account's hash-chained, tamper-evident log and returns a
// receipt; the log is not signed.

import type { ResolvedDisclosure } from "./policy.ts";
import { isJurisdictionId } from "./policy.ts";
import type { JurisdictionId } from "./policy-types.ts";

export const DEFAULT_API_BASE = "https://dev-api.originalpictures.com";

export const EVENT_KINDS = [
  "ai_interaction_notice",
  "visible_label_offered",
  "visible_label_applied",
  "user_acknowledged",
] as const;
export type DisclosureEventKind = (typeof EVENT_KINDS)[number];
export type Surface = "web" | "app" | "voice" | "api" | "other";

/** op_domain.disclosures.DISCLOSURE_REFERENCE_PATTERN: opaque, never an email or a name. */
export const REFERENCE_PATTERN = /^[A-Za-z0-9._:~-]{1,128}$/;
const POLICY_VERSION_PATTERN = /^\d{4}-\d{2}-\d{2}\.\d{1,3}$/;
const RULE_ID_PATTERN = /^[a-z0-9]+(?:[._-][a-z0-9]+)*$/;
const LOCALE_PATTERN = /^[A-Za-z]{2,3}(?:-[A-Za-z0-9]{2,8})*$/;
// op_services.api_keys: "opk_" + lookup id + "." + secret.
const KEY_PATTERN = /^opk_[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+$/;

/** The request body, exactly as DisclosureEventRequest defines it. */
export interface DisclosureEventRequest {
  kind: DisclosureEventKind;
  jurisdiction: JurisdictionId;
  policy_version: string;
  rule_id: string | null;
  subject_ref: string;
  content_ref: string | null;
  client_time: string;
  surface: Surface | null;
  locale: string | null;
}

export interface DisclosureEventReceipt {
  event_id: string;
  sequence: number;
  prev_hash: string;
  hash: string;
  received_at: string;
}

export interface DisclosureEventInput {
  kind: DisclosureEventKind;
  jurisdiction: JurisdictionId;
  policyVersion: string;
  ruleId?: string | null;
  /** Your pseudonymous reference for the person or session (see pseudonymousSubject). */
  subjectRef: string;
  /** Your reference for the labelled content, e.g. an ast_ asset id. */
  contentRef?: string | null;
  locale?: string | null;
  surface?: Surface | null;
  /** Defaults to now. */
  clientTime?: Date;
}

export class DisclosureEventError extends Error {
  override readonly name = "DisclosureEventError";
  readonly code: string;
  readonly status: number | null;
  constructor(code: string, message: string, status: number | null = null) {
    super(message);
    this.code = code;
    this.status = status;
  }
}

/** Validates an event and returns the exact JSON body the API accepts. */
export function buildEventPayload(input: DisclosureEventInput): DisclosureEventRequest {
  const invalid = (message: string) => new DisclosureEventError("DISCLOSURE_INVALID", message);
  if (!(EVENT_KINDS as readonly string[]).includes(input.kind)) throw invalid("unknown event kind");
  if (!isJurisdictionId(input.jurisdiction)) throw invalid("unknown jurisdiction");
  if (!POLICY_VERSION_PATTERN.test(input.policyVersion)) throw invalid("malformed policy version");
  const ruleId = input.ruleId ?? null;
  if (ruleId !== null && (!RULE_ID_PATTERN.test(ruleId) || ruleId.length > 96)) {
    throw invalid("malformed rule id");
  }
  if (!REFERENCE_PATTERN.test(input.subjectRef)) {
    throw invalid("subject_ref must be an opaque reference (letters, digits and ._:~-)");
  }
  const contentRef = input.contentRef ?? null;
  if (contentRef !== null && !REFERENCE_PATTERN.test(contentRef)) {
    throw invalid("content_ref must be an opaque reference (letters, digits and ._:~-)");
  }
  const locale = input.locale ?? null;
  if (locale !== null && !LOCALE_PATTERN.test(locale)) throw invalid("malformed locale");
  const time = input.clientTime ?? new Date();
  if (Number.isNaN(time.getTime())) throw invalid("malformed client time");
  return {
    kind: input.kind,
    jurisdiction: input.jurisdiction,
    policy_version: input.policyVersion,
    rule_id: ruleId,
    subject_ref: input.subjectRef,
    content_ref: contentRef,
    client_time: time.toISOString(),
    surface: input.surface ?? null,
    locale,
  };
}

/** The event input for showing a resolved disclosure. */
export function eventFor(
  resolved: ResolvedDisclosure,
  kind: DisclosureEventKind,
  refs: { subjectRef: string; contentRef?: string | null; surface?: Surface | null },
): DisclosureEventInput {
  return {
    kind,
    jurisdiction: resolved.jurisdiction.id,
    policyVersion: resolved.policyVersion,
    ruleId: resolved.rule.id,
    subjectRef: refs.subjectRef,
    contentRef: refs.contentRef ?? null,
    locale: resolved.locale,
    surface: refs.surface ?? "web",
  };
}

export interface DisclosureClientOptions {
  /** A publishable opk_ key restricted to disclosure:write. Never a full-access key in a browser. */
  publishableKey: string;
  apiBase?: string;
  fetch?: typeof globalThis.fetch;
  /** Wait before the single retry of a failed send (default 1 s). */
  retryDelayMs?: number;
}

function newIdempotencyKey(): string {
  const cryptoApi = globalThis.crypto;
  if (cryptoApi && typeof cryptoApi.randomUUID === "function")
    return `dse-${cryptoApi.randomUUID()}`;
  const bytes = new Uint8Array(16);
  cryptoApi.getRandomValues(bytes);
  return `dse-${Array.from(bytes, (b) => b.toString(16).padStart(2, "0")).join("")}`;
}

export class DisclosureClient {
  readonly #key: string;
  readonly #base: string;
  readonly #fetch: typeof globalThis.fetch;
  readonly #retryDelayMs: number;

  constructor(options: DisclosureClientOptions) {
    if (!KEY_PATTERN.test(options.publishableKey)) {
      throw new DisclosureEventError("DISCLOSURE_INVALID", "a publishable opk_ key is required");
    }
    const base = new URL(options.apiBase ?? DEFAULT_API_BASE);
    const loopback = ["localhost", "127.0.0.1", "[::1]"].includes(base.hostname);
    if (base.protocol !== "https:" && !(base.protocol === "http:" && loopback)) {
      throw new DisclosureEventError("DISCLOSURE_INVALID", "the API base must use https");
    }
    this.#key = options.publishableKey;
    this.#base = base.toString().replace(/\/+$/, "");
    this.#fetch = options.fetch ?? globalThis.fetch.bind(globalThis);
    this.#retryDelayMs = options.retryDelayMs ?? 1_000;
  }

  /**
   * Records one event. A network failure or a 5xx is retried once with the same
   * Idempotency-Key, so the server never records it twice.
   */
  async log(input: DisclosureEventInput): Promise<DisclosureEventReceipt> {
    const body = JSON.stringify(buildEventPayload(input));
    const key = newIdempotencyKey();
    for (let attempt = 0; ; attempt += 1) {
      let response: Response;
      try {
        response = await this.#fetch(`${this.#base}/v1/disclosures/events`, {
          method: "POST",
          credentials: "omit",
          // A label shown just before navigation should still be recorded.
          keepalive: true,
          headers: {
            Authorization: `Bearer ${this.#key}`,
            "Content-Type": "application/json",
            Accept: "application/json",
            "Idempotency-Key": key,
          },
          body,
        });
      } catch {
        if (attempt === 0) {
          await delay(this.#retryDelayMs);
          continue;
        }
        throw new DisclosureEventError("NETWORK_ERROR", "the disclosure log could not be reached");
      }
      if (response.status >= 500 && attempt === 0) {
        await delay(this.#retryDelayMs);
        continue;
      }
      const payload = (await response.json().catch(() => null)) as Record<string, unknown> | null;
      if (response.status === 201 && payload && typeof payload.event_id === "string") {
        return payload as unknown as DisclosureEventReceipt;
      }
      throw new DisclosureEventError(
        typeof payload?.code === "string" ? payload.code : `HTTP_${response.status}`,
        typeof payload?.message === "string" ? payload.message : "the event was not recorded",
        response.status,
      );
    }
  }

  /** Records that a resolved disclosure was shown, offered, applied or acknowledged. */
  logResolved(
    resolved: ResolvedDisclosure,
    kind: DisclosureEventKind,
    refs: { subjectRef: string; contentRef?: string | null; surface?: Surface | null },
  ): Promise<DisclosureEventReceipt> {
    return this.log(eventFor(resolved, kind, refs));
  }
}

function delay(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

const SUBJECT_STORAGE_KEY = "op-disclosure-subject";
let memorySubject: string | null = null;

/**
 * A random, stable-per-browser reference ("visitor:" + 16 hex) for subject_ref.
 * It identifies no one by itself; map it to your own records if you need to.
 */
export function pseudonymousSubject(storage?: Storage | null): string {
  let store: Storage | null;
  try {
    store = storage === undefined ? (globalThis.localStorage ?? null) : storage;
    const existing = store?.getItem(SUBJECT_STORAGE_KEY);
    if (existing && REFERENCE_PATTERN.test(existing)) return existing;
  } catch {
    store = null;
  }
  if (!store && memorySubject) return memorySubject;
  const bytes = new Uint8Array(8);
  globalThis.crypto.getRandomValues(bytes);
  const subject = `visitor:${Array.from(bytes, (b) => b.toString(16).padStart(2, "0")).join("")}`;
  try {
    store?.setItem(SUBJECT_STORAGE_KEY, subject);
  } catch {
    // Storage can be full or blocked; the in-memory value still works for this page.
  }
  memorySubject = subject;
  return subject;
}
