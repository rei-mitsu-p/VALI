from fastapi import APIRouter
from app.services import tarot_service

router = APIRouter()


@router.get("/card", summary="カード取得API")
async def get_card():
    return tarot_service.get_card()
