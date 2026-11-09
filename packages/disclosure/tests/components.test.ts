import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import "../src/index.ts";
import { resetUnauthorizedWarning } from "../src/component-support.ts";
import type { OpAiLabelElement, OpAiNoticeElement } from "../src/core.ts";

const KEY = "opk_AbCdEfGhIjKl.secret-part_123";
const RECEIPT = {
  event_id: "dse_abcdefghijklmnop",
  sequence: 1,
  prev_hash: `sha256:${"0".repeat(64)}`,
  hash: `sha256:${"3f".repeat(32)}`,
  received_at: "2026-10-19T09:30:00.412345Z",
};

let bodies: Record<string, unknown>[];

beforeEach(() => {
  document.body.replaceChildren();
  sessionStorage.clear();
  localStorage.clear();
  bodies = [];
  vi.stubGlobal(
    "fetch",
    vi.fn(async (_url: string, init: RequestInit) => {
      bodies.push(JSON.parse(String(init.body)));
      return new Response(JSON.stringify(RECEIPT), {
        status: 201,
        headers: { "content-type": "application/json" },
      });
    }),
  );
});

afterEach(() => vi.unstubAllGlobals());

async function settle(): Promise<void> {
  for (let i = 0; i < 5; i += 1) await new Promise((resolve) => setTimeout(resolve, 0));
}

function mount<T extends HTMLElement>(tag: string, attributes: Record<string, string>): T {
  const element = document.createElement(tag) as T;
  for (const [name, value] of Object.entries(attributes)) element.setAttribute(name, value);
  document.body.append(element);
  return element;
}

describe("<op-ai-notice>", () => {
  it("shows the jurisdiction's text at first interaction and logs it", async () => {
    const seen = vi.fn();
    document.body.addEventListener("op-disclosure-event", (e) => seen((e as CustomEvent).detail));
    const notice = mount<OpAiNoticeElement>("op-ai-notice", {
      jurisdiction: "EU",
      locale: "de",
      "publishable-key": KEY,
      "subject-ref": "visitor:abc123",
    });
    await settle();
    const root = notice.shadowRoot!;
    const box = root.querySelector(".notice")!;
    expect(box.hasAttribute("hidden")).toBe(false);
    expect(box.getAttribute("role")).toBe("note");
    expect(box.getAttribute("aria-label")).toBe("AI disclosure");
    const text = root.querySelector(".text")!;
    expect(text.textContent).toBe("Sie chatten mit einem KI-System.");
    expect(text.getAttribute("lang")).toBe("de");
    const ack = root.querySelector<HTMLButtonElement>("button.ack")!;
    expect(ack.getAttribute("type")).toBe("button");
    expect(root.getElementById(ack.getAttribute("aria-describedby")!)).toBe(text);
    expect(bodies).toEqual([
      expect.objectContaining({
        kind: "ai_interaction_notice",
        jurisdiction: "EU",
        rule_id: "eu.art50.1.ai-interaction",
        subject_ref: "visitor:abc123",
        locale: "de",
        surface: "web",
      }),
    ]);
    expect(seen).toHaveBeenCalledWith(expect.objectContaining({ kind: "ai_interaction_notice" }));
  });

  it("logs the acknowledgement, collapses to a focused chip and remembers it", async () => {
    const notice = mount<OpAiNoticeElement>("op-ai-notice", {
      jurisdiction: "US-ME",
      "publishable-key": KEY,
    });
    await settle();
    notice.shadowRoot!.querySelector<HTMLButtonElement>("button.ack")!.click();
    await settle();
    const chip = notice.shadowRoot!.querySelector<HTMLButtonElement>("button.chip")!;
    expect(chip.hasAttribute("hidden")).toBe(false);
    expect(chip.getAttribute("aria-label")).toBe(
      "You are not chatting with a human. This is an AI chatbot.",
    );
    expect(notice.shadowRoot!.activeElement).toBe(chip);
    expect(bodies.map((b) => b.kind)).toEqual(["ai_interaction_notice", "user_acknowledged"]);

    const again = mount<OpAiNoticeElement>("op-ai-notice", {
      jurisdiction: "US-ME",
      "publishable-key": KEY,
    });
    await settle();
    expect(again.shadowRoot!.querySelector(".notice")!.hasAttribute("hidden")).toBe(true);
    expect(bodies).toHaveLength(2);
  });

  it("repeats after the configured interval", async () => {
    sessionStorage.setItem(
      "op-ai-notice:us-ny.gbl47.companion-notice:2026-10-19.2",
      String(Date.now() - 181 * 60_000),
    );
    const notice = mount<OpAiNoticeElement>("op-ai-notice", {
      jurisdiction: "US-NY",
      "repeat-after": "180",
    });
    await settle();
    expect(notice.shadowRoot!.querySelector(".notice")!.hasAttribute("hidden")).toBe(false);
  });

  it("waits for show() where the rule is disclosure on request", async () => {
    const notice = mount<OpAiNoticeElement>("op-ai-notice", {
      jurisdiction: "US-UT",
      "publishable-key": KEY,
    });
    await settle();
    expect(notice.resolved?.timing).toBe("on_request");
    expect(notice.shadowRoot!.querySelector(".notice")!.hasAttribute("hidden")).toBe(true);
    expect(bodies).toHaveLength(0);
    notice.show();
    await settle();
    expect(notice.shadowRoot!.querySelector(".text")!.textContent).toBe(
      "You are interacting with generative AI, not a human.",
    );
    expect(bodies.map((b) => b.rule_id)).toEqual(["us-ut.sb149.disclose-on-request"]);
  });

  it("falls back to the EU rule where the jurisdiction has none, and logs it as EU", async () => {
    mount("op-ai-notice", { jurisdiction: "IN", "publishable-key": KEY });
    await settle();
    expect(bodies[0]).toMatchObject({ jurisdiction: "EU", rule_id: "eu.art50.1.ai-interaction" });
  });

  it("sends nothing without a publishable key but still emits the event", async () => {
    const seen = vi.fn();
    document.body.addEventListener("op-disclosure-event", seen);
    mount("op-ai-notice", { jurisdiction: "KR" });
    await settle();
    expect(fetch).not.toHaveBeenCalled();
    expect(seen).toHaveBeenCalledOnce();
  });

  it("reports a refused event without throwing", async () => {
    const errors = vi.fn();
    document.body.addEventListener("op-disclosure-error", (e) => errors((e as CustomEvent).detail));
    mount("op-ai-notice", {
      jurisdiction: "EU",
      "subject-ref": "someone@example.com",
      "publishable-key": KEY,
    });
    await settle();
    expect(errors).toHaveBeenCalledWith(expect.objectContaining({ code: "DISCLOSURE_INVALID" }));
    expect(fetch).not.toHaveBeenCalled();
  });
});

