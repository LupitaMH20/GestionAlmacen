<script setup lang="ts">
import {ref} from 'vue'
import axios from 'axios';
import Dialog1 from '../../Elements/Dialog1.vue';
import FormCompanyC from './FormCompanyC.vue';
import {Building2, Building} from 'lucide-vue-next'

const formRef = ref<any>(null)
const isDialogisOpen = ref(false)
const emit = defineEmits(['companyCreate'])

const handleCancel=()=>{
    isDialogisOpen.value = false
    console.log('Se cancelo el registro de la empresa')
}

const apiSaveCompany = async (data: any) => {
    try{
        await axios.post('http://127.0.0.1:8000/api/companies/', data)
        console.log('Empresa registrada',  data)
        isDialogisOpen.value=false
        emit('companyCreate')
    }catch(error){
        console.log('No se pudo guardar la empresa', error)
    }
}

const handleSave=()=>{
    if (formRef.value) {
        const data = formRef.value.submitForm()
        if (data){
            apiSaveCompany(data)
        }
    } else {
        console.log("No hay datos en el formulario")
    }
}
</script>

<template>
    <Dialog1
        title="Registro de empresa"
        :iconP="Building2"
        :iconT="Building"
        @cancel="handleCancel"
        @save="handleSave"
        v-model:open="isDialogisOpen">
        
        <template #forms>
            <FormCompanyC ref="formRef"/>
        </template>
    </Dialog1>
</template>