"""openacademy platform: serves the curated content catalog and course bundles."""

import io
import os
import zipfile
from pathlib import Path

import yaml
from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONTENT = REPO_ROOT / "content"
DEFAULT_PLUGIN = REPO_ROOT / "plugins" / "cognitive-sparring-partner"
STATIC_DIR = Path(__file__).resolve().parent / "static"

CourseKey = tuple[str, str, str]

BUNDLE_README = """# {title} (openacademy bundle)

`course/` holds the course package and `addon/` holds the Cognitive Sparring Partner protocol your agent runs.

1. Attach the addon to your agent: see `addon/README.md` for Claude Code, claude.ai, Cursor, Codex, Gemini, and ChatGPT.
2. Open your agent in this folder and say: "Start the course in ./course."
3. Later, say "Continue the course." Progress lives in `course/progress.md`, which your agent maintains.
"""


def _read_manifest(path: Path) -> dict:
    try:
        data = yaml.safe_load(path.read_text())
    except yaml.YAMLError as exc:
        raise ValueError(f"malformed manifest {path}: {exc}") from exc
    if not isinstance(data, dict) or "id" not in data or "title" not in data:
        raise ValueError(f"manifest {path} must be a mapping with id and title")
    return data


def load_catalog(content_dir: Path) -> tuple[list[dict], dict[CourseKey, Path]]:
    """Scan field.yaml, subfield.yaml, course.yaml; return the public catalog and a (field, subfield, course) -> dir index."""
    fields = []
    course_dirs: dict[CourseKey, Path] = {}
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
                subfield["courses"].append(course)
                course_dirs[(field["id"], subfield["id"], course["id"])] = course_manifest.parent
            field["subfields"].append(subfield)
        fields.append(field)
    return fields, course_dirs


def _add_tree(archive: zipfile.ZipFile, root: Path, prefix: str) -> None:
    for path in sorted(root.rglob("*")):
        if path.is_file():
            archive.write(path, f"{prefix}/{path.relative_to(root).as_posix()}")


def build_bundle(course: dict, course_dir: Path, plugin_dir: Path) -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("README.md", BUNDLE_README.format(title=course["title"]))
        _add_tree(archive, course_dir, "course")
        _add_tree(archive, plugin_dir, "addon")
    return buffer.getvalue()


def create_app(content_dir: Path, plugin_dir: Path) -> FastAPI:
    catalog, course_dirs = load_catalog(content_dir)
    courses = {
        (field["id"], subfield["id"], course["id"]): course
        for field in catalog
        for subfield in field["subfields"]
        for course in subfield["courses"]
    }
    app = FastAPI(title="openacademy")

    def find_course(field_id: str, subfield_id: str, course_id: str) -> dict:
        try:
            return courses[(field_id, subfield_id, course_id)]
        except KeyError:
            raise HTTPException(404, f"course not found: {field_id}/{subfield_id}/{course_id}")

    @app.get("/api/fields")
    def list_fields() -> list[dict]:
        return catalog

    @app.get("/api/fields/{field_id}/subfields/{subfield_id}/courses/{course_id}")
    def get_course(field_id: str, subfield_id: str, course_id: str) -> dict:
        return find_course(field_id, subfield_id, course_id)

    @app.get("/api/fields/{field_id}/subfields/{subfield_id}/courses/{course_id}/download")
    def download_course(field_id: str, subfield_id: str, course_id: str) -> Response:
        course = find_course(field_id, subfield_id, course_id)
        return Response(
            content=build_bundle(course, course_dirs[(field_id, subfield_id, course_id)], plugin_dir),
            media_type="application/zip",
            headers={"Content-Disposition": f'attachment; filename="{course_id}-openacademy.zip"'},
        )

    app.mount("/", StaticFiles(directory=STATIC_DIR, html=True), name="static")
    return app


app = create_app(
    Path(os.environ.get("OPENACADEMY_CONTENT", DEFAULT_CONTENT)),
    Path(os.environ.get("OPENACADEMY_PLUGIN", DEFAULT_PLUGIN)),
)
