/** Typed TypeScript SDK for the complete Original Pictures public API. */

import { hmac } from "@noble/hashes/hmac.js";
import { sha256 } from "@noble/hashes/sha2.js";
import { bytesToHex, utf8ToBytes } from "@noble/hashes/utils.js";

import {
  PUBLIC_API_OPERATIONS,
  type ExecutablePublicApiOperationId,
  type PublicApiOperationId,
  type PublicApiOperationModels,
} from "./generated/public-api.js";

export * from "./generated/public-api.js";

export const SDK_STATUS = "complete" as const;
export const SDK_TYPED_OPERATION_COUNT = PUBLIC_API_OPERATIONS.length;
export const SDK_EXECUTABLE_OPERATION_COUNT = PUBLIC_API_OPERATIONS.filter(
  (operation) => operation.executable,
).length;
export const DEFAULT_MAX_RESPONSE_BYTES = 16 * 1024 * 1024;
export const DEFAULT_MAX_TRANSFER_BYTES = 5 * 1024 * 1024 * 1024;

export class OriginalPicturesError extends Error {}
export class ConfigurationError extends OriginalPicturesError {}
export class TransportError extends OriginalPicturesError {}
export class DeadlineExceededError extends TransportError {}
export class CancelledError extends OriginalPicturesError {}
export class IntegrityError extends OriginalPicturesError {}
export class ResponseTooLargeError extends OriginalPicturesError {}

export class ApiError extends OriginalPicturesError {
  public constructor(
    message: string,
    public readonly statusCode: number,
    public readonly code?: string,
    public readonly requestId?: string,
    public readonly retryable?: boolean,
    public readonly fieldDetails: Readonly<Record<string, string>> = {},
    public readonly documentationUrl?: string,
    public readonly jobReference?: string,
    public readonly validationErrors: ReadonlyArray<Readonly<Record<string, unknown>>> = [],
  ) {
    super(message);
  }
}
export class AuthenticationError extends ApiError {}
export class PermissionDeniedError extends ApiError {}
export class NotFoundError extends ApiError {}
export class ConflictError extends ApiError {}
export class ValidationError extends ApiError {}
export class RateLimitError extends ApiError {}
export class ServiceUnavailableError extends ApiError {}

interface CommonRequestOptions<Id extends ExecutablePublicApiOperationId> {
  readonly parameters?: PublicApiOperationModels[Id]["parameters"];
  readonly headers?: PublicApiOperationModels[Id]["headers"];
  readonly signal?: AbortSignal;
}

export type RequestOptions<Id extends ExecutablePublicApiOperationId> = CommonRequestOptions<Id> &
  (PublicApiOperationModels[Id]["request"] extends null
    ? { readonly body?: never }
    : { readonly body: PublicApiOperationModels[Id]["request"] });

export type OperationMethods = {
  readonly [Id in ExecutablePublicApiOperationId]: (
    ...args: PublicApiOperationModels[Id]["request"] extends null
      ? [options?: RequestOptions<Id>]
      : [options: RequestOptions<Id>]
  ) => Promise<PublicApiOperationModels[Id]["response"]>;
};

export interface ClientOptions {
  readonly baseUrl: string;
  readonly apiKey?: string;
  readonly timeoutMs?: number;
  readonly maxResponseBytes?: number;
  readonly fetch?: typeof globalThis.fetch;
}

type Operation = (typeof PUBLIC_API_OPERATIONS)[number];
const operationById = new Map(
  PUBLIC_API_OPERATIONS.map((operation) => [operation.operationId, operation]),
);

export class OriginalPicturesClient {
  readonly operations: OperationMethods;
  private readonly baseUrl: string;
  private readonly apiKey?: string;
  private readonly timeoutMs: number;
  private readonly maxResponseBytes: number;
  private readonly fetchImplementation: typeof globalThis.fetch;

