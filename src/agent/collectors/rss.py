from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional

import feedparser

from src.models.job import Job


def _safe_get(entry: Any, key: str, default: str = "") -> str:
    val = getattr(entry, key, None)
    return str(val) if val is not None else default


def _parse_published(entry: Any) -> Optional[datetime]:
    t = getattr(entry, "published_parsed", None)
    if t is None:
        return None
    try:
        return datetime(*t[:6])
    except Exception:
        return None


def collect_from_rss(feeds: List[Dict[str, str]]) -> List[Job]:
    jobs: List[Job] = []

    for feed in feeds:
        name = feed.get("name", "rss")
        url = feed["url"]

        parsed = feedparser.parse(url)
        for e in parsed.entries:
            title = _safe_get(e, "title", "").strip()
            link = _safe_get(e, "link", "").strip()

            snippet = _safe_get(e, "summary", "").strip()
            if len(snippet) > 200:
                snippet = snippet[:200] + "..."

            jobs.append(
                Job(
                    title=title or "Untitled",
                    company="",
                    location="",
                    url=link,
                    source=name,
                    published_at=_parse_published(e),
                    snippet=snippet,
                )
            )

    return jobs
