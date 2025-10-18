<script setup lang="ts">
import Dialog3 from '../../../Elements/Dialog3.vue';
import FormConsumablesC1 from './FormConsumablesC1.vue';
import FormExistence from '../../../Elements/FormExistence.vue';
import FormConsumablesC3 from './FormConsumablesC3.vue';
import {FilePlus2, Building2, Hammer, Notebook} from 'lucide-vue-next';

const handleCancel = () => {
    console.log("Acción de Cancelar");
};

const handleSave = () => {
    console.log("Datos guardados!");
};
</script>

<template>
    <Dialog3 
        title="Solicitud Consumibles"
        titleButton="Consumible"
        :iconP="FilePlus2" 
        :iconT="FilePlus2"
        recordof="Registro"
        :iconOf="Building2"
        existence = "Producto"
        :iconE="Hammer"
        description="Descripción"
        :iconD="Notebook"
        @cancel="handleCancel"
        @save="handleSave">
        
        <template #form1>
            <FormConsumablesC1 />
        </template>
        <template #form2>
            <FormExistence />
        </template>
        <template #form3>
            <FormConsumablesC3 />
        </template>
    </Dialog3>
</template>