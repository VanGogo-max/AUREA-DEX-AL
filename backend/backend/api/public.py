from fastapi import APIRouter, Request
import os, json
from pathlib import Path
from backend.trading_core.exchanges import get_all_exchanges

router = APIRouter()

@router.get("/api/exchanges")
async def exchanges():
    return get_all_exchanges()

@router.get("/api/translations/{lang}")
async def translations(lang: str):
    tpath = Path(__file__).parent.parent.parent / "frontend" / "translations" / f"{lang}.json"
    if tpath.exists():
        return json.loads(tpath.read_text(encoding="utf-8"))
    return {"error":"lang not found"}
