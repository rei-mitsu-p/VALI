from fastapi import FastAPI

app: FastAPI = FastAPI(title="VALI API")


@app.get("/", summary="TOP画面表示用メッセージ取得API", tags=["TOP"])
async def top_message():
    return {"message": "Welcome to VALI!"}
