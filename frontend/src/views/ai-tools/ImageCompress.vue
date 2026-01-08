<template>
  <div class="tool-page">
    <h2>🗜️ 图片压缩</h2>
    <el-card class="tool-card">
      <el-upload :auto-upload="false" :on-change="handleChange" accept="image/*" :show-file-list="false" drag>
        <el-icon :size="48"><UploadFilled /></el-icon>
        <div>点击或拖拽上传图片</div>
      </el-upload>
      <div v-if="preview" class="preview-section">
        <img :src="preview" class="preview-img" />
        <div class="quality-control">
          <span>压缩质量: {{ quality }}%</span>
          <el-slider v-model="quality" :min="10" :max="100" />
        </div>
        <el-button type="primary" @click="compress" :loading="loading">压缩并下载</el-button>
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
.tool-card { border-radius: 12px; }
.preview-section { margin-top: 24px; text-align: center; }
.preview-img { max-width: 400px; max-height: 300px; border-radius: 8px; margin-bottom: 16px; }
.quality-control { max-width: 300px; margin: 0 auto 16px; }
</style>