from typing import Optional, List
from pydantic import BaseModel, Field


# JSON工具
class JsonFormatRequest(BaseModel):
    content: str = Field(..., description="JSON字符串")
    indent: int = Field(default=2, ge=0, le=8, description="缩进空格数")


class JsonValidateResponse(BaseModel):
    valid: bool
    error: Optional[str] = None


# 加解密工具
class Base64Request(BaseModel):
    content: str = Field(..., description="待编码/解码的内容")


class HashRequest(BaseModel):
    content: str = Field(..., description="待加密的内容")
    algorithm: str = Field(default="md5", description="算法: md5/sha1/sha256/sha512")


class UrlEncodeRequest(BaseModel):
    content: str = Field(..., description="待编码/解码的内容")


# 编码转换
class BaseConvertRequest(BaseModel):
    value: str = Field(..., description="待转换的值")
    from_base: int = Field(..., ge=2, le=36, description="源进制")
    to_base: int = Field(..., ge=2, le=36, description="目标进制")


class TimestampRequest(BaseModel):
    timestamp: Optional[int] = Field(None, description="时间戳")
    datetime_str: Optional[str] = Field(None, description="日期时间字符串")
    format: str = Field(default="%Y-%m-%d %H:%M:%S", description="格式")


class UnicodeRequest(BaseModel):
    content: str = Field(..., description="内容")
    direction: str = Field(default="to_unicode", description="to_unicode/from_unicode")


# 文本处理
class TextDiffRequest(BaseModel):
    text1: str = Field(..., description="文本1")
    text2: str = Field(..., description="文本2")


class RegexTestRequest(BaseModel):
    pattern: str = Field(..., description="正则表达式")
    text: str = Field(..., description="测试文本")
    flags: str = Field(default="", description="标志: i/m/s")


class TextStatsRequest(BaseModel):
    content: str = Field(..., description="文本内容")


class TextStatsResponse(BaseModel):
    chars: int
    chars_no_space: int
    words: int
    lines: int