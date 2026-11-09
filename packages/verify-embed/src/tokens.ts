// Brand values from @op/design-tokens (themes.light / themes.dark in
// dist/tokens.json), copied so the embed ships with no runtime dependency.
// tests/tokens.test.ts fails if they drift from the design-tokens package.

export interface ThemeTokens {
  canvas: string;
  surface: string;
  sunken: string;
  text: string;
  textSecondary: string;
  textMuted: string;
  border: string;
  borderStrong: string;
  focus: string;
  link: string;
  actionBackground: string;
  actionForeground: string;
  successForeground: string;
  successBackground: string;
  warningForeground: string;
  warningBackground: string;
  dangerForeground: string;
  dangerBackground: string;
  neutralForeground: string;
  neutralBackground: string;
}

export const LIGHT: ThemeTokens = {
  canvas: "#F5F9FC",
  surface: "#FFFFFF",
  sunken: "#EEF3F7",
  text: "#0A1C28",
  textSecondary: "#345D73",
  textMuted: "#4A6577",
  border: "#D8E2E9",
  borderStrong: "#5E7A8C",
  focus: "#00748C",
  link: "#00748C",
  actionBackground: "#0A1C28",
  actionForeground: "#F5F9FC",
  successForeground: "#0A7A45",
  successBackground: "#DDF3E7",
  warningForeground: "#7A5100",
  warningBackground: "#FFF1CC",
  dangerForeground: "#A3141F",
  dangerBackground: "#F9E0E2",
  neutralForeground: "#4A6577",
  neutralBackground: "#E6EDF2",
};

export const DARK: ThemeTokens = {
  canvas: "#0A1C28",
  surface: "#0E242F",
  sunken: "#071520",
  text: "#F5F9FC",
  textSecondary: "#D3DEE6",
  textMuted: "#A9BCCB",
  border: "#F5F9FC38",
  borderStrong: "#A9BCCB",
  focus: "#05E4FF",
  link: "#05E4FF",
  actionBackground: "#FDF6EA",
  actionForeground: "#0A1C28",
  successForeground: "#20EC84",
  successBackground: "#0F3326",
  warningForeground: "#FFC84A",
  warningBackground: "#3B2D12",
  dangerForeground: "#F69A92",
  dangerBackground: "#431F22",
  neutralForeground: "#A9BCCB",
  neutralBackground: "#1C3240",
};

/** Where each token comes from in @op/design-tokens' tokens.json. */
export const TOKEN_SOURCES: Readonly<Record<keyof ThemeTokens, string>> = {
  canvas: "background.canvas",
  surface: "surface.default",
  sunken: "surface.sunken",
  text: "text.primary",
  textSecondary: "text.secondary",
  textMuted: "text.muted",
  border: "border.default",
  borderStrong: "border.strong",
  focus: "border.focus",
  link: "text.link",
  actionBackground: "action.primary.background",
  actionForeground: "action.primary.foreground",
  successForeground: "status.success.foreground",
  successBackground: "status.success.background",
  warningForeground: "status.warning.foreground",
  warningBackground: "status.warning.background",
  dangerForeground: "status.danger.foreground",
  dangerBackground: "status.danger.background",
  neutralForeground: "status.neutral.foreground",
  neutralBackground: "status.neutral.background",
};

export const FONT_STACK =
  '"IBM Plex Sans", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif';

/** CSS custom property declarations for one theme. */
export function themeCss(tokens: ThemeTokens): string {
  return (Object.keys(tokens) as (keyof ThemeTokens)[])
    .map((key) => `--op-${kebab(key)}:${tokens[key]};`)
    .join("");
}

function kebab(name: string): string {
  return name.replace(/[A-Z]/g, (letter) => `-${letter.toLowerCase()}`);
}

/** WCAG relative luminance of a #rrggbb colour. */
export function luminance(hex: string): number {
  const channels = [1, 3, 5].map((offset) => {
    const value = parseInt(hex.slice(offset, offset + 2), 16) / 255;
    return value <= 0.03928 ? value / 12.92 : ((value + 0.055) / 1.055) ** 2.4;
  });
  const [r = 0, g = 0, b = 0] = channels;
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
}

/** WCAG contrast ratio between two #rrggbb colours. */
export function contrast(a: string, b: string): number {
  const [hi, lo] = [luminance(a), luminance(b)].sort((x, y) => y - x) as [number, number];
  return (hi + 0.05) / (lo + 0.05);
}

/** The brand ink or light text, whichever reads better on `background`. */
export function readableOn(background: string): string {
  return contrast(background, LIGHT.text) >= contrast(background, DARK.text)
    ? LIGHT.text
    : DARK.text;
}
