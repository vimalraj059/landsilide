from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel

from app.services.chat import orchestrator


router = APIRouter()


class ChatRequest(BaseModel):
    message: str
    user_id: Optional[str] = None


class ChatResponse(BaseModel):
    reply: str
    language: str


@router.get("/healthz")
async def healthz() -> dict:
    return {"status": "ok"}


@router.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest) -> ChatResponse:
    reply_text, lang = orchestrator.respond(req.message, user_id=req.user_id or "anon")
    return ChatResponse(reply=reply_text, language=lang)

