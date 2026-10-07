"""openacademy platform: serves the curated library catalog and course bundles."""

import io
import os
import zipfile
from pathlib import Path

import yaml
from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_LIBRARY = REPO_ROOT / "library"
DEFAULT_ADDON = REPO_ROOT / "addon"
STATIC_DIR = Path(__file__).resolve().parent / "static"

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


def load_catalog(library_dir: Path) -> tuple[list[dict], dict[tuple[str, str], Path]]:
    """Scan realm.yaml and course.yaml files; return the public catalog and a (realm, course) -> dir index."""
    realms = []
    course_dirs: dict[tuple[str, str], Path] = {}
    for realm_manifest in sorted(library_dir.glob("*/realm.yaml")):
        realm = _read_manifest(realm_manifest)
        realm["courses"] = []
        for course_manifest in sorted(realm_manifest.parent.glob("*/course.yaml")):
            course = _read_manifest(course_manifest)
            course["realm"] = realm["id"]
            realm["courses"].append(course)
            course_dirs[(realm["id"], course["id"])] = course_manifest.parent
        realms.append(realm)
    return sorted(realms, key=lambda r: r["id"]), course_dirs


def _add_tree(archive: zipfile.ZipFile, root: Path, prefix: str) -> None:
    for path in sorted(root.rglob("*")):
        if path.is_file():
            archive.write(path, f"{prefix}/{path.relative_to(root).as_posix()}")


def build_bundle(course: dict, course_dir: Path, addon_dir: Path) -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("README.md", BUNDLE_README.format(title=course["title"]))
        _add_tree(archive, course_dir, "course")
        _add_tree(archive, addon_dir, "addon")
    return buffer.getvalue()


def create_app(library_dir: Path, addon_dir: Path) -> FastAPI:
    catalog, course_dirs = load_catalog(library_dir)
    courses = {
        (realm["id"], course["id"]): course for realm in catalog for course in realm["courses"]
    }
    app = FastAPI(title="openacademy")

    def find_course(realm_id: str, course_id: str) -> dict:
        try:
            return courses[(realm_id, course_id)]
        except KeyError:
            raise HTTPException(404, f"course not found: {realm_id}/{course_id}")

    @app.get("/api/realms")
    def list_realms() -> list[dict]:
        return catalog

    @app.get("/api/realms/{realm_id}/courses/{course_id}")
    def get_course(realm_id: str, course_id: str) -> dict:
        return find_course(realm_id, course_id)

    @app.get("/api/realms/{realm_id}/courses/{course_id}/download")
    def download_course(realm_id: str, course_id: str) -> Response:
        course = find_course(realm_id, course_id)
        return Response(
            content=build_bundle(course, course_dirs[(realm_id, course_id)], addon_dir),
            media_type="application/zip",
            headers={"Content-Disposition": f'attachment; filename="{course_id}-openacademy.zip"'},
        )

    app.mount("/", StaticFiles(directory=STATIC_DIR, html=True), name="static")
    return app


app = create_app(
    Path(os.environ.get("OPENACADEMY_LIBRARY", DEFAULT_LIBRARY)),
    Path(os.environ.get("OPENACADEMY_ADDON", DEFAULT_ADDON)),
)
