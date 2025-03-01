from sqlalchemy import create_engine
from app.core.config import settings
from app.models.base import Base
from app.models.user import User  # Make sure to import all models here
from app.models.pet import Pet
from app.models.habit import Habit
from app.models.metric import Metric
from app.models.reward import Reward

def init_db():
    engine = create_engine(settings.DATABASE_URL)
    Base.metadata.drop_all(bind=engine)  # Drop existing tables
    Base.metadata.create_all(bind=engine)  # Create all tables in one go

if __name__ == "__main__":
    init_db()
