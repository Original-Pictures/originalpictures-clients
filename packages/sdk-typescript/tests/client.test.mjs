import assert from "node:assert/strict";
import { createHash, createHmac } from "node:crypto";
import { readFileSync } from "node:fs";
import { spawn } from "node:child_process";
import { once } from "node:events";
import { createInterface } from "node:readline";
import test from "node:test";
import { fileURLToPath } from "node:url";

import {
  CancelledError,
  ConfigurationError,
  DeadlineExceededError,
  IntegrityError,
  OriginalPicturesClient,
  PUBLIC_API_OPERATIONS,
  PermissionDeniedError,
  ResponseTooLargeError,
  SDK_EXECUTABLE_OPERATION_COUNT,
  SDK_TYPED_OPERATION_COUNT,
  TransportError,
  ValidationError,
  poll,
  signJobTerminal,
  verificationJobTerminal,
  verifyWebhook,
} from "../dist/index.js";

test("Sign and Verify readiness helpers enforce identifier meaning", () => {
  assert.equal(
    signJobTerminal({ job_id: "job_aaaaaaaaaaaaaaaa", state: "running", result: null }),
    false,
  );
  assert.equal(
    signJobTerminal({
      job_id: "job_aaaaaaaaaaaaaaaa",
      state: "completed",
      result: { verification_id: "vfy_aaaaaaaaaaaaaaaa" },
    }),
    true,
  );
  assert.throws(
    () =>
      signJobTerminal({
        job_id: "job_aaaaaaaaaaaaaaaa",
        state: "completed",
        result: { verification_id: "vjob_aaaaaaaaaaaaaaaa" },
      }),
    /ready vfy_/,
  );
  assert.equal(
    verificationJobTerminal({
      verification_id: "vjob_aaaaaaaaaaaaaaaa",
      state: "running",
      evidence_id: null,
    }),
    false,
  );
  assert.equal(
    verificationJobTerminal({
      verification_id: "vjob_aaaaaaaaaaaaaaaa",
      state: "completed",
      evidence_id: "vfy_aaaaaaaaaaaaaaaa",
    }),
    true,
  );
  assert.throws(
    () =>
      verificationJobTerminal({
        verification_id: "vfy_aaaaaaaaaaaaaaaa",
        state: "completed",
        evidence_id: "vfy_aaaaaaaaaaaaaaaa",
      }),
    /vjob_/,
  );
});

test("client rejects embedded credentials and reports caller cancellation", async () => {
  assert.throws(
    () => new OriginalPicturesClient({ baseUrl: "https://secret@example.test" }),
    ConfigurationError,
  );
  const client = new OriginalPicturesClient({
    baseUrl: "https://api.originalpictures.example",
    apiKey: "sdk-secret",
    fetch: async (_url, init) => {
      await new Promise((_resolve, reject) => {
        init.signal.addEventListener("abort", () => reject(init.signal.reason), { once: true });
      });
    },
  });
  const controller = new AbortController();
  controller.abort();
  let fetchCalls = 0;
  const preAbortedClient = new OriginalPicturesClient({
    baseUrl: "https://api.originalpictures.example",
    apiKey: "sdk-secret",
    fetch: async () => {
      fetchCalls += 1;
      return new Response("{}");
    },
  });
  await assert.rejects(
    preAbortedClient.operations.getCurrentUser({ signal: controller.signal }),
    CancelledError,
  );
  assert.equal(fetchCalls, 0);

  const activeController = new AbortController();
  const pending = client.operations.getCurrentUser({ signal: activeController.signal });
  activeController.abort();
  await assert.rejects(pending, CancelledError);
});

