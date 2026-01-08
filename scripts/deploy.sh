#!/bin/bash
# 部署脚本 - 构建并推送Docker镜像到Docker Hub

# 配置
DOCKER_USER="your-dockerhub-username"
IMAGE_NAME="aily"
VERSION=${1:-latest}

# 构建镜像
echo "Building image..."
docker build -t $DOCKER_USER/$IMAGE_NAME:$VERSION .
docker tag $DOCKER_USER/$IMAGE_NAME:$VERSION $DOCKER_USER/$IMAGE_NAME:latest

# 推送到Docker Hub
echo "Pushing to Docker Hub..."
docker push $DOCKER_USER/$IMAGE_NAME:$VERSION
docker push $DOCKER_USER/$IMAGE_NAME:latest

echo "Done! Image: $DOCKER_USER/$IMAGE_NAME:$VERSION"
echo "Render will auto-deploy the new image."