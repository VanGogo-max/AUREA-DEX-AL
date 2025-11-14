from fastapi import APIRouter

router = APIRouter()

@router.get("/logs")
async def get_logs():
    # stub
    return [{"time":"2025-11-12T21:00:00","msg":"Test log"}]

@router.get("/stats")
async def get_stats():
    return {"users": 10, "strategies": 5, "payments": 3}
