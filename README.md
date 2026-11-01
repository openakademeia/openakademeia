# openacademy

A curated course library you attach your own AI to. The platform owns the content and its coherence; your agent, running the Mentor protocol, owns the conversation. Courses teach by making you commit to a prediction, breaking it, and introducing the concept as the repair.

## Run

```
docker compose up --build
```

Open http://localhost:8080 and browse fields, subfields, and courses. The local server is the same image as the hosted one; `DATABASE_URL` selects SQLite (default, stored in `./data/`) or Postgres. `content/` and the plugin are mounted read-only, so edits show up on refresh.

Learner state lives on the server, never on the learner's machine. The Mentor API (`/api/v1`): `POST /learners` issues a bearer token; `POST /enrollments` enrolls in a course; `GET /enrollments/{id}/next` returns the next rung with its text (402 if the course tier exceeds the learner's plan); `POST /enrollments/{id}/attempts` records a commit, confidence, and outcome; `GET /me` reports plan, weekly streak, and progress. The download bundle under `/api/fields` is legacy and goes away when the Mentor plugin becomes an MCP client of this API.

## Layout

- `content/<field>/field.yaml`, `<subfield>/subfield.yaml`, `<course>/course.yaml`: the catalog. A course directory holds `syllabus.md` and `rungs/*.md`; a course is flights of rungs, and each rung file has Concept, Commit, Truth, Repair, Exercises, and Twist sections. Subfields without courses are listed as planned.
- `plugins/mentor/`: the teaching protocol (`SKILL.md`) and attach instructions. Open source and thin; becomes an MCP client of the server.
- `src/`: FastAPI server (`app.py`: catalog, learners, enrollments, attempts, streak), static frontend (`static/`), tests, Dockerfile.
- `docs/`: foundations, research notes, and design specs.

## Develop

```
cd src && pip install -r requirements-dev.txt && pytest
```

Tests run against the real `content/` plus a synthetic pro-tier course, on a temporary SQLite database.

## Status

One field (Mathematics) with six subfields and one placeholder course (Algebra / Linear Algebra) whose rungs are lorem ipsum. Its proposed syllabus is `content/mathematics/algebra/linear-algebra/syllabus.md`. The protocol in `plugins/mentor/SKILL.md` reflects the current pedagogy design but still assumes local files; `docs/superpowers/specs/2026-11-02-stateful-platform-design.md` is the plan that moves it onto the API. See also `docs/csp-foundations.md` and `docs/research/`.
