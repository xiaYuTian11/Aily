@echo off
setlocal enabledelayedexpansion

:: 配置
set DOCKER_USER=xiaytian
set IMAGE_NAME=aily

:: 读取版本号
set /p VERSION=<VERSION

:: 解析版本号 (major.minor.patch)
for /f "tokens=1,2,3 delims=." %%a in ("%VERSION%") do (
    set MAJOR=%%a
    set MINOR=%%b
    set PATCH=%%c
)

:: 递增patch版本
set /a PATCH=%PATCH%+1
set NEW_VERSION=%MAJOR%.%MINOR%.%PATCH%

:: 更新VERSION文件
echo %NEW_VERSION%>VERSION

echo Building version %NEW_VERSION%...
docker build -t %DOCKER_USER%/%IMAGE_NAME%:%NEW_VERSION% .
docker tag %DOCKER_USER%/%IMAGE_NAME%:%NEW_VERSION% %DOCKER_USER%/%IMAGE_NAME%:latest

echo Pushing to Docker Hub...
docker push %DOCKER_USER%/%IMAGE_NAME%:%NEW_VERSION%
docker push %DOCKER_USER%/%IMAGE_NAME%:latest

echo Done! Image: %DOCKER_USER%/%IMAGE_NAME%:%NEW_VERSION%