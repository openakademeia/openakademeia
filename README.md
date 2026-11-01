# openacademy

A curated course library you attach your own AI to. The platform owns the content and its coherence; your agent, running the Mentor protocol, owns the conversation. Courses teach by making you commit to a prediction, breaking it, and introducing the concept as the repair.

## Run

```
docker compose up --build
```

Open http://localhost:8080, pick a field, a subfield, and a course, and download the bundle. It contains `course/` and `addon/`; `addon/README.md` explains how to attach the protocol to Claude Code, claude.ai, Cursor, Codex, Gemini, or ChatGPT. `content/` and the plugin are mounted into the container, so edits show up on refresh.

## Layout

- `content/<field>/field.yaml`, `<subfield>/subfield.yaml`, `<course>/course.yaml`: the catalog. A course directory holds `syllabus.md` and `rungs/*.md`; a course is flights of rungs, and each rung file has Concept, Commit, Truth, Repair, Exercises, and Twist sections. Subfields without courses are listed as planned.
- `plugins/mentor/`: the teaching protocol (`SKILL.md`) and attach instructions, shipped in every bundle as `addon/`.
- `src/`: FastAPI server (`app.py`), static frontend (`static/`), tests, Dockerfile.
- `docs/`: foundations, research notes, and design specs.

## Develop

```
cd src && pip install -r requirements-dev.txt && pytest
```

Tests run against the real `content/` and plugin directories, so they also validate the shipped content.

## Status

One field (Mathematics) with six subfields and one placeholder course (Algebra / Linear Algebra) whose rungs are lorem ipsum. Its proposed syllabus is `content/mathematics/algebra/linear-algebra/syllabus.md`. The protocol in `plugins/mentor/SKILL.md` reflects the current pedagogy design; see `docs/csp-foundations.md` and `docs/research/`.
