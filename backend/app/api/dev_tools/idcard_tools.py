from fastapi import APIRouter
from app.services.dev.idcard_service import generate_idcard

router = APIRouter(prefix="/idcard", tags=["身份证"])

@router.get("/generate")
async def generate():
    return {"code": 0, "message": "success", "data": generate_idcard()}