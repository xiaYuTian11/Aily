# 后端代码规范

## 一、技术栈
Python 3.11 + FastAPI + Uvicorn + Pydantic

## 二、目录结构
```
backend/app/
├── main.py           # 入口
├── config.py         # 配置
├── api/              # 路由
│   ├── dev_tools/    # 编程工具
│   └── ai_tools/     # AI工具
├── services/         # 业务逻辑
├── models/           # 数据模型
└── utils/            # 工具函数
```

## 三、命名规范
| 类型 | 规范 | 示例 |
|------|------|------|
| 文件 | snake_case | `json_tools.py` |
| 类 | PascalCase | `JsonService` |
| 函数/变量 | snake_case | `format_json` |
| 常量 | UPPER_SNAKE | `MAX_SIZE` |

## 四、Pydantic模型
```python
from pydantic import BaseModel, Field

class JsonFormatRequest(BaseModel):
    content: str = Field(..., description="JSON字符串")
    indent: int = Field(default=2, ge=0, le=8)

class ApiResponse(BaseModel):
    code: int = 200
    message: str = "success"
    data: dict = None
```

## 五、路由规范
```python
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/dev/json", tags=["JSON工具"])

@router.post("/format")
async def format_json(req: JsonFormatRequest):
    try:
        result = JsonService.format(req.content, req.indent)
        return {"code": 200, "data": {"result": result}}
    except Exception as e:
        raise HTTPException(400, str(e))
```

## 六、Service层
```python
import json

class JsonService:
    @staticmethod
    def format(content: str, indent: int = 2) -> str:
        data = json.loads(content)
        return json.dumps(data, indent=indent, ensure_ascii=False)
```

## 七、异常处理
```python
from fastapi import Request
from fastapi.responses import JSONResponse

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"code": 500, "message": str(exc), "data": None}
    )
```

## 八、依赖配置
```txt
# requirements.txt
fastapi>=0.104.0
uvicorn[standard]>=0.24.0
python-multipart>=0.0.6
pydantic>=2.5.0
pillow>=10.0.0
pypdf2>=3.0.0
pycryptodome>=3.19.0