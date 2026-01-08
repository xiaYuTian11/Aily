from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from typing import List
from app.services.ai.document_service import DocumentService
import io

router = APIRouter(prefix="/ai/document", tags=["文档转换"])


@router.post("/images-to-pdf")
async def images_to_pdf(files: List[UploadFile] = File(...)):
    try:
        pdf_bytes = await DocumentService.images_to_pdf(files)
        return StreamingResponse(
            io.BytesIO(pdf_bytes),
            media_type="application/pdf",
            headers={"Content-Disposition": "attachment; filename=output.pdf"}
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/pdf-to-images")
async def pdf_to_images(file: UploadFile = File(...)):
    try:
        zip_bytes = await DocumentService.pdf_to_images(file)
        return StreamingResponse(
            io.BytesIO(zip_bytes),
            media_type="application/zip",
            headers={"Content-Disposition": "attachment; filename=images.zip"}
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/pdf-merge")
async def pdf_merge(files: List[UploadFile] = File(...)):
    try:
        pdf_bytes = await DocumentService.pdf_merge(files)
        return StreamingResponse(
            io.BytesIO(pdf_bytes),
            media_type="application/pdf",
            headers={"Content-Disposition": "attachment; filename=merged.pdf"}
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))