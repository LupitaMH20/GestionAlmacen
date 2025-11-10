<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { Table, TableBody, TableCaption, TableCell, TableHead, TableHeader, TableRow } from '../components/ui/table'
import CreateUser from '../components/Forms/Users/CreateUser.vue'
import UpdateUser from '../components/Forms/Users/UpdateUser.vue'
import DisableUser from '../components/Forms/Users/DisableUser.vue'
import Input from '../components/ui/input/Input.vue'
import Button from '../components/ui/button/Button.vue'
import { Search } from 'lucide-vue-next'
import { Card, CardHeader, CardTitle, CardContent } from '../components/ui/card';

const users = ref<any[]>([])
const displayedUsers = ref<any[]>([])
const filter = ref<'active' | 'inactive'>('active')
const searchQuery = ref('')

const positionMap: Record<string, string> = {
    "director": "Director",
    "counter": "Contador",
    "managerJom": "Encargado de JOM",
    "managerNs": "Encargado de NARANJA STORE",
    "managerPrintek": "Encargado PRINTEK",
    "managerHefesto": "Encargado HEFESTO",
    "managerBlackWorkshop": "Encargado BLACK GARAGE",
    "applicant": "Solicitante",
    "deliberystaff": "Personal de entrega"
}

const loadUsers = async () => {
    try {
        const url =
            filter.value === 'inactive'
                ? 'http://127.0.0.1:8000/api/users/?inactive=true'
                : 'http://127.0.0.1:8000/api/users/'
        const response = await axios.get(url)
        users.value = response.data
        displayedUsers.value = [...users.value]
    } catch (eror) {

    }
}

const searchUsers = () => {
    const query = searchQuery.value.toLowerCase()
    displayedUsers.value = users.value.filter(user =>
        user.id_user.toLowerCase().includes(query) ||
        user.name.toLowerCase().includes(query) ||
        user.last_name.toLowerCase().includes(query)
    )
}

const handleUserDisabled = (id: string) => {
    users.value = users.value.map(u => u.id_user === id ? { ...u, active: false } : u)
    displayedUsers.value = displayedUsers.value.filter(u => u.id_user !== id)
}

onMounted(() => {
    loadUsers()
})
</script>

<template>
    <div class="flex justify-between items-center w-full mb-2">
        <div class="flex gap-2">
            <Input v-model="searchQuery" placeholder="Buscar usuario" class="w-75 text-12 font-sans font-light" />
            <Button @click="searchUsers"
                class="bg-white text-black hover:bg-black hover:text-white border border-gray-300">
                <Search /> Buscar
            </Button>
        </div>
        <select v-model="filter" @change="loadUsers"
            class="border border-gray-300 rounded-md text-base font-normal px-3 py-1 focus:outline-none focus:ring-2 focus:bg-white">
            <option value="active">Activos</option>
            <option value="inactive">Desactivados</option>
        </select>
    </div>

    <Card class="flex flex-col h-full shadow-lg hover:shadow-xl transition-shadow duration-300">
        <CardHeader>
            <div class="flex justify-between items-center w-full text-black font-sans font-bold text-3xl pt-5">
                <CardTitle> Usuarios </CardTitle>
                <CreateUser @user-created="loadUsers" />
            </div>
        </CardHeader>
        <CardContent>
            <Table>
                <TableCaption>Usuarios registrados.</TableCaption>
                <TableHeader>
                    <TableRow>
                        <TableHead class="w-[100px]">ID</TableHead>
                        <TableHead>Nombre</TableHead>
                        <TableHead>Puesto</TableHead>
                        <TableHead class="text-right">Opciones</TableHead>
                    </TableRow>
                </TableHeader>
                <TableBody>
                    <TableRow v-for="user in displayedUsers" :key="user.id_user">
                        <TableCell class="font-medium">{{ user.id_user }}</TableCell>
                        <TableCell>{{ user.name }}</TableCell>
                        <TableCell>{{ positionMap[user.position] || user.position}}</TableCell>
                        <TableCell v-if="user.active" class="text-right">
                            <div class="flex justify-end items-center gap-4">
                                <UpdateUser :user="user" @update-user="loadUsers" />
                                <DisableUser :id_user="user.id_user" @userDisabled="handleUserDisabled" />
                            </div>
                        </TableCell>
                    </TableRow>
                </TableBody>
            </Table>
        </CardContent>
    </Card>
</template>