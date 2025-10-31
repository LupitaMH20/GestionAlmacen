<script setup lang="ts">
import {ref} from 'vue'
import axios from 'axios';
import Dialog1 from '../../../Elements/Dialog1.vue'
import FormCategoryC from './FormCategoryC.vue';
import {PencilLine} from 'lucide-vue-next'

const formRef = ref<any>(null)
const isDialogisOpen = ref(false)
const emit = defineEmits(['createCategory'])

const handelCancel = () => {
    console.log('Se cancelo el registro de la categoria')
    isDialogisOpen.value = false
}

const apiSaveCategory = async(data: any) => {
    try{
        console.log('datos', data)
        await axios.post('http://127.0.0.1:8000/api/category/', data)
        console.log('Se registro la categoria', data)
        isDialogisOpen.value = false
        emit('createCategory')
    } catch(error){

    }
}

const handleSave = () => {
  if (formRef.value) {
    const data = formRef.value.submitForm()
    if(data){
        apiSaveCategory(data)
    }
  } else {
    console.log("No hay datos del formulario")
  }
}
</script>

<template>
    <Dialog1
    title="Registro de Categorias"
    titleButton="Categoria"
    :icon-p="PencilLine"
    :icon-t="PencilLine"
    @cancel="handelCancel"
    @save="handleSave"
    v-model="isDialogisOpen">

    <template #forms>
        <FormCategoryC ref="formRef"/>
    </template>
    </Dialog1>
</template>