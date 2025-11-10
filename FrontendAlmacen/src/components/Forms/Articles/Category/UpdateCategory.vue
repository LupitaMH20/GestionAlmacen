<script setup lang="ts">
import { reactive, ref, watch } from 'vue'
import axios from 'axios';
import Dialog1 from '../../../Elements/Dialog1.vue'
import FormCategoryU from './FormCategoryU.vue';
import { NotebookPen, Box } from 'lucide-vue-next'

const isDialogisOpen = ref(false)
const emit = defineEmits(['updateCategory'])

const props = defineProps<{
    id_Category: string | number,
}>()

watch(isDialogisOpen, (newValue) => {
    if (newValue && props.id_Category) {
        loadata(props.id_Category);

    }
});

const data = reactive({
    id_Category: '',
    name: ''
})

const loadata = async (id: string | number) => {
    try {
        const response = await axios.get(`http://127.0.0.1:8000/api/category/${id}/`);
        const apiData = response.data;

        Object.assign(data, {
            id_Category: apiData.id_Category,
            name: apiData.name
        });
        console.log('Datos de la categoria cargados:', data);
    } catch (error) {
        console.error('No se pudieron cargar los datos de la categoria', error);
    }
}

const apiUpdateCategory = async (data: any) => {
    try {
        console.log('datos', data)
        await axios.post('http://127.0.0.1:8000/api/category/', data)
        console.log('Se registro la categoria', data)
        isDialogisOpen.value = false
        emit('updateCategory')
    } catch (error) {

    }
}

const handelCancel = () => {
    console.log('Se cancelo la edicion de la categoria')
    isDialogisOpen.value = false
}

const handleSave = async () => {
    try {
        await axios.patch(`http://127.0.0.1:8000/api/category/${data.id_Category}/`, data)
        console.log('Categoria actualizada', data)
        isDialogisOpen.value = false
        emit('updateCategory')
    } catch (error) {
        console.log('Error al actualizar la categoria', error)
    }
}
</script>

<template>
    <Dialog1 
        title="Actualizar Categorias" 
        titleButton="Actualizar" 
        :icon-p="NotebookPen" 
        :icon-t="Box"
        @cancel="handelCancel" 
        @save="handleSave" 
        v-model="isDialogisOpen">

        <template #forms>
            <FormCategoryU v-model:props="data"/>
        </template>
    </Dialog1>
</template>