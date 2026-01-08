from fastapi import APIRouter, HTTPException
from app.models.dev_tools import TextDiffRequest, RegexTestRequest, TextStatsRequest
from app.services.dev.text_service import TextService

router = APIRouter(prefix="/dev/text", tags=["文本处理"])


@router.post("/diff")
async def text_diff(req: TextDiffRequest):
    result = TextService.diff(req.text1, req.text2)
    return {"code": 200, "data": {"diff": result}}


@router.post("/regex")
async def regex_test(req: RegexTestRequest):
    try:
        matches = TextService.regex_test(req.pattern, req.text, req.flags)
        return {"code": 200, "data": {"matches": matches}}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/stats")
async def text_stats(req: TextStatsRequest):
    result = TextService.stats(req.content)
    return {"code": 200, "data": result}