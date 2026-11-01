import io
import zipfile

COURSE_URL = "/api/fields/mathematics/subfields/algebra/courses/linear-algebra"


def test_catalog_lists_mathematics_field_with_subfields_and_linear_algebra_course(client):
    response = client.get("/api/fields")

    assert response.status_code == 200
    fields = response.json()
    assert [field["id"] for field in fields] == ["mathematics"]
    assert fields[0]["title"] == "Mathematics"
    subfields = {subfield["id"]: subfield for subfield in fields[0]["subfields"]}
    assert set(subfields) == {
        "foundations",
        "algebra",
        "analysis",
        "geometry",
        "discrete",
        "probability-and-statistics",
    }
    assert [course["id"] for course in subfields["algebra"]["courses"]] == ["linear-algebra"]
    assert [course["id"] for course in subfields["analysis"]["courses"]] == ["pro-course"]


def test_course_detail_returns_manifest_with_flights_and_location(client):
    response = client.get(COURSE_URL)

    assert response.status_code == 200
    course = response.json()
    assert course["title"] == "Linear Algebra"
    assert course["field"] == "mathematics"
    assert course["subfield"] == "algebra"
    assert [flight["id"] for flight in course["flights"]] == ["01-what-a-matrix-does"]
    assert len(course["flights"][0]["rungs"]) == 3


def test_download_bundle_contains_course_syllabus_plugin_and_readme(client):
    response = client.get(f"{COURSE_URL}/download")

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/zip"
    names = set(zipfile.ZipFile(io.BytesIO(response.content)).namelist())
    assert {
        "README.md",
        "course/course.yaml",
        "course/syllabus.md",
        "course/rungs/01-01-vectors-as-arrows.md",
        "addon/SKILL.md",
        "addon/README.md",
    } <= names


def test_download_bundle_is_named_after_the_course(client):
    response = client.get(f"{COURSE_URL}/download")

    assert response.headers["content-disposition"] == 'attachment; filename="linear-algebra-openacademy.zip"'


def test_unknown_course_returns_404_naming_the_full_path(client):
    response = client.get("/api/fields/mathematics/subfields/geometry/courses/topology")

    assert response.status_code == 404
    assert response.json() == {"detail": "course not found: mathematics/geometry/topology"}


def test_root_serves_the_frontend_page(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/html")
    assert "openacademy" in response.text
