"""Tests for Git tool."""
import pytest

from agent.tools.git import GitTool


@pytest.mark.asyncio
async def test_git_tool_init() -> None:
    """Test Git tool initialization."""
    tool = GitTool()
    assert tool.work_dir.exists()


@pytest.mark.asyncio
async def test_create_branch() -> None:
    """Test creating a branch."""
    tool = GitTool()
    result = await tool.create_branch("feature/test")
    assert result is True


@pytest.mark.asyncio
async def test_commit_changes() -> None:
    """Test committing changes."""
    tool = GitTool()
    commit_sha = await tool.commit_changes("Test commit")
    assert commit_sha is not None
    assert len(commit_sha) > 0
