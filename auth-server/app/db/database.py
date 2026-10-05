from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings

#The engine is SQLAlchemy's connection interface to PostgreSQL.
engine = create_engine(settings.DATABASE_URL)

#A session represents a working interaction with the database.
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

class Base(DeclarativeBase):
    pass