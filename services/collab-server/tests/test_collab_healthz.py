from collab_server.main import app
from httpx import ASGITransport, AsyncClient


async def test_collab_healthz() -> None:
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.get("/api/v1/healthz")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "collab-server",
        "version": app.version,
    }
