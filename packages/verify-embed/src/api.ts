import type { PublicCheckResult, PublicVerifyPage } from "./types.ts";

/**
 * The deployed public API. Production may later move host (owner decision,
 * docs/deployment/domains.md); pass `apiBase` (or the `api-base` attribute) to
 * point at another deployment.
 */
export const DEFAULT_API_BASE = "https://dev-api.originalpictures.com";
/** op_domain.verify_pages.VERIFY_PAGE_SLUG_PATTERN */
export const SLUG_PATTERN = /^[a-z0-9](?:[a-z0-9-]{1,46})[a-z0-9]$/;
/** op_domain.verify_pages.PUBLIC_CHECK_MAX_BYTES */
export const MAX_UPLOAD_BYTES = 25 * 1024 * 1024;
const CHECK_ID_PATTERN = /^pchk_[a-z2-7]{16}$/;
/** The contract asks clients to poll a running check at most every 2 seconds. */
const MIN_POLL_INTERVAL_MS = 2_000;
const DEFAULT_TIMEOUT_MS = 5 * 60_000;

/**
 * The sentence every public answer carries (op_domain.verify_pages.
 * PUBLIC_CHECK_STATEMENT). The server's copy wins; this one is shown only
 * when no response arrived.
 */
export const CHECK_STATEMENT =
  "This describes what the file declares about its origin and whether this provider's " +
  "system has a record of it. It is not a judgement of whether the content is real.";

/**
 * Codes raised before or around a request, beside the API's own reason codes.
 * SOURCE_* codes come from loading a displayed asset for an inspection; they
 * are raised before any check request, so nothing was checked or billed.
 */
export type ClientErrorCode =
  "NETWORK_ERROR" | "CHECK_TIMEOUT" | "ABORTED" | "UNEXPECTED_RESPONSE" | SourceErrorCode;

/** Why a displayed asset could not be loaded for a check. */
export type SourceErrorCode =
  | "SOURCE_INVALID"
  | "SOURCE_UNREACHABLE"
  | "SOURCE_HTTP_ERROR"
  | "SOURCE_TOO_LARGE"
  | "SOURCE_EMPTY";

/** Address schemes a displayed asset may have; anything else is refused. */
const MEDIA_PROTOCOLS = new Set(["https:", "http:", "blob:", "data:"]);

export class VerifyError extends Error {
  override readonly name = "VerifyError";
  /** An API reason code (e.g. PUBLIC_CHECK_RATE_LIMITED) or a ClientErrorCode. */
  readonly code: string;
  readonly status: number | null;
  readonly retryAfterSeconds: number | null;
  readonly requestId: string | null;

  constructor(
    code: string,
    message: string,
    options: {
      status?: number | null;
      retryAfterSeconds?: number | null;
      requestId?: string | null;
    } = {},
  ) {
    super(message);
    this.code = code;
    this.status = options.status ?? null;
    this.retryAfterSeconds = options.retryAfterSeconds ?? null;
    this.requestId = options.requestId ?? null;
  }
}

export interface RequestOptions {
  /** API origin; defaults to DEFAULT_API_BASE. */
  apiBase?: string;
  /** Injected fetch (tests, server-side rendering). */
  fetch?: typeof globalThis.fetch;
  signal?: AbortSignal;
}

export interface VerifyOptions extends RequestOptions {
  /** The verify page slug, as in <op-verify page="studio-nova">. */
  page: string;
  /** Poll interval while a check runs; never below 2 seconds. */
  pollIntervalMs?: number;
  /** Give up polling after this long (default 5 minutes; checks expire after 15). */
  timeoutMs?: number;
  /** Refuse larger files before uploading (default 25 MB, or the page's limit). */
  maxUploadBytes?: number;
  /** Called with each non-terminal snapshot while the check runs. */
  onProgress?: (snapshot: PublicCheckResult) => void;
}

/** Normalises and validates an API origin: https, or http on a loopback host. */
export function normaliseApiBase(apiBase: string | undefined): string {
  const raw = (apiBase ?? DEFAULT_API_BASE).trim();
  let url: URL;
  try {
    url = new URL(raw);
  } catch {
    throw new VerifyError("VERIFY_PAGE_INVALID", "The API base is not a URL.");
  }
  const loopback = ["localhost", "127.0.0.1", "[::1]"].includes(url.hostname);
  if (url.protocol !== "https:" && !(url.protocol === "http:" && loopback)) {
    throw new VerifyError("VERIFY_PAGE_INVALID", "The API base must use https.");
  }
  if (url.search || url.hash || url.username || url.password) {
    throw new VerifyError("VERIFY_PAGE_INVALID", "The API base must be a plain origin.");
  }
  return url.toString().replace(/\/+$/, "");
}

export function assertSlug(slug: string): string {
  if (!SLUG_PATTERN.test(slug)) {
    throw new VerifyError("VERIFY_PAGE_INVALID", "The verify page name is not valid.");
  }
  return slug;
}

