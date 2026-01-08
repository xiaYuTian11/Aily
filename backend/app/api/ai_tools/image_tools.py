from fastapi import APIRouter, UploadFile, File, HTTPException, Form
from fastapi.responses import StreamingResponse
from app.models.ai_tools import QrcodeGenerateRequest
from app.services.ai.image_service import ImageService
import io

router = APIRouter(prefix="/ai/image", tags=["图片处理"])


@router.post("/compress")
async def compress_image(
    file: UploadFile = File(...),
    quality: int = Form(default=80, ge=1, le=100)
):
    try:
        result = await ImageService.compress(file, quality)
        return StreamingResponse(
            io.BytesIO(result),
            media_type=file.content_type,
            headers={"Content-Disposition": f"attachment; filename=compressed_{file.filename}"}
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/convert")
async def convert_image(
    file: UploadFile = File(...),
    format: str = Form(default="png")
):
    try:
        result, content_type = await ImageService.convert(file, format)
        return StreamingResponse(
            io.BytesIO(result),
            media_type=content_type,
            headers={"Content-Disposition": f"attachment; filename=converted.{format}"}
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/resize")
async def resize_image(
    file: UploadFile = File(...),
    width: int = Form(...),
    height: int = Form(...)
):
    try:
        result = await ImageService.resize(file, width, height)
        return StreamingResponse(
            io.BytesIO(result),
            media_type=file.content_type,
            headers={"Content-Disposition": f"attachment; filename=resized_{file.filename}"}
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/qrcode/generate")
async def generate_qrcode(req: QrcodeGenerateRequest):
    try:
        result = ImageService.generate_qrcode(req.content, req.size)
        return StreamingResponse(
            io.BytesIO(result),
            media_type="image/png",
            headers={"Content-Disposition": "attachment; filename=qrcode.png"}
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/qrcode/decode")
async def decode_qrcode(file: UploadFile = File(...)):
    try:
        content = await ImageService.decode_qrcode(file)
        return {"code": 200, "data": {"content": content}}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))