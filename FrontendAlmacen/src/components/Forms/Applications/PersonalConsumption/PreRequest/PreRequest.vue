<script setup lang="ts">
import { ref, onMounted, reactive } from 'vue'
import Dialog2 from '../../../../Elements/Dialog2.vue';
import FormPrerequestC1 from './FormPreRequestC1.vue';
import FormPreRequestC2 from '../PreRequest/FormPreRequestC2.vue';
import { Building2, Notebook } from 'lucide-vue-next';
import axios from 'axios';
import { User2 } from 'lucide-vue-next';

const isDialogOpen = ref(false)
const emit = defineEmits(['createPreRequest'])
const company = ref<any[]>([])
const userRequest = ref<any[]>([])
const collaborator = ref<any[]>([])

const preRequest = reactive({
    applicant: '',
    collaborator: '',
    type: 'ConsumoPersonal',
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
        console.log('Sin Empresas mostradas')
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

const loadCollaboartor = async () => {
    try{
        const response =await axios.get('http://127.0.0.1:8000/api/collaborator/')
        collaborator.value = response.data
    }catch(error){
        console.log('Sin colaboradores')
    }
}

const handleSave = async () => {
    try {
        console.log('Datos a guardar:', preRequest)
        const payload = {
            ...preRequest,
            requestingCompany_id: preRequest.requestingCompany,
            supplierCompany_id: preRequest.supplierCompany,
            applicant_id: preRequest.applicant,
            collaborator_id: preRequest.collaborator,
        }
        await axios.post('http://127.0.0.1:8000/api/prerequest/', payload)
        console.log('Se registró la presolicitud correctamente')
        isDialogOpen.value = false
        emit('createPreRequest')
    } catch (error) {
        console.error('No se guardó la solicitud:', error)
    }
}

onMounted(() => {
    loadCompanies(), loadUser('applicant'), loadCollaboartor()
})
</script>

<template>
    <Dialog2 
    title="Registro PreSolicitud" 
    titleButton="Consumo Personal" 
    :iconP="User2" 
    :iconT="User2"
        recordof="Registro" 
        :IconOf="Building2" 
        description="Descripción" 
        :IconD="Notebook" 
        @save="handleSave"
        @cancel="handleCancel"
        v-model:open="isDialogOpen">

        <template #form1>
            <FormPrerequestC1 v-model:props="preRequest" :companies="company" :users="userRequest" :collaborator="collaborator"/>
        </template>
        <template #form2>
            <FormPreRequestC2 v-model:props="preRequest"/>
        </template>
    </Dialog2>
</template>