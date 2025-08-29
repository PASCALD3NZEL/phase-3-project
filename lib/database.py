from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///bugtracker.db")

Base = declarative_base()

# Session setup
SessionLocal = sessionmaker(bind=engine, autoflush=True, autocommit=False)
session = SessionLocal()