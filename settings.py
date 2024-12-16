from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI - Test Task"

    DATABASE_URL: str | None = "sqlite:///./products.db"

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
