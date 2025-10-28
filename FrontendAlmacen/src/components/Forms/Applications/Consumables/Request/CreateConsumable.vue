<script setup lang="ts">
import { ref, onMounted, reactive, watch } from 'vue'
import axios from 'axios';
import Dialog2 from '../../../../Elements/Dialog2.vue';
import FormConsumablesC1 from '../Request/FormConsumablesC1.vue';
import FormExistence from '../../../../Elements/FormExistence.vue';
import FormConsumablesC2 from '../Request/FormConsumablesC2.vue';
import { FilePlus2, Building2, Hammer, Notebook } from 'lucide-vue-next';

const isDialogOpen = ref(false);
const emit = defineEmits(['updatePreRequest'])
const company = ref<any[]>([]);
const users = ref<any[]>([]);

const props = defineProps<{
    preRequest: {
        id_PreRequest: string | number;
        applicant?: string;
        collaborator?: string;
        type?: 'Consumible';
        article?: string;
        description?: string;
        amount?: number;
        order_workshop?: string;
        store?: string;
        requestingCompany?: string;
        supplierCompany?: string;
        request?: {
            position?: string;
        }
    }
}>()

const request = reactive({
    position: '',
    applicant: '',
    collaborator: '',
    type: 'Consumible',
    article: '',
    description: '',
    amount: 0,
    order_workshop: '',
    store: '',
    requestingCompany: '',
    supplierCompany: '',
})

watch(isDialogOpen, (newValue) => {
  if (newValue) {
    Object.assign(request, {
        position: '',
        applicant: props.preRequest.applicant || '',
        collaborator: props.preRequest.collaborator || '',
        type: props.preRequest.type || 'Consumible',
        article: props.preRequest.article || '',
        description: props.preRequest.description || '',
        amount: props.preRequest.amount || 0,
        order_workshop: props.preRequest.order_workshop || '',
        store: props.preRequest.store || '',
        requestingCompany: props.preRequest.requestingCompany || '',
        supplierCompany: props.preRequest.supplierCompany || '',
    });
    console.log("Formulario de Solicitud cargado con datos:", request);
  }
});

const loadCompanies = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/companies/')
        company.value = response.data
    } catch (error) {
        console.log('Empresas mostradas')
    }
}

const loadUser = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/users/')
        users.value = response.data
    } catch (error) {
        console.error('Error al mostrar usuarios', error)
    }
}

const handleCancel = () => {
    isDialogOpen.value = false;
};

const handleSave = async() => {
    try {
        const data = {
            prerequest: props.preRequest.id_PreRequest,
            position: request.position,
            applicant: props.preRequest.applicant,
            collaborator: props.preRequest.collaborator || null,
            type: props.preRequest.type,
            article: props.preRequest.article || null,
            description: props.preRequest.description,
            amount: props.preRequest.amount,
            order_workshop: props.preRequest.order_workshop,
            store: props.preRequest.store,
            requestingCompany: props.preRequest.requestingCompany || null,
            supplierCompany: props.preRequest.supplierCompany || null,
        };

        await axios.post('http://127.0.0.1:8000/api/request/', data);
        isDialogOpen.value = false;
        emit('updatePreRequest');
    } catch (error) {
        console.error('Error al crear la solicitud:', error);
        if (axios.isAxiosError(error) && error.response) {
            console.error("Detalles del error:", error.response.data);
        }
    }
}

onMounted(() => {
    loadCompanies(), loadUser()
})
</script>

<template>
    <Dialog2 
        title="Registro de Consumibles" 
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
            <FormConsumablesC1 v-model:props="request" :companies="company" :users="users"/>
        </template>
        <template #form2>
            <FormConsumablesC2 v-model:props="request"/>
        </template>
    </Dialog2>
</template>