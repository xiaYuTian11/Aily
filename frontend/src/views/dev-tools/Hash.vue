<template>
  <div class="tool-page">
    <div class="page-header">
      <h2>🔒 Hash 加密</h2>
      <p class="page-desc">计算文本的哈希值，支持多种算法</p>
    </div>
    <el-card class="tool-card">
      <el-row :gutter="24">
        <el-col :span="12">
          <div class="section">
            <div class="section-title">输入内容</div>
            <el-input v-model="input" type="textarea" :rows="8" placeholder="输入要计算哈希的内容..." />
            <div class="algo-buttons">
              <el-button :type="algorithm === 'md5' ? 'primary' : 'default'" @click="hash('md5')">MD5</el-button>
              <el-button :type="algorithm === 'sha1' ? 'primary' : 'default'" @click="hash('sha1')">SHA1</el-button>
              <el-button :type="algorithm === 'sha256' ? 'primary' : 'default'" @click="hash('sha256')">SHA256</el-button>
              <el-button :type="algorithm === 'sha512' ? 'primary' : 'default'" @click="hash('sha512')">SHA512</el-button>
            </div>
          </div>
        </el-col>
        <el-col :span="12">
          <div class="section result-section">
            <div class="section-title">计算结果</div>
            <div v-if="results.length" class="results-list">
              <div v-for="r in results" :key="r.algo" class="result-item">
                <div class="result-header">
                  <span class="algo-tag">{{ r.algo }}</span>
                  <el-button size="small" text @click="copyResult(r.value)">复制</el-button>
                </div>
                <div class="result-value">{{ r.value }}</div>
              </div>
            </div>
            <div v-else class="empty-tip">选择算法计算哈希值</div>
          </div>
        </el-col>
      </el-row>
      <el-divider />
      <div class="tips">
        <div class="tips-title">💡 算法说明</div>
        <div class="algo-info">
          <div class="algo-item"><span class="tag">MD5</span> 128位，速度快，已不推荐用于安全场景</div>
          <div class="algo-item"><span class="tag">SHA1</span> 160位，已被证明存在碰撞风险</div>
          <div class="algo-item"><span class="tag">SHA256</span> 256位，目前广泛使用的安全算法</div>
          <div class="algo-item"><span class="tag">SHA512</span> 512位，安全性最高</div>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { ElMessage } from 'element-plus'
import { md5Hash, shaHash } from '@/api/dev-tools'

const input = ref('')
const algorithm = ref('')
const results = ref<{algo: string, value: string}[]>([])

async function hash(algo: string) {
  if (!input.value) return ElMessage.warning('请输入内容')
  algorithm.value = algo
  let value = ''
  if (algo === 'md5') {
    const res = await md5Hash(input.value)
    value = res.data.result
  } else {
    const res = await shaHash(input.value, algo)
    value = res.data.result
  }
  const existing = results.value.find(r => r.algo === algo.toUpperCase())
  if (existing) {
    existing.value = value
  } else {
    results.value.push({ algo: algo.toUpperCase(), value })
  }
  ElMessage.success(`${algo.toUpperCase()} 计算完成`)
}

function copyResult(value: string) {
  navigator.clipboard.writeText(value)
  ElMessage.success('已复制')
}
</script>

<style scoped>
.page-header { margin-bottom: 20px; }
.page-header h2 { margin-bottom: 8px; }
.page-desc { color: #909399; font-size: 14px; }
.tool-card { border-radius: 12px; }
.section { padding: 20px; background: #f5f7fa; border-radius: 8px; min-height: 300px; }
.section-title { font-weight: 600; margin-bottom: 16px; font-size: 16px; }
.algo-buttons { display: flex; gap: 12px; margin-top: 16px; flex-wrap: wrap; }
.result-section { overflow-y: auto; max-height: 340px; }
.results-list { display: flex; flex-direction: column; gap: 12px; }
.result-item { background: #fff; padding: 12px; border-radius: 6px; border: 1px solid #ebeef5; }
.result-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; }
.algo-tag { background: #409eff; color: #fff; padding: 2px 8px; border-radius: 4px; font-size: 12px; }
.result-value { font-family: monospace; word-break: break-all; font-size: 13px; color: #606266; }
.empty-tip { color: #c0c4cc; text-align: center; padding: 80px 0; }
.tips { background: #ecf5ff; padding: 16px; border-radius: 8px; }
.tips-title { font-weight: 500; margin-bottom: 12px; color: #409eff; }
.algo-info { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
.algo-item { font-size: 13px; color: #606266; }
.algo-item .tag { background: #f0f2f5; padding: 2px 6px; border-radius: 3px; margin-right: 8px; font-weight: 500; }
</style>