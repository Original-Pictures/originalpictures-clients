// The policy engine: pick the jurisdiction, the rule and the text to show.
// The rule text is a draft for owner and legal review (needs_legal_review on
// every rule); resolving it tells a site what to show, not that showing it
// satisfies a law.

import bundled from "../assets/policy/op.disclosure-policy.2026-10.v1.json" with { type: "json" };
import {
  JURISDICTION_IDS,
  type BadgeId,
  type DisclosureInstrument,
  type DisclosurePolicyDocument,
  type DisclosureRule,
  type JurisdictionId,
  type ObligatedParty,
  type RuleKind,
  type Timing,
} from "./policy-types.ts";

/** op.disclosure-policy.2026-10.v1, as bundled at build time. */
export const BUNDLED_POLICY = bundled as unknown as DisclosurePolicyDocument;
export const POLICY_SCHEMA = "op.disclosure-policy.2026-10.v1";

/** Which hint chose the jurisdiction. */
export type DetectionBasis = "explicit" | "region" | "timezone" | "language" | "fallback";

export interface JurisdictionHints {
  /** A server-side geolocation hint: ISO 3166-1 ("DE") or 3166-2 ("US-CA"). The most reliable. */
  region?: string | null;
  /** An IANA time zone, e.g. Intl.DateTimeFormat().resolvedOptions().timeZone. */
  timeZone?: string | null;
  /** An Accept-Language header value or navigator.languages joined with commas. */
  acceptLanguage?: string | null;
}

export interface ResolveOptions extends JurisdictionHints {
  /** A jurisdiction id, or "auto" (default) to detect one from the hints. */
  jurisdiction?: JurisdictionId | "auto";
  /** The kind of disclosure wanted (default ai_interaction_notice). */
  kind?: RuleKind;
  /** Choose an exact rule, e.g. "us-ut.sb226.regulated-occupation". */
  ruleId?: string;
  /** The preferred display locale; otherwise the Accept-Language order, then English. */
  locale?: string | null;
  /** Used when no hint matches a covered jurisdiction (default "EU"); null to resolve nothing. */
  fallback?: JurisdictionId | null;
  /** A newer document, e.g. from GET /v1/disclosures/policies. */
  policy?: DisclosurePolicyDocument;
}

export interface ResolvedDisclosure {
  policyVersion: string;
  jurisdiction: { id: JurisdictionId; name: string };
  detectedBy: DetectionBasis;
  rule: {
    id: string;
    kind: RuleKind;
    provision: string;
    obligatedParty: ObligatedParty;
    trigger: string;
    exceptions: readonly string[];
  };
  instrument: DisclosureInstrument;
  /** The draft text to show, or null for machine-readable marking. */
  text: string | null;
  /** The BCP 47 locale of `text`. */
  locale: string | null;
  form: string;
  timing: Timing;
  badgeSet: BadgeId | null;
  /** Always true until the owner clears the text. Show it to whoever ships the notice. */
  needsLegalReview: boolean;
  disclaimer: string;
}

const EU_MEMBER_STATES = new Set([
  "AT",
  "BE",
  "BG",
  "HR",
  "CY",
  "CZ",
  "DK",
  "EE",
  "FI",
  "FR",
  "DE",
  "GR",
  "EL",
  "HU",
  "IE",
  "IT",
  "LV",
  "LT",
  "LU",
  "MT",
  "NL",
  "PL",
  "PT",
  "RO",
  "SK",
  "SI",
  "ES",
  "SE",
]);

// Zones that lie wholly inside one covered jurisdiction. A US zone spans many
// states, so none maps to a state: pass `region` from server geolocation.
const ZONE_JURISDICTIONS: Readonly<Record<string, JurisdictionId>> = {
  ...Object.fromEntries(
    [
      "Europe/Vienna",
      "Europe/Brussels",
      "Europe/Sofia",
      "Europe/Zagreb",
      "Asia/Nicosia",
      "Asia/Famagusta",
      "Europe/Nicosia",
      "Europe/Prague",
      "Europe/Copenhagen",
      "Europe/Tallinn",
      "Europe/Helsinki",
      "Europe/Mariehamn",
      "Europe/Paris",
      "Europe/Berlin",
      "Europe/Busingen",
      "Europe/Athens",
      "Europe/Budapest",
      "Europe/Dublin",
      "Europe/Rome",
      "Europe/Riga",
      "Europe/Vilnius",
      "Europe/Luxembourg",
      "Europe/Malta",
      "Europe/Amsterdam",
      "Europe/Warsaw",
      "Europe/Lisbon",
      "Atlantic/Madeira",
      "Atlantic/Azores",
      "Europe/Bucharest",
      "Europe/Bratislava",
      "Europe/Ljubljana",
      "Europe/Madrid",
      "Africa/Ceuta",
      "Atlantic/Canary",
      "Europe/Stockholm",
      "America/Guadeloupe",
      "America/Martinique",
      "America/Cayenne",
      "Indian/Reunion",
      "Indian/Mayotte",
    ].map((zone) => [zone, "EU" as const]),
  ),
  "Asia/Shanghai": "CN",
  "Asia/Urumqi": "CN",
  "Asia/Chongqing": "CN",
  "Asia/Chungking": "CN",
  "Asia/Harbin": "CN",
  "Asia/Kashgar": "CN",
  PRC: "CN",
  "Asia/Seoul": "KR",
  ROK: "KR",
  "Asia/Kolkata": "IN",
  "Asia/Calcutta": "IN",
};

