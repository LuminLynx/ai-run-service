"""Test configuration."""
import pytest


@pytest.fixture
def api_client():
    """Fixture for API client."""
    from fastapi.testclient import TestClient

    from service.main import app

    return TestClient(app)
