import { describe, expect, it, vi } from "vitest";
import { DisclosureClient, badge, badgePlacement, resolve } from "../src/core.ts";

describe("badgePlacement", () => {
  it("scales to the shorter side and keeps the badge inside the image", () => {
    expect(badgePlacement(1000, 500, { width: 130, height: 28 })).toEqual({
      x: 851,
      y: 460,
      width: 139,
      height: 30,
    });
    expect(
      badgePlacement(1000, 500, { width: 130, height: 28 }, { position: "top-left" }),
    ).toMatchObject({ x: 10, y: 10 });
    const tiny = badgePlacement(40, 30, { width: 130, height: 28 });
    expect(tiny.width).toBeLessThanOrEqual(40);
    expect(tiny.height).toBeLessThanOrEqual(30);
    expect(tiny.x).toBeGreaterThanOrEqual(0);
  });
});

describe("badge(<img>)", () => {
  it("overlays without touching the image and removes cleanly", async () => {
    const host = document.createElement("div");
    const image = document.createElement("img");
    image.src = "https://example.test/photo.jpg";
    host.append(image);
    const handle = await badge(image, { badge: "ai-manipulated", position: "top-right" });
    const wrapper = image.parentElement!;
    expect(wrapper.hasAttribute("data-op-ai-badge")).toBe(true);
    expect(handle.element.alt).toBe("AI-manipulated");
    expect(handle.element.src).toMatch(/^data:image\/svg\+xml/);
    expect(handle.element.style.top).toBe("2%");
    expect(handle.element.style.right).toBe("2%");
    expect(image.src).toBe("https://example.test/photo.jpg");
    await expect(handle.receipt).resolves.toBeNull();
    handle.remove();
    expect(image.parentElement).toBe(host);
    expect(host.querySelector("[data-op-ai-badge]")).toBeNull();
  });

  it("logs visible_label_applied when given a client", async () => {
    const receipt = {
      event_id: "dse_abcdefghijklmnop",
      sequence: 2,
      prev_hash: "",
      hash: "",
      received_at: "",
    };
    const fetch = vi.fn(async () => new Response(JSON.stringify(receipt), { status: 201 }));
    const client = new DisclosureClient({
      publishableKey: "opk_AbCd.Ef",
      fetch: fetch as typeof globalThis.fetch,
    });
    const resolved = resolve({ jurisdiction: "CN", kind: "visible_label" })!;
    const handle = await badge(document.createElement("img"), {
      disclosure: { client, resolved, subjectRef: "editor:42", contentRef: "ast_abcdefghijklmnop" },
    });
    await expect(handle.receipt).resolves.toEqual(receipt);
    const body = JSON.parse(
      String((fetch.mock.calls[0] as unknown as [string, RequestInit])[1].body),
    );
    expect(body).toMatchObject({
      kind: "visible_label_applied",
      jurisdiction: "CN",
      rule_id: "cn.labeling.explicit-label",
    });
  });

  it("refuses anything but an image element or a Blob", async () => {
    await expect(
      badge(document.createElement("div") as unknown as HTMLImageElement),
    ).rejects.toThrow(TypeError);
  });
});
