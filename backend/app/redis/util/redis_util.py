from app.redis.client import redis_client


def get_with_update_expiration(key: str, ex: int) -> str:
    redis_client.expire(key, ex)
    return str(redis_client.get(key))
