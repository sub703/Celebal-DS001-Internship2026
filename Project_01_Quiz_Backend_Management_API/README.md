# Project 01 – Quiz Backend Management API using FastAPI

## Overview

This project was completed as part of the **Celebal Excellence Internship (CEI) 2026** under the **Data Science (DS001)** track at **Celebal Technologies**.

The project focuses on developing a RESTful backend system for managing quiz questions and their answer choices using **FastAPI**. The application implements complete CRUD operations, request and response validation, relational database management, and automatically generated interactive API documentation.

The system is designed as a general-purpose quiz management platform capable of supporting questions across domains such as **General Knowledge, Programming, Mathematics, Data Science, and other categories**.

---

## Problem Statement

**Develop a Quiz Backend Management System using FastAPI.**

The project involved building a backend application capable of:

* Creating quiz questions and answer choices
* Retrieving questions and choices
* Updating existing quiz data
* Deleting questions and associated choices
* Maintaining relationships between questions and choices
* Validating API requests and responses
* Storing quiz data using a relational database
* Providing interactive API documentation
* Supporting optional question categories
* Allowing pagination and category-based filtering

---

## Key Features

* Full **CRUD operations** for questions
* Full **CRUD operations** for answer choices
* One-to-many relationship between questions and choices
* Correct/incorrect flag for each answer choice
* Optional category field for questions
* Category-based question filtering
* Pagination support for question and choice retrieval
* Pydantic-based request and response validation
* SQLAlchemy ORM for database operations
* Automatic cascade deletion of choices when a question is deleted
* SQLite database by default
* PostgreSQL/MySQL support through the `DATABASE_URL` environment variable
* Interactive API documentation using FastAPI's OpenAPI/Swagger interface
* Sample database seeding script

The project requirements specifically emphasize CRUD operations, database relationships, Pydantic validation, SQLAlchemy ORM, and API documentation.

---

## Technology Stack

| Technology           | Purpose                         |
| -------------------- | ------------------------------- |
| Python               | Application development         |
| FastAPI              | REST API framework and routing  |
| SQLAlchemy           | ORM and database management     |
| Pydantic             | Request and response validation |
| SQLite               | Default relational database     |
| Uvicorn              | ASGI server                     |
| OpenAPI / Swagger UI | Interactive API documentation   |

The project uses pinned versions of FastAPI, Uvicorn, SQLAlchemy, and Pydantic in `requirements.txt`.

---

## Project Architecture

```text
Client Request
      │
      ▼
FastAPI Routes
      │
      ▼
Pydantic Validation
      │
      ▼
CRUD Layer
      │
      ▼
SQLAlchemy ORM
      │
      ▼
SQLite Database
```

The application separates API routing, validation schemas, CRUD/database logic, ORM models, and database configuration into dedicated modules.

---

## Project Structure

```text
Project_01_Quiz_Backend_Management_API/
│
├── app/
│   ├── __init__.py
│   ├── crud.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── main.py
│
├── seed_data.py
├── requirements.txt
├── .gitignore
└── README.md
```

### Module Responsibilities

| File               | Purpose                                                          |
| ------------------ | ---------------------------------------------------------------- |
| `main.py`          | FastAPI application and API route definitions                    |
| `crud.py`          | Database create, read, update and delete operations              |
| `database.py`      | SQLAlchemy engine, session management and database configuration |
| `models.py`        | SQLAlchemy ORM models for questions and choices                  |
| `schemas.py`       | Pydantic request and response schemas                            |
| `seed_data.py`     | Inserts sample quiz questions into the database                  |
| `requirements.txt` | Project dependencies                                             |
| `.gitignore`       | Files excluded from version control                              |

## The CRUD layer contains separate operations for both questions and choices, while the models define the one-to-many Question–Choice relationship.

## Database Design

### Question

| Field           | Type    | Description              |
| --------------- | ------- | ------------------------ |
| `id`            | Integer | Primary key              |
| `question_text` | String  | Quiz question            |
| `category`      | String  | Optional category/domain |

### Choice

| Field         | Type    | Description                             |
| ------------- | ------- | --------------------------------------- |
| `id`          | Integer | Primary key                             |
| `choice_text` | String  | Answer option                           |
| `is_correct`  | Boolean | Indicates whether the choice is correct |
| `question_id` | Integer | Foreign key referencing a question      |

## Each question can contain multiple choices, while every choice belongs to a single question. Deleting a question also removes its associated choices through the configured cascade relationship.

## API Endpoints

### Health

| Method | Endpoint | Description      |
| ------ | -------- | ---------------- |
| GET    | `/`      | API health check |

### Questions

| Method | Endpoint                   | Description                                                        |
| ------ | -------------------------- | ------------------------------------------------------------------ |
| POST   | `/questions`               | Create a question, optionally with choices                         |
| GET    | `/questions`               | Retrieve questions with pagination and optional category filtering |
| GET    | `/questions/{question_id}` | Retrieve a specific question                                       |
| PUT    | `/questions/{question_id}` | Update a question                                                  |
| DELETE | `/questions/{question_id}` | Delete a question and its choices                                  |

### Choices

| Method | Endpoint               | Description                      |
| ------ | ---------------------- | -------------------------------- |
| POST   | `/choices`             | Create an answer choice          |
| GET    | `/choices`             | Retrieve choices with pagination |
| GET    | `/choices/{choice_id}` | Retrieve a specific choice       |
| PUT    | `/choices/{choice_id}` | Update an answer choice          |
| DELETE | `/choices/{choice_id}` | Delete an answer choice          |

The implemented routes correspond to the project requirements for question and choice management.

---

## API Documentation

FastAPI automatically generates interactive API documentation.

After starting the server, open:

```text
http://127.0.0.1:8000/docs
```

The Swagger interface allows the available endpoints to be explored and tested directly from the browser.

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Celebal-DS001-Internship2026.git
cd Celebal-DS001-Internship2026/Project_01_Quiz_Backend_Management_API
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the FastAPI server

```bash
uvicorn app.main:app --reload
```

### 5. Open the API documentation

```text
http://127.0.0.1:8000/docs
```

---

## Sample Data

The project includes `seed_data.py`, which inserts sample questions from multiple categories, including Programming, Mathematics, Data Science, and General Knowledge.

To populate the database:

```bash
python seed_data.py
```

---

## Database Configuration

The project uses SQLite by default:

```text
sqlite:///./quiz.db
```

The database can be changed through the `DATABASE_URL` environment variable to support PostgreSQL or MySQL.

---

## Learning Outcomes

Through this project, the following concepts were practiced:

* RESTful API development
* FastAPI application development
* CRUD API implementation
* Database design
* Relational database concepts
* SQLAlchemy ORM
* One-to-many database relationships
* Pydantic data validation
* Request and response schema design
* API routing
* Pagination and filtering
* Database session management
* Interactive API documentation
* Backend application architecture
* Python virtual environments
* API testing and development

---

## Future Enhancements

Potential extensions include:

* User authentication and authorization
* Quiz attempt tracking
* Score and leaderboard management
* Timed quizzes
* Analytics dashboard
* Adaptive quizzes
* Performance-based recommendations
* User-specific quiz history

These extensions are also identified in the project support document as possible future improvements.

---

## Author

**Subrata Kumar Dey**

**Data Science Intern – CEI 2026**

B.Tech in Computer Science & Engineering (Cyber Security & Privacy)

DIT University