test("client rejects base URL query and fragment before auth and preserves path prefixes", async () => {
  let fetches = 0;
  for (const baseUrl of [
    "https://api.originalpictures.example?tenant=secret",
    "https://api.originalpictures.example#fragment",
    "https://api.originalpictures.example?",
    "https://api.originalpictures.example#",
  ]) {
    assert.throws(
      () =>
        new OriginalPicturesClient({
          baseUrl,
          apiKey: "must-not-send",
          fetch: async () => {
            fetches += 1;
            return new Response("{}");
          },
        }),
      ConfigurationError,
    );
  }
  assert.equal(fetches, 0);

  const seen = [];
  const client = new OriginalPicturesClient({
    baseUrl: "https://api.originalpictures.example/prefix/",
    fetch: async (url) => {
      seen.push(String(url));
      return new Response("{}", { headers: { "content-type": "application/json" } });
    },
  });
  await client.operations.getHealthz();
  assert.deepEqual(seen, ["https://api.originalpictures.example/prefix/healthz"]);
});

test("generated contract exposes all 128 operations including retention and billing", () => {
  const fixture = JSON.parse(
    readFileSync(new URL("../../../tests/fixtures/developer-surfaces/v1.json", import.meta.url)),
  );
  const ids = new Set(PUBLIC_API_OPERATIONS.map((operation) => operation.operationId));
  assert.equal(PUBLIC_API_OPERATIONS.length, fixture.operation_count);
  assert.equal(SDK_TYPED_OPERATION_COUNT, 128);
  assert.equal(SDK_EXECUTABLE_OPERATION_COUNT, 126);
  assert.equal(ids.size, fixture.operation_count);
  assert.ok(ids.has("getApiKey"));
  assert.ok(ids.has("completeApiKeyRotation"));
  assert.ok(ids.has("cancelApiKeyRotation"));
  assert.ok(ids.has("getWebhookDelivery"));
  assert.ok(ids.has("completeWebhookEndpointSecretOverlap"));
  assert.ok(fixture.required_workflow_operations.every((operation) => ids.has(operation)));
  for (const [operationId, method, path] of [
    ["getApiKeyRetention", "GET", "/v1/api-keys/{api_key_id}/retention"],
    ["setApiKeyRetention", "PUT", "/v1/api-keys/{api_key_id}/retention"],
    ["listBillingCharges", "GET", "/v1/billing/charges"],
    ["getBillingPricing", "GET", "/v1/billing/pricing"],
    ["createBillingQuote", "POST", "/v1/billing/quotes"],
  ]) {
    const operation = PUBLIC_API_OPERATIONS.find((item) => item.operationId === operationId);
    assert.ok(operation, operationId);
    assert.equal(operation.method, method);
    assert.equal(operation.path, path);
    assert.equal(operation.executable, true);
  }
  assert.equal(
    PUBLIC_API_OPERATIONS.find((item) => item.operationId === "receiveClerkWebhook").executable,
    false,
  );
  assert.equal(
    PUBLIC_API_OPERATIONS.find((item) => item.operationId === "receiveStripeWebhook").executable,
    false,
  );
  assert.ok(PUBLIC_API_OPERATIONS.every((operation) => operation.responses.length >= 1));
  assert.deepEqual(
    new Set(
      PUBLIC_API_OPERATIONS.filter((operation) => operation.path.startsWith("/v1/capture-")).map(
        (operation) => operation.operationId,
      ),
    ),
    new Set([
      "createCaptureIdentityEnrollment",
      "createCaptureIdentity",
      "listCaptureIdentities",
      "getCaptureIdentity",
      "createCaptureAdmissionChallenge",
      "createCaptureAdmission",
      "listCaptureAdmissions",
      "getCaptureAdmission",
      "revokeCaptureIdentity",
    ]),
  );
});

test("README states the generated contract's operation counts", () => {
  const prose = readFileSync(new URL("../README.md", import.meta.url), "utf8");
  const statedTotal = prose.match(/all\s+(\d+)\s+operations/);
  const statedConsumer = prose.match(/the\s+(\d+)\s+consumer\s+operations/);
  assert.ok(statedTotal, "README no longer states the total operation count");
  assert.ok(statedConsumer, "README no longer states the consumer operation count");
  assert.equal(Number(statedTotal[1]), SDK_TYPED_OPERATION_COUNT);
  assert.equal(Number(statedConsumer[1]), SDK_EXECUTABLE_OPERATION_COUNT);
});

