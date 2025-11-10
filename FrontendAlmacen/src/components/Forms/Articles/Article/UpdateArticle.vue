<script setup lang="ts">
import { ref, reactive, watch, onMounted } from 'vue'
import axios from 'axios';
import Dialog2 from '../../../Elements/Dialog2.vue';
import { NotebookPen, FileSpreadsheet, PackageOpen } from 'lucide-vue-next';
import FormArticleU1 from './FormArticleU1.vue';
import FormArticleU2 from './FormArticleU2.vue';

const category = ref<any[]>([]);
const companies = ref<any[]>([]);

const props = defineProps<{ 
    id_mainarticle: string | number,    
}>()

const isDialogOpen = ref(false)
const emit = defineEmits(['updateArticle'])

watch(isDialogOpen, (newValue) => {
    if (newValue && props.id_mainarticle) {
        loadata(props.id_mainarticle);
    }
});

const data = reactive({
    id_mainarticle: '',
    alternativearticle: '',
    name: '',
    stock: 0,
    price: 0,
    description: '',
    category: '',
    company: ''
});

onMounted(async () => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/companies/');
        companies.value = response.data;
        console.log('Categorías cargadas:', companies.value);
    } catch (error) {
        console.error('No se pudieron cargar las empresas', error);
    }
    
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/category/');
        category.value = response.data;
        console.log('Categorías cargadas:', category.value);
    } catch (error) {
        console.error('No se pudieron cargar las categorías', error);
    }
});

const loadata = async (id: string | number) => {
    try {
        const response = await axios.get(`http://127.0.0.1:8000/api/article/${id}/`);
        const apiData = response.data;

        Object.assign(data, {
            id_mainarticle: apiData.id_mainarticle,
            alternativearticle: apiData.alternativearticle,
            name: apiData.name,
            stock: apiData.stock,
            price: apiData.price,
            description: apiData.description || '',
            category: apiData.category || apiData.category,
            company: apiData.companyId || apiData.company
        });
        
        console.log('Datos cargados:', data);
    } catch (error) {
        console.log('No se pudo cargar los datos del articulo', error)
    }
}

const handleCancel = () => {
    console.log("Acción de Cancelar");
    isDialogOpen.value = false
};

const handleSave = async() => {
    try{
        await axios.patch(`http://127.0.0.1:8000/api/article/${props.id_mainarticle}/`, data)
        console.log('Datos guardados:', data)
        isDialogOpen.value = false
        emit('updateArticle')
    }catch(error){
        console.log('No se guardo la actualización de los datos', error)
    }
};
</script>

<template>
    <Dialog2 
        title="Actualizar producto" 
        titleButton="Actualizar"
        :iconP="NotebookPen" 
        :iconT="NotebookPen" 
        recordof="Producto"
        :IconOf="PackageOpen" 
        description="Descripción" 
        :IconD="FileSpreadsheet" 
        @cancel="handleCancel"
        @save="handleSave"
        v-model:open="isDialogOpen">

        <template #form1>
            <FormArticleU1 v-model:props="data"/>
        </template>
        <template #form2>
            <FormArticleU2 v-model:props="data" :companies="companies" :category="category"/>
        </template>
    </Dialog2>
</template>