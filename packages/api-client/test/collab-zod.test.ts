import { zCollabAgentState, zDocOp } from "@workspace/api-client/collab/zod"
import { describe, expect, it } from "vitest"

describe("generated CollabAgentState schema", () => {
  it("accepts the current document and todo progress", () => {
    const state = {
      active_doc_id: "doc-1",
      outline_confirmed: true,
      todos: [{ id: "todo-1", title: "Draft the introduction", status: "in_progress" }],
    }

    expect(zCollabAgentState.parse(state)).toEqual(state)
  })

  it("rejects an unknown todo status", () => {
    const state = {
      todos: [{ id: "todo-1", title: "Draft the introduction", status: "done" }],
    }

    expect(zCollabAgentState.safeParse(state).success).toBe(false)
  })
})

describe("generated DocOp schema", () => {
  const target = { op_id: "op-1", para_id: "para-1" }

  it.each([
    { ...target, op: "replace_paragraph", text: "Revised text" },
    { ...target, op: "insert_paragraph", position: "after", text: "New paragraph" },
    { ...target, op: "delete_paragraph" },
    { ...target, op: "add_comment", text: "Cite a source" },
  ])("accepts $op", (operation) => {
    expect(zDocOp.parse(operation)).toEqual(operation)
  })

  it("rejects unknown operations and missing variant fields", () => {
    expect(zDocOp.safeParse({ ...target, op: "rename_document" }).success).toBe(false)
    expect(zDocOp.safeParse({ ...target, op: "replace_paragraph" }).success).toBe(false)
    expect(
      zDocOp.safeParse({ ...target, op: "insert_paragraph", position: "over", text: "Text" })
        .success,
    ).toBe(false)
  })
})
