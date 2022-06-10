import os
from functools import lru_cache
from pydantic import BaseSettings


class Config(BaseSettings):
    APP_TITLE: str = 'Jeen-Yuhs Quotes'
    APP_VERSION: str = '0.1.0'
    APP_PORT: int = 5001
    DOCS_URL: str = '/api/docs'
    OPEN_API_URL: str = '/api/openapi.json'
    TWITTER_ACCESS_TOKEN: str = os.getenv('TWITTER_ACCESS_TOKEN', '')
    BACKEND_CORS_ORIGIN: list = ["*"]


@lru_cache()
def get_config():
    config = Config()
    return config
