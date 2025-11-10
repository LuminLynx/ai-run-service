"""Tests for test runner tool."""
import pytest

from agent.tools.test_runner import TestRunnerTool


@pytest.mark.asyncio
async def test_run_tests() -> None:
    """Test running tests."""
    runner = TestRunnerTool()
    result = await runner.run_tests()
    
    assert result.success is not None
    assert result.tests_run >= 0
    assert result.tests_passed >= 0
    assert result.tests_failed >= 0


@pytest.mark.asyncio
async def test_run_linter() -> None:
    """Test running linter."""
    runner = TestRunnerTool()
    result = await runner.run_linter()
    assert isinstance(result, bool)


@pytest.mark.asyncio
async def test_run_type_checker() -> None:
    """Test running type checker."""
    runner = TestRunnerTool()
    result = await runner.run_type_checker()
    assert isinstance(result, bool)
