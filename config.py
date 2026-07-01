import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = "sqlite:///eduflex.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    NOMBA_ACCOUNT_ID = os.getenv("NOMBA_ACCOUNT_ID")
    NOMBA_SUB_ACCOUNT_ID = os.getenv("NOMBA_SUB_ACCOUNT_ID")

    NOMBA_CLIENT_ID = os.getenv("NOMBA_CLIENT_ID")
    NOMBA_CLIENT_SECRET = os.getenv("NOMBA_CLIENT_SECRET")