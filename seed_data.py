"""Populate the database with a small set of sample questions.

Run this once after starting the project to have some data to explore:

    python seed_data.py

It is safe to run on an empty database. Running it repeatedly will add
duplicate rows, so use it mainly for a fresh setup or a quick demo.
"""

from app.database import Base, SessionLocal, engine
from app import models

Base.metadata.create_all(bind=engine)

SAMPLE_QUESTIONS = [
    {
        "question_text": "Which keyword is used to define a function in Python?",
        "category": "Programming",
        "choices": [
            ("func", False),
            ("def", True),
            ("function", False),
            ("lambda", False),
        ],
    },
    {
        "question_text": "What is the value of 7 multiplied by 8?",
        "category": "Mathematics",
        "choices": [
            ("54", False),
            ("56", True),
            ("48", False),
            ("64", False),
        ],
    },
    {
        "question_text": "Which data structure works on a First In First Out basis?",
        "category": "Data Science",
        "choices": [
            ("Stack", False),
            ("Queue", True),
            ("Tree", False),
            ("Graph", False),
        ],
    },
    {
        "question_text": "Which planet is known as the Red Planet?",
        "category": "General Knowledge",
        "choices": [
            ("Venus", False),
            ("Mars", True),
            ("Jupiter", False),
            ("Saturn", False),
        ],
    },
]


def seed():
    db = SessionLocal()
    try:
        for item in SAMPLE_QUESTIONS:
            question = models.Question(
                question_text=item["question_text"],
                category=item["category"],
            )
            for text, correct in item["choices"]:
                question.choices.append(
                    models.Choice(choice_text=text, is_correct=correct)
                )
            db.add(question)
        db.commit()
        print(f"Inserted {len(SAMPLE_QUESTIONS)} sample questions.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
