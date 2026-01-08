# Aily 工具箱 - 需求设计文档

## 一、项目概述

### 1.1 项目名称
**Aily** - 一个集成编程工具和AI工具的综合性工具箱

### 1.2 项目目标
为开发者和普通用户提供一个功能丰富、易于使用的在线工具平台，涵盖编程开发常用工具和AI智能处理工具两大类。

### 1.3 技术栈
- **后端**: Python 3.10+ (FastAPI框架)
- **前端**: Vue 3 + TypeScript + Element Plus
- **数据库**: SQLite (轻量级存储) / Redis (缓存)
- **部署**: Docker

---

## 二、功能模块设计

### 2.1 编程工具类 (Developer Tools)

#### 2.1.1 JSON工具
| 功能 | 描述 | 优先级 |
|------|------|--------|
| JSON格式化 | 美化JSON字符串，支持缩进设置 | P0 |
| JSON压缩 | 移除空格和换行，压缩JSON | P0 |
| JSON校验 | 验证JSON格式是否正确，显示错误位置 | P0 |
| JSON转换 | JSON ↔ XML、JSON ↔ YAML、JSON ↔ CSV | P1 |
| JSON路径查询 | 支持JSONPath表达式查询 | P2 |
| JSON对比 | 对比两个JSON的差异 | P2 |

#### 2.1.2 加解密工具
| 功能 | 描述 | 优先级 |
|------|------|--------|
| Base64编解码 | Base64编码/解码，支持文件 | P0 |
| URL编解码 | URL编码/解码 | P0 |
| MD5加密 | 生成MD5哈希值 | P0 |
| SHA加密 | SHA1/SHA256/SHA512哈希 | P0 |
| AES加解密 | AES对称加密/解密 | P1 |
| RSA加解密 | RSA非对称加密/解密 | P1 |
| JWT解析 | 解析JWT Token内容 | P1 |
| 密码生成器 | 生成随机安全密码 | P2 |

#### 2.1.3 编码转换工具
| 功能 | 描述 | 优先级 |
|------|------|--------|
| 进制转换 | 二进制/八进制/十进制/十六进制互转 | P0 |
| Unicode转换 | Unicode ↔ 中文/字符 | P0 |
| ASCII转换 | ASCII码 ↔ 字符 | P0 |
| 时间戳转换 | 时间戳 ↔ 日期时间格式 | P0 |
| 颜色转换 | HEX ↔ RGB ↔ HSL | P1 |

#### 2.1.4 文本处理工具
| 功能 | 描述 | 优先级 |
|------|------|--------|
| 文本对比 | Diff对比两段文本差异 | P0 |
| 正则测试 | 正则表达式在线测试 | P0 |
| 字符统计 | 统计字符数、单词数、行数 | P0 |
| 大小写转换 | 大写/小写/首字母大写/驼峰等 | P1 |
| 文本去重 | 按行去重 | P1 |
| 文本排序 | 按行排序（升序/降序/随机） | P1 |

#### 2.1.5 代码工具
| 功能 | 描述 | 优先级 |
|------|------|--------|
| 代码格式化 | 支持多种语言代码格式化 | P1 |
| SQL格式化 | SQL语句美化 | P1 |
| Cron表达式 | Cron表达式解析和生成 | P2 |
| 正则生成器 | 可视化生成正则表达式 | P2 |

---

### 2.2 AI工具类 (AI Tools)

#### 2.2.1 文档转换工具
| 功能 | 描述 | 优先级 |
|------|------|--------|
| 图片转PDF | 多张图片合并为PDF | P0 |
| PDF转图片 | PDF每页转为图片 | P0 |
| 图片转PPT | 图片批量生成PPT | P1 |
| Word转PDF | Word文档转PDF | P1 |
| PDF合并 | 多个PDF合并为一个 | P1 |
| PDF拆分 | 一个PDF拆分为多个 | P1 |
| Markdown转PDF | Markdown渲染为PDF | P2 |

#### 2.2.2 图片处理工具
| 功能 | 描述 | 优先级 |
|------|------|--------|
| 图片压缩 | 压缩图片大小，保持质量 | P0 |
| 图片格式转换 | PNG/JPG/WEBP/GIF互转 | P0 |
| 图片裁剪 | 在线裁剪图片 | P1 |
| 图片水印 | 添加文字/图片水印 | P1 |
| 图片拼接 | 多图横向/纵向拼接 | P1 |
| 图片Base64 | 图片与Base64互转 | P1 |
| 二维码生成 | 生成二维码图片 | P0 |
| 二维码识别 | 识别二维码内容 | P1 |

