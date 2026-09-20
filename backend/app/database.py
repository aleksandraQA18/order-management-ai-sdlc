"""Database configuration and SQLAlchemy session helpers.

This module centralizes the connection settings used across the application so
that API routes can request a database session in a consistent way.
"""

import os
from functools import lru_cache

import psycopg
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_required_env(name: str) -> str:
    """Read an env value and fail early with a clear config error when missing."""
    value = os.getenv(name)
    if value is None or value == "":
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def get_database_url() -> str:
    """Build the PostgreSQL connection string from the environment variables."""
    return (
        f"postgresql+psycopg://{get_required_env('DB_USER')}:{get_required_env('DB_PASSWORD')}"
        f"@{get_required_env('DB_HOST')}:{get_required_env('DB_PORT')}/{get_required_env('DB_NAME')}"
    )


@lru_cache
def get_session_factory():
    """Create and cache a SQLAlchemy session factory for the app database."""
    return sessionmaker(
        bind=create_engine(get_database_url()),
        autocommit=False,
        autoflush=False,
    )


def get_db():
    """Yield a database session that is automatically closed after each request."""
    db = get_session_factory()()
    try:
        yield db
    finally:
        db.close()


def check_database_connection() -> bool:
    """Return True when the configured database accepts a simple connection test."""
    try:
        with psycopg.connect(
            host=get_required_env("DB_HOST"),
            port=get_required_env("DB_PORT"),
            dbname=get_required_env("DB_NAME"),
            user=get_required_env("DB_USER"),
            password=get_required_env("DB_PASSWORD"),
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
        return True
    except Exception:
        return False
