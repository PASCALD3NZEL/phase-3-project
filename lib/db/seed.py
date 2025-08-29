# lib/db/seed.py

from faker import Faker
from lib.db.models import Project, User, Ticket, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random

# Setup
fake = Faker()
engine = create_engine('sqlite:///bugtracker.db')
Base.metadata.create_all(engine) # This is redundant after alembic, but safe
Session = sessionmaker(bind=engine)
session = Session()

# Clear existing data (optional, useful for testing)
print("🗑️ Clearing old data...")
session.query(Ticket).delete()
session.query(User).delete()
session.query(Project).delete()

print("🌱 Seeding the database...")

# Create Projects
projects = []
for idx in range(3):
    project = Project(
        name=fake.catch_phrase(),
        description=fake.bs()
    )
    session.add(project)
    projects.append(project)
session.commit()

# Create Users
users = []
for idx in range(5):
    user = User(
        name=fake.name(),
        email=fake.email()
    )
    session.add(user)
    users.append(user)
session.commit()

# Create Tickets
statuses = ['New', 'Open', 'In Progress', 'Resolved', 'Closed']
priorities = ['Low', 'Medium', 'High', 'Critical']

for idx in range(20):
    ticket = Ticket(
        title=fake.sentence(),
        description=fake.paragraph(nb_sentences=3),
        status=random.choice(statuses),
        priority=random.choice(priorities),
        project_id=random.choice(projects).id,
        assignee_id=random.choice(users).id,
        reporter_id=random.choice(users).id
    )
    session.add(ticket)
session.commit()

print("✅ Database seeded successfully!")
session.close()