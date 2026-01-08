from fastapi import APIRouter, HTTPException
from app.models.dev_tools import JsonFormatRequest, JsonValidateResponse
from app.services.dev.json_service import JsonService

router = APIRouter(prefix="/dev/json", tags=["JSON工具"])


@router.post("/format")
async def format_json(req: JsonFormatRequest):
    try:
        result = JsonService.format(req.content, req.indent)
        return {"code": 200, "data": {"result": result}}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/compress")
async def compress_json(req: JsonFormatRequest):
    try:
        result = JsonService.compress(req.content)
        return {"code": 200, "data": {"result": result}}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/validate", response_model=None)
async def validate_json(req: JsonFormatRequest):
    valid, error = JsonService.validate(req.content)
    return {"code": 200, "data": {"valid": valid, "error": error}}