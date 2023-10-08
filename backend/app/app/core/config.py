from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    postgres_server: str
    postgres_host: str
    postgres_port: str
    postgres_user: str
    postgres_password: str

    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    SQLALCHEMY_DATABASE_URI = f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_server}"

    model_config = SettingsConfigDict(env_file="../../../../.env")


settings = Settings()
