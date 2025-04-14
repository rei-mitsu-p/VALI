from fastapi import APIRouter
from app.routes.tarot_router import router as tarot_router
from app.services import top_service

router = APIRouter()


@router.get("/", summary="TOP画面表示用メッセージ取得API", tags=["TOP"])
async def top_message():
    return top_service.get_message()


router.include_router(tarot_router, prefix="/tarot", tags=["TALOT"])
