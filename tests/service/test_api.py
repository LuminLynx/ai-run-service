"""Tests for service API routes."""
from fastapi.testclient import TestClient


def test_health_check(api_client: TestClient) -> None:
    """Test health check endpoint."""
    response = api_client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["version"] == "0.1.0"
    assert "timestamp" in data
    assert "agent_enabled" in data


def test_root_endpoint(api_client: TestClient) -> None:
    """Test root endpoint."""
    response = api_client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "AI Run Service API"
    assert data["version"] == "0.1.0"
    assert data["docs"] == "/docs"


def test_create_task(api_client: TestClient) -> None:
    """Test creating a task."""
    task_data = {
        "description": "Test task",
        "repository_url": "https://github.com/test/repo",
        "branch": "main",
    }
    response = api_client.post("/tasks", json=task_data)
    assert response.status_code == 201
    data = response.json()
    assert "task_id" in data
    assert data["status"] == "pending"
    assert data["description"] == "Test task"


def test_get_task(api_client: TestClient) -> None:
    """Test getting a task."""
    # Create a task first
    task_data = {"description": "Test task"}
    create_response = api_client.post("/tasks", json=task_data)
    task_id = create_response.json()["task_id"]

    # Get the task
    response = api_client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["task_id"] == task_id
    assert data["description"] == "Test task"


def test_get_nonexistent_task(api_client: TestClient) -> None:
    """Test getting a nonexistent task."""
    response = api_client.get("/tasks/nonexistent-id")
    assert response.status_code == 404


def test_list_tasks(api_client: TestClient) -> None:
    """Test listing all tasks."""
    # Create some tasks
    for i in range(3):
        task_data = {"description": f"Test task {i}"}
        api_client.post("/tasks", json=task_data)

    # List tasks
    response = api_client.get("/tasks")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 3
