from typing import List
from fastapi import UploadFile
from PIL import Image
from PyPDF2 import PdfReader, PdfWriter
import io
import zipfile


class DocumentService:
    @staticmethod
    async def images_to_pdf(files: List[UploadFile]) -> bytes:
        images = []
        for file in files:
            content = await file.read()
            img = Image.open(io.BytesIO(content))
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            images.append(img)
        
        if not images:
            raise ValueError("没有有效的图片")
        
        output = io.BytesIO()
        images[0].save(output, format='PDF', save_all=True, append_images=images[1:])
        return output.getvalue()

    @staticmethod
    async def pdf_to_images(file: UploadFile) -> bytes:
        # 简化实现，实际需要使用pdf2image库
        raise NotImplementedError("PDF转图片功能需要安装poppler")

    @staticmethod
    async def pdf_merge(files: List[UploadFile]) -> bytes:
        writer = PdfWriter()
        for file in files:
            content = await file.read()
            reader = PdfReader(io.BytesIO(content))
            for page in reader.pages:
                writer.add_page(page)
        
        output = io.BytesIO()
        writer.write(output)
        return output.getvalue()