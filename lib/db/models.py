# lib/db/models.py

# Import the necessary tools from SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from datetime import datetime

# This creates a base class that all our models will inherit from
Base = declarative_base()

class Project(Base):
    """Represents a software project that contains many issues"""
    __tablename__ = 'projects'  # This will be the table name in the database

    id = Column(Integer, primary_key=True)  # Unique ID for each project
    name = Column(String, unique=True)      # Project name (must be unique)
    description = Column(String)            # Short description of the project

    # This creates a relationship - one project can have many issues
    issues = relationship('Issue', backref='project')

    def __repr__(self):
        """How the project will display when printed"""
        return f"Project(id={self.id}, name='{self.name}')"

class User(Base):
    """Represents a team member who can be assigned issues"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)  # Unique ID for each user
    name = Column(String)                   # User's full name
    email = Column(String, unique=True)     # User's email (must be unique)

    # Relationships: a user can be assigned many issues and can report many issues
    assigned_issues = relationship('Issue', foreign_keys='Issue.assignee_id', backref='assignee')
    reported_issues = relationship('Issue', foreign_keys='Issue.reporter_id', backref='reporter')

    def __repr__(self):
        """How the user will display when printed"""
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"

class Issue(Base):
    """Represents a bug report or feature request"""
    __tablename__ = 'issues'  # Changed from 'tickets' to match your project idea!

    id = Column(Integer, primary_key=True)  # Unique ID for each issue
    title = Column(String)                  # Short title of the issue
    description = Column(Text)              # Detailed description of the issue
    status = Column(String, default='Open') # Current status: Open, In Progress, Closed
    priority = Column(String, default='Medium')  # Priority: Low, Medium, High, Critical
    
    # Foreign keys to link to projects and users
    project_id = Column(Integer, ForeignKey('projects.id'))
    assignee_id = Column(Integer, ForeignKey('users.id'))
    reporter_id = Column(Integer, ForeignKey('users.id'))
    
    # Timestamps for when the issue was created and last updated
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        """How the issue will display when printed"""
        return f"Issue(id={self.id}, title='{self.title}', status='{self.status}')"


# --- This code is for testing the models directly ---
# You can run this file with `python models.py` to test if everything works
if __name__ == "__main__":
    # Create a temporary database for testing
    engine = create_engine('sqlite:///test_db.db')
    
    # Create all tables in the database
    Base.metadata.create_all(engine)
    
    # Set up a session to talk to the database
    Session = sessionmaker(bind=engine)
    session = Session()
    
    print("✅ Database tables created successfully!")
    print("📋 Tables created:")
    for table in Base.metadata.tables:
        print(f"  - {table}")
    
    session.close()