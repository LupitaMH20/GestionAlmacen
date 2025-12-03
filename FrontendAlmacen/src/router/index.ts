import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';

import login from '../components/pages/login.vue';
import Admin from '../components/pages/Admin.vue';
import Staff from '../components/pages/Staff.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/admin',
    name: 'admin',
    component: Admin,
    meta: { requiresAuth: true },
    redirect: { name: 'admin-start' },
    children: [
      { path: 'start', name: 'admin-start', component: () => import('../views/Start.vue') },
      { path: 'preApplication', name: 'admin-preApplication', component: () => import("../views/PreApplication.vue") },
      { path: 'application', name: 'admin-application', component: () => import('../views/Application.vue') },
      { path: 'authorize', name: 'admin-authorize', component: () => import('../views/Authorize.vue') },
      { path: 'supply', name: 'admin-supply', component: () => import('../views/Supply.vue') },
      { path: 'archived', name: "admin-archived", component: () => import('../views/Archived.vue') },
      { path: 'user', name: 'admin-user', component: () => import('../views/User.vue') },
      { path: 'company', name: 'admin-company', component: () => import('../views/Company.vue') },
      { path: 'collaborator', name: 'admin-collaborator', component: () => import('../views/Collaborator.vue') },
      { path: 'articles', name: 'admin-articles', component: () => import('../views/Articles.vue') },
      { path: 'report', name: 'admin-report', component: () => import('../views/Reports.vue') },
      { path: 'history', name: 'admin-history', component: () => import('../views/History.vue') },
    ]
  },
  {
    path: '/staff',
    name: 'staff',
    component: Staff,
    meta: { requiresAuth: true },
    redirect: { name: 'staff-start' },
    children: [
      { path: 'start', name: 'staff-start', component: () => import('../views/Start.vue') },
      { path: 'preApplication', name: 'staff-preApplication', component: () => import("../views/PreApplication.vue") },
      { path: 'application', name: 'staff-application', component: () => import('../views/Application.vue') },
      { path: 'authorize', name: 'staff-authorize', component: () => import('../views/Authorize.vue') },
      { path: 'supply', name: 'staff-supply', component: () => import('../views/Supply.vue') },
    ]
  },
  { path: '/', redirect: '/login' },
  { path: '/login', name: 'login', component: login, meta: { requiresGuest: true } }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const userString = sessionStorage.getItem('user');
  const isLoggedIn = !!userString;

  if (to.meta.requiresAuth && !isLoggedIn) {
    next({ name: 'login' });
  }
  else if (to.meta.requiresGuest && isLoggedIn) {
    const user = JSON.parse(sessionStorage.getItem('user')!);
    const position = user.position?.toLowerCase();

    if (['managerJom', 'managerNs', 'managerPrintek', 'managerHefesto', 'managerBlackWorkshop', 'applicant', 'deliberystaff'].includes(position)) {
      next({ name: 'staff' });
    } else if (['director', 'counter'].includes(position)) {
      next({ name: 'admin' });
    } else {
      next();
    }
  }
  else {
    next();
  }
});

export default router;