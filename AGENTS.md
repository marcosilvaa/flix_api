# Flix API — Agent Notes

## Project Overview

Django REST Framework API for movies, actors, genres, and reviews. Brazilian Portuguese locale (`pt-br`). Backend for the Flix App dashboard (https://github.com/marcosilvaa/flix_app).

## Commands

```bash
# Install dependencies
uv sync

# Run dev server
python manage.py runserver

# Run all tests
python manage.py test

# Run tests for a single app
python manage.py test genres
python manage.py test movies

# Lint (flake8 — ignores E501, excludes .venv)
python -m flake8 .

# Create migrations after model changes
python manage.py makemigrations
python manage.py migrate

# Import actors from CSV
python manage.py import_actors actors.csv

# Collect static files (production)
python manage.py collectstatic --noinput
```

## Architecture

- **Django settings module**: `app.settings` (not the default project structure)
- **Apps** (all at repo root, not nested): `app`, `genres`, `actors`, `movies`, `reviews`, `authentication`
- **All API routes** are under `/api/v1/` prefix, wired in `app/urls.py`
- **Database**: SQLite (`db.sqlite3` at project root) — tracked in git (`.gitignore` has it commented out)

## Key Conventions

- **Permission pattern**: Views use `(IsAuthenticated, GlobalDefaultPermission)` from `app/permissions.py`. It auto-maps HTTP methods to Django model permissions as `{app_label}.{action}_{model_name}` (e.g., `movies.view_movie`, `genres.add_genre`). Exception: `genres/views.py` also has `GenrePermissionClass` in `genres/permissions.py` doing the same mapping manually.
- **Serializer pattern**: List/detail views use `get_serializer_class()` to return a richer serializer on GET and a simpler one on POST/PUT/PATCH.
- **Module structure** for each app: `models.py`, `serializers.py`, `views.py`, `urls.py`, `admin.py`, `apps.py`
- **JWT auth**: SimpleJWT with 1-day access token, 7-day refresh token. Endpoints at `/api/v1/authentication/token/`, `/api/v1/authentication/token/refresh/`, `/api/v1/authentication/token/verify/`

## Quirks & Gotchas

- **Tests only exist in `genres/tests.py`**. Other apps (actors, movies, reviews, authentication) have no test files.
- **Dev dependency file is misspelled**: `requirementes_dev.txt` (typo in filename).
- **flake8** is listed as a production dependency in `pyproject.toml` but also in the dev requirements file.
- **`db.sqlite3` is tracked in git** — the `.gitignore` line is commented out (`#db.sqlite3`).
- **`DEBUG = False`** even in development settings — you may need to set it to `True` locally or requests to non-listed hosts will be rejected.
- **Trailing slash inconsistency**: genre/actor URLs use trailing slash (`/genres/{id}/`), movie/review URLs don't (`/movies/{id}`).
- **Validation message bugs**: `MovieModelSerializer.validate_release_date` says "1990" but checks for < 1900; `validate_resume` says "200 chars" but checks for > 500.
- **`ReviewSerializers`** is named in plural (should be `ReviewSerializer` per DRF convention).
- **Dead code**: `GenrePermissionClass` in `genres/permissions.py` is never used; `MovieSerializer` (plain Serializer) in `movies/serializers.py` is never used in views.
- **Per-app READMEs** (actors, movies, reviews, app) are in English and partially outdated.

## Documentation

Detailed technical docs are in `docs/` (in Portuguese): structure, data models, API endpoints, permissions, auth, conventions, dev guide, and known issues. See `docs/README.md` for the index.