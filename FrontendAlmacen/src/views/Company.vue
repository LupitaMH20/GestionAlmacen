<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios';
import { Table, TableBody, TableCaption, TableCell, TableHead, TableHeader, TableRow } from '../components/ui/table'
import CreateCompany from '../components/Forms/Companies/CreateCompany.vue';
import UpdateCompany from '../components/Forms/Companies/UpdateCompany.vue';
import DeleteCompany from '../components/Forms/Companies/DeleteCompany.vue';
import Input from '../components/ui/input/Input.vue'
import Button from '../components/ui/button/Button.vue'
import { Search } from 'lucide-vue-next'
import { Card, CardHeader, CardTitle, CardContent } from '../components/ui/card';

const companies = ref<any[]>([])
const displayedCompanies = ref<any[]>([])
const filter = ref<'active' | 'inactive'>('active')
const searchQuery = ref('')

const loadCompanies = async () => {
    const url =
        filter.value === 'inactive'
            ? 'http://127.0.0.1:8000/api/companies/?inactive=true'
            : 'http://127.0.0.1:8000/api/companies/'
    const response = await axios.get(url)
    companies.value = response.data
    displayedCompanies.value = [...companies.value]
}

const searchCompanies = () => {
    const query = searchQuery.value.toLowerCase()
    displayedCompanies.value = companies.value.filter(companies =>
        companies.name.toLowerCase().includes(query) ||
        companies.id_Company.toString().includes(query)

    )
}

const handleCompaniesDisabled = (id: String) => {
    companies.value = companies.value.map(u => u.id_Company === id ? { ...u, active: false } : u)
    displayedCompanies.value = displayedCompanies.value.filter(u => u.id_Company !== id)
}

onMounted(() => {
    loadCompanies()
})
</script>

<template>
    <div class="flex justify-between items-center w-full mb-2">
        <div class="flex gap-2">
            <Input v-model="searchQuery" placeholder="Buscar empresa" class="w-75 text-12 font-sans font-light" />
            <Button @click="searchCompanies"
                class="bg-white text-black hover:bg-black hover:text-white border border-gray-300">
                <Search /> Buscar
            </Button>
        </div>
        <select v-model="filter" @change="loadCompanies"
            class="border border-gray-300 rounded-md text-base font-normal px-3 py-1 focus:outline-none focus:ring-2 focus:bg-white">
            <option value="active">Activa</option>
            <option value="inactive">Desactivadas</option>
        </select>
    </div>
    <Card class="flex flex-col h-full shadow-lg hover:shadow-xl transition-shadow duration-300">
        <CardHeader>
            <div class="flex justify-between items-center w-full text-black font-sans font-bold text-3xl pt-5">
                <CardTitle> Empresas </CardTitle>
                <CreateCompany @companyCreate="loadCompanies" />
            </div>
        </CardHeader>
        <CardContent>
            <Table>
                <TableCaption>Empresas registradas.</TableCaption>
                <TableHeader>
                    <TableRow>
                        <TableHead class="w-[100px]"> ID </TableHead>
                        <TableHead>Nombre</TableHead>
                        <TableHead>Dirección</TableHead>
                        <TableHead class="text-right"> Opciones </TableHead>
                    </TableRow>
                </TableHeader>
                <TableBody>
                    <TableRow v-for="company in displayedCompanies" :key="company.id_Company">
                        <TableCell class="font-medium"> {{ company.id_Company }} </TableCell>
                        <TableCell>{{ company.name }}</TableCell>
                        <TableCell>{{ company.address }}</TableCell>
                        <TableCell v-if="company.active" class="text-right">
                            <div class="flex justify-end item-center gap-20">
                                <UpdateCompany :company="company" @UpdateCompany="loadCompanies" />
                                <DeleteCompany :id_Company="company.id_Company"
                                    @disablecompany="handleCompaniesDisabled" />
                            </div>
                        </TableCell>
                    </TableRow>
                </TableBody>
            </Table>
        </CardContent>
    </Card>
</template>