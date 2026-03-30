GIT_ROOT := $(shell git rev-parse --show-toplevel 2>/dev/null || pwd)

help:
	@echo "Available commands:"

# Dependency management via uv
install:
	uv add -r "${GIT_ROOT}/app/src/backend/requirements.txt"
export:
	uv export -o "${GIT_ROOT}/app/src/backend/requirements.txt"

format:
	uv tool run ruff format
lint:
	uv tool run ruff check

ci: format lint
	@echo "CI checks passed!"