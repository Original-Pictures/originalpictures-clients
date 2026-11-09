import { existsSync, readFileSync } from "node:fs";
import { join } from "node:path";
import { describe, expect, it } from "vitest";

const dist = (name: string) => join(process.cwd(), "dist", name);

// `pnpm test` builds first (scripts/build.mjs), so these read fresh bundles.
describe("published bundles", () => {
  it("ships ESM entries and declarations without .ts specifiers", () => {
    for (const name of ["index.js", "core.js", "types/index.d.ts", "types/core.d.ts"]) {
      expect(existsSync(dist(name)), name).toBe(true);
    }
    expect(readFileSync(dist("types/core.d.ts"), "utf8")).not.toMatch(/from "\.\/[^"]+\.ts"/);
  });

  it("the script-tag bundle defines both elements and exposes resolve()", () => {
    const code = readFileSync(dist("disclosure.iife.js"), "utf8");
    const exported = new Function(`${code};return OriginalPicturesDisclosure;`)() as Record<
      string,
      unknown
    >;
    expect(typeof exported.resolve).toBe("function");
    expect(typeof exported.badge).toBe("function");
    expect(customElements.get("op-ai-notice")).toBeDefined();
    expect(customElements.get("op-ai-label")).toBeDefined();
  });
});
