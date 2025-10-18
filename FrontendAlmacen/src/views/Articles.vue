<script setup lang="ts">
import { Table, TableBody, TableCaption, TableCell, TableHead, TableHeader, TableRow } from '../components/ui/table'
import ArticleCreate from '../components/Forms/Articles/CreateArticle.vue';
import ArticleUpdate from '../components/Forms/Articles/UpdateArticle.vue';
import DeleteArticle from '../components/Forms/Articles/DeleteArticle.vue';
import Category from '../components/Forms/Articles/Category.vue';
import Input from '../components/ui/input/Input.vue';
import Button from '../components/ui/button/Button.vue';
import { Search } from 'lucide-vue-next';
import { onMounted, ref } from 'vue';
import axios from 'axios';
import { loadavg } from 'os';

const props = defineProps<{
    article: {
        articleId: string | number;
    };
    companies: any[];
    loadArticle: () => void;
}>();
const isEditModalOpen = ref(false);
const openEditModal = () => {
    isEditModalOpen.value = true;
};

const companies = ref<any[]>([])
const articles = ref<any[]>([])
const displayedArticles = ref<any[]>([])
const searchQuery = ref('')
const filter = ref<'active' | 'inactive'>('active')

const loadArticle = async () => {
    try {
        const url =
            filter.value == 'inactive'
                ? 'http://127.0.0.1:8000/api/article/?inactive=true'
                : 'http://127.0.0.1:8000/api/article/'
        const response = await axios.get(url)
        articles.value = response.data
        displayedArticles.value = [...articles.value]
    } catch (errror) {

    }
}

const loadCompany = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/companies/')
        companies.value = response.data
    } catch (error) {
        console.log('error al mostrar', error)
    }
}

const searchArticle = () => {
    const query = searchQuery.value.toLowerCase()
    displayedArticles.value = articles.value.filter(article =>
        article.id_mainarticle.toLowerCase().includes(query) ||
        article.id_alternativearticle.toLowerCase().includes(query) ||
        article.name.toLowerCase().includes(query)
    )
}

const handleArticleDisabled = (id: string) => {
    articles.value = articles.value.map(u => u.id_mainarticle === id ? { ...u, active: false } : u)
    displayedArticles.value = displayedArticles.value.filter(u => u.id_mainarticle !== id)
}

onMounted(() => {
    loadArticle(),
    loadCompany()
})

</script>

<template>
    <div class="flex justify-between items-center w-full mb-2">
        <div class="flex gap-2">
            <Input v-model="searchQuery" placeholder="Buscar colaborador" class="w-75 text-12 font-sans font-light" />
            <Button @click="searchArticle"
                class="bg-white text-black hover:bg-black hover:text-white border border-gray-300">
                <Search /> Buscar
            </Button>
        </div>
        <select v-model="filter" @change="loadArticle"
            class="border border-gray-300 rounded-md text-base font-normal px-3 py-1 focus:outline-none focus:ring-2 focus:bg-white">
            <option value="active">Activa</option>
            <option value="inactive">Desactiva</option>
        </select>
    </div>
    <div class="flex justify-between items-center w-full text-black font-sans font-bold text-3xl">
        Articulos
        <div class="flex items-center gap-2">
            <ArticleCreate @creatArticle="loadArticle"/>
            <Category @createCategory="loadArticle"/>
        </div>

    </div>
    <Table>
        <TableCaption>Articulos registrados.</TableCaption>
        <TableHeader>
            <TableRow>
                <TableHead class="w-[100px]"> ID Principal</TableHead>
                <TableHead class="w-[100px]"> ID Alternativo</TableHead>
                <TableHead>Nombre</TableHead>
                <TableHead>Cantidad</TableHead>
                <TableHead>Precio</TableHead>
                <TableHead>Descripción</TableHead>
                <TableHead>Categoria</TableHead>
                <TableHead>Empresa</TableHead>
                <TableHead class="text-right"> Opciones </TableHead>
            </TableRow>
        </TableHeader>
        <TableBody>
            <TableRow v-for="article in displayedArticles" :key="article.id_mainarticle">
                <TableCell class="font-medium">{{ article.id_mainarticle }} </TableCell>
                <TableCell class="font-medium">{{ article.id_alternativearticle }}</TableCell>
                <TableCell>{{ article.name }}</TableCell>
                <TableCell>{{ article.stock }}</TableCell>
                <TableCell>{{ article.price }}</TableCell>
                <TableCell>{{ article.description }}</TableCell>
                <TableCell>{{ article.category }}</TableCell>
                <TableCell>{{ article.company_name }}</TableCell>
                <TableCell v-if="article.active" class="text-right">
                    <div class="flex justify-end item-center gap-10">
                        <ArticleUpdate :id_mainarticle="article.id_mainarticle" :companies="companies" @updateArticle="loadArticle"/>
                        <DeleteArticle :id_mainarticle="article.id_mainarticle" @disableArticle="handleArticleDisabled"/>
                    </div>
                </TableCell>
            </TableRow>
        </TableBody>
    </Table>
</template>