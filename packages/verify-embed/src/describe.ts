// Turns a public check into the words the card shows. Every sentence states
// what the file *declares* and whether the page owner's system has a record of
// it; none judges the content. tests/describe.test.ts holds the vocabulary.

import { CHECK_STATEMENT, MAX_UPLOAD_BYTES, VerifyError } from "./api.ts";
import type { CredentialsStatus, MadeWithMethod, PublicCheckResult } from "./types.ts";

export type Tone = "success" | "neutral" | "warning" | "danger";

export interface OriginRow {
  label: string;
  value: string;
}

export interface ResultView {
  credentials: { tone: Tone; headline: string; detail: string };
  origin: OriginRow[];
  madeWith: { tone: Tone; question: string; headline: string; detail: string } | null;
  failure: string | null;
  statement: string;
}

const STATUS_TEXT: Readonly<
  Record<CredentialsStatus, { tone: Tone; headline: string; detail: string }>
> = {
  valid: {
    tone: "success",
    headline: "Content Credentials found",
    detail: "The manifest is intact and its signer is on the C2PA trust list.",
  },
  valid_untrusted: {
    tone: "warning",
    headline: "Content Credentials found; signer not on the trust list",
    detail:
      "The manifest is intact, but the certificate that signed it is not on the C2PA trust list.",
  },
  invalid: {
    tone: "danger",
    headline: "Content Credentials found, but they do not validate",
    detail:
      "The file or its manifest changed after signing, or the signing certificate is no longer " +
      "valid, so what it declares cannot be relied on.",
  },
  absent: {
    tone: "neutral",
    headline: "No Content Credentials found",
    detail:
      "This file carries no C2PA manifest that could be read. Many apps remove them when a file " +
      "is re-saved or shared.",
  },
};

const ACTION_NAMES: Readonly<Record<string, string>> = {
  "c2pa.created": "created",
  "c2pa.opened": "opened",
  "c2pa.placed": "placed",
  "c2pa.edited": "edited",
  "c2pa.edited.metadata": "metadata edited",
  "c2pa.converted": "converted",
  "c2pa.transcoded": "transcoded",
  "c2pa.color_adjustments": "colour adjusted",
  "c2pa.cropped": "cropped",
  "c2pa.resized": "resized",
  "c2pa.filtered": "filtered",
  "c2pa.watermarked": "watermarked",
  "c2pa.watermarked.bound": "watermarked",
  "c2pa.published": "published",
  "c2pa.repackaged": "repackaged",
  "c2pa.redacted": "redacted",
};

function madeWithEvidence(method: MadeWithMethod | null, provider: string): string {
  switch (method) {
    case "watermark":
      return `${provider}'s invisible watermark was found in it.`;
    case "fingerprint":
      return `It matches a fingerprint ${provider} stored when it was signed.`;
    case "c2pa_manifest":
    default:
      return `Its Content Credentials were signed for ${provider}.`;
  }
}

/** "2026-10-19 09:12 UTC", independent of the visitor's locale and zone. */
export function formatUtc(iso: string): string {
  const date = new Date(iso);
  if (Number.isNaN(date.getTime())) return iso;
  return `${date.toISOString().slice(0, 16).replace("T", " ")} UTC`;
}

export function describeActions(actions: readonly string[]): string {
  if (actions.length === 0) return "None listed";
  return actions.map((action) => ACTION_NAMES[action] ?? action).join(", ");
}

