// <op-verify page="slug">: a zero-dependency, shadow-DOM web component that
// checks a visitor's file against a verify page and shows its Content
// Credentials. All text goes in through textContent, never innerHTML, because
// the manifest fields it shows are attacker-controlled.
//
// Two modes:
// - upload (default): the visitor drops or chooses a file.
// - inspect (`src="https://..."` or `for="media-id"`): the element inspects an
//   asset the page already shows. It renders a compact chip that, when pressed,
//   loads the asset, runs the same public check, and expands into the card.
//   Every check is billed to the page owner, so it never runs on page view:
//   only on the first press of the chip, or on connect when the host opts in
//   with `autocheck`.

import {
  CHECK_STATEMENT,
  MAX_UPLOAD_BYTES,
  VerifyError,
  fetchMedia,
  fetchVerifyPage,
  normaliseApiBase,
  verify,
} from "./api.ts";
import {
  describeAvailability,
  describeLimits,
  describeResult,
  describeVerifyError,
  refusedBeforeUpload,
  type ResultView,
  type Tone,
} from "./describe.ts";
import { contrast, DARK, FONT_STACK, LIGHT, readableOn, themeCss } from "./tokens.ts";
import type { PublicCheckResult, PublicVerifyPage } from "./types.ts";

export const TAG_NAME = "op-verify";
const HOME_URL = "https://originalpictures.com/verify/";
const HEX = /^#[0-9a-fA-F]{6}$/;

/** What the inspection chip says before anything was checked. */
const CHIP_IDLE = "Check Content Credentials";
const FALLBACK_HINT = "You can save the file and drop it here to check it.";

type InspectState = "idle" | "busy" | "done" | "failed";

interface Parts {
  root: HTMLElement;
  head: HTMLElement;
  chip: HTMLButtonElement;
  chipDot: HTMLElement;
  chipLabel: HTMLElement;
  panel: HTMLElement;
  note: HTMLElement;
  title: HTMLElement;
  sub: HTMLElement;
  logo: HTMLImageElement;
  drop: HTMLElement;
  choose: HTMLButtonElement;
  input: HTMLInputElement;
  limits: HTMLElement;
  status: HTMLElement;
  error: HTMLElement;
  result: HTMLElement;
}

export interface VerifyResultEventDetail {
  result: PublicCheckResult;
}
export interface VerifyErrorEventDetail {
  code: string;
  message: string;
}

