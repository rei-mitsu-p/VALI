from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.settings import FRONT_URL

app = FastAPI(title="VALI API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONT_URL],
    allow_credentials=True,
    allow_methods=["*"],
)


@app.get("/", summary="TOP画面表示用メッセージ取得API", tags=["TOP"])
async def top_message():
    return {"message": "Welcome to VALI!"}
