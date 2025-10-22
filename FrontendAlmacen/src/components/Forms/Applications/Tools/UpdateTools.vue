<script setup lang="ts">
import {ref,onMounted,reactive} from 'vue'
import axios from 'axios';
import Dialog2 from '../../../Elements/Dialog2.vue';
import FormApplicationU from '../../../Elements/FormApplicationU.vue';
import FormToolsU from './FormToolsU.vue';
import { Building2, Hammer, Notebook} from 'lucide-vue-next';

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

const loadUser = async (positions: string[]) => {
    try {
        const params = new URLSearchParams()
        positions.forEach(pos => params.append('position', pos))

        const response = await axios.get('http://127.0.0.1:8000/api/users/', { params })
        userRequest.value = response.data
        console.log('Usuarios filtrados por posiciones:', positions)
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
    loadUser(['managerJom','managerNs','managerPrintek','managerHefesto','managerBlackwWorkshop']);
    loadCollaboartor()
})
</script>

<template>
    <Dialog2 
        title="Actualizar la solicitud herramientas" 
        titleButton="Actualizar"
        :iconP="Hammer" 
        :iconT="Hammer" 
        recordof="Producto"
        :IconOf="Building2" 
        description="Descripción" 
        :IconD="Notebook"
        @cancel="handleCancel"
        @save="handleSave"
    >
        <template #form1>
            <FormApplicationU v-model:props="request" :companies="company" :users="userRequest" :collaborator="collaborator" />
        </template>
        <template #form2>
            <FormToolsU />
        </template>
    </Dialog2>
</template>