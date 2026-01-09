<template>
  <div class="home">
    <div class="decor decor-1"></div>
    <div class="decor decor-2"></div>
    <div class="decor decor-3"></div>
    <div class="hero">
      <h1>🛠️ Aily 工具箱</h1>
      <p>一站式开发者工具平台，提升你的工作效率</p>
    </div>
    <el-row :gutter="16">
      <el-col :span="12">
        <el-card class="tool-card card-animate" shadow="hover">
          <template #header>
            <div class="card-header">
              <el-icon :size="24" color="#409eff"><Tools /></el-icon>
              <span>编程工具</span>
            </div>
          </template>
          <div class="tool-list">
            <router-link to="/dev/json" class="tool-item">
              <span>📋</span> JSON格式化
            </router-link>
            <router-link to="/dev/base64" class="tool-item">
              <span>🔐</span> Base64编解码
            </router-link>
            <router-link to="/dev/hash" class="tool-item">
              <span>🔒</span> Hash加密
            </router-link>
            <router-link to="/dev/timestamp" class="tool-item">
              <span>⏰</span> 时间戳转换
            </router-link>
          </div>
        </el-card>
      </el-col>
      <el-col :span="12">
        <el-card class="tool-card card-animate card-delay" shadow="hover">
          <template #header>
            <div class="card-header">
              <el-icon :size="24" color="#67c23a"><MagicStick /></el-icon>
              <span>AI工具</span>
            </div>
          </template>
          <div class="tool-list">
            <router-link to="/ai/image-to-pdf" class="tool-item">
              <span>📄</span> 图片转PDF
            </router-link>
            <router-link to="/ai/image-compress" class="tool-item">
              <span>🗜️</span> 图片压缩
            </router-link>
            <router-link to="/ai/qrcode" class="tool-item">
              <span>📱</span> 二维码工具
            </router-link>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script setup lang="ts">
import { Tools, MagicStick } from '@element-plus/icons-vue'
</script>

<style scoped>
.home { max-width: 1000px; margin: 0 auto; position: relative; }
.decor {
  position: absolute;
  border-radius: 50%;
  background: linear-gradient(135deg, rgba(102, 126, 234, 0.15), rgba(118, 75, 162, 0.15));
  animation: float 6s ease-in-out infinite;
  pointer-events: none;
}
.decor-1 { width: 80px; height: 80px; top: 20px; right: 10%; animation-delay: 0s; }
.decor-2 { width: 50px; height: 50px; top: 120px; left: 5%; animation-delay: 2s; }
.decor-3 { width: 30px; height: 30px; bottom: 100px; right: 5%; animation-delay: 4s; border-radius: 4px; }
@keyframes float {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-15px) rotate(5deg); }
}
.hero {
  text-align: center;
  padding: 32px 0 24px;
  background: radial-gradient(ellipse at center, rgba(102, 126, 234, 0.1) 0%, transparent 70%);
  border-radius: 16px;
  margin-bottom: 8px;
}
.hero h1 {
  font-size: 36px;
  margin-bottom: 8px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.hero p { color: #909399; font-size: 16px; }
.tool-card {
  border-radius: 12px;
  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.3);
}
.card-animate {
  animation: slideUp 0.5s ease forwards;
  opacity: 0;
}
.card-delay { animation-delay: 0.15s; }
@keyframes slideUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
.card-header { display: flex; align-items: center; gap: 8px; font-size: 18px; font-weight: 600; }
.tool-list { display: flex; flex-direction: column; gap: 8px; }
.tool-item {
  display: flex; align-items: center; gap: 8px; padding: 10px 14px;
  background: rgba(245, 247, 250, 0.8);
  border-radius: 8px; text-decoration: none; color: #303133;
  transition: all 0.3s ease;
  backdrop-filter: blur(4px);
}
.tool-item:hover {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: #fff;
  transform: translateX(8px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}
</style>