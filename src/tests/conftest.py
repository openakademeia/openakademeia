import shutil
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app import create_app

REPO = Path(__file__).resolve().parents[2]
CONTENT = REPO / "content"

PRO_COURSE = """id: pro-course
title: Pro Course
summary: Paid placeholder.
tier: pro
flights:
  - id: 01-only
    title: Only flight
    lessons:
      - id: 01-only-lesson
        title: Only lesson
        kind: confirm
        file: lessons/01-only-lesson.md
"""


@pytest.fixture
def content_dir(tmp_path):
    """Real content plus one pro-tier course under mathematics/analysis."""
    target = tmp_path / "content"
    shutil.copytree(CONTENT, target)
    course = target / "mathematics" / "analysis" / "pro-course"
    (course / "lessons").mkdir(parents=True)
    (course / "course.yaml").write_text(PRO_COURSE)
    (course / "lessons" / "01-only-lesson.md").write_text("# Only lesson\n\nPaid text.\n")
    return target


@pytest.fixture
def client(content_dir, tmp_path):
    return TestClient(create_app(content_dir, f"sqlite:///{tmp_path / 'test.db'}"))


@pytest.fixture
def auth(client):
    token = client.post("/api/v1/learners").json()["token"]
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def enrollment_id(client, auth):
    response = client.post(
        "/api/v1/enrollments",
        json={"field": "mathematics", "subfield": "algebra", "course": "linear-algebra"},
        headers=auth,
    )
    assert response.status_code == 201
    return response.json()["id"]
