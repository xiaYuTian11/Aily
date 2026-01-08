# Aily 工具箱

一个集成编程工具和AI工具的综合性工具平台。

## 技术栈
- 后端: Python 3.11 + FastAPI
- 前端: Vue 3 + TypeScript + Element Plus
- 部署: Docker

## 快速开始

### 本地开发

```bash
# 后端
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

# 前端
cd frontend
npm install
npm run dev
```

### Docker部署

```bash
# 构建并运行
docker-compose up -d

# 或手动构建
docker build -t aily:latest .
docker run -d -p 80:80 aily:latest
```

## 功能模块

### 编程工具
- JSON格式化/压缩/校验
- Base64/URL编解码
- MD5/SHA加密
- 时间戳转换

### AI工具
- 图片转PDF
- 图片压缩
- 二维码生成/识别