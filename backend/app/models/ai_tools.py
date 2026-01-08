from pydantic import BaseModel, Field


class QrcodeGenerateRequest(BaseModel):
    content: str = Field(..., description="二维码内容")
    size: int = Field(default=300, ge=100, le=1000, description="尺寸")