// Everything the package offers, without registering elements. Import
// "@originalpictures/disclosure" instead to get <op-ai-notice> and
// <op-ai-label> defined on import.

export * from "./policy-types.ts";
export {
  BUNDLED_POLICY,
  POLICY_SCHEMA,
  browserHints,
  detectJurisdiction,
  fetchPolicy,
  isJurisdictionId,
  parseAcceptLanguage,
  pickText,
  resolve,
  resolveAll,
  type DetectionBasis,
  type JurisdictionHints,
  type ResolveOptions,
  type ResolvedDisclosure,
} from "./policy.ts";
export {
  DEFAULT_API_BASE,
  DisclosureClient,
  DisclosureEventError,
  EVENT_KINDS,
  REFERENCE_PATTERN,
  buildEventPayload,
  eventFor,
  pseudonymousSubject,
  type DisclosureClientOptions,
  type DisclosureEventInput,
  type DisclosureEventKind,
  type DisclosureEventReceipt,
  type DisclosureEventRequest,
  type Surface,
} from "./events.ts";
export {
  BADGE_DESCRIPTIONS,
  BADGE_LABELS,
  BADGE_NOTICE,
  badgeDataUrl,
  badgeFileName,
  badgePalette,
  badgeSize,
  badgeSvg,
  type BadgeSvgOptions,
} from "./badges.ts";
export {
  badge,
  badgePlacement,
  type BadgeOverlayHandle,
  type BadgeOverlayOptions,
  type BadgePosition,
  type Placement,
} from "./overlay.ts";
export { NOTICE_TAG, OpAiNoticeElement, defineAiNotice } from "./notice.ts";
export { LABEL_TAG, OpAiLabelElement, defineAiLabel } from "./label.ts";
export type {
  DisclosureErrorDetail,
  DisclosureEventDetail,
  DisclosureLoggedDetail,
} from "./component-support.ts";
