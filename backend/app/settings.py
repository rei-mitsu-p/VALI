from os import environ

from dotenv import load_dotenv

load_dotenv()

FRONT_URL: str = environ.get("FRONT_URL", "")

REDIS_HOST: str = environ.get("REDIS_HOST", "localhost")
REDIS_PORT: int = int(environ.get("REDIS_PORT", 6379))
REDIS_USERNAME: str = environ.get("REDIS_USERNAME", "")
REDIS_PASSWORD: str = environ.get("REDIS_PASSWORD", "")
