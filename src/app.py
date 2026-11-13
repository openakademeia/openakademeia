"""openakademeia server: catalog, learner state, progress, and the Plato API."""

import os
import re
import secrets
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Literal

import yaml
from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
    Text,
    UniqueConstraint,
    create_engine,
    inspect,
    insert,
    select,
    text as sql_text,
)
from sqlalchemy.engine import Engine

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONTENT = REPO_ROOT / "content"
DEFAULT_DATABASE_URL = f"sqlite:///{REPO_ROOT / '.openakademeia.db'}"
STATIC_DIR = Path(__file__).resolve().parent / "static"

CourseKey = tuple[str, str, str]

CONCEPT_HEADING = re.compile(r"^### (?P<title>.+?) \{#(?P<id>[a-z0-9-]+)\}$")

metadata = MetaData()

learners = Table(
    "learners",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("token", String(64), unique=True, nullable=False),
    Column("plan", String(16), nullable=False, default="free"),
    Column("created_at", DateTime, nullable=False),
)

enrollments = Table(
    "enrollments",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("learner_id", Integer, ForeignKey("learners.id"), nullable=False),
    Column("field", String(64), nullable=False),
    Column("subfield", String(64), nullable=False),
    Column("course", String(64), nullable=False),
    Column("created_at", DateTime, nullable=False),
    UniqueConstraint("learner_id", "field", "subfield", "course"),
)

attempts = Table(
    "attempts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("enrollment_id", Integer, ForeignKey("enrollments.id"), nullable=False),
    Column("chapter_id", String(64), nullable=False),
    Column("lesson_id", String(64), nullable=False),
    Column("commit", Text, nullable=False),
    Column("confidence", Integer, nullable=False),
    Column("outcome", String(16), nullable=False),
    Column("assisted", Boolean, nullable=False),
    Column("artifact_result", Text),
    Column("created_at", DateTime, nullable=False),
)

PLAN_RANK = {"free": 0, "pro": 1}


class EnrollIn(BaseModel):
    field: str
    subfield: str
    course: str


class AttemptIn(BaseModel):
    lesson_id: str
    commit: str
    confidence: int = Field(ge=1, le=4)
    outcome: Literal["correct", "wrong"]
    assisted: bool = False
    artifact_result: str | None = None


class ShellStaticFiles(StaticFiles):
    """Serves the app shell with no-cache so a redeploy shows up on the next load, not when the browser's heuristic expires."""

    REVALIDATE = (".html", ".js", ".css")

    def file_response(self, full_path, *args, **kwargs):
        response = super().file_response(full_path, *args, **kwargs)
        if str(full_path).endswith(self.REVALIDATE):
            response.headers["Cache-Control"] = "no-cache"
        return response


def _now() -> datetime:
    return datetime.now(timezone.utc).replace(tzinfo=None)


def _read_manifest(path: Path) -> dict:
    try:
        data = yaml.safe_load(path.read_text())
    except yaml.YAMLError as exc:
        raise ValueError(f"malformed manifest {path}: {exc}") from exc
    if not isinstance(data, dict) or "id" not in data or "title" not in data:
        raise ValueError(f"manifest {path} must be a mapping with id and title")
    return data


def reading_concepts(text: str) -> dict[str, str]:
    """Split a course reading into its `### Title {#id}` concepts; each runs to the next heading of level 1-3."""
    concepts: dict[str, list[str]] = {}
    current: list[str] | None = None
    for line in text.splitlines():
        heading = CONCEPT_HEADING.match(line)
        if heading:
            if heading["id"] in concepts:
                raise ValueError(f"duplicate reading concept {heading['id']}")
            current = concepts[heading["id"]] = [f"### {heading['title']}"]
        elif re.match(r"^#{1,3} ", line) or line.strip() == "---":
            current = None
        elif current is not None:
            current.append(line)
    return {concept_id: "\n".join(lines).strip() + "\n" for concept_id, lines in concepts.items()}


def _load_reading(course_dir: Path, course: dict) -> dict | None:
    """The course reading with its concepts, after checking every lesson points at a concept that exists."""
    path = course_dir / "reading.md"
    text = path.read_text() if path.exists() else None
    concepts = reading_concepts(text) if text else {}
    for _, lesson in lesson_sequence(course):
        if "reading" in lesson and lesson["reading"] not in concepts:
            raise ValueError(f"lesson {lesson['id']} names missing reading concept {lesson['reading']!r} in {course_dir}")
    return {"text": text, "concepts": concepts} if text else None


