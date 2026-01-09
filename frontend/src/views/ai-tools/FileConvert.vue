<template>
  <div class="tool-page">
    <div class="page-header">
      <h2>📄 文件转换</h2>
      <p class="page-desc">PDF 与图片格式互相转换</p>
    </div>
    <el-card class="tool-card">
      <el-tabs v-model="activeTab" class="custom-tabs">
        <el-tab-pane label="PDF转图片" name="pdf2img">
          <div class="convert-section">
            <el-upload :auto-upload="false" :on-change="handlePdf" accept=".pdf" :show-file-list="false" drag class="upload-area">
              <el-icon :size="48" class="upload-icon"><UploadFilled /></el-icon>
              <div class="upload-text">将 PDF 文件拖到此处，或点击上传</div>
              <div class="upload-hint">支持单个 PDF 文件</div>
            </el-upload>
            <div v-if="pdfFile" class="file-info">
              <span class="file-name">📎 {{ pdfFile.name }}</span>
              <el-button text type="danger" @click="pdfFile = null">移除</el-button>
            </div>
            <el-button v-if="pdfFile" type="primary" size="large" @click="convertPdfToImages" :loading="loading">转换为图片并下载</el-button>
          </div>
        </el-tab-pane>
        <el-tab-pane label="图片转PDF" name="img2pdf">
          <div class="convert-section">
            <el-upload :auto-upload="false" :on-change="handleImages" accept="image/*" multiple :file-list="imageFiles" drag class="upload-area">
              <el-icon :size="48" class="upload-icon"><UploadFilled /></el-icon>
              <div class="upload-text">将图片拖到此处，或点击上传</div>
              <div class="upload-hint">支持多选，按上传顺序合并</div>
            </el-upload>
            <div v-if="imageFiles.length" class="file-count">已选择 {{ imageFiles.length }} 个文件</div>
            <el-button v-if="imageFiles.length" type="primary" size="large" @click="convertImagesToPdf" :loading="loading">合并为 PDF 并下载</el-button>
          </div>
        </el-tab-pane>
      </el-tabs>
      <el-divider />
      <div class="tips">
        <div class="tips-title">💡 使用说明</div>
        <ul>
          <li>PDF转图片：每页 PDF 将转换为一张图片，打包下载</li>
          <li>图片转PDF：多张图片按顺序合并为一个 PDF 文件</li>
          <li>支持常见图片格式：JPG、PNG、GIF 等</li>
        </ul>
      </div>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { UploadFilled } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus'

const activeTab = ref('pdf2img')
const pdfFile = ref<File | null>(null)
const imageFiles = ref<any[]>([])
const loading = ref(false)

function handlePdf(f: any) { pdfFile.value = f.raw }
function handleImages(_f: any, list: any[]) { imageFiles.value = list }

async function convertPdfToImages() {
  if (!pdfFile.value) return
  loading.value = true
  const fd = new FormData()
  fd.append('file', pdfFile.value)
  const res = await fetch('/api/convert/pdf-to-images', { method: 'POST', body: fd })
  const blob = await res.blob()
  download(blob, 'images.zip')
  loading.value = false
  ElMessage.success('转换成功')
}

async function convertImagesToPdf() {
  if (!imageFiles.value.length) return
  loading.value = true
  const fd = new FormData()
  imageFiles.value.forEach(f => fd.append('files', f.raw))
  const res = await fetch('/api/convert/images-to-pdf', { method: 'POST', body: fd })
  const blob = await res.blob()
  download(blob, 'output.pdf')
  loading.value = false
  ElMessage.success('转换成功')
}

function download(blob: Blob, name: string) {
  const a = document.createElement('a')
  a.href = URL.createObjectURL(blob)
  a.download = name
  a.click()
}
</script>

<style scoped>
.page-header { margin-bottom: 20px; }
.page-header h2 { margin-bottom: 8px; }
.page-desc { color: #909399; font-size: 14px; }
.tool-card { border-radius: 12px; }
.convert-section { text-align: center; padding: 20px 0; }
.upload-area { width: 100%; }
.upload-icon { color: #909399; }
.upload-text { margin-top: 8px; font-size: 14px; }
.upload-hint { font-size: 12px; color: #909399; margin-top: 4px; }
.file-info { margin: 16px 0; display: flex; align-items: center; justify-content: center; gap: 12px; }
.file-name { color: #409eff; }
.file-count { margin: 16px 0; color: #67c23a; }
.tips { background: #ecf5ff; padding: 16px; border-radius: 8px; }
.tips-title { font-weight: 500; margin-bottom: 8px; color: #409eff; }
.tips ul { margin: 0; padding-left: 20px; color: #909399; font-size: 13px; }
.tips li { margin-bottom: 4px; }
</style>