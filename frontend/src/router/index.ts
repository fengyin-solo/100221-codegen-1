import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Collection = () => import('@/views/collection/index.vue')
const Relic = () => import('@/views/relic/index.vue')
const Disease = () => import('@/views/disease/index.vue')
const Scheme = () => import('@/views/scheme/index.vue')
const Process = () => import('@/views/process/index.vue')
const Material = () => import('@/views/material/index.vue')
const Environment = () => import('@/views/environment/index.vue')
const Box = () => import('@/views/box/index.vue')
const Scan = () => import('@/views/scan/index.vue')
const Rubbing = () => import('@/views/rubbing/index.vue')
const Exhibit = () => import('@/views/exhibit/index.vue')
const Transport = () => import('@/views/transport/index.vue')
const Pest = () => import('@/views/pest/index.vue')
const Accept = () => import('@/views/accept/index.vue')
const Shelf = () => import('@/views/shelf/index.vue')
const Extract = () => import('@/views/extract/index.vue')
const Photo = () => import('@/views/photo/index.vue')
const Log = () => import('@/views/log/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/collection', name: 'collection', component: Collection },
    { path: '/relic', name: 'relic', component: Relic },
    { path: '/disease', name: 'disease', component: Disease },
    { path: '/scheme', name: 'scheme', component: Scheme },
    { path: '/process', name: 'process', component: Process },
    { path: '/material', name: 'material', component: Material },
    { path: '/environment', name: 'environment', component: Environment },
    { path: '/box', name: 'box', component: Box },
    { path: '/scan', name: 'scan', component: Scan },
    { path: '/rubbing', name: 'rubbing', component: Rubbing },
    { path: '/exhibit', name: 'exhibit', component: Exhibit },
    { path: '/transport', name: 'transport', component: Transport },
    { path: '/pest', name: 'pest', component: Pest },
    { path: '/accept', name: 'accept', component: Accept },
    { path: '/shelf', name: 'shelf', component: Shelf },
    { path: '/extract', name: 'extract', component: Extract },
    { path: '/photo', name: 'photo', component: Photo },
    { path: '/log', name: 'log', component: Log },
  ],
})

export default router
