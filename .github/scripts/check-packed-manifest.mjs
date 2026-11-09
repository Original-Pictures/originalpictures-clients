// Checks one packed npm tarball before it may be published: the packed
// package.json carries no workspace: ranges, is not private, names Apache-2.0,
// ships LICENSE and README.md, and every file its "exports" (after pnpm applied
// publishConfig) points at is in the tarball.
// Usage: node .github/scripts/check-packed-manifest.mjs <tarball.tgz>
import { execFileSync } from "node:child_process";

const tarball = process.argv[2];
if (!tarball) {
  console.error("usage: check-packed-manifest.mjs <tarball.tgz>");
  process.exit(2);
}

const raw = execFileSync("tar", ["-xOzf", tarball, "package/package.json"], { encoding: "utf8" });
const manifest = JSON.parse(raw);
const entries = new Set(
  execFileSync("tar", ["-tzf", tarball], { encoding: "utf8" })
    .split("\n")
    .filter(Boolean)
    .map((entry) => entry.replace(/^package\//, "")),
);

const problems = [];
if (raw.includes('"workspace:')) problems.push("packed package.json still contains workspace: ranges");
if (manifest.private) problems.push("packed package.json is private");
if (manifest.license !== "Apache-2.0") problems.push(`license is ${manifest.license}, not Apache-2.0`);
for (const required of ["LICENSE", "README.md", "package.json"]) {
  if (!entries.has(required)) problems.push(`${required} is missing from the tarball`);
}

const targets = [];
const collect = (value) => {
  if (typeof value === "string") targets.push(value);
  else if (value && typeof value === "object") Object.values(value).forEach(collect);
};
collect(manifest.exports);
for (const field of ["main", "module", "types"]) collect(manifest[field]);
if (targets.length === 0) problems.push("packed package.json declares no entry points");
for (const target of targets) {
  const path = target.replace(/^\.\//, "");
  if (path.includes("*")) {
    const prefix = path.slice(0, path.indexOf("*"));
    if (![...entries].some((entry) => entry.startsWith(prefix)))
      problems.push(`no packed file matches export ${target}`);
  } else if (!entries.has(path)) {
    problems.push(`export ${target} is not in the tarball`);
  }
}

if (problems.length) {
  for (const problem of problems) console.error(`::error::${manifest.name}: ${problem}`);
  process.exit(1);
}
console.log(`${manifest.name}@${manifest.version}: packed manifest OK (${targets.length} entry points)`);
