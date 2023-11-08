from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.env import config

DEBUG = config("DEBUG", cast=bool, default=False)
FRONTEND_ORIGINS = config("FRONTEND_ORIGINS", cast=lambda x: [s.strip() for s in x.split(",")], default="")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/hello-world')
def get_hello():
    return {
        'hello': 'world',
        "Debug": DEBUG,
    }
