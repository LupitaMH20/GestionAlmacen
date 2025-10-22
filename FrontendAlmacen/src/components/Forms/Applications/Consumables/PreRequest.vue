<script setup lang="ts">
import { ref, onMounted, reactive } from 'vue'
import Dialog2 from '../../../Elements/Dialog2.vue';
import FormPrerequestC1 from './FormPrerequestC1.vue';
import FormPreRequestC2 from './FormPreRequestC2.vue';
import { FilePlus2, Building2, Hammer, Notebook } from 'lucide-vue-next';
import axios from 'axios';

const isDialogOpen = ref(false)
const emit = defineEmits(['createPreRequest'])
const company = ref<any[]>([])
const userRequest = ref<any[]>([])

const preRequest = reactive({
    applicant: '',
    collaborator: '',
    type: 'Consumible',
    article: '',
    description: '',
    amount: 0,
    status: 'prerequest',
    order_workshop: '',
    store: '',
    requestingCompany: '',
    supplierCompany: '',
});

const handleCancel = () => {
    isDialogOpen.value = false
    Object.assign(preRequest, {
        applicant: '',
        collaborator: '',
        type: '',
        article: '',
        description: '',
        amount: 0,
        status: '',
        order_workshop: '',
        store: '',
        requestingCompany: '',
        supplierCompany: '',
})
}

const loadCompanies = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/companies/')
        company.value = response.data
    } catch (error) {
        console.log('Empresas mostradas')
    }
}

const loadUser = async (position: string) => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/users/', {
            params: { position: position }
        })
        userRequest.value = response.data
        console.log('Usuarios filtrados por posición:', position)
    } catch (error) {
        console.error('Error al mostrar usuarios', error)
    }
}

const handleSave = async () => {
    try {
        console.log('data', preRequest)
        await axios.post('http://127.0.0.1:8000/api/prerequest/', preRequest)
        console.log('se registro la presolicitud')
        isDialogOpen.value = false
        emit('createPreRequest')
    } catch (error) {
        console.log('No se guardo la solicitud', error)
    }
}

onMounted(() => {
    loadCompanies(), loadUser('applicant')
})
</script>

<template>
    <Dialog2 
        title="Registro PreSolicitud" 
        titleButton="Consumible" 
        :iconP="FilePlus2" 
        :iconT="FilePlus2"
        recordof="Registro" 
        :IconOf="Building2" 
        description="Descripción" 
        :IconD="Notebook" 
        @save="handleSave"
        @cancel="handleCancel" 
        v-model:open="isDialogOpen">

        <template #form1>
            <FormPrerequestC1 v-model:props="preRequest" :companies="company" :users="userRequest" />
        </template>
        <template #form2>
            <FormPreRequestC2 v-model:props="preRequest" />
        </template>
    </Dialog2>
</template>