from app.redis.client import redis_client


def get_with_update_expiration(key: str, second: int) -> str:
    redis_client.expire(key, second)
    return str(redis_client.get(key))
