# AI Job Match Agent

A configurable, engineering-grade AI agent that collects job posts, deduplicates them, ranks them against a resume, and sends a daily top-N digest.

## Roadmap (high level)
- Day 1: scaffold + config templates + logging plan
- Day 2: collectors interface + one data source
- Day 3: storage (SQLite) + dedup
- Day 4: explainable LLM scoring card (structured JSON output)
- Day 5: embedding pre-filter + caching
- Day 6: multi-channel notifications (email + telegram)
- Day 7: tests + CI + docs polish

## Disclaimer
Built from scratch. Inspired by common job-digest agent patterns, with no code copied from other repositories.
