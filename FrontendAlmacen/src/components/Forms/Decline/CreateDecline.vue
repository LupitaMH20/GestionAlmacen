<script setup lang="ts">
import Dialog1 from '../../Elements/Dialog1.vue';
import FormDecline from './FormDecline.vue';
import { BookX } from 'lucide-vue-next';

const handleCancel = () => {
    console.log("Acción de Cancelar");
};

const handleSave = () => {
    console.log("Datos guardados!");
};
</script>

<template>
    <Dialog1 
        title="Rechaza" 
        titleButton="Rechazar"
        :iconP="BookX" 
        :iconT="BookX"
        @cancel="handleCancel"
        @save="handleSave">
        
        <template #forms>
            <FormDecline />
        </template>
    </Dialog1>
</template>