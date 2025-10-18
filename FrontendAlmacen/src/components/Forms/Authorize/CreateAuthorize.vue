<script setup lang="ts">
import Dialog1 from '../../Elements/Dialog1.vue';
import FormAuthorize from './FormAuthorize.vue';
import { BookCheck } from 'lucide-vue-next';

const handleCancel = () => {
    console.log("Acción de Cancelar");
};

const handleSave = () => {
    console.log("Datos guardados!");
};
</script>

<template>
    <Dialog1 
        title="Autorizar" 
        titleButton="Autorizar"
        :iconP="BookCheck" 
        :iconT="BookCheck"
        @cancel="handleCancel"
        @save="handleSave">
        
        <template #forms>
            <FormAuthorize />
        </template>
    </Dialog1>
</template>