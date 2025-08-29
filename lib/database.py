from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# connect to SQLite (adjust if you’re using another DB)
engine = create_engine("sqlite:///bugtracker.db")

Base = declarative_base()

# configure session
Session = sessionmaker(bind=engine, autoflush=True, autocommit=False)