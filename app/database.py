"""Database configuration and session management.

Sets up the SQLAlchemy engine, a session factory, and the declarative base
that all ORM models inherit from. SQLite is used by default so the project
runs without any external database server. To switch to PostgreSQL or MySQL,
change DATABASE_URL and remove the SQLite-only connect_args below.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Default to a local SQLite file. Override with the DATABASE_URL environment
# variable to point at PostgreSQL or MySQL in a production setting.
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./quiz.db")

# check_same_thread is a SQLite-specific flag. It is required because FastAPI
# may access the same connection from different threads. Drop this argument
# when using PostgreSQL or MySQL.
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """Yield a database session and guarantee it is closed afterwards.

    FastAPI calls this as a dependency for every request that needs the
    database, which keeps session handling out of the route functions.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
