from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PARSED_PAINTINGS_PATH: str
    SELECTED_PAINTINGS_PATH: str

    class Config:
        env_file = ".env"


config = Settings()