function pageUrl(apiBase: string | undefined, slug: string): string {
  return `${normaliseApiBase(apiBase)}/v1/public/verify-pages/${assertSlug(slug)}`;
}

/** Reads a verify page's public configuration (name, logo, colours, limits). */
export async function fetchVerifyPage(
  slug: string,
  options: RequestOptions = {},
): Promise<PublicVerifyPage> {
  const body = await request(pageUrl(options.apiBase, slug), { method: "GET" }, options);
  if (!isRecord(body) || body.schema_version !== "op.public-verify-page.v1") {
    throw new VerifyError("UNEXPECTED_RESPONSE", "the verify page answer was not understood");
  }
  return body as unknown as PublicVerifyPage;
}

/**
 * Checks one file against a verify page and resolves with the terminal result
 * (state `completed` or `failed`). The file goes to the public check endpoint
 * under a neutral part name; nothing else about it is sent.
 */
export async function verify(file: Blob, options: VerifyOptions): Promise<PublicCheckResult> {
  const base = pageUrl(options.apiBase, options.page);
  if (!(file instanceof Blob)) {
    throw new VerifyError("VERIFY_PAGE_INVALID", "Choose a file to check.");
  }
  if (file.size === 0) {
    throw new VerifyError("VERIFY_PAGE_INVALID", "The file is empty.");
  }
  const limit = options.maxUploadBytes ?? MAX_UPLOAD_BYTES;
  if (file.size > limit) {
    throw new VerifyError(
      "MEDIA_COMPRESSED_SIZE_LIMIT",
      `the file is larger than ${Math.floor(limit / (1024 * 1024))} MB`,
      { status: 413 },
    );
  }
  const form = new FormData();
  // The visitor's file name is not needed for the check, so it is not sent.
  form.append("file", new File([file], "upload", { type: file.type }));
  let snapshot = asCheck(await request(`${base}/checks`, { method: "POST", body: form }, options));

  const interval = Math.max(options.pollIntervalMs ?? MIN_POLL_INTERVAL_MS, MIN_POLL_INTERVAL_MS);
  const deadline = Date.now() + (options.timeoutMs ?? DEFAULT_TIMEOUT_MS);
  while (snapshot.state === "running") {
    options.onProgress?.(snapshot);
    if (Date.now() + interval > deadline) {
      throw new VerifyError("CHECK_TIMEOUT", "the check is taking too long; try again later");
    }
    await sleep(interval, options.signal);
    try {
      snapshot = asCheck(
        await request(`${base}/checks/${snapshot.check_id}`, { method: "GET" }, options),
      );
    } catch (error) {
      if (error instanceof VerifyError && error.code === "PUBLIC_CHECK_RATE_LIMITED") {
        await sleep((error.retryAfterSeconds ?? 5) * 1000, options.signal);
        continue;
      }
      throw error;
    }
  }
  return snapshot;
}

export interface FetchMediaOptions {
  /** Injected fetch (tests). */
  fetch?: typeof globalThis.fetch;
  signal?: AbortSignal;
  /** Refuse larger media without reading all of it (default 25 MB). */
  maxBytes?: number;
  /** Resolves a relative address; defaults to the document's base URL. */
  baseUrl?: string;
}

/**
 * Loads an asset the page already shows (an image or video URL) so it can be
 * checked. The browser enforces CORS: an asset whose server does not allow
 * this page's origin to read it fails with SOURCE_UNREACHABLE, which cannot be
 * told apart from a network failure. Reading stops as soon as the size limit
 * is passed, so an oversized asset is never fully downloaded.
 */
export async function fetchMedia(src: string, options: FetchMediaOptions = {}): Promise<Blob> {
  const url = resolveMediaUrl(src, options.baseUrl);
  const limit = options.maxBytes ?? MAX_UPLOAD_BYTES;
  const doFetch = options.fetch ?? globalThis.fetch;
  let response: Response;
  try {
    response = await doFetch(url, { method: "GET", mode: "cors", signal: options.signal });
  } catch {
    if (options.signal?.aborted) throw new VerifyError("ABORTED", "the check was cancelled");
    throw new VerifyError(
      "SOURCE_UNREACHABLE",
      "the media could not be loaded from this page (its server's sharing rules or the network)",
    );
  }
  if (!response.ok) {
    void response.body?.cancel().catch(() => undefined);
    throw new VerifyError("SOURCE_HTTP_ERROR", `the media server answered ${response.status}`, {
      status: response.status,
    });
  }
  const declared = Number.parseInt(response.headers.get("Content-Length") ?? "", 10);
  if (Number.isFinite(declared) && declared > limit) {
    void response.body?.cancel().catch(() => undefined);
    throw tooLarge(limit);
  }
  const type = (response.headers.get("Content-Type") ?? "").split(";")[0]?.trim() ?? "";
  const blob = await readCapped(response, limit, type, options.signal);
  if (blob.size === 0) throw new VerifyError("SOURCE_EMPTY", "the media is empty");
  return blob;
}

