<template>
  <el-container class="layout">
    <el-aside width="240px" class="sidebar">
      <div class="logo">
        <span class="logo-icon">🛠️</span>
        <span class="logo-text">Aily 工具箱</span>
      </div>
      <el-menu :default-active="route.path" router class="menu">
        <el-menu-item index="/">
          <el-icon><HomeFilled /></el-icon>
          <span>首页</span>
        </el-menu-item>
        <el-sub-menu index="dev">
          <template #title>
            <el-icon><Tools /></el-icon>
            <span>编程工具</span>
          </template>
          <el-menu-item index="/dev/json">JSON格式化</el-menu-item>
          <el-menu-item index="/dev/base64">Base64编解码</el-menu-item>
          <el-menu-item index="/dev/hash">Hash加密</el-menu-item>
          <el-menu-item index="/dev/timestamp">时间戳转换</el-menu-item>
          <el-menu-item index="/dev/idcard">身份证生成</el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="ai">
          <template #title>
            <el-icon><MagicStick /></el-icon>
            <span>AI工具</span>
          </template>
          <el-menu-item index="/ai/image-compress">图片压缩</el-menu-item>
          <el-menu-item index="/ai/qrcode">二维码工具</el-menu-item>
          <el-menu-item index="/ai/translate">中英互译</el-menu-item>
          <el-menu-item index="/ai/convert">文件转换</el-menu-item>
          <el-menu-item index="/ai/watermark">图片水印</el-menu-item>
        </el-sub-menu>
      </el-menu>
    </el-aside>
    <el-main class="main">
      <router-view />
    </el-main>
  </el-container>
</template>

<script setup lang="ts">
import { useRoute } from 'vue-router'
import { HomeFilled, Tools, MagicStick } from '@element-plus/icons-vue'
const route = useRoute()
</script>

<style scoped>
.layout { height: 100vh; }
.sidebar {
  background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
  border-right: none;
}
.logo {
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  border-bottom: 1px solid rgba(255,255,255,0.1);
}
.logo-icon { font-size: 24px; }
.logo-text { color: #fff; font-size: 18px; font-weight: 600; }
.menu {
  background: transparent;
  border: none;
}
.menu :deep(.el-menu-item),
.menu :deep(.el-sub-menu__title) {
  color: rgba(255,255,255,0.8);
}
.menu :deep(.el-sub-menu .el-menu) {
  background: rgba(0,0,0,0.2);
}
.menu :deep(.el-sub-menu .el-menu .el-menu-item) {
  color: rgba(255,255,255,0.7);
  padding-left: 56px !important;
}
.menu :deep(.el-menu-item:hover),
.menu :deep(.el-sub-menu__title:hover),
.menu :deep(.el-sub-menu .el-menu .el-menu-item:hover) {
  background: rgba(255,255,255,0.1);
  color: #fff;
}
.menu :deep(.el-menu-item.is-active) {
  background: linear-gradient(90deg, #409eff 0%, #53a8ff 100%);
  color: #fff;
}
.main {
  background: #f0f2f5;
  padding: 24px;
  overflow-y: auto;
}
</style>