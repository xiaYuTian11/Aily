<template>
  <div class="tool-page">
    <div class="page-header">
      <h2>📱 二维码工具</h2>
      <p class="page-desc">生成和识别二维码，支持自定义尺寸</p>
    </div>
    
    <el-card class="tool-card">
      <el-tabs v-model="activeTab" class="custom-tabs">
        <el-tab-pane label="生成二维码" name="generate">
          <div class="input-section">
            <label class="input-label">输入内容</label>
            <el-input 
              v-model="content" 
              placeholder="输入网址或文本内容..." 
              :rows="4" 
              type="textarea"
              class="content-input"
            />
          </div>
          
          <div class="size-section">
            <label class="input-label">二维码尺寸</label>
            <el-slider v-model="qrSize" :min="100" :max="500" :step="50" show-stops />
            <span class="size-value">{{ qrSize }} x {{ qrSize }} px</span>
          </div>
          
          <div class="actions">
            <el-button type="primary" size="large" @click="generate" :loading="loading">
              生成二维码
            </el-button>
          </div>
          
          <div v-if="qrcodeUrl" class="qrcode-result">
            <div class="result-card">
              <img :src="qrcodeUrl" class="qrcode-img" :style="{ width: qrSize + 'px', height: qrSize + 'px' }" />
              <div class="result-actions">
                <el-button type="success" @click="downloadQrcode">下载二维码</el-button>
              </div>
            </div>
          </div>
        </el-tab-pane>
        
        <el-tab-pane label="识别二维码" name="decode">
          <div class="upload-section">
            <el-upload 
              :auto-upload="false" 
              :on-change="handleFile" 
              accept="image/*" 
              :show-file-list="false" 
              drag
              class="qr-upload"
            >
              <el-icon :size="48" class="upload-icon"><UploadFilled /></el-icon>
              <div class="upload-text">将二维码图片拖到此处，或点击上传</div>
              <div class="upload-hint">支持 JPG、PNG、GIF 等格式</div>
            </el-upload>
          </div>
          
          <div v-if="decoded" class="decode-result">
            <div class="result-card">
              <div class="result-header">
                <span class="result-icon">✅</span>
                <span class="result-title">识别成功</span>
              </div>
              <div class="result-content">
                <div class="result-value">{{ decoded }}</div>
              </div>
              <div class="result-actions">
                <el-button type="primary" @click="copyDecoded">复制内容</el-button>
                <el-button v-if="isUrl" type="success" @click="openUrl">打开链接</el-button>
              </div>
            </div>
          </div>
        </el-tab-pane>
      </el-tabs>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { UploadFilled } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus'

const activeTab = ref('generate')
const content = ref('')
const qrSize = ref(200)
const qrcodeUrl = ref('')
const decoded = ref('')
const loading = ref(false)

const isUrl = computed(() => /^https?:\/\//.test(decoded.value))

async function generate() {
  if (!content.value) return ElMessage.warning('请输入内容')
  loading.value = true
  try {
    const res = await fetch('/api/ai/image/qrcode/generate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ content: content.value, size: qrSize.value })
    })
    const blob = await res.blob()
    qrcodeUrl.value = URL.createObjectURL(blob)
    ElMessage.success('生成成功')
  } finally {
    loading.value = false
  }
}

function downloadQrcode() {
  const a = document.createElement('a')
  a.href = qrcodeUrl.value
  a.download = 'qrcode.png'
  a.click()
}

async function handleFile(f: any) {
  const formData = new FormData()
  formData.append('file', f.raw)
  try {
    const res = await fetch('/api/ai/image/qrcode/decode', { method: 'POST', body: formData })
    const data = await res.json()
    decoded.value = data.data.content
    ElMessage.success('识别成功')
  } catch {
    ElMessage.error('识别失败')
  }
}

function copyDecoded() {
  navigator.clipboard.writeText(decoded.value)
  ElMessage.success('已复制')
}

function openUrl() {
  window.open(decoded.value, '_blank')
}
</script>

<style scoped>
.page-header { margin-bottom: 24px; }
.page-header h2 { font-size: 24px; margin-bottom: 8px; }
.page-desc { color: #909399; }
.tool-card { border-radius: 12px; }
.input-section, .size-section { margin-bottom: 20px; }
.input-label { display: block; margin-bottom: 8px; font-weight: 500; }
.size-value { margin-left: 12px; color: #409eff; }
.actions { margin: 20px 0; }
.qrcode-result, .decode-result { margin-top: 24px; }
.result-card { text-align: center; padding: 24px; background: #f5f7fa; border-radius: 8px; }
.qrcode-img { border: 1px solid #eee; border-radius: 8px; }
.result-actions { margin-top: 16px; }
.upload-icon { color: #909399; }
.upload-text { margin-top: 8px; }
.upload-hint { font-size: 12px; color: #909399; }
.result-header { margin-bottom: 16px; }
.result-icon { font-size: 24px; margin-right: 8px; }
.result-title { font-size: 18px; font-weight: 500; }
.result-value { padding: 16px; background: #fff; border-radius: 4px; word-break: break-all; }
</style>