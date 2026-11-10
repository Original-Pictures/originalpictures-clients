// The committed policy copy is what the published package ships, and what the
// public mirror builds from (it has no packages/domain). In the monorepo it
// must equal its one source byte for byte; `pnpm --filter
// @originalpictures/disclosure generate` refreshes it.
import { existsSync, readFileSync } from "node:fs";
import { join } from "node:path";
import { describe, expect, it } from "vitest";

const POLICY = "op.disclosure-policy.2026-10.v1.json";
const SOURCE = join(process.cwd(), "../domain/src/op_domain/resources/disclosure-policy", POLICY);
const COPY = join(process.cwd(), "assets/policy", POLICY);
const IN_MONOREPO = existsSync(join(process.cwd(), "../domain/pyproject.toml"));

describe("committed disclosure policy copy", () => {
  it("exists, since the published package and the mirror build ship it", () => {
    expect(existsSync(COPY)).toBe(true);
  });

  it.skipIf(!IN_MONOREPO)("matches packages/domain byte for byte", () => {
    expect(existsSync(SOURCE), `${SOURCE} is missing inside the monorepo`).toBe(true);
    expect(readFileSync(COPY, "utf8")).toBe(readFileSync(SOURCE, "utf8"));
  });
});
