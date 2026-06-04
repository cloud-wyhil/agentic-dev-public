.PHONY: install run test lint format docker-up

install:
	pip install -e ".[dev]"

run:
	uvicorn app.main:app --reload

test:
	pytest -v

lint:
	ruff check .

format:
	ruff format .

docker-up:
	docker compose up --build