  public constructor(options: ClientOptions) {
    let baseUrl: URL;
    try {
      baseUrl = new URL(options.baseUrl);
    } catch (error) {
      throw new ConfigurationError("baseUrl must be an absolute HTTP(S) URL", { cause: error });
    }
    if (
      !new Set(["http:", "https:"]).has(baseUrl.protocol) ||
      baseUrl.username !== "" ||
      baseUrl.password !== "" ||
      baseUrl.search !== "" ||
      baseUrl.hash !== "" ||
      options.baseUrl.includes("?") ||
      options.baseUrl.includes("#")
    ) {
      throw new ConfigurationError(
        "baseUrl must be an absolute HTTP(S) URL without a query or fragment",
      );
    }
    if (options.apiKey?.includes("\n") || options.apiKey?.includes("\r")) {
      throw new ConfigurationError("apiKey is invalid");
    }
    this.baseUrl = baseUrl.href.replace(/\/$/, "");
    this.apiKey = options.apiKey;
    this.timeoutMs = options.timeoutMs ?? 30_000;
    this.maxResponseBytes = options.maxResponseBytes ?? DEFAULT_MAX_RESPONSE_BYTES;
    if (!Number.isFinite(this.timeoutMs) || this.timeoutMs <= 0)
      throw new ConfigurationError("timeoutMs must be positive");
    if (!Number.isSafeInteger(this.maxResponseBytes) || this.maxResponseBytes <= 0)
      throw new ConfigurationError("maxResponseBytes must be a positive safe integer");
    this.fetchImplementation = options.fetch ?? globalThis.fetch;
    this.operations = new Proxy({} as OperationMethods, {
      get: (_target, property) => {
        if (typeof property !== "string" || !operationById.has(property as PublicApiOperationId)) {
          return undefined;
        }
        const operation = operationById.get(property as PublicApiOperationId);
        if (!operation?.executable) return undefined;
        return (requestOptions?: RequestOptions<ExecutablePublicApiOperationId>) =>
          this.request(
            property as ExecutablePublicApiOperationId,
            requestOptions as RequestOptions<ExecutablePublicApiOperationId>,
          );
      },
    });
  }

  public async request<Id extends ExecutablePublicApiOperationId>(
    operationId: Id,
    ...args: PublicApiOperationModels[Id]["request"] extends null
      ? [options?: RequestOptions<Id>]
      : [options: RequestOptions<Id>]
  ): Promise<PublicApiOperationModels[Id]["response"]> {
    const options = (args[0] ?? {}) as RequestOptions<Id>;
    const operation = operationById.get(operationId);
    if (!operation) throw new TypeError(`unknown generated operation: ${operationId}`);
    const usesBearer = usesBearerAuth(operation);
    if (usesBearer && !this.apiKey) {
      throw new ConfigurationError("this operation requires an Original Pictures API key");
    }
    const { path, query } = requestParts(
      operation,
      options.parameters as Record<string, unknown> | undefined,
    );
    const headers = new Headers(options.headers as HeadersInit | undefined);
    for (const name of headers.keys()) {
      if (["authorization", "host", "content-length"].includes(name.toLowerCase())) {
        throw new TypeError("generated operation headers may not override transport authority");
      }
    }
    if (usesBearer && this.apiKey) headers.set("Authorization", `Bearer ${this.apiKey}`);
    if (operation.requestContentTypes.length) headers.set("Content-Type", "application/json");
    const abort = abortScope(options.signal, this.timeoutMs, "request");
    try {
      const response = await this.fetchImplementation(this.baseUrl + path + query, {
        method: operation.method,
        headers,
        body: operation.requestContentTypes.length
          ? JSON.stringify(options.body ?? null)
          : undefined,
        redirect: "manual",
        signal: abort.signal,
      });
      const bytes = await readBounded(response.body, this.maxResponseBytes);
      if (!response.ok) throw apiError(response, bytes);
      if (response.status === 204 || bytes.length === 0) {
        return undefined as unknown as PublicApiOperationModels[Id]["response"];
      }
      try {
        return JSON.parse(
          new TextDecoder().decode(bytes),
        ) as PublicApiOperationModels[Id]["response"];
      } catch (error) {
        throw new TransportError("Original Pictures returned an invalid JSON response", {
          cause: error,
        });
      }
    } catch (error) {
      throwStableTransport(error, abort, "Original Pictures request");
    } finally {
      abort.cleanup();
    }
  }

  /** Dispatch to the explicit browser Blob or Node streaming strategy. */
  public async upload(
    url: string,
    source: AsyncIterable<Uint8Array> | Iterable<Uint8Array> | Uint8Array | Blob,
    options: TransferOptions,
  ): Promise<TransferResult> {
    if (typeof Blob !== "undefined" && source instanceof Blob)
      return this.uploadBlob(url, source, options);
    return this.uploadNodeStream(
      url,
      source as AsyncIterable<Uint8Array> | Iterable<Uint8Array> | Uint8Array,
      options,
    );
  }

