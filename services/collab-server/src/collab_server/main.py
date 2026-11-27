from importlib.metadata import version

from fastapi import FastAPI
from shared_py import HealthResponse


def create_app() -> FastAPI:
    service = "collab-server"
    service_version = version(service)
    app = FastAPI(title=service, version=service_version)

    @app.get(
        "/api/v1/healthz", operation_id="getHealth", summary="Check service health"
    )
    async def healthz() -> HealthResponse:
        return HealthResponse(service=service, version=service_version)

    return app


app = create_app()
