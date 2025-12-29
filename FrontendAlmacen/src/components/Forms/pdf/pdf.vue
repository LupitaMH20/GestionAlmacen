<script setup lang="ts">
import { ref, inject, Ref } from 'vue'
import Dialog1 from '../../Elements/Dialog1.vue'
import { FilePlus2, Building2, Notebook } from 'lucide-vue-next'
import { PdfService } from './pdfService'

interface User {
    id_user: string
    name: string
    position: string
    admin: boolean
}

const loggedInUser = inject<Ref<User | null>>('loggedInUser')

const isDialogOpen = ref(false)

const props = defineProps<{
    Request: {
        id_Request: string | number
    }
}>()

const handleCancel = () => {
    isDialogOpen.value = false
}

const handleDownloadPdf = async () => {
    try {
        await PdfService.downloadEquipmentCheckout(props.Request.id_Request)
    } catch (error) {
        console.error('Error al descargar PDF', error)
    }
}
</script>

<template>
    <Dialog1 title="Generar PDF" titleButton="Generar PDF" :iconP="FilePlus2" :iconT="FilePlus2" @cancel="handleCancel"
        v-model:open="isDialogOpen" @save="handleDownloadPdf">
        <template #actions-extra>
            <button type="button" class="px-3 py-1 text-sm bg-orange-50 text-white rounded" @click="handleDownloadPdf">
                Generar PDF de resguardo
            </button>
        </template>
    </Dialog1>
</template>
