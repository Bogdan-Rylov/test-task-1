from sqlalchemy.orm import Session

from database import SessionLocal


def get_db() -> Session | None:
    with SessionLocal() as db:
        yield db
