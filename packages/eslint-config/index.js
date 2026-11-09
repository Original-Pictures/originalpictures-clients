// Shared ESLint flat config for the TypeScript client packages.
// Non-type-aware for speed and reliability across polyglot roots.
import js from "@eslint/js";
import prettier from "eslint-config-prettier";
import globals from "globals";
import tseslint from "typescript-eslint";

/** @type {import('eslint').Linter.Config[]} */
export default tseslint.config(
  {
    ignores: [
      "**/dist/**",
      "**/.next/**",
      "**/.expo/**",
      "**/node_modules/**",
      "**/*.config.mjs",
      "**/*.config.js",
    ],
  },
  js.configs.recommended,
  ...tseslint.configs.recommended,
  {
    // Node-executed scripts and ESM tooling files get Node globals.
    files: ["**/scripts/**", "**/*.mjs", "**/*.cjs"],
    languageOptions: {
      globals: globals.node,
    },
  },
  // Turn off ESLint rules that conflict with Prettier formatting (keep last).
  prettier,
);
