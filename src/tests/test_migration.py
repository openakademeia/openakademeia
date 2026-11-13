import sqlite3

from app import create_app
from conftest import CONTENT


def attempt_columns(path) -> set[str]:
    with sqlite3.connect(path) as conn:
        return {row[1] for row in conn.execute("PRAGMA table_info(attempts)")}


def test_a_database_with_flight_id_is_renamed_to_chapter_id(tmp_path):
    path = tmp_path / "db.sqlite"
    create_app(CONTENT, f"sqlite:///{path}")
    with sqlite3.connect(path) as conn:
        conn.execute("ALTER TABLE attempts RENAME COLUMN chapter_id TO flight_id")

    create_app(CONTENT, f"sqlite:///{path}")

    assert "chapter_id" in attempt_columns(path)
    assert "flight_id" not in attempt_columns(path)
