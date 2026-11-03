import asyncio

from mentor.server import build_server


def test_server_exposes_the_mentor_tools_and_the_protocol_as_instructions():
    server = build_server()

    names = {tool.name for tool in asyncio.run(server.list_tools())}

    assert names == {"list_courses", "start_course", "next_lesson", "record_attempt", "progress"}
    assert server.instructions.startswith("# Mentor")
