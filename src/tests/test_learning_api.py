from datetime import date

from app import streak_weeks

ENROLL = {"field": "mathematics", "subfield": "algebra", "course": "linear-algebra"}
ATTEMPT = {"rung_id": "01-two-numbers-one-arrow", "commit": "it lands at (2, 1)", "confidence": 3, "outcome": "correct", "assisted": False}


def test_catalog_v1_exposes_course_tier(client):
    response = client.get("/api/v1/catalog")

    assert response.status_code == 200
    courses = {c["id"]: c for f in response.json() for s in f["subfields"] for c in s["courses"]}
    assert courses["linear-algebra"]["tier"] == "free"
    assert courses["pro-course"]["tier"] == "pro"


def test_creating_a_learner_returns_a_free_plan_token(client):
    response = client.post("/api/v1/learners")

    assert response.status_code == 201
    body = response.json()
    assert body["plan"] == "free"
    assert len(body["token"]) >= 32


def test_learner_routes_require_a_valid_token(client):
    assert client.get("/api/v1/enrollments").status_code == 401
    assert client.get("/api/v1/enrollments", headers={"Authorization": "Bearer nope"}).status_code == 401


def test_enrolling_twice_in_the_same_course_conflicts(client, auth, enrollment_id):
    response = client.post("/api/v1/enrollments", json=ENROLL, headers=auth)

    assert response.status_code == 409


def test_enrolling_in_an_unknown_course_is_404(client, auth):
    response = client.post("/api/v1/enrollments", json={**ENROLL, "course": "topology"}, headers=auth)

    assert response.status_code == 404
    assert response.json() == {"detail": "course not found: mathematics/algebra/topology"}


def test_next_returns_the_first_rung_with_its_text(client, auth, enrollment_id):
    response = client.get(f"/api/v1/enrollments/{enrollment_id}/next", headers=auth)

    assert response.status_code == 200
    body = response.json()
    assert body["done"] is False
    assert body["flight"]["id"] == "01-arrows-and-columns"
    assert body["rung"]["id"] == "01-two-numbers-one-arrow"
    assert body["rung"]["kind"] == "confirm"
    assert body["rung"]["text"].startswith("# Two numbers, one arrow")


def test_recording_an_attempt_advances_to_the_next_rung(client, auth, enrollment_id):
    created = client.post(f"/api/v1/enrollments/{enrollment_id}/attempts", json=ATTEMPT, headers=auth)

    assert created.status_code == 201
    assert created.json()["rung_id"] == "01-two-numbers-one-arrow"
    following = client.get(f"/api/v1/enrollments/{enrollment_id}/next", headers=auth).json()
    assert following["rung"]["id"] == "02-tip-to-tail"


def test_completing_every_rung_marks_the_enrollment_done(client, auth, enrollment_id):
    for rung_id in ["01-two-numbers-one-arrow", "02-tip-to-tail", "03-reaching-every-point", "04-when-arrows-agree", "05-two-views-one-thing"]:
        client.post(f"/api/v1/enrollments/{enrollment_id}/attempts", json={**ATTEMPT, "rung_id": rung_id}, headers=auth)

    assert client.get(f"/api/v1/enrollments/{enrollment_id}/next", headers=auth).json() == {"done": True}
    listed = client.get("/api/v1/enrollments", headers=auth).json()
    assert [(e["course"], e["completed"], e["total"]) for e in listed] == [("linear-algebra", 5, 5)]


def test_attempt_rejects_unknown_rung_and_bad_confidence(client, auth, enrollment_id):
    url = f"/api/v1/enrollments/{enrollment_id}/attempts"

    assert client.post(url, json={**ATTEMPT, "rung_id": "nope"}, headers=auth).status_code == 422
    assert client.post(url, json={**ATTEMPT, "confidence": 5}, headers=auth).status_code == 422


def test_enrollment_of_another_learner_is_invisible(client, auth, enrollment_id):
    other = {"Authorization": f"Bearer {client.post('/api/v1/learners').json()['token']}"}

    assert client.get(f"/api/v1/enrollments/{enrollment_id}/next", headers=other).status_code == 404


def test_free_learner_cannot_fetch_a_pro_rung(client, auth):
    enrolled = client.post("/api/v1/enrollments", json={**ENROLL, "subfield": "analysis", "course": "pro-course"}, headers=auth)
    assert enrolled.status_code == 201

    response = client.get(f"/api/v1/enrollments/{enrolled.json()['id']}/next", headers=auth)

    assert response.status_code == 402
    assert response.json() == {"detail": "course tier pro requires a pro plan"}


def test_me_reports_streak_and_next_action(client, auth, enrollment_id):
    before = client.get("/api/v1/me", headers=auth).json()
    assert before["plan"] == "free"
    assert before["streak_weeks"] == 0

    client.post(f"/api/v1/enrollments/{enrollment_id}/attempts", json=ATTEMPT, headers=auth)

    after = client.get("/api/v1/me", headers=auth).json()
    assert after["streak_weeks"] == 1
    assert after["enrollments"][0]["next_rung"] == "02-tip-to-tail"


def test_streak_counts_consecutive_iso_weeks_and_resets_on_a_gap():
    today = date(2026, 11, 2)  # Monday of ISO week 45

    assert streak_weeks([], today) == 0
    assert streak_weeks([date(2026, 11, 2)], today) == 1
    assert streak_weeks([date(2026, 10, 29), date(2026, 10, 21)], today) == 2  # weeks 44 and 43; current week empty but alive
    assert streak_weeks([date(2026, 10, 21)], today) == 0  # week 43 only; week 44 missed
    assert streak_weeks([date(2026, 11, 2), date(2026, 10, 29), date(2026, 10, 15)], today) == 2