  /** Browser-safe upload: hashes the Blob before fetch and sets no forbidden headers/options. */
  public async uploadBlob(
    url: string,
    source: Blob,
    options: TransferOptions,
  ): Promise<TransferResult> {
    validateTransfer(url, options);
    if (source.size !== options.byteLength)
      throw new IntegrityError("upload Blob length does not match authenticated length");
    const abort = abortScope(
      options.signal,
      options.timeoutMs ?? this.timeoutMs,
      "transfer upload",
    );
    try {
      const actualSha256 = await hashReadableStream(
        source.stream(),
        options.byteLength,
        abort.signal,
      );
      if (actualSha256 !== options.sha256)
        throw new IntegrityError("upload Blob failed preflight SHA-256 verification");
      const response = await this.fetchImplementation(url, {
        method: "PUT",
        headers: transferHeaders(options.headers),
        body: source,
        redirect: "manual",
        signal: abort.signal,
      });
      await readBounded(response.body, Math.min(this.maxResponseBytes, 1024 * 1024));
      if (!response.ok)
        throw new TransportError(`transfer upload failed with status ${response.status}`);
      return { byteLength: source.size, sha256: actualSha256 };
    } catch (error) {
      return throwStableTransport(error, abort, "transfer upload");
    } finally {
      abort.cleanup();
    }
  }

  /** Node Fetch streaming upload: uses the Node-only duplex request extension explicitly. */
  public async uploadNodeStream(
    url: string,
    source: AsyncIterable<Uint8Array> | Iterable<Uint8Array> | Uint8Array,
    options: TransferOptions,
  ): Promise<TransferResult> {
    validateTransfer(url, options);
    const headers = transferHeaders(options.headers);
    headers.set("Content-Length", String(options.byteLength));
    const abort = abortScope(
      options.signal,
      options.timeoutMs ?? this.timeoutMs,
      "transfer upload",
    );
    const hash = sha256.create();
    let sent = 0;
    const iterator = byteIterator(source);
    const body = new ReadableStream<Uint8Array>({
      async pull(controller) {
        const next = await iterator.next();
        if (next.done) return controller.close();
        sent += next.value.length;
        if (sent > options.byteLength)
          return controller.error(new IntegrityError("upload exceeded authenticated length"));
        hash.update(next.value);
        controller.enqueue(next.value);
      },
      async cancel() {
        await closeAsyncIterator(iterator);
      },
    });
    try {
      const response = await this.fetchImplementation(url, {
        method: "PUT",
        headers,
        body,
        redirect: "manual",
        signal: abort.signal,
        ...({ duplex: "half" } as object),
      });
      await readBounded(response.body, Math.min(this.maxResponseBytes, 1024 * 1024));
      if (!response.ok)
        throw new TransportError(`transfer upload failed with status ${response.status}`);
      const actualSha256 = bytesToHex(hash.digest());
      if (sent !== options.byteLength || actualSha256 !== options.sha256) {
        throw new IntegrityError("uploaded bytes failed length or SHA-256 verification");
      }
      return { byteLength: sent, sha256: actualSha256 };
    } catch (error) {
      return throwStableTransport(error, abort, "transfer upload");
    } finally {
      await closeAsyncIterator(iterator);
      abort.cleanup();
    }
  }

