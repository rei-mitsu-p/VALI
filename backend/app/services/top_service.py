from app.redis.client import redisClient

TOP_PV_KEY = "top_pv"


def get_message():
    redisClient.incr(TOP_PV_KEY)
    return {"message": f"サイト総閲覧数 {redisClient.get(TOP_PV_KEY)} 回"}
