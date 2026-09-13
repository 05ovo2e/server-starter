"""pytest 설정 및 픽스처."""

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    """TestClient 픽스처."""
    return TestClient(app)
