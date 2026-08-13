# Quiz Backend Management API

A RESTful backend for managing quiz questions and their answer choices, built with FastAPI. The service exposes clean CRUD endpoints for questions and choices, validates every request with Pydantic, and persists data through the SQLAlchemy ORM. It works as a general purpose quiz platform, so questions from any domain such as General Knowledge, Programming, Mathematics, or Data Science can live in the same system, separated by an optional category field.

## Features

- Full create, read, update, and delete support for both questions and choices
- One question owns many choices, with each choice flagged as correct or incorrect
- Deleting a question automatically removes its choices through a cascade rule
- Optional category field so questions can be grouped and filtered by domain
- Request and response validation handled by Pydantic
- Interactive API documentation generated automatically by FastAPI
- SQLite by default with no setup, and a single change to move to PostgreSQL or MySQL

## Tech stack

| Technology | Role |
|------------|------|
| FastAPI | Web framework and routing |
| SQLAlchemy | Object relational mapper for database access |
| Pydantic | Request and response validation |
| SQLite | Default storage, swappable for PostgreSQL or MySQL |
| Uvicorn | ASGI server that runs the application |

## Project structure

```
quiz-backend-api/
├── app/
│   ├── __init__.py
│   ├── database.py      # Engine, session factory, and the declarative base
│   ├── models.py        # Question and Choice ORM models
│   ├── schemas.py       # Pydantic schemas for validation and serialization
│   ├── crud.py          # All database read and write logic
│   └── main.py          # FastAPI application and route definitions
├── seed_data.py         # Optional script that inserts sample questions
├── requirements.txt
├── .gitignore
└── README.md
```

The layout keeps each concern in its own file. Routes stay thin because the database work lives in `crud.py`, and the data shapes are defined once in `schemas.py`, which makes the project easy to read and extend.

## Getting started

You will need Python 3.9 or newer.

1. Clone the repository and move into the folder.

   ```bash
   git clone https://github.com/your-username/quiz-backend-api.git
   cd quiz-backend-api
   ```

2. Create and activate a virtual environment.

   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows use: venv\Scripts\activate
   ```

3. Install the dependencies.

   ```bash
   pip install -r requirements.txt
   ```

4. Start the server.

   ```bash
   uvicorn app.main:app --reload
   ```

The API is now running at `http://127.0.0.1:8000`.

5. Open the interactive documentation in your browser.

   ```
   http://127.0.0.1:8000/docs
   ```

This page lets you send real requests to every endpoint without writing any code, which is the quickest way to try the API.

### Optional sample data

To load a handful of ready made questions so there is something to query straight away, run:

```bash
python seed_data.py
```

## API reference

The base URL for all endpoints is `http://127.0.0.1:8000`.

### Questions

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/questions` | Create a question, optionally with choices included |
| GET | `/questions` | List questions, with optional category filter and pagination |
| GET | `/questions/{id}` | Retrieve a single question and its choices |
| PUT | `/questions/{id}` | Update a question's text or category |
| DELETE | `/questions/{id}` | Delete a question and all of its choices |

### Choices

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/choices` | Add a choice to an existing question |
| GET | `/choices` | List all choices with pagination |
| GET | `/choices/{id}` | Retrieve a single choice |
| PUT | `/choices/{id}` | Update a choice or move it to another question |
| DELETE | `/choices/{id}` | Delete a single choice |

## Example requests

Create a question together with its choices in one call.

```bash
curl -X POST http://127.0.0.1:8000/questions \
  -H "Content-Type: application/json" \
  -d '{
        "question_text": "Which keyword defines a function in Python?",
        "category": "Programming",
        "choices": [
          {"choice_text": "func", "is_correct": false},
          {"choice_text": "def", "is_correct": true},
          {"choice_text": "function", "is_correct": false}
        ]
      }'
```

List every question in the Programming category.

```bash
curl "http://127.0.0.1:8000/questions?category=Programming"
```

Add a single choice to the question with id 1.

```bash
curl -X POST http://127.0.0.1:8000/choices \
  -H "Content-Type: application/json" \
  -d '{"choice_text": "lambda", "is_correct": false, "question_id": 1}'
```

## Data model

The schema is intentionally small. A question holds the prompt text and an optional category. Each question owns any number of choices, and each choice records its text and whether it is the correct answer.

**Question**

| Field | Type | Notes |
|-------|------|-------|
| id | Integer | Primary key |
| question_text | String | The prompt shown to a quiz taker |
| category | String | Optional domain label used for grouping |

**Choice**

| Field | Type | Notes |
|-------|------|-------|
| id | Integer | Primary key |
| choice_text | String | The answer option text |
| is_correct | Boolean | Marks the correct answer |
| question_id | Integer | Foreign key linking back to a question |

## Switching the database

The project runs on SQLite out of the box so it needs no external setup. To use PostgreSQL or MySQL instead, set the `DATABASE_URL` environment variable before starting the server, for example:

```bash
export DATABASE_URL="postgresql://user:password@localhost:5432/quizdb"
```

The connection settings in `app/database.py` adjust automatically for anything other than SQLite.

## Possible extensions

The design leaves clear room to grow. Natural next steps include user authentication, scoring and leaderboards, a record of past quiz attempts, timed quizzes, and an analytics dashboard built on top of the collected data.
