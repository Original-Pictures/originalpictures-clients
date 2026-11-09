// <op-ai-notice>: the first-interaction notice for a chatbot or other AI
// system, with the text, form and timing of the jurisdiction's draft rule.
// Shown when it connects (or on request where the rule says so), logged as
// ai_interaction_notice; acknowledging it logs user_acknowledged and leaves a
// small "AI" chip so the disclosure stays reachable.

import { badgeSvg } from "./badges.ts";
import {
  THEME_CSS,
  ElementBase,
  el,
  logDisclosure,
  resolveFromAttributes,
} from "./component-support.ts";
import type { ResolvedDisclosure } from "./policy.ts";

export const NOTICE_TAG = "op-ai-notice";
type Remember = "none" | "session" | "local";

const STYLES = `${THEME_CSS}
:host{display:block}
.notice{display:flex;gap:12px;align-items:center;padding:12px 16px;border-radius:12px;
  background:var(--op-sunken);color:var(--op-text);border:1px solid var(--op-border);line-height:1.5}
.notice[hidden],.chip[hidden]{display:none}
.icon{flex:none;line-height:0}
.text{margin:0;flex:1;font-size:15px}
.ack{flex:none;min-height:36px;padding:6px 16px;border-radius:999px;border:1px solid transparent;cursor:pointer;
  background:var(--op-action-background);color:var(--op-action-foreground);font-weight:500}
.chip{min-height:28px;padding:2px 10px;border-radius:999px;border:1px solid var(--op-border);cursor:pointer;
  background:var(--op-surface);color:var(--op-text-muted);font-size:13px;font-weight:500}
`;

let instances = 0;

export class OpAiNoticeElement extends ElementBase {
  static get observedAttributes(): string[] {
    return ["jurisdiction", "rule", "locale", "region"];
  }

  #root: ShadowRoot;
  #id: string;
  #resolved: ResolvedDisclosure | null = null;
  #notice: HTMLElement;
  #text: HTMLElement;
  #ack: HTMLButtonElement;
  #chip: HTMLButtonElement;
  #icon: HTMLElement;
  #logged = false;

  constructor() {
    super();
    instances += 1;
    this.#id = `opn${instances}`;
    this.#root = this.attachShadow({ mode: "open" });
    const style = el("style");
    style.textContent = STYLES;
    this.#notice = el("div", {
      class: "notice",
      part: "notice",
      role: "note",
      "aria-label": "AI disclosure",
    });
    this.#notice.hidden = true;
    this.#icon = el("span", { class: "icon", "aria-hidden": "true" });
    this.#text = el("p", { class: "text", id: `${this.#id}-t` });
    this.#ack = el(
      "button",
      { type: "button", class: "ack", part: "button", "aria-describedby": `${this.#id}-t` },
      "OK",
    ) as HTMLButtonElement;
    this.#notice.append(this.#icon, this.#text, this.#ack);
    this.#chip = el(
      "button",
      { type: "button", class: "chip", part: "chip", "aria-expanded": "false" },
      "AI",
    ) as HTMLButtonElement;
    this.#chip.hidden = true;
    this.#root.append(style, this.#notice, this.#chip);
    this.#ack.addEventListener("click", () => void this.acknowledge());
    this.#chip.addEventListener("click", () => this.#expand());
  }

  /** The rule and text this notice shows. */
  get resolved(): ResolvedDisclosure | null {
    return this.#resolved;
  }

  connectedCallback(): void {
    this.#init();
  }

  attributeChangedCallback(_name: string, previous: string | null, next: string | null): void {
    if (previous !== next && this.isConnected) this.#init();
  }

  /** Shows the notice now: for on-request rules, or to repeat it. Logs it once per showing. */
  show(): void {
    if (!this.#resolved) return;
    this.#chip.hidden = true;
    this.#chip.setAttribute("aria-expanded", "true");
    this.#notice.hidden = false;
    void logDisclosure(this, this.#resolved, "ai_interaction_notice");
    this.#logged = true;
  }

  /** Records that the person acknowledged the notice and collapses it to the chip. */
  async acknowledge(): Promise<void> {
    if (!this.#resolved || this.#notice.hidden) return;
    this.#notice.hidden = true;
    this.#chip.hidden = false;
    this.#chip.setAttribute("aria-expanded", "false");
    this.#chip.focus();
    this.#remember();
    await logDisclosure(this, this.#resolved, "user_acknowledged");
  }

  #init(): void {
    const resolved = resolveFromAttributes(this, "ai_interaction_notice");
    this.#resolved = resolved;
    if (!resolved?.text) {
      this.#notice.hidden = true;
      this.#chip.hidden = true;
      return;
    }
    this.#text.textContent = resolved.text;
    if (resolved.locale) this.#text.setAttribute("lang", resolved.locale);
    this.#ack.textContent = this.getAttribute("acknowledge-label") ?? "OK";
    this.#chip.setAttribute("aria-label", resolved.text);
    this.#chip.title = resolved.text;
    // Our own generated SVG (escaped text), so markup insertion is safe here.
    this.#icon.innerHTML = badgeSvg("ai-interaction", "neutral", {
      label: "AI",
      height: 20,
      idPrefix: this.#id,
    });
    if (resolved.timing === "on_request") {
      this.#notice.hidden = true;
      this.#chip.hidden = true;
      return;
    }
    if (this.#acknowledgedRecently()) {
      this.#notice.hidden = true;
      this.#chip.hidden = false;
      return;
    }
    if (!this.#logged) this.show();
  }

  #expand(): void {
    this.#chip.hidden = true;
    this.#notice.hidden = false;
    this.#ack.focus();
  }

  #storage(): Storage | null {
    const remember = (this.getAttribute("remember") ?? "session") as Remember;
    try {
      if (remember === "local") return globalThis.localStorage ?? null;
      if (remember === "session") return globalThis.sessionStorage ?? null;
    } catch {
      // Blocked storage: the notice shows every time, which errs on the side of showing it.
    }
    return null;
  }

  #storageKey(): string {
    return `op-ai-notice:${this.#resolved?.rule.id}:${this.#resolved?.policyVersion}`;
  }

  #remember(): void {
    try {
      this.#storage()?.setItem(this.#storageKey(), String(Date.now()));
    } catch {
      // Not remembering only means the notice is shown again next time.
    }
  }

  #acknowledgedRecently(): boolean {
    try {
      const value = this.#storage()?.getItem(this.#storageKey());
      if (!value) return false;
      const repeatMinutes = Number.parseFloat(this.getAttribute("repeat-after") ?? "");
      if (!Number.isFinite(repeatMinutes) || repeatMinutes <= 0) return true;
      return Date.now() - Number(value) < repeatMinutes * 60_000;
    } catch {
      return false;
    }
  }
}

export function defineAiNotice(tagName: string = NOTICE_TAG): void {
  if (typeof customElements === "undefined") return;
  if (!customElements.get(tagName)) customElements.define(tagName, OpAiNoticeElement);
}
