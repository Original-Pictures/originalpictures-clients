// Shapes of the public verify-page API (op.public-verify-page.v1 and
// op.public-check.v1). They mirror PublicVerifyPageResponse and
// PublicCheckResponse in apps/api/src/op_api/routers/verify_pages.py; the
// OpenAPI document is the authority and these are a hand-kept projection so the
// embed stays dependency-free.

export interface VerifyPageColours {
  accent?: string | null;
  background?: string | null;
  text?: string | null;
}

export interface PublicVerifyPage {
  schema_version: "op.public-verify-page.v1";
  slug: string;
  display_name: string;
  logo_url: string | null;
  colours: VerifyPageColours;
  recover_own_assets: boolean;
  check_url: string;
  max_upload_bytes: number;
  statement: string;
  /**
   * The media types a check accepts (added 2026-10-19; absent from older API
   * releases). Any other type is refused before it is billed.
   */
  accepted_media_types?: string[] | null;
}

/** What the file's Content Credentials are, stated without a verdict. */
export type CredentialsStatus = "valid" | "valid_untrusted" | "invalid" | "absent";
export type MadeWithAnswer = "yes" | "no_record";
export type MadeWithMethod = "c2pa_manifest" | "watermark" | "fingerprint";

export interface DeclaredOrigin {
  signed_by: string | null;
  claim_generator: string | null;
  signed_at: string | null;
  ai_generated: boolean;
  digital_source_type: string | null;
  software_agent: string | null;
  actions: string[];
}

export interface PublicCheckResult {
  schema_version: "op.public-check.v1";
  check_id: string;
  state: "running" | "completed" | "failed";
  page: { slug: string; display_name: string };
  media_type: string | null;
  content_credentials: {
    status: CredentialsStatus;
    declared_origin: DeclaredOrigin | null;
  } | null;
  made_with: {
    answer: MadeWithAnswer;
    provider_name: string;
    method: MadeWithMethod | null;
    recovery_checked: boolean;
  } | null;
  statement: string;
  created_at: string;
  completed_at: string | null;
  failure_reason: string | null;
}
