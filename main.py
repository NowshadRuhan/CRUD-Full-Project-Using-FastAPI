# from typing import Union
# from fastapi import FastAPI
# from routes.index import our_user

# app = FastAPI()
# app.include_router(our_user)

from fastapi import FastAPI
from token import OP
from typing import Optional

import uvicorn
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

from routes.index import our_user

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = "http://localhost:3000/",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(our_user)

