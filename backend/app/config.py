from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Aily"
    max_file_size: int = 50 * 1024 * 1024  # 50MB


settings = Settings()