  public async download(url: string, options: DownloadOptions): Promise<TransferResult> {
    validateTransfer(url, options);
    const abort = abortScope(
      options.signal,
      options.timeoutMs ?? this.timeoutMs,
      "transfer download",
    );
    let reader: ReadableStreamDefaultReader<Uint8Array> | undefined;
    let sinkAborted = false;
    const hash = sha256.create();
    let received = 0;
    try {
      const response = await this.fetchImplementation(url, {
        method: "GET",
        headers: transferHeaders(options.headers),
        redirect: "manual",
        signal: abort.signal,
      });
      if (!response.ok)
        throw new TransportError(`transfer download failed with status ${response.status}`);
      const declared = response.headers.get("content-length");
      if (declared !== null && Number(declared) !== options.byteLength) {
        throw new IntegrityError("download Content-Length does not match authenticated length");
      }
      reader = response.body?.getReader();
      while (reader) {
        const { done, value } = await reader.read();
        if (done) break;
        received += value.length;
        if (received > options.byteLength)
          throw new IntegrityError("download exceeded authenticated length");
        hash.update(value);
        await options.sink?.write(value);
      }
      const actualSha256 = bytesToHex(hash.digest());
      if (received !== options.byteLength || actualSha256 !== options.sha256) {
        throw new IntegrityError("downloaded bytes failed length or SHA-256 verification");
      }
      await options.sink?.commit();
      return { byteLength: received, sha256: actualSha256 };
    } catch (error) {
      if (options.sink) {
        sinkAborted = true;
        await swallowCleanup(() => options.sink?.abort(error));
      }
      if (reader) {
        const activeReader = reader;
        await swallowCleanup(() => activeReader.cancel(error));
      }
      return throwStableTransport(error, abort, "transfer download");
    } finally {
      await swallowCleanup(() => reader?.releaseLock());
      if (options.sink && !sinkAborted && abort.signal.aborted) {
        await swallowCleanup(() => options.sink?.abort(abort.signal.reason));
      }
      abort.cleanup();
    }
  }
}

export interface TransferOptions {
  readonly byteLength: number;
  readonly sha256: string;
  readonly headers?: HeadersInit;
  readonly maxBytes?: number;
  readonly signal?: AbortSignal;
  readonly timeoutMs?: number;
}
export interface DownloadOptions extends TransferOptions {
  /** Writes must remain staged until `commit`; failures call `abort` and never `commit`. */
  readonly sink?: StagedDownloadSink;
}
export interface StagedDownloadSink {
  write(chunk: Uint8Array): void | Promise<void>;
  commit(): void | Promise<void>;
  abort(reason: unknown): void | Promise<void>;
}
export interface TransferResult {
  readonly byteLength: number;
  readonly sha256: string;
}

export function idempotencyKey(prefix = "sdk"): string {
  const value = `${prefix}-${crypto.randomUUID()}`;
  if (!/^[\x21-\x7e]{1,255}$/.test(value)) throw new TypeError("invalid idempotency-key prefix");
  return value;
}

const SIGN_JOB_ID = /^job_[a-z2-7]{16}$/;
const VERIFY_JOB_ID = /^vjob_[a-z2-7]{16}$/;
const VERIFY_EVIDENCE_ID = /^vfy_[a-z2-7]{16}$/;
const SIGN_TERMINAL = new Set(["completed", "failed", "rejected", "canceled", "expired"]);
const SIGN_STATES = new Set([
  "accepted",
  "queued",
  "running",
  "cancel_requested",
  ...SIGN_TERMINAL,
]);
const VERIFY_TERMINAL = new Set(["completed", "failed"]);
const VERIFY_STATES = new Set(["accepted", "running", ...VERIFY_TERMINAL]);

// Typed as ``object`` so a generated response interface (``JobResponse``, which has no
// index signature) passes straight to ``poll`` under ``tsc --strict``; the checks below
// read it as an untrusted record either way.
export function signJobTerminal(value: object): boolean {
  const snapshot = value as Readonly<Record<string, unknown>>;
  if (typeof snapshot.job_id !== "string" || !SIGN_JOB_ID.test(snapshot.job_id))
    throw new TypeError("Sign snapshot requires a job_ identifier");
  if (typeof snapshot.state !== "string" || !SIGN_STATES.has(snapshot.state))
    throw new TypeError("Sign snapshot has an unsupported lifecycle state");
  if (snapshot.state === "completed") {
    if (typeof snapshot.result !== "object" || snapshot.result === null)
      throw new TypeError("completed Sign snapshot requires a result");
    const evidenceId = (snapshot.result as Readonly<Record<string, unknown>>).verification_id;
    if (typeof evidenceId !== "string" || !VERIFY_EVIDENCE_ID.test(evidenceId))
      throw new TypeError("completed Sign result requires ready vfy_ evidence");
  } else if (snapshot.result != null) {
    throw new TypeError("non-completed Sign snapshot cannot expose a result");
  }
  return SIGN_TERMINAL.has(snapshot.state);
}