describe("a refused publishable key", () => {
  beforeEach(() => {
    resetUnauthorizedWarning();
    vi.stubGlobal(
      "fetch",
      vi.fn(
        async () =>
          new Response(JSON.stringify({ code: "UNAUTHENTICATED", message: "unauthenticated" }), {
            status: 401,
            headers: { "content-type": "application/json" },
          }),
      ),
    );
  });

  it("dispatches op-disclosure-error with the status and warns once per page", async () => {
    const warn = vi.spyOn(console, "warn").mockImplementation(() => undefined);
    const errors = vi.fn();
    document.body.addEventListener("op-disclosure-error", (e) => errors((e as CustomEvent).detail));
    mount("op-ai-notice", { jurisdiction: "EU", "publishable-key": KEY });
    mount("op-ai-label", { jurisdiction: "EU", kind: "visible_label", "publishable-key": KEY });
    await settle();
    expect(errors).toHaveBeenCalledTimes(2);
    expect(errors).toHaveBeenCalledWith(
      expect.objectContaining({ kind: "ai_interaction_notice", status: 401 }),
    );
    expect(warn).toHaveBeenCalledOnce();
    expect(String(warn.mock.calls[0]![0])).toContain("revoked, rotated or expired");
    warn.mockRestore();
  });
});

describe("<op-ai-label>", () => {
  it("renders an accessible applied label and logs visible_label_applied", async () => {
    const label = mount<OpAiLabelElement>("op-ai-label", {
      jurisdiction: "EU",
      kind: "deepfake_label",
      "content-ref": "ast_abcdefghijklmnop",
      "publishable-key": KEY,
      "show-text": "",
    });
    await settle();
    const root = label.shadowRoot!;
    const badge = root.querySelector("[role=img]")!;
    expect(badge.getAttribute("aria-label")).toBe(
      "AI-manipulated: This content has been artificially generated or manipulated.",
    );
    expect(root.querySelectorAll("svg")).toHaveLength(2);
    expect(root.querySelector(".text")!.getAttribute("aria-hidden")).toBe("true");
    expect(bodies).toEqual([
      expect.objectContaining({
        kind: "visible_label_applied",
        rule_id: "eu.art50.4.deep-fake",
        content_ref: "ast_abcdefghijklmnop",
      }),
    ]);
  });

  it("honours an explicit badge and a fixed variant", async () => {
    const label = mount<OpAiLabelElement>("op-ai-label", {
      badge: "ai-assisted",
      variant: "neutral",
      jurisdiction: "EU",
    });
    await settle();
    const svgs = label.shadowRoot!.querySelectorAll("svg");
    expect(svgs).toHaveLength(1);
    expect(svgs[0]!.querySelector("title")!.textContent).toBe("AI-assisted");
  });

  it("offers the label as a switch, logging the offer and then the application", async () => {
    const label = mount<OpAiLabelElement>("op-ai-label", {
      mode: "offer",
      // California's offer duty was deleted by SB 1000 (policy 2026-10-19.2); Korea still
      // requires a visible label on generated output.
      jurisdiction: "KR",
      "publishable-key": KEY,
    });
    await settle();
    const toggle = label.shadowRoot!.querySelector<HTMLButtonElement>("[role=switch]")!;
    expect(toggle.getAttribute("aria-checked")).toBe("false");
    expect(toggle.textContent).toBe("Add the “AI-generated” label");
    expect(label.applied).toBe(false);
    const changes = vi.fn();
    label.addEventListener("op-ai-label-change", (e) => changes((e as CustomEvent).detail));
    toggle.click();
    await settle();
    expect(toggle.getAttribute("aria-checked")).toBe("true");
    expect(label.applied).toBe(true);
    expect(changes).toHaveBeenCalledWith({ applied: true, badge: "ai-generated" });
    expect(bodies.map((b) => [b.kind, b.rule_id])).toEqual([
      ["visible_label_offered", "kr.art31.2.output-label"],
      ["visible_label_applied", "kr.art31.2.output-label"],
    ]);
  });
});
