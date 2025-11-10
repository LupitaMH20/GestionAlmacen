<script setup lang="ts">
import { ref, provide, readonly, onMounted } from 'vue'

interface User {
  id_user: string;
  name: string;
  position: string;
  admin: boolean;
}

const user = ref<User | null>(null)

function login(userData: User, authToken: string | null) {
  console.log('App.vue: loginAction llamada', userData); 
  user.value = userData;
  localStorage.setItem('user', JSON.stringify(userData)); 
}

function logout() {
  console.log('App.vue: logoutAction llamada');
  user.value = null;
  localStorage.removeItem('user');
  localStorage.removeItem('token');
}

onMounted(() => {
  const storedUser = localStorage.getItem('user');
  if (storedUser) {
    user.value = JSON.parse(storedUser);
  }
  console.log('App.vue montado, usuario cargado:', user.value);
})

provide('loggedInUser', readonly(user));
provide('loginAction', login);
provide('logoutAction', logout);
</script>

<template>
  <router-view />
</template>