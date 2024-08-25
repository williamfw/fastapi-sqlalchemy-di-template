from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    SQLALCHEMY_DATABASE_URL: str
    ECHO_SQL: bool = True
    
settings = Settings()   # type: ignore
