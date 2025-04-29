from socketio import AsyncNamespace

from app.redis.client import redis_client
from app.redis.util.redis_util import get_with_update_expire
from app.utils.constants import REDIS_EXPIRE_SECOND_NAME, REDIS_KEY_PREFIX_NAME

EVENT_NAME_MESSAGE = "message"


class ChatEvent(AsyncNamespace):
    def __init__(self: "ChatEvent", namespace: str) -> None:
        super().__init__(namespace)

    async def on_connect(self: "ChatEvent", sid: str, __env__: dict[str, str]) -> None:
        await self.emit(EVENT_NAME_MESSAGE, "connected", to=sid)

    async def on_disconnect(
        self: "ChatEvent", sid: str, __env__: dict[str, str]
    ) -> None:
        redis_client.delete(f"{REDIS_KEY_PREFIX_NAME}{sid}")
        await self.emit(EVENT_NAME_MESSAGE, "disconnected", to=sid)

    async def on_set_name(self: "ChatEvent", sid: str, data: dict[str, str]) -> None:
        redis_client.setex(
            f"{REDIS_KEY_PREFIX_NAME}{sid}", REDIS_EXPIRE_SECOND_NAME, data["name"]
        )

    async def on_enter_room(self: "ChatEvent", sid: str, data: dict[str, str]) -> None:
        room_name: str = data["roomName"]
        await self.enter_room(sid, room_name)
        await self.emit(
            EVENT_NAME_MESSAGE,
            f"{get_with_update_expire(f'{REDIS_KEY_PREFIX_NAME}{sid}', REDIS_EXPIRE_SECOND_NAME)} joined",
            room=room_name,
        )

    async def on_leave_room(self: "ChatEvent", sid: str, data: dict[str, str]) -> None:
        room_name: str = data["roomName"]
        await self.leave_room(sid, room_name)
        await self.emit(
            EVENT_NAME_MESSAGE,
            f"{redis_client.get(f'{REDIS_KEY_PREFIX_NAME}{sid}')} left",
            room=room_name,
        )

    async def on_send_message(
        self: "ChatEvent", sid: str, data: dict[str, str]
    ) -> None:
        await self.emit(
            EVENT_NAME_MESSAGE,
            f"{get_with_update_expire((f'{REDIS_KEY_PREFIX_NAME}{sid}'), REDIS_EXPIRE_SECOND_NAME)}: {data['message']}",
            room=data["roomName"],
        )
