from pydantic_settings import BaseSettings


class configEnv(BaseSettings):
    OPENAI_API_KEY: str
    OPENAI_BASE_URL: str

env = configEnv()
