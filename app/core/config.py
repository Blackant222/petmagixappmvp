# Last modified: 2025-03-01 12:29:18 by Blackant222
try:
    from pydantic_settings import BaseSettings
except ImportError:
    from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "PetMagix API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Security
    SECRET_KEY: str = "super-secret-key-2025-03-01"  # Change in production
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    
    # Database
    DATABASE_URL: str = "sqlite:///./petmagix.db"
    
    # AI
    XAI_API_KEY: str = "xai-0ENHv44ZrlYuaaa4HnpImP27NijUPMR4BPbxs7xK6VeGxoI1qPFaTBmonCTI5w8UsUc042qTOsi5xoDT"
    
    # Default user
    DEFAULT_USER: str = "Blackant222"
    CURRENT_TIMESTAMP: str = "2025-03-01 12:29:18"
    
    class Config:
        case_sensitive = True

settings = Settings()