"""Tests for agent orchestrator."""
import pytest

from agent.orchestrator.engine import AgentOrchestrator, PlanStatus


@pytest.mark.asyncio
async def test_create_plan() -> None:
    """Test creating a plan."""
    orchestrator = AgentOrchestrator()
    plan = await orchestrator.create_plan("task-1", "Test task description")

    assert plan.task_id == "task-1"
    assert plan.description == "Test task description"
    assert plan.status == PlanStatus.DRAFT
    assert len(plan.steps) > 0


@pytest.mark.asyncio
async def test_execute_plan() -> None:
    """Test executing a plan."""
    orchestrator = AgentOrchestrator()
    
    # Create a plan first
    await orchestrator.create_plan("task-1", "Test task")
    
    # Execute the plan
    result = await orchestrator.execute_plan("task-1")
    
    assert result["success"] is True
    assert result["task_id"] == "task-1"
    assert "steps_completed" in result


@pytest.mark.asyncio
async def test_execute_nonexistent_plan() -> None:
    """Test executing a nonexistent plan."""
    orchestrator = AgentOrchestrator()
    result = await orchestrator.execute_plan("nonexistent")
    
    assert result["success"] is False
    assert "error" in result


@pytest.mark.asyncio
async def test_get_plan() -> None:
    """Test getting a plan."""
    orchestrator = AgentOrchestrator()
    
    # Create a plan
    await orchestrator.create_plan("task-1", "Test task")
    
    # Get the plan
    plan = await orchestrator.get_plan("task-1")
    
    assert plan is not None
    assert plan.task_id == "task-1"


@pytest.mark.asyncio
async def test_calculate_risk_score() -> None:
    """Test calculating risk score."""
    orchestrator = AgentOrchestrator()
    
    # Create a plan
    await orchestrator.create_plan("task-1", "Test task")
    
    # Calculate risk score
    risk_score = await orchestrator.calculate_risk_score("task-1")
    
    assert 0.0 <= risk_score <= 1.0
