from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

from app.services.intent import classify_intent
from app.services.math import solve_expression
from app.services.knowledge import wikipedia_summary
from app.services.culture import random_proverb, random_quote
from app.services.translate import translate


@dataclass
class ChatTurn:
    user: str
    bot: str


class ChatSession:
    def __init__(self) -> None:
        self.history: list[ChatTurn] = []

    def add(self, user_text: str, bot_text: str) -> None:
        self.history.append(ChatTurn(user=user_text, bot=bot_text))


class ChatOrchestrator:
    def __init__(self) -> None:
        self.sessions: Dict[str, ChatSession] = {}

    def get_session(self, user_id: str) -> ChatSession:
        if user_id not in self.sessions:
            self.sessions[user_id] = ChatSession()
        return self.sessions[user_id]

    def respond(self, message: str, user_id: str = "anon") -> tuple[str, str]:
        intent_res = classify_intent(message)
        intent = intent_res.intent
        lang = intent_res.language
        session = self.get_session(user_id)

        if intent == "greeting":
            reply = "வணக்கம்! Hello! How can I help you today?"
        elif intent == "farewell":
            reply = "நன்றி! Goodbye! See you soon."
        elif intent == "math":
            value = solve_expression(intent_res.query)
            reply = f"Answer: {value}" if value is not None else "Sorry, I could not solve that."
        elif intent == "wikipedia":
            res = wikipedia_summary(intent_res.query)
            if res:
                reply = f"{res.title}: {res.summary} (More: {res.url})"
            else:
                reply = "No Wikipedia page found."
        elif intent == "culture":
            reply = f"{random_proverb()} | {random_quote()}"
        elif intent == "translate_en2ta":
            reply = translate(intent_res.query, direction="en2ta")
        elif intent == "translate_ta2en":
            reply = translate(intent_res.query, direction="ta2en")
        else:
            reply = "நான் உதவ தயாராக இருக்கிறேன்! Ask me anything."

        session.add(message, reply)
        return reply, lang


orchestrator = ChatOrchestrator()