export function verificationJobTerminal(value: object): boolean {
  const snapshot = value as Readonly<Record<string, unknown>>;
  if (typeof snapshot.verification_id !== "string" || !VERIFY_JOB_ID.test(snapshot.verification_id))
    throw new TypeError("public Verify snapshot requires a vjob_ identifier");
  if (typeof snapshot.state !== "string" || !VERIFY_STATES.has(snapshot.state))
    throw new TypeError("public Verify snapshot has an unsupported lifecycle state");
  if (snapshot.state === "completed") {
    if (typeof snapshot.evidence_id !== "string" || !VERIFY_EVIDENCE_ID.test(snapshot.evidence_id))
      throw new TypeError("completed public Verify job requires ready vfy_ evidence");
  } else if (snapshot.evidence_id != null) {
    throw new TypeError("non-completed public Verify job cannot expose vfy_ evidence");
  }
  return VERIFY_TERMINAL.has(snapshot.state);
}

export async function poll<T>(
  fetchValue: (signal: AbortSignal) => Promise<T>,
  done: (value: T) => boolean,
  options: {
    timeoutMs?: number;
    intervalMs?: number;
    maxAttempts?: number;
    signal?: AbortSignal;
  } = {},
): Promise<T> {
  const timeoutMs = options.timeoutMs ?? 60_000;
  const intervalMs = options.intervalMs ?? 1_000;
  const maxAttempts = options.maxAttempts ?? 120;
  if (timeoutMs <= 0 || intervalMs < 0 || maxAttempts <= 0)
    throw new TypeError("invalid polling bounds");
  const deadline = performance.now() + timeoutMs;
  for (let attempt = 0; attempt < maxAttempts; attempt += 1) {
    if (options.signal?.aborted) throw new CancelledError("polling cancelled");
    const remainingBeforeFetch = deadline - performance.now();
    if (remainingBeforeFetch <= 0) break;
    const fetchAbort = abortScope(options.signal, remainingBeforeFetch, "polling");
    let value: T;
    try {
      value = await raceWithAbort(fetchValue(fetchAbort.signal), fetchAbort.signal);
    } catch (error) {
      if (fetchAbort.timedOut()) throw new DeadlineExceededError("polling deadline exceeded");
      if (fetchAbort.signal.aborted) throw new CancelledError("polling cancelled");
      throw error;
    } finally {
      fetchAbort.cleanup();
    }
    if (done(value)) return value;
    const remaining = deadline - performance.now();
    if (remaining <= 0 || attempt + 1 >= maxAttempts) break;
    await sleepWithSignal(Math.min(intervalMs * 1.5 ** attempt, 5_000, remaining), options.signal);
  }
  throw new DeadlineExceededError("polling deadline exceeded");
}

export function verifyWebhook(
  body: Uint8Array,
  options: {
    secret: Uint8Array | string;
    eventId: string;
    timestamp: number;
    signature: string;
    toleranceSeconds?: number;
    now?: number;
  },
): void {
  const secret = typeof options.secret === "string" ? utf8ToBytes(options.secret) : options.secret;
  if (
    body.length > 256 * 1024 ||
    secret.length < 32 ||
    !Number.isSafeInteger(options.timestamp) ||
    options.timestamp < 0 ||
    !Number.isFinite(options.toleranceSeconds ?? 300) ||
    (options.toleranceSeconds ?? 300) < 0 ||
    options.eventId.length === 0 ||
    options.eventId.includes(".") ||
    [...options.eventId].some((character) => character.charCodeAt(0) > 0x7f)
  )
    throw new ValidationError("invalid webhook inputs", 400);
  const now = options.now ?? Math.floor(Date.now() / 1000);
  if (Math.abs(now - options.timestamp) > (options.toleranceSeconds ?? 300))
    throw new ValidationError("webhook timestamp outside tolerance", 400);

  const legacyPrefix = utf8ToBytes(`${options.timestamp}.${options.eventId}.`);
  const legacyMessage = new Uint8Array(legacyPrefix.length + body.length);
  legacyMessage.set(legacyPrefix);
  legacyMessage.set(body, legacyPrefix.length);
  const legacyExpected = `v1=${bytesToHex(hmac(sha256, secret, legacyMessage))}`;

  const standardKey = standardWebhookKey(secret);
  let standardExpected: string | undefined;
  if (standardKey) {
    const standardPrefix = utf8ToBytes(`${options.eventId}.${options.timestamp}.`);
    const standardMessage = new Uint8Array(standardPrefix.length + body.length);
    standardMessage.set(standardPrefix);
    standardMessage.set(body, standardPrefix.length);
    standardExpected = `v1,${bytesToBase64(hmac(sha256, standardKey, standardMessage))}`;
  }

  let valid = false;
  for (const candidate of options.signature.split(/\s+/u).filter(Boolean)) {
    if (candidate.startsWith("v1,") && standardExpected)
      valid = constantTimeEqual(standardExpected, candidate) || valid;
    else if (candidate.startsWith("v1="))
      valid = constantTimeEqual(legacyExpected, candidate) || valid;
  }
  if (!valid) throw new ValidationError("webhook signature invalid", 400);
}

