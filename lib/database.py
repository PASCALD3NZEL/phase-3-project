from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Single database file for the whole app
engine = create_engine("sqlite:///bugtracker.db")

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, autoflush=True, autocommit=False)
session = SessionLocal()
