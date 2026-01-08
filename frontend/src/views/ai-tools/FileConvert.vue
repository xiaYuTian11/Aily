<template>
  <div class="tool-page">
    <h2>📄 文件转换</h2>
    <el-card class="tool-card">
      <el-tabs v-model="activeTab">
        <el-tab-pane label="PDF转图片" name="pdf2img">
          <el-upload :auto-upload="false" :on-change="handlePdf" accept=".pdf" :show-file-list="false" drag>
            <div>上传PDF文件</div>
          </el-upload>
          <el-button v-if="pdfFile" type="primary" @click="convertPdfToImages" :loading="loading" style="margin-top:16px">转换并下载</el-button>
        </el-tab-pane>
        <el-tab-pane label="图片转PDF" name="img2pdf">
          <el-upload :auto-upload="false" :on-change="handleImages" accept="image/*" multiple :file-list="imageFiles" drag>
            <div>上传图片（可多选）</div>
          </el-upload>
          <el-button v-if="imageFiles.length" type="primary" @click="convertImagesToPdf" :loading="loading" style="margin-top:16px">转换并下载</el-button>
        </el-tab-pane>
      </el-tabs>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { ElMessage } from 'element-plus'

const activeTab = ref('pdf2img')
const pdfFile = ref<File | null>(null)
const imageFiles = ref<any[]>([])
const loading = ref(false)

function handlePdf(f: any) { pdfFile.value = f.raw }
function handleImages(f: any, list: any[]) { imageFiles.value = list }

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
.tool-card { border-radius: 12px; }
</style>