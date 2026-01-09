<template>
  <div class="tool-page">
    <div class="page-header">
      <h2>🗜️ 图片压缩</h2>
      <p class="page-desc">压缩图片文件大小，保持较好的画质</p>
    </div>
    <el-card class="tool-card">
      <el-row :gutter="24">
        <el-col :span="12">
          <div class="section">
            <div class="section-title">上传图片</div>
            <el-upload :auto-upload="false" :on-change="handleChange" accept="image/*" :show-file-list="false" drag class="upload-area">
              <el-icon :size="48" class="upload-icon"><UploadFilled /></el-icon>
              <div class="upload-text">点击或拖拽上传图片</div>
              <div class="upload-hint">支持 JPG、PNG、GIF 等格式</div>
            </el-upload>
            <div v-if="file" class="file-info">
              <span>📎 {{ file.name }}</span>
              <span class="file-size">{{ formatSize(file.size) }}</span>
            </div>
            <div class="quality-control">
              <div class="quality-header">
                <span>压缩质量</span>
                <span class="quality-value">{{ quality }}%</span>
              </div>
              <el-slider v-model="quality" :min="10" :max="100" :marks="{ 30: '低', 60: '中', 90: '高' }" />
            </div>
            <el-button type="primary" size="large" @click="compress" :loading="loading" :disabled="!file">压缩并下载</el-button>
          </div>
        </el-col>
        <el-col :span="12">
          <div class="section preview-section">
            <div class="section-title">预览</div>
            <div v-if="preview" class="preview-box">
              <img :src="preview" class="preview-img" />
            </div>
            <div v-else class="empty-preview">上传图片后显示预览</div>
          </div>
        </el-col>
      </el-row>
      <el-divider />
      <div class="tips">
        <div class="tips-title">💡 使用说明</div>
        <ul>
          <li>质量越低，文件越小，但画质损失越大</li>
          <li>建议质量设置在 60-80 之间，平衡大小和画质</li>
          <li>PNG 格式会转换为 JPG 进行压缩</li>
        </ul>
      </div>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { UploadFilled } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus'

const file = ref<File | null>(null)
const preview = ref('')
const quality = ref(80)
const loading = ref(false)

function handleChange(f: any) {
  file.value = f.raw
  preview.value = URL.createObjectURL(f.raw)
}

function formatSize(bytes: number) {
  if (bytes < 1024) return bytes + ' B'
  if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB'
  return (bytes / 1024 / 1024).toFixed(1) + ' MB'
}

async function compress() {
  if (!file.value) return
  loading.value = true
  const formData = new FormData()
  formData.append('file', file.value)
  formData.append('quality', String(quality.value))
  try {
    const res = await fetch('/api/ai/image/compress', { method: 'POST', body: formData })
    const blob = await res.blob()
    const a = document.createElement('a')
    a.href = URL.createObjectURL(blob)
    a.download = 'compressed.jpg'
    a.click()
    ElMessage.success('压缩成功')
  } catch {
    ElMessage.error('压缩失败')
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.page-header { margin-bottom: 20px; }
.page-header h2 { margin-bottom: 8px; }
.page-desc { color: #909399; font-size: 14px; }
.tool-card { border-radius: 12px; }
.section { padding: 20px; background: #f5f7fa; border-radius: 8px; min-height: 360px; }
.section-title { font-weight: 600; margin-bottom: 16px; font-size: 16px; }
.upload-area { width: 100%; }
.upload-icon { color: #909399; }
.upload-text { margin-top: 8px; }
.upload-hint { font-size: 12px; color: #909399; }
.file-info { margin: 16px 0; display: flex; justify-content: space-between; padding: 12px; background: #fff; border-radius: 6px; }
.file-size { color: #909399; }
.quality-control { margin: 20px 0; }
.quality-header { display: flex; justify-content: space-between; margin-bottom: 8px; }
.quality-value { color: #409eff; font-weight: 500; }
.preview-section { display: flex; flex-direction: column; }
.preview-box { flex: 1; display: flex; align-items: center; justify-content: center; background: #fff; border-radius: 8px; padding: 16px; }
.preview-img { max-width: 100%; max-height: 280px; border-radius: 4px; }
.empty-preview { flex: 1; display: flex; align-items: center; justify-content: center; color: #c0c4cc; }
.tips { background: #f0f9eb; padding: 16px; border-radius: 8px; }
.tips-title { font-weight: 500; margin-bottom: 8px; color: #67c23a; }
.tips ul { margin: 0; padding-left: 20px; color: #909399; font-size: 13px; }
.tips li { margin-bottom: 4px; }
</style>