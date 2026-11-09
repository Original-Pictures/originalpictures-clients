// Everything the package offers, without registering the element. Import
// "@originalpictures/verify" instead to get <op-verify> defined on import.

export {
  CHECK_STATEMENT,
  DEFAULT_API_BASE,
  MAX_UPLOAD_BYTES,
  SLUG_PATTERN,
  VerifyError,
  fetchMedia,
  fetchVerifyPage,
  inspect,
  verify,
  type ClientErrorCode,
  type FetchMediaOptions,
  type RequestOptions,
  type SourceErrorCode,
  type VerifyOptions,
} from "./api.ts";
export {
  describeActions,
  describeAvailability,
  describeError,
  describeMediaTypes,
  describeResult,
  describeVerifyError,
  formatUtc,
  type Availability,
  type ErrorContext,
  type OriginRow,
  type ResultView,
  type Tone,
} from "./describe.ts";
export {
  OpVerifyElement,
  TAG_NAME,
  defineOpVerify,
  type VerifyErrorEventDetail,
  type VerifyResultEventDetail,
} from "./element.ts";
export type * from "./types.ts";