// `[hidden]{display:none!important}`: the UA rule for [hidden] loses to any class
// here that sets display (`.chip{display:inline-flex}`, `.drop{display:grid}`), so
// without it a part the element hides (the inspect chip in upload mode, the drop zone
// in inspect mode) would still render.
const STYLES = `
:host{display:block;max-width:44rem;font-family:${FONT_STACK};${themeCss(LIGHT)}
  --op-root-bg:var(--op-page-background,var(--op-surface));
  --op-root-fg:var(--op-page-text,var(--op-text));
  color-scheme:light}
@media (prefers-color-scheme:dark){:host(:not([theme="light"])){${themeCss(DARK)}
  --op-root-bg:var(--op-surface);--op-root-fg:var(--op-text);color-scheme:dark}}
:host([theme="dark"]){${themeCss(DARK)}--op-root-bg:var(--op-surface);--op-root-fg:var(--op-text);color-scheme:dark}
:host([hidden]){display:none}
[hidden]{display:none!important}
*{box-sizing:border-box}
.root{background:var(--op-root-bg);color:var(--op-root-fg);border:1px solid var(--op-border);
  border-radius:16px;padding:24px;line-height:1.5;font-size:16px}
.head{display:flex;gap:12px;align-items:center;margin-bottom:16px}
.logo{height:32px;width:auto;max-width:160px;object-fit:contain}
.title{margin:0;font-size:20px;font-weight:500;line-height:1.3}
.sub{margin:2px 0 0;color:var(--op-text-muted);font-size:14px}
.drop{border:2px dashed var(--op-border-strong);border-radius:12px;padding:24px;text-align:center;
  background:var(--op-sunken)}
.drop.dragging{border-style:solid;border-color:var(--op-focus)}
.drop p{margin:0 0 12px}
.drop .limits{margin:12px 0 0;font-size:14px;color:var(--op-text-muted)}
.btn{font:inherit;font-weight:500;min-height:44px;padding:10px 20px;border-radius:999px;cursor:pointer;
  border:1px solid transparent;background:var(--op-page-accent,var(--op-action-background));
  color:var(--op-page-accent-fg,var(--op-action-foreground))}
.btn.secondary{background:transparent;color:var(--op-root-fg);border-color:var(--op-border-strong)}
.btn:disabled{cursor:not-allowed;opacity:.6}
.btn:focus-visible,.result-title:focus-visible{outline:3px solid var(--op-focus);outline-offset:2px}
.status{margin:12px 0 0;min-height:1.5em;color:var(--op-text-secondary);font-size:14px}
.status[data-busy="true"]::before{content:"";display:inline-block;width:12px;height:12px;margin-right:8px;
  border:2px solid currentColor;border-right-color:transparent;border-radius:50%;vertical-align:-1px}
@media (prefers-reduced-motion:no-preference){.status[data-busy="true"]::before{animation:op-spin .8s linear infinite}}
@keyframes op-spin{to{transform:rotate(360deg)}}
.error{margin:12px 0 0;padding:12px 16px;border-radius:8px;background:var(--op-danger-background);
  color:var(--op-danger-foreground)}
.card{margin-top:16px;padding:20px;border-radius:12px;background:var(--op-surface);color:var(--op-text);
  border:1px solid var(--op-border)}
.result-title{margin:0 0 8px;font-size:18px;font-weight:500}
.pill{display:inline-block;margin:0 0 8px;padding:4px 12px;border-radius:999px;font-weight:500;font-size:14px}
.tone-success{background:var(--op-success-background);color:var(--op-success-foreground)}
.tone-warning{background:var(--op-warning-background);color:var(--op-warning-foreground)}
.tone-danger{background:var(--op-danger-background);color:var(--op-danger-foreground)}
.tone-neutral{background:var(--op-neutral-background);color:var(--op-neutral-foreground)}
.detail{margin:0 0 16px;color:var(--op-text-secondary)}
dl{margin:0 0 16px;display:grid;grid-template-columns:minmax(8rem,auto) 1fr;gap:6px 16px}
dt{color:var(--op-text-muted);font-size:14px}
dd{margin:0;overflow-wrap:anywhere}
.made{margin:0 0 16px;padding:16px;border-radius:8px;background:var(--op-sunken)}
.made h4{margin:0 0 4px;font-size:14px;font-weight:500;color:var(--op-text-muted)}
.made .answer{margin:0 0 4px;font-weight:500}
.made p{margin:0}
.statement{margin:0 0 16px;font-size:14px;color:var(--op-text-muted)}
.foot{margin-top:16px;font-size:12px;color:var(--op-text-muted)}
.foot a{color:var(--op-link)}
.chip{font:inherit;font-size:14px;font-weight:500;display:inline-flex;align-items:center;gap:8px;
  min-height:36px;padding:6px 14px;border-radius:999px;cursor:pointer;
  background:var(--op-surface);color:var(--op-text);border:1px solid var(--op-border-strong)}
.chip:focus-visible{outline:3px solid var(--op-focus);outline-offset:2px}
.chip[aria-busy="true"]{cursor:progress}
.chip .dot{width:10px;height:10px;border-radius:50%;flex:none;background:var(--op-border-strong)}
.chip .dot.tone-success{background:var(--op-success-foreground)}
.chip .dot.tone-warning{background:var(--op-warning-foreground)}
.chip .dot.tone-danger{background:var(--op-danger-foreground)}
.chip .dot.tone-neutral{background:var(--op-neutral-foreground)}
.chip .chev{font-size:12px;line-height:1}
@media (prefers-reduced-motion:no-preference){.chip .chev{transition:transform .15s ease}}
.chip[aria-expanded="true"] .chev{transform:rotate(180deg)}
.root.inspect{background:transparent;border:0;padding:0;color:inherit}
.root.inspect .panel{margin-top:8px;padding:16px;border-radius:12px;border:1px solid var(--op-border);
  background:var(--op-root-bg);color:var(--op-root-fg)}
.root.inspect .card{margin-top:0}
.note{margin:0 0 12px;color:var(--op-text-secondary)}
.visually-hidden{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
@media (max-width:480px){.root{padding:16px}dl{grid-template-columns:1fr}dd{margin-bottom:8px}}
@media (forced-colors:active){.btn,.chip{border-color:ButtonText}.drop{border-color:CanvasText}
  .chip .dot{forced-color-adjust:none;border:1px solid CanvasText}}
`;