test("anonymous operations omit bearer and signed provider ingress is non-callable", async () => {
  const calls = [];
  const client = new OriginalPicturesClient({
    baseUrl: "https://api.originalpictures.example",
    apiKey: "private-key",
    fetch: async (url, init) => {
      calls.push({
        url: String(url),
        authorization: new Headers(init.headers).get("authorization"),
      });
      return new Response("{}", { headers: { "content-type": "application/json" } });
    },
  });
  await client.operations.getSharedVerification({ parameters: { token: "share-token" } });
  assert.deepEqual(calls, [
    {
      url: "https://api.originalpictures.example/v1/shared-verifications/share-token",
      authorization: null,
    },
  ]);
  await assert.rejects(
    client.request("receiveClerkWebhook", { body: {}, headers: {}, parameters: {} }),
    ConfigurationError,
  );
  assert.equal(calls.length, 1);
});

test("typed operation methods use generated paths and never leak secret errors", async () => {
  const seen = {};
  const client = new OriginalPicturesClient({
    baseUrl: "https://api.originalpictures.example",
    apiKey: "sdk-secret",
    fetch: async (url, init) => {
      seen.url = String(url);
      seen.authorization = new Headers(init.headers).get("authorization");
      return new Response(
        JSON.stringify({
          code: "SCOPE_REQUIRED",
          detail: "sdk-secret",
          retryable: false,
          field_details: { scope: "assets:read" },
          documentation_url: "https://docs.example/errors/SCOPE_REQUIRED",
          job_reference: "job_fixture",
        }),
        {
          status: 403,
          headers: { "content-type": "application/json", "x-request-id": "req_1" },
        },
      );
    },
  });
  await assert.rejects(client.operations.getJob({ parameters: { job_id: "job_1" } }), (error) => {
    assert.ok(error instanceof PermissionDeniedError);
    assert.equal(error.code, "SCOPE_REQUIRED");
    assert.equal(error.requestId, "req_1");
    assert.equal(error.retryable, false);
    assert.deepEqual(error.fieldDetails, { scope: "assets:read" });
    assert.equal(error.documentationUrl, "https://docs.example/errors/SCOPE_REQUIRED");
    assert.equal(error.jobReference, "job_fixture");
    assert.equal(String(error).includes("sdk-secret"), false);
    return true;
  });
  assert.deepEqual(seen, {
    url: "https://api.originalpictures.example/v1/jobs/job_1",
    authorization: "Bearer sdk-secret",
  });
});

test("exact upload hashes streaming bytes and strips API authorization", async () => {
  const payload = new TextEncoder().encode("Original Pictures exact bytes");
  const digest = createHash("sha256").update(payload).digest("hex");
  const client = new OriginalPicturesClient({
    baseUrl: "https://api.originalpictures.example",
    apiKey: "must-not-forward",
    fetch: async (_url, init) => {
      const headers = new Headers(init.headers);
      assert.equal(headers.has("authorization"), false);
      assert.equal(headers.get("content-length"), String(payload.length));
      assert.equal(init.duplex, "half");
      const chunks = [];
      for await (const chunk of init.body) chunks.push(chunk);
      assert.deepEqual(Buffer.concat(chunks), Buffer.from(payload));
      return new Response(null, { status: 200 });
    },
  });
  const result = await client.upload("https://storage.example/upload", payload, {
    byteLength: payload.length,
    sha256: digest,
  });
  assert.deepEqual(result, { byteLength: payload.length, sha256: digest });
});

test("browser Blob upload preflights integrity without Content-Length or Node duplex", async () => {
  const payload = new TextEncoder().encode("browser fixture");
  const digest = createHash("sha256").update(payload).digest("hex");
  const client = new OriginalPicturesClient({
    baseUrl: "https://api.originalpictures.example",
    fetch: async (_url, init) => {
      assert.ok(init.body instanceof Blob);
      assert.equal(new Headers(init.headers).has("content-length"), false);
      assert.equal(Object.hasOwn(init, "duplex"), false);
      return new Response(null, { status: 200 });
    },
  });
  assert.deepEqual(
    await client.uploadBlob("https://storage.example/upload", new Blob([payload]), {
      byteLength: payload.length,
      sha256: digest,
    }),
    { byteLength: payload.length, sha256: digest },
  );
  await assert.rejects(
    client.uploadBlob("https://storage.example/upload", new Blob([payload]), {
      byteLength: payload.length,
      sha256: "0".repeat(64),
    }),
    IntegrityError,
  );
});

