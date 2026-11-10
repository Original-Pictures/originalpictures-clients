import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import "../src/index.ts";
import { OpVerifyElement as OpVerifyElementClass, type OpVerifyElement } from "../src/element.ts";
import { PAGE, STATEMENT, VERDICT_WORDS, completed, json, mockFetch } from "./fixtures.ts";

let fetchMock: ReturnType<typeof mockFetch>;

beforeEach(() => {
  document.body.replaceChildren();
});

afterEach(() => {
  vi.unstubAllGlobals();
});

async function settle(): Promise<void> {
  for (let i = 0; i < 5; i += 1) await new Promise((resolve) => setTimeout(resolve, 0));
}

async function mount(
  attributes: Record<string, string> = { page: "studio-nova" },
  ...answers: (Response | Error)[]
) {
  fetchMock = mockFetch(...answers);
  vi.stubGlobal("fetch", fetchMock);
  const element = document.createElement("op-verify") as OpVerifyElement;
  for (const [name, value] of Object.entries(attributes)) element.setAttribute(name, value);
  document.body.append(element);
  await settle();
  const root = element.shadowRoot!;
  const button = root.querySelector<HTMLButtonElement>("button.btn")!;
  return { element, root, button };
}

function dropFile(root: ShadowRoot, file: File): void {
  const event = new Event("drop", { bubbles: true, cancelable: true });
  Object.defineProperty(event, "dataTransfer", { value: { files: [file] } });
  root.querySelector(".drop")!.dispatchEvent(event);
}

const jpeg = () =>
  new File([new Uint8Array([0xff, 0xd8, 0xff])], "holiday.jpg", { type: "image/jpeg" });