function standardWebhookKey(secret: Uint8Array): Uint8Array | undefined {
  let rendered: string;
  try {
    rendered = new TextDecoder("ascii", { fatal: true }).decode(secret);
  } catch {
    return secret.length >= 24 && secret.length <= 64 ? secret : undefined;
  }
  if (rendered.startsWith("whsec_")) {
    const decoded = decodeBase64(rendered.slice("whsec_".length));
    return decoded && decoded.length >= 24 && decoded.length <= 64 ? decoded : undefined;
  }
  return secret.length >= 24 && secret.length <= 64 ? secret : undefined;
}

function decodeBase64(value: string): Uint8Array | undefined {
  if (!/^[A-Za-z0-9+/_-]+={0,2}$/u.test(value)) return undefined;
  const normalized = value.replaceAll("-", "+").replaceAll("_", "/");
  if (normalized.length % 4 === 1) return undefined;
  const padded = normalized.padEnd(normalized.length + ((4 - (normalized.length % 4)) % 4), "=");
  try {
    return Uint8Array.from(atob(padded), (character) => character.charCodeAt(0));
  } catch {
    return undefined;
  }
}

function bytesToBase64(value: Uint8Array): string {
  return btoa(String.fromCharCode(...value));
}

function requestParts(
  operation: Operation,
  parameters?: Record<string, unknown>,
): { path: string; query: string } {
  const remaining = { ...(parameters ?? {}) };
  let path: string = operation.path;
  for (const match of path.matchAll(/\{([^{}]+)\}/g)) {
    const name = match[1];
    if (!name || remaining[name] === undefined || remaining[name] === null)
      throw new TypeError(`missing required path parameter: ${name ?? "unknown"}`);
    path = path.replace(`{${name}}`, encodeURIComponent(String(remaining[name])));
    delete remaining[name];
  }
  const query = new URLSearchParams();
  for (const [name, value] of Object.entries(remaining)) {
    if (value === undefined || value === null) continue;
    if (Array.isArray(value)) value.forEach((item) => query.append(name, String(item)));
    else query.append(name, String(value));
  }
  const encoded = query.toString();
  return { path, query: encoded ? `?${encoded}` : "" };
}

function usesBearerAuth(operation: Operation): boolean {
  if (!operation.executable) {
    const schemes = [...new Set(operation.securityAlternatives.flat())].sort().join(", ");
    throw new ConfigurationError(
      `operation ${operation.operationId} is typed but intentionally non-callable; ` +
        `it requires exact raw-body security scheme(s): ${schemes || "unknown"}`,
    );
  }
  const alternatives: readonly (readonly string[])[] = operation.securityAlternatives;
  if (alternatives.length === 0 || alternatives.some((alternative) => alternative.length === 0))
    return false;
  if (
    alternatives.some((alternative) => alternative.length === 1 && alternative[0] === "bearerAuth")
  )
    return true;
  throw new ConfigurationError(
    `operation ${operation.operationId} has no supported security alternative`,
  );
}

interface AbortScope {
  readonly signal: AbortSignal;
  readonly timedOut: () => boolean;
  readonly cleanup: () => void;
}

function abortScope(signal: AbortSignal | undefined, timeoutMs: number, label: string): AbortScope {
  if (!Number.isFinite(timeoutMs) || timeoutMs <= 0)
    throw new ConfigurationError(`${label} timeout must be positive`);
  if (signal?.aborted) throw new CancelledError(`${label} cancelled`);
  const controller = new AbortController();
  let didTimeOut = false;
  const timeout = setTimeout(() => {
    didTimeOut = true;
    controller.abort(new DeadlineExceededError(`${label} deadline exceeded`));
  }, timeoutMs);
  const onAbort = () => controller.abort(signal?.reason);
  signal?.addEventListener("abort", onAbort, { once: true });
  return {
    signal: controller.signal,
    timedOut: () => didTimeOut,
    cleanup: () => {
      clearTimeout(timeout);
      signal?.removeEventListener("abort", onAbort);
    },
  };
}

