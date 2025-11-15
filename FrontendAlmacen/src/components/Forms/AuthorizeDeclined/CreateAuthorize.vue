<script setup lang="ts">
import Dialog1 from '../../Elements/Dialog1.vue';
import FormAuthorize from './FormAuthorizeDeclined.vue';
import { BookCheck } from 'lucide-vue-next';
import { ref, inject, Ref, computed } from 'vue';
import axios from 'axios';

const props = defineProps<{
    Request: {
        id_Request: string | number;
        user: { id_user: string };
        acceptance: {
            id_acceptance: number;
        } | null
    }
}>();

interface User {
    id_user: string;
    name: string;
    position: string;
    admin: boolean;
}

const loggedInUser = inject<Ref<User | null>>('loggedInUser')
const isDialogOpen = ref(false)
const emit = defineEmits(['createAuthorized'])
const comment = ref('');

const canAuthorize = computed(() => {
    const user = loggedInUser?.value

    if (!user) return false;

    if (user.position === 'applicant' || user.position === 'deliberystaff') {
        return false;
    }

    if (user.id_user === props.Request.user?.id_user) {
        return false
    }
    return true
})

const handleCancel = () => {
    console.log("Acción de Cancelar");
    isDialogOpen.value = false
    comment.value = ''
};

const handleSave = async () => {
    if (!comment.value.trim()) {
        alert("El comentario es obligatorio para rechazar una solicitud.");
        return;
    }

    if (!props.Request.acceptance || !props.Request.acceptance.id_acceptance) {
        alert("Error: No se encontró el ID de Aceptación (id_acceptance) en esta solicitud.");
        return;
    }

    try {
        const token = sessionStorage.getItem('token');
        if (!token) {
            alert("Error: Tu sesión ha expirado. Por favor, inicie sesión de nuevo")
            return;
        }

        const payload = {
            acceptance: props.Request.acceptance.id_acceptance,
            action: 'authorized',
            comment: comment.value || 'Autorizado'
        };
        console.log("DATOS", payload)

        const config = {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        }

        await axios.post('http://127.0.0.1:8000/api/requestActions/', payload, config)
        alert('Solicitud Autorizada con éxito');

        isDialogOpen.value = false
        emit('createAuthorized');
        comment.value = '';
    } catch (error) {
        console.error('Error al autorizar:', error);
        if (axios.isAxiosError(error) && error.response) {
            if (error.response.status === 404) {
                alert("Error 404: No se encontró la URL '/api/requestActions/'. Revisa las URLs de Django.");
            } else {
                const errorMsg = error.response.data.error || error.response.data.detail || 'No se pudo autorizar.';
                alert(`Error: ${errorMsg}`);
            }
        }
    }
};
</script>

<template>
    <Dialog1 v-if="canAuthorize" title="Autorizar" titleButton="Autorizar" :iconP="BookCheck" :iconT="BookCheck"
        @cancel="handleCancel" @save="handleSave" v-model:open=isDialogOpen>

        <template #forms>
            <FormAuthorize v-model:comment="comment" />
        </template>
    </Dialog1>
</template>