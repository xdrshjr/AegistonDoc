import json
from importlib import import_module
from pathlib import Path
from typing import Any

from pydantic.json_schema import models_json_schema

from .schemas import (
    CanonicalParagraph,
    CollabAgentState,
    DocxApplyOpsRequest,
    DocxApplyOpsResponse,
    DocxExportRequest,
    DocxExportResponse,
    DocxInspectRequest,
    DocxInspectResponse,
    InterruptPayload,
)

COLLAB_CONTRACTS = (
    CollabAgentState,
    InterruptPayload,
    CanonicalParagraph,
    DocxInspectRequest,
    DocxInspectResponse,
    DocxApplyOpsRequest,  # Includes the named DocOp union and its variants.
    DocxApplyOpsResponse,
    DocxExportRequest,
    DocxExportResponse,
)


def build_openapi_documents() -> dict[str, dict[str, Any]]:
    collab_app = import_module("collab_server.main").create_app()
    kb_app = import_module("kb_server.main").create_app()
    collab_openapi = collab_app.openapi()

    _, schemas = models_json_schema(
        [(model, "validation") for model in COLLAB_CONTRACTS],
        ref_template="#/components/schemas/{model}",
    )
    collab_openapi.setdefault("components", {}).setdefault("schemas", {}).update(
        schemas["$defs"]
    )
    return {"collab": collab_openapi, "kb": kb_app.openapi()}


def main() -> None:
    workspace = Path(__file__).resolve().parents[4]
    output_dir = workspace / "packages" / "api-client" / "openapi"
    output_dir.mkdir(parents=True, exist_ok=True)
    for name, document in build_openapi_documents().items():
        content = json.dumps(document, ensure_ascii=False, indent=2, sort_keys=True)
        (output_dir / f"{name}.json").write_text(
            f"{content}\n", encoding="utf-8", newline="\n"
        )
