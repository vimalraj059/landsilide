from __future__ import annotations

from typing import Literal


Direction = Literal["en2ta", "ta2en"]


def translate(text: str, direction: Direction) -> str:
    """Placeholder translation function.
    In production, load HuggingFace models (e.g., ai4bharat/indictrans2-en-ta, ta-en).
    """
    if not text:
        return ""
    if direction == "en2ta":
        return "[TA] " + text
    else:
        return "[EN] " + text

