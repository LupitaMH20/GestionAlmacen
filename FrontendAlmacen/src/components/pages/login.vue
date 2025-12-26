<script setup lang="ts">
import { ref, inject } from 'vue'
import { useRouter } from 'vue-router'
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from '../ui/card'
import { Input } from '../ui/input'
import { Button } from '../ui/button'
import { Lock, User, Eye, EyeOff } from 'lucide-vue-next'
import axios from 'axios'

const router = useRouter()
const name = ref('')
const password = ref('')
const errorMessage = ref('')
const showPassword = ref(false)

const loginAction = inject<Function>('loginAction')

const toggleShowPassword = () => {
    showPassword.value = !showPassword.value
}

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
        if (['applicant', 'deliberystaff'].includes(position)) {
            router.push('/staff')
        } else if (['director', 'counter'].includes(position)) {
            router.push('/admin')
        } else if (['managerjom', 'managerns', 'managerprintek', 'managerhefesto', 'managerblackworkshop', 'managerelektra'].includes(position)) {
            router.push('/manager')
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
    <div class="flex flex-col items-center justify-center min-h-screen bg-gradient-to-br from-orange-400 via-orange-700 to-orange-950">
        <h1 class="text-white text-6xl font-bold mb-8 text-center">CONSUMO INTERNO</h1>
        <div>
            <Card
            class="w-[750px] h-[550px] bg-amber-50/5 backdrop-blur-lg text text-amber-50 rounded-2xl shadow-xl border border-stone-100">
            <CardHeader class="text-center pt-8">
                <CardTitle class="flex flex-col items-center justify-center text-4xl font-bold mb-2">
                    <div class="bg-amber-50 rounded-full p-4 mb-4">
                        <User class="w-25 h-25 text-stone-500" />
                    </div>
                    Iniciar Sesión
                </CardTitle>
            </CardHeader>

            <CardContent class="space-y-6 px-20 mt-2">
                <div class="relative h-10">
                    <User class="absolute left-3 top-3 text-black-50 w-10 h-10" />
                    <Input v-model="name" placeholder="Usuario"
                        class="pl-15 text-3xl border-amber-50 text-black-50 placeholder-white focus:ring-black h-15" />
                </div>
                <div class="relative h-10 pt-2">
                    <Lock class="absolute left-3 top-3 text-black-50 w-10 h-10" />
                    <Input :type="showPassword ? 'text' : 'password'" v-model="password" placeholder="Contraseña"
                        class="pl-15 pr-10 bg-transparent border-amber-50 text-black-50 placeholder-white focus:ring-black h-15 text-3xl" />
                    <div class="absolute right-3 top-3 cursor-pointer" @click="toggleShowPassword">
                        <Eye v-if="!showPassword" class="pt-2 text-black-50 w-10 h-10" />
                        <EyeOff v-else class="text-black-50 w-10 h-10" />
                    </div>
                </div>
            </CardContent>

            <CardFooter class="flex justify-end pt-8 ">
                <Button @click="handleLogin"
                    class="w-35 h-15 bg-transparent border border-white text-amber-50 font-bold rounded-lg transition-all">
                    Iniciar sesión
                </Button>
            </CardFooter>
        </Card>
        </div>
    </div>
</template>