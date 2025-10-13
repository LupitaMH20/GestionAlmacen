<script setup lang="ts">
import Dialog2 from '../../../Elements/Dialog2.vue';
import FormApplicationU from '../../../Elements/FormAppicationU.vue';
import FormPersonalConsumptionU from './FormPersonalConsumptionU.vue';
import {Users, Building2, Hammer, Notebook} from 'lucide-vue-next';

const handleCancel = () => {
    console.log("Acción de Cancelar");
};

const handleSave = () => {
    console.log("Datos guardados!");
};
</script>

<template>
    <Dialog2 
        title="Actualizar la solicitud de Consumo Personal"
        :iconP="Users" 
        :iconT="Users" 
        recordof="Producto"
        :IconOf="Building2" 
        description="Descripción" 
        :IconD="Notebook"
        @cancel="handleCancel"
        @save="handleSave"
    >
        <template #form1>
            <FormApplicationU />
        </template>
        <template #form2>
            <FormPersonalConsumptionU />
        </template>
    </Dialog2>
</template>