def load_catalog(content_dir: Path) -> tuple[list[dict], dict[CourseKey, Path], dict[CourseKey, dict]]:
    """Scan field.yaml, subfield.yaml, course.yaml; return the public catalog plus course-dir and reading indexes."""
    fields = []
    course_dirs: dict[CourseKey, Path] = {}
    readings: dict[CourseKey, dict] = {}
    for field_manifest in sorted(content_dir.glob("*/field.yaml")):
        field = _read_manifest(field_manifest)
        field["subfields"] = []
        for subfield_manifest in sorted(field_manifest.parent.glob("*/subfield.yaml")):
            subfield = _read_manifest(subfield_manifest)
            subfield["field"] = field["id"]
            subfield["courses"] = []
            for course_manifest in sorted(subfield_manifest.parent.glob("*/course.yaml")):
                course = _read_manifest(course_manifest)
                course["field"] = field["id"]
                course["subfield"] = subfield["id"]
                course.setdefault("tier", "free")
                syllabus = course_manifest.parent / "syllabus.md"
                course["syllabus"] = syllabus.read_text() if syllabus.exists() else None
                key = (field["id"], subfield["id"], course["id"])
                reading = _load_reading(course_manifest.parent, course)
                course["reading_url"] = "/api/v1/courses/{}/{}/{}/reading".format(*key) if reading else None
                if reading:
                    readings[key] = reading
                subfield["courses"].append(course)
                course_dirs[key] = course_manifest.parent
            field["subfields"].append(subfield)
        fields.append(field)
    return fields, course_dirs, readings


def lesson_sequence(course: dict) -> list[tuple[dict, dict]]:
    return [(chapter, lesson) for chapter in course.get("chapters", []) for lesson in chapter.get("lessons", [])]


def streak_weeks(days: list[date], today: date) -> int:
    """Consecutive ISO weeks with activity, counted back from this week, or from last week if this one is still empty."""
    active = {(d.isocalendar()[0], d.isocalendar()[1]) for d in days}
    year, week, _ = today.isocalendar()
    cursor = date.fromisocalendar(year, week, 1)
    if (year, week) not in active:
        cursor = date.fromordinal(cursor.toordinal() - 7)
    count = 0
    while (cursor.isocalendar()[0], cursor.isocalendar()[1]) in active:
        count += 1
        cursor = date.fromordinal(cursor.toordinal() - 7)
    return count


def _make_engine(database_url: str) -> Engine:
    connect_args = {"check_same_thread": False} if database_url.startswith("sqlite") else {}
    engine = create_engine(database_url, connect_args=connect_args)
    # Databases from before chapters were renamed from flights still have attempts.flight_id.
    if "attempts" in inspect(engine).get_table_names() and "flight_id" in {c["name"] for c in inspect(engine).get_columns("attempts")}:
        with engine.begin() as conn:
            conn.execute(sql_text("ALTER TABLE attempts RENAME COLUMN flight_id TO chapter_id"))
    metadata.create_all(engine)
    return engine