test("corrupt download preserves integrity failure when abort cleanup fails", async () => {
  const payload = new TextEncoder().encode("corrupt fixture");
  for (const abortFailure of [
    () => {
      throw new Error("synchronous cleanup failure");
    },
    async () => {
      throw new Error("asynchronous cleanup failure");
    },
  ]) {
    const staged = [];
    let committed = 0;
    let aborted = 0;
    const client = new OriginalPicturesClient({
      baseUrl: "https://api.originalpictures.example",
      fetch: async () =>
        new Response(payload, {
          headers: { "content-length": String(payload.length) },
        }),
    });
    await assert.rejects(
      client.download("https://storage.example/download", {
        byteLength: payload.length,
        sha256: "0".repeat(64),
        sink: {
          write(chunk) {
            staged.push(chunk);
          },
          commit() {
            committed += 1;
          },
          abort() {
            aborted += 1;
            return abortFailure();
          },
        },
      }),
      IntegrityError,
    );
    assert.ok(staged.length > 0);
    assert.equal(committed, 0);
    assert.equal(aborted, 1);
  }
});

test("download preserves commit and cancellation errors across abort cleanup failures", async () => {
  const payload = new TextEncoder().encode("primary failure fixture");
  const digest = createHash("sha256").update(payload).digest("hex");
  const commitFailure = new IntegrityError("commit failed");
  const commitClient = new OriginalPicturesClient({
    baseUrl: "https://api.originalpictures.example",
    fetch: async () => new Response(payload),
  });
  await assert.rejects(
    commitClient.download("https://storage.example/download", {
      byteLength: payload.length,
      sha256: digest,
      sink: {
        write() {},
        commit() {
          throw commitFailure;
        },
        abort() {
          return Promise.reject(new Error("abort cleanup rejected"));
        },
      },
    }),
    (error) => error === commitFailure,
  );

  const controller = new AbortController();
  let committed = 0;
  let aborted = 0;
  const cancelClient = new OriginalPicturesClient({
    baseUrl: "https://api.originalpictures.example",
    fetch: async (_url, init) =>
      new Promise((_resolve, reject) => {
        init.signal.addEventListener("abort", () => reject(init.signal.reason), { once: true });
        controller.abort();
      }),
  });
  await assert.rejects(
    cancelClient.download("https://storage.example/download", {
      byteLength: 0,
      sha256: createHash("sha256").digest("hex"),
      signal: controller.signal,
      sink: {
        write() {},
        commit() {
          committed += 1;
        },
        abort() {
          aborted += 1;
          throw new Error("abort cleanup threw");
        },
      },
    }),
    CancelledError,
  );
  assert.equal(committed, 0);
  assert.equal(aborted, 1);
});

test("transfer deadlines translate stably and close Node iterators", async () => {
  let cleaned = false;
  let reads = 0;
  const slowSource = {
    [Symbol.asyncIterator]() {
      return this;
    },
    async next() {
      reads += 1;
      if (reads === 1) return { done: false, value: new Uint8Array([1]) };
      return new Promise(() => {});
    },
    async return() {
      cleaned = true;
      return { done: true };
    },
  };
  const client = new OriginalPicturesClient({
    baseUrl: "https://api.originalpictures.example",
    fetch: async (_url, init) => {
      const reader = init.body.getReader();
      await reader.read();
      if (init.signal.aborted) throw init.signal.reason;
      await new Promise((_resolve, reject) =>
        init.signal.addEventListener("abort", () => reject(init.signal.reason), { once: true }),
      );
    },
  });
  await assert.rejects(
    client.uploadNodeStream("https://storage.example/upload", slowSource, {
      byteLength: 2,
      sha256: "0".repeat(64),
      timeoutMs: 20,
    }),
    DeadlineExceededError,
  );
  assert.equal(cleaned, true);
});

