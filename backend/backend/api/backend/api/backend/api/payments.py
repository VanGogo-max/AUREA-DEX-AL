from fastapi import APIRouter
import qrcode
from io import BytesIO
from fastapi.responses import StreamingResponse
from backend.config import POLYGON_USDT_ADDRESS

router = APIRouter()

@router.get("/qr")
async def get_payment_qr():
    # generates QR for polygon USDT address (simple text payload)
    data = f"polygon:{POLYGON_USDT_ADDRESS}"
    img = qrcode.make(data)
    buf = BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")

@router.get("/check/{wallet}/{amount}")
async def check_payment(wallet: str, amount: float):
    # TODO: implement on-chain check via web3
    return {"paid": False, "required": amount}
