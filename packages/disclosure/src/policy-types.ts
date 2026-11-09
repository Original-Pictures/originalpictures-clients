// Shapes of op.disclosure-policy.2026-10.v1, mirroring DisclosurePolicyDocument
// in apps/api/src/op_api/routers/disclosures.py (the OpenAPI document is the
// authority). The document itself is packages/domain/src/op_domain/resources/
// disclosure-policy/op.disclosure-policy.2026-10.v1.json, copied into assets/.

export const JURISDICTION_IDS = [
  "EU",
  "US-CA",
  "US-ME",
  "US-NH",
  "US-NY",
  "US-UT",
  "IN",
  "CN",
  "KR",
] as const;
export type JurisdictionId = (typeof JURISDICTION_IDS)[number];

export type RuleKind =
  "ai_interaction_notice" | "visible_label" | "deepfake_label" | "machine_readable_marking";
export type Timing =
  | "before_first_interaction"
  | "at_first_interaction"
  | "on_display"
  | "on_publication"
  | "on_request";
export type ObligatedParty = "provider" | "deployer" | "operator" | "platform";
export type InstrumentStatus = "in_force" | "enacted_not_in_force" | "amended" | "proposed";

export const BADGE_IDS = [
  "ai-generated",
  "ai-manipulated",
  "ai-interaction",
  "ai-assisted",
] as const;
export type BadgeId = (typeof BADGE_IDS)[number];
export const BADGE_VARIANTS = ["brand-light", "brand-dark", "neutral"] as const;
export type BadgeVariant = (typeof BADGE_VARIANTS)[number];

export interface DisclosureInstrument {
  id: string;
  title: string;
  citation: string;
  url: string | null;
  status: InstrumentStatus;
  applies_from: string | null;
}

export interface DisclosureText {
  locale: string;
  text: string;
}

export interface DisclosureRule {
  id: string;
  kind: RuleKind;
  instrument: string;
  provision: string;
  obligated_party: ObligatedParty;
  trigger: string;
  timing: Timing;
  form: string;
  texts: DisclosureText[];
  badge_set: BadgeId | null;
  exceptions: string[];
  needs_legal_review: boolean;
}

export interface DisclosureJurisdictionPolicy {
  id: JurisdictionId;
  name: string;
  instruments: DisclosureInstrument[];
  rules: DisclosureRule[];
}

export interface DisclosureBadgeSet {
  id: BadgeId;
  label: string;
  meaning: string;
  variants: BadgeVariant[];
}

export interface DisclosurePolicyDocument {
  schema_version: "op.disclosure-policy.2026-10.v1";
  policy_version: string;
  published_at: string;
  needs_legal_review: boolean;
  disclaimer: string;
  jurisdictions: DisclosureJurisdictionPolicy[];
  badge_sets: DisclosureBadgeSet[];
}
