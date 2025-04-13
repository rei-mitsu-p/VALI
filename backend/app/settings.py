from os import environ
from dotenv import load_dotenv

load_dotenv()

FRONT_URL: str = environ.get("FRONT_URL", "")
