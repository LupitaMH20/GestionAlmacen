<script setup lang="ts">
import { ref, inject, type Ref } from 'vue';
import axios from 'axios';
import Button from '../../ui/button/Button.vue';
import { RefreshCw } from 'lucide-vue-next';

const props = defineProps<{
    Request: {
        id_Request: number | string;
        status?: string;
    };
}>();

const emit = defineEmits(['regenerate']);

const handleRegenerate = async () => {
    if (!confirm('¿Estás seguro de que deseas regenerar esta solicitud? Volverá a estado de Pre-Solicitud.')) {
        return;
    }

    try {
        const token = sessionStorage.getItem('token');
        if (!token) {
            alert("Error: Tu sesión ha expirado. Por favor, inicie sesión de nuevo")
            return;
        }

        const config = {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        }

        await axios.post(`http://127.0.0.1:8000/api/request/${props.Request.id_Request}/regenerate_request/`, {}, config);
        
        alert('Solicitud regenerada exitosamente.');
        emit('regenerate');
        
    } catch (error) {
        console.error('Error al regenerar:', error);
        alert('Error al regenerar la solicitud.');
    }
};
</script>

<template>
    <Button 
        variant="outline" 
        class="flex items-center gap-2 text-blue-600 border-blue-200 hover:bg-blue-50"
        @click="handleRegenerate">
        <RefreshCw class="w-4 h-4" />
        Regenerar Solicitud
    </Button>
</template>
