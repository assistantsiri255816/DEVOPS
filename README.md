# python-microservices-devops
Multi-service Python project (Flask backend + Flask frontend + Logger) with Docker Compose and Terraform configs for AWS.

**Structure**:
- backend/
- frontend/
- logger/
- docker-compose.yml
- terraform/
- .github/workflows/ci.yml (example CI workflow)

How to run locally:
1. Install Docker & Docker Compose
2. From repo root: `docker compose up --build`
3. Frontend: http://localhost:8080
4. Backend API: http://localhost:5000/api/data
5. Logger accepts POST /log to append to `/logs/app.log`
