import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl,  HttpUrl


class Settings():
    API_V1_STR: str = "/api/v1"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    PROJECT_NAME: str ='jobdoors backend'


    POSTGRES_SERVER: str = 'postgresql://postgres:password@localhost'
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: str= 'postgresql://postgres:admin@localhost/jobdoor'




settings = Settings()