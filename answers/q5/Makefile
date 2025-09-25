run:
	poetry run uvicorn app.main:app --reload

db-up:
	docker compose up -d db

alembic-rev:
	poetry run alembic revision --autogenerate -m "auto"

alembic-up:
	poetry run alembic upgrade head

seed-roles:
	poetry run python -m app.infra.db.sqlalchemy.seed_roles

test:
	poetry run pytest -q

lint:
	poetry run ruff check .
	poetry run black --check .
	poetry run isort --check-only .

format:
	poetry run isort .
	poetry run black .


