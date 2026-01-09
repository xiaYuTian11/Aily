<template>
  <div class="tool-page">
    <div class="page-header">
      <h2>🪪 身份证生成</h2>
      <p class="page-desc">生成符合规则的虚拟身份证号，仅供测试使用</p>
    </div>
    <el-card class="tool-card">
      <el-row :gutter="24">
        <el-col :span="12">
          <div class="section">
            <div class="section-title">生成选项</div>
            <el-form label-width="80px">
              <el-form-item label="性别">
                <el-radio-group v-model="gender">
                  <el-radio value="">随机</el-radio>
                  <el-radio value="male">男</el-radio>
                  <el-radio value="female">女</el-radio>
                </el-radio-group>
              </el-form-item>
              <el-form-item label="生成数量">
                <el-input-number v-model="count" :min="1" :max="10" />
              </el-form-item>
            </el-form>
            <el-button type="primary" size="large" @click="generate" :loading="loading">生成身份证号</el-button>
          </div>
        </el-col>
        <el-col :span="12">
          <div class="section result-section">
            <div class="section-title">生成结果</div>
            <div v-if="results.length" class="results-list">
              <div v-for="(item, idx) in results" :key="idx" class="result-card">
                <div class="result-row">
                  <span class="label">身份证号</span>
                  <code class="value">{{ item.idcard }}</code>
                  <el-button size="small" text @click="copy(item.idcard)">复制</el-button>
                </div>
                <div class="result-row">
                  <span class="label">地区</span><span class="value-text">{{ item.area }}</span>
                </div>
                <div class="result-row">
                  <span class="label">出生日期</span><span class="value-text">{{ item.birth }}</span>
                  <span class="label" style="margin-left:16px">性别</span><span class="value-text">{{ item.gender }}</span>
                </div>
              </div>
            </div>
            <div v-else class="empty-tip">点击左侧按钮生成身份证号</div>
          </div>
        </el-col>
      </el-row>
      <el-divider />
      <div class="tips">
        <div class="tips-title">💡 使用说明</div>
        <ul>
          <li>生成的身份证号符合国家标准校验规则</li>
          <li>仅供软件测试、数据模拟等场景使用</li>
          <li>请勿用于任何非法用途</li>
        </ul>
      </div>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { ElMessage } from 'element-plus'

const results = ref<any[]>([])
const gender = ref('')
const count = ref(1)
const loading = ref(false)

async function generate() {
  loading.value = true
  results.value = []
  for (let i = 0; i < count.value; i++) {
    const url = gender.value ? `/api/idcard/generate?gender=${gender.value}` : '/api/idcard/generate'
    const res = await fetch(url)
    const data = await res.json()
    results.value.push(data.data)
  }
  loading.value = false
  ElMessage.success(`已生成 ${count.value} 个身份证号`)
}

function copy(text: string) {
  navigator.clipboard.writeText(text)
  ElMessage.success('已复制')
}
</script>

<style scoped>
.page-header { margin-bottom: 20px; }
.page-header h2 { margin-bottom: 8px; }
.page-desc { color: #909399; font-size: 14px; }
.section { padding: 20px; background: #f5f7fa; border-radius: 8px; min-height: 280px; }
.section-title { font-weight: 600; margin-bottom: 16px; font-size: 16px; }
.result-section { overflow-y: auto; max-height: 320px; }
.results-list { display: flex; flex-direction: column; gap: 12px; }
.result-card { background: #fff; padding: 12px 16px; border-radius: 6px; border: 1px solid #ebeef5; }
.result-row { display: flex; align-items: center; gap: 8px; margin-bottom: 6px; }
.result-row:last-child { margin-bottom: 0; }
.label { color: #909399; font-size: 13px; min-width: 60px; }
.value { color: #409eff; font-size: 15px; font-weight: 500; }
.value-text { color: #303133; font-size: 14px; }
.empty-tip { color: #c0c4cc; text-align: center; padding: 60px 0; }
.tips { background: #fdf6ec; padding: 16px; border-radius: 8px; }
.tips-title { font-weight: 500; margin-bottom: 8px; color: #e6a23c; }
.tips ul { margin: 0; padding-left: 20px; color: #909399; font-size: 13px; }
.tips li { margin-bottom: 4px; }
</style>