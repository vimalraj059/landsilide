import re
import unicodedata
from typing import Literal


LanguageCode = Literal["ta", "en", "mix", "unknown"]


TAMIL_RANGE = re.compile(r"[\u0B80-\u0BFF]")
EN_RANGE = re.compile(r"[A-Za-z]")


def normalize_text(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = text.strip()
    # Collapse whitespace
    text = re.sub(r"\s+", " ", text)
    return text


def detect_language(text: str) -> LanguageCode:
    """Detect Tamil/English/mixed based on Unicode script presence.

    - Returns "mix" if both Tamil and English are present
    - Returns "ta" if Tamil only
    - Returns "en" if English only
    - "unknown" otherwise
    """
    if not text:
        return "unknown"
    has_tamil = bool(TAMIL_RANGE.search(text))
    has_english = bool(EN_RANGE.search(text))
    if has_tamil and has_english:
        return "mix"
    if has_tamil:
        return "ta"
    if has_english:
        return "en"
    return "unknown"

