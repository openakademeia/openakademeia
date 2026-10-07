import io
import zipfile
from pathlib import Path

from fastapi.testclient import TestClient

from app import create_app

REPO = Path(__file__).resolve().parents[2]
LIBRARY = REPO / "library"
ADDON = REPO / "addon"


def test_catalog_lists_mathematics_realm_with_linear_algebra_course():
    client = TestClient(create_app(LIBRARY, ADDON))

    response = client.get("/api/realms")

    assert response.status_code == 200
    realms = response.json()
    assert [realm["id"] for realm in realms] == ["mathematics"]
    assert realms[0]["title"] == "Mathematics"
    assert [course["id"] for course in realms[0]["courses"]] == ["linear-algebra"]


def test_course_detail_returns_manifest_with_flights():
    client = TestClient(create_app(LIBRARY, ADDON))

    response = client.get("/api/realms/mathematics/courses/linear-algebra")

    assert response.status_code == 200
    course = response.json()
    assert course["title"] == "Linear Algebra"
    assert course["realm"] == "mathematics"
    assert [flight["id"] for flight in course["flights"]] == ["01-what-a-matrix-does"]
    assert len(course["flights"][0]["rungs"]) == 3


def test_download_bundle_contains_course_addon_and_readme():
    client = TestClient(create_app(LIBRARY, ADDON))

    response = client.get("/api/realms/mathematics/courses/linear-algebra/download")

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/zip"
    names = set(zipfile.ZipFile(io.BytesIO(response.content)).namelist())
    assert {
        "README.md",
        "course/course.yaml",
        "course/rungs/01-01-vectors-as-arrows.md",
        "addon/SKILL.md",
        "addon/README.md",
    } <= names


def test_download_bundle_is_named_after_the_course():
    client = TestClient(create_app(LIBRARY, ADDON))

    response = client.get("/api/realms/mathematics/courses/linear-algebra/download")

    assert response.headers["content-disposition"] == 'attachment; filename="linear-algebra-openacademy.zip"'


def test_unknown_course_returns_404_naming_the_course():
    client = TestClient(create_app(LIBRARY, ADDON))

    response = client.get("/api/realms/mathematics/courses/topology")

    assert response.status_code == 404
    assert response.json() == {"detail": "course not found: mathematics/topology"}


def test_root_serves_the_frontend_page():
    client = TestClient(create_app(LIBRARY, ADDON))

    response = client.get("/")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/html")
    assert "openacademy" in response.text
