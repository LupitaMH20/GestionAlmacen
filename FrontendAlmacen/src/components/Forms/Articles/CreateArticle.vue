<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue'
import axios from 'axios';
import Dialog2 from '../../Elements/Dialog2.vue';
import { Plus, ArchiveRestore, FileSpreadsheet, PackageOpen } from 'lucide-vue-next';
import FormArticleC1 from './FormArticleC1.vue';
import FormArticleC2 from './FormArticleC2.vue'

const prop = defineProps<{ companies: any[], categories: any[] }>()
const isDialogOpen = ref(false)
const emit = defineEmits(['creatArticle'])

const articleData = reactive({
    id_mainarticle: '',
    id_alternativearticle: '',
    name: '',
    stock: 0,
    price: 0,
    description: '',
    category: '',
    company: ''
});

const handleCancel = () => {
    console.log("Acción de Cancelar");
    isDialogOpen.value = false
    Object.assign(articleData, {
        id_mainarticle: '',
        id_alternativearticle: '',
        name: '',
        stock: 0,
        money: 0,
        description: '',
        caategory: '',
        company: ''
    })
};

const handleSave = async () => {
    try {
        console.log('datos', articleData)
        await axios.post('http://127.0.0.1:8000/api/article/', articleData)
        console.log('Datos de ariculos ', articleData)
        isDialogOpen.value = false
        emit('creatArticle')
    } catch (error) {
        console.log('No se realizo el registro de los aticulos', error)
    }
};
</script>

<template>
    <Dialog2 
        title="Registro de producto" 
        titleButton="Producto"
        :iconP="Plus" 
        :iconT="ArchiveRestore" 
        recordof="Producto"
        :IconOf="PackageOpen" 
        description="Descripción" 
        :IconD="FileSpreadsheet" 
        @cancel="handleCancel"
        @save="handleSave"
        v-model:open="isDialogOpen">

        <template #form1>
            <FormArticleC1 v-model:props="articleData" />
        </template>
        <template #form2>
            <FormArticleC2 v-model:props="articleData" :companies="prop.companies" :category="prop.categories"/>
        </template>
    </Dialog2>
</template>