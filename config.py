from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PG_HOST: str
    PG_USER: str
    PG_PASS: str
    PG_DBNAME: str

    @property
    def database_url_asyncpg(self):
        return f'postgresql+asyncpg://{self.PG_USER}:{self.PG_PASS}@{self.PG_HOST}/{self.PG_DBNAME}'

    @property
    def database_url_psycopg(self):
        return f'postgresql+psycopg://{self.PG_USER}:{self.PG_PASS}@{self.PG_HOST}/{self.PG_DBNAME}'

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
