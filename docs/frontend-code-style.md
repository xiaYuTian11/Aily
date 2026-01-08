# 前端代码规范

## 一、技术栈
Vue 3 + TypeScript + Vite + Element Plus + Pinia + Axios

## 二、目录结构
```
src/
├── api/          # API请求
├── components/   # 公共组件
├── composables/  # 组合式函数
├── router/       # 路由
├── stores/       # 状态管理
├── types/        # 类型定义
├── utils/        # 工具函数
└── views/        # 页面
```

## 三、命名规范
| 类型 | 规范 | 示例 |
|------|------|------|
| 组件文件 | PascalCase | `JsonFormat.vue` |
| TS文件 | camelCase | `useClipboard.ts` |
| 常量 | UPPER_SNAKE | `MAX_SIZE` |
| 变量/函数 | camelCase | `userName` |
| 类型/接口 | PascalCase | `UserInfo` |

## 四、组件规范
```vue
<script setup lang="ts">
// 1.导入 2.Props/Emits 3.响应式 4.计算属性 5.方法 6.生命周期
import { ref, computed } from 'vue'
const props = defineProps<{ title: string }>()
const loading = ref(false)
const isValid = computed(() => true)
function submit() {}
</script>
```

## 五、API封装
```typescript
// api/index.ts
import axios from 'axios'
const request = axios.create({ baseURL: '/api', timeout: 30000 })
export default request

// api/dev-tools.ts
export const formatJson = (data: JsonFormatReq) =>
  request.post('/dev/json/format', data)
```

## 六、ESLint配置
```javascript
// .eslintrc.cjs
module.exports = {
  extends: [
    'eslint:recommended',
    '@vue/typescript/recommended',
    'plugin:vue/vue3-recommended',
    'prettier'
  ],
  rules: {
    'vue/multi-word-component-names': 'off',
    '@typescript-eslint/no-explicit-any': 'warn'
  }
}
```

## 七、Prettier配置
```json
{
  "semi": false,
  "singleQuote": true,
  "tabWidth": 2,
  "trailingComma": "none",
  "printWidth": 100
}