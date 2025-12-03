<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios';
import Input from '../components/ui/input/Input.vue'
import Button from '../components/ui/button/Button.vue'
import { Search } from 'lucide-vue-next'
import { Table, TableBody, TableCaption, TableCell, TableHead, TableHeader, TableRow } from '../components/ui/table'
import CreateCollaborator from '../components/Forms/Collaborators/CreateCollaborator.vue';
import UpdateCollaborator from '../components/Forms/Collaborators/UpdateCollaborator.vue';
import DeleteCollaborator from '../components/Forms/Collaborators/DeleteCollaborator.vue';
import { Card, CardHeader, CardTitle, CardContent } from '../components/ui/card';

const collaborator = ref<any[]>([])
const company = ref<any[]>([])
const displayedCollaborator = ref<any[]>([])
const filter = ref<'active' | 'inactive'>('active')
const searchQuery = ref('')

const positionMap: Record<string, string> = {
    "director": "Director",
    "counter": "Contador",
    "manager": "Encargado",
    "storekeeper": "Almacenista",
    "display": "Mostrador"
}

const loadCollaborator = async () => {
    const url =
        filter.value === 'inactive'
            ? 'http://127.0.0.1:8000/api/collaborator/?inactive=true'
            : 'http://127.0.0.1:8000/api/collaborator/'
    const response = await axios.get(url)
    collaborator.value = response.data
    displayedCollaborator.value = [...collaborator.value]
}

const loadCompanies = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/companies/')
        company.value = response.data
    } catch (error) {
        console.error("Error al cargar empresas:", error);
    }
}

const searchCollaborator = () => {
    const query = searchQuery.value.toLowerCase()
    displayedCollaborator.value = collaborator.value.filter(collaborator =>
        collaborator.id_Collaborator.toLowerCase().includes(query) ||
        collaborator.name.toLowerCase().includes(query) ||
        collaborator.last_name.toLowerCase().includes(query) ||
        collaborator.company_name.toLowerCase().includes(query)
    )
}

const handleCollaboratorDisabled = (id: String) => {
    collaborator.value = collaborator.value.map(u => u.id_Collaborator === id ? { ...u, active: false } : u)
    displayedCollaborator.value = displayedCollaborator.value.filter(u => u.id_Collaborator !== id)
}

onMounted(() => {
    loadCollaborator(),
        loadCompanies()
})
</script>

<template>
    <div class="flex justify-between items-center w-full mb-2">
        <div class="flex gap-2">
            <Input v-model="searchQuery" placeholder="Buscar colaborador" class="w-75 text-12 font-sans font-light" />
            <Button @click="searchCollaborator"
                class="bg-white text-black hover:bg-black hover:text-white border border-gray-300">
                <Search /> Buscar
            </Button>
        </div>
        <select v-model="filter" @change="loadCollaborator"
            class="border border-gray-300 rounded-md text-base font-normal px-3 py-1 focus:outline-none focus:ring-2 focus:bg-white">
            <option value="active">Activa</option>
            <option value="inactive">Desactivado</option>
        </select>
    </div>
    <Card class="flex flex-col h-full shadow-lg hover:shadow-xl transition-shadow duration-300">
        <CardHeader>
            <div class="flex justify-between items-center w-full text-black font-sans font-bold text-3xl pt-5">
                <CardTitle> Colaboradores </CardTitle>
                <CreateCollaborator @collaboratorCreate="loadCollaborator" />
            </div>
        </CardHeader>
        <CardContent>
            <Table>
                <TableCaption>Colaboradores registrados.</TableCaption>
                <TableHeader>
                    <TableRow>
                        <TableHead class="w-[100px]"> ID </TableHead>
                        <TableHead>Nombre</TableHead>
                        <TableHead>Apellido</TableHead>
                        <TableHead>Puesto</TableHead>
                        <TableHead>Empresa</TableHead>
                        <TableHead>Dirección</TableHead>
                        <TableHead>Telefono</TableHead>
                        <TableHead class="text-right"> Opciones </TableHead>
                    </TableRow>
                </TableHeader>
                <TableBody>
                    <TableRow v-for="collaborator in displayedCollaborator" :key="collaborator.id_Collaborator">
                        <TableCell class="font-medium"> {{ collaborator.id_Collaborator }} </TableCell>
                        <TableCell>{{ collaborator.name }}</TableCell>
                        <TableCell>{{ collaborator.last_name }}</TableCell>
                        <TableCell>{{ positionMap[collaborator.position] || collaborator.position}}</TableCell>
                        <TableCell>{{ collaborator.company_name }}</TableCell>
                        <TableCell>{{ collaborator.address }}</TableCell>
                        <TableCell>{{ collaborator.phone }}</TableCell>
                        <TableCell v-if="collaborator.active" class="text-right">
                            <div class="flex justify-end item-center gap-4">
                                <UpdateCollaborator :collaborator="collaborator" :company="company"
                                    @updateCollaborator="loadCollaborator" />
                                <DeleteCollaborator :id_Collaborator="collaborator.id_Collaborator"
                                    @disableCollaborator="handleCollaboratorDisabled" />
                            </div>
                        </TableCell>
                    </TableRow>
                </TableBody>
            </Table>
        </CardContent>
    </Card>
</template>