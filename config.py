import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")


class BaseConfig:
    """Configuración común del ejercicio didáctico."""

    SECRET_KEY = os.getenv("SECRET_KEY", "development-only-change-me")
    DATA_MODE = os.getenv("DATA_MODE", "memory").lower()

    # Se inicializará en la sesión 2 cuando DATA_MODE cambie a database.
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg://taller_user:taller_password@localhost:5432/taller_store",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"


class TestConfig(BaseConfig):
    TESTING = True
    SECRET_KEY = "test-secret-key"
    DATA_MODE = "memory"
    WTF_CSRF_ENABLED = False