def create_app(content_dir: Path, database_url: str) -> FastAPI:
    catalog, course_dirs, readings = load_catalog(content_dir)
    courses = {
        (field["id"], subfield["id"], course["id"]): course
        for field in catalog
        for subfield in field["subfields"]
        for course in subfield["courses"]
    }
    engine = _make_engine(database_url)
    app = FastAPI(title="openakademeia")

    def find_course(field_id: str, subfield_id: str, course_id: str) -> dict:
        try:
            return courses[(field_id, subfield_id, course_id)]
        except KeyError:
            raise HTTPException(404, f"course not found: {field_id}/{subfield_id}/{course_id}")

    def current_learner(authorization: str = Header(default="")) -> dict:
        scheme, _, token = authorization.partition(" ")
        if scheme.lower() != "bearer" or not token:
            raise HTTPException(401, "bearer token required")
        with engine.connect() as conn:
            row = conn.execute(select(learners).where(learners.c.token == token)).mappings().first()
        if row is None:
            raise HTTPException(401, "unknown token")
        return dict(row)

    def own_enrollment(enrollment_id: int, learner: dict) -> dict:
        with engine.connect() as conn:
            row = (
                conn.execute(
                    select(enrollments).where(
                        enrollments.c.id == enrollment_id, enrollments.c.learner_id == learner["id"]
                    )
                )
                .mappings()
                .first()
            )
        if row is None:
            raise HTTPException(404, f"enrollment not found: {enrollment_id}")
        return dict(row)

    def completed_lessons(enrollment_id: int) -> set[str]:
        with engine.connect() as conn:
            rows = conn.execute(select(attempts.c.lesson_id).where(attempts.c.enrollment_id == enrollment_id)).all()
        return {row[0] for row in rows}

    def next_lesson(enrollment: dict) -> tuple[dict, dict] | None:
        course = courses[(enrollment["field"], enrollment["subfield"], enrollment["course"])]
        done = completed_lessons(enrollment["id"])
        return next(((chapter, lesson) for chapter, lesson in lesson_sequence(course) if lesson["id"] not in done), None)

    def enrollment_summary(enrollment: dict) -> dict:
        course = courses[(enrollment["field"], enrollment["subfield"], enrollment["course"])]
        upcoming = next_lesson(enrollment)
        return {
            "id": enrollment["id"],
            "field": enrollment["field"],
            "subfield": enrollment["subfield"],
            "course": enrollment["course"],
            "title": course["title"],
            "completed": len(completed_lessons(enrollment["id"])),
            "total": len(lesson_sequence(course)),
            "next_lesson": upcoming[1]["id"] if upcoming else None,
        }

    @app.get("/api/v1/catalog")
    def catalog_v1() -> list[dict]:
        return catalog

    @app.get("/api/v1/courses/{field_id}/{subfield_id}/{course_id}/reading")
    def reading(field_id: str, subfield_id: str, course_id: str) -> dict:
        """The whole course reading as markdown; public, since it holds explanations and no answer keys."""
        course = find_course(field_id, subfield_id, course_id)
        found = readings.get((field_id, subfield_id, course_id))
        if found is None:
            raise HTTPException(404, f"no reading for {field_id}/{subfield_id}/{course_id}")
        return {"title": course["title"], "text": found["text"]}

    @app.post("/api/v1/learners", status_code=201)
    def create_learner() -> dict:
        token = secrets.token_urlsafe(32)
        with engine.begin() as conn:
            conn.execute(insert(learners).values(token=token, plan="free", created_at=_now()))
        return {"token": token, "plan": "free"}

    @app.post("/api/v1/enrollments", status_code=201)
    def enroll(body: EnrollIn, learner: dict = Depends(current_learner)) -> dict:
        find_course(body.field, body.subfield, body.course)
        with engine.begin() as conn:
            existing = conn.execute(
                select(enrollments.c.id).where(
                    enrollments.c.learner_id == learner["id"],
                    enrollments.c.field == body.field,
                    enrollments.c.subfield == body.subfield,
                    enrollments.c.course == body.course,
                )
            ).first()
            if existing:
                raise HTTPException(409, f"already enrolled: {existing[0]}")
            result = conn.execute(
                insert(enrollments).values(
                    learner_id=learner["id"],
                    field=body.field,
                    subfield=body.subfield,
                    course=body.course,
                    created_at=_now(),
                )
            )
        return enrollment_summary(own_enrollment(result.inserted_primary_key[0], learner))

    @app.get("/api/v1/enrollments")
    def list_enrollments(learner: dict = Depends(current_learner)) -> list[dict]:
        with engine.connect() as conn:
            rows = conn.execute(select(enrollments).where(enrollments.c.learner_id == learner["id"])).mappings().all()
        return [enrollment_summary(dict(row)) for row in rows]

    @app.get("/api/v1/enrollments/{enrollment_id}/next")
    def get_next(enrollment_id: int, learner: dict = Depends(current_learner)) -> dict:
        enrollment = own_enrollment(enrollment_id, learner)
        course = courses[(enrollment["field"], enrollment["subfield"], enrollment["course"])]
        if PLAN_RANK[course["tier"]] > PLAN_RANK[learner["plan"]]:
            raise HTTPException(402, f"course tier {course['tier']} requires a {course['tier']} plan")
        upcoming = next_lesson(enrollment)
        if upcoming is None:
            return {"done": True}
        chapter, lesson = upcoming
        key = (enrollment["field"], enrollment["subfield"], enrollment["course"])
        course_dir = course_dirs[key]
        concepts = readings.get(key, {}).get("concepts", {})
        return {
            "done": False,
            "chapter": {"id": chapter["id"], "title": chapter["title"]},
            "lesson": {
                "id": lesson["id"],
                "title": lesson["title"],
                "kind": lesson["kind"],
                "text": (course_dir / lesson["file"]).read_text(),
                "reading": concepts.get(lesson.get("reading")),
            },
        }

    @app.post("/api/v1/enrollments/{enrollment_id}/attempts", status_code=201)
    def record_attempt(enrollment_id: int, body: AttemptIn, learner: dict = Depends(current_learner)) -> dict:
        enrollment = own_enrollment(enrollment_id, learner)
        course = courses[(enrollment["field"], enrollment["subfield"], enrollment["course"])]
        chapter_id = next((chapter["id"] for chapter, lesson in lesson_sequence(course) if lesson["id"] == body.lesson_id), None)
        if chapter_id is None:
            raise HTTPException(422, f"unknown lesson: {body.lesson_id}")
        values = {**body.model_dump(), "enrollment_id": enrollment_id, "chapter_id": chapter_id, "created_at": _now()}
        with engine.begin() as conn:
            result = conn.execute(insert(attempts).values(**values))
        return {"id": result.inserted_primary_key[0], **values, "created_at": values["created_at"].isoformat()}

    @app.get("/api/v1/me")
    def me(learner: dict = Depends(current_learner)) -> dict:
        with engine.connect() as conn:
            rows = conn.execute(select(enrollments).where(enrollments.c.learner_id == learner["id"])).mappings().all()
            days = conn.execute(
                select(attempts.c.created_at)
                .join(enrollments, attempts.c.enrollment_id == enrollments.c.id)
                .where(enrollments.c.learner_id == learner["id"])
            ).all()
        return {
            "plan": learner["plan"],
            "streak_weeks": streak_weeks([row[0].date() for row in days], _now().date()),
            "enrollments": [enrollment_summary(dict(row)) for row in rows],
        }

    app.mount("/", ShellStaticFiles(directory=STATIC_DIR, html=True), name="static")
    return app


app = create_app(
    Path(os.environ.get("OPENAKADEMEIA_CONTENT", DEFAULT_CONTENT)),
    os.environ.get("DATABASE_URL", DEFAULT_DATABASE_URL),
)
