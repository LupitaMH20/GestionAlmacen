<script setup lang="ts">
import Dialog1 from '../../Elements/Dialog1.vue';
import FormCollaboratorC from './FormCollaboratorC.vue';
import { UserPlus } from 'lucide-vue-next';

const handleCancel = () => {
    console.log("Acción de Cancelar");
};

const handleSave = () => {
    console.log("Datos guardados!");
};
</script>

<template>
    <Dialog1 
        title="Registro del Colaborador" 
        :iconP="UserPlus" 
        :iconT="UserPlus"
        @cancel="handleCancel"
        @save="handleSave">
        
        <template #forms>
            <FormCollaboratorC />
        </template>
    </Dialog1>
</template>