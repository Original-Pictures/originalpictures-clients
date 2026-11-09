import { readFileSync } from "node:fs";
import { join } from "node:path";
import { describe, expect, it } from "vitest";
import { DARK, LIGHT, TOKEN_SOURCES, contrast } from "../src/tokens.ts";

const tokens = JSON.parse(
  readFileSync(join(process.cwd(), "..", "design-tokens", "dist", "tokens.json"), "utf8"),
) as { themes: Record<"light" | "dark", Record<string, { value: string }>> };

describe("brand tokens", () => {
  it.each([
    ["light", LIGHT],
    ["dark", DARK],
  ] as const)("match @op/design-tokens %s values", (theme, values) => {
    for (const [key, source] of Object.entries(TOKEN_SOURCES)) {
      expect(values[key as keyof typeof values], `${theme} ${source}`).toBe(
        tokens.themes[theme][source]?.value,
      );
    }
  });

  it("keeps body text and status text readable (WCAG AA)", () => {
    for (const theme of [LIGHT, DARK]) {
      expect(contrast(theme.text, theme.surface)).toBeGreaterThanOrEqual(4.5);
      expect(contrast(theme.successForeground, theme.successBackground)).toBeGreaterThanOrEqual(
        4.5,
      );
      expect(contrast(theme.dangerForeground, theme.dangerBackground)).toBeGreaterThanOrEqual(4.5);
      expect(contrast(theme.actionForeground, theme.actionBackground)).toBeGreaterThanOrEqual(4.5);
    }
  });
});