function throwStableTransport(error: unknown, abort: AbortScope, label: string): never {
  if (abort.timedOut()) throw new DeadlineExceededError(`${label} deadline exceeded`);
  if (abort.signal.aborted) throw new CancelledError(`${label} cancelled`);
  if (error instanceof OriginalPicturesError) throw error;
  throw new TransportError(`${label} failed`, { cause: error });
}

async function readBounded(
  body: ReadableStream<Uint8Array> | null,
  maxBytes: number,
): Promise<Uint8Array> {
  if (!body) return new Uint8Array();
  const reader = body.getReader();
  const chunks: Uint8Array[] = [];
  let total = 0;
  try {
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      total += value.length;
      if (total > maxBytes) throw new ResponseTooLargeError("response exceeded configured bound");
      chunks.push(value);
    }
  } catch (error) {
    await swallowCleanup(() => reader.cancel(error));
    throw error;
  } finally {
    await swallowCleanup(() => reader.releaseLock());
  }
  const output = new Uint8Array(total);
  let offset = 0;
  for (const chunk of chunks) {
    output.set(chunk, offset);
    offset += chunk.length;
  }
  return output;
}

async function swallowCleanup(cleanup: () => void | Promise<void> | undefined): Promise<void> {
  try {
    await cleanup();
  } catch {
    /* Cleanup must never replace the primary SDK result or failure. */
  }
}

async function raceWithAbort<T>(promise: Promise<T>, signal: AbortSignal): Promise<T> {
  if (signal.aborted) throw signal.reason;
  return new Promise<T>((resolve, reject) => {
    const cleanup = () => signal.removeEventListener("abort", onAbort);
    const onAbort = () => {
      cleanup();
      reject(signal.reason);
    };
    signal.addEventListener("abort", onAbort, { once: true });
    promise.then(
      (value) => {
        cleanup();
        resolve(value);
      },
      (error: unknown) => {
        cleanup();
        reject(error);
      },
    );
  });
}

function sleepWithSignal(delayMs: number, signal?: AbortSignal): Promise<void> {
  return new Promise<void>((resolve, reject) => {
    const cleanup = () => {
      clearTimeout(timer);
      signal?.removeEventListener("abort", onAbort);
    };
    const onAbort = () => {
      cleanup();
      reject(new CancelledError("polling cancelled"));
    };
    const timer = setTimeout(() => {
      cleanup();
      resolve();
    }, delayMs);
    signal?.addEventListener("abort", onAbort, { once: true });
    if (signal?.aborted) onAbort();
  });
}

function apiError(response: Response, body: Uint8Array): ApiError {
  const classes: Record<number, typeof ApiError> = {
    401: AuthenticationError,
    402: PermissionDeniedError,
    403: PermissionDeniedError,
    404: NotFoundError,
    409: ConflictError,
    410: ConflictError,
    400: ValidationError,
    413: ValidationError,
    422: ValidationError,
    429: RateLimitError,
  };
  const ErrorClass =
    classes[response.status] ?? (response.status >= 500 ? ServiceUnavailableError : ApiError);
  let code: string | undefined;
  let requestId = response.headers.get("x-request-id") ?? undefined;
  let retryable: boolean | undefined;
  let fieldDetails: Record<string, string> = {};
  let documentationUrl: string | undefined;
  let jobReference: string | undefined;
  let validationErrors: ReadonlyArray<Readonly<Record<string, unknown>>> = [];
  try {
    const payload = JSON.parse(new TextDecoder().decode(body)) as Record<string, unknown>;
    const candidate = payload.code ?? payload.reason_code;
    if (typeof candidate === "string" && candidate.length <= 128) code = candidate;
    if (!requestId && typeof payload.request_id === "string" && payload.request_id.length <= 2048)
      requestId = payload.request_id;
    if (typeof payload.retryable === "boolean") retryable = payload.retryable;
    if (typeof payload.documentation_url === "string" && payload.documentation_url.length <= 2048)
      documentationUrl = payload.documentation_url;
    if (typeof payload.job_reference === "string" && payload.job_reference.length <= 2048)
      jobReference = payload.job_reference;
    if (payload.field_details && typeof payload.field_details === "object") {
      fieldDetails = Object.fromEntries(
        Object.entries(payload.field_details)
          .filter(([name, value]) => name.length <= 128 && typeof value === "string")
          .map(([name, value]) => [name, (value as string).slice(0, 512)]),
      );
    }
    if (Array.isArray(payload.detail)) {
      validationErrors = payload.detail
        .filter(
          (item): item is Record<string, unknown> => item !== null && typeof item === "object",
        )
        .map((item) =>
          Object.fromEntries(
            Object.entries(item).filter(
              ([name, value]) =>
                ["loc", "type"].includes(name) &&
                (typeof value === "string" || Array.isArray(value)),
            ),
          ),
        );
    }
  } catch {
    /* stable fallback */
  }
  return new ErrorClass(
    "Original Pictures API request failed",
    response.status,
    code,
    requestId,
    retryable,
    fieldDetails,
    documentationUrl,
    jobReference,
    validationErrors,
  );
}

