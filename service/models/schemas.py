"""Pydantic models for API requests and responses."""
from datetime import datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class TaskStatus(str, Enum):
    """Status of a task."""

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class TaskRequest(BaseModel):
    """Request to create a new task."""

    description: str = Field(..., description="Description of the task to perform")
    repository_url: str | None = Field(None, description="Repository URL if applicable")
    branch: str | None = Field(None, description="Target branch")
    metadata: dict[str, Any] | None = Field(default_factory=dict, description="Additional metadata")


class TaskResponse(BaseModel):
    """Response for a task."""

    task_id: str = Field(..., description="Unique task identifier")
    status: TaskStatus = Field(..., description="Current task status")
    description: str = Field(..., description="Task description")
    created_at: datetime = Field(..., description="Task creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")
    result: dict[str, Any] | None = Field(None, description="Task result if completed")
    error: str | None = Field(None, description="Error message if failed")


class HealthResponse(BaseModel):
    """Health check response."""

    status: str = Field(..., description="Service status")
    version: str = Field(..., description="Service version")
    timestamp: datetime = Field(..., description="Current timestamp")
    agent_enabled: bool = Field(..., description="Whether agent is enabled")