test("transfer pre-cancellation and transport failures use stable taxonomy", async () => {
  let fetchCalls = 0;
  const client = new OriginalPicturesClient({
    baseUrl: "https://api.originalpictures.example",
    fetch: async () => {
      fetchCalls += 1;
      throw new Error("unsafe transport details");
    },
  });
  const controller = new AbortController();
  controller.abort();
  await assert.rejects(
    client.download("https://storage.example/download", {
      byteLength: 0,
      sha256: createHash("sha256").digest("hex"),
      signal: controller.signal,
    }),
    CancelledError,
  );
  assert.equal(fetchCalls, 0);
  await assert.rejects(
    client.download("https://storage.example/download", {
      byteLength: 0,
      sha256: createHash("sha256").digest("hex"),
    }),
    TransportError,
  );
  assert.equal(fetchCalls, 1);
});

test("poll bounds in-flight fetches, propagates cancellation, and removes listeners", async () => {
  const neverBefore = performance.now();
  await assert.rejects(
    poll(
      () => new Promise(() => {}),
      () => false,
      { timeoutMs: 20, intervalMs: 0 },
    ),
    DeadlineExceededError,
  );
  assert.ok(performance.now() - neverBefore < 200);

  let timedOutFetchCancelled = false;
  const before = performance.now();
  await assert.rejects(
    poll(
      (signal) =>
        new Promise((_resolve, reject) =>
          signal.addEventListener(
            "abort",
            () => {
              timedOutFetchCancelled = true;
              reject(signal.reason);
            },
            { once: true },
          ),
        ),
      () => false,
      { timeoutMs: 20, intervalMs: 0 },
    ),
    DeadlineExceededError,
  );
  assert.ok(performance.now() - before < 200);
  assert.equal(timedOutFetchCancelled, true);

  const controller = new AbortController();
  const signal = controller.signal;
  const originalAdd = signal.addEventListener.bind(signal);
  const originalRemove = signal.removeEventListener.bind(signal);
  let activeAbortListeners = 0;
  signal.addEventListener = (type, listener, options) => {
    if (type === "abort") activeAbortListeners += 1;
    return originalAdd(type, listener, options);
  };
  signal.removeEventListener = (type, listener, options) => {
    if (type === "abort") activeAbortListeners -= 1;
    return originalRemove(type, listener, options);
  };
  await assert.rejects(
    poll(
      async () => false,
      (value) => value,
      {
        timeoutMs: 1_000,
        intervalMs: 0,
        maxAttempts: 20,
        signal,
      },
    ),
    DeadlineExceededError,
  );
  assert.equal(activeAbortListeners, 0);

  const cancelledController = new AbortController();
  let fetchObservedCancellation = false;
  const pending = poll(
    (fetchSignal) =>
      new Promise((_resolve, reject) =>
        fetchSignal.addEventListener(
          "abort",
          () => {
            fetchObservedCancellation = true;
            reject(fetchSignal.reason);
          },
          { once: true },
        ),
      ),
    () => false,
    { timeoutMs: 1_000, signal: cancelledController.signal },
  );
  cancelledController.abort();
  await assert.rejects(pending, CancelledError);
  assert.equal(fetchObservedCancellation, true);

  const sleepController = new AbortController();
  const sleepSignal = sleepController.signal;
  const sleepAdd = sleepSignal.addEventListener.bind(sleepSignal);
  const sleepRemove = sleepSignal.removeEventListener.bind(sleepSignal);
  let sleepListeners = 0;
  sleepSignal.addEventListener = (type, listener, options) => {
    if (type === "abort") sleepListeners += 1;
    return sleepAdd(type, listener, options);
  };
  sleepSignal.removeEventListener = (type, listener, options) => {
    if (type === "abort") sleepListeners -= 1;
    return sleepRemove(type, listener, options);
  };
  const sleeping = poll(
    async () => false,
    (value) => value,
    {
      timeoutMs: 1_000,
      intervalMs: 500,
      signal: sleepSignal,
    },
  );
  await new Promise((resolve) => setTimeout(resolve, 5));
  sleepController.abort();
  await assert.rejects(sleeping, CancelledError);
  assert.equal(sleepListeners, 0);
});

