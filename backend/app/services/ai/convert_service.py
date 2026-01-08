import io
import os
import tempfile
from PIL import Image
from PyPDF2 import PdfReader
import fitz  # PyMuPDF

def pdf_to_images(pdf_bytes: bytes) -> list:
    """PDF转图片"""
    images = []
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    for page in doc:
        pix = page.get_pixmap(dpi=150)
        img_bytes = pix.tobytes("png")
        images.append(img_bytes)
    doc.close()
    return images

def images_to_pdf(image_files: list) -> bytes:
    """图片转PDF"""
    imgs = []
    for f in image_files:
        img = Image.open(io.BytesIO(f))
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        imgs.append(img)
    output = io.BytesIO()
    imgs[0].save(output, "PDF", save_all=True, append_images=imgs[1:])
    return output.getvalue()