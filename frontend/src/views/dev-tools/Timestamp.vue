<template>
  <div class="tool-page">
    <h2>⏰ 时间戳转换</h2>
    <el-card class="tool-card">
      <el-row :gutter="24">
        <el-col :span="12">
          <div class="section">
            <div class="section-title">时间戳 → 日期时间</div>
            <el-input v-model="timestamp" placeholder="输入时间戳" />
            <div class="options">
              <el-radio-group v-model="inputUnit">
                <el-radio value="s">秒</el-radio>
                <el-radio value="ms">毫秒</el-radio>
              </el-radio-group>
              <el-button type="primary" @click="toDatetime">转换</el-button>
            </div>
            <div class="result" v-if="datetimeResult">{{ datetimeResult }}</div>
          </div>
        </el-col>
        <el-col :span="12">
          <div class="section">
            <div class="section-title">日期时间 → 时间戳</div>
            <el-date-picker v-model="datetime" type="datetime" placeholder="选择日期时间" style="width: 100%;" />
            <div class="options">
              <el-radio-group v-model="outputUnit">
                <el-radio value="s">秒</el-radio>
                <el-radio value="ms">毫秒</el-radio>
              </el-radio-group>
              <el-button type="primary" @click="toTimestamp">转换</el-button>
            </div>
            <div class="result" v-if="timestampResult">{{ timestampResult }}</div>
          </div>
        </el-col>
      </el-row>
      <el-divider />
      <div class="current-time">
        <span>当前时间戳 (点击复制):</span>
        <code class="clickable" @click="copy(currentTimestamp)">{{ currentTimestamp }} 秒</code>
        <code class="clickable" @click="copy(currentTimestampMs)">{{ currentTimestampMs }} 毫秒</code>
      </div>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import { ElMessage } from 'element-plus'

const timestamp = ref('')
const datetime = ref<Date | null>(null)
const datetimeResult = ref('')
const timestampResult = ref('')
const currentTimestamp = ref(0)
const currentTimestampMs = ref(0)
const inputUnit = ref('s')
const outputUnit = ref('s')

let timer: number

onMounted(() => {
  timer = window.setInterval(() => {
    currentTimestampMs.value = Date.now()
    currentTimestamp.value = Math.floor(currentTimestampMs.value / 1000)
  }, 1000)
})

onUnmounted(() => clearInterval(timer))

function toDatetime() {
  if (!timestamp.value) return ElMessage.warning('请输入时间戳')
  const ts = Number(timestamp.value)
  const ms = inputUnit.value === 'ms' ? ts : ts * 1000
  datetimeResult.value = new Date(ms).toLocaleString('zh-CN')
}

function toTimestamp() {
  if (!datetime.value) return ElMessage.warning('请选择日期时间')
  const ms = datetime.value.getTime()
  timestampResult.value = outputUnit.value === 'ms' ? String(ms) : String(Math.floor(ms / 1000))
}

function copy(val: number) {
  navigator.clipboard.writeText(String(val))
  ElMessage.success('已复制')
}
</script>

<style scoped>
.section { padding: 20px; background: #f5f7fa; border-radius: 8px; min-height: 200px; }
.section-title { font-weight: 600; margin-bottom: 16px; font-size: 16px; }
.options { display: flex; justify-content: space-between; align-items: center; margin-top: 16px; }
.result { margin-top: 16px; padding: 12px; background: #fff; border-radius: 4px; font-family: monospace; font-size: 14px; }
.current-time { display: flex; align-items: center; gap: 16px; }
.current-time code { font-size: 14px; color: #409eff; padding: 8px 12px; background: #ecf5ff; border-radius: 4px; cursor: pointer; }
.clickable:hover { background: #409eff; color: #fff; }
</style>