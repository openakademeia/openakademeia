import stat
import pytest

from mentor.client import MentorClient, MentorError

COURSE = ("mathematics", "algebra", "linear-algebra")


def test_first_use_signs_up_and_persists_the_token(http, token_path):
    mentor = MentorClient(http, token_path)

    progress = mentor.progress()

    assert progress["plan"] == "free"
    assert token_path.read_text().strip() == mentor.token
    assert MentorClient(http, token_path).token == mentor.token


def test_token_file_and_directory_are_private_to_the_user(http, token_path):
    MentorClient(http, token_path)

    assert stat.S_IMODE(token_path.stat().st_mode) == 0o600
    assert stat.S_IMODE(token_path.parent.stat().st_mode) == 0o700


def test_list_courses_flattens_the_catalog(mentor):
    courses = mentor.list_courses()

    assert {"field": "mathematics", "subfield": "algebra", "course": "linear-algebra", "title": "Linear Algebra", "tier": "free"} in [
        {k: c[k] for k in ("field", "subfield", "course", "title", "tier")} for c in courses
    ]


def test_start_course_enrolls_and_returns_the_first_rung(mentor):
    started = mentor.start_course(*COURSE)

    assert started["enrollment_id"] == 1
    assert started["done"] is False
    assert started["rung"]["id"] == "01-vectors-as-arrows"
    assert started["rung"]["text"].startswith("# Vectors as arrows")


def test_start_course_twice_resumes_the_same_enrollment(mentor):
    first = mentor.start_course(*COURSE)
    mentor.record_attempt(first["enrollment_id"], "01-vectors-as-arrows", "guess", 2, "wrong")

    resumed = mentor.start_course(*COURSE)

    assert resumed["enrollment_id"] == first["enrollment_id"]
    assert resumed["rung"]["id"] == "02-matrix-as-machine"


def test_record_attempt_then_next_rung_advances(mentor):
    enrollment_id = mentor.start_course(*COURSE)["enrollment_id"]

    attempt = mentor.record_attempt(enrollment_id, "01-vectors-as-arrows", "lands at (2,1)", 3, "correct", assisted=False)
    following = mentor.next_rung(enrollment_id)

    assert attempt["rung_id"] == "01-vectors-as-arrows"
    assert following["rung"]["id"] == "02-matrix-as-machine"


def test_progress_reports_streak_and_enrollments(mentor):
    enrollment_id = mentor.start_course(*COURSE)["enrollment_id"]
    mentor.record_attempt(enrollment_id, "01-vectors-as-arrows", "x", 1, "wrong")

    progress = mentor.progress()

    assert progress["streak_weeks"] == 1
    assert progress["enrollments"][0]["completed"] == 1


def test_server_errors_surface_as_mentor_errors(mentor):
    with pytest.raises(MentorError, match="course not found"):
        mentor.start_course("mathematics", "algebra", "topology")