test("bounded response failures cancel and release without masking the primary error", async () => {
  for (const cancelFailure of [
    undefined,
    () => {
      throw new Error("cancel threw");
    },
    async () => {
      throw new Error("cancel rejected");
    },
  ]) {
    let cancelled = 0;
    let released = 0;
    let reads = 0;
    const body = {
      getReader() {
        return {
          async read() {
            reads += 1;
            return { done: false, value: new Uint8Array([1, 2]) };
          },
          cancel() {
            cancelled += 1;
            return cancelFailure?.();
          },
          releaseLock() {
            released += 1;
          },
        };
      },
    };
    const client = new OriginalPicturesClient({
      baseUrl: "https://api.originalpictures.example",
      maxResponseBytes: 1,
      fetch: async () => ({
        ok: true,
        status: 200,
        headers: new Headers({ "content-type": "application/json" }),
        body,
      }),
    });
    await assert.rejects(client.operations.getHealthz(), ResponseTooLargeError);
    assert.equal(reads, 1);
    assert.equal(cancelled, 1);
    assert.equal(released, 1);
  }

  let cancelled = 0;
  const client = new OriginalPicturesClient({
    baseUrl: "https://api.originalpictures.example",
    fetch: async () => ({
      ok: true,
      status: 200,
      headers: new Headers(),
      body: {
        getReader() {
          return {
            async read() {
              throw new Error("unsafe reader failure");
            },
            cancel() {
              cancelled += 1;
              throw new Error("unsafe cancel failure");
            },
            releaseLock() {},
          };
        },
      },
    }),
  });
  await assert.rejects(client.operations.getHealthz(), TransportError);
  assert.equal(cancelled, 1);
});

test("shared V1 fixture executes through the real TypeScript client", async () => {
  const rawFixture = JSON.parse(
    readFileSync(new URL("../../../tests/fixtures/developer-surfaces/v1.json", import.meta.url)),
  );
  await withFixtureServer(async (baseUrl) => {
    const fixture = JSON.parse(JSON.stringify(rawFixture).replaceAll("$BASE_URL", baseUrl));
    const client = new OriginalPicturesClient({
      baseUrl,
      apiKey: fixture.sdk.valid_api_key,
      timeoutMs: 1_000,
    });
    assert.deepEqual(
      await client.operations.getSharedVerification({
        parameters: { token: fixture.sdk.anonymous_share_token },
      }),
      fixture.sdk.anonymous_response,
    );
    assert.deepEqual(await client.operations.getCurrentUser(), fixture.cli.user_response);

    const denied = new OriginalPicturesClient({
      baseUrl,
      apiKey: fixture.cli.scope_denied_api_key,
    });
    await assert.rejects(denied.operations.listAssets(), (error) => {
      assert.ok(error instanceof PermissionDeniedError);
      assert.equal(error.code, fixture.cli.scope_error.code);
      assert.equal(error.requestId, fixture.cli.scope_error.request_id);
      assert.equal(error.retryable, false);
      assert.equal(String(error).includes(fixture.cli.scope_error.detail), false);
      return true;
    });

    const mcpClient = new OriginalPicturesClient({
      baseUrl,
      apiKey: fixture.mcp.valid_api_key,
    });
    assert.deepEqual(
      await mcpClient.operations.createVerification({
        body: { object_id: fixture.mcp.verification.object_id },
        headers: { "Idempotency-Key": fixture.mcp.verification.idempotency_key },
      }),
      fixture.mcp.verification.response,
    );
    const slowClient = new OriginalPicturesClient({
      baseUrl,
      apiKey: fixture.mcp.valid_api_key,
      timeoutMs: 25,
    });
    await assert.rejects(
      slowClient.operations.getAsset({ parameters: { asset_id: fixture.mcp.slow_asset.id } }),
      DeadlineExceededError,
    );

    const downloadPayload = Buffer.from(fixture.cli.download.bytes_base64, "base64");
    const staged = [];
    let committed = false;
    assert.deepEqual(
      await client.download(fixture.cli.download.grant_response.url, {
        byteLength: fixture.cli.download.byte_length,
        sha256: fixture.cli.download.sha256,
        headers: fixture.cli.download.grant_response.headers,
        sink: {
          write(chunk) {
            staged.push(chunk);
          },
          commit() {
            committed = true;
          },
          abort(error) {
            throw error;
          },
        },
      }),
      { byteLength: downloadPayload.length, sha256: fixture.cli.download.sha256 },
    );
    assert.equal(committed, true);
    assert.deepEqual(Buffer.concat(staged), downloadPayload);

    const uploadPayload = Buffer.from(fixture.cli.upload.bytes_base64, "base64");
    await client.uploadNodeStream(fixture.cli.upload.create_response.upload.url, uploadPayload, {
      byteLength: fixture.cli.upload.byte_length,
      sha256: fixture.cli.upload.sha256,
      headers: fixture.cli.upload.create_response.upload.headers,
    });
  });
});

