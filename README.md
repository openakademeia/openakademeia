# openacademy

A curated course library you attach your own AI to. The platform owns the content and its coherence; your agent, running the Cognitive Sparring Partner protocol, owns the conversation. Courses teach by making you commit to a prediction, breaking it, and introducing the concept as the repair.

## Run

```
docker compose up --build
```

Open http://localhost:8080, pick a realm and a course, and download the bundle. It contains `course/` and `addon/`; `addon/README.md` explains how to attach the protocol to Claude Code, claude.ai, Cursor, Codex, Gemini, or ChatGPT. The library and addon directories are mounted into the container, so content edits show up on refresh.

## Layout

- `addon/`: the teaching protocol (`SKILL.md`) and attach instructions.
- `library/<realm>/realm.yaml`, `library/<realm>/<course>/course.yaml`, `rungs/*.md`: the catalog. A course is flights of rungs; each rung file has Concept, Commit, Truth, Repair, Exercises, and Twist sections.
- `platform/`: FastAPI server (`app.py`), static frontend (`static/`), tests, Dockerfile.
- `docs/`: foundations, research notes, and design specs.

## Develop

```
cd platform && pip install -r requirements-dev.txt && pytest
```

Tests run against the real `library/` and `addon/` directories, so they also validate the shipped content.

## Status

One realm (Mathematics) and one placeholder course (Linear Algebra) with lorem ipsum rungs. The protocol in `addon/SKILL.md` reflects the current pedagogy design; see `docs/csp-foundations.md` and `docs/research/`.
