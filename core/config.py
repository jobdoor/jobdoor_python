import secrets
from typing import Any, Dict, List, Optional, Union
import os
from dotenv import load_dotenv,find_dotenv
from pydantic import AnyHttpUrl,  HttpUrl
from abc import ABC, abstractproperty

load_dotenv(find_dotenv())

class Settings(ABC):
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    PROJECT_NAME: str ='jobdoors backend'
    SQLALCHEMY_DATABASE_URI: str
    
class LocalSettings(Settings):
    SQLALCHEMY_DATABASE_URI: str= os.getenv('DATABASE_URI_LOC','')
    
class ProductionSettings(Settings):
    SQLALCHEMY_DATABASE_URI: str= os.getenv('DATABASE_URI_PROD','')

if(os.getenv('ENVIROMENT','')=='PRODUCTION'):
    settings = ProductionSettings()
else:
    settings = LocalSettings()


