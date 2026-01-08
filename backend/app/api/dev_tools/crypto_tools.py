from fastapi import APIRouter, HTTPException
from app.models.dev_tools import Base64Request, HashRequest, UrlEncodeRequest
from app.services.dev.crypto_service import CryptoService

router = APIRouter(prefix="/dev/crypto", tags=["加解密工具"])


@router.post("/base64/encode")
async def base64_encode(req: Base64Request):
    try:
        result = CryptoService.base64_encode(req.content)
        return {"code": 200, "data": {"result": result}}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/base64/decode")
async def base64_decode(req: Base64Request):
    try:
        result = CryptoService.base64_decode(req.content)
        return {"code": 200, "data": {"result": result}}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/md5")
async def md5_hash(req: Base64Request):
    result = CryptoService.md5(req.content)
    return {"code": 200, "data": {"result": result}}


@router.post("/sha")
async def sha_hash(req: HashRequest):
    try:
        result = CryptoService.sha(req.content, req.algorithm)
        return {"code": 200, "data": {"result": result}}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/url/encode")
async def url_encode(req: UrlEncodeRequest):
    result = CryptoService.url_encode(req.content)
    return {"code": 200, "data": {"result": result}}


@router.post("/url/decode")
async def url_decode(req: UrlEncodeRequest):
    try:
        result = CryptoService.url_decode(req.content)
        return {"code": 200, "data": {"result": result}}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))