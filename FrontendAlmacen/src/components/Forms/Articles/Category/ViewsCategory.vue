<script setup lang="ts">
import { Table, TableBody, TableCaption, TableCell, TableHead, TableHeader, TableRow } from '../../../ui/table'
import CreateCategory from './CreateCategory.vue';
import UpdateCategory from './UpdateCategory.vue';
import DeleteCategory from './DeleteCategory.vue';
import Input from '../../../ui/input/Input.vue';
import Button from '../../../ui/button/Button.vue';
import { Search } from 'lucide-vue-next';
import { onMounted, ref } from 'vue';
import axios from 'axios';
import { Card, CardHeader, CardTitle, CardContent } from '../../../ui/card';

const category = ref<any[]>([])
const displayedCategory = ref<any[]>([])
const searchQuery = ref('')
const filter = ref<'active' | 'inactive'>('active')

const loadCategory = async () => {
    try {
        const url =
            filter.value == 'inactive'
                ? 'http://127.0.0.1:8000/api/article/?inactive=true'
                : 'http://127.0.0.1:8000/api/category/'
        const response = await axios.get(url)
        category.value = response.data
        displayedCategory.value = [...category.value]
    } catch (errror) {

    }
}

const searchCategory = () => {
    const query = searchQuery.value.toLowerCase()
    displayedCategory.value = category.value.filter(category =>
        // category.id_Category.toLowerCase().includes(query) ||
        category.name.toLowerCase().includes(query) ||
        category.id_Category.toLowerCase().includes(query)
    )
}

const handleCategoryDisabled = (id: string) => {
    category.value = category.value.map(u => u.id_Category === id ? { ...u, active: false } : u)
    displayedCategory.value = displayedCategory.value.filter(u => u.id_Category !== id)
}

onMounted(() => { loadCategory() })

</script>

<template>
    <Card class="flex flex-col h-full shadow-lg hover:shadow-xl transition-shadow duration-300">
        <CardHeader>
            <div class="flex justify-between items-center w-full mb-2">
                <div class="flex gap-2">
                    <Input v-model="searchQuery" placeholder="Buscar categoria"
                        class="w-75 text-12 font-sans font-light" />
                    <Button @click="searchCategory"
                        class="bg-white text-black hover:bg-black hover:text-white border border-gray-300">
                        <Search /> Buscar
                    </Button>
                </div>
                <select v-model="filter" @change="loadCategory"
                    class="border border-gray-300 rounded-md text-base font-normal px-3 py-1 focus:outline-none focus:ring-2 focus:bg-white">
                    <option value="active">Activa</option>
                    <option value="inactive">Desactiva</option>
                </select>
            </div>

            <div class="flex justify-between items-center w-full text-black font-sans font-bold text-3xl pt-5">
                <CardTitle> Categorias</CardTitle>
                <div class="flex items-center gap-2">
                    <CreateCategory @createCategory="loadCategory" />
                </div>
            </div>
        </CardHeader>
        <CardContent>
            <Table>
                <TableCaption>Categorias registrados.</TableCaption>
                <TableHeader>
                    <TableRow>
                        <TableHead> ID Categoria </TableHead>
                        <TableHead> Nombre </TableHead>
                        <TableHead class="text-right"> Opciones </TableHead>
                    </TableRow>
                </TableHeader>
                <TableBody>
                    <TableRow v-for="category in displayedCategory" :key="category.id_Category">
                        <TableCell class="font-medium">{{ category.id_Category }} </TableCell>
                        <TableCell>{{ category.name }}</TableCell>
                        <TableCell v-if="category.active" class="text-right">
                            <div class="flex justify-end item-center gap-10">
                                <UpdateCategory :id_Category="category" @updateCategory="loadCategory" />
                                <DeleteCategory :id_Category="category" @deleteCategory="handleCategoryDisabled" />
                            </div>
                        </TableCell>
                    </TableRow>
                </TableBody>
            </Table>
        </CardContent>
    </Card>
</template>