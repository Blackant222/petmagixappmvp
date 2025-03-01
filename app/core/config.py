from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional
import os
from pathlib import Path
import secrets

class Settings(BaseSettings):
    # Project Settings
    PROJECT_NAME: str = "PetMagix API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Security
    SECRET_KEY: str = secrets.token_urlsafe(32)  # Generate a new secret key using secrets
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    
    # Database settings
    DATABASE_URL: Optional[str] = "sqlite:///petmagix.db"  # Optional, can be overridden
    
    # JWT Settings (Legacy)
    # SECRET_KEY: str = "your-secret-key-here"
    # ALGORITHM: str = "HS256"
    # ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # AI Settings
    XAI_API_KEY: str = "xai-0ENHv44ZrlYuaaa4HnpImP27NijUPMR4BPbxs7xK6VeGxoI1qPFaTBmonCTI5w8UsUc042qTOsi5xoDT"
    
    # Default user settings
    DEFAULT_USER: str = "Blackant222"
    CURRENT_TIMESTAMP: str = "2025-03-01 13:32:37"

    # Define configuration for environment variables
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True
    )
    
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return self.DATABASE_URL

settings = Settings()
