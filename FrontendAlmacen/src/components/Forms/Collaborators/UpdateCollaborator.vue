<script setup lang="ts">
import Dialog1 from '../../Elements/Dialog1.vue';
import FormCollaboratorU from './FormCollaboratorU.vue';
import { UserPen, NotebookPen } from 'lucide-vue-next'

const handleCancel = () => {
    console.log("Acción de Cancelar");
}

const handleSave = () => {
    console.log("Datos guardados!");
}
</script>

<template>
    <Dialog1
        title="Actualizar colaborador"
        :iconP="NotebookPen"
        :iconT="UserPen"
        @cancel="handleCancel"
        @save="handleSave">
        
        <template #forms>
            <FormCollaboratorU />
        </template>
    </Dialog1>
</template>