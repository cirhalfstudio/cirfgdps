.PHONY: help up down run test cq

help:
	@echo "all commands:"
	@echo "up (run docker compose)"
	@echo "down (stop docker compose)"
	@echo "run (run fastapi app)"
	@echo "test (run pytest)"
	@echo "cq (run pre-commit)"

up:
	docker compose up -d

down:
	docker compose down

run:
	uv sync
	uv run alembic upgrade head
	uv run uvicorn src.backend.main:app --host 0.0.0.0 --port 8000

test:
	uv sync
	uv run pytest

cq:
	uv sync
	uv run pre-commit run --all-files
