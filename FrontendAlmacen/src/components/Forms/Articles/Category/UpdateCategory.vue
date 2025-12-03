<script setup lang="ts">
import { reactive, ref, watch } from 'vue'
import axios from 'axios';
import Dialog1 from '../../../Elements/Dialog1.vue'
import FormCategoryU from './FormCategoryU.vue';
import { NotebookPen, Box } from 'lucide-vue-next'

const props = defineProps<{
    id_Category: string | number,
    name: string
}>()

const formRef = ref<any>(null)
const isDialogisOpen = ref(false)
const emit = defineEmits(['updateCategory'])

const handelCancel = () => {
    console.log('Se cancelo la edicion de la categoria')
    isDialogisOpen.value = false
}

const apiUpdateCategory = async (data: any) => {
    try {
        console.log('datos', data)
        await axios.patch(`http://127.0.0.1:8000/api/category/${props.id_Category}/`, data)
        console.log('Se actualizo la categoria', data)
        isDialogisOpen.value = false
        emit('updateCategory')
    } catch (error) {
        console.log('No se pudo actualizar el colaborador', error)
    }
}

const handleSave = async () => {
    if (formRef.value) {
        const data = formRef.value.submitForm()
        if (data) {
            apiUpdateCategory(data)
        }else {
            console.log("vacio el formulario");
        }
    } else {
        console.log('No continen nada el formulario')
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
            <FormCategoryU :id_Category="id_Category" :name="name" ref="formRef"/>
        </template>
    </Dialog1>
</template>