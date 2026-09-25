<template>
  <section class="page">
    <header class="page-head">
      <div>
        <h2>运营概览</h2>
        <p class="page-desc">汇总各业务模块的关键指标，先看总量再看异常。</p>
      </div>
    </header>
    <div class="stat-row">
      <article v-for="card in cards" :key="card.label" class="stat-card">
        <span class="stat-label">{{ card.label }}</span>
        <strong class="stat-value">{{ card.value }}</strong>
      </article>
    </div>
    <table class="data-table">
      <thead>
        <tr><th>业务模块</th><th>今日新增</th><th>待处理</th><th>异常量</th></tr>
      </thead>
      <tbody>
        <tr v-for="row in moduleRows" :key="row.name">
          <td>{{ row.name }}</td>
          <td>{{ row.created }}</td>
          <td>{{ row.pending }}</td>
          <td>{{ row.abnormal }}</td>
        </tr>
      </tbody>
    </table>
  </section>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'

import { fetchJson } from '@/api/client'

type Overview = {
  cards: { label: string; value: number }[]
  modules: { name: string; created: number; pending: number; abnormal: number }[]
}

const cards = ref<Overview['cards']>([])
const moduleRows = ref<Overview['modules']>([])

onMounted(async () => {
  try {
    const payload = await fetchJson<Overview>('/api/overview')
    cards.value = payload.cards
    moduleRows.value = payload.modules
  } catch {
    cards.value = [{"label": "业务模块", "value": 0}, {"label": "今日新增", "value": 0}]
    moduleRows.value = [{"name": "藏品建档", "created": 0, "pending": 0, "abnormal": 0}, {"name": "文物本体", "created": 0, "pending": 0, "abnormal": 0}, {"name": "病害调查", "created": 0, "pending": 0, "abnormal": 0}, {"name": "修复方案", "created": 0, "pending": 0, "abnormal": 0}, {"name": "修复工序", "created": 0, "pending": 0, "abnormal": 0}, {"name": "修复材料", "created": 0, "pending": 0, "abnormal": 0}, {"name": "环境监控", "created": 0, "pending": 0, "abnormal": 0}, {"name": "囊匣制作", "created": 0, "pending": 0, "abnormal": 0}, {"name": "三维扫描", "created": 0, "pending": 0, "abnormal": 0}, {"name": "拓片制作", "created": 0, "pending": 0, "abnormal": 0}, {"name": "展陈布置", "created": 0, "pending": 0, "abnormal": 0}, {"name": "借展运输", "created": 0, "pending": 0, "abnormal": 0}, {"name": "虫害防治", "created": 0, "pending": 0, "abnormal": 0}, {"name": "保护验收", "created": 0, "pending": 0, "abnormal": 0}, {"name": "库房排架", "created": 0, "pending": 0, "abnormal": 0}, {"name": "提取使用", "created": 0, "pending": 0, "abnormal": 0}, {"name": "影像采集", "created": 0, "pending": 0, "abnormal": 0}, {"name": "保护日志", "created": 0, "pending": 0, "abnormal": 0}]
  }
})
</script>
