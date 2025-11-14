# copy to backend/config.py and fill values or set env vars
import os

RPC_URL = os.getenv("RPC_URL", "https://polygon-rpc.com")
POLYGON_USDT_ADDRESS = os.getenv("POLYGON_USDT_ADDRESS", "0xfee37e7e64d70f37f96c42375131abb57c1481c2")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./aurea.db")
APP_NAME = "AUREA AI"
SECRET_KEY = os.getenv("SECRET_KEY", "change_me")
