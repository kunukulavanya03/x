from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session
from sqlalchemy.orm.session import sessionmaker
from main import app

SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost:5432/database"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

Base = declarative_base()

SessionLocal = scoped_session(sessionmaker(bind=engine))
