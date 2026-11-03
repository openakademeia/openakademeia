import pytest

LEGACY_URLS = [
    "/api/fields",
    "/api/fields/mathematics/subfields/algebra/courses/linear-algebra",
    "/api/fields/mathematics/subfields/algebra/courses/linear-algebra/download",
]


def test_catalog_lists_mathematics_field_with_subfields_and_courses(client):
    response = client.get("/api/v1/catalog")

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
    course = subfields["algebra"]["courses"][0]
    assert course["id"] == "linear-algebra"
    assert len(course["flights"]) == 15
    assert course["flights"][0]["id"] == "01-arrows-and-columns"
    assert [lesson["kind"] for lesson in course["flights"][0]["lessons"]] == ["confirm", "confirm", "break", "confirm", "unify"]
    assert course["flights"][1]["lessons"] == []
    assert [course["id"] for course in subfields["analysis"]["courses"]] == ["pro-course"]


def test_catalog_carries_each_course_syllabus_when_one_exists(client):
    fields = client.get("/api/v1/catalog").json()
    subfields = {subfield["id"]: subfield for subfield in fields[0]["subfields"]}

    assert "## Chapters" in subfields["algebra"]["courses"][0]["syllabus"]
    assert subfields["analysis"]["courses"][0]["syllabus"] is None


def test_catalog_never_includes_lesson_text(client):
    body = client.get("/api/v1/catalog").text

    assert "Lorem" not in body
    assert "skewed grid" not in body
    assert '"text"' not in body


@pytest.mark.parametrize("url", LEGACY_URLS)
def test_legacy_catalog_and_download_routes_are_gone(client, url):
    assert client.get(url).status_code == 404


def test_root_serves_the_frontend_page(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/html")
    assert "openacademy" in response.text


def test_frontend_points_agents_at_the_v1_catalog_and_mcp_plugin(client):
    script = client.get("/app.js").text

    assert "/api/v1/catalog" in script
    assert "/api/fields" not in script
    assert "openacademy-mentor" in script
    assert "download" not in script.lower()
    assert "renderSetup" in script
    assert "function renderCourse(" in script
    assert "openacademy-mentor" not in script[script.index("function renderCourse(") : script.index("function renderNotFound")]


def test_header_links_to_the_setup_page(client):
    assert 'href="#/setup"' in client.get("/").text
