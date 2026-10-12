# CLAUDE.md

## Language
All code, comments, docstrings, commit messages and PR text must be in English.

## Checks
Run these when developing a new feature and again before creating a PR (they mirror `.github/workflows`):

```bash
uv sync --locked --all-extras --dev
uv run pytest tests
uv run ruff check .
uv run ruff format --check .
uv run mypy examples src tests
uv run pre-commit run --all-files   # codespell, pylint, file/format checks
uv run yamllint .
```

Fix every failure before opening the PR.

## TeslaMateApi compatibility
When the client is updated for a new teslamateapi release, update the "TeslaMateApi Compatibility" badge in `README.md` (line 4: both the badge text and the release link) to that version.
