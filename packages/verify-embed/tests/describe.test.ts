import { describe, expect, it } from "vitest";
import {
  VerifyError,
  describeError,
  describeMediaTypes,
  describeResult,
  describeVerifyError,
  formatUtc,
} from "../src/core.ts";
import { describeLimits, refusedBeforeUpload } from "../src/describe.ts";
import type { CredentialsStatus } from "../src/types.ts";
import { STATEMENT, VERDICT_WORDS, completed } from "./fixtures.ts";

function allText(view: ReturnType<typeof describeResult>): string {
  return [
    view.credentials.headline,
    view.credentials.detail,
    ...view.origin.flatMap((row) => [row.label, row.value]),
    view.madeWith?.question ?? "",
    view.madeWith?.headline ?? "",
    view.madeWith?.detail ?? "",
  ].join(" \n");
}

describe("describeResult", () => {
  it("quotes the declared origin and the provider's record", () => {
    const view = describeResult(completed());
    expect(view.credentials).toMatchObject({
      tone: "success",
      headline: "Content Credentials found",
    });
    expect(view.origin).toEqual([
      { label: "Signed by", value: "Original Pictures" },
      { label: "Credentials written by", value: "Original Pictures" },
      { label: "Signed at", value: "2026-10-19 09:12 UTC" },
      {
        label: "Declared as AI-generated",
        value: "Yes, the signer declares it (trainedAlgorithmicMedia)",
      },
      { label: "Generating software", value: "Studio Nova Imagine 2" },
      { label: "Recorded actions", value: "created" },
    ]);
    expect(view.madeWith?.headline).toBe("Yes: Studio Nova's system has a record of this file");
    expect(view.madeWith?.detail).toBe("Its Content Credentials were signed for Studio Nova.");
    expect(view.statement).toBe(STATEMENT);
  });

  it.each<CredentialsStatus>(["valid", "valid_untrusted", "invalid", "absent"])(
    "never uses verdict words for status %s",
    (status) => {
      for (const answer of ["yes", "no_record"] as const) {
        const view = describeResult(
          completed({
            content_credentials: {
              status,
              declared_origin:
                status === "absent" ? null : completed().content_credentials!.declared_origin,
            },
            made_with: {
              answer,
              provider_name: "Studio Nova",
              method: answer === "yes" ? "watermark" : null,
              recovery_checked: false,
            },
          }),
        );
        expect(allText(view)).not.toMatch(VERDICT_WORDS);
      }
    },
  );

  it("says what no record does not mean, and when recovery was off", () => {
    const view = describeResult(
      completed({
        content_credentials: { status: "absent", declared_origin: null },
        made_with: {
          answer: "no_record",
          provider_name: "Studio Nova",
          method: null,
          recovery_checked: false,
        },
      }),
    );
    expect(view.origin).toEqual([]);
    expect(view.madeWith?.headline).toBe(
      "No record: Studio Nova's system has no record of this file",
    );
    expect(view.madeWith?.detail).toContain("does not mean it was made elsewhere");
    expect(view.madeWith?.detail).toContain("Watermark and fingerprint search is off");
  });

  it("names watermark and fingerprint evidence", () => {
    const made = (method: "watermark" | "fingerprint") =>
      describeResult(
        completed({
          made_with: { answer: "yes", provider_name: "Nova", method, recovery_checked: true },
        }),
      ).madeWith?.detail;
    expect(made("watermark")).toBe("Nova's invisible watermark was found in it.");
    expect(made("fingerprint")).toBe("It matches a fingerprint Nova stored when it was signed.");
  });

  it("explains a failed check without a verdict", () => {
    const view = describeResult(
      completed({
        state: "failed",
        content_credentials: null,
        made_with: null,
        failure_reason: "MEDIA_TYPE_UNSUPPORTED",
      }),
    );
    expect(view.credentials.headline).toBe("The check could not be completed");
    expect(view.credentials.detail).toBe("This file type or file cannot be checked.");
    expect(view.madeWith).toBeNull();
  });
});

describe("describeError and formatUtc", () => {
  it("turns reason codes into visitor sentences", () => {
    expect(describeError("PUBLIC_CHECK_RATE_LIMITED", 30)).toBe(
      "Too many checks from your network. Try again in 30 seconds.",
    );
    expect(describeError("MEDIA_COMPRESSED_SIZE_LIMIT")).toBe("This file is larger than 25 MB.");
    expect(describeError("VERIFY_PAGE_NOT_FOUND")).toContain("does not exist");
    expect(describeError("SOMETHING_NEW")).toBe("The check could not be completed. Try again.");
  });

  it("names a refused media type and what the page checks instead", () => {
    expect(
      describeError("PUBLIC_CHECK_MEDIA_UNSUPPORTED", null, {
        mediaType: "video/mp4",
        acceptedMediaTypes: ["image/jpeg", "image/png", "application/pdf"],
      }),
    ).toBe(
      "MP4 video cannot be checked here, so nothing was checked. This page checks JPEG, PNG and PDF files.",
    );
    expect(describeError("PUBLIC_CHECK_MEDIA_UNSUPPORTED")).toBe(
      "This kind of file cannot be checked here, so nothing was checked.",
    );
    expect(
      describeError("MEDIA_FORMAT_UNDETECTED", null, { acceptedMediaTypes: ["audio/mp4"] }),
    ).toBe("This file type or file cannot be checked. This page checks M4A files.");
    expect(describeMediaTypes(["image/jpeg", "image/x-new"])).toBe("JPEG and image/x-new");
  });

  it("reads the refused and accepted types from the API's own refusal", () => {
    const refusal = new VerifyError(
      "PUBLIC_CHECK_MEDIA_UNSUPPORTED",
      "a public check does not run video/mp4; it accepts image/jpeg, image/png, audio/wav",
      { status: 415 },
    );
    expect(describeVerifyError(refusal)).toBe(
      "MP4 video cannot be checked here, so nothing was checked. This page checks JPEG, PNG and WAV files.",
    );
    // The page's configuration wins over the message when the element has it.
    expect(describeVerifyError(refusal, ["application/pdf"])).toBe(
      "MP4 video cannot be checked here, so nothing was checked. This page checks PDF files.",
    );
  });

  it("says a page that has used its month resumes next month", () => {
    const text = describeError("PUBLIC_CHECK_MONTHLY_LIMIT_REACHED", 86_400);
    expect(text).toBe(
      "This page has answered all the checks it offers this month. Checks resume next month.",
    );
    expect(text).not.toMatch(VERDICT_WORDS);
  });

  it("refuses only a certain mismatch before uploading, and describes the limits", () => {
    const accepted = ["image/jpeg", "audio/wav", "application/pdf"];
    expect(refusedBeforeUpload("video/mp4", accepted)).toBe(true);
    expect(refusedBeforeUpload("video/mp4", null)).toBe(false);
    // Browsers spell some types differently; the API decides those from the bytes.
    expect(refusedBeforeUpload("image/jpg", accepted)).toBe(false);
    expect(refusedBeforeUpload("video/mp4", [...accepted, "video/mp4"])).toBe(false);
    expect(describeLimits(25 * 1024 * 1024, accepted)).toBe(
      "Images, audio and documents up to 25 MB. The file is used only for this check and is not stored.",
    );
    expect(describeLimits(25 * 1024 * 1024, null)).toContain("Images, video, audio and documents");
  });

  it("formats times in UTC whatever the visitor's zone", () => {
    expect(formatUtc("2026-10-19T23:59:59+02:00")).toBe("2026-10-19 21:59 UTC");
    expect(formatUtc("not a date")).toBe("not a date");
  });
});
