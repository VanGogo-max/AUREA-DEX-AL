from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from backend.api import public, strategies, payments, admin
import backend.config as config

app = FastAPI(title=config.APP_NAME)

# include routers
app.include_router(public.router, prefix="", tags=["public"])
app.include_router(strategies.router, prefix="/api/strategies", tags=["strategies"])
app.include_router(payments.router, prefix="/api/payments", tags=["payments"])
app.include_router(admin.router, prefix="/api/admin", tags=["admin"])

# serve frontend static (for simple deploy)
app.mount("/static", StaticFiles(directory="../frontend/static"), name="static")
app.mount("/", StaticFiles(directory="../frontend", html=True), name="frontend")
