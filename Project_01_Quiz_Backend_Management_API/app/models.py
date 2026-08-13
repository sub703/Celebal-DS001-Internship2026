"""SQLAlchemy ORM models.

Two tables model the quiz data. A Question holds the prompt and an optional
category, and each Question owns many Choice rows. A Choice belongs to exactly
one Question and records whether it is the correct answer.
"""

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String, nullable=False)
    category = Column(String, nullable=True, index=True)

    # A question owns its choices. Deleting a question deletes its choices too,
    # which is handled by the cascade setting below.
    choices = relationship(
        "Choice",
        back_populates="question",
        cascade="all, delete-orphan",
    )


class Choice(Base):
    __tablename__ = "choices"

    id = Column(Integer, primary_key=True, index=True)
    choice_text = Column(String, nullable=False)
    is_correct = Column(Boolean, default=False, nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)

    question = relationship("Question", back_populates="choices")
