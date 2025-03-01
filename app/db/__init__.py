# Initialize the database setup and session
from app.db.base_class import Base
from app.db.session import SessionLocal, engine

# Ensure that all models are available for Alembic's autogeneration.
# Import models here from app.models to register them with Alembic migrations.
# The models themselves should not be imported here directly, 
# but are handled by Alembic through autoload mechanism.

# Example:
# from app.models import user, pet

# Create all tables in the database (if not already created)
Base.metadata.create_all(bind=engine)
