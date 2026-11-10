import { afterEach, describe, expect, it, vi } from "vitest";
import { VerifyError, fetchMedia, fetchVerifyPage, inspect, verify } from "../src/core.ts";
import { PAGE, completed, json, mockFetch } from "./fixtures.ts";

const BASE = "https://api.originalpictures.com/v1/public/verify-pages/studio-nova";
const file = () => new Blob([new Uint8Array([0xff, 0xd8, 0xff])], { type: "image/jpeg" });

afterEach(() => {
  vi.useRealTimers();
});

describe("fetchVerifyPage", () => {
  it("reads the public page configuration anonymously", async () => {
    const fetch = mockFetch(json(PAGE));
    await expect(fetchVerifyPage("studio-nova", { fetch })).resolves.toEqual(PAGE);
    expect(fetch.calls[0]?.url).toBe(BASE);
    expect(fetch.calls[0]?.init.credentials).toBe("omit");
  });

  it("maps a 404 to VERIFY_PAGE_NOT_FOUND", async () => {
    const fetch = mockFetch(json({ code: "VERIFY_PAGE_NOT_FOUND", message: "no page" }, 404));
    await expect(fetchVerifyPage("studio-nova", { fetch })).rejects.toMatchObject({
      code: "VERIFY_PAGE_NOT_FOUND",
      status: 404,
    });
  });

  it("refuses an answer of the wrong schema", async () => {
    const fetch = mockFetch(json({ schema_version: "something-else" }));
    await expect(fetchVerifyPage("studio-nova", { fetch })).rejects.toMatchObject({
      code: "UNEXPECTED_RESPONSE",
    });
  });
});

describe("verify", () => {
  it("posts the file as multipart without its name or credentials", async () => {
    const fetch = mockFetch(json(completed()));
    const named = new File([new Uint8Array([1, 2, 3])], "holiday-in-lisbon.jpg", {
      type: "image/jpeg",
    });
    const result = await verify(named, { page: "studio-nova", fetch });
    expect(result.state).toBe("completed");
    const call = fetch.calls[0]!;
    expect(call.url).toBe(`${BASE}/checks`);
    expect(call.init.method).toBe("POST");
    expect(call.init.credentials).toBe("omit");
    const body = call.init.body as FormData;
    const part = body.get("file") as File;
    expect(part).toBeInstanceOf(Blob);
    expect(part.name).toBe("upload");
    expect(part.type).toBe("image/jpeg");
    expect(part.size).toBe(3);
    expect([...body.keys()]).toEqual(["file"]);
  });

  it("polls a running check no faster than every two seconds", async () => {
    vi.useFakeTimers();
    const running = completed({
      state: "running",
      content_credentials: null,
      made_with: null,
      completed_at: null,
    });
    const fetch = mockFetch(json(running, 202), json(running), json(completed()));
    const progress = vi.fn();
    const pending = verify(file(), {
      page: "studio-nova",
      fetch,
      pollIntervalMs: 10,
      onProgress: progress,
    });
    await vi.advanceTimersByTimeAsync(1_999);
    expect(fetch.calls).toHaveLength(1);
    await vi.advanceTimersByTimeAsync(1);
    expect(fetch.calls).toHaveLength(2);
    await vi.advanceTimersByTimeAsync(2_000);
    await expect(pending).resolves.toMatchObject({ state: "completed" });
    expect(fetch.calls[1]?.url).toBe(`${BASE}/checks/pchk_abcdefghijklmnop`);
    expect(fetch.calls[1]?.init.method).toBe("GET");
    expect(progress).toHaveBeenCalledTimes(2);
  });

  it("surfaces the rate limit with its Retry-After", async () => {
    const fetch = mockFetch(
      json({ code: "PUBLIC_CHECK_RATE_LIMITED", message: "slow down", request_id: "req_1" }, 429, {
        "Retry-After": "42",
      }),
    );
    const error = await verify(file(), { page: "studio-nova", fetch }).catch((e: unknown) => e);
    expect(error).toBeInstanceOf(VerifyError);
    expect(error).toMatchObject({
      code: "PUBLIC_CHECK_RATE_LIMITED",
      status: 429,
      retryAfterSeconds: 42,
      requestId: "req_1",
    });
  });

  it("refuses a file over the limit before uploading it", async () => {
    const fetch = mockFetch();
    const big = new Blob([new Uint8Array(11)]);
    await expect(
      verify(big, { page: "studio-nova", fetch, maxUploadBytes: 10 }),
    ).rejects.toMatchObject({
      code: "MEDIA_COMPRESSED_SIZE_LIMIT",
    });
    expect(fetch.calls).toHaveLength(0);
  });

  it("refuses a malformed slug and an empty file before any request", async () => {
    const fetch = mockFetch();
    await expect(verify(file(), { page: "../admin", fetch })).rejects.toMatchObject({
      code: "VERIFY_PAGE_INVALID",
    });
    await expect(verify(new Blob([]), { page: "studio-nova", fetch })).rejects.toMatchObject({
      code: "VERIFY_PAGE_INVALID",
    });
    expect(fetch.calls).toHaveLength(0);
  });

  it("accepts https or loopback http API bases only", async () => {
    await expect(
      verify(file(), { page: "studio-nova", apiBase: "http://evil.example", fetch: mockFetch() }),
    ).rejects.toMatchObject({ code: "VERIFY_PAGE_INVALID" });
    const fetch = mockFetch(json(completed()));
    await verify(file(), { page: "studio-nova", apiBase: "http://127.0.0.1:3120/", fetch });
    expect(fetch.calls[0]?.url).toBe(
      "http://127.0.0.1:3120/v1/public/verify-pages/studio-nova/checks",
    );
  });

  it("reports an unreachable service as NETWORK_ERROR", async () => {
    const fetch = mockFetch(new TypeError("Failed to fetch"));
    await expect(verify(file(), { page: "studio-nova", fetch })).rejects.toMatchObject({
      code: "NETWORK_ERROR",
    });
  });

  it("refuses a check answer that is not op.public-check.v1", async () => {
    const fetch = mockFetch(json({ ...completed(), check_id: "chk_1" }));
    await expect(verify(file(), { page: "studio-nova", fetch })).rejects.toMatchObject({
      code: "UNEXPECTED_RESPONSE",
    });
  });
});

