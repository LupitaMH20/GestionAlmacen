<script setup lang="ts">
import { ref, onMounted, reactive, watch} from 'vue'
import Dialog2 from '../../../../Elements/Dialog2.vue';
import FormPrerequestC1 from './FormPrerequestC1.vue';
import FormPreRequestC2 from './FormPreRequestC2.vue';
import { Building2, Hammer, Notebook } from 'lucide-vue-next';
import axios from 'axios'

const isDialogOpen = ref(false)
const emit = defineEmits(['updateRequest'])
const company = ref<any[]>([])
const userRequest = ref<any[]>([])
const collaborator = ref<any[]>([])

const props = defineProps<{
    preRequest: {
        id_PreRequest: string | number;
        applicant?: string;
        collaborator?: string;
        type?: string;
        article?: string;
        description?: string;
        amount?: number;
        status?: string;
        order_workshop?: string;
        store?: string;
        requestingCompany?: string;
        supplierCompany?: string;
    }
}>()

const data = reactive({
    id_PreRequest: '',
    applicant: '',
    collaborator: '',
    type: '',
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

const loadCollaboartor = async () => {
    try{
        const response =await axios.get('http://127.0.0.1:8000/api/collaborator/')
        collaborator.value = response.data
    }catch(error){
        console.log('Sin colaboradores')
    }
}

watch(isDialogOpen, (newVal) => {
    if (newVal) {
        Object.assign(data, {
            id_PreRequest: props.preRequest.id_PreRequest || '',
            applicant: props.preRequest.applicant || '',
            collaborator: props.preRequest.collaborator || '',
            type: props.preRequest.type || '',
            article: props.preRequest.article || '',
            description: props.preRequest.description || '',
            amount: props.preRequest.amount || 0,
            status: props.preRequest.status || 'prerequest',
            order_workshop: props.preRequest.order_workshop || '',
            store: props.preRequest.store || '',
            requestingCompany: props.preRequest.requestingCompany || '',
            supplierCompany: props.preRequest.supplierCompany || '',
        });
    }
});

const handleSave = async () => {
    try {
        await axios.patch(`http://127.0.0.1:8000/api/prerequest/${data.id_PreRequest}/`, data);
        console.log('se actualizo la presolicitud')
        isDialogOpen.value = false
        emit('updateRequest')
    } catch (error) {
        console.error('No se guardó la solicitud:', error)
    }
}

onMounted(()=> {
    loadCompanies(), loadUser('applicant'), loadCollaboartor()
})
</script>

<template>
    <Dialog2 title="Registro PreSolicitud" 
    titleButton="Actualizar" 
    :iconP="Hammer" 
    :iconT="Hammer"
    recordof="Registro" 
    :IconOf="Building2" 
    description="Descripción" 
    :IconD="Notebook" 
    @save="handleSave"
    @cancel="handleCancel"
    v-model:open="isDialogOpen">

        <template #form1>
            <FormPrerequestC1 v-model:props="data" :companies="company" :users="userRequest" :collaborator="collaborator"/>
        </template>
        <template #form2>
            <FormPreRequestC2 v-model:props="data"/>
        </template>
    </Dialog2>
</template>