"""Pydantic schemas for request validation and response serialization.

These models define the shape of data entering and leaving the API. FastAPI
uses them to validate request bodies, generate the interactive documentation,
and convert ORM objects into JSON responses.
"""

from typing import List, Optional

from pydantic import BaseModel, ConfigDict


# ---------------------------------------------------------------------------
# Choice schemas
# ---------------------------------------------------------------------------

class ChoiceBase(BaseModel):
    choice_text: str
    is_correct: bool = False


class ChoiceCreate(ChoiceBase):
    """Payload for creating a choice on its own, tied to a question by id."""
    question_id: int


class ChoiceUpdate(BaseModel):
    """Every field is optional so a client can update just what it needs."""
    choice_text: Optional[str] = None
    is_correct: Optional[bool] = None
    question_id: Optional[int] = None


class ChoiceOut(ChoiceBase):
    id: int
    question_id: int

    model_config = ConfigDict(from_attributes=True)


# ---------------------------------------------------------------------------
# Question schemas
# ---------------------------------------------------------------------------

class ChoiceNested(BaseModel):
    """A trimmed choice used when choices are created inline with a question."""
    choice_text: str
    is_correct: bool = False


class QuestionBase(BaseModel):
    question_text: str
    category: Optional[str] = None


class QuestionCreate(QuestionBase):
    """A question can be created together with a list of choices in one call."""
    choices: List[ChoiceNested] = []


class QuestionUpdate(BaseModel):
    question_text: Optional[str] = None
    category: Optional[str] = None


class QuestionOut(QuestionBase):
    id: int
    choices: List[ChoiceOut] = []

    model_config = ConfigDict(from_attributes=True)
