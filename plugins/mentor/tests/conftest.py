from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app import create_app
from mentor.client import MentorClient

REPO = Path(__file__).resolve().parents[3]


@pytest.fixture
def http(tmp_path):
    """The real server, in-process, on a throwaway database."""
    app = create_app(REPO / "content", f"sqlite:///{tmp_path / 'db.sqlite'}")
    return TestClient(app)


@pytest.fixture
def token_path(tmp_path):
    return tmp_path / "token"


@pytest.fixture
def mentor(http, token_path):
    return MentorClient(http, token_path)
