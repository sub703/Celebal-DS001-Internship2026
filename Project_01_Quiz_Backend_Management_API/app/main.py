"""Application entry point.

Creates the FastAPI application, builds the database tables on startup, and
registers every route for managing questions and choices. Run the server with:

    uvicorn app.main:app --reload

Then open http://127.0.0.1:8000/docs to explore the API.
"""

from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, Query, status
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.database import Base, engine, get_db

# Create the tables the first time the app runs. For a larger project this
# would be handled by a migration tool such as Alembic.
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Quiz Backend Management API",
    description=(
        "A RESTful backend for managing quiz questions and their answer "
        "choices. Supports full create, read, update, and delete operations "
        "across multiple quiz categories."
    ),
    version="1.0.0",
)


@app.get("/", tags=["Health"])
def root():
    """Simple health check so you can confirm the server is up."""
    return {"status": "ok", "message": "Quiz Backend Management API is running"}


# ---------------------------------------------------------------------------
# Question routes
# ---------------------------------------------------------------------------

@app.post(
    "/questions",
    response_model=schemas.QuestionOut,
    status_code=status.HTTP_201_CREATED,
    tags=["Questions"],
)
def create_question(question: schemas.QuestionCreate, db: Session = Depends(get_db)):
    """Create a question, optionally with its choices in the same request."""
    return crud.create_question(db, question)


@app.get("/questions", response_model=List[schemas.QuestionOut], tags=["Questions"])
def read_questions(
    skip: int = 0,
    limit: int = Query(100, le=500),
    category: Optional[str] = None,
    db: Session = Depends(get_db),
):
    """List questions, with optional filtering by category and pagination."""
    return crud.get_questions(db, skip=skip, limit=limit, category=category)


@app.get("/questions/{question_id}", response_model=schemas.QuestionOut, tags=["Questions"])
def read_question(question_id: int, db: Session = Depends(get_db)):
    """Fetch a single question and its choices by id."""
    db_question = crud.get_question(db, question_id)
    if db_question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return db_question


@app.put("/questions/{question_id}", response_model=schemas.QuestionOut, tags=["Questions"])
def update_question(
    question_id: int,
    updates: schemas.QuestionUpdate,
    db: Session = Depends(get_db),
):
    """Update the text or category of an existing question."""
    db_question = crud.update_question(db, question_id, updates)
    if db_question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return db_question


@app.delete("/questions/{question_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Questions"])
def delete_question(question_id: int, db: Session = Depends(get_db)):
    """Delete a question along with all of its choices."""
    if not crud.delete_question(db, question_id):
        raise HTTPException(status_code=404, detail="Question not found")
    return None


# ---------------------------------------------------------------------------
# Choice routes
# ---------------------------------------------------------------------------

@app.post(
    "/choices",
    response_model=schemas.ChoiceOut,
    status_code=status.HTTP_201_CREATED,
    tags=["Choices"],
)
def create_choice(choice: schemas.ChoiceCreate, db: Session = Depends(get_db)):
    """Add a choice to an existing question."""
    db_choice = crud.create_choice(db, choice)
    if db_choice is None:
        raise HTTPException(
            status_code=400,
            detail="Cannot add choice: the referenced question does not exist",
        )
    return db_choice


@app.get("/choices", response_model=List[schemas.ChoiceOut], tags=["Choices"])
def read_choices(
    skip: int = 0,
    limit: int = Query(100, le=500),
    db: Session = Depends(get_db),
):
    """List all answer choices with pagination."""
    return crud.get_choices(db, skip=skip, limit=limit)


@app.get("/choices/{choice_id}", response_model=schemas.ChoiceOut, tags=["Choices"])
def read_choice(choice_id: int, db: Session = Depends(get_db)):
    """Fetch a single choice by id."""
    db_choice = crud.get_choice(db, choice_id)
    if db_choice is None:
        raise HTTPException(status_code=404, detail="Choice not found")
    return db_choice


@app.put("/choices/{choice_id}", response_model=schemas.ChoiceOut, tags=["Choices"])
def update_choice(
    choice_id: int,
    updates: schemas.ChoiceUpdate,
    db: Session = Depends(get_db),
):
    """Update a choice, including moving it to a different question."""
    db_choice = crud.update_choice(db, choice_id, updates)
    if db_choice is None:
        raise HTTPException(
            status_code=404,
            detail="Choice not found, or the target question does not exist",
        )
    return db_choice


@app.delete("/choices/{choice_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Choices"])
def delete_choice(choice_id: int, db: Session = Depends(get_db)):
    """Delete a single answer choice."""
    if not crud.delete_choice(db, choice_id):
        raise HTTPException(status_code=404, detail="Choice not found")
    return None
