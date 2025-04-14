from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.settings import FRONT_URL
from app.routes.router import router

app = FastAPI(title="VALI API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONT_URL],
    allow_credentials=True,
    allow_methods=["*"],
)
app.include_router(router)
