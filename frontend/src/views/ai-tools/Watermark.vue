<template>
  <div class="tool-page">
    <h2>💧 图片水印</h2>
    <el-card class="tool-card">
      <el-upload :auto-upload="false" :on-change="handleFile" accept="image/*" :show-file-list="false" drag>
        <div>上传图片</div>
      </el-upload>
      <div v-if="preview" class="preview"><img :src="preview" /></div>
      <el-form label-width="80px" style="margin-top:16px">
        <el-form-item label="水印文字"><el-input v-model="text" placeholder="输入水印文字" /></el-form-item>
        <el-form-item label="透明度"><el-slider v-model="opacity" :min="10" :max="100" /></el-form-item>
        <el-form-item label="位置">
          <el-select v-model="position">
            <el-option label="居中" value="center" />
            <el-option label="左上" value="top-left" />
            <el-option label="右上" value="top-right" />
            <el-option label="左下" value="bottom-left" />
            <el-option label="右下" value="bottom-right" />
          </el-select>
        </el-form-item>
      </el-form>
      <el-button type="primary" @click="addWatermark" :loading="loading" :disabled="!file">添加水印</el-button>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
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
.preview { margin: 16px 0; }
.preview img { max-width: 300px; max-height: 200px; border-radius: 8px; }
</style>