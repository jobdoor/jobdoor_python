import secrets
from typing import Any, Dict, List, Optional, Union
import os
from dotenv import load_dotenv,find_dotenv
from pydantic import AnyHttpUrl,  HttpUrl

load_dotenv(find_dotenv())

print()
#os.getenv('REPORT_CONN_DRIVER','')
class Settings():
    API_V1_STR: str = "/api/v1"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    PROJECT_NAME: str ='jobdoors backend'

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: str= os.getenv('DATABASE_URI_PROD','')




settings = Settings()