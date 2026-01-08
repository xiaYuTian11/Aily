from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import Response
from app.services.ai.watermark_service import add_watermark

router = APIRouter(prefix="/watermark", tags=["水印"])

@router.post("/add")
async def add_watermark_api(
    file: UploadFile = File(...),
    text: str = Form(...),
    opacity: int = Form(50),
    position: str = Form("center")
):
    result = add_watermark(await file.read(), text, opacity, position)
    return Response(result, media_type="image/png", headers={"Content-Disposition": "attachment; filename=watermarked.png"})