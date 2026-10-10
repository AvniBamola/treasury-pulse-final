from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    app_env: str = "development"
    database_url: str = "sqlite:///./treasurypulse.db"
    cors_origins: str = "http://localhost:5173"
settings = Settings()
