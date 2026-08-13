"""Database access layer.

Every read and write against the database lives here, which keeps the route
functions in main.py short and focused on request handling. Each function
takes an active session and returns ORM objects or None.
"""

from typing import List, Optional

from sqlalchemy.orm import Session

from app import models, schemas


# ---------------------------------------------------------------------------
# Question operations
# ---------------------------------------------------------------------------

def create_question(db: Session, question: schemas.QuestionCreate) -> models.Question:
    db_question = models.Question(
        question_text=question.question_text,
        category=question.category,
    )
    # Attach any choices supplied inline with the question.
    for choice in question.choices:
        db_question.choices.append(
            models.Choice(
                choice_text=choice.choice_text,
                is_correct=choice.is_correct,
            )
        )
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question


def get_questions(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    category: Optional[str] = None,
) -> List[models.Question]:
    query = db.query(models.Question)
    if category:
        query = query.filter(models.Question.category == category)
    return query.offset(skip).limit(limit).all()


def get_question(db: Session, question_id: int) -> Optional[models.Question]:
    return db.query(models.Question).filter(models.Question.id == question_id).first()


def update_question(
    db: Session,
    question_id: int,
    updates: schemas.QuestionUpdate,
) -> Optional[models.Question]:
    db_question = get_question(db, question_id)
    if db_question is None:
        return None
    # exclude_unset means only the fields the client actually sent get applied.
    for field, value in updates.model_dump(exclude_unset=True).items():
        setattr(db_question, field, value)
    db.commit()
    db.refresh(db_question)
    return db_question


def delete_question(db: Session, question_id: int) -> bool:
    db_question = get_question(db, question_id)
    if db_question is None:
        return False
    db.delete(db_question)  # cascade removes the attached choices
    db.commit()
    return True


# ---------------------------------------------------------------------------
# Choice operations
# ---------------------------------------------------------------------------

def create_choice(db: Session, choice: schemas.ChoiceCreate) -> Optional[models.Choice]:
    # Guard against attaching a choice to a question that does not exist.
    if get_question(db, choice.question_id) is None:
        return None
    db_choice = models.Choice(
        choice_text=choice.choice_text,
        is_correct=choice.is_correct,
        question_id=choice.question_id,
    )
    db.add(db_choice)
    db.commit()
    db.refresh(db_choice)
    return db_choice


def get_choices(db: Session, skip: int = 0, limit: int = 100) -> List[models.Choice]:
    return db.query(models.Choice).offset(skip).limit(limit).all()


def get_choice(db: Session, choice_id: int) -> Optional[models.Choice]:
    return db.query(models.Choice).filter(models.Choice.id == choice_id).first()


def update_choice(
    db: Session,
    choice_id: int,
    updates: schemas.ChoiceUpdate,
) -> Optional[models.Choice]:
    db_choice = get_choice(db, choice_id)
    if db_choice is None:
        return None
    data = updates.model_dump(exclude_unset=True)
    # If the question_id is being changed, confirm the new question exists.
    if "question_id" in data and get_question(db, data["question_id"]) is None:
        return None
    for field, value in data.items():
        setattr(db_choice, field, value)
    db.commit()
    db.refresh(db_choice)
    return db_choice


def delete_choice(db: Session, choice_id: int) -> bool:
    db_choice = get_choice(db, choice_id)
    if db_choice is None:
        return False
    db.delete(db_choice)
    db.commit()
    return True
