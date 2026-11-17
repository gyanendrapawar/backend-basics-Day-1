# Todo List API

A simple todo list REST API built with FastAPI. Tasks are stored in memory, so they reset when the server restarts.

## Features

- Add, view, update, and delete todo items
- Data validation with Pydantic
- Interactive API docs with Swagger UI

## Requirements

- Python 3.9+

## Setup

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install fastapi uvicorn
uvicorn main:app --reload
```

The API runs at http://127.0.0.1:8000 and the docs are at http://127.0.0.1:8000/docs.

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| POST | `/add-todo` | Create a todo item |
| GET | `/todo-list` | Get all todo items |
| GET | `/todo-list/{todo_id}` | Get one todo item |
| PUT | `/todo-list/{task_id}` | Update a todo item |
| DELETE | `/todo-list/{task_id}` | Delete a todo item |

## Todo Schema

```json
{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "completed": false
}
```

`title` is required. `description` is required `completed` is optional (`completed` defaults to `false`).


## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn
