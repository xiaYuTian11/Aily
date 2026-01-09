<template>
  <div class="tool-page">
    <div class="page-header">
      <h2>💧 图片水印</h2>
      <p class="page-desc">为图片添加文字水印，支持自定义位置和透明度</p>
    </div>
    <el-card class="tool-card">
      <el-row :gutter="24">
        <el-col :span="12">
          <div class="section">
            <div class="section-title">上传图片</div>
            <el-upload :auto-upload="false" :on-change="handleFile" accept="image/*" :show-file-list="false" drag class="upload-area">
              <el-icon :size="48" class="upload-icon"><UploadFilled /></el-icon>
              <div class="upload-text">点击或拖拽上传图片</div>
            </el-upload>
            <el-form label-width="80px" class="watermark-form">
              <el-form-item label="水印文字">
                <el-input v-model="text" placeholder="输入水印文字" />
              </el-form-item>
              <el-form-item label="透明度">
                <el-slider v-model="opacity" :min="10" :max="100" show-input />
              </el-form-item>
              <el-form-item label="位置">
                <el-radio-group v-model="position">
                  <el-radio value="top-left">左上</el-radio>
                  <el-radio value="top-right">右上</el-radio>
                  <el-radio value="center">居中</el-radio>
                  <el-radio value="bottom-left">左下</el-radio>
                  <el-radio value="bottom-right">右下</el-radio>
                </el-radio-group>
              </el-form-item>
            </el-form>
            <el-button type="primary" size="large" @click="addWatermark" :loading="loading" :disabled="!file">添加水印并下载</el-button>
          </div>
        </el-col>
        <el-col :span="12">
          <div class="section preview-section">
            <div class="section-title">预览</div>
            <div v-if="preview" class="preview-box">
              <img :src="preview" class="preview-img" />
              <div class="watermark-preview" :class="position">{{ text }}</div>
            </div>
            <div v-else class="empty-preview">上传图片后显示预览</div>
          </div>
        </el-col>
      </el-row>
      <el-divider />
      <div class="tips">
        <div class="tips-title">💡 使用说明</div>
        <ul>
          <li>透明度越低，水印越淡</li>
          <li>支持 5 种位置：四角和居中</li>
          <li>水印会自动适应图片大小</li>
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
const text = ref('水印')
const opacity = ref(50)
const position = ref('center')
const loading = ref(false)

function handleFile(f: any) {
  file.value = f.raw
  preview.value = URL.createObjectURL(f.raw)
}

async function addWatermark() {
  if (!file.value || !text.value) return ElMessage.warning('请上传图片并输入水印文字')
  loading.value = true
  const fd = new FormData()
  fd.append('file', file.value)
  fd.append('text', text.value)
  fd.append('opacity', String(opacity.value))
  fd.append('position', position.value)
  const res = await fetch('/api/watermark/add', { method: 'POST', body: fd })
  const blob = await res.blob()
  const a = document.createElement('a')
  a.href = URL.createObjectURL(blob)
  a.download = 'watermarked.png'
  a.click()
  loading.value = false
  ElMessage.success('水印添加成功')
}
</script>

<style scoped>
.page-header { margin-bottom: 20px; }
.page-header h2 { margin-bottom: 8px; }
.page-desc { color: #909399; font-size: 14px; }
.tool-card { border-radius: 12px; }
.section { padding: 20px; background: #f5f7fa; border-radius: 8px; min-height: 400px; }
.section-title { font-weight: 600; margin-bottom: 16px; font-size: 16px; }
.upload-area { width: 100%; }
.upload-icon { color: #909399; }
.upload-text { margin-top: 8px; }
.watermark-form { margin-top: 20px; }
.preview-section { display: flex; flex-direction: column; }
.preview-box { flex: 1; position: relative; background: #fff; border-radius: 8px; padding: 16px; display: flex; align-items: center; justify-content: center; }
.preview-img { max-width: 100%; max-height: 300px; border-radius: 4px; }
.watermark-preview { position: absolute; color: rgba(0,0,0,0.3); font-size: 14px; padding: 4px 8px; }
.watermark-preview.top-left { top: 20px; left: 20px; }
.watermark-preview.top-right { top: 20px; right: 20px; }
.watermark-preview.center { top: 50%; left: 50%; transform: translate(-50%, -50%); }
.watermark-preview.bottom-left { bottom: 20px; left: 20px; }
.watermark-preview.bottom-right { bottom: 20px; right: 20px; }
.empty-preview { flex: 1; display: flex; align-items: center; justify-content: center; color: #c0c4cc; }
.tips { background: #ecf5ff; padding: 16px; border-radius: 8px; }
.tips-title { font-weight: 500; margin-bottom: 8px; color: #409eff; }
.tips ul { margin: 0; padding-left: 20px; color: #909399; font-size: 13px; }
.tips li { margin-bottom: 4px; }
</style>