const COUNTRY_JURISDICTIONS: Readonly<Record<string, JurisdictionId>> = {
  CN: "CN",
  KR: "KR",
  IN: "IN",
};
// A bare language is a weak hint, so only languages spoken (almost) only there.
const LANGUAGE_JURISDICTIONS: Readonly<Record<string, JurisdictionId>> = { ko: "KR", hi: "IN" };

export function isJurisdictionId(value: unknown): value is JurisdictionId {
  return typeof value === "string" && (JURISDICTION_IDS as readonly string[]).includes(value);
}

/** Parses an Accept-Language value into tags ordered by preference. */
export function parseAcceptLanguage(header: string | null | undefined): string[] {
  if (!header) return [];
  return header
    .split(",")
    .map((part, index) => {
      const [tag = "", ...params] = part.trim().split(";");
      const q = params.map((p) => p.trim()).find((p) => p.startsWith("q="));
      const weight = q ? Number.parseFloat(q.slice(2)) : 1;
      return { tag: tag.trim(), weight: Number.isFinite(weight) ? weight : 0, index };
    })
    .filter((entry) => entry.tag && entry.tag !== "*" && entry.weight > 0)
    .sort((a, b) => b.weight - a.weight || a.index - b.index)
    .map((entry) => entry.tag);
}

function fromRegion(region: string): JurisdictionId | null {
  const code = region.trim().toUpperCase();
  if (isJurisdictionId(code)) return code;
  const country = code.split("-")[0] ?? "";
  if (EU_MEMBER_STATES.has(country)) return "EU";
  return COUNTRY_JURISDICTIONS[country] ?? null;
}

function fromLanguageTag(tag: string): JurisdictionId | null {
  const subtags = tag.split("-");
  const language = (subtags[0] ?? "").toLowerCase();
  const region = subtags.slice(1).find((part) => /^[A-Za-z]{2}$/.test(part));
  if (region) return fromRegion(region);
  return LANGUAGE_JURISDICTIONS[language] ?? null;
}

/**
 * Best-effort jurisdiction from client hints, strongest first: a server region,
 * then the time zone, then Accept-Language. A hint is not a legal determination
 * of where a person is; deployers who need certainty pass `jurisdiction`.
 */
export function detectJurisdiction(
  hints: JurisdictionHints,
): { id: JurisdictionId; basis: Exclude<DetectionBasis, "explicit" | "fallback"> } | null {
  if (hints.region) {
    const id = fromRegion(hints.region);
    if (id) return { id, basis: "region" };
  }
  if (hints.timeZone) {
    const id = ZONE_JURISDICTIONS[hints.timeZone];
    if (id) return { id, basis: "timezone" };
  }
  for (const tag of parseAcceptLanguage(hints.acceptLanguage)) {
    const id = fromLanguageTag(tag);
    if (id) return { id, basis: "language" };
  }
  return null;
}

/** The text whose locale best matches the preferences; then English; then the first. */
export function pickText(
  texts: readonly { locale: string; text: string }[],
  preferences: readonly string[],
): { locale: string; text: string } | null {
  if (texts.length === 0) return null;
  const lower = (value: string) => value.toLowerCase();
  for (const preference of preferences) {
    const exact = texts.find((text) => lower(text.locale) === lower(preference));
    if (exact) return exact;
    const language = lower(preference.split("-")[0] ?? "");
    const sameLanguage = texts.find((text) => lower(text.locale.split("-")[0] ?? "") === language);
    if (sameLanguage) return sameLanguage;
  }
  return texts.find((text) => text.locale === "en") ?? texts[0] ?? null;
}

