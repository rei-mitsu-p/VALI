from app.socketio_instance import socketio_instance

NAME_SPACE = "/chat"


def get_roomnames() -> dict[str, list[str]]:
    rooms_dict = socketio_instance.manager.rooms.get(NAME_SPACE, {})
    roomname_list: list[str] = []
    for key, value in rooms_dict.items():
        if key is not None and key not in value:
            roomname_list.append(key)
    return {"result": roomname_list}