describe("<op-verify>", () => {
  it("is defined on import and renders accessible landmarks", async () => {
    expect(customElements.get("op-verify")).toBeDefined();
    const { root, button } = await mount(undefined, json(PAGE));
    const section = root.querySelector("section.root")!;
    const titleId = section.getAttribute("aria-labelledby")!;
    expect(root.getElementById(titleId)?.textContent).toBe("Check a file with Studio Nova");
    expect(button.getAttribute("type")).toBe("button");
    expect(button.disabled).toBe(false);
    for (const id of button.getAttribute("aria-describedby")!.split(" ")) {
      expect(root.getElementById(id)).not.toBeNull();
    }
    const status = root.querySelector(".status")!;
    expect(status.getAttribute("role")).toBe("status");
    expect(status.getAttribute("aria-live")).toBe("polite");
    expect(root.querySelector(".error")!.getAttribute("role")).toBe("alert");
    const input = root.querySelector<HTMLInputElement>("input[type=file]")!;
    expect(input.hidden).toBe(true);
    expect(input.getAttribute("tabindex")).toBe("-1");
    const logo = root.querySelector<HTMLImageElement>("img.logo")!;
    expect(logo.hidden).toBe(false);
    expect(logo.alt).toBe("Studio Nova");
    expect(fetchMock.calls[0]?.url).toBe(
      "https://api.originalpictures.com/v1/public/verify-pages/studio-nova",
    );
  });

  it("opens the file picker from the keyboard-reachable button", async () => {
    const { root, button } = await mount(undefined, json(PAGE));
    const input = root.querySelector<HTMLInputElement>("input[type=file]")!;
    const click = vi.spyOn(input, "click").mockImplementation(() => undefined);
    button.focus();
    expect(root.activeElement).toBe(button);
    button.click();
    expect(click).toHaveBeenCalledOnce();
  });

  it("checks a dropped file, shows the card, moves focus and emits the result", async () => {
    const { element, root } = await mount(undefined, json(PAGE), json(completed()));
    const seen = vi.fn();
    element.addEventListener("op-verify-result", (event) => seen((event as CustomEvent).detail));
    dropFile(root, jpeg());
    await settle();
    const card = root.querySelector("article.card")!;
    expect(card).not.toBeNull();
    expect(card.querySelector(".pill")?.textContent).toBe("Content Credentials found");
    expect(card.querySelector(".statement")?.textContent).toBe(STATEMENT);
    expect(card.querySelector(".made .answer")?.textContent).toBe(
      "Yes: Studio Nova's system has a record of this file",
    );
    expect(root.activeElement?.classList.contains("result-title")).toBe(true);
    expect(root.querySelector(".status")?.textContent).toBe("Check complete.");
    expect(seen).toHaveBeenCalledWith({ result: completed() });
    const text = card.textContent!.replace(STATEMENT, "");
    expect(text).not.toMatch(VERDICT_WORDS);
  });

  it("renders manifest fields as text, never markup", async () => {
    const hostile = completed();
    hostile.content_credentials!.declared_origin!.signed_by = '<img src=x onerror="alert(1)">';
    const { root } = await mount(undefined, json(PAGE), json(hostile));
    dropFile(root, jpeg());
    await settle();
    expect(root.querySelector("article.card img")).toBeNull();
    expect(root.querySelector("dd")?.textContent).toBe('<img src=x onerror="alert(1)">');
  });

  it("returns focus to the button when checking another file", async () => {
    const { root, button } = await mount(undefined, json(PAGE), json(completed()));
    dropFile(root, jpeg());
    await settle();
    root.querySelector<HTMLButtonElement>("button.secondary")!.click();
    expect(root.querySelector(".result")!.hasAttribute("hidden")).toBe(true);
    expect(root.activeElement).toBe(button);
  });

  it("announces errors in the alert region", async () => {
    const { element, root } = await mount(
      undefined,
      json(PAGE),
      json({ code: "PUBLIC_CHECK_RATE_LIMITED", message: "x" }, 429, { "Retry-After": "9" }),
    );
    const errors = vi.fn();
    element.addEventListener("op-verify-error", (event) => errors((event as CustomEvent).detail));
    dropFile(root, jpeg());
    await settle();
    const alert = root.querySelector(".error")!;
    expect(alert.hasAttribute("hidden")).toBe(false);
    expect(alert.textContent).toBe("Too many checks from your network. Try again in 9 seconds.");
    expect(errors).toHaveBeenCalledWith({
      code: "PUBLIC_CHECK_RATE_LIMITED",
      message: "Too many checks from your network. Try again in 9 seconds.",
    });
  });

  it("explains a refused MP4 with the types the page checks", async () => {
    const { element, root } = await mount(
      undefined,
      json(PAGE),
      json(
        {
          code: "PUBLIC_CHECK_MEDIA_UNSUPPORTED",
          message: "a public check does not run video/mp4; it accepts image/jpeg, image/png",
        },
        415,
      ),
    );
    const errors = vi.fn();
    element.addEventListener("op-verify-error", (event) => errors((event as CustomEvent).detail));
    dropFile(root, new File([new Uint8Array(16)], "clip.bin", { type: "" }));
    await settle();
    const expected =
      "MP4 video cannot be checked here, so nothing was checked. This page checks JPEG and PNG files.";
    expect(root.querySelector(".error")?.textContent).toBe(expected);
    expect(errors).toHaveBeenCalledWith({
      code: "PUBLIC_CHECK_MEDIA_UNSUPPORTED",
      message: expected,
    });
    expect(root.querySelector("article.card")).toBeNull();
  });

  it("refuses a video before uploading when the page checks no video", async () => {
    const page = { ...PAGE, accepted_media_types: ["image/jpeg", "image/png", "application/pdf"] };
    const { root } = await mount(undefined, json(page));
    const input = root.querySelector<HTMLInputElement>('input[type="file"]')!;
    expect(input.accept).toBe("image/jpeg,image/png,application/pdf");
    expect(root.querySelector(".limits")?.textContent).toContain(
      "Images and documents up to 25 MB",
    );
    dropFile(root, new File([new Uint8Array(16)], "clip.mp4", { type: "video/mp4" }));
    await settle();
    // Only the page configuration was fetched: nothing was sent, so nothing was billed.
    expect(fetchMock.calls).toHaveLength(1);
    expect(root.querySelector(".error")?.textContent).toBe(
      "MP4 video cannot be checked here, so nothing was checked. This page checks JPEG, PNG and PDF files.",
    );
  });

  it("says when the page has used its checks for the month", async () => {
    const { root } = await mount(
      undefined,
      json(PAGE),
      json({ code: "PUBLIC_CHECK_MONTHLY_LIMIT_REACHED", message: "x" }, 429, {
        "Retry-After": "86400",
      }),
    );
    dropFile(root, jpeg());
    await settle();
    expect(root.querySelector(".error")?.textContent).toBe(
      "This page has answered all the checks it offers this month. Checks resume next month.",
    );
  });

  it("keeps the picker disabled when the page does not exist", async () => {
    const { root, button } = await mount(
      undefined,
      json({ code: "VERIFY_PAGE_NOT_FOUND", message: "x" }, 404),
    );
    expect(button.disabled).toBe(true);
    expect(root.querySelector(".error")?.textContent).toBe(
      "This verify page does not exist or is turned off.",
    );
  });

  it("uses a configuration the host already fetched", async () => {
    fetchMock = mockFetch();
    vi.stubGlobal("fetch", fetchMock);
    const element = document.createElement("op-verify") as OpVerifyElement;
    element.setAttribute("page", "studio-nova");
    element.pageConfig = PAGE;
    document.body.append(element);
    await settle();
    expect(fetchMock.calls).toHaveLength(0);
    expect(element.shadowRoot!.querySelector("button.btn")!.hasAttribute("disabled")).toBe(false);
  });

  it("keeps a configuration set before the element was defined", async () => {
    fetchMock = mockFetch();
    vi.stubGlobal("fetch", fetchMock);
    const early = document.createElement("op-verify-later") as HTMLElement & {
      pageConfig?: unknown;
    };
    early.setAttribute("page", "studio-nova");
    early.pageConfig = PAGE;
    document.body.append(early);
    class Later extends OpVerifyElementClass {}
    customElements.define("op-verify-later", Later);
    await settle();
    expect(fetchMock.calls).toHaveLength(0);
    expect(early.shadowRoot!.querySelector("h2")!.textContent).toBe(
      "Check a file with Studio Nova",
    );
  });

  it("applies the owner's accent with a readable label, and only a readable ground", async () => {
    const lowContrast = {
      ...PAGE,
      colours: { accent: "#0F4C5C", background: "#FFFFFF", text: "#FAFAFA" },
    };
    const { element } = await mount(undefined, json(lowContrast));
    expect(element.style.getPropertyValue("--op-page-accent")).toBe("#0F4C5C");
    expect(element.style.getPropertyValue("--op-page-accent-fg")).toBe("#F5F9FC");
    expect(element.style.getPropertyValue("--op-page-background")).toBe("");
    const readable = await mount(undefined, json(PAGE));
    expect(readable.element.style.getPropertyValue("--op-page-background")).toBe("#F7F5F0");
  });

  it("styles light, dark, system and reduced-motion preferences", async () => {
    const { root } = await mount({ page: "studio-nova", theme: "dark" }, json(PAGE));
    const css = root.querySelector("style")!.textContent!;
    expect(css).toContain(':host([theme="dark"])');
    expect(css).toContain('@media (prefers-color-scheme:dark){:host(:not([theme="light"]))');
    expect(css).toContain("@media (prefers-reduced-motion:no-preference)");
    expect(css).toContain("--op-canvas:#0A1C28");
  });
});

