from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Literal, Optional

from app.nlp.detect import detect_language


Intent = Literal[
    "greeting",
    "farewell",
    "translate_en2ta",
    "translate_ta2en",
    "math",
    "wikipedia",
    "culture",
    "smalltalk",
]


@dataclass
class IntentResult:
    intent: Intent
    language: str
    query: str


GREETING_WORDS = {"vanakkam", "hello", "hi", "hey", "வணக்கம்"}
FAREWELL_WORDS = {"bye", "goodbye", "tata", "போறேன்", "நன்றி"}


def classify_intent(text: str) -> IntentResult:
    normalized = text.strip()
    lang = detect_language(normalized)
    lower = normalized.lower()

    # Greetings
    if any(word in lower for word in GREETING_WORDS):
        return IntentResult(intent="greeting", language=lang, query=normalized)

    if any(word in lower for word in FAREWELL_WORDS):
        return IntentResult(intent="farewell", language=lang, query=normalized)

    # Translation triggers
    if lower.startswith("translate to tamil:"):
        return IntentResult(intent="translate_en2ta", language=lang, query=lower.split(":", 1)[1].strip())
    if lower.startswith("translate to english:"):
        return IntentResult(intent="translate_ta2en", language=lang, query=lower.split(":", 1)[1].strip())

    # Math heuristic
    if re.fullmatch(r"[\d\s+\-*/().^]+", lower):
        return IntentResult(intent="math", language=lang, query=normalized)

    # Wikipedia heuristic
    if lower.startswith("wiki ") or lower.startswith("wikipedia "):
        q = normalized.split(" ", 1)[1].strip()
        return IntentResult(intent="wikipedia", language=lang, query=q)

    # Cultural content
    if any(k in lower for k in ["proverb", "quote", "பழமொழி", "கவிதை"]):
        return IntentResult(intent="culture", language=lang, query=normalized)

    # Fallback smalltalk
    return IntentResult(intent="smalltalk", language=lang, query=normalized)

