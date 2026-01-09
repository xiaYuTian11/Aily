# 阶段1: 构建前端
FROM node:18-alpine AS frontend-builder
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm ci --registry=https://registry.npmmirror.com
COPY frontend/ ./
RUN npm run build

# 阶段2: 最终镜像
FROM python:3.11-slim
RUN apt-get update && apt-get install -y --no-install-recommends nginx supervisor libzbar0 && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY backend/ ./backend/
COPY --from=frontend-builder /app/frontend/dist /usr/share/nginx/html
COPY docker/nginx.conf /etc/nginx/nginx.conf
COPY docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
EXPOSE 80
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]