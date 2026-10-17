from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # machine learning variables with default values
    top_k_elements: int = 5
    threshold: float = 0.5

    # database login
    db_name : str = "ai_wiki_db"
    db_user : str = "postgres"
    db_password : str = ""

    # read the envoironment variables from the .env file
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()

