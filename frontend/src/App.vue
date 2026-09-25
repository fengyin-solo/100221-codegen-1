<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">文物藏品保护修复平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向博物馆藏品建档、病害调查、修复方案编制、修复工序实施与展陈环境监控的一体化保护修复后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "藏品建档", path: "/collection" }, { label: "文物本体", path: "/relic" }, { label: "病害调查", path: "/disease" }, { label: "修复方案", path: "/scheme" }, { label: "修复工序", path: "/process" }, { label: "修复材料", path: "/material" }, { label: "环境监控", path: "/environment" }, { label: "囊匣制作", path: "/box" }, { label: "三维扫描", path: "/scan" }, { label: "拓片制作", path: "/rubbing" }, { label: "展陈布置", path: "/exhibit" }, { label: "借展运输", path: "/transport" }, { label: "虫害防治", path: "/pest" }, { label: "保护验收", path: "/accept" }, { label: "库房排架", path: "/shelf" }, { label: "提取使用", path: "/extract" }, { label: "影像采集", path: "/photo" }, { label: "保护日志", path: "/log" }]
</script>
