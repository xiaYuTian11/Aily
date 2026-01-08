<template>
  <div class="tool-page">
    <h2>🪪 身份证生成</h2>
    <el-card class="tool-card">
      <el-button type="primary" size="large" @click="generate">生成身份证号</el-button>
      <div v-if="result" class="result-card">
        <div class="result-item"><span>身份证号:</span><code>{{ result.idcard }}</code><el-button size="small" @click="copy(result.idcard)">复制</el-button></div>
        <div class="result-item"><span>地区:</span><code>{{ result.area }}</code></div>
        <div class="result-item"><span>出生日期:</span><code>{{ result.birth }}</code></div>
        <div class="result-item"><span>性别:</span><code>{{ result.gender }}</code></div>
      </div>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { ElMessage } from 'element-plus'

const result = ref<any>(null)

async function generate() {
  const res = await fetch('/api/idcard/generate')
  const data = await res.json()
  result.value = data.data
}

function copy(text: string) {
  navigator.clipboard.writeText(text)
  ElMessage.success('已复制')
}
</script>

<style scoped>
.result-card { margin-top: 24px; padding: 20px; background: #f5f7fa; border-radius: 8px; }
.result-item { display: flex; align-items: center; gap: 12px; margin-bottom: 12px; }
.result-item span { width: 80px; }
.result-item code { font-size: 16px; color: #409eff; }
</style>