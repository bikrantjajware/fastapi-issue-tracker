# FastAPI Issue Tracker

A small FastAPI app for practicing and revising FastAPI syntax, Pydantic models, request validation, and API routes.

## Run locally

Use Python 3 and install the dependencies from the project root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

The app runs at <http://127.0.0.1:8000>. Interactive API documentation is available at <http://127.0.0.1:8000/docs>, with the alternative documentation at <http://127.0.0.1:8000/redoc>.

## Endpoints

All API routes except the health check use the `/api/v1` prefix.

| Method | Path | Purpose |
| --- | --- | --- |
| `GET` | `/health` | Check that the app is running |
| `GET` | `/api/v1/issues/` | List issues |
| `GET` | `/api/v1/issues/{issue_id}` | Get an issue by ID |
| `POST` | `/api/v1/issues` | Create an issue |
| `PUT` | `/api/v1/issues/{issue_id}` | Update an issue |
| `DELETE` | `/api/v1/issues/{issue_id}` | Delete an issue |
| `GET` | `/api/v1/practice` | List practice messages |
| `POST` | `/api/v1/practice/create` | Add a practice message |

Issue request bodies are validated using the Pydantic schemas in `app/schemas/issues_schemas.py`. For example:

```json
{
  "title": "Example issue",
  "description": "A short description",
  "priority": "medium",
  "status": "open"
}
```

The practice message endpoint accepts a body like:

```json
{
  "author": "Alex",
  "msg": "Practicing FastAPI"
}
```

## Project layout

```text
main.py                    App setup and health endpoint
app/
  routes/                  Issue and practice API routes
  schemas/                 Pydantic request and response models
  storage.py               JSON file load/save helpers
data/
  issues.json              Issue data file
```

Issue data is loaded from `data/issues.json` when the issues route is imported. Updates and deletes save the current issue list to that file; newly created issues are currently held in memory until they are saved by a later update or delete.
