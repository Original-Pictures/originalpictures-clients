// Builds the publishable bundles: ESM (dist/index.js, dist/core.js), a
// script-tag IIFE (dist/disclosure.iife.js, global OriginalPicturesDisclosure,
// which defines both elements on load), declarations under dist/types, and the
// policy document and badge SVGs as files under dist/.
import { cpSync, readdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { createRequire } from "node:module";
import { spawnSync } from "node:child_process";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { build } from "esbuild";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const dist = join(root, "dist");
rmSync(dist, { recursive: true, force: true });

const check = spawnSync(process.execPath, [join(root, "scripts/generate.mjs"), "--check"], {
  stdio: "inherit",
});
if (check.status !== 0) process.exit(check.status ?? 1);

const shared = { bundle: true, target: "es2022", legalComments: "none", logLevel: "warning" };
await build({
  ...shared,
  entryPoints: [join(root, "src/index.ts"), join(root, "src/core.ts")],
  outdir: dist,
  format: "esm",
  splitting: true,
  chunkNames: "chunks/[name]-[hash]",
});
await build({
  ...shared,
  entryPoints: [join(root, "src/index.ts")],
  outfile: join(dist, "disclosure.iife.js"),
  format: "iife",
  globalName: "OriginalPicturesDisclosure",
  minify: true,
});

cpSync(join(root, "assets/badges"), join(dist, "badges"), { recursive: true });
cpSync(join(root, "assets/policy"), join(dist, "policy"), { recursive: true });

const tscBin = createRequire(import.meta.url).resolve("typescript/bin/tsc");
const tsc = spawnSync(process.execPath, [tscBin, "-p", "tsconfig.build.json"], {
  cwd: root,
  stdio: "inherit",
});
if (tsc.status !== 0) process.exit(tsc.status ?? 1);

// Sources import "./x.ts" (bundler resolution); published declarations must
// name the ".js" files a Node-resolution consumer would load.
const types = join(dist, "types");
for (const name of readdirSync(types)) {
  const path = join(types, name);
  if (!name.endsWith(".d.ts")) continue;
  writeFileSync(path, readFileSync(path, "utf8").replace(/(from\s+"\.\/[^"]+)\.ts"/g, '$1.js"'));
}
