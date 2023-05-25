from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware    
from core.config import settings
from api.api import api_router
#pipenv run uvicorn app:app --host 0.0.0.0 --port 9797 --reload

app = FastAPI(
    title=settings.PROJECT_NAME
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
    
