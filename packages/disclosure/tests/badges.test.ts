import { spawnSync } from "node:child_process";
import { existsSync, readFileSync } from "node:fs";
import { join } from "node:path";
import { describe, expect, it } from "vitest";
import {
  BADGE_IDS,
  BADGE_LABELS,
  BADGE_VARIANTS,
  BUNDLED_POLICY,
  badgeDataUrl,
  badgeFileName,
  badgePalette,
  badgeSvg,
} from "../src/core.ts";

function luminance(hex: string): number {
  const [r = 0, g = 0, b = 0] = [1, 3, 5].map((i) => {
    const v = parseInt(hex.slice(i, i + 2), 16) / 255;
    return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4;
  });
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
}
const contrast = (a: string, b: string) => {
  const [hi, lo] = [luminance(a), luminance(b)].sort((x, y) => y - x) as [number, number];
  return (hi + 0.05) / (lo + 0.05);
};

describe("badge set", () => {
  it("covers the policy's four badge sets in three variants", () => {
    expect(BUNDLED_POLICY.badge_sets.map((b) => b.id)).toEqual([...BADGE_IDS]);
    for (const set of BUNDLED_POLICY.badge_sets) {
      expect(set.label).toBe(BADGE_LABELS[set.id]);
      expect(set.variants).toEqual([...BADGE_VARIANTS]);
    }
  });

  it("keeps text at WCAG AA and the glyph at 3:1 on every variant", () => {
    for (const variant of BADGE_VARIANTS) {
      const palette = badgePalette(variant);
      expect(contrast(palette.text, palette.background), variant).toBeGreaterThanOrEqual(4.5);
      expect(contrast(palette.glyph, palette.background), variant).toBeGreaterThanOrEqual(3);
    }
  });

  it("names itself and says it is not an official EU mark", () => {
    for (const id of BADGE_IDS) {
      const svg = new DOMParser().parseFromString(
        badgeSvg(id, "neutral"),
        "image/svg+xml",
      ).documentElement;
      expect(svg.getAttribute("role")).toBe("img");
      const title = svg.querySelector("title")!;
      expect(svg.getAttribute("aria-labelledby")).toBe(title.getAttribute("id"));
      expect(title.textContent).toBe(BADGE_LABELS[id]);
      expect(svg.querySelector("desc")!.textContent).toContain("not an official EU mark");
    }
  });

  it("escapes a custom label", () => {
    const svg = badgeSvg("ai-generated", "brand-dark", { label: `<b>&"KI"` });
    expect(svg).toContain("&lt;b&gt;&amp;&quot;KI&quot;");
    expect(svg).not.toContain("<b>");
    expect(badgeDataUrl("ai-generated", "neutral")).toMatch(
      /^data:image\/svg\+xml;charset=utf-8,%3Csvg/,
    );
  });

  it("ships the generated files unchanged (scripts/generate.mjs --check)", () => {
    const result = spawnSync(process.execPath, ["scripts/generate.mjs", "--check"], {
      encoding: "utf8",
    });
    expect(result.stderr).toBe("");
    expect(result.status).toBe(0);
    for (const id of BADGE_IDS) {
      for (const variant of BADGE_VARIANTS) {
        const file = join(process.cwd(), "assets/badges", badgeFileName(id, variant));
        expect(readFileSync(file, "utf8")).toBe(`${badgeSvg(id, variant)}\n`);
      }
    }
  });

  it("copies badges and the policy into dist", () => {
    expect(existsSync(join(process.cwd(), "dist/badges/ai-generated-brand-light.svg"))).toBe(true);
    expect(
      existsSync(join(process.cwd(), "dist/policy/op.disclosure-policy.2026-10.v1.json")),
    ).toBe(true);
  });
});
