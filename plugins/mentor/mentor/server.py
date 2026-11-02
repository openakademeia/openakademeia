"""Mentor MCP server: five tools over the openacademy API, with the teaching protocol as instructions."""

from pathlib import Path
from typing import Literal

from mcp.server.mcpserver import MCPServer

from mentor.client import MentorClient, connect

SKILL_PATH = Path(__file__).resolve().parent.parent / "SKILL.md"


def protocol_text() -> str:
    """SKILL.md without its frontmatter block."""
    text = SKILL_PATH.read_text()
    if text.startswith("---"):
        text = text.split("---", 2)[2]
    return text.lstrip()


def build_server(client: MentorClient | None = None) -> MCPServer:
    server = MCPServer("openacademy-mentor", instructions=protocol_text())
    state: dict[str, MentorClient | None] = {"client": client}

    def mentor() -> MentorClient:
        if state["client"] is None:
            state["client"] = connect()
        return state["client"]

    @server.tool(description="List every course in the openacademy catalog with its field, subfield, id, and tier.")
    def list_courses() -> list[dict]:
        return mentor().list_courses()

    @server.tool(description="Enroll the learner in a course, or resume it, and return the next rung with its full text.")
    def start_course(field: str, subfield: str, course: str) -> dict:
        return mentor().start_course(field, subfield, course)

    @server.tool(description="Return the next unfinished rung of an enrollment with its full text, or done: true.")
    def next_rung(enrollment_id: int) -> dict:
        return mentor().next_rung(enrollment_id)

    @server.tool(
        description="Record a finished rung: the learner's commit, confidence 1-4, outcome, whether the repair was given outright, and any artifact result line."
    )
    def record_attempt(
        enrollment_id: int,
        rung_id: str,
        commit: str,
        confidence: int,
        outcome: Literal["correct", "wrong"],
        assisted: bool = False,
        artifact_result: str | None = None,
    ) -> dict:
        return mentor().record_attempt(enrollment_id, rung_id, commit, confidence, outcome, assisted, artifact_result)

    @server.tool(description="The learner's plan, weekly streak, and progress in every enrollment.")
    def progress() -> dict:
        return mentor().progress()

    return server


def main() -> None:
    build_server().run()


if __name__ == "__main__":
    main()
