<template>
  <div class="tool-page">
    <h2>🌐 中英互译</h2>
    <el-card class="tool-card">
      <div class="translate-container">
        <div class="input-area">
          <div class="lang-header">
            <span>{{ sourceLang === 'zh' ? '中文' : '英文' }}</span>
          </div>
          <el-input v-model="input" type="textarea" :rows="8" placeholder="输入要翻译的内容..." />
        </div>
        <div class="swap-btn">
          <el-button circle @click="swapLang">⇄</el-button>
        </div>
        <div class="output-area">
          <div class="lang-header">
            <span>{{ targetLang === 'en' ? '英文' : '中文' }}</span>
          </div>
          <el-input v-model="output" type="textarea" :rows="8" readonly placeholder="翻译结果..." />
        </div>
      </div>
      <div class="actions">
        <el-button type="primary" size="large" @click="doTranslate" :loading="loading">翻译</el-button>
        <el-button @click="copy">复制结果</el-button>
        <el-button text @click="clear">清空</el-button>
      </div>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { ElMessage } from 'element-plus'

const input = ref('')
const output = ref('')
const loading = ref(false)
const sourceLang = ref('en')
const targetLang = ref('zh')

function swapLang() {
  [sourceLang.value, targetLang.value] = [targetLang.value, sourceLang.value]
  ;[input.value, output.value] = [output.value, input.value]
}

async function doTranslate() {
  if (!input.value) return ElMessage.warning('请输入内容')
  loading.value = true
  try {
    const res = await fetch('/api/translate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: input.value, source: sourceLang.value, target: targetLang.value })
    })
    const data = await res.json()
    output.value = data.data.result
    ElMessage.success('翻译成功')
  } catch {
    ElMessage.error('翻译失败')
  } finally {
    loading.value = false
  }
}

function copy() {
  if (!output.value) return
  navigator.clipboard.writeText(output.value)
  ElMessage.success('已复制')
}

function clear() {
  input.value = ''
  output.value = ''
}
</script>

<style scoped>
.translate-container { display: flex; gap: 16px; align-items: center; }
.input-area, .output-area { flex: 1; }
.lang-header { margin-bottom: 8px; font-weight: 500; color: #409eff; }
.swap-btn { padding: 0 8px; }
.actions { margin-top: 20px; display: flex; gap: 12px; }
</style>