import pytest
from httpx import ASGITransport, AsyncClient

from app.main import app


@pytest.mark.asyncio
async def test_create_user_endpoint_validation():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        resp = await client.post("/v1/users", json={"name": "", "email": "bad", "role_id": 1})
        assert resp.status_code in (400, 422)