function chooseJurisdiction(
  options: ResolveOptions,
): { id: JurisdictionId; basis: DetectionBasis } | null {
  const requested = options.jurisdiction ?? "auto";
  if (requested !== "auto") {
    if (!isJurisdictionId(requested))
      throw new RangeError(`unknown jurisdiction ${String(requested)}`);
    return { id: requested, basis: "explicit" };
  }
  const detected = detectJurisdiction(options);
  if (detected) return detected;
  const fallback = options.fallback === undefined ? "EU" : options.fallback;
  return fallback ? { id: fallback, basis: "fallback" } : null;
}

/** Every rule of `kind` that applies in the chosen jurisdiction, in document order. */
export function resolveAll(options: ResolveOptions = {}): ResolvedDisclosure[] {
  const policy = options.policy ?? BUNDLED_POLICY;
  const chosen = chooseJurisdiction(options);
  if (!chosen) return [];
  const jurisdiction = policy.jurisdictions.find((entry) => entry.id === chosen.id);
  if (!jurisdiction) return [];
  const kind = options.kind ?? "ai_interaction_notice";
  const rules = jurisdiction.rules.filter((rule) =>
    options.ruleId ? rule.id === options.ruleId : rule.kind === kind,
  );
  const preferences = [
    ...(options.locale ? [options.locale] : []),
    ...parseAcceptLanguage(options.acceptLanguage),
  ];
  return rules.map((rule) => toResolved(policy, jurisdiction, rule, chosen.basis, preferences));
}

/**
 * The first rule of `kind` in the chosen jurisdiction, or null when that
 * jurisdiction has none (e.g. no AI-interaction rule in India). Pass `ruleId`
 * where a jurisdiction has several, such as Utah's on-request and
 * regulated-occupation notices.
 */
export function resolve(options: ResolveOptions = {}): ResolvedDisclosure | null {
  return resolveAll(options)[0] ?? null;
}

function toResolved(
  policy: DisclosurePolicyDocument,
  jurisdiction: DisclosurePolicyDocument["jurisdictions"][number],
  rule: DisclosureRule,
  basis: DetectionBasis,
  preferences: readonly string[],
): ResolvedDisclosure {
  const instrument = jurisdiction.instruments.find((entry) => entry.id === rule.instrument);
  if (!instrument) throw new Error(`policy rule ${rule.id} names no instrument`);
  const text = pickText(rule.texts, preferences);
  return {
    policyVersion: policy.policy_version,
    jurisdiction: { id: jurisdiction.id, name: jurisdiction.name },
    detectedBy: basis,
    rule: {
      id: rule.id,
      kind: rule.kind,
      provision: rule.provision,
      obligatedParty: rule.obligated_party,
      trigger: rule.trigger,
      exceptions: rule.exceptions,
    },
    instrument,
    text: text?.text ?? null,
    locale: text?.locale ?? null,
    form: rule.form,
    timing: rule.timing,
    badgeSet: rule.badge_set,
    needsLegalReview: rule.needs_legal_review || policy.needs_legal_review,
    disclaimer: policy.disclaimer,
  };
}

/** The browser's own hints, or nothing on a server. */
export function browserHints(): JurisdictionHints {
  const hints: JurisdictionHints = {};
  try {
    hints.timeZone = Intl.DateTimeFormat().resolvedOptions().timeZone;
  } catch {
    // An engine without Intl time zones gives no zone hint.
  }
  if (typeof navigator !== "undefined" && Array.isArray(navigator.languages)) {
    hints.acceptLanguage = navigator.languages.join(",");
  }
  return hints;
}

/** Fetches a policy version from GET /v1/disclosures/policies (anonymous). */
export async function fetchPolicy(
  options: { apiBase?: string; version?: string; fetch?: typeof globalThis.fetch } = {},
): Promise<DisclosurePolicyDocument> {
  const base = (options.apiBase ?? "https://api.originalpictures.com").replace(/\/+$/, "");
  const query = options.version ? `?version=${encodeURIComponent(options.version)}` : "";
  const response = await (options.fetch ?? globalThis.fetch)(
    `${base}/v1/disclosures/policies${query}`,
    {
      credentials: "omit",
      headers: { Accept: "application/json" },
    },
  );
  if (!response.ok) throw new Error(`policy request failed (${response.status})`);
  const body = (await response.json()) as DisclosurePolicyDocument;
  if (body?.schema_version !== POLICY_SCHEMA) throw new Error("unexpected policy schema");
  return body;
}
