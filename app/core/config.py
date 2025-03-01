from pydantic_settings import BaseSettings
from typing import Optional
import secrets

class Settings(BaseSettings):
    PROJECT_NAME: str = "PetMagix API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Security
    SECRET_KEY: str = secrets.token_urlsafe(32)  # Generate a new secret key using secrets
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    
    # Database settings
    DATABASE_URL: Optional[str] = "sqlite:///petmagix.db"  # Optional, can be overridden
    
    # AI Settings
    XAI_API_KEY: str = "xai-0ENHv44ZrlYuaaa4HnpImP27NijUPMR4BPbxs7xK6VeGxoI1qPFaTBmonCTI5w8UsUc042qTOsi5xoDT"
    
    # Default user settings
    DEFAULT_USER: str = "Blackant222"
    CURRENT_TIMESTAMP: str = "2025-03-01 13:32:37"
    
    class Config:
        case_sensitive = True

settings = Settings()
