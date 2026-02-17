from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int    
    DB_NAME: str
    LLM_MODEL: str
    OLLAMA_BASE_URL: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


    @property
    def database_url(self) -> str:
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"                   

@lru_cache
def get_settings(): 
    return Settings()   