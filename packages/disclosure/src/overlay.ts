// badge(): put a visible AI label on an image in the browser. On an <img> it
// overlays the badge in the DOM and leaves the image untouched; on a Blob it
// draws a labelled copy. Nothing is sent to a server except, when a client is
// given, the visible_label_applied event.

import {
  BADGE_LABELS,
  badgeDataUrl,
  badgeSize,
  type BadgeId,
  type BadgeVariant,
} from "./badges.ts";
import {
  eventFor,
  type DisclosureClient,
  type DisclosureEventReceipt,
  type Surface,
} from "./events.ts";
import type { ResolvedDisclosure } from "./policy.ts";

export type BadgePosition = "top-left" | "top-right" | "bottom-left" | "bottom-right";

export interface BadgeOverlayOptions {
  badge?: BadgeId;
  variant?: BadgeVariant;
  position?: BadgePosition;
  /** Badge height as a fraction of the image's shorter side (default 0.06, at least 20 px). */
  scale?: number;
  /** Gap from the edges as a fraction of the shorter side (default 0.02). */
  margin?: number;
  /** Log visible_label_applied for this labelling. */
  disclosure?: {
    client: DisclosureClient;
    resolved: ResolvedDisclosure;
    subjectRef: string;
    contentRef?: string | null;
    surface?: Surface;
  };
}

export interface BadgeOverlayHandle {
  /** The overlay <img>. */
  element: HTMLImageElement;
  /** The event receipt when a client was given and the log answered. */
  receipt: Promise<DisclosureEventReceipt | null>;
  /** Removes the overlay and unwraps the image. */
  remove(): void;
}

export interface Placement {
  x: number;
  y: number;
  width: number;
  height: number;
}

/** Where a badge of natural size badgeWidth x badgeHeight goes on an image. */
export function badgePlacement(
  imageWidth: number,
  imageHeight: number,
  badge: { width: number; height: number },
  options: Pick<BadgeOverlayOptions, "position" | "scale" | "margin"> = {},
): Placement {
  const shorter = Math.min(imageWidth, imageHeight);
  const height = Math.min(Math.max(shorter * (options.scale ?? 0.06), 20), imageHeight);
  const width = Math.min((badge.width / badge.height) * height, imageWidth);
  const gap = Math.round(shorter * (options.margin ?? 0.02));
  const position = options.position ?? "bottom-right";
  const x = position.endsWith("left") ? gap : imageWidth - width - gap;
  const y = position.startsWith("top") ? gap : imageHeight - height - gap;
  return {
    x: Math.max(0, Math.round(x)),
    y: Math.max(0, Math.round(y)),
    width: Math.round(width),
    height: Math.round(height),
  };
}

function logApplied(options: BadgeOverlayOptions): Promise<DisclosureEventReceipt | null> {
  const disclosure = options.disclosure;
  if (!disclosure) return Promise.resolve(null);
  return disclosure.client
    .log(eventFor(disclosure.resolved, "visible_label_applied", disclosure))
    .catch(() => null);
}

const WRAPPER_ATTRIBUTE = "data-op-ai-badge";

function overlayImage(image: HTMLImageElement, options: BadgeOverlayOptions): BadgeOverlayHandle {
  const id = options.badge ?? "ai-generated";
  const variant = options.variant ?? "brand-light";
  const doc = image.ownerDocument;
  let wrapper = image.parentElement;
  const wrapped = wrapper?.hasAttribute(WRAPPER_ATTRIBUTE) ?? false;
  if (!wrapped || !wrapper) {
    wrapper = doc.createElement("span");
    wrapper.setAttribute(WRAPPER_ATTRIBUTE, "");
    wrapper.style.position = "relative";
    wrapper.style.display = "inline-block";
    wrapper.style.lineHeight = "0";
    image.replaceWith(wrapper);
    wrapper.append(image);
  }
  const overlay = doc.createElement("img");
  overlay.src = badgeDataUrl(id, variant);
  overlay.alt = BADGE_LABELS[id];
  overlay.setAttribute("part", "ai-badge");
  overlay.style.position = "absolute";
  overlay.style.pointerEvents = "none";
  const position = options.position ?? "bottom-right";
  const margin = `${Math.round((options.margin ?? 0.02) * 100)}%`;
  overlay.style.height = `max(20px, ${Math.round((options.scale ?? 0.06) * 1000) / 10}%)`;
  overlay.style.width = "auto";
  overlay.style[position.startsWith("top") ? "top" : "bottom"] = margin;
  overlay.style[position.endsWith("left") ? "left" : "right"] = margin;
  wrapper.append(overlay);
  const container = wrapper;
  return {
    element: overlay,
    receipt: logApplied(options),
    remove() {
      overlay.remove();
      if (
        container.hasAttribute(WRAPPER_ATTRIBUTE) &&
        !container.querySelector(`img[part="ai-badge"]`)
      ) {
        container.replaceWith(image);
      }
    },
  };
}

async function loadImage(src: string): Promise<HTMLImageElement> {
  const image = new Image();
  image.src = src;
  await image.decode();
  return image;
}

async function labelBlob(blob: Blob, options: BadgeOverlayOptions): Promise<Blob> {
  const id = options.badge ?? "ai-generated";
  const variant = options.variant ?? "brand-light";
  const bitmap = await createImageBitmap(blob);
  const canvas = document.createElement("canvas");
  canvas.width = bitmap.width;
  canvas.height = bitmap.height;
  const context = canvas.getContext("2d");
  if (!context) throw new Error("this browser cannot draw images");
  context.drawImage(bitmap, 0, 0);
  bitmap.close?.();
  const place = badgePlacement(canvas.width, canvas.height, badgeSize(BADGE_LABELS[id]), options);
  const badgeImage = await loadImage(badgeDataUrl(id, variant, { height: place.height }));
  context.drawImage(badgeImage, place.x, place.y, place.width, place.height);
  const type = ["image/png", "image/jpeg", "image/webp"].includes(blob.type)
    ? blob.type
    : "image/png";
  const result = await new Promise<Blob | null>((resolve) => canvas.toBlob(resolve, type, 0.92));
  if (!result) throw new Error("the labelled image could not be encoded");
  await logApplied(options);
  return result;
}

/**
 * Labels an image visibly.
 *
 * - `badge(imgElement)` overlays the badge on the page; the image file is not
 *   changed. Returns a handle with `remove()`.
 * - `badge(blob)` returns a new image with the badge drawn in. It is a new
 *   encoding, so any Content Credentials in the original are not carried over:
 *   label first, then sign the labelled copy if it is to be published.
 */
export function badge(
  target: HTMLImageElement,
  options?: BadgeOverlayOptions,
): Promise<BadgeOverlayHandle>;
export function badge(target: Blob, options?: BadgeOverlayOptions): Promise<Blob>;
export async function badge(
  target: HTMLImageElement | Blob,
  options: BadgeOverlayOptions = {},
): Promise<BadgeOverlayHandle | Blob> {
  if (typeof Blob !== "undefined" && target instanceof Blob) return labelBlob(target, options);
  if (typeof HTMLImageElement !== "undefined" && target instanceof HTMLImageElement) {
    return overlayImage(target, options);
  }
  throw new TypeError("badge() takes an <img> element or an image Blob");
}
