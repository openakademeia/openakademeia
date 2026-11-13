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
    assert len(course["chapters"]) == 15
    assert course["chapters"][0]["id"] == "01-arrows-and-columns"
    assert [lesson["kind"] for lesson in course["chapters"][0]["lessons"]] == ["confirm", "confirm", "break", "confirm", "unify"]
    assert course["chapters"][1]["lessons"] == []
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
    assert "openakademeia" in response.text


def test_frontend_points_agents_at_the_v1_catalog_and_mcp_plugin(client):
    script = client.get("/app.js").text

    assert "/api/v1/catalog" in script
    assert "/api/fields" not in script
    assert "openakademeia-plato" in script
    assert "openakademeia/philosophers" in script
    assert "plato@philosophers" in script
    assert "download" not in script.lower()
    assert "renderSetup" in script
    assert "function renderCourse(" in script
    assert "openakademeia-plato" not in script[script.index("function renderCourse(") : script.index("function renderNotFound")]


def test_header_links_to_the_setup_page(client):
    assert 'href="#/setup"' in client.get("/").text


def test_header_links_to_an_about_page_that_names_the_open_and_premium_split(client):
    script = client.get("/app.js").text
    about = script[script.index("function renderAbout(") : script.index("function renderCourse(")]

    assert 'href="#/about"' in client.get("/").text
    assert "open source" in about
    assert "premium tier" in about


READING_URL = "/api/v1/courses/mathematics/algebra/linear-algebra/reading"


def test_catalog_links_each_course_reading_without_carrying_its_text(client):
    fields = client.get("/api/v1/catalog").json()
    subfields = {subfield["id"]: subfield for subfield in fields[0]["subfields"]}

    assert subfields["algebra"]["courses"][0]["reading_url"] == READING_URL
    assert subfields["analysis"]["courses"][0]["reading_url"] is None
    assert "Vectors are displacements" not in client.get("/api/v1/catalog").text


def test_reading_returns_the_whole_course_text_without_auth(client):
    response = client.get(READING_URL)

    assert response.status_code == 200
    body = response.json()
    assert body["title"] == "Linear Algebra"
    assert "### Vectors are displacements {#vectors-are-displacements}" in body["text"]
    assert "### Systems are combinations {#systems-are-combinations}" in body["text"]


def test_course_without_a_reading_has_no_reading_route(client):
    assert client.get("/api/v1/courses/mathematics/analysis/pro-course/reading").status_code == 404
    assert client.get("/api/v1/courses/mathematics/algebra/topology/reading").status_code == 404


def test_course_page_links_the_reader(client):
    script = client.get("/app.js").text

    assert "reading_url" in script[script.index("function renderCourse(") : script.index("function renderNotFound")]
    assert "function renderReader(" in script


@pytest.mark.parametrize("path", ["/", "/app.js", "/style.css"])
def test_app_shell_is_revalidated_on_every_load(client, path):
    response = client.get(path)

    assert response.status_code == 200
    assert response.headers["cache-control"] == "no-cache"


def test_media_keeps_default_caching(client):
    response = client.get("/media/plato.png")

    assert response.status_code == 200
    assert "cache-control" not in response.headers
