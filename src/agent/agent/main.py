from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

import yaml

from src.collectors.rss import collect_from_rss


def load_config() -> Dict[str, Any]:
    # Prefer user config.yaml, fallback to config.yaml.example
    root = Path(__file__).resolve().parents[2]
    cfg_path = root / "config.yaml"
    if not cfg_path.exists():
        cfg_path = root / "config.yaml.example"

    with cfg_path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main() -> None:
    cfg = load_config()

    rss_cfg = (cfg.get("sources", {}) or {}).get("rss", {}) or {}
    if not rss_cfg.get("enabled", False):
        print("RSS source disabled. Set sources.rss.enabled = true in config.")
        return

    feeds: List[Dict[str, str]] = rss_cfg.get("feeds", []) or []
    jobs = collect_from_rss(feeds)

    top_n = int((cfg.get("ranking", {}) or {}).get("top_n", 10))
    print(f"Collected {len(jobs)} jobs. Showing top {min(top_n, len(jobs))}:\n")

    for j in jobs[:top_n]:
        t = j.published_at.isoformat(sep=" ", timespec="minutes") if j.published_at else "N/A"
        print(f"- [{j.source}] {j.title} ({t})")
        print(f"  {j.url}\n")


if __name__ == "__main__":
    main()
