from PIL import Image, ImageDraw, ImageFont
import io

def add_watermark(img_bytes: bytes, text: str, opacity: int = 50, position: str = "center") -> bytes:
    img = Image.open(io.BytesIO(img_bytes)).convert("RGBA")
    txt_layer = Image.new("RGBA", img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt_layer)
    
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    
    positions = {
        "center": ((img.width - tw) // 2, (img.height - th) // 2),
        "top-left": (10, 10),
        "top-right": (img.width - tw - 10, 10),
        "bottom-left": (10, img.height - th - 10),
        "bottom-right": (img.width - tw - 10, img.height - th - 10),
    }
    x, y = positions.get(position, positions["center"])
    
    alpha = int(255 * opacity / 100)
    draw.text((x, y), text, font=font, fill=(255, 255, 255, alpha))
    
    result = Image.alpha_composite(img, txt_layer).convert("RGB")
    output = io.BytesIO()
    result.save(output, "PNG")
    return output.getvalue()