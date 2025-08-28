from __future__ import annotations

from dataclasses import dataclass
from typing import Optional
import wikipediaapi


wiki = wikipediaapi.Wikipedia(language="en", extract_format=wikipediaapi.ExtractFormat.WIKI)


@dataclass
class WikiResult:
    title: str
    summary: str
    url: str


def wikipedia_summary(query: str) -> Optional[WikiResult]:
    page = wiki.page(query)
    if not page.exists():
        return None
    summary = page.summary[0:800]
    return WikiResult(title=page.title, summary=summary, url=page.fullurl)

