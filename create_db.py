from lib.database import Base, engine
from lib.db import models  # 👈 important, so User/Project/Issue classes are registered

print("Creating database tables...")
Base.metadata.create_all(engine)
print("✅ Database tables created successfully!")
