<script setup lang="ts">
import { ref, onMounted, reactive, inject, Ref, computed} from 'vue'
import Dialog2 from '../../../../Elements/Dialog2.vue';
import FormPreRequestC1 from './FormPreRequestC1.vue';
import FormPreRequestC2 from '../PreRequest/FormPreRequestC2.vue';
import { Building2, Notebook } from 'lucide-vue-next';
import axios from 'axios';
import { User2 } from 'lucide-vue-next';

interface User{
    id_user: string;
    name:string;
    position:string;
    admin: boolean;
}

const loggedInUser = inject<Ref<User | null>>('loggedInUser')

const CanCreate = computed(() => {
    return loggedInUser?.value?.position === 'applicant'
})

const isDialogOpen = ref(false)
const emit = defineEmits(['createPreRequest'])
const company = ref<any[]>([])
const collaborator = ref<any[]>([])

const preRequest = reactive({
    user: loggedInUser?.value?.id_user,
    collaborator: '',
    type: 'PersonalConsumption',
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
        user: loggedInUser?.value?.id_user || '',
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
            user_id: preRequest.user,
            collaborator_id: preRequest.collaborator,
        }
        await axios.post('http://127.0.0.1:8000/api/request/', payload)
        console.log('Se registró la presolicitud correctamente')
        isDialogOpen.value = false
        emit('createPreRequest')
    } catch (error) {
        console.error('No se guardó la solicitud:', error)
    }
}

onMounted(() => { loadCompanies(), loadCollaboartor() })
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
            <FormPreRequestC1 v-model:props="preRequest" :companies="company" :collaborator="collaborator"/>
        </template>
        <template #form2>
            <FormPreRequestC2 v-model:props="preRequest"/>
        </template>
    </Dialog2>
</template>