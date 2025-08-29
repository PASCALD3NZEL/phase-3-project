from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from lib.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    issues = relationship("Issue", back_populates="user")

    def __repr__(self):
        return f"<User id={self.id} name={self.name} email={self.email}>"

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)

    issues = relationship("Issue", back_populates="project")

    def __repr__(self):
        return f"<Project id={self.id} name={self.name}>"

class Issue(Base):
    __tablename__ = "issues"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    status = Column(String, default="Open")

    project_id = Column(Integer, ForeignKey("projects.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    project = relationship("Project", back_populates="issues")
    user = relationship("User", back_populates="issues")

    def __repr__(self):
        return f"<Issue id={self.id} title={self.title} status={self.status}>"