/**
 * Loads a displayed asset and checks it against a verify page. Each call that
 * reaches the check is billed to the page owner as one verification.
 */
export async function inspect(
  src: string,
  options: VerifyOptions & Pick<FetchMediaOptions, "baseUrl">,
): Promise<PublicCheckResult> {
  assertSlug(options.page);
  const media = await fetchMedia(src, {
    fetch: options.fetch,
    signal: options.signal,
    maxBytes: options.maxUploadBytes,
    baseUrl: options.baseUrl,
  });
  return verify(media, options);
}

function resolveMediaUrl(src: string, baseUrl: string | undefined): string {
  const base = baseUrl ?? (typeof document === "undefined" ? undefined : document.baseURI);
  let url: URL;
  try {
    url = new URL(src.trim(), base);
  } catch {
    throw new VerifyError("SOURCE_INVALID", "the media address is not a URL");
  }
  if (!src.trim() || !MEDIA_PROTOCOLS.has(url.protocol)) {
    throw new VerifyError("SOURCE_INVALID", "the media address cannot be loaded");
  }
  return url.toString();
}

function tooLarge(limit: number): VerifyError {
  return new VerifyError(
    "SOURCE_TOO_LARGE",
    `the media is larger than ${Math.floor(limit / (1024 * 1024))} MB`,
  );
}

async function readCapped(
  response: Response,
  limit: number,
  type: string,
  signal: AbortSignal | undefined,
): Promise<Blob> {
  try {
    const reader = response.body?.getReader();
    if (!reader) {
      const whole = await response.blob();
      if (whole.size > limit) throw tooLarge(limit);
      return type && whole.type !== type ? new Blob([whole], { type }) : whole;
    }
    const chunks: BlobPart[] = [];
    let total = 0;
    for (;;) {
      const { done, value } = await reader.read();
      if (done) break;
      total += value.byteLength;
      if (total > limit) {
        await reader.cancel().catch(() => undefined);
        throw tooLarge(limit);
      }
      chunks.push(value as Uint8Array<ArrayBuffer>);
    }
    return new Blob(chunks, { type });
  } catch (error) {
    if (error instanceof VerifyError) throw error;
    if (signal?.aborted) throw new VerifyError("ABORTED", "the check was cancelled");
    throw new VerifyError("SOURCE_UNREACHABLE", "the media stopped loading before it finished");
  }
}

function asCheck(body: unknown): PublicCheckResult {
  if (
    !isRecord(body) ||
    body.schema_version !== "op.public-check.v1" ||
    typeof body.check_id !== "string" ||
    !CHECK_ID_PATTERN.test(body.check_id) ||
    !["running", "completed", "failed"].includes(String(body.state))
  ) {
    throw new VerifyError("UNEXPECTED_RESPONSE", "the check answer was not understood");
  }
  return body as unknown as PublicCheckResult;
}

async function request(url: string, init: RequestInit, options: RequestOptions): Promise<unknown> {
  const doFetch = options.fetch ?? globalThis.fetch;
  let response: Response;
  try {
    response = await doFetch(url, {
      ...init,
      credentials: "omit",
      headers: { Accept: "application/json" },
      signal: options.signal,
    });
  } catch {
    if (options.signal?.aborted) throw new VerifyError("ABORTED", "the check was cancelled");
    throw new VerifyError("NETWORK_ERROR", "the verify service could not be reached");
  }
  const body = await readJson(response);
  if (response.ok) return body;
  const envelope = isRecord(body) ? body : {};
  const retryAfter = Number.parseInt(response.headers.get("Retry-After") ?? "", 10);
  throw new VerifyError(
    typeof envelope.code === "string" ? envelope.code : `HTTP_${response.status}`,
    typeof envelope.message === "string" ? envelope.message : `request failed (${response.status})`,
    {
      status: response.status,
      retryAfterSeconds: Number.isFinite(retryAfter) ? retryAfter : null,
      requestId: typeof envelope.request_id === "string" ? envelope.request_id : null,
    },
  );
}

async function readJson(response: Response): Promise<unknown> {
  const text = await response.text();
  if (!text) return null;
  try {
    return JSON.parse(text) as unknown;
  } catch {
    if (!response.ok) return null;
    throw new VerifyError("UNEXPECTED_RESPONSE", "the verify service sent an unreadable answer", {
      status: response.status,
    });
  }
}

function sleep(ms: number, signal: AbortSignal | undefined): Promise<void> {
  return new Promise((resolve, reject) => {
    if (signal?.aborted) {
      reject(new VerifyError("ABORTED", "the check was cancelled"));
      return;
    }
    const timer = setTimeout(() => {
      signal?.removeEventListener("abort", onAbort);
      resolve();
    }, ms);
    const onAbort = () => {
      clearTimeout(timer);
      reject(new VerifyError("ABORTED", "the check was cancelled"));
    };
    signal?.addEventListener("abort", onAbort, { once: true });
  });
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}
