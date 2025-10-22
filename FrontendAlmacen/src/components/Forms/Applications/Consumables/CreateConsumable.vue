<script setup lang="ts">
import Dialog2 from '../../../Elements/Dialog2.vue';
import FormConsumablesC1 from './FormConsumablesC1.vue';
import FormExistence from '../../../Elements/FormExistence.vue';
import FormConsumablesC2 from './FormConsumablesC2.vue';
import {FilePlus2, Building2, Hammer, Notebook} from 'lucide-vue-next';

const handleCancel = () => {
    console.log("Acción de Cancelar");
};

const handleSave = () => {
    console.log("Datos guardados!");
};
</script>

<template>
    <Dialog2
        title="Registro de Consumibles"
        titleButton="Consumible"
        :iconP="FilePlus2"
        :iconT="FilePlus2"
        recordof="Registro"
        :IconOf="Building2"
        description="Descripción"
        :IconD="Notebook"
        @save="handleSave"
        @cancel="handleCancel">

        <template #form1>
            <FormConsumablesC1/>
        </template>
        <template #form2>
            <FormConsumablesC2/>
        </template>
    </Dialog2>
</template>