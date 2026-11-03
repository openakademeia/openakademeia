"""Quality gates for every course in content/: lesson structure, reading links, and length limits from the teaching protocol."""

import re
from pathlib import Path

import pytest
import yaml

from app import lesson_sequence, load_catalog, reading_sections

CONTENT = Path(__file__).resolve().parents[2] / "content"
REQUIRED_SECTIONS = ["Commit", "Truth", "Repair", "Exercises", "Twist"]
ALLOWED_SECTIONS = {*REQUIRED_SECTIONS, "Artifact"}
REPAIR_MAX_WORDS = 150
READING_SECTION_MAX_WORDS = 450

COURSES = [
    (manifest.parent, yaml.safe_load(manifest.read_text())) for manifest in sorted(CONTENT.glob("*/*/*/course.yaml"))
]
LESSONS = [
    pytest.param(course_dir, lesson, id=f"{course['id']}/{lesson['id']}")
    for course_dir, course in COURSES
    for _, lesson in lesson_sequence(course)
]


def lesson_sections(text: str) -> dict[str, str]:
    parts = re.split(r"^## (.+)$", text, flags=re.M)
    return {title.strip(): body.strip() for title, body in zip(parts[1::2], parts[2::2])}


def words(text: str) -> int:
    return len(text.split())


def test_real_content_loads():
    load_catalog(CONTENT)


@pytest.mark.parametrize(("course_dir", "lesson"), LESSONS)
def test_lesson_has_the_protocol_sections_in_order(course_dir, lesson):
    sections = lesson_sections((course_dir / lesson["file"]).read_text())

    assert set(sections) <= ALLOWED_SECTIONS, "explanations belong in reading.md, not the lesson"
    assert [name for name in sections if name in REQUIRED_SECTIONS] == REQUIRED_SECTIONS


@pytest.mark.parametrize(("course_dir", "lesson"), LESSONS)
def test_lesson_commit_asks_for_a_confidence(course_dir, lesson):
    assert "confidence" in lesson_sections((course_dir / lesson["file"]).read_text())["Commit"]


@pytest.mark.parametrize(("course_dir", "lesson"), LESSONS)
def test_lesson_repair_stays_short(course_dir, lesson):
    assert words(lesson_sections((course_dir / lesson["file"]).read_text())["Repair"]) <= REPAIR_MAX_WORDS


@pytest.mark.parametrize(("course_dir", "lesson"), LESSONS)
def test_lesson_has_an_exercise_only_the_learner_can_answer(course_dir, lesson):
    assert "In your own words" in lesson_sections((course_dir / lesson["file"]).read_text())["Exercises"]


@pytest.mark.parametrize(("course_dir", "lesson"), LESSONS)
def test_lesson_points_at_a_reading_section(course_dir, lesson):
    assert lesson.get("reading") in reading_sections((course_dir / "reading.md").read_text())


@pytest.mark.parametrize(("course_dir", "course"), [pytest.param(d, c, id=c["id"]) for d, c in COURSES if (d / "reading.md").exists()])
def test_every_reading_section_is_used_and_readable(course_dir, course):
    sections = reading_sections((course_dir / "reading.md").read_text())
    used = {lesson.get("reading") for _, lesson in lesson_sequence(course)}

    assert set(sections) == used
    for section_id, text in sections.items():
        assert words(text) <= READING_SECTION_MAX_WORDS, section_id


def test_reading_sections_split_on_anchored_headings_only():
    text = "# Course\n\nIntro.\n\n## 1. Chapter\n\n### First {#first}\n\nOne.\n\n### Second {#second}\n\nTwo.\n\n---\n\nFooter.\n"

    assert reading_sections(text) == {"first": "### First\n\nOne.\n", "second": "### Second\n\nTwo.\n"}


def test_a_lesson_naming_a_missing_reading_section_fails_the_load(tmp_path):
    course = tmp_path / "f" / "s" / "c"
    course.mkdir(parents=True)
    (tmp_path / "f" / "field.yaml").write_text("id: f\ntitle: F\n")
    (tmp_path / "f" / "s" / "subfield.yaml").write_text("id: s\ntitle: S\n")
    (course / "course.yaml").write_text(
        "id: c\ntitle: C\nflights:\n  - id: one\n    title: One\n    lessons:\n"
        "      - {id: l, title: L, kind: confirm, file: l.md, reading: nowhere}\n"
    )
    (course / "reading.md").write_text("### Somewhere {#somewhere}\n\nText.\n")

    with pytest.raises(ValueError, match="nowhere"):
        load_catalog(tmp_path)
