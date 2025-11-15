<script setup lang="ts">
import Dialog1 from '../../Elements/Dialog1.vue';
import FormDecline from './FormAuthorizeDeclined.vue';
import { BookCheck } from 'lucide-vue-next';
import { ref, inject, Ref, computed } from 'vue';
import axios from 'axios';

const props = defineProps<{
    Request:{
        id_Request: string | number;
        acceptance: number;
        user: {id_user:string};
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
const emit = defineEmits(['createDeclined'])
const comment = ref('');

const canDeclined = computed( () => {
    const user = loggedInUser?.value
    
    if(!user) return false;
    
    if (user.position === 'applicant' || user.position === 'deliberystaff') {
        return false;
    }

    if (user.id_user === props.Request.user?.id_user){
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

    try {
        const token = sessionStorage.getItem('token');
        if(!token){
            alert ("Error: Tu sesión ha expirado. Por favor, inicie sesión de nuevo")
            return;
        }

        const payload = {
            acceptance:props.Request.acceptance,
            action: 'declined',
            comment: comment.value
        };

        const config = {
            headers: {
                'Authorization':`Bearer ${token}`
            }
        }

        await axios.post('http://127.0.0.1:8000/api/requestActions/', payload, config)
        alert('Solicitud Rechazada');
        isDialogOpen.value = false
        emit('createDeclined');
        comment.value = '';
    } catch (error){
        console.error('Error al autorizar:', error);
        if (axios.isAxiosError(error) && error.response) {
            const errorMsg = error.response.data.error || error.response.data.detail || 'No se pudo autorizar.';
            alert(`Error: ${errorMsg}`);
        }
    }
};
</script>

<template>
    <Dialog1 
        v-if="canDeclined"
        title="Rechazar" 
        titleButton="Rechazar"
        :iconP="BookCheck" 
        :iconT="BookCheck"
        @cancel="handleCancel"
        @save="handleSave"
        v-model:open = isDialogOpen>
        
        <template #forms>
            <FormDecline v-model:comment="comment"/>
        </template>
    </Dialog1>
</template>