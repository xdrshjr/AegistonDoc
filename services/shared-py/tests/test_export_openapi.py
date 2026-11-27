from shared_py.export_openapi import build_openapi_documents


def test_collab_openapi_exports_stream_and_sidecar_contracts() -> None:
    documents = build_openapi_documents()
    schemas = documents["collab"]["components"]["schemas"]

    assert {
        "HealthResponse",
        "TodoItem",
        "CollabAgentState",
        "InterruptPayload",
        "DocOp",
        "CanonicalParagraph",
        "DocxInspectRequest",
        "DocxInspectResponse",
        "DocxApplyOpsRequest",
        "DocxApplyOpsResponse",
        "DocxExportRequest",
        "DocxExportResponse",
    } <= schemas.keys()
    assert schemas["DocxApplyOpsRequest"]["properties"]["ops"]["items"] == {
        "$ref": "#/components/schemas/DocOp"
    }
    assert schemas["DocOp"]["discriminator"] == {
        "propertyName": "op",
        "mapping": {
            "replace_paragraph": "#/components/schemas/ReplaceParagraphOp",
            "insert_paragraph": "#/components/schemas/InsertParagraphOp",
            "delete_paragraph": "#/components/schemas/DeleteParagraphOp",
            "add_comment": "#/components/schemas/AddCommentOp",
        },
    }
    assert documents["kb"]["components"]["schemas"].keys() == {"HealthResponse"}