describe("fetchMedia", () => {
  it("refuses addresses that are not http(s), blob or data", async () => {
    for (const src of ["javascript:alert(1)", "ftp://example.com/a.jpg", "  "]) {
      await expect(
        fetchMedia(src, { fetch: mockFetch(), baseUrl: "https://site.example/" }),
      ).rejects.toMatchObject({ code: "SOURCE_INVALID" });
    }
  });

  it("maps a refused answer to SOURCE_HTTP_ERROR", async () => {
    const fetch = mockFetch(new Response("no", { status: 403 }));
    await expect(fetchMedia("https://cdn.example/a.jpg", { fetch })).rejects.toMatchObject({
      code: "SOURCE_HTTP_ERROR",
      status: 403,
    });
  });

  it("resolves a relative address and keeps the media type", async () => {
    const fetch = mockFetch(
      new Response(new Uint8Array([1, 2]), { headers: { "content-type": "video/mp4; codecs=x" } }),
    );
    const blob = await fetchMedia("clips/a.mp4", { fetch, baseUrl: "https://site.example/p/" });
    expect(fetch.calls[0]?.url).toBe("https://site.example/p/clips/a.mp4");
    expect(blob.type).toBe("video/mp4");
    expect(blob.size).toBe(2);
  });
});

describe("inspect", () => {
  it("loads the asset and checks it", async () => {
    const fetch = mockFetch(new Response(new Uint8Array([1, 2, 3])), json(completed()));
    const result = await inspect("https://cdn.example/a.jpg", { page: "studio-nova", fetch });
    expect(result.state).toBe("completed");
    expect(fetch.calls[1]?.url).toBe(`${BASE}/checks`);
  });
});
