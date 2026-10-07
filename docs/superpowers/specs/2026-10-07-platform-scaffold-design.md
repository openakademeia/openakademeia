# Platform scaffold: curated library + bring-your-own-AI

## Goal

A local-first learning platform where a curious person browses curated content, picks a course, and downloads it together with a teaching protocol their own AI agent runs. The platform owns content and coherence; the learner's agent owns the conversation. This iteration is the thinnest end-to-end slice: one realm (Mathematics), one placeholder course (Linear Algebra), one addon, one Docker container.

## Architecture

Three top-level directories, each with one job:

- `addon/`: the Cognitive Sparring Partner protocol as `SKILL.md` (Claude skill format, which is plain markdown with frontmatter, so it also pastes into Cursor rules, AGENTS.md, Gems, or custom GPTs) plus a `README.md` with per-agent attach steps. Agent-agnostic by construction: no tool calls assumed, artifacts optional.
- `library/<realm>/realm.yaml` and `library/<realm>/<course>/course.yaml`: the content catalog. A course lists flights; a flight lists rungs; each rung is one markdown file under `rungs/` with sections Concept, Commit, Truth, Repair, Exercises, Twist. The addon reads this format.
- `platform/`: FastAPI app (`app.py`) exposing `GET /api/realms`, `GET /api/realms/{realm}/courses/{course}`, and `GET /api/realms/{realm}/courses/{course}/download` (zip with `course/`, `addon/`, and a root `README.md`), and serving `static/` at `/`. `create_app(library_dir, addon_dir)` is the factory; `app` is the module-level instance for uvicorn.

Docker: `platform/Dockerfile` on `python:3.12-slim`; root `docker-compose.yml` mounts `./library` and `./addon` read-only into `/data` and publishes port 8080.

## Data flow

Startup scans the library directory for `realm.yaml` files, then `course.yaml` under each realm. The frontend fetches the catalog, routes by URL hash, and links the download endpoint. The download endpoint zips the course directory and the addon directory on request; nothing is cached or precomputed.

## Error handling

Unknown realm or course returns 404 with a JSON detail. A malformed manifest fails at startup with the file path in the error rather than silently dropping the course.

## Testing

pytest with FastAPI's TestClient against the real `library/` and `addon/` directories, so the tests also validate the shipped content package. Docker verified by building, running, and curling the three endpoints.

## Out of scope

Accounts, server-side progress, search, more realms, real Linear Algebra content, the interactive artifact kit, and any pedagogy decisions still open in the brainstorm.
