// @originalpictures/disclosure: importing this module defines <op-ai-notice>
// and <op-ai-label>.
import { defineAiLabel } from "./label.ts";
import { defineAiNotice } from "./notice.ts";

export * from "./core.ts";

defineAiNotice();
defineAiLabel();
