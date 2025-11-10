# AI Run Service

AI-powered service orchestrator for automated development workflows.

## Overview

The AI Run Service is an intelligent orchestrator that automates development tasks including:
- Automated code generation and modifications
- Test execution and validation
- Git operations and PR creation
- Risk assessment and approval workflows
- CI/CD integration with AKS deployment

## Architecture

```
ai-run-service/
├── service/           # FastAPI service
│   ├── api/          # API routes and endpoints
│   ├── core/         # Core configuration
│   └── models/       # Pydantic models
├── agent/            # AI agent orchestrator
│   ├── orchestrator/ # Main orchestration engine
│   └── tools/        # Agent tools (git, testing, etc.)
├── helm/             # Kubernetes Helm charts
├── tests/            # Test suite
└── .github/          # CI/CD workflows
```

## Quick Start

### Prerequisites

- Python 3.11+
- Docker (optional, for containerized deployment)
- kubectl and Helm (for Kubernetes deployment)

### Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/LuminLynx/ai-run-service.git
   cd ai-run-service
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the service:**
   ```bash
   uvicorn service.main:app --reload
   ```

4. **Access the API:**
   - API: http://localhost:8000
   - Docs: http://localhost:8000/docs
   - Health: http://localhost:8000/health

### Docker

Build and run using Docker:

```bash
docker build -t ai-run-service .
docker run -p 8000:8000 ai-run-service
```

Or use Docker Compose:

```bash
docker-compose up
```

## Testing

### Run Tests

```bash
# Run all tests with coverage
pytest tests/ -v --cov=service --cov=agent

# Run specific test file
pytest tests/service/test_api.py -v

# Run with coverage report
pytest tests/ --cov=service --cov=agent --cov-report=html
```

### Linting and Type Checking

```bash
# Run ruff linter
ruff check service/ agent/

# Run mypy type checker
mypy service/ agent/

# Auto-fix linting issues
ruff check --fix service/ agent/
```

## API Endpoints

### Health Check
```bash
GET /health
```

### Create Task
```bash
POST /tasks
Content-Type: application/json

{
  "description": "Add new feature",
  "repository_url": "https://github.com/org/repo",
  "branch": "main"
}
```

### Get Task
```bash
GET /tasks/{task_id}
```

### List Tasks
```bash
GET /tasks
```

## Kubernetes Deployment

### Using Helm

1. **Install the chart:**
   ```bash
   helm install ai-run-service ./helm/ai-run-service
   ```

2. **Upgrade the release:**
   ```bash
   helm upgrade ai-run-service ./helm/ai-run-service
   ```

3. **Customize values:**
   ```bash
   helm install ai-run-service ./helm/ai-run-service \
     --set image.tag=v0.1.0 \
     --set replicaCount=3 \
     --set ingress.enabled=true
   ```

### Configuration

Create a `values.yaml` file to customize the deployment:

```yaml
replicaCount: 2

image:
  repository: ghcr.io/luminlynx/ai-run-service
  tag: "0.1.0"

ingress:
  enabled: true
  hosts:
    - host: ai-run-service.example.com
      paths:
        - path: /
          pathType: Prefix
```

## CI/CD

The project includes GitHub Actions workflows for:

- **CI (`.github/workflows/ci.yml`)**: Linting, testing, and building
- **CD (`.github/workflows/cd.yml`)**: Docker image publishing and deployment

### CI Pipeline

Triggered on push and PR to main/develop branches:
1. Lint code with ruff
2. Type check with mypy
3. Run tests with pytest
4. Build Docker image

### CD Pipeline

Triggered on push to main branch:
1. Build and push Docker image to GitHub Container Registry
2. Deploy to staging via ArgoCD (placeholder)

## Development Roadmap

### W1: Foundation ✅
- ✅ Scaffold repo structure (service + agent folders)
- ✅ FastAPI service with basic endpoints
- ✅ Helm charts for Kubernetes deployment
- ✅ CI/CD workflows
- ✅ Agent skeleton
- ✅ Local build/test cycle

### W2: Orchestrator & Tooling
- Build orchestrator (plan → code → test loop)
- Integrate LLM calls for plan & codegen
- Implement git automation (branch, commit, open PR)
- Local test runner (pytest, ruff, mypy)
- Risk scoring logic
- Open first AI-generated PR

### W3: Approvals & Safety Gates
- Risk-based approval workflow
- Human review queue + sign-off
- Staging auto-deploy via ArgoCD
- Post-deploy smoke tests
- Cost tracking & budget alerts
- Chaos test in staging

### W4: Prod & Observability
- SLO thresholds & alerting
- Auto-promote to prod if SLOs hold
- Auto-rollback on failure
- Dashboards & runbook
- Acceptance: 3 PRs → prod, 1 with single approval

## Configuration

Configuration is managed through environment variables:

```bash
# API Settings
API_TITLE="AI Run Service"
API_VERSION="0.1.0"
DEBUG=false

# Server Settings
HOST=0.0.0.0
PORT=8000

# Agent Settings
AGENT_ENABLED=true
AGENT_MAX_RETRIES=3
AGENT_TIMEOUT=300
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

## License

MIT License

## Support

For issues and questions, please open an issue on GitHub.