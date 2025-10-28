<script setup lang="ts">
import Dialog2 from '../../../../Elements/Dialog2.vue';
import FormConsumableU1 from './FormConsumableU1.vue';
import FormConsumableU2 from './FormConsumableU2.vue';
import {FilePlus2, Building2, Notebook} from 'lucide-vue-next';

const handleCancel = () => {
    console.log("Acción de Cancelar");
};

const handleSave = () => {
    console.log("Datos guardados!");
};
</script>

<template>

        <Dialog2 
        title="Actualizar la solicitud Consumibles" 
        titleButton="Actualizar"
        :iconP="FilePlus2" 
        :iconT="FilePlus2" 
        recordof="Producto"
        :IconOf="Building2" 
        description="Descripción" 
        :IconD="Notebook"
        @cancel="handleCancel"
        @save="handleSave"
    >
        <template #form1>
            <FormConsumableU1 />
        </template>
        <template #form2>
            <FormConsumableU2 />
        </template>
    </Dialog2>
</template>