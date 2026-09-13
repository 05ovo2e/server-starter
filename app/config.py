"""환경변수 설정 관리."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """애플리케이션 설정."""

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)

    app_name: str = "Server Starter"
    app_version: str = "0.1.0"
    environment: str = "development"
    debug: bool = True


settings = Settings()