// Server-side rendering imports this module too; only a browser defines elements.
const ElementBase: typeof HTMLElement =
  typeof HTMLElement === "undefined" ? (class {} as unknown as typeof HTMLElement) : HTMLElement;

let instances = 0;

export class OpVerifyElement extends ElementBase {
  static get observedAttributes(): string[] {
    return ["page", "api-base", "theme", "src", "for", "autocheck"];
  }

  #root: ShadowRoot;
  #ids: string;
  #config: PublicVerifyPage | null = null;
  #presetConfig: PublicVerifyPage | null = null;
  #abort: AbortController | null = null;
  #loadToken = 0;
  #els: Parts;
  #inspectState: InspectState = "idle";
  /** The mode last laid out; null until first connected. */
  #mode: "upload" | "inspect" | null = null;
  #expanded = false;

  constructor() {
    super();
    instances += 1;
    this.#ids = `opv${instances}`;
    this.#root = this.attachShadow({ mode: "open" });
    this.#els = this.#render();
  }

  /** A configuration the host page already fetched; skips the page request. */
  set pageConfig(config: PublicVerifyPage | null) {
    this.#presetConfig = config;
    if (this.isConnected && !this.#isInspect()) void this.#load();
  }
  get pageConfig(): PublicVerifyPage | null {
    return this.#config;
  }

  connectedCallback(): void {
    // A framework may set pageConfig before the element is defined; that lands
    // as an own property shadowing the accessor, so re-apply it through it.
    if (Object.prototype.hasOwnProperty.call(this, "pageConfig")) {
      const early = (this as { pageConfig?: PublicVerifyPage | null }).pageConfig ?? null;
      delete (this as { pageConfig?: unknown }).pageConfig;
      this.#presetConfig = early;
    }
    // Moving a connected element in the DOM keeps an inspection answer, so a
    // re-insert neither loses it nor bills a second automatic check.
    const mode = this.#isInspect() ? "inspect" : "upload";
    if (mode !== this.#mode) this.#applyMode();
    if (mode === "upload") {
      void this.#load();
    } else if (this.hasAttribute("autocheck") && this.#inspectState === "idle") {
      void this.#runInspection({ expand: false });
    }
  }

  disconnectedCallback(): void {
    this.#abort?.abort();
    this.#abort = null;
    // An inspection cut off mid-way produced no answer; let the chip start over.
    if (this.#inspectState === "busy") {
      this.#setChip(CHIP_IDLE, null, "idle");
      this.#setBusy(false, "");
    }
  }

  attributeChangedCallback(name: string, previous: string | null, next: string | null): void {
    if (previous === next || !this.isConnected) return;
    if (name === "theme") return;
    if (name === "autocheck") {
      if (next !== null && this.#isInspect() && this.#inspectState === "idle") {
        void this.#runInspection({ expand: false });
      }
      return;
    }
    // Any other change means a different page or a different asset: drop the
    // answer, which described the old one.
    this.#abort?.abort();
    this.#config = null;
    this.#applyMode();
    if (!this.#isInspect()) {
      void this.#load();
    } else if (this.hasAttribute("autocheck")) {
      void this.#runInspection({ expand: false });
    }
  }

  /**
   * Inspects the asset named by `src` or `for` and expands the card, as if the
   * visitor had pressed the chip. Billed to the page owner when the check runs.
   */
  async inspect(): Promise<PublicCheckResult | null> {
    if (!this.#isInspect()) return null;
    return this.#runInspection({ expand: true });
  }

  /** Checks a file programmatically, as if the visitor had chosen it. */
  async check(file: Blob): Promise<PublicCheckResult | null> {
    const abort = this.#startRun();
    this.#setBusy(true, "Checking the file…");
    return this.#checkBlob(file, abort, { fromSource: false });
  }

  #startRun(): AbortController {
    this.#abort?.abort();
    const abort = new AbortController();
    this.#abort = abort;
    this.#showError(null);
    this.#els.result.hidden = true;
    this.#els.result.replaceChildren();
    return abort;
  }

  async #checkBlob(
    file: Blob,
    abort: AbortController,
    { fromSource }: { fromSource: boolean },
  ): Promise<PublicCheckResult | null> {
    const slug = this.getAttribute("page") ?? "";
    const accepted = this.#config?.accepted_media_types ?? null;
    try {
      if (refusedBeforeUpload(file.type, accepted)) {
        // Said here, without a request: the page would refuse it, and every check it
        // answers is billed to the page owner.
        throw new VerifyError(
          "PUBLIC_CHECK_MEDIA_UNSUPPORTED",
          `a public check does not run ${file.type}; it accepts ${accepted?.join(", ") ?? ""}`,
          { status: 415 },
        );
      }
      const result = await verify(file, {
        page: slug,
        apiBase: this.#apiBase(),
        signal: abort.signal,
        maxUploadBytes: this.#config?.max_upload_bytes ?? MAX_UPLOAD_BYTES,
      });
      if (abort.signal.aborted) return null;
      this.#setBusy(false, "Check complete.");
      if (fromSource) {
        this.#hideFallback();
        const availability = describeAvailability(result);
        this.#setChip(availability.label, availability.tone, "done");
      }
      const inspect = this.#isInspect();
      // In inspect mode focus stays on the chip; an automatic check must never move it.
      this.#showResult(describeResult(result), { focus: !inspect, again: !fromSource });
      this.dispatchEvent(
        new CustomEvent<VerifyResultEventDetail>("op-verify-result", {
          detail: { result },
          bubbles: true,
          composed: true,
        }),
      );
      return result;
    } catch (error) {
      if (error instanceof VerifyError && error.code === "ABORTED") return null;
      this.#setBusy(false, "");
      const message = describeVerifyError(error, accepted);
      this.#showError(message);
      if (fromSource) {
        this.#setChip("Content Credentials could not be checked", "neutral", "failed");
        this.#showFallback(null);
      }
      this.#emitError(error, message);
      return null;
    } finally {
      if (this.#abort === abort) this.#abort = null;
    }
  }

  /** Clears the result and returns focus to the file button (or the chip). */
  reset(): void {
    this.#abort?.abort();
    this.#els.result.hidden = true;
    this.#els.result.replaceChildren();
    this.#showError(null);
    this.#setBusy(false, "");
    if (this.#isInspect() && this.#els.drop.hidden) this.#els.chip.focus();
    else this.#els.choose.focus();
  }

  #isInspect(): boolean {
    return this.hasAttribute("src") || this.hasAttribute("for");
  }

  /** Lays the element out for its mode and forgets any inspection answer. */
  #applyMode(): void {
    const inspect = this.#isInspect();
    this.#mode = inspect ? "inspect" : "upload";
    const { root, head, chip, panel, drop, result } = this.#els;
    root.classList.toggle("inspect", inspect);
    head.hidden = inspect;
    chip.hidden = !inspect;
    this.#inspectState = "idle";
    this.#setChip(CHIP_IDLE, null, "idle");
    this.#hideFallback();
    result.hidden = true;
    result.replaceChildren();
    this.#showError(null);
    this.#setBusy(false, "");
    if (inspect) {
      this.#setExpanded(false);
    } else {
      panel.hidden = false;
      drop.hidden = false;
    }
  }

  #onChip(): void {
    if (this.#inspectState === "idle") {
      void this.#runInspection({ expand: true });
      return;
    }
    // Once a check ran (or could not), the chip only shows and hides the
    // answer; it never runs and bills a second check.
    this.#setExpanded(!this.#expanded);
  }

