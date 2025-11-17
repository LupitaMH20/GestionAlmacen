<script setup lang="ts">
import { ref, onMounted, reactive, inject, computed } from 'vue'
import type { Ref } from 'vue'
import Dialog2 from '../../../../Elements/Dialog2.vue';
import FormPrerequestC1 from '../PreRequest/FormPrerequestC1.vue';
import FormPreRequestC2 from '../PreRequest/FormPreRequestC2.vue';
import { FilePlus2, Building2, Hammer, Notebook } from 'lucide-vue-next';
import axios from 'axios';

interface User {
    id_user: string;
    name: string;
    position: string;
    admin: boolean;
}

const loggedInUser = inject<Ref<User | null>>('loggedInUser')

const canCreate = computed(() => {
    return loggedInUser?.value?.position === 'applicant'
})

const isDialogOpen = ref(false)
const emit = defineEmits(['createPreRequest'])
const company = ref<any[]>([])

const preRequest = reactive({
    user: loggedInUser?.value?.id_user,
    collaborator: '',
    supplierCompany: '',
    requestingCompany: '',
    article: '',
    type: 'Consumable',
    description: '',
    amount: '',
    status: 'prerequest',
    order_workshop: '',
    store: '',
});

const handleCancel = () => {
    isDialogOpen.value = false
    Object.assign(preRequest, {
        user: loggedInUser?.value?.id_user || '',
        collaborator: '',
        supplierCompany: '',
        requestingCompany: '',
        article: '',
        type: '',
        description: '',
        amount: 0,
        status: '',
        order_workshop: '',
        store: '',
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

const handleSave = async () => {
    try {
        console.log('Datos a guardar:', preRequest)
        const payload = {
            ...preRequest,
            requestingCompany_id: preRequest.requestingCompany,
            supplierCompany_id: preRequest.supplierCompany,
            user_id: preRequest.user,
            collaborator_id: preRequest.collaborator || null,
        }
        await axios.post('http://127.0.0.1:8000/api/request/', payload)
        console.log('Se registró la presolicitud correctamente')
        isDialogOpen.value = false
        emit('createPreRequest')
    } catch (error) {
        console.error('No se guardó la solicitud:', error)
    }
}

onMounted(() => { loadCompanies() })
</script>

<template>
    <template v-if="canCreate">
        <Dialog2 title="Registro PreSolicitud" titleButton="Consumible" :iconP="FilePlus2" :iconT="FilePlus2"
            recordof="Registro" :IconOf="Building2" description="Descripción" :IconD="Notebook" @save="handleSave"
            @cancel="handleCancel" v-model:open="isDialogOpen">

            <template #form1>
                <FormPrerequestC1 v-model:props="preRequest" :companies="company" />
            </template>
            <template #form2>
                <FormPreRequestC2 v-model:props="preRequest" />
            </template>
        </Dialog2>
    </template>
</template>