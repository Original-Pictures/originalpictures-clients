import type { PublicCheckResult, PublicVerifyPage } from "../src/types.ts";

export const STATEMENT =
  "This describes what the file declares about its origin and whether this provider's " +
  "system has a record of it. It is not a judgement of whether the content is real.";

export const PAGE: PublicVerifyPage = {
  schema_version: "op.public-verify-page.v1",
  slug: "studio-nova",
  display_name: "Studio Nova",
  logo_url: "https://dev-api.originalpictures.com/v1/public/verify-pages/studio-nova/logo",
  colours: { accent: "#0F4C5C", background: "#F7F5F0", text: "#14213D" },
  recover_own_assets: true,
  check_url: "https://dev-api.originalpictures.com/v1/public/verify-pages/studio-nova/checks",
  max_upload_bytes: 25 * 1024 * 1024,
  statement: STATEMENT,
};

export function completed(overrides: Partial<PublicCheckResult> = {}): PublicCheckResult {
  return {
    schema_version: "op.public-check.v1",
    check_id: "pchk_abcdefghijklmnop",
    state: "completed",
    page: { slug: "studio-nova", display_name: "Studio Nova" },
    media_type: "image/jpeg",
    content_credentials: {
      status: "valid",
      declared_origin: {
        signed_by: "Original Pictures",
        claim_generator: "Original Pictures",
        signed_at: "2026-10-19T09:12:03Z",
        ai_generated: true,
        digital_source_type: "trainedAlgorithmicMedia",
        software_agent: "Studio Nova Imagine 2",
        actions: ["c2pa.created"],
      },
    },
    made_with: {
      answer: "yes",
      provider_name: "Studio Nova",
      method: "c2pa_manifest",
      recovery_checked: true,
    },
    statement: STATEMENT,
    created_at: "2026-10-19T09:20:00Z",
    completed_at: "2026-10-19T09:20:02Z",
    failure_reason: null,
    ...overrides,
  };
}

export function json(body: unknown, status = 200, headers: Record<string, string> = {}): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "content-type": "application/json", ...headers },
  });
}

export interface RecordedCall {
  url: string;
  init: RequestInit;
}

/** A fetch double that answers from a queue and records every call. */
export function mockFetch(...answers: (Response | Error)[]) {
  const calls: RecordedCall[] = [];
  const fn = async (input: RequestInfo | URL, init: RequestInit = {}) => {
    calls.push({ url: String(input), init });
    const next = answers.shift();
    if (!next) throw new Error(`unexpected request ${String(input)}`);
    if (next instanceof Error) throw next;
    return next;
  };
  return Object.assign(fn as typeof fetch, { calls });
}

/** Words a public check must never use to describe content (contract § 7). */
export const VERDICT_WORDS =
  /\b(?:real|fake|authentic|genuine|verified human|deepfake detected|compliant)\b/i;
