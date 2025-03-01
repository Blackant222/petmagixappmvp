from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Create SQLite database in the current directory
DATABASE_URL = settings.DATABASE_URL
engine = create_engine(
    DATABASE_URL, 
    pool_pre_ping=True,
    connect_args={"check_same_thread": False}  # Only needed for SQLite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)