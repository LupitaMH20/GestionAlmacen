<script setup lang="ts">
import axios from 'axios'
import { ref, inject, type Ref, computed } from 'vue'
import Dialog1 from '../../../../Elements/Dialog1.vue';
import { Building2, Hammer, Notebook} from 'lucide-vue-next';

interface User {
    id_user: string;
    name: string;
    position: string;
    admin: boolean;
}
const loggedInUser = inject<Ref<User | null>>('loggedInUser')

const isDialogOpen = ref(false);
const emit = defineEmits(['createRequest'])

const props = defineProps<{
    Request: {
        id_Request: string | number;
        article?: string;
        amount?: number;
        type?: string;
    }
}>()

const canAccept = computed(() => {
    const pos = loggedInUser?.value?.position?.toLowerCase()
    return pos && pos !== 'applicant' && pos !== 'deliberystaff'
})

const handleCancel = () => {
    isDialogOpen.value = false
}

const handleSave = async () => {
    try {
        const token = sessionStorage.getItem('token')

        if (!token) {
            alert("Tu sesión ha expirado o no estás logueado. Por favor, inicia sesión nuevamente.")
            return
        }

        const payload = {
            request_id: props.Request.id_Request,
        }

        const config = {
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        }

        const response = await axios.post('http://127.0.0.1:8000/api/acceptance/', payload, config)

        alert('Solicitud Aceptada! El stock ha sido actualizado.')
        isDialogOpen.value = false
        emit('createRequest')

    } catch (error: any) {
        console.error('Error al aceptar la solicitud:', error)

        if (axios.isAxiosError(error) && error.response) {
            const errorMsg = error.response.data.error || error.response.data.detail || 'No se pudo procesar la solicitud.'
            alert(`Error: ${errorMsg}`)
        } else {
            alert('Error desconocido al procesar la solicitud.')
        }
    }
}
</script>

<template>
    <Dialog1 v-if="canAccept"
        title="Pre-Solicitud a Herramienta" 
        titleButton="Solicitud"
        :iconP="Hammer" 
        :iconT="Hammer"
        @cancel="handleCancel"
        @save="handleSave"
        v-model:open="isDialogOpen">
        
        <template #forms>
            <div class="space-y-3 p-4">
                <p>Estás a punto de aceptar la pre-solicitud:</p>
                <ul class="list-disc pl-5 my-2 p-3 bg-gray-50 rounded-md border">
                    <li><strong>ID:</strong> {{ props.Request.id_Request }}</li>
                    <li><strong>Artículo:</strong> {{ props.Request.article }}</li>
                    <li><strong>Cantidad:</strong> {{ props.Request.amount }}</li>
                </ul>
                <p>El sistema verificará que el artículo exista en la base de datos y que haya stock suficiente.</p>
                <p class="font-semibold text-center mt-4">¿Deseas continuar?</p>
            </div>
        </template>
    </Dialog1>
</template>