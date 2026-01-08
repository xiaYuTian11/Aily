<template>
  <div class="tool-page">
    <h2>🔒 Hash 加密</h2>
    <el-card class="tool-card">
      <el-input v-model="input" type="textarea" :rows="6" placeholder="输入要加密的内容..." />
      <div class="actions">
        <el-button type="primary" @click="hash('md5')">MD5</el-button>
        <el-button @click="hash('sha1')">SHA1</el-button>
        <el-button @click="hash('sha256')">SHA256</el-button>
        <el-button @click="hash('sha512')">SHA512</el-button>
      </div>
      <div class="result-box" v-if="output">
        <div class="result-label">{{ algorithm.toUpperCase() }} 结果:</div>
        <div class="result-value">{{ output }}</div>
        <el-button size="small" @click="copy">复制</el-button>
      </div>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { ElMessage } from 'element-plus'
import { md5Hash, shaHash } from '@/api/dev-tools'

const input = ref('')
const output = ref('')
const algorithm = ref('md5')

async function hash(algo: string) {
  if (!input.value) return ElMessage.warning('请输入内容')
  algorithm.value = algo
  if (algo === 'md5') {
    const res = await md5Hash(input.value)
    output.value = res.data.result
  } else {
    const res = await shaHash(input.value, algo)
    output.value = res.data.result
  }
  ElMessage.success(`${algo.toUpperCase()} 加密成功`)
}

function copy() {
  navigator.clipboard.writeText(output.value)
  ElMessage.success('已复制')
}
</script>

<style scoped>
.tool-card { border-radius: 12px; }
.actions { display: flex; gap: 12px; margin: 16px 0; }
.result-box { background: #f5f7fa; padding: 16px; border-radius: 8px; margin-top: 16px; }
.result-label { font-size: 12px; color: #909399; margin-bottom: 8px; }
.result-value { font-family: monospace; word-break: break-all; margin-bottom: 12px; }
</style>