const MEDIA_URL = "https://cdn.studio-nova.example/gallery/sunrise.jpg";
const CHECKS_URL = "https://api.originalpictures.com/v1/public/verify-pages/studio-nova/checks";

function media(bytes = 3, headers: Record<string, string> = {}): Response {
  return new Response(new Uint8Array(bytes).fill(0xff), {
    status: 200,
    headers: { "content-type": "image/jpeg", ...headers },
  });
}

function chipOf(root: ShadowRoot) {
  const chip = root.querySelector<HTMLButtonElement>("button.chip")!;
  return {
    chip,
    label: () => chip.querySelector(".chip-label")!.textContent,
    panel: () => root.getElementById(chip.getAttribute("aria-controls")!)!,
  };
}

describe("<op-verify src> inspect mode", () => {
  it("shows a collapsed chip and checks nothing until it is pressed", async () => {
    const { root } = await mount({ page: "studio-nova", src: MEDIA_URL });
    const { chip, label, panel } = chipOf(root);
    expect(chip.hidden).toBe(false);
    expect(chip.getAttribute("type")).toBe("button");
    expect(chip.getAttribute("aria-expanded")).toBe("false");
    expect(label()).toBe("Check Content Credentials");
    expect(panel().hidden).toBe(true);
    expect(root.querySelector<HTMLElement>(".head")!.hidden).toBe(true);
    // Billed to the page owner: no page view runs a check, or even loads the asset.
    expect(fetchMock.calls).toHaveLength(0);
  });

  it("loads the asset on press, checks it and expands into the card", async () => {
    const { element, root } = await mount(
      { page: "studio-nova", src: MEDIA_URL },
      json(PAGE),
      media(),
      json(completed()),
    );
    const seen = vi.fn();
    element.addEventListener("op-verify-result", (event) => seen((event as CustomEvent).detail));
    const { chip, label, panel } = chipOf(root);
    chip.focus();
    chip.click();
    await settle();
    expect(fetchMock.calls.map((call) => call.url)).toEqual([
      "https://api.originalpictures.com/v1/public/verify-pages/studio-nova",
      MEDIA_URL,
      CHECKS_URL,
    ]);
    expect(fetchMock.calls[1]?.init.mode).toBe("cors");
    const sent = (fetchMock.calls[2]?.init.body as FormData).get("file") as File;
    expect(sent.size).toBe(3);
    expect(sent.type).toBe("image/jpeg");
    expect(label()).toBe("Content Credentials");
    expect(chip.getAttribute("aria-expanded")).toBe("true");
    expect(panel().hidden).toBe(false);
    const card = root.querySelector("article.card")!;
    expect(card.querySelector(".pill")?.textContent).toBe("Content Credentials found");
    expect(card.querySelector(".statement")?.textContent).toBe(STATEMENT);
    expect(card.querySelector("button.secondary")).toBeNull();
    expect(root.activeElement).toBe(chip);
    expect(seen).toHaveBeenCalledWith({ result: completed() });
    const shown = root.querySelector(".root")!.textContent!.replace(STATEMENT, "");
    expect(shown).not.toMatch(VERDICT_WORDS);

    chip.click();
    expect(chip.getAttribute("aria-expanded")).toBe("false");
    expect(panel().hidden).toBe(true);
    chip.click();
    await settle();
    expect(chip.getAttribute("aria-expanded")).toBe("true");
    expect(fetchMock.calls).toHaveLength(3);
  });

  it("says when the asset carries no Content Credentials", async () => {
    const absent = completed({ content_credentials: { status: "absent", declared_origin: null } });
    const { root } = await mount(
      { page: "studio-nova", src: MEDIA_URL },
      json(PAGE),
      media(),
      json(absent),
    );
    chipOf(root).chip.click();
    await settle();
    expect(chipOf(root).label()).toBe("No Content Credentials found");
  });

  it("offers the file drop, and no answer, when CORS blocks the asset", async () => {
    const { element, root } = await mount(
      { page: "studio-nova", src: MEDIA_URL },
      json(PAGE),
      new TypeError("Failed to fetch"),
    );
    const errors = vi.fn();
    element.addEventListener("op-verify-error", (event) => errors((event as CustomEvent).detail));
    const { chip, label } = chipOf(root);
    chip.click();
    await settle();
    expect(fetchMock.calls).toHaveLength(2);
    expect(fetchMock.calls.some((call) => call.url === CHECKS_URL)).toBe(false);
    expect(label()).toBe("Content Credentials could not be checked");
    expect(chip.getAttribute("aria-expanded")).toBe("true");
    const note = root.querySelector<HTMLElement>(".note")!;
    expect(note.hidden).toBe(false);
    expect(note.textContent).toContain("Nothing was checked.");
    expect(note.textContent).toContain("drop it here");
    expect(root.querySelector<HTMLElement>(".drop")!.hidden).toBe(false);
    expect(root.querySelector<HTMLElement>(".error")!.hidden).toBe(true);
    expect(root.querySelector("article.card")).toBeNull();
    expect(root.querySelector(".root")!.textContent).not.toMatch(VERDICT_WORDS);
    expect(errors).toHaveBeenCalledWith(expect.objectContaining({ code: "SOURCE_UNREACHABLE" }));

    // The fallback path checks a dropped file and shows its card.
    fetchMock = mockFetch(json(completed()));
    vi.stubGlobal("fetch", fetchMock);
    dropFile(root, jpeg());
    await settle();
    expect(fetchMock.calls[0]?.url).toBe(CHECKS_URL);
    expect(root.querySelector("article.card .pill")?.textContent).toBe("Content Credentials found");
  });

  it("refuses an asset over the size limit before checking it", async () => {
    const { root } = await mount(
      { page: "studio-nova", src: MEDIA_URL },
      json(PAGE),
      media(3, { "Content-Length": String(30 * 1024 * 1024) }),
    );
    const { chip, label } = chipOf(root);
    chip.click();
    await settle();
    expect(fetchMock.calls).toHaveLength(2);
    expect(label()).toBe("Content Credentials could not be checked");
    expect(root.querySelector(".note")?.textContent).toContain(
      "This media is larger than 25 MB, more than a check accepts, so nothing was checked.",
    );
    expect(root.querySelector<HTMLElement>(".drop")!.hidden).toBe(false);
    expect(root.querySelector("article.card")).toBeNull();
  });

  it("stops reading an asset that grows past the page's limit without a length", async () => {
    const small = { ...PAGE, max_upload_bytes: 1024 };
    const { root } = await mount({ page: "studio-nova", src: MEDIA_URL }, json(small), media(4096));
    chipOf(root).chip.click();
    await settle();
    expect(fetchMock.calls).toHaveLength(2);
    expect(root.querySelector(".note")?.textContent).toContain("nothing was checked");
  });

  it("checks on connect with autocheck and stays collapsed", async () => {
    const { root } = await mount(
      { page: "studio-nova", src: MEDIA_URL, autocheck: "" },
      json(PAGE),
      media(),
      json(completed()),
    );
    const { chip, label, panel } = chipOf(root);
    expect(fetchMock.calls).toHaveLength(3);
    expect(label()).toBe("Content Credentials");
    expect(chip.getAttribute("aria-expanded")).toBe("false");
    expect(panel().hidden).toBe(true);
    chip.click();
    expect(chip.getAttribute("aria-expanded")).toBe("true");
    expect(fetchMock.calls).toHaveLength(3);
  });

  it("inspects the media element named by for", async () => {
    const image = document.createElement("img");
    image.id = "hero";
    image.setAttribute("src", MEDIA_URL);
    document.body.append(image);
    const { root } = await mount(
      { page: "studio-nova", for: "hero" },
      json(PAGE),
      media(),
      json(completed()),
    );
    chipOf(root).chip.click();
    await settle();
    expect(fetchMock.calls[1]?.url).toBe(MEDIA_URL);
    expect(chipOf(root).label()).toBe("Content Credentials");
  });

  it("checks nothing when the for element is missing", async () => {
    const { root } = await mount({ page: "studio-nova", for: "missing" }, json(PAGE));
    chipOf(root).chip.click();
    await settle();
    expect(fetchMock.calls).toHaveLength(1);
    expect(root.querySelector(".note")?.textContent).toContain(
      "There is no media here to check, so nothing was checked.",
    );
  });
});

describe("hidden parts", () => {
  it("are hidden even when a class gives them a display value", async () => {
    const { root } = await mount(undefined, json(PAGE));
    const sheet = root.querySelector("style")!.sheet!;
    const rule = [...sheet.cssRules].find(
      (candidate): candidate is CSSStyleRule =>
        candidate instanceof CSSStyleRule && candidate.selectorText === "[hidden]",
    );
    expect(rule).toBeDefined();
    expect(rule!.style.getPropertyValue("display")).toBe("none");
    expect(rule!.style.getPropertyPriority("display")).toBe("important");
    // `.chip` sets display:inline-flex; hidden, it must still not render.
    const chip = root.querySelector<HTMLElement>(".chip")!;
    expect(chip.hidden).toBe(true);
    expect(getComputedStyle(chip).display).toBe("none");
  });
});
