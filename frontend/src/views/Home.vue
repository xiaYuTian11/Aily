<template>
  <div class="home">
    <div class="hero">
      <h1>🛠️ Aily 工具箱</h1>
      <p>一站式开发者工具平台，提升你的工作效率</p>
    </div>
    <el-row :gutter="24">
      <el-col :span="12">
        <el-card class="tool-card" shadow="hover">
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
        <el-card class="tool-card" shadow="hover">
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
.home { max-width: 1000px; margin: 0 auto; }
.hero { text-align: center; padding: 48px 0; }
.hero h1 { font-size: 36px; margin-bottom: 12px; }
.hero p { color: #909399; font-size: 16px; }
.tool-card { border-radius: 12px; }
.card-header { display: flex; align-items: center; gap: 8px; font-size: 18px; font-weight: 600; }
.tool-list { display: flex; flex-direction: column; gap: 12px; }
.tool-item {
  display: flex; align-items: center; gap: 8px; padding: 12px 16px;
  background: #f5f7fa; border-radius: 8px; text-decoration: none; color: #303133;
  transition: all 0.2s;
}
.tool-item:hover { background: #ecf5ff; color: #409eff; transform: translateX(4px); }
</style>