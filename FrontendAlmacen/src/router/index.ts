import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';

const routes: Array<RouteRecordRaw> = [
  {path: '/', redirect: '/start'},
  { path: '/start', name: 'start', component: () => import('../views/Start.vue') },
  { path: '/preApplication', name:'preApplication', component: () => import("../views/PreApplication.vue") },
  { path: '/application', name: 'application', component: () => import('../views/Application.vue') },
  { path: '/authorize', name: 'authorize', component: () => import('../views/Authorize.vue') },
  { path: '/supply', name: 'supply', component: () => import('../views/Supply.vue') },
  { path: '/finished', name: 'deliveries', component: () => import('../views/Finish.vue') },
  { path: '/user', name: 'user', component: () => import('../views/User.vue') },
  { path: '/company', name: 'company', component: () => import('../views/Company.vue') },
  { path: '/collaborator', name: 'collaborator', component: () => import('../views/Collaborator.vue') },
  { path: '/articles', name: 'articles', component: () => import('../views/Articles.vue') },
  { path: '/report', name: 'report', component: () => import('../views/Reports.vue') },
  { path: '/history', name: 'history', component:() => import('../views/History.vue') }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;