from fastapi import APIRouter, UploadFile, File
from fastapi.responses import Response
import zipfile
import io
from app.services.ai.convert_service import pdf_to_images, images_to_pdf

router = APIRouter(prefix="/convert", tags=["文件转换"])

@router.post("/pdf-to-images")
async def pdf_to_images_api(file: UploadFile = File(...)):
    images = pdf_to_images(await file.read())
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w') as zf:
        for i, img in enumerate(images):
            zf.writestr(f"page_{i+1}.png", img)
    return Response(buf.getvalue(), media_type="application/zip", headers={"Content-Disposition": "attachment; filename=images.zip"})

@router.post("/images-to-pdf")
async def images_to_pdf_api(files: list[UploadFile] = File(...)):
    data = [await f.read() for f in files]
    pdf = images_to_pdf(data)
    return Response(pdf, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=output.pdf"})