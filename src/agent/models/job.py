from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(frozen=True)
class Job:
    title: str
    company: str
    location: strd
    url: str
    source: str
    published_at: Optional[datetime] = None
    snippet: str = ""
