from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # machine learning variables with default values
    top_k_elements: int = 5

    # read the envoironment variables from the .env file
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()