#### 2.2.3 AI智能处理
| 功能 | 描述 | 优先级 |
|------|------|--------|
| OCR文字识别 | 图片中提取文字 | P0 |
| 图片背景移除 | AI去除图片背景 | P1 |
| 图片超分辨率 | AI放大图片清晰度 | P2 |
| 智能抠图 | AI智能抠图 | P2 |

#### 2.2.4 音视频工具
| 功能 | 描述 | 优先级 |
|------|------|--------|
| 音频格式转换 | MP3/WAV/FLAC等互转 | P2 |
| 视频转GIF | 视频片段转GIF | P2 |
| 音频提取 | 从视频中提取音频 | P2 |

---

## 三、项目结构设计

```
Aily/
├── backend/                    # Python后端
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py            # FastAPI入口
│   │   ├── config.py          # 配置文件
│   │   ├── api/               # API路由
│   │   │   ├── __init__.py
│   │   │   ├── dev_tools/     # 编程工具API
│   │   │   │   ├── json_tools.py
│   │   │   │   ├── crypto_tools.py
│   │   │   │   ├── encoding_tools.py
│   │   │   │   └── text_tools.py
│   │   │   └── ai_tools/      # AI工具API
│   │   │       ├── document_tools.py
│   │   │       ├── image_tools.py
│   │   │       └── ocr_tools.py
│   │   ├── services/          # 业务逻辑层
│   │   │   ├── dev/
│   │   │   └── ai/
│   │   ├── models/            # 数据模型
│   │   └── utils/             # 工具函数
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/                   # Vue前端
│   ├── src/
│   │   ├── main.ts
│   │   ├── App.vue
│   │   ├── router/            # 路由配置
│   │   ├── views/             # 页面组件
│   │   │   ├── DevTools/      # 编程工具页面
│   │   │   └── AITools/       # AI工具页面
│   │   ├── components/        # 公共组件
│   │   ├── api/               # API请求
│   │   ├── stores/            # Pinia状态管理
│   │   └── styles/            # 样式文件
│   ├── package.json
│   └── vite.config.ts
│
├── docs/                       # 文档
│   └── requirements.md
├── docker-compose.yml
└── README.md
```

---

## 四、API设计规范

### 4.1 基础规范
- RESTful风格
- 统一响应格式：
```json
{
  "code": 200,
  "message": "success",
  "data": {}
}
```

### 4.2 API示例

#### JSON格式化
```
POST /api/dev/json/format
Request:
{
  "content": "{\"name\":\"test\"}",
  "indent": 2
}
Response:
{
  "code": 200,
  "data": {
    "result": "{\n  \"name\": \"test\"\n}"
  }
}
```

#### 图片转PDF
```
POST /api/ai/document/images-to-pdf
Content-Type: multipart/form-data
Request: files[] (多个图片文件)
Response: PDF文件流
```

---

## 五、开发计划

### 第一阶段 (Week 1-2) - 基础框架
- [ ] 搭建后端FastAPI项目结构
- [ ] 搭建前端Vue3项目结构
- [ ] 实现基础布局和路由
- [ ] 完成JSON工具模块

### 第二阶段 (Week 3-4) - 编程工具
- [ ] 完成加解密工具模块
- [ ] 完成编码转换工具模块
- [ ] 完成文本处理工具模块

### 第三阶段 (Week 5-6) - AI工具
- [ ] 完成图片处理工具模块
- [ ] 完成文档转换工具模块
- [ ] 完成OCR文字识别

### 第四阶段 (Week 7-8) - 优化部署
- [ ] 性能优化
- [ ] Docker部署配置
- [ ] 文档完善

---

## 六、技术要点

### 6.1 后端关键依赖
```
fastapi          # Web框架
uvicorn          # ASGI服务器
python-multipart # 文件上传
pillow           # 图片处理
pypdf2           # PDF处理
python-pptx      # PPT处理
pycryptodome     # 加密算法
paddleocr        # OCR识别(可选)
```

### 6.2 前端关键依赖
```
vue@3            # 前端框架
vue-router       # 路由
pinia            # 状态管理
element-plus    # UI组件库
axios            # HTTP请求
monaco-editor    # 代码编辑器
```

---

## 七、注意事项

1. **文件大小限制**: 上传文件限制在50MB以内
2. **并发处理**: AI工具需要考虑异步处理和队列
3. **安全性**: 加解密工具不存储用户数据，所有处理在内存中完成
4. **错误处理**: 统一的错误码和错误信息
5. **日志记录**: 关键操作需要记录日志

---

## 八、扩展规划

未来可扩展功能：
- 用户系统（收藏工具、历史记录）
- API开放平台
- 更多AI能力集成（ChatGPT、图像生成等）
- 移动端适配