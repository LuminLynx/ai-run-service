.PHONY: help install dev test lint format clean docker-build docker-run

help:
	@echo "Available commands:"
	@echo "  make install       - Install dependencies"
	@echo "  make dev           - Run development server"
	@echo "  make test          - Run tests with coverage"
	@echo "  make lint          - Run linting and type checking"
	@echo "  make format        - Format code with ruff"
	@echo "  make clean         - Clean build artifacts"
	@echo "  make docker-build  - Build Docker image"
	@echo "  make docker-run    - Run Docker container"

install:
	pip install -r requirements.txt

dev:
	uvicorn service.main:app --reload --host 0.0.0.0 --port 8000

test:
	pytest tests/ -v --cov=service --cov=agent --cov-report=term-missing --cov-report=html

lint:
	ruff check service/ agent/
	mypy service/ agent/

format:
	ruff check --fix service/ agent/
	ruff format service/ agent/

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	rm -rf htmlcov/ .coverage dist/ build/

docker-build:
	docker build -t ai-run-service:latest .

docker-run:
	docker run -p 8000:8000 ai-run-service:latest
