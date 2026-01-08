# API接口文档

## 基础信息
- 基础路径: `/api`
- 响应格式: `{ "code": 200, "message": "success", "data": {} }`

---

## 一、编程工具 (Dev Tools)

### 1.1 JSON工具

#### POST /dev/json/format - JSON格式化
```json
// Request
{ "content": "{\"name\":\"test\"}", "indent": 2 }
// Response
{ "code": 200, "data": { "result": "{\n  \"name\": \"test\"\n}" } }
```

#### POST /dev/json/compress - JSON压缩
```json
// Request
{ "content": "{\n  \"name\": \"test\"\n}" }
// Response
{ "code": 200, "data": { "result": "{\"name\":\"test\"}" } }
```

#### POST /dev/json/validate - JSON校验
```json
// Request
{ "content": "{\"name\":\"test\"}" }
// Response
{ "code": 200, "data": { "valid": true, "error": null } }
```

### 1.2 加解密工具

#### POST /dev/crypto/base64/encode - Base64编码
```json
// Request
{ "content": "Hello World" }
// Response
{ "code": 200, "data": { "result": "SGVsbG8gV29ybGQ=" } }
```

#### POST /dev/crypto/base64/decode - Base64解码
```json
// Request
{ "content": "SGVsbG8gV29ybGQ=" }
// Response
{ "code": 200, "data": { "result": "Hello World" } }
```

#### POST /dev/crypto/md5 - MD5加密
```json
// Request
{ "content": "Hello World" }
// Response
{ "code": 200, "data": { "result": "b10a8db164e0754105b7a99be72e3fe5" } }
```

#### POST /dev/crypto/sha - SHA加密
```json
// Request
{ "content": "Hello World", "algorithm": "sha256" }
// Response
{ "code": 200, "data": { "result": "a591a6d40bf..." } }
```

#### POST /dev/crypto/url/encode - URL编码
```json
// Request
{ "content": "hello world" }
// Response
{ "code": 200, "data": { "result": "hello%20world" } }
```

#### POST /dev/crypto/url/decode - URL解码
```json
// Request
{ "content": "hello%20world" }
// Response
{ "code": 200, "data": { "result": "hello world" } }
```

### 1.3 编码转换

#### POST /dev/encoding/base-convert - 进制转换
```json
// Request
{ "value": "255", "from_base": 10, "to_base": 16 }
// Response
{ "code": 200, "data": { "result": "ff" } }
```

#### POST /dev/encoding/timestamp - 时间戳转换
```json
// Request
{ "timestamp": 1704672000, "format": "%Y-%m-%d %H:%M:%S" }
// Response
{ "code": 200, "data": { "result": "2024-01-08 00:00:00" } }
```

#### POST /dev/encoding/unicode - Unicode转换
```json
// Request
{ "content": "你好", "direction": "to_unicode" }
// Response
{ "code": 200, "data": { "result": "\\u4f60\\u597d" } }
```

### 1.4 文本处理

#### POST /dev/text/diff - 文本对比
```json
// Request
{ "text1": "hello", "text2": "hallo" }
// Response
{ "code": 200, "data": { "diff": "..." } }
```

#### POST /dev/text/regex - 正则测试
```json
// Request
{ "pattern": "\\d+", "text": "abc123def", "flags": "" }
// Response
{ "code": 200, "data": { "matches": ["123"] } }
```

#### POST /dev/text/stats - 字符统计
```json
// Request
{ "content": "Hello World" }
// Response
{ "code": 200, "data": { "chars": 11, "words": 2, "lines": 1 } }
```

---

## 二、AI工具 (AI Tools)

### 2.1 文档转换

#### POST /ai/document/images-to-pdf - 图片转PDF
```
Content-Type: multipart/form-data
files: [图片文件...]
Response: application/pdf (文件流)
```

#### POST /ai/document/pdf-to-images - PDF转图片
```
Content-Type: multipart/form-data
file: PDF文件
Response: application/zip (图片压缩包)
```

#### POST /ai/document/pdf-merge - PDF合并
```
Content-Type: multipart/form-data
files: [PDF文件...]
Response: application/pdf
```

### 2.2 图片处理

#### POST /ai/image/compress - 图片压缩
```
Content-Type: multipart/form-data
file: 图片文件
quality: 80 (可选,1-100)
Response: image/*
```

#### POST /ai/image/convert - 图片格式转换
```
Content-Type: multipart/form-data
file: 图片文件
format: png|jpg|webp
Response: image/*
```

#### POST /ai/image/resize - 图片缩放
```
Content-Type: multipart/form-data
file: 图片文件
width: 800
height: 600
Response: image/*
```

#### POST /ai/image/qrcode/generate - 二维码生成
```json
// Request
{ "content": "https://example.com", "size": 300 }
// Response: image/png
```

#### POST /ai/image/qrcode/decode - 二维码识别
```
Content-Type: multipart/form-data
file: 二维码图片
Response: { "code": 200, "data": { "content": "https://..." } }
```

### 2.3 AI处理

#### POST /ai/ocr/recognize - OCR文字识别
```
Content-Type: multipart/form-data
file: 图片文件
Response: { "code": 200, "data": { "text": "识别的文字..." } }
```

---

## 三、错误码

| code | 说明 |
|------|------|
| 200 | 成功 |
| 400 | 请求参数错误 |
| 413 | 文件过大 |
| 500 | 服务器错误 |