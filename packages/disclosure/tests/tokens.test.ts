import { readFileSync } from "node:fs";
import { join } from "node:path";
import { describe, expect, it } from "vitest";
import { BRAND, BRASS_DEEP, DARK, LIGHT, TOKEN_SOURCES } from "../src/tokens.ts";

const tokens = JSON.parse(
  readFileSync(join(process.cwd(), "../design-tokens/dist/tokens.json"), "utf8"),
) as {
  shared: Record<string, { value: string }>;
  themes: Record<"light" | "dark", Record<string, { value: string }>>;
};

describe("brand tokens", () => {
  it("match @op/design-tokens", () => {
    for (const [key, source] of Object.entries(TOKEN_SOURCES)) {
      expect(LIGHT[key as keyof typeof LIGHT], source).toBe(tokens.themes.light[source]?.value);
      expect(DARK[key as keyof typeof DARK], source).toBe(tokens.themes.dark[source]?.value);
    }
    for (const [key, value] of Object.entries(BRAND))
      expect(tokens.shared[`brand.${key}`]?.value).toBe(value);
    // brassDeep is a private primitive; the light theme exposes it as brand.accentText.
    expect(tokens.themes.light["brand.accentText"]?.value).toBe(BRASS_DEEP);
  });
});
