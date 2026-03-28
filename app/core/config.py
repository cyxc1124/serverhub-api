from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    PROJECT_NAME: str = "ServerHub"
    VERSION: str = "0.1.0"
    DEBUG: bool = True

    # Database
    DB_TYPE: str = "postgresql"  # mysql | mariadb | postgresql
    DB_HOST: str = "127.0.0.1"
    DB_PORT: int = 5432
    DB_USER: str = "serverhub"
    DB_PASSWORD: str = "serverhub_secret"
    DB_NAME: str = "serverhub"

    # JWT
    SECRET_KEY: str = "change-this-to-a-random-secret-key"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    ALGORITHM: str = "HS256"

    # CORS
    CORS_ORIGINS: str = "http://localhost:5173,http://localhost:3000"

    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    @property
    def cors_origins_list(self) -> List[str]:
        return [origin.strip() for origin in self.CORS_ORIGINS.split(",")]

    @property
    def database_url(self) -> str:
        db_type = self.DB_TYPE.lower()
        if db_type in ("mysql", "mariadb"):
            return (
                f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}"
                f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
            )
        elif db_type == "postgresql":
            return (
                f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}"
                f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
            )
        raise ValueError(f"Unsupported DB_TYPE: {db_type}")

    @property
    def async_database_url(self) -> str:
        db_type = self.DB_TYPE.lower()
        if db_type in ("mysql", "mariadb"):
            return (
                f"mysql+aiomysql://{self.DB_USER}:{self.DB_PASSWORD}"
                f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
            )
        elif db_type == "postgresql":
            return (
                f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}"
                f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
            )
        raise ValueError(f"Unsupported DB_TYPE: {db_type}")

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
