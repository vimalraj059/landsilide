from typing import Dict
import re


# Minimal heuristic transliteration map (Tanglish -> Tamil)
# This is not exhaustive; it handles common syllables for demo purposes.
_MAP: Dict[str, str] = {
    "aa": "ஆ",
    "a": "அ",
    "ee": "ஈ",
    "e": "எ",
    "ii": "ஈ",
    "i": "இ",
    "oo": "ஊ",
    "o": "ஒ",
    "uu": "ஊ",
    "u": "உ",
    "ka": "க",
    "nga": "ங",
    "ca": "ச",
    "ja": "ஜ",
    "tha": "த",
    "dha": "த",
    "pa": "ப",
    "ba": "ப",
    "ma": "ம",
    "ya": "ய",
    "ra": "ர",
    "la": "ல",
    "va": "வ",
    "sa": "ச",
    "ha": "ஹ",
    "na": "ந",
}


def transliterate_tanglish_to_tamil(text: str) -> str:
    s = text.lower()
    # Greedy longest-first replacement
    for latin, tamil in sorted(_MAP.items(), key=lambda x: -len(x[0])):
        s = re.sub(re.escape(latin), tamil, s)
    # Basic special cases
    s = s.replace("vanakkam", "வணக்கம்")
    s = s.replace("nandri", "நன்றி")
    return s

