import { afterEach, describe, expect, it, vi } from "vitest";
import {
  DisclosureClient,
  buildEventPayload,
  eventFor,
  pseudonymousSubject,
  resolve,
  type DisclosureEventInput,
} from "../src/core.ts";

const KEY = "opk_AbCdEfGhIjKl.secret-part_123";
const RECEIPT = {
  event_id: "dse_abcdefghijklmnop",
  sequence: 7,
  prev_hash: `sha256:${"a1".repeat(32)}`,
  hash: `sha256:${"3f".repeat(32)}`,
  received_at: "2026-10-19T09:30:00.412345Z",
};
const INPUT: DisclosureEventInput = {
  kind: "ai_interaction_notice",
  jurisdiction: "EU",
  policyVersion: "2026-10-19.1",
  ruleId: "eu.art50.1.ai-interaction",
  subjectRef: "visitor:7f3c2a91",
  locale: "de-DE",
  surface: "web",
  clientTime: new Date("2026-10-19T09:30:00.120Z"),
};

function recorder(...answers: (Response | Error)[]) {
  const calls: { url: string; init: RequestInit }[] = [];
  const fetch = (async (url: RequestInfo | URL, init: RequestInit = {}) => {
    calls.push({ url: String(url), init });
    const next = answers.shift();
    if (!next) throw new Error("unexpected request");
    if (next instanceof Error) throw next;
    return next;
  }) as typeof globalThis.fetch;
  return { fetch, calls };
}
const json = (body: unknown, status: number) =>
  new Response(JSON.stringify(body), { status, headers: { "content-type": "application/json" } });

afterEach(() => vi.useRealTimers());

describe("buildEventPayload", () => {
  it("produces exactly the DisclosureEventRequest body", () => {
    expect(buildEventPayload(INPUT)).toEqual({
      kind: "ai_interaction_notice",
      jurisdiction: "EU",
      policy_version: "2026-10-19.1",
      rule_id: "eu.art50.1.ai-interaction",
      subject_ref: "visitor:7f3c2a91",
      content_ref: null,
      client_time: "2026-10-19T09:30:00.120Z",
      surface: "web",
      locale: "de-DE",
    });
  });

  it.each([
    ["an email as subject", { subjectRef: "person@example.com" }],
    ["a name with spaces as subject", { subjectRef: "Ada Lovelace" }],
    ["an unknown jurisdiction", { jurisdiction: "US-TX" }],
    ["a malformed policy version", { policyVersion: "v1" }],
    ["an unknown kind", { kind: "label_removed" }],
    ["a malformed rule id", { ruleId: "EU Art 50" }],
    ["a malformed content ref", { contentRef: "https://x.example/a?b=c" }],
  ])("refuses %s", (_name, patch) => {
    expect(() =>
      buildEventPayload({ ...INPUT, ...(patch as Partial<DisclosureEventInput>) }),
    ).toThrow(expect.objectContaining({ code: "DISCLOSURE_INVALID" }));
  });

  it("builds the event for a resolved rule", () => {
    const resolved = resolve({ jurisdiction: "KR", locale: "ko" })!;
    expect(
      eventFor(resolved, "user_acknowledged", {
        subjectRef: "s1",
        contentRef: "ast_abcdefghijklmnop",
      }),
    ).toMatchObject({
      kind: "user_acknowledged",
      jurisdiction: "KR",
      policyVersion: "2026-10-19.2",
      ruleId: "kr.art31.1.advance-notice",
      locale: "ko",
      contentRef: "ast_abcdefghijklmnop",
      surface: "web",
    });
  });
});

describe("DisclosureClient", () => {
  it("posts with the publishable key and an idempotency key", async () => {
    const { fetch, calls } = recorder(json(RECEIPT, 201));
    const client = new DisclosureClient({ publishableKey: KEY, fetch });
    await expect(client.log(INPUT)).resolves.toEqual(RECEIPT);
    const call = calls[0]!;
    expect(call.url).toBe("https://api.originalpictures.com/v1/disclosures/events");
    expect(call.init.method).toBe("POST");
    expect(call.init.credentials).toBe("omit");
    expect(call.init.keepalive).toBe(true);
    const headers = call.init.headers as Record<string, string>;
    expect(headers.Authorization).toBe(`Bearer ${KEY}`);
    expect(headers["Content-Type"]).toBe("application/json");
    expect(headers["Idempotency-Key"]).toMatch(/^dse-[0-9a-f-]{32,36}$/);
    expect(JSON.parse(String(call.init.body))).toEqual(buildEventPayload(INPUT));
  });

  it("retries a 503 once with the same idempotency key", async () => {
    vi.useFakeTimers();
    const { fetch, calls } = recorder(
      json({ code: "SERVICE_UNAVAILABLE" }, 503),
      json(RECEIPT, 201),
    );
    const client = new DisclosureClient({ publishableKey: KEY, fetch, retryDelayMs: 10 });
    const pending = client.log(INPUT);
    await vi.advanceTimersByTimeAsync(10);
    await expect(pending).resolves.toEqual(RECEIPT);
    const keys = calls.map((c) => (c.init.headers as Record<string, string>)["Idempotency-Key"]);
    expect(keys).toHaveLength(2);
    expect(keys[0]).toBe(keys[1]);
  });

  it("surfaces the API's reason code", async () => {
    const { fetch } = recorder(json({ code: "DISCLOSURE_INVALID", message: "bad" }, 422));
    const client = new DisclosureClient({ publishableKey: KEY, fetch });
    await expect(client.log(INPUT)).rejects.toMatchObject({
      code: "DISCLOSURE_INVALID",
      status: 422,
    });
  });

  it("refuses a key that is not an opk_ key, and a plain-http API", () => {
    expect(() => new DisclosureClient({ publishableKey: "sk_live_123" })).toThrow(/publishable/);
    expect(
      () => new DisclosureClient({ publishableKey: KEY, apiBase: "http://api.example" }),
    ).toThrow(/https/);
    expect(
      () => new DisclosureClient({ publishableKey: KEY, apiBase: "http://localhost:3121" }),
    ).not.toThrow();
  });
});

describe("pseudonymousSubject", () => {
  it("is a stable opaque reference per storage", () => {
    const store = new Map<string, string>();
    const storage = {
      getItem: (k: string) => store.get(k) ?? null,
      setItem: (k: string, v: string) => void store.set(k, v),
    } as unknown as Storage;
    const first = pseudonymousSubject(storage);
    expect(first).toMatch(/^visitor:[0-9a-f]{16}$/);
    expect(pseudonymousSubject(storage)).toBe(first);
  });
});
