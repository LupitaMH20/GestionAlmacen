<script setup lang="ts">
import { ref, inject } from 'vue'
import { useRouter } from 'vue-router'
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from '../ui/card'
import { Input } from '../ui/input'
import { Button } from '../ui/button'
import { Lock, User } from 'lucide-vue-next'
import axios from 'axios'

const router = useRouter()
const name = ref('')
const password = ref('')
const errorMessage = ref('')

const loginAction = inject<Function>('loginAction')

const handleLogin = async () => {
    errorMessage.value = ''

    if (!name.value || !password.value) {
        errorMessage.value = 'Por favor, complete todos los campos.'
        alert(errorMessage.value)
        return
    }

    try {
        const response = await axios.post('http://127.0.0.1:8000/api/users/login/', {
            name: name.value,
            password: password.value
        })

        const { user, access, refresh } = response.data

        if (!access || !user) {
            throw new Error('El servidor no devolvió token o usuario.')
        }

        // Guarda los tokens en localStorage
        localStorage.setItem('access', access)
        localStorage.setItem('refresh', refresh)
        localStorage.setItem('user', JSON.stringify(user))
        if (loginAction) {
            loginAction(user, access)
        }

        const position = user.position?.toLowerCase()
        if (['managerjom', 'managerns', 'managerprintek', 'managerhefesto', 'managerblackworkshop', 'applicant', 'deliberystaff'].includes(position)) {
            router.push('/staff')
        } else if (['director', 'counter'].includes(position)) {
            router.push('/admin')
        } else {
            router.push('/home')
        }

        alert(`Bienvenido ${user.name}`)

    } catch (error: any) {
        console.error('Error de login:', error)
        if (error.response?.status === 401) {
            errorMessage.value = 'Usuario o contraseña incorrectos'
        } else if (error.response?.status === 403) {
            errorMessage.value = 'Usuario inactivo'
        } else {
            errorMessage.value = 'Error en el servidor. Intenta más tarde.'
        }
        alert(errorMessage.value)
    }
}
</script>

<template>
    <div class="flex items-center justify-center min-h-screen bg-gradient-to-br">
        <Card
            class="w-[350px] h-[350px] bg-white/10 backdrop-blur-lg text-white rounded-2xl shadow-xl border border-white/20">
            <CardHeader class="text-center">
                <CardTitle class="flex flex-col items-center justify-center text-2xl font-semibold mb-2">
                    <div class="bg-black/20 rounded-full p-4 mb-2">
                        <User class="w-10 h-10 text-black" />
                    </div>
                    Iniciar Sesión
                </CardTitle>
            </CardHeader>

            <CardContent class="space-y-4">
                <div class="relative">
                    <User class="absolute left-3 top-3 text-gray-400 w-5 h-5" />
                    <Input v-model="name" placeholder="Usuario"
                        class="pl-10 bg-white/20 border border-white/30 text-black placeholder-gray-300" />
                </div>
                <div class="relative">
                    <Lock class="absolute left-3 top-3 text-gray-400 w-5 h-5" />
                    <Input type="password" v-model="password" placeholder="Contraseña"
                        class="pl-10 bg-white/20 border border-white/30 text-black placeholder-gray-300" />
                </div>
            </CardContent>

            <CardFooter>
                <Button @click="handleLogin"
                    class="w-full bg-gray-100 text-black font-semibold py-2 rounded-lg transition-all">
                    Iniciar sesión
                </Button>
            </CardFooter>
        </Card>
    </div>
</template>