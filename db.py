from lib.database import engine, Base
# Import models so SQLAlchemy knows them before create_all
from lib import models  # noqa: F401

def main():
    # Drop and recreate for a clean slate while finishing the project.
    # If you need to preserve data, remove drop_all.
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("Tables created.")

if __name__ == "__main__":
    main()