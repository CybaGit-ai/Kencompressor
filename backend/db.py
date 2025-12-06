from __future__ import annotations

from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///./app.db"
engine = create_engine(DATABASE_URL, echo=False)


def init_db() -> None:
    SQLModel.metadata.create_all(bind=engine)


@asynccontextmanager
def get_session() -> AsyncGenerator[Session, None]:
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()
