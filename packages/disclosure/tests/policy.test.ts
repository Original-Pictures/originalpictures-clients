import { readFileSync } from "node:fs";
import { join } from "node:path";
import { describe, expect, it } from "vitest";
import {
  BUNDLED_POLICY,
  JURISDICTION_IDS,
  detectJurisdiction,
  parseAcceptLanguage,
  pickText,
  resolve,
  resolveAll,
  type ResolveOptions,
} from "../src/core.ts";

interface Vector {
  name: string;
  options: Record<string, string | null>;
  expect: Record<string, string | null> | null;
}
const { vectors } = JSON.parse(
  readFileSync(join(process.cwd(), "tests/fixtures/resolution-vectors.json"), "utf8"),
) as { vectors: Vector[] };

function toOptions(raw: Vector["options"]): ResolveOptions {
  const map: Record<string, keyof ResolveOptions> = {
    jurisdiction: "jurisdiction",
    locale: "locale",
    region: "region",
    accept_language: "acceptLanguage",
    time_zone: "timeZone",
    kind: "kind",
    rule_id: "ruleId",
    fallback: "fallback",
  };
  return Object.fromEntries(
    Object.entries(raw).map(([key, value]) => [map[key] ?? key, value]),
  ) as ResolveOptions;
}

describe("resolve: shared vectors", () => {
  it.each(vectors.map((vector) => [vector.name, vector] as const))("%s", (_name, vector) => {
    const resolved = resolve(toOptions(vector.options));
    if (vector.expect === null) {
      expect(resolved).toBeNull();
      return;
    }
    expect(resolved).not.toBeNull();
    const actual: Record<string, unknown> = {
      jurisdiction: resolved!.jurisdiction.id,
      basis: resolved!.detectedBy,
      rule_id: resolved!.rule.id,
      locale: resolved!.locale,
      text: resolved!.text,
      timing: resolved!.timing,
      badge_set: resolved!.badgeSet,
    };
    for (const [key, value] of Object.entries(vector.expect)) expect(actual[key], key).toBe(value);
    expect(resolved!.needsLegalReview).toBe(true);
    expect(resolved!.policyVersion).toBe("2026-10-19.2");
  });
});

describe("policy engine", () => {
  it("bundles the nine jurisdictions in contract order", () => {
    expect(BUNDLED_POLICY.schema_version).toBe("op.disclosure-policy.2026-10.v1");
    expect(BUNDLED_POLICY.jurisdictions.map((j) => j.id)).toEqual([...JURISDICTION_IDS]);
  });

  it("resolves every rule in the document, each with its citation and review flag", () => {
    for (const jurisdiction of BUNDLED_POLICY.jurisdictions) {
      for (const rule of jurisdiction.rules) {
        const resolved = resolve({ jurisdiction: jurisdiction.id, ruleId: rule.id });
        expect(resolved?.rule.id).toBe(rule.id);
        expect(resolved?.instrument.citation).toBeTruthy();
        expect(resolved?.rule.provision).toBeTruthy();
        expect(resolved?.needsLegalReview).toBe(true);
        expect(resolved?.disclaimer).toContain("does not by itself satisfy any law");
      }
    }
  });

  it("lists all rules of a kind", () => {
    expect(resolveAll({ jurisdiction: "CN", kind: "visible_label" }).map((r) => r.rule.id)).toEqual(
      ["cn.labeling.explicit-label", "cn.labeling.platform-label"],
    );
  });

  it("refuses an unknown explicit jurisdiction", () => {
    expect(() => resolve({ jurisdiction: "US-TX" as never })).toThrow(RangeError);
  });

  it("uses a newer document passed in", () => {
    const newer = structuredClone(BUNDLED_POLICY);
    newer.policy_version = "2026-11-01.1";
    expect(resolve({ jurisdiction: "EU", policy: newer })?.policyVersion).toBe("2026-11-01.1");
  });
});

describe("hints", () => {
  it("orders Accept-Language by quality and drops wildcards and q=0", () => {
    expect(parseAcceptLanguage("da, en-GB;q=0.8, en;q=0.7, *;q=0.5, fr;q=0")).toEqual([
      "da",
      "en-GB",
      "en",
    ]);
    expect(parseAcceptLanguage(undefined)).toEqual([]);
  });

  it("maps whole-jurisdiction time zones only", () => {
    expect(detectJurisdiction({ timeZone: "Europe/Berlin" })).toEqual({
      id: "EU",
      basis: "timezone",
    });
    expect(detectJurisdiction({ timeZone: "Asia/Kolkata" })).toEqual({
      id: "IN",
      basis: "timezone",
    });
    expect(detectJurisdiction({ timeZone: "America/Los_Angeles" })).toBeNull();
    expect(detectJurisdiction({ timeZone: "Europe/London" })).toBeNull();
    expect(detectJurisdiction({ timeZone: "Asia/Hong_Kong" })).toBeNull();
  });

  it("does not read a country into an ambiguous bare language", () => {
    expect(detectJurisdiction({ acceptLanguage: "zh" })).toBeNull();
    expect(detectJurisdiction({ acceptLanguage: "de" })).toBeNull();
    expect(detectJurisdiction({ acceptLanguage: "zh-TW" })).toBeNull();
    expect(detectJurisdiction({ acceptLanguage: "ko" })).toEqual({ id: "KR", basis: "language" });
  });

  it("picks the closest text locale, then English", () => {
    const texts = [
      { locale: "en", text: "A" },
      { locale: "zh-CN", text: "B" },
    ];
    expect(pickText(texts, ["zh-Hans-CN"])?.locale).toBe("zh-CN");
    expect(pickText(texts, ["sv"])?.locale).toBe("en");
    expect(pickText([], ["en"])).toBeNull();
  });
});
