from fastapi import APIRouter, HTTPException
from app.models.dev_tools import BaseConvertRequest, TimestampRequest, UnicodeRequest
from app.services.dev.encoding_service import EncodingService

router = APIRouter(prefix="/dev/encoding", tags=["编码转换"])


@router.post("/base-convert")
async def base_convert(req: BaseConvertRequest):
    try:
        result = EncodingService.base_convert(req.value, req.from_base, req.to_base)
        return {"code": 200, "data": {"result": result}}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/timestamp")
async def timestamp_convert(req: TimestampRequest):
    try:
        result = EncodingService.timestamp_convert(req.timestamp, req.datetime_str, req.format)
        return {"code": 200, "data": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/unicode")
async def unicode_convert(req: UnicodeRequest):
    try:
        result = EncodingService.unicode_convert(req.content, req.direction)
        return {"code": 200, "data": {"result": result}}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))