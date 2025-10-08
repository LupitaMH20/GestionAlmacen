import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';

const routes: Array<RouteRecordRaw> = [
  {path: '/', 
    redirect: '/start'},
  { path: '/start', name: 'start', component: () => import('../views/Start.vue') },
  { path: '/application', name: 'application', component: () => import('../views/Application.vue') },
  { path: '/authorize', name: 'authorize', component: () => import('../views/Authorize.vue') },
  { path: '/supply', name: 'supply', component: () => import('../views/Supply.vue') },
  { path: '/deliveries', name: 'deliveries', component: () => import('../views/Deliveries.vue') },
  { path: '/user', name: 'user', component: () => import('../views/User.vue') },
  { path: '/company', name: 'company', component: () => import('../views/Company.vue') },
  { path: '/collaborator', name: 'collaborator', component: () => import('../views/Collaborator.vue') },
  { path: '/report', name: 'report', component: () => import('../views/Reports.vue') },
  { path: '/record', name: 'record', component: () => import('../views/Record.vue') },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;