<template>
  <div class="tool-page">
    <div class="page-header">
      <h2>🌐 中英互译</h2>
      <p class="page-desc">中文与英文之间的快速翻译</p>
    </div>
    <el-card class="tool-card">
      <div class="translate-container">
        <div class="input-area">
          <div class="lang-header">
            <span class="lang-label">{{ sourceLang === 'zh' ? '🇨🇳 中文' : '🇺🇸 英文' }}</span>
            <el-button size="small" text @click="input = ''">清空</el-button>
          </div>
          <el-input v-model="input" type="textarea" :rows="10" placeholder="输入要翻译的内容..." />
          <div class="char-count">{{ input.length }} 字符</div>
        </div>
        <div class="swap-btn">
          <el-button circle size="large" @click="swapLang">⇄</el-button>
        </div>
        <div class="output-area">
          <div class="lang-header">
            <span class="lang-label">{{ targetLang === 'en' ? '🇺🇸 英文' : '🇨🇳 中文' }}</span>
            <el-button size="small" text @click="copy">复制</el-button>
          </div>
          <el-input v-model="output" type="textarea" :rows="10" readonly placeholder="翻译结果将显示在这里..." />
        </div>
      </div>
      <div class="actions">
        <el-button type="primary" size="large" @click="doTranslate" :loading="loading">翻译</el-button>
      </div>
      <el-divider />
      <div class="tips">
        <div class="tips-title">💡 使用说明</div>
        <ul>
          <li>点击中间按钮可切换翻译方向</li>
          <li>支持中英文自动检测</li>
          <li>翻译结果可直接复制使用</li>
        </ul>
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
</script>

<style scoped>
.page-header { margin-bottom: 20px; }
.page-header h2 { margin-bottom: 8px; }
.page-desc { color: #909399; font-size: 14px; }
.tool-card { border-radius: 12px; }
.translate-container { display: flex; gap: 16px; align-items: stretch; }
.input-area, .output-area { flex: 1; display: flex; flex-direction: column; }
.lang-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; }
.lang-label { font-weight: 500; color: #409eff; font-size: 15px; }
.char-count { text-align: right; font-size: 12px; color: #909399; margin-top: 4px; }
.swap-btn { display: flex; align-items: center; padding: 0 8px; }
.actions { margin-top: 20px; display: flex; justify-content: center; }
.tips { background: #ecf5ff; padding: 16px; border-radius: 8px; }
.tips-title { font-weight: 500; margin-bottom: 8px; color: #409eff; }
.tips ul { margin: 0; padding-left: 20px; color: #909399; font-size: 13px; }
.tips li { margin-bottom: 4px; }
</style>