test("webhook helper verifies the exact raw body", () => {
  const body = new TextEncoder().encode('{"event_id":"evt_1"}');
  const secret = new TextEncoder().encode("s".repeat(32));
  const timestamp = 1_700_000_000;
  const signature = `v1=${createHmac("sha256", secret)
    .update(`${timestamp}.evt_1.`)
    .update(body)
    .digest("hex")}`;
  verifyWebhook(body, { secret, eventId: "evt_1", timestamp, signature, now: timestamp });
});

test("webhook helper accepts either Standard Webhooks signer during overlap", () => {
  const body = new TextEncoder().encode('{"event_id":"evt_overlap","value":1}');
  const oldKey = Buffer.alloc(32, 0x31);
  const newKey = Buffer.alloc(32, 0x32);
  const oldSecret = `whsec_${oldKey.toString("base64")}`;
  const newSecret = `whsec_${newKey.toString("base64")}`;
  const timestamp = 1_700_000_000;
  const message = Buffer.concat([
    Buffer.from(`evt_overlap.${timestamp}.`, "ascii"),
    Buffer.from(body),
  ]);
  const signatures = [oldKey, newKey]
    .map((key) => `v1,${createHmac("sha256", key).update(message).digest("base64")}`)
    .join(" ");

  for (const secret of [oldSecret, newSecret]) {
    verifyWebhook(body, {
      secret,
      eventId: "evt_overlap",
      timestamp,
      signature: signatures,
      now: timestamp,
    });
  }
  assert.throws(
    () =>
      verifyWebhook(body, {
        secret: `whsec_${Buffer.alloc(32, 0x33).toString("base64")}`,
        eventId: "evt_overlap",
        timestamp,
        signature: signatures,
        now: timestamp,
      }),
    ValidationError,
  );
  assert.throws(
    () =>
      verifyWebhook(new TextEncoder().encode('{"event_id":"evt_overlap","value":2}'), {
        secret: newSecret,
        eventId: "evt_overlap",
        timestamp,
        signature: signatures,
        now: timestamp,
      }),
    ValidationError,
  );
  assert.throws(
    () =>
      verifyWebhook(body, {
        secret: newSecret,
        eventId: "evt_overlap",
        timestamp,
        signature: signatures,
        now: timestamp + 301,
      }),
    ValidationError,
  );
});

async function withFixtureServer(callback) {
  const repositoryRoot = fileURLToPath(new URL("../../..", import.meta.url));
  const child = spawn("uv", ["run", "--frozen", "python", "tests/fixtures/developer_surfaces.py"], {
    cwd: repositoryRoot,
    stdio: ["ignore", "pipe", "inherit"],
  });
  const lines = createInterface({ input: child.stdout });
  try {
    const [baseUrl] = await Promise.race([
      once(lines, "line"),
      new Promise((_, reject) =>
        setTimeout(() => reject(new Error("fixture server startup timed out")), 5_000),
      ),
    ]);
    await callback(baseUrl);
  } finally {
    lines.close();
    child.kill("SIGTERM");
    await once(child, "exit");
  }
}
