import asyncio

import pytest
from httpx import AsyncClient
from app.main import app


@pytest.mark.asyncio
async def test_healthz():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        res = await ac.get("/healthz")
        assert res.status_code == 200
        payload = res.json()
        assert payload["status"] == "ok"


@pytest.mark.asyncio
async def test_chat_basic():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        res = await ac.post("/chat", json={"message": "Vanakkam"})
        assert res.status_code == 200
        data = res.json()
        assert isinstance(data["reply"], str)
        assert data["language"] in {"ta", "en", "mix", "unknown"}

