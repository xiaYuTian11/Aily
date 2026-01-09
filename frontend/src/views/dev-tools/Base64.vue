<template>
  <div class="tool-page">
    <div class="page-header">
      <h2>🔐 Base64 编解码</h2>
      <p class="page-desc">对文本进行 Base64 编码或解码转换</p>
    </div>
    <el-card class="tool-card">
      <el-row :gutter="24">
        <el-col :span="11">
          <div class="editor-header">
            <span>输入内容</span>
            <el-button size="small" text @click="input = ''">清空</el-button>
          </div>
          <el-input v-model="input" type="textarea" :rows="12" placeholder="输入要编码/解码的内容..." />
        </el-col>
        <el-col :span="2" class="action-col">
          <el-button type="primary" @click="encode">编码 →</el-button>
          <el-button @click="decode">← 解码</el-button>
          <el-button text @click="swap">⇄ 交换</el-button>
        </el-col>
        <el-col :span="11">
          <div class="editor-header">
            <span>输出结果</span>
            <el-button size="small" text @click="copy">复制</el-button>
          </div>
          <el-input v-model="output" type="textarea" :rows="12" placeholder="结果将显示在这里..." readonly />
        </el-col>
      </el-row>
      <el-divider />
      <div class="tips">
        <div class="tips-title">💡 使用说明</div>
        <ul>
          <li>Base64 是一种将二进制数据编码为 ASCII 字符的方法</li>
          <li>常用于在 URL、Cookie、网页中传输少量二进制数据</li>
          <li>编码后的数据比原始数据大约 33%</li>
        </ul>
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
  [input.value, output.value] = [output.value, input.value]
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
.editor-header { display: flex; justify-content: space-between; margin-bottom: 8px; font-weight: 500; }
.action-col { display: flex; flex-direction: column; justify-content: center; gap: 12px; }
.tips { background: #f0f9eb; padding: 16px; border-radius: 8px; }
.tips-title { font-weight: 500; margin-bottom: 8px; color: #67c23a; }
.tips ul { margin: 0; padding-left: 20px; color: #909399; font-size: 13px; }
.tips li { margin-bottom: 4px; }
</style>