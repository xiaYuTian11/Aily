from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.dev_tools import json_tools, crypto_tools, encoding_tools, text_tools, idcard_tools
from app.api.ai_tools import document_tools, image_tools, translate_tools, convert_tools, watermark_tools

app = FastAPI(
    title="Aily API",
    description="编程工具和AI工具API",
    version="1.0.0"
)

# CORS配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(json_tools.router, prefix="/api")
app.include_router(crypto_tools.router, prefix="/api")
app.include_router(encoding_tools.router, prefix="/api")
app.include_router(text_tools.router, prefix="/api")
app.include_router(idcard_tools.router, prefix="/api")
app.include_router(document_tools.router, prefix="/api")
app.include_router(image_tools.router, prefix="/api")
app.include_router(translate_tools.router, prefix="/api")
app.include_router(convert_tools.router, prefix="/api")
app.include_router(watermark_tools.router, prefix="/api")


@app.get("/api/health")
async def health_check():
    return {"status": "ok"}