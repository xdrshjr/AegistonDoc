from typing import Literal

from pydantic import BaseModel, Field


class TodoItem(BaseModel):
    id: str
    title: str
    status: Literal["pending", "in_progress", "completed", "cancelled"]


class CollabAgentState(BaseModel):
    todos: list[TodoItem] = Field(default_factory=list)
    active_doc_id: str | None = None
    outline_confirmed: bool = False


class InterruptPayload(BaseModel):
    kind: Literal["outline_confirm", "section_review", "tool_approval"]
    title: str
    summary: str
    outline_markdown: str | None = None
    options: list[str] = Field(default_factory=list)
