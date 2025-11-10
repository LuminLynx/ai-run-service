"""API router definitions."""
from datetime import UTC, datetime
from uuid import uuid4

from fastapi import APIRouter, HTTPException, status

from service.core.config import get_settings
from service.models.schemas import HealthResponse, TaskRequest, TaskResponse, TaskStatus

router = APIRouter()
settings = get_settings()

# In-memory storage for tasks (will be replaced with proper storage in W2)
tasks_store: dict[str, TaskResponse] = {}


@router.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check() -> HealthResponse:
    """Health check endpoint."""
    return HealthResponse(
        status="healthy",
        version=settings.api_version,
        timestamp=datetime.now(UTC),
        agent_enabled=settings.agent_enabled,
    )


@router.get("/", tags=["Root"])
async def root() -> dict[str, str]:
    """Root endpoint."""
    return {
        "message": "AI Run Service API",
        "version": settings.api_version,
        "docs": "/docs",
    }


@router.post(
    "/tasks",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Tasks"],
)
async def create_task(task_request: TaskRequest) -> TaskResponse:
    """Create a new task."""
    task_id = str(uuid4())
    now = datetime.now(UTC)

    task = TaskResponse(
        task_id=task_id,
        status=TaskStatus.PENDING,
        description=task_request.description,
        created_at=now,
        updated_at=now,
        result=None,
        error=None,
    )

    tasks_store[task_id] = task
    return task


@router.get("/tasks/{task_id}", response_model=TaskResponse, tags=["Tasks"])
async def get_task(task_id: str) -> TaskResponse:
    """Get task by ID."""
    if task_id not in tasks_store:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task {task_id} not found",
        )
    return tasks_store[task_id]


@router.get("/tasks", response_model=list[TaskResponse], tags=["Tasks"])
async def list_tasks() -> list[TaskResponse]:
    """List all tasks."""
    return list(tasks_store.values())
