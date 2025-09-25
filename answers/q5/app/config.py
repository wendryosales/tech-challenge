from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    secret_key: str = "dev-secret"
    password_length: int = 12

    model_config = ConfigDict(env_file=".env")


settings = Settings()