  async #runInspection({ expand }: { expand: boolean }): Promise<PublicCheckResult | null> {
    if (this.#inspectState === "busy") return null;
    if (expand) this.#setExpanded(true);
    const abort = this.#startRun();
    this.#hideFallback();
    this.#setChip("Checking…", null, "busy");
    this.#setBusy(true, "Loading the media…");
    if (!(await this.#ensureConfig())) {
      if (abort.signal.aborted) return null;
      this.#setBusy(false, "");
      this.#setChip(CHIP_IDLE, null, "idle");
      if (this.#abort === abort) this.#abort = null;
      return null;
    }
    if (abort.signal.aborted) return null;
    let media: Blob;
    try {
      media = await fetchMedia(this.#mediaSource(), {
        signal: abort.signal,
        maxBytes: this.#config?.max_upload_bytes ?? MAX_UPLOAD_BYTES,
      });
    } catch (error) {
      if (this.#abort === abort) this.#abort = null;
      if (abort.signal.aborted || (error instanceof VerifyError && error.code === "ABORTED")) {
        return null;
      }
      // Nothing reached the check, so this is not an answer about the media.
      this.#setBusy(false, "Nothing was checked.");
      this.#setChip("Content Credentials could not be checked", null, "failed");
      const message = describeVerifyError(error);
      this.#showFallback(message);
      this.#emitError(error, message);
      return null;
    }
    if (abort.signal.aborted) return null;
    this.#setBusy(true, "Checking the media…");
    return this.#checkBlob(media, abort, { fromSource: true });
  }

  /** The asset to inspect: `src`, or the current source of the `for` element. */
  #mediaSource(): string {
    const src = this.getAttribute("src");
    if (src !== null) return src;
    const id = this.getAttribute("for") ?? "";
    const scope = this.getRootNode() as Document | ShadowRoot;
    const target = typeof scope.getElementById === "function" ? scope.getElementById(id) : null;
    if (!target) return "";
    const media = target as Partial<HTMLImageElement & HTMLMediaElement>;
    return (
      media.currentSrc ||
      target.getAttribute("src") ||
      target.querySelector("source[src]")?.getAttribute("src") ||
      ""
    );
  }

  /** Loads the page configuration if it is not loaded yet; true when it is. */
  async #ensureConfig(): Promise<boolean> {
    const slug = this.getAttribute("page") ?? "";
    if (this.#config?.slug === slug) return true;
    await this.#load();
    return this.#config !== null;
  }

  #setChip(label: string, tone: Tone | null, state: InspectState): void {
    const { chip, chipDot, chipLabel } = this.#els;
    this.#inspectState = state;
    chipLabel.textContent = label;
    chipDot.className = tone ? `dot tone-${tone}` : "dot";
    chip.setAttribute("aria-busy", String(state === "busy"));
  }

