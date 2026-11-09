// Brand values from @op/design-tokens (themes.light / themes.dark and the
// brand primitives), copied so the package ships with no runtime dependency.
// tests/tokens.test.ts fails if they drift.

export const FONT_STACK =
  '"IBM Plex Sans", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif';

export const LIGHT = {
  surface: "#FFFFFF",
  sunken: "#EEF3F7",
  text: "#0A1C28",
  textMuted: "#4A6577",
  border: "#D8E2E9",
  focus: "#00748C",
  actionBackground: "#0A1C28",
  actionForeground: "#F5F9FC",
} as const;

export const DARK = {
  surface: "#0E242F",
  sunken: "#071520",
  text: "#F5F9FC",
  textMuted: "#A9BCCB",
  border: "#F5F9FC38",
  focus: "#05E4FF",
  actionBackground: "#FDF6EA",
  actionForeground: "#0A1C28",
} as const;

export const TOKEN_SOURCES: Readonly<Record<keyof typeof LIGHT, string>> = {
  surface: "surface.default",
  sunken: "surface.sunken",
  text: "text.primary",
  textMuted: "text.muted",
  border: "border.default",
  focus: "border.focus",
  actionBackground: "action.primary.background",
  actionForeground: "action.primary.foreground",
};

/** Brand primitives the badges use (tokens.json "shared" brand.*). */
export const BRAND = {
  deepSea: "#0A1C28",
  paleBlue: "#F5F9FC",
  paper: "#FDF6EA",
  brass: "#CFA274",
} as const;
/** primitives.color.brand.brassDeep: brass that carries text on a light ground. */
export const BRASS_DEEP = "#8A5E32";

export function themeCss(tokens: Readonly<Record<string, string>>): string {
  return Object.entries(tokens)
    .map(([key, value]) => `--op-${key.replace(/[A-Z]/g, (c) => `-${c.toLowerCase()}`)}:${value};`)
    .join("");
}
