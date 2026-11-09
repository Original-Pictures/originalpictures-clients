import { existsSync, readFileSync, statSync } from "node:fs";
import { join } from "node:path";
import { describe, expect, it } from "vitest";

// Vitest runs from the package root; happy-dom replaces URL, so plain paths.
const dist = (name: string) => join(process.cwd(), "dist", name);

// `pnpm test` builds first (scripts/build.mjs), so these read fresh bundles.
describe("published bundles", () => {
  it("ships ESM entries and declarations", () => {
    for (const name of ["index.js", "core.js", "types/index.d.ts", "types/core.d.ts"]) {
      expect(existsSync(dist(name)), name).toBe(true);
    }
    expect(readFileSync(dist("types/core.d.ts"), "utf8")).not.toMatch(/from "\.\/[^"]+\.ts"/);
  });

  it("the script-tag bundle defines <op-verify> and exposes the API", () => {
    const code = readFileSync(dist("verify.iife.js"), "utf8");
    expect(statSync(dist("verify.iife.js")).size).toBeLessThan(40_000);
    expect(code).not.toMatch(/\bimport\s*\(|\brequire\(/);
    // As a <script> would: the bundle declares one global and defines the element.
    const exported = new Function(`${code};return OriginalPicturesVerify;`)() as Record<
      string,
      unknown
    >;
    expect(typeof exported.verify).toBe("function");
    expect(typeof exported.fetchVerifyPage).toBe("function");
    expect(customElements.get("op-verify")).toBeDefined();
  });
});
