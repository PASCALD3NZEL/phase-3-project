from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the engine (SQLite example)
engine = create_engine("sqlite:///bugtracker.db")

Base = declarative_base()

# Configure session
SessionLocal = sessionmaker(bind=engine, autoflush=True, autocommit=False)
session = SessionLocal()