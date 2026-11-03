# Plato

The openacademy teaching protocol as an MCP server. It is thin and open: five tools over the openacademy HTTP API (`list_courses`, `start_course`, `next_lesson`, `record_attempt`, `progress`) plus `skills/plato/SKILL.md`, which the server hands to your agent as its instructions. Course text and all progress stay on the openacademy server; nothing is written on your machine except a learner token in `~/.openacademy/<host>.token`.

## Configure

Environment: `OPENACADEMY_URL` (default `http://localhost:8080`), `OPENACADEMY_TOKEN` (optional; otherwise a free learner is created on first use and the token saved).

Run it with `uvx`, no install:

```
uvx --from "git+https://github.com/slow42/openacademy#subdirectory=plugins/plato" openacademy-plato
```

- **Claude Code**: `claude mcp add openacademy -e OPENACADEMY_URL=http://localhost:8080 -- uvx --from "git+https://github.com/slow42/openacademy#subdirectory=plugins/plato" openacademy-plato`
- **Cursor** (`.cursor/mcp.json`), **Codex** (`~/.codex/config.toml`), **Gemini CLI** (`~/.gemini/settings.json`): add a stdio server named `openacademy` with the same command, args, and env.
- **claude.ai, ChatGPT**: need a hosted openacademy URL over streamable HTTP; not available while the server is local-only.

Then say: "Start a course." The agent calls `progress`, then `list_courses` or `next_lesson`, and runs the lesson loop described in `skills/plato/SKILL.md`. On connect the server sends its icon and an ASCII banner, which the agent shows once per session.

## Develop

```
cd plugins/plato && pip install -e . pytest && pytest
```

Tests run the real server in-process on a temporary database.
