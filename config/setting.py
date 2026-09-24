
import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv(Path(__file__).resolve().parent.parent/".env")

def get_env(name: str, default:str | None = None) ->str:
    value = os.getenv(name, default)
    if not value:
        raise RuntimeError(
            f"Missing environment variable {name}. "
            "set it in your .env file (see .env.example) or in the CI environment."
        )
    return value 

ROOMS_SITE_URL = get_env("ROOMS_SITE_URL", "https://automationintesting.online")
API_BASE_URL = get_env("API_BASE_URL", "https://jsonplaceholder.typicode.com")
ADMIN_USERNAME = get_env("ADMIN_USERNAME")
ADMIN_PASSWORD = get_env("ADMIN_PASSWORD")
LOGIN_USERNAME = get_env("LOGIN_USERNAME")
LOGIN_PASSWORD = get_env("LOGIN_PASSWORD")
    