<script setup lang="ts">
import { ref, onMounted, reactive, watch, inject, Ref } from 'vue'
import Dialog2 from '../../../../Elements/Dialog2.vue';
import FormPreRequestU1 from './FormPreRequestU1.vue';
import FormPreRequestU2 from './FormPreRequestU2.vue';
import { FilePlus2, Building2, Hammer, Notebook } from 'lucide-vue-next';
import axios from 'axios';

interface User {
    id_user: string;
    name: string;
    position: string;
    admin: boolean;
}

const loggedInUser = inject<Ref<User | null>>('loggedInUser')

const isDialogOpen = ref(false)
const emit = defineEmits(['updatePreRequest'])
const company = ref<any[]>([])

const props = defineProps<{
    Request: {
        id_Request: string | number;
        user?: string;
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
}>();

const data = reactive({
    id_Request: '',
    user: loggedInUser?.value?.id_user,
    collaborator: '',
    type: 'Consumable',
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

watch(isDialogOpen, (newValue) => {
    if (newValue) {
        Object.assign(data, {
            id_Request: props.Request.id_Request,
            user: props.Request.user || '',
            collaborator: props.Request.collaborator || '',
            type: props.Request.type || '',
            article: props.Request.article || '',
            description: props.Request.description || '',
            amount: props.Request.amount || 0,
            status: props.Request.status || 'prerequest',
            order_workshop: props.Request.order_workshop || '',
            store: props.Request.store || '',
            requestingCompany: props.Request.requestingCompany || '',
            supplierCompany: props.Request.supplierCompany || '',
        });
        console.log("Formulario cargado con datos:", data);
    }
});

const handleSave = async () => {
    try {
        const payload = {
            user_id: data.user,
            collaborator_id: data.collaborator || null,
            requestingCompany_id: data.requestingCompany,
            supplierCompany_id: data.supplierCompany,
            type: data.type,
            article: data.article,
            description: data.description,
            amount: data.amount,
            status: data.status,
            order_workshop: data.order_workshop,
            store: data.store
        };
        await axios.patch(`http://127.0.0.1:8000/api/request/${data.id_Request}/`, payload);
        console.log('se actualizo la presolicitud')
        isDialogOpen.value = false
        emit('updatePreRequest')
    } catch (error) {
        console.log('No se guardo la solicitud', error)
    }
}

onMounted(() => { loadCompanies() })
</script>

<template>
    <Dialog2 title="Actualizar PreSolicitud" titleButton="Actualizar" :iconP="FilePlus2" :iconT="FilePlus2"
        recordof="Registro" :IconOf="Building2" description="Descripción" :IconD="Notebook" @save="handleSave"
        @cancel="handleCancel" v-model:open="isDialogOpen">

        <template #form1>
            <FormPreRequestU1 v-model:props="data" :companies="company" />
        </template>
        <template #form2>
            <FormPreRequestU2 v-model:props="data" />
        </template>
    </Dialog2>
</template>