from __future__ import annotations

from io import BytesIO
from typing import Literal

from gtts import gTTS


Lang = Literal["ta", "en"]


def synthesize_tts(text: str, lang: Lang) -> bytes:
    if not text:
        return b""
    if lang not in {"ta", "en"}:
        lang = "en"
    tts = gTTS(text=text, lang=lang)
    buf = BytesIO()
    tts.write_to_fp(buf)
    return buf.getvalue()

