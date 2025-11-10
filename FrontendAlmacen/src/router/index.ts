import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
const routes: Array<RouteRecordRaw> = [
  { path: '/', redirect: '/start' },
  { path: '/start', name: 'start', component: () => import('../views/Start.vue'), meta: { requiresAuth: true } },
  { path: '/preApplication', name: 'preApplication', component: () => import("../views/PreApplication.vue"), meta: { requiresAuth: true } },
  { path: '/application', name: 'application', component: () => import('../views/Application.vue'), meta: { requiresAuth: true } },
  { path: '/authorize', name: 'authorize', component: () => import('../views/Authorize.vue'), meta: { requiresAuth: true } },
  { path: '/supply', name: 'supply', component: () => import('../views/Supply.vue'), meta: { requiresAuth: true } },
  { path: '/finished', name: 'deliveries', component: () => import('../views/Finish.vue'), meta: { requiresAuth: true } },
  { path: '/user', name: 'user', component: () => import('../views/User.vue'), meta: { requiresAuth: true } },
  { path: '/company', name: 'company', component: () => import('../views/Company.vue'), meta: { requiresAuth: true } },
  { path: '/collaborator', name: 'collaborator', component: () => import('../views/Collaborator.vue'), meta: { requiresAuth: true } },
  { path: '/articles', name: 'articles', component: () => import('../views/Articles.vue'), meta: { requiresAuth: true } },
  { path: '/report', name: 'report', component: () => import('../views/Reports.vue'), meta: { requiresAuth: true } },
  { path: '/history', name: 'history', component: () => import('../views/History.vue'), meta: { requiresAuth: true } },

  { path: '/admin', name: 'admin', component: () => import('../components/pages/Admin.vue'), meta: { requiresAuth: true } },
  { path: '/staff', name: 'staff', component: () => import('../components/pages/Staff.vue'), meta: { requiresAuth: true } },

  { path: '/login', name: 'login', component: () => import('../components/pages/login.vue'), meta: { requiresGuest: true } }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});
router.beforeEach((to, from, next) => {
  
  const userString = localStorage.getItem('user');
  const isLoggedIn = !!userString;

  if (to.meta.requiresAuth && !isLoggedIn) {
    next({ name: 'login' });
  } 
  else if (to.meta.requiresGuest && isLoggedIn) {
    const user = JSON.parse(userString!);
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