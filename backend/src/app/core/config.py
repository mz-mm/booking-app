from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Booking app"

    postgres_server: str
    postgres_host: str
    postgres_port: str
    postgres_user: str
    postgres_password: str

    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    model_config = SettingsConfigDict(env_file="../../../../.env")


settings = Settings()

SQLALCHEMY_DATABASE_URI = f"postgresql://{settings.postgres_user}:{settings.postgres_password}@{settings.postgres_host}:{settings.postgres_port}/{settings.postgres_server}"
