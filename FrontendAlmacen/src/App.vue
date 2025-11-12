<script setup lang="ts">
import { ref, provide, readonly, onMounted } from 'vue'

interface User {
  id_user: string;
  name: string;
  position: string;
  admin: boolean;
}

const user = ref<User | null>(null)
const token = ref<string | null>(null)

function login(userData: User, authToken: string | null) {
  console.log('App.vue: loginAction llamada', userData); 
  user.value = userData;
  sessionStorage.setItem('user', JSON.stringify(userData)); 

  if(authToken){
    token.value = authToken;
    sessionStorage.setItem('token', authToken);
  }
}

function logout() {
  console.log('App.vue: logoutAction llamada');
  user.value = null;
  token.value = null;
  sessionStorage.removeItem('user');
  sessionStorage.removeItem('token');
}

onMounted(() => {
  const storedUser = sessionStorage.getItem('user');
  const storedToken = sessionStorage.getItem('token');
  
  if (storedUser) {
    user.value = JSON.parse(storedUser);
  }
  if (storedToken) {
    token.value = storedToken;
  }
})

provide('loggedInUser', readonly(user));
provide('loginAction', login);
provide('logoutAction', logout);
</script>

<template>
  <router-view />
</template>