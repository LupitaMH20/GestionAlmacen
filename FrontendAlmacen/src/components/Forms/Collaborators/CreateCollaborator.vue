<script setup lang="ts">
import {ref, onMounted} from 'vue'
import axios from 'axios';
import Dialog1 from '../../Elements/Dialog1.vue';
import FormCollaboratorC from './FormCollaboratorC.vue';
import { Users } from 'lucide-vue-next';

const formRef = ref<any>(null)
const isDialogisOpen = ref(false)
const emit = defineEmits(['collaboratorCreate'])
const companies = ref<any[]>([])

const loadCompanies= async () => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/companies/');
        companies.value= response.data
    }catch(error){
        console.log('No se cargaron', error)
    }
}

const handleCancel=()=>{
    isDialogisOpen.value = false
    console.log('Se cancelo el registro del colaborador')
}

const apiSaveCollaborator = async (data: any) => {
    try{
        await axios.post('http://127.0.0.1:8000/api/collaborator/', data)
        console.log('Colaborador registrado',  data)
        isDialogisOpen.value=false
        emit('collaboratorCreate')
    }catch(error){
        console.log('No se pudo guardar el colaborador', error)
    }
}

const handleSave=()=>{
    if (formRef.value) {
        const data = formRef.value.submitForm()
        if (data){
            apiSaveCollaborator(data)
        }
    } else {
        console.log("No hay datos en el formulario")
    }
}

onMounted(()=>{
    loadCompanies();
});
</script>

<template>
    <Dialog1 
        title="Registro del Colaborador"
        titleButton="Colaborador" 
        :iconP="Users" 
        :iconT="Users"
        @cancel="handleCancel"
        @save="handleSave"
        v-model:open="isDialogisOpen">
        
        <template #forms>
            <FormCollaboratorC ref="formRef" :companies="companies"/>
        </template>
    </Dialog1>
</template>