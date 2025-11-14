from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel
from typing import Optional, List
import uuid
from backend.storage import get_db

router = APIRouter()

class StrategyCreate(BaseModel):
    name: str
    owner: str  # wallet address
    mode: str   # "visual" or "code"
    spec: dict  = {}   # for visual: JSON AST, for code: { "lang":"python", "source":"..." }
    symbols: Optional[List[str]] = []
    timeframe: Optional[str] = "1h"
    enabled: Optional[bool] = False

# In-memory simple store for MVP (replace by DB)
_STRATEGIES = {}

@router.post("/", status_code=201)
async def create_strategy(payload: StrategyCreate):
    sid = str(uuid.uuid4())
    obj = payload.dict()
    obj.update({"id": sid})
    _STRATEGIES[sid] = obj
    return obj

@router.get("/",)
async def list_strategies(owner: Optional[str] = None):
    vals = list(_STRATEGIES.values())
    if owner:
        vals = [v for v in vals if v["owner"].lower() == owner.lower()]
    return vals

@router.get("/{strategy_id}")
async def get_strategy(strategy_id: str):
    if strategy_id not in _STRATEGIES:
        raise HTTPException(status_code=404, detail="Not found")
    return _STRATEGIES[strategy_id]

@router.post("/{strategy_id}/enable")
async def enable_strategy(strategy_id: str):
    if strategy_id not in _STRATEGIES:
        raise HTTPException(status_code=404, detail="Not found")
    _STRATEGIES[strategy_id]["enabled"] = True
    return {"status":"enabled"}

@router.post("/{strategy_id}/disable")
async def disable_strategy(strategy_id: str):
    if strategy_id not in _STRATEGIES:
        raise HTTPException(status_code=404, detail="Not found")
    _STRATEGIES[strategy_id]["enabled"] = False
    return {"status":"disabled"}

@router.post("/{strategy_id}/backtest")
async def backtest_strategy(strategy_id: str, lookback_days: int = 30):
    # TODO: hook to backtest engine
    if strategy_id not in _STRATEGIES:
        raise HTTPException(status_code=404, detail="Not found")
    # placeholder simple result
    return {"strategy_id": strategy_id, "trades": [], "pnl": 0.0}