function validateTransfer(url: string, options: TransferOptions): void {
  const parsed = new URL(url);
  if (
    parsed.username ||
    parsed.password ||
    (parsed.protocol !== "https:" &&
      !(
        parsed.protocol === "http:" && ["localhost", "127.0.0.1", "[::1]"].includes(parsed.hostname)
      ))
  )
    throw new TypeError("transfer URL must use HTTPS");
  if (
    !Number.isSafeInteger(options.byteLength) ||
    options.byteLength < 0 ||
    options.byteLength > (options.maxBytes ?? DEFAULT_MAX_TRANSFER_BYTES)
  )
    throw new TypeError("transfer byte length outside bound");
  if (!/^[0-9a-f]{64}$/.test(options.sha256))
    throw new TypeError("sha256 must be lowercase hexadecimal");
  if (
    options.timeoutMs !== undefined &&
    (!Number.isFinite(options.timeoutMs) || options.timeoutMs <= 0)
  )
    throw new TypeError("transfer timeout must be positive");
}

function transferHeaders(input?: HeadersInit): Headers {
  const headers = new Headers(input);
  for (const name of headers.keys())
    if (["authorization", "proxy-authorization", "cookie"].includes(name.toLowerCase()))
      throw new TypeError("API credentials must never be forwarded to transfer URLs");
  return headers;
}

function byteIterator(
  source: AsyncIterable<Uint8Array> | Iterable<Uint8Array> | Uint8Array,
): AsyncIterator<Uint8Array> {
  if (source instanceof Uint8Array) {
    return asyncFromIterable([source]);
  }
  if (Symbol.asyncIterator in source) {
    return (source as AsyncIterable<Uint8Array>)[Symbol.asyncIterator]();
  }
  return asyncFromIterable(source as Iterable<Uint8Array>);
}

async function* asyncFromIterable(
  source: Iterable<Uint8Array>,
): AsyncGenerator<Uint8Array, void, unknown> {
  yield* source;
}

async function closeAsyncIterator(iterator: AsyncIterator<Uint8Array>): Promise<void> {
  if (!iterator.return) return;
  await Promise.race([
    Promise.resolve(iterator.return()).then(() => undefined),
    new Promise<void>((resolve) => setTimeout(resolve, 100)),
  ]).catch(() => undefined);
}

async function hashReadableStream(
  stream: ReadableStream<Uint8Array>,
  expectedLength: number,
  signal: AbortSignal,
): Promise<string> {
  const reader = stream.getReader();
  const hash = sha256.create();
  let total = 0;
  try {
    while (true) {
      if (signal.aborted) throw signal.reason;
      const { done, value } = await reader.read();
      if (done) break;
      total += value.length;
      if (total > expectedLength)
        throw new IntegrityError("upload exceeded authenticated length during preflight");
      hash.update(value);
    }
  } finally {
    if (signal.aborted) await reader.cancel(signal.reason).catch(() => undefined);
    reader.releaseLock();
  }
  if (total !== expectedLength)
    throw new IntegrityError("upload length changed during preflight verification");
  return bytesToHex(hash.digest());
}

function constantTimeEqual(left: string, right: string): boolean {
  const a = utf8ToBytes(left);
  const b = utf8ToBytes(right);
  let mismatch = a.length ^ b.length;
  for (let index = 0; index < Math.max(a.length, b.length); index += 1)
    mismatch |= (a[index % a.length] ?? 0) ^ (b[index % b.length] ?? 0);
  return mismatch === 0;
}
