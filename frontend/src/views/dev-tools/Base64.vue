<template>
  <div class="tool-page">
    <h2>🔐 Base64 编解码</h2>
    <el-card class="tool-card">
      <el-input v-model="input" type="textarea" :rows="8" placeholder="输入要编码/解码的内容..." />
      <div class="actions">
        <el-button type="primary" @click="encode">编码 →</el-button>
        <el-button @click="decode">← 解码</el-button>
        <el-button text @click="swap">交换</el-button>
      </div>
      <el-input v-model="output" type="textarea" :rows="8" placeholder="结果..." readonly />
      <div class="actions">
        <el-button @click="copy">复制结果</el-button>
        <el-button text @click="clear">清空</el-button>
      </div>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { ElMessage } from 'element-plus'
import { base64Encode, base64Decode } from '@/api/dev-tools'

const input = ref('')
const output = ref('')

async function encode() {
  if (!input.value) return ElMessage.warning('请输入内容')
  const res = await base64Encode(input.value)
  output.value = res.data.result
  ElMessage.success('编码成功')
}

async function decode() {
  if (!input.value) return ElMessage.warning('请输入内容')
  try {
    const res = await base64Decode(input.value)
    output.value = res.data.result
    ElMessage.success('解码成功')
  } catch {
    ElMessage.error('解码失败，请检查输入')
  }
}

function swap() {
  const temp = input.value
  input.value = output.value
  output.value = temp
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
.tool-card { border-radius: 12px; }
.actions { display: flex; gap: 12px; margin: 16px 0; }
</style>