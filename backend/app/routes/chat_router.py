from fastapi import APIRouter

from app.services import chat_service

router = APIRouter()


@router.get("/roomnames")
async def get_roomnames() -> dict[str, list[str]]:
    return chat_service.get_roomnames()
