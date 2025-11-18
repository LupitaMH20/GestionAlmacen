<script setup lang="ts">
import Dialog1 from '../../Elements/Dialog1.vue';
import FormSupply from '../Supply/FormSupply.vue';
import { PackageCheck } from 'lucide-vue-next';
import { ref, inject, Ref, computed, watch } from 'vue';
import axios from 'axios';

interface Users { id_user: string; name: string; }

interface LoggedInUserType {
    id_user: string;
    name: string;
    position: string;
    admin: boolean;
}

interface Collaborator { id_Collaborator: string; name: string; last_name: string; }
interface Companies { id_Company: string; name: string };
interface Article { id_mainarticle: string, name: string }

const props = defineProps<{
    Request: {
        id_Request: string | number;
        user?: Users | null;
        userName?: Users;
        collaborator?: string;
        collaboratorName?: Collaborator;
        type?: string;
        article?: string;
        articleName?: Article;
        description?: string;
        amount?: number;
        status?: string;
        order_workshop?: string;
        store?: string;
        requestingCompany?: string;
        supplierCompany?: string;
        requestingCompanyName?: Companies;
        supplierCompanyName?: Companies;
        date?: string;
        time?: string;
        acceptance?: {
            id_acceptance: number;
            user?: Users | null;
            userName?: Users;
            article?: Article | null;
            articleName?: Article;
            date?: string;
            time?: string;
            requestactions?: {
                id_RequestActions: number;
                action: 'authorized' | 'declined';
                comment: string;
                requestactions_datetime: string;
                user: Users | null;
                userName?: Users;
                date?: string;
                time?: string;
            } | null;
        } | null;
    };
}>();

const loggedInUser = inject<Ref<LoggedInUserType | null>>('loggedInUser');
const emit = defineEmits(['supplyCreated']);
const isDialogOpen = ref(false);

const collaboratorId = ref<string | null>(null);
const collaboratorsList = ref<Collaborator[]>([]);
const comment = ref('');
const selectedFile = ref<File | null>(null);

const canSupply = computed(() => {
    if (!loggedInUser?.value) return false;
    return loggedInUser.value.position === 'deliberystaff' || loggedInUser.value.admin;
})

const loadCollaborators = async () => {
    try {
        const token = sessionStorage.getItem('token');
        if (!token) {
            alert("Error de sesión al cargar colaboradores.");
            return;
        }
        const config = { headers: { 'Authorization': `Bearer ${token}` } };
        const response = await axios.get('http://127.0.0.1:8000/api/collaborator/', config)
        collaboratorsList.value = response.data
    } catch (error) {
        console.log('Sin colaboradores', error)
        // Verificar si es error 401
        if (axios.isAxiosError(error) && error.response?.status === 401) {
            alert('Sesión expirada. Por favor, inicie sesión nuevamente.');
            // Aquí podrías redirigir al login
            // window.location.href = '/login';
        }
    }
}

watch(isDialogOpen, (newVal) => { if (newVal) loadCollaborators(); });

const handleSave = async () => {
    // Validaciones
    if (!collaboratorId.value) {
        alert("Debe seleccionar el colaborador que recibe.");
        return;
    }
    
    const requestActionsId = props.Request.acceptance?.requestactions?.id_RequestActions;
    if (!requestActionsId) {
        alert("Error: No se encontró el ID de la autorización (RequestActions).");
        return;
    }
    
    const token = sessionStorage.getItem('token');
    if (!token) {
        alert("No se encontró el token de sesión. Por favor, inicie sesión nuevamente.");
        // Opcional: redirigir al login
        // window.location.href = '/login';
        return;
    }

    if (!loggedInUser || !loggedInUser.value) {
        alert("Error de sesión. Por favor, inicie sesión de nuevo.");
        return;
    }

    const requestType = props.Request.type;
    if ((requestType === 'Tool') && !selectedFile.value) {
        alert('El documento es obligatorio para surtir Herramientas o Consumibles');
        return;
    }

    const formData = new FormData();
    formData.append('requestActions', requestActionsId.toString());
    formData.append('collaborator', collaboratorId.value);
    formData.append('user', loggedInUser.value.id_user);
    formData.append('comment', comment.value);

    if (selectedFile.value) {
        formData.append('document', selectedFile.value);
    }

    console.log('Token:', token);
    console.log('Usuario:', loggedInUser.value);
    console.log('RequestActionsId:', requestActionsId);
    console.log('CollaboratorId:', collaboratorId.value);
    console.log('comment:', comment.value)
    const config = {
        headers: {
            'Authorization': `Token ${token}`,
            'Content-Type': 'multipart/form-data'
        }
    };

    try {
        const response = await axios.post('http://127.0.0.1:8000/api/supply/', formData, config);
        console.log('Respuesta exitosa:', response.data);
        alert('Solicitud surtida con éxito.');
        isDialogOpen.value = false;
        
        // Limpiar el formulario
        collaboratorId.value = null;
        comment.value = '';
        selectedFile.value = null;
        
        emit('supplyCreated');
    } catch (error) {
        console.error('Error completo:', error);
        
        if (axios.isAxiosError(error)) {
            if (error.response?.status === 401) {
                alert('Sesión expirada. Por favor, inicie sesión nuevamente.');
                // Limpiar sesión y redirigir
                sessionStorage.removeItem('token');
                // window.location.href = '/login';
            } else if (error.response) {
                console.error('Datos del error:', error.response.data);
                alert(`Error: ${error.response.data.error || error.response.data.message || 'No se pudo surtir.'}`);
            } else {
                alert('Error de conexión. Verifique su red.');
            }
        }
    }
};

const handleCancel = () => {
    isDialogOpen.value = false
    collaboratorId.value = null;
    comment.value = '';
    selectedFile.value = null;
};
</script>

<template>
    <Dialog1 v-if="canSupply" title="Surtir Solicitud" titleButton="Surtir" :iconP="PackageCheck" :iconT="PackageCheck"
        @save="handleSave" @cancel="handleCancel" v-model:open="isDialogOpen">
        <template #forms>
            <FormSupply :collaboratorsList="collaboratorsList" :requestType="props.Request.type"
                v-model:collaboratorId="collaboratorId" v-model:comment="comment" v-model:selectedFile="selectedFile" />
        </template>
    </Dialog1>
</template>