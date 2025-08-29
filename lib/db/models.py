# lib/db/models.py

# Import the necessary tools from SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship, sessionmaker
from lib.database import Base

class Project(Base):
    """Represents a software project that contains many issues"""
    __tablename__ = 'projects'  # This will be the table name in the database

    id = Column(Integer, primary_key=True)  # Unique ID for each project
    name = Column(String, nullable=False)      # Project name (must be unique)
    description = Column(Text)            # Short description of the project

    # This creates a relationship - one project can have many issues
    issues = relationship("Issue", back_populates="project")

    def __repr__(self):
        """How the project will display when printed"""
        return f"<Project(name={self.name})>"

class User(Base):
    """Represents a team member who can be assigned issues"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)  # Unique ID for each user
    name = Column(String, nullable=False)                   # User's full name
    email = Column(String, unique=True, nullable=False)     # User's email (must be unique)

    # Relationships: a user can be assigned many issues and can report many issues
    issues = relationship("Issue", back_populates="user")

    def __repr__(self):
        """How the user will display when printed"""
        return f"<User(name={self.name}, email={self.email})>"

class Issue(Base):
    """Represents a bug report or feature request"""
    __tablename__ = 'issues'  # Changed from 'tickets' to match your project idea!

    id = Column(Integer, primary_key=True)  # Unique ID for each issue
    title = Column(String, nullable=False)                  # Short title of the issue
    description = Column(Text)              # Detailed description of the issue
    status = Column(String, default="open") # Current status: Open, In Progress, Closed

    project_id = Column(Integer, ForeignKey("projects.id"))
    user_id = Column(Integer, ForeignKey("users.id"))  # assigned user

    project = relationship("Project", back_populates="issues")
    user = relationship("User", back_populates="issues")

    def __repr__(self):
        """How the issue will display when printed"""
        return f"<Issue(title={self.title}, status={self.status})>"


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