# Stateful platform design

Date: 2026-11-02. Supersedes the download-bundle model in `2026-10-07-platform-scaffold-design.md` for everything except the catalog.

## Decision

openacademy is a freemium product. Content (`content/`) and the agent plugin (`plugins/plato`) are open source and thin. The server (`src/`) is the product: it owns learner state, progress, streaks, next-rung selection, entitlements, and the dashboard. There is one server codebase and one Docker image; a local run is a faithful mirror of the hosted service, selected only by `DATABASE_URL` (SQLite locally, Postgres hosted). No local-only code paths, no markdown contract: the agent never reads rungs from disk or writes `progress.md`. All rung text and all state move through the HTTP API.

## Architecture

```
learner's agent ── MCP (plugins/plato) ──► server (src/)
                                              ├─ content/ loaded at start
                                              ├─ DATABASE_URL: sqlite | postgres
                                              └─ web: catalog, dashboard, connect-your-AI
```

## Data model

- `learners(id, token, plan, created_at)`; `plan ∈ {free, pro}`. Local runs create learners via `POST /api/v1/learners`; hosted puts signup in front of the same table.
- `enrollments(id, learner_id, field, subfield, course, created_at)`; unique per learner and course.
- `attempts(id, enrollment_id, flight_id, rung_id, commit, confidence 1–4, outcome ∈ {correct, wrong}, assisted bool, artifact_result nullable, created_at)`. One row per completed rung; the attempt is the unit of progress. Streak and next rung derive from attempts; nothing else is stored.

## API v1 (bearer token except where noted)

- `GET /api/v1/catalog` (public): fields → subfields → courses with `tier`.
- `POST /api/v1/learners` (public): creates a learner, returns `{token, plan}`.
- `POST /api/v1/enrollments` `{field, subfield, course}` → enrollment. 404 unknown course; 409 already enrolled.
- `GET /api/v1/enrollments` → enrollments with `completed`, `total`.
- `GET /api/v1/enrollments/{id}/next` → `{done: false, flight, rung: {id, title, kind, text}}` or `{done: true}`. The rung text is read from the course's rung file server-side. 402 if the course tier exceeds the learner plan.
- `POST /api/v1/enrollments/{id}/attempts` → attempt. 422 on unknown rung or confidence outside 1–4.
- `GET /api/v1/me` → `{plan, streak_weeks, enrollments: [...with next action]}`.

Streak: ISO weeks with at least one attempt count. Counting starts at the current week, or at the previous week if the current one is empty (the streak is alive until the week ends), and runs back over consecutive weeks. A gap resets to zero, per the user's decision.

Errors are JSON `{"detail": ...}`. Malformed content still fails at startup naming the file.

## Sequencing

1. This spec; data model, attempts API, streak, tiers; SQLite via SQLAlchemy; tests against a temp database. Legacy `/api/fields*` and the download endpoint stay until step 2.
2. `plugins/plato` becomes an MCP server over the API; `SKILL.md` rewritten to drive the tools; download page becomes "connect your AI". Legacy routes removed.
3. Dashboard in the web frontend.
4. Entitlement UI and hosted signup.

## Out of scope now

Payments, OAuth, Postgres migrations tooling, cohorts, analytics, agent clients without tool use.
