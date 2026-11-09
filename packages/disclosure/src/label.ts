// <op-ai-label>: a visible AI label beside content, or (mode="offer") a switch
// that offers the label to whoever publishes the content. Rendering an applied
// label logs visible_label_applied; showing the offer logs
// visible_label_offered, and accepting it logs visible_label_applied.

import { BADGE_IDS, BADGE_LABELS, badgeSvg, type BadgeId, type BadgeVariant } from "./badges.ts";
import {
  THEME_CSS,
  ElementBase,
  el,
  logDisclosure,
  resolveFromAttributes,
} from "./component-support.ts";
import type { ResolvedDisclosure } from "./policy.ts";
import type { RuleKind } from "./policy-types.ts";

export const LABEL_TAG = "op-ai-label";

// Inline label text inherits the host page's ink: the label has no ground of
// its own, so a theme colour could vanish on the page behind it.
const STYLES = `${THEME_CSS}
:host{display:inline-block;vertical-align:middle}
.label{display:inline-flex;gap:8px;align-items:center;line-height:0}
.label .text{line-height:1.4;font-size:14px;color:inherit}
.dark{display:none}
@media (prefers-color-scheme:dark){:host(:not([theme="light"])) .light{display:none}:host(:not([theme="light"])) .dark{display:inline}}
:host([theme="dark"]) .light{display:none}
:host([theme="dark"]) .dark{display:inline}
.offer{display:inline-flex;gap:12px;align-items:center}
.switch{display:inline-flex;gap:8px;align-items:center;min-height:36px;padding:4px 12px 4px 4px;border-radius:999px;
  border:1px solid var(--op-border);background:var(--op-surface);color:var(--op-text);cursor:pointer}
.track{width:32px;height:20px;border-radius:999px;background:var(--op-border);position:relative;flex:none}
.track::after{content:"";position:absolute;top:2px;left:2px;width:16px;height:16px;border-radius:50%;background:var(--op-surface);
  box-shadow:0 0 0 1px var(--op-text-muted)}
.switch[aria-checked="true"] .track{background:var(--op-action-background)}
.switch[aria-checked="true"] .track::after{left:14px}
@media (prefers-reduced-motion:no-preference){.track::after{transition:left .15s}}
.preview[hidden]{display:none}
`;

let instances = 0;

function isBadgeId(value: string | null): value is BadgeId {
  return value !== null && (BADGE_IDS as readonly string[]).includes(value);
}

export class OpAiLabelElement extends ElementBase {
  static get observedAttributes(): string[] {
    return [
      "badge",
      "variant",
      "kind",
      "jurisdiction",
      "rule",
      "locale",
      "region",
      "mode",
      "show-text",
      "size",
    ];
  }

  #root: ShadowRoot;
  #id: string;
  #resolved: ResolvedDisclosure | null = null;
  #applied = false;
  #loggedOffer = false;
  #loggedApplied = false;

  constructor() {
    super();
    instances += 1;
    this.#id = `opl${instances}`;
    this.#root = this.attachShadow({ mode: "open" });
  }

  get resolved(): ResolvedDisclosure | null {
    return this.#resolved;
  }

  /** In offer mode, whether the person turned the label on. Always true otherwise. */
  get applied(): boolean {
    return this.#mode() === "applied" || this.#applied;
  }

  connectedCallback(): void {
    this.#render();
  }

  attributeChangedCallback(_name: string, previous: string | null, next: string | null): void {
    if (previous !== next && this.isConnected) this.#render();
  }

  #mode(): "applied" | "offer" {
    return this.getAttribute("mode") === "offer" ? "offer" : "applied";
  }

  #badge(): BadgeId {
    const requested = this.getAttribute("badge");
    if (isBadgeId(requested)) return requested;
    return this.#resolved?.badgeSet ?? "ai-generated";
  }

  #badgeMarkup(): HTMLElement {
    const badge = this.#badge();
    const label = BADGE_LABELS[badge];
    const height = Number.parseFloat(this.getAttribute("size") ?? "") || 28;
    const variant = this.getAttribute("variant") ?? "auto";
    // The wrapper carries the accessible name: the label plus the rule's text.
    const name = this.#resolved?.text ? `${label}: ${this.#resolved.text}` : label;
    const wrapper = el("span", { class: "badge", role: "img", "aria-label": name, part: "badge" });
    const svg = (v: BadgeVariant, cls: string) => {
      const span = el("span", { class: cls, "aria-hidden": "true" });
      // Our own generated SVG (escaped text), so markup insertion is safe here.
      span.innerHTML = badgeSvg(badge, v, { height, idPrefix: `${this.#id}-${cls}` });
      return span;
    };
    if (variant === "brand-light" || variant === "brand-dark" || variant === "neutral") {
      wrapper.append(svg(variant, "fixed"));
    } else {
      wrapper.append(svg("brand-light", "light"), svg("brand-dark", "dark"));
    }
    return wrapper;
  }

  #render(): void {
    const kind = (
      this.getAttribute("kind") === "deepfake_label" ? "deepfake_label" : "visible_label"
    ) as RuleKind;
    this.#resolved = resolveFromAttributes(this, kind);
    const style = el("style");
    style.textContent = STYLES;
    if (this.#mode() === "offer") {
      this.#root.replaceChildren(style, this.#renderOffer());
      if (!this.#loggedOffer && this.#resolved) {
        this.#loggedOffer = true;
        void logDisclosure(this, this.#resolved, "visible_label_offered");
      }
      return;
    }
    const label = el("span", { class: "label", part: "label" });
    label.append(this.#badgeMarkup());
    if (this.hasAttribute("show-text") && this.#resolved?.text) {
      const text = el("span", { class: "text", "aria-hidden": "true" }, this.#resolved.text);
      if (this.#resolved.locale) text.setAttribute("lang", this.#resolved.locale);
      label.append(text);
    }
    this.#root.replaceChildren(style, label);
    if (!this.#loggedApplied && this.#resolved) {
      this.#loggedApplied = true;
      void logDisclosure(this, this.#resolved, "visible_label_applied");
    }
  }

  #renderOffer(): HTMLElement {
    const wrapper = el("span", { class: "offer", part: "offer" });
    const name = BADGE_LABELS[this.#badge()];
    const toggle = el("button", {
      type: "button",
      role: "switch",
      class: "switch",
      part: "switch",
      "aria-checked": String(this.#applied),
    }) as HTMLButtonElement;
    toggle.append(
      el("span", { class: "track", "aria-hidden": "true" }),
      el("span", {}, this.getAttribute("offer-label") ?? `Add the “${name}” label`),
    );
    const preview = el("span", { class: "preview" });
    preview.append(this.#badgeMarkup());
    preview.hidden = !this.#applied;
    toggle.addEventListener("click", () => {
      this.#applied = !this.#applied;
      toggle.setAttribute("aria-checked", String(this.#applied));
      preview.hidden = !this.#applied;
      this.dispatchEvent(
        new CustomEvent("op-ai-label-change", {
          detail: { applied: this.#applied, badge: this.#badge() },
          bubbles: true,
          composed: true,
        }),
      );
      if (this.#applied && this.#resolved)
        void logDisclosure(this, this.#resolved, "visible_label_applied");
    });
    wrapper.append(toggle, preview);
    return wrapper;
  }
}

export function defineAiLabel(tagName: string = LABEL_TAG): void {
  if (typeof customElements === "undefined") return;
  if (!customElements.get(tagName)) customElements.define(tagName, OpAiLabelElement);
}
