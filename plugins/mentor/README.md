# Mentor addon

`SKILL.md` is the teaching protocol. It is plain markdown with a short frontmatter header, so it loads as a Claude skill and pastes unchanged into any other agent's instruction slot. The protocol expects a course folder containing `course.yaml` and `rungs/*.md`, which is what the openacademy download gives you.

## Attach it

- **Claude Code**: copy this folder to `.claude/skills/mentor/` in the project that holds `course/`, or to `~/.claude/skills/` for all projects.
- **claude.ai**: upload this folder as a custom skill, or paste the body of `SKILL.md` into a Project's custom instructions and add the course files to the Project.
- **Cursor**: save the body of `SKILL.md` as `.cursor/rules/mentor.mdc`.
- **Codex, Gemini CLI, and other AGENTS.md readers**: append the body of `SKILL.md` to `AGENTS.md` (or `GEMINI.md`).
- **ChatGPT, Gemini web**: paste the body of `SKILL.md` into a custom GPT or Gem's instructions and attach the course files.

## Start

Open your agent in the folder that contains `course/` and say: "Start the course in ./course." The agent creates `course/progress.md` and runs the first rung. To continue later, say "Continue the course."
