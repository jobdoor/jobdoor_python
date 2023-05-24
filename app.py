from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware    

#pipenv run uvicorn app:app --host 0.0.0.0 --port 9797 --reload

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)