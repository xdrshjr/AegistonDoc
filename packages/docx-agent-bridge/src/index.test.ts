import { DOCX_AGENT_BRIDGE_PACKAGE_NAME } from "@workspace/docx-agent-bridge"
import { expect, it } from "vitest"

it("exposes the bridge through its package entry point", () => {
  expect(DOCX_AGENT_BRIDGE_PACKAGE_NAME).toBe("@workspace/docx-agent-bridge")
})
