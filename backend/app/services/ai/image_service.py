from fastapi import UploadFile
from PIL import Image
import qrcode
from pyzbar.pyzbar import decode
import io
from typing import Tuple


class ImageService:
    @staticmethod
    async def compress(file: UploadFile, quality: int) -> bytes:
        content = await file.read()
        img = Image.open(io.BytesIO(content))
        output = io.BytesIO()
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        img.save(output, format='JPEG', quality=quality, optimize=True)
        return output.getvalue()

    @staticmethod
    async def convert(file: UploadFile, format: str) -> Tuple[bytes, str]:
        content = await file.read()
        img = Image.open(io.BytesIO(content))
        output = io.BytesIO()
        
        format_map = {
            'png': ('PNG', 'image/png'),
            'jpg': ('JPEG', 'image/jpeg'),
            'jpeg': ('JPEG', 'image/jpeg'),
            'webp': ('WEBP', 'image/webp'),
            'gif': ('GIF', 'image/gif'),
        }
        
        if format not in format_map:
            raise ValueError(f"不支持的格式: {format}")
        
        pil_format, content_type = format_map[format]
        if pil_format == 'JPEG' and img.mode == 'RGBA':
            img = img.convert('RGB')
        img.save(output, format=pil_format)
        return output.getvalue(), content_type

    @staticmethod
    async def resize(file: UploadFile, width: int, height: int) -> bytes:
        content = await file.read()
        img = Image.open(io.BytesIO(content))
        img = img.resize((width, height), Image.Resampling.LANCZOS)
        output = io.BytesIO()
        img.save(output, format=img.format or 'PNG')
        return output.getvalue()

    @staticmethod
    def generate_qrcode(content: str, size: int) -> bytes:
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(content)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img = img.resize((size, size))
        output = io.BytesIO()
        img.save(output, format='PNG')
        return output.getvalue()

    @staticmethod
    async def decode_qrcode(file: UploadFile) -> str:
        content = await file.read()
        img = Image.open(io.BytesIO(content))
        decoded = decode(img)
        if not decoded:
            raise ValueError("未识别到二维码")
        return decoded[0].data.decode('utf-8')