  #setExpanded(expanded: boolean): void {
    this.#expanded = expanded;
    this.#els.chip.setAttribute("aria-expanded", String(expanded));
    this.#els.panel.hidden = !expanded;
  }

  /** Offers the file-drop path after the page could not inspect the asset. */
  #showFallback(message: string | null): void {
    const { note, drop } = this.#els;
    note.textContent = message ? `${message} ${FALLBACK_HINT}` : FALLBACK_HINT;
    note.hidden = false;
    drop.hidden = false;
  }

  #hideFallback(): void {
    const { note, drop } = this.#els;
    note.textContent = "";
    note.hidden = true;
    drop.hidden = this.#isInspect();
  }

  #emitError(error: unknown, message: string): void {
    this.dispatchEvent(
      new CustomEvent<VerifyErrorEventDetail>("op-verify-error", {
        detail: { code: error instanceof VerifyError ? error.code : "UNKNOWN", message },
        bubbles: true,
        composed: true,
      }),
    );
  }

  #apiBase(): string | undefined {
    return this.getAttribute("api-base") ?? undefined;
  }

  async #load(): Promise<void> {
    const token = ++this.#loadToken;
    const slug = this.getAttribute("page") ?? "";
    this.#showError(null);
    if (this.#presetConfig && this.#presetConfig.slug === slug) {
      this.#applyConfig(this.#presetConfig);
      return;
    }
    this.#els.choose.disabled = true;
    try {
      const config = await fetchVerifyPage(slug, { apiBase: this.#apiBase() });
      if (token !== this.#loadToken) return;
      this.#applyConfig(config);
    } catch (error) {
      if (token !== this.#loadToken) return;
      this.#config = null;
      this.#showError(describeVerifyError(error));
    }
  }

  #applyConfig(config: PublicVerifyPage): void {
    this.#config = config;
    const { title, sub, logo, choose, limits } = this.#els;
    title.textContent = `Check a file with ${config.display_name}`;
    sub.textContent = `See its Content Credentials and whether ${config.display_name}'s system has a record of it.`;
    const logoUrl = this.#safeLogoUrl(config.logo_url);
    if (logoUrl) {
      logo.src = logoUrl;
      logo.alt = config.display_name;
      logo.hidden = false;
    } else {
      logo.removeAttribute("src");
      logo.hidden = true;
    }
    const accepted = config.accepted_media_types ?? null;
    limits.textContent = describeLimits(config.max_upload_bytes || MAX_UPLOAD_BYTES, accepted);
    if (accepted?.length) this.#els.input.accept = accepted.join(",");
    else this.#els.input.removeAttribute("accept");
    this.#applyColours(config);
    choose.disabled = false;
  }

  #safeLogoUrl(url: string | null): string | null {
    if (!url) return null;
    try {
      const parsed = new URL(url);
      if (parsed.protocol === "https:") return parsed.toString();
      const api = new URL(normaliseApiBase(this.#apiBase()));
      return parsed.origin === api.origin ? parsed.toString() : null;
    } catch {
      return null;
    }
  }

  #applyColours(config: PublicVerifyPage): void {
    const style = this.style;
    for (const name of [
      "--op-page-accent",
      "--op-page-accent-fg",
      "--op-page-background",
      "--op-page-text",
    ]) {
      style.removeProperty(name);
    }
    const { accent, background, text } = config.colours ?? {};
    if (accent && HEX.test(accent)) {
      style.setProperty("--op-page-accent", accent);
      style.setProperty("--op-page-accent-fg", readableOn(accent));
    }
    // The owner's ground and ink apply only as a readable pair (WCAG AA), and
    // only to the light theme; dark mode keeps the brand dark tokens.
    if (
      background &&
      text &&
      HEX.test(background) &&
      HEX.test(text) &&
      contrast(background, text) >= 4.5
    ) {
      style.setProperty("--op-page-background", background);
      style.setProperty("--op-page-text", text);
    }
  }

  #setBusy(busy: boolean, message: string): void {
    const { choose, status, drop } = this.#els;
    choose.disabled = busy || !this.#config;
    drop.setAttribute("aria-busy", String(busy));
    status.dataset.busy = String(busy);
    status.textContent = message;
  }

  #showError(message: string | null): void {
    const { error } = this.#els;
    error.textContent = message ?? "";
    error.hidden = message === null;
  }

  #showResult(view: ResultView, { focus, again }: { focus: boolean; again: boolean }): void {
    const { result } = this.#els;
    const card = el("article", { class: "card", "aria-labelledby": `${this.#ids}-rt` });
    const heading = el("h3", { class: "result-title", id: `${this.#ids}-rt`, tabindex: "-1" });
    heading.textContent = "Content Credentials";
    card.append(heading);
    card.append(
      text("p", view.credentials.headline, { class: `pill tone-${view.credentials.tone}` }),
    );
    card.append(text("p", view.credentials.detail, { class: "detail" }));
    if (view.origin.length) {
      const list = el("dl", { "aria-label": "What the file declares" });
      for (const row of view.origin) {
        const pair = el("div", { style: "display:contents" });
        pair.append(text("dt", row.label), text("dd", row.value));
        list.append(pair);
      }
      card.append(list);
    }
    if (view.madeWith) {
      const made = el("section", { class: "made", "aria-labelledby": `${this.#ids}-mw` });
      made.append(text("h4", view.madeWith.question, { id: `${this.#ids}-mw` }));
      made.append(text("p", view.madeWith.headline, { class: "answer" }));
      made.append(text("p", view.madeWith.detail));
      card.append(made);
    }
    card.append(text("p", view.statement || CHECK_STATEMENT, { class: "statement" }));
    if (again) {
      const button = text("button", "Check another file", {
        type: "button",
        class: "btn secondary",
      });
      button.addEventListener("click", () => this.reset());
      card.append(button);
    }
    result.replaceChildren(card);
    result.hidden = false;
    if (focus) heading.focus();
  }

  #render(): Parts {
    const id = this.#ids;
    const style = document.createElement("style");
    style.textContent = STYLES;
    const root = el("section", { class: "root", part: "root", "aria-labelledby": `${id}-t` });

    const head = el("header", { class: "head" });
    const logo = el("img", {
      class: "logo",
      part: "logo",
      alt: "",
      referrerpolicy: "no-referrer",
    }) as HTMLImageElement;
    logo.hidden = true;
    const titles = el("div");
    const title = text("h2", "Check a file's Content Credentials", {
      class: "title",
      id: `${id}-t`,
    });
    const sub = text("p", "Loading…", { class: "sub" });
    titles.append(title, sub);
    head.append(logo, titles);

    const chip = el("button", {
      type: "button",
      class: "chip",
      part: "chip",
      "aria-expanded": "false",
      "aria-controls": `${id}-p`,
    }) as HTMLButtonElement;
    const chipDot = el("span", { class: "dot", "aria-hidden": "true" });
    const chipLabel = text("span", CHIP_IDLE, { class: "chip-label" });
    chip.append(chipDot, chipLabel, text("span", "▾", { class: "chev", "aria-hidden": "true" }));
    chip.hidden = true;

    const panel = el("div", { class: "panel", part: "panel", id: `${id}-p` });
    const note = el("p", { class: "note" });
    note.hidden = true;

    const drop = el("div", { class: "drop", part: "dropzone" });
    const help = text("p", "Drop a file here, or", { id: `${id}-h` });
    const choose = text("button", "Choose a file", {
      type: "button",
      class: "btn",
      part: "button",
      "aria-describedby": `${id}-h ${id}-l`,
    }) as HTMLButtonElement;
    choose.disabled = true;
    const limits = text("p", "", { class: "limits", id: `${id}-l` });
    const input = el("input", {
      type: "file",
      tabindex: "-1",
      "aria-hidden": "true",
    }) as HTMLInputElement;
    input.hidden = true;
    drop.append(help, choose, limits, input);

    const status = el("p", { class: "status", role: "status", "aria-live": "polite" });
    const error = el("div", { class: "error", role: "alert" });
    error.hidden = true;
    const result = el("div", { class: "result" });
    result.hidden = true;

    const foot = el("p", { class: "foot" });
    const link = text("a", "Original Pictures", {
      href: HOME_URL,
      target: "_blank",
      rel: "noopener",
    });
    foot.append("Checks by ", link);

    panel.append(note, drop, status, error, result, foot);
    root.append(head, chip, panel);
    this.#root.append(style, root);

    chip.addEventListener("click", () => this.#onChip());
    choose.addEventListener("click", () => input.click());
    input.addEventListener("change", () => {
      const file = input.files?.[0];
      input.value = "";
      if (file) void this.check(file);
    });
    drop.addEventListener("dragover", (event) => {
      event.preventDefault();
      if (!choose.disabled) drop.classList.add("dragging");
    });
    drop.addEventListener("dragleave", () => drop.classList.remove("dragging"));
    drop.addEventListener("drop", (event) => {
      event.preventDefault();
      drop.classList.remove("dragging");
      if (choose.disabled) return;
      const file = (event as DragEvent).dataTransfer?.files?.[0];
      if (file) void this.check(file);
    });

    return {
      root,
      head,
      chip,
      chipDot,
      chipLabel,
      panel,
      note,
      title,
      sub,
      logo,
      drop,
      choose,
      input,
      limits,
      status,
      error,
      result,
    };
  }
}

function el(tag: string, attributes: Record<string, string> = {}): HTMLElement {
  const node = document.createElement(tag);
  for (const [name, value] of Object.entries(attributes)) node.setAttribute(name, value);
  return node;
}

function text(tag: string, content: string, attributes: Record<string, string> = {}): HTMLElement {
  const node = el(tag, attributes);
  node.textContent = content;
  return node;
}

/** Registers <op-verify> once; safe to call repeatedly and on the server. */
export function defineOpVerify(tagName: string = TAG_NAME): void {
  if (typeof customElements === "undefined") return;
  if (!customElements.get(tagName)) customElements.define(tagName, OpVerifyElement);
}

declare global {
  interface HTMLElementTagNameMap {
    "op-verify": OpVerifyElement;
  }
}
