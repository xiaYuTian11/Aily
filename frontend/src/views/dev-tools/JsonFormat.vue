<template>
  <div class="tool-page">
    <h2>📋 JSON格式化</h2>
    <el-card class="tool-card">
      <el-row :gutter="24">
        <el-col :span="12">
          <div class="editor-header">
            <span>输入JSON</span>
            <el-button size="small" text @click="input = ''">清空</el-button>
          </div>
          <el-input v-model="input" type="textarea" :rows="18" placeholder="在此粘贴JSON..." />
        </el-col>
        <el-col :span="12">
          <div class="editor-header">
            <span>输出结果</span>
            <el-button size="small" text @click="copy">复制</el-button>
          </div>
          <el-input v-model="output" type="textarea" :rows="18" placeholder="结果将显示在这里..." readonly />
        </el-col>
      </el-row>
      <div class="actions">
        <el-button type="primary" @click="format" :loading="loading">格式化</el-button>
        <el-button @click="compress">压缩</el-button>
        <el-button @click="validate">校验</el-button>
        <el-select v-model="indent" style="width: 100px; margin-left: auto;">
          <el-option :value="2" label="2空格" />
          <el-option :value="4" label="4空格" />
        </el-select>
      </div>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { ElMessage } from 'element-plus'
import { formatJson, compressJson, validateJson } from '@/api/dev-tools'

const input = ref('')
const output = ref('')
const indent = ref(2)
const loading = ref(false)

async function format() {
  if (!input.value.trim()) return ElMessage.warning('请输入JSON')
  loading.value = true
  try {
    const res = await formatJson(input.value, indent.value)
    output.value = res.data.result
    ElMessage.success('格式化成功')
  } catch (e: any) {
    ElMessage.error(e.response?.data?.detail || '格式化失败')
  } finally {
    loading.value = false
  }
}

async function compress() {
  if (!input.value.trim()) return ElMessage.warning('请输入JSON')
  try {
    const res = await compressJson(input.value)
    output.value = res.data.result
    ElMessage.success('压缩成功')
  } catch (e: any) {
    ElMessage.error(e.response?.data?.detail || '压缩失败')
  }
}

async function validate() {
  if (!input.value.trim()) return ElMessage.warning('请输入JSON')
  const res = await validateJson(input.value)
  if (res.data.valid) {
    ElMessage.success('JSON格式正确 ✓')
  } else {
    ElMessage.error(`格式错误: ${res.data.error}`)
  }
}

function copy() {
  if (!output.value) return
  navigator.clipboard.writeText(output.value)
  ElMessage.success('已复制到剪贴板')
}
</script>

<style scoped>
.tool-card { border-radius: 12px; }
.editor-header { display: flex; justify-content: space-between; margin-bottom: 8px; font-weight: 500; }
.actions { display: flex; gap: 12px; margin-top: 20px; padding-top: 20px; border-top: 1px solid #ebeef5; }
</style>