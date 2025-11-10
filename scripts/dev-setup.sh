#!/bin/bash
# Development setup and run script

set -e

echo "🚀 AI Run Service - Local Development Setup"
echo "============================================"

# Check Python version
echo "📋 Checking Python version..."
python3 --version

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -q -r requirements.txt

# Run linting
echo "🔍 Running linting checks..."
ruff check service/ agent/

# Run type checking
echo "🔍 Running type checks..."
mypy service/ agent/

# Run tests
echo "🧪 Running tests..."
pytest tests/ -v --cov=service --cov=agent --cov-report=term-missing

echo ""
echo "✅ All checks passed!"
echo ""
echo "To start the development server, run:"
echo "  source venv/bin/activate"
echo "  uvicorn service.main:app --reload"
echo ""
echo "Or use:"
echo "  make dev"
