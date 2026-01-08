# Aily 部署方案设计

## 一、部署方案选择

| 方案 | 描述 | 推荐场景 |
|------|------|----------|
| **单镜像部署** | 前后端打包到一个Docker镜像 | ✅ 本项目推荐 |
| **分离部署** | 前后端各自独立镜像 | 大型生产环境 |

**本项目采用单镜像方案**：一个镜像包含Nginx+FastAPI，直接推送Docker Hub即可部署。

---

## 二、架构设计

```
┌────────────────────────────────┐
│       Docker Container         │
│  ┌──────────────────────────┐ │
│  │    Nginx (:80)           │ │
│  │  - 静态文件 (Vue dist)   │ │
│  │  - 反向代理 /api -> 8000 │ │
│  └────────────┬─────────────┘ │
│               │               │
│  ┌────────────▼─────────────┐ │
│  │  FastAPI (Uvicorn:8000)  │ │
│  └──────────────────────────┘ │
└────────────────────────────────┘
```

---

## 三、快速使用命令

```bash
# 构建镜像
docker build -t aily:latest .

# 本地运行
docker run -d -p 80:80 --name aily aily:latest

# 推送到Docker Hub
docker tag aily:latest yourusername/aily:latest
docker push yourusername/aily:latest

# 服务器拉取运行
docker pull yourusername/aily:latest
docker run -d -p 80:80 --name aily yourusername/aily:latest
```

---

## 四、Makefile快捷命令

项目根目录提供Makefile，简化操作：

```bash
make dev        # 本地开发（前后端分别启动）
make build      # 构建Docker镜像
make run        # 运行容器
make push       # 推送到Docker Hub
make deploy     # 一键构建+推送
```

---

## 五、配置文件说明

详细配置文件见：
- `Dockerfile` - 多阶段构建配置
- `docker/nginx.conf` - Nginx配置
- `docker/supervisord.conf` - 进程管理
- `docker-compose.yml` - 本地开发编排
- `docker-compose.prod.yml` - 生产部署编排

---

## 六、CI/CD集成（可选）

支持GitHub Actions自动构建推送：

```yaml
# .github/workflows/docker.yml
name: Build and Push Docker
on:
  push:
    branches: [main]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Build and push
        run: |
          docker build -t ${{ secrets.DOCKER_USERNAME }}/aily:latest .
          echo ${{ secrets.DOCKER_PASSWORD }} | docker login -u ${{ secrets.DOCKER_USERNAME }} --password-stdin
          docker push ${{ secrets.DOCKER_USERNAME }}/aily:latest