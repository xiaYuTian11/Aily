import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      component: () => import('@/layouts/DefaultLayout.vue'),
      children: [
        { path: '', name: 'Home', component: () => import('@/views/Home.vue') },
        // 编程工具
        { path: 'dev/json', name: 'JsonFormat', component: () => import('@/views/dev-tools/JsonFormat.vue') },
        { path: 'dev/base64', name: 'Base64', component: () => import('@/views/dev-tools/Base64.vue') },
        { path: 'dev/hash', name: 'Hash', component: () => import('@/views/dev-tools/Hash.vue') },
        { path: 'dev/timestamp', name: 'Timestamp', component: () => import('@/views/dev-tools/Timestamp.vue') },
        { path: 'dev/idcard', name: 'IdCard', component: () => import('@/views/dev-tools/IdCard.vue') },
        // AI工具
        { path: 'ai/image-compress', name: 'ImageCompress', component: () => import('@/views/ai-tools/ImageCompress.vue') },
        { path: 'ai/qrcode', name: 'Qrcode', component: () => import('@/views/ai-tools/Qrcode.vue') },
        { path: 'ai/translate', name: 'Translate', component: () => import('@/views/ai-tools/Translate.vue') },
        { path: 'ai/convert', name: 'FileConvert', component: () => import('@/views/ai-tools/FileConvert.vue') },
        { path: 'ai/watermark', name: 'Watermark', component: () => import('@/views/ai-tools/Watermark.vue') },
      ]
    }
  ]
})

export default router