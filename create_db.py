from sqlalchemy import create_engine
from lib.db.models import Base

# Create engine and tables
engine = create_engine('sqlite:///bug_tracker.db')
Base.metadata.create_all(engine)

print("Database tables created successfully!")
