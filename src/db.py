from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import Session

from src.config import Settings

__engine: Engine = create_engine(Settings().DATABASE_URL)


def get_session():
    with Session(__engine) as session:
        yield session
