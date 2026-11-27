from typing import Annotated, Literal

from pydantic import BaseModel, Field


class ReplaceParagraphOp(BaseModel):
    op: Literal["replace_paragraph"]
    op_id: str
    para_id: str
    text: str


class InsertParagraphOp(BaseModel):
    """Insert a paragraph before or after the anchor identified by para_id."""

    op: Literal["insert_paragraph"]
    op_id: str
    para_id: str
    position: Literal["before", "after"]
    text: str


class DeleteParagraphOp(BaseModel):
    op: Literal["delete_paragraph"]
    op_id: str
    para_id: str


class AddCommentOp(BaseModel):
    """Attach a comment to the paragraph identified by para_id."""

    op: Literal["add_comment"]
    op_id: str
    para_id: str
    text: str


type DocOp = Annotated[
    ReplaceParagraphOp | InsertParagraphOp | DeleteParagraphOp | AddCommentOp,
    Field(discriminator="op"),
]


class CanonicalParagraph(BaseModel):
    para_id: str
    text: str
    style_id: str | None = None


class DocxInspectRequest(BaseModel):
    docx_base64: str


class DocxInspectResponse(BaseModel):
    paragraphs: list[CanonicalParagraph]


class DocxApplyOpsRequest(BaseModel):
    docx_base64: str
    ops: list[DocOp]


class DocxApplyOpsResponse(BaseModel):
    docx_base64: str
    applied_op_ids: list[str]


class DocxExportRequest(BaseModel):
    docx_base64: str


class DocxExportResponse(BaseModel):
    docx_base64: str
