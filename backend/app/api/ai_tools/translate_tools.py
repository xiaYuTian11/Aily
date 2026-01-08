from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ai.translate_service import translate

router = APIRouter(prefix="/translate", tags=["翻译"])

class TranslateRequest(BaseModel):
    text: str
    source: str = "auto"
    target: str = "en"

@router.post("")
async def translate_text(req: TranslateRequest):
    result = await translate(req.text, req.source, req.target)
    return {"code": 0, "message": "success", "data": {"result": result}}