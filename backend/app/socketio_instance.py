from socketio import AsyncServer

from app.settings import FRONT_URL

socketio_instance = AsyncServer(async_mode="asgi", cors_allowed_origins=FRONT_URL)