export function describeResult(result: PublicCheckResult): ResultView {
  const statement = result.statement || CHECK_STATEMENT;
  if (result.state === "failed" || !result.content_credentials) {
    return {
      credentials: {
        tone: "neutral",
        headline: "The check could not be completed",
        detail: describeError(result.failure_reason ?? "CHECK_FAILED"),
      },
      origin: [],
      madeWith: null,
      failure: result.failure_reason,
      statement,
    };
  }
  const declared = result.content_credentials.declared_origin;
  const origin: OriginRow[] = declared
    ? [
        { label: "Signed by", value: declared.signed_by ?? "Not stated" },
        { label: "Credentials written by", value: declared.claim_generator ?? "Not stated" },
        {
          label: "Signed at",
          value: declared.signed_at ? formatUtc(declared.signed_at) : "No trusted time",
        },
        {
          label: "Declared as AI-generated",
          value: declared.ai_generated
            ? `Yes, the signer declares it${declared.digital_source_type ? ` (${declared.digital_source_type})` : ""}`
            : "Not declared",
        },
        ...(declared.software_agent
          ? [{ label: "Generating software", value: declared.software_agent }]
          : []),
        { label: "Recorded actions", value: describeActions(declared.actions) },
      ]
    : [];

  const made = result.made_with;
  const provider = made?.provider_name ?? result.page.display_name;
  const madeWith = made
    ? made.answer === "yes"
      ? {
          tone: "success" as const,
          question: `Made with ${provider}'s system?`,
          headline: `Yes: ${provider}'s system has a record of this file`,
          detail: madeWithEvidence(made.method, provider),
        }
      : {
          tone: "neutral" as const,
          question: `Made with ${provider}'s system?`,
          headline: `No record: ${provider}'s system has no record of this file`,
          detail:
            "That does not mean it was made elsewhere or changed." +
            (made.recovery_checked
              ? ""
              : " Watermark and fingerprint search is off for this page, so a copy without " +
                "Content Credentials cannot be matched."),
        }
    : null;

  return {
    credentials: STATUS_TEXT[result.content_credentials.status],
    origin,
    madeWith,
    failure: null,
    statement,
  };
}

export interface Availability {
  tone: Tone;
  /** The inspection chip's label: whether the file carries Content Credentials. */
  label: string;
}

/**
 * The compact answer an inspection chip shows before it is expanded. It says
 * only whether credentials are present; the card says what they declare.
 */
export function describeAvailability(result: PublicCheckResult): Availability {
  if (result.state === "failed" || !result.content_credentials) {
    return { tone: "neutral", label: "Content Credentials could not be checked" };
  }
  switch (result.content_credentials.status) {
    case "absent":
      return { tone: "neutral", label: "No Content Credentials found" };
    case "invalid":
      return { tone: "danger", label: "Content Credentials that do not validate" };
    case "valid_untrusted":
      return { tone: "warning", label: "Content Credentials" };
    case "valid":
    default:
      return { tone: "success", label: "Content Credentials" };
  }
}

/** Plain names for the media types a public check can name. */
const MEDIA_TYPE_NAMES: Readonly<Record<string, string>> = {
  "image/jpeg": "JPEG",
  "image/png": "PNG",
  "image/webp": "WebP",
  "image/tiff": "TIFF",
  "image/avif": "AVIF",
  "image/heic": "HEIC",
  "image/heif": "HEIF",
  "audio/wav": "WAV",
  "audio/mp4": "M4A",
  "audio/mpeg": "MP3",
  "audio/flac": "FLAC",
  "video/mp4": "MP4 video",
  "application/pdf": "PDF",
};

const MEDIA_TYPE_TOKEN = /\b(?:image|audio|video|application)\/[a-z0-9.+-]+/gu;

/** The media types named in a sentence, in order (the API's refusal lists them). */
export function mediaTypesIn(text: string): string[] {
  return text.match(MEDIA_TYPE_TOKEN) ?? [];
}

/** "JPEG, PNG and PDF", in the order given, unknown types by their media type. */
export function describeMediaTypes(types: readonly string[]): string {
  const names = [...new Set(types.map((type) => MEDIA_TYPE_NAMES[type] ?? type))];
  if (names.length <= 1) return names.join("");
  return `${names.slice(0, -1).join(", ")} and ${names.at(-1)}`;
}

/** Context that makes a refusal's sentence specific. */
export interface ErrorContext {
  /** What the page accepts (`accepted_media_types`), when known. */
  acceptedMediaTypes?: readonly string[] | null;
  /** The type that was refused, when known. */
  mediaType?: string | null;
}

