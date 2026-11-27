from httpx import ASGITransport, AsyncClient
from kb_server.main import app


async def test_kb_healthz() -> None:
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.get("/api/v1/healthz")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "kb-server",
        "version": app.version,
    }
