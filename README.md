# openakademeia

A curated course library you attach your own AI to. The platform owns the content and its coherence; your agent, running the Plato protocol, owns the conversation. Courses teach by making you commit to a prediction, breaking it, and introducing the concept as the repair.

## Run

```
docker compose up --build
```

Open http://localhost:8080 and browse fields, subfields, and courses. The local server is the same image as the hosted one; `DATABASE_URL` selects SQLite (default, stored in `./data/`) or Postgres. `content/` is mounted read-only, so edits show up on refresh.

Learner state lives on the server, never on the learner's machine. The Plato API (`/api/v1`): `POST /learners` issues a bearer token; `POST /enrollments` enrolls in a course; `GET /enrollments/{id}/next` returns the next lesson with its text and its section of the course book (402 if the course tier exceeds the learner's plan); `POST /enrollments/{id}/attempts` records a commit, confidence, and outcome; `GET /me` reports plan, weekly streak, and progress. `GET /catalog` and `GET /courses/{field}/{subfield}/{course}/reading` (the whole book) are public; everything else needs the bearer token.

## Connect your AI

Plato, the teaching agent, lives in [openakademeia/philosophers](https://github.com/openakademeia/philosophers) as a plugin (MCP server + skill). In Claude Code:

```
/plugin marketplace add openakademeia/philosophers
/plugin install plato@philosophers
```

Then say "Start the course mathematics/algebra/linear-algebra." Plato talks to `OPENAKADEMEIA_URL` (default `http://localhost:8080`, the local server), signs up on first use, and stores its token in `~/.openakademeia/`. The site's setup page (`#/setup`) and the philosophers README cover Codex, Cursor, and plain MCP config.

## Layout

- `content/<field>/field.yaml`, `<subfield>/subfield.yaml`, `<course>/course.yaml`: the catalog. A course directory holds `syllabus.md`, `reading.md` (the course book, one `### Title {#id}` section per lesson, public on the site), and `lessons/*.md`; a course is flights of lessons, each lesson names its book section with `reading:` in `course.yaml`, and each lesson file has Commit, Truth, Repair, Exercises, and Twist sections. `src/tests/test_content.py` enforces that structure. Subfields without courses are listed as planned.
- `src/`: FastAPI server (`app.py`: catalog, learners, enrollments, attempts, streak), static frontend (`static/`), tests, Dockerfile.
- `docs/`: foundations, research notes, and design specs.

## Develop

```
cd src && pip install -r requirements-dev.txt && pytest
```

Server tests run against the real `content/` plus a synthetic pro-tier course, on a temporary SQLite database. Plato's client tests run in the philosophers repo against this server in-process; they expect this checkout next to it (or `OPENAKADEMEIA_REPO`).

## Status

One field (Mathematics) with six subfields and one course, Algebra / Linear Algebra: syllabus approved, chapter 1 (five lessons) written, chapters 2 to 14 and the epilogue listed as planned flights. Syllabus: `content/mathematics/algebra/linear-algebra/syllabus.md`. Plato drives the API end to end; `docs/superpowers/specs/2026-11-02-stateful-platform-design.md` tracks what is left (dashboard, entitlement UI, hosted signup). See also `docs/csp-foundations.md` and `docs/research/`.
