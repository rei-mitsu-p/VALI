import socketio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.events.chat_event import ChatEvent
from app.routes.chat_router import router as chat_router
from app.settings import FRONT_URL
from app.socketio_instance import socketio_instance

fastapi_app = FastAPI(title="VALI API")
fastapi_app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONT_URL],
    allow_credentials=True,
    allow_methods=["*"],
)


@fastapi_app.api_route("/", methods=["GET", "HEAD"], tags=["INDEX"])
async def check_health() -> dict[str, str]:
    return {"result": "OK"}


fastapi_app.include_router(chat_router, prefix="/chat", tags=["CHAT"])

socketio_instance.register_namespace(ChatEvent("/chat"))

app = socketio.ASGIApp(socketio_instance, other_asgi_app=fastapi_app)