/** A visitor-facing sentence for an API reason code or a client error code. */
export function describeError(
  code: string,
  retryAfterSeconds?: number | null,
  context: ErrorContext = {},
): string {
  const accepted = context.acceptedMediaTypes?.length
    ? ` This page checks ${describeMediaTypes(context.acceptedMediaTypes)} files.`
    : "";
  if (code === "PUBLIC_CHECK_MEDIA_UNSUPPORTED") {
    const kind = context.mediaType
      ? (MEDIA_TYPE_NAMES[context.mediaType] ?? context.mediaType)
      : "this kind of file";
    return `${kind.charAt(0).toUpperCase()}${kind.slice(1)} cannot be checked here, so nothing was checked.${accepted}`;
  }
  if (code === "PUBLIC_CHECK_MONTHLY_LIMIT_REACHED") {
    return "This page has answered all the checks it offers this month. Checks resume next month.";
  }
  if (code === "PUBLIC_CHECK_RATE_LIMITED") {
    return retryAfterSeconds
      ? `Too many checks from your network. Try again in ${retryAfterSeconds} seconds.`
      : "Too many checks from your network. Try again in a minute.";
  }
  if (code === "MEDIA_COMPRESSED_SIZE_LIMIT") {
    return `This file is larger than ${MAX_UPLOAD_BYTES / (1024 * 1024)} MB.`;
  }
  if (code === "VERIFY_PAGE_NOT_FOUND") return "This verify page does not exist or is turned off.";
  if (code === "PUBLIC_CHECK_NOT_FOUND") return "The check expired. Check the file again.";
  if (code === "NETWORK_ERROR") {
    return "The verify service could not be reached. Check your connection and try again.";
  }
  if (code === "CHECK_TIMEOUT") return "The check is taking too long. Try again later.";
  if (code === "ABORTED") return "The check was cancelled.";
  if (code === "SOURCE_TOO_LARGE") {
    return `This media is larger than ${MAX_UPLOAD_BYTES / (1024 * 1024)} MB, more than a check accepts, so nothing was checked.`;
  }
  if (code === "SOURCE_INVALID") return "There is no media here to check, so nothing was checked.";
  if (code === "SOURCE_EMPTY") return "This media loaded empty, so nothing was checked.";
  if (code.startsWith("SOURCE_")) {
    return (
      "This media could not be loaded for a check from this page; its server may not allow it, " +
      "or the network failed. Nothing was checked."
    );
  }
  if (code.startsWith("MEDIA_")) return `This file type or file cannot be checked.${accepted}`;
  return "The check could not be completed. Try again.";
}

/**
 * The sentence for a failed check. A media refusal names the refused type and what
 * the page accepts: from the page's configuration when the element has it, else from
 * the API's own message, which lists them.
 */
export function describeVerifyError(
  error: unknown,
  acceptedMediaTypes?: readonly string[] | null,
): string {
  if (error instanceof VerifyError) {
    if (error.code === "VERIFY_PAGE_INVALID" && error.status === null) return error.message;
    const named = mediaTypesIn(error.message);
    const refusedType = error.code === "PUBLIC_CHECK_MEDIA_UNSUPPORTED" ? named[0] : undefined;
    const fromMessage = refusedType === undefined ? named : named.slice(1);
    return describeError(error.code, error.retryAfterSeconds, {
      acceptedMediaTypes: acceptedMediaTypes?.length ? acceptedMediaTypes : fromMessage,
      mediaType: refusedType ?? null,
    });
  }
  return describeError("UNKNOWN");
}

/**
 * Whether a file is certainly one the page refuses, so the element can say so without
 * sending (and billing) a check. Only a video file on a page that accepts no video is
 * refused here: browsers name other types inconsistently (audio/x-wav, image/jpg), and
 * the API decides those from the bytes.
 */
export function refusedBeforeUpload(
  fileType: string,
  acceptedMediaTypes: readonly string[] | null | undefined,
): boolean {
  if (!acceptedMediaTypes?.length || !fileType.startsWith("video/")) return false;
  return !acceptedMediaTypes.some((type) => type.startsWith("video/"));
}

/** The limits line under the drop zone, from what the page accepts. */
export function describeLimits(
  maxUploadBytes: number,
  acceptedMediaTypes: readonly string[] | null | undefined,
): string {
  const mb = Math.floor(maxUploadBytes / (1024 * 1024));
  const kinds = acceptedMediaTypes?.length
    ? describeKinds(acceptedMediaTypes)
    : "Images, video, audio and documents";
  return `${kinds} up to ${mb} MB. The file is used only for this check and is not stored.`;
}

function describeKinds(types: readonly string[]): string {
  const kinds: string[] = [];
  if (types.some((type) => type.startsWith("image/"))) kinds.push("images");
  if (types.some((type) => type.startsWith("video/"))) kinds.push("video");
  if (types.some((type) => type.startsWith("audio/"))) kinds.push("audio");
  if (types.some((type) => type.startsWith("application/"))) kinds.push("documents");
  const text =
    kinds.length <= 1 ? kinds.join("") : `${kinds.slice(0, -1).join(", ")} and ${kinds.at(-1)}`;
  return text ? `${text.charAt(0).toUpperCase()}${text.slice(1)}` : "Files";
}
