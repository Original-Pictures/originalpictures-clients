// Copies the policy document from its one source (packages/domain) and writes
// the badge SVG files. `--check` fails instead of writing when anything drifted.
// Node runs the TypeScript badge module directly (type stripping).
//
// The public mirror (Original-Pictures/originalpictures-clients) ships this
// package without packages/domain. There the committed assets/policy copy is
// the source, and only the badges are regenerated and checked; in the monorepo
// tests/policy-source.test.ts fails if that copy drifts from packages/domain.
import { mkdirSync, readFileSync, readdirSync, writeFileSync, existsSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const check = process.argv.includes("--check");
const { BADGE_IDS, BADGE_VARIANTS, badgeFileName, badgeSvg } = await import("../src/badges.ts");

const POLICY = "op.disclosure-policy.2026-10.v1.json";
const source = join(root, "../domain/src/op_domain/resources/disclosure-policy", POLICY);
const wanted = new Map();
if (existsSync(source)) {
  wanted.set(join(root, "assets/policy", POLICY), readFileSync(source, "utf8"));
} else if (!existsSync(join(root, "assets/policy", POLICY))) {
  console.error(`neither ${source} nor the committed assets/policy/${POLICY} exists`);
  process.exit(1);
}
for (const id of BADGE_IDS) {
  for (const variant of BADGE_VARIANTS) {
    wanted.set(
      join(root, "assets/badges", badgeFileName(id, variant)),
      `${badgeSvg(id, variant)}\n`,
    );
  }
}

const drift = [];
for (const [path, content] of wanted) {
  const current = existsSync(path) ? readFileSync(path, "utf8") : null;
  if (current === content) continue;
  drift.push(path.slice(root.length + 1));
  if (!check) {
    mkdirSync(dirname(path), { recursive: true });
    writeFileSync(path, content);
  }
}
const badgeDir = join(root, "assets/badges");
for (const name of existsSync(badgeDir) ? readdirSync(badgeDir) : []) {
  if (![...wanted.keys()].includes(join(badgeDir, name)))
    drift.push(`assets/badges/${name} (unexpected)`);
}
if (check && drift.length) {
  console.error(
    `generated assets are stale; run pnpm --filter @originalpictures/disclosure generate:\n  ${drift.join("\n  ")}`,
  );
  process.exit(1);
}
if (!check) console.log(drift.length ? `wrote ${drift.join(", ")}` : "assets up to date");
