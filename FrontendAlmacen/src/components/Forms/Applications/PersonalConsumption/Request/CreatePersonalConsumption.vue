<script setup lang="ts">
import { ref, onMounted, reactive } from 'vue'
import Dialog2 from '../../../../Elements/Dialog2.vue';
import FormApplicationC from '../../../../Elements/FormApplicationC.vue';
import FormPersonalConsumptionC from '../Request/FormPersonalConsumptionC.vue';
import { Building2, Notebook } from 'lucide-vue-next';
import axios from 'axios';
import { User2 } from 'lucide-vue-next';

const isDialogOpen = ref(false)
const emit = defineEmits(['createrequest'])
const company = ref<any[]>([])
const userRequest = ref<any[]>([])
const collaborator = ref<any[]>([])

const request = reactive({
    request:'',
    applicant: '',
    collaborator: '',
    type: 'ConsumoPersonal',
    article: '',
    description: '',
    amount: 0,
    status: 'request',
    order_workshop: '',
    store: '',
    requestingCompany: '',
    supplierCompany: '',
    position:''
});

const handleCancel = () => {
    isDialogOpen.value = false
    Object.assign(request, {
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

const loadUser = async () => {
    try {

        const response = await axios.get('http://127.0.0.1:8000/api/users/')
        userRequest.value = response.data
        console.log('Usuarios filtrados por posiciones:')
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
        console.log('datos', request)
        await axios.post('http://127.0.0.1:8000/api/request/', request)
        console.log('se registro la presolicitud')
        isDialogOpen.value = false
        emit('createrequest')
    } catch (error) {
        console.log('Seguardo lasolicitud')
    }
}

onMounted(() => {
    loadCompanies();
    loadUser();
    loadCollaboartor()
})
</script>

<template>
    <Dialog2 
    title="Registro Solicitud" 
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
            <FormApplicationC v-model:props="request" :companies="company" :users="userRequest" :collaborator="collaborator" />
        </template>
        <template #form2>
            <FormPersonalConsumptionC v-model:props="request"/>
        </template>
    </Dialog2>
</template>