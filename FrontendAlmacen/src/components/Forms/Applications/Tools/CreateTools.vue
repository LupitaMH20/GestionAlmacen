<script setup lang="ts">
import Dialog3 from '../../../Elements/Dialog3.vue';
import FormApplicationC from '../../../Elements/FormApplicationC.vue';
import FormExistence from '../../../Elements/FormExistence.vue';
import FormToolsC from './FormToolsC.vue';
import { Building2, Hammer, Notebook} from 'lucide-vue-next';

const handleCancel = () => {
    console.log("Acción de Cancelar");
};

const handleSave = () => {
    console.log("Datos guardados!");
};
</script>

<template>
    <Dialog3 
        title="Solicitud Herramienta" 
        :iconP="Hammer" 
        :iconT="Hammer"
        recordof="Registro"
        :iconOf="Building2"
        existence = "Producto"
        :iconE="Hammer"
        description="Descripción"
        :iconD="Notebook"
        @cancel="handleCancel"
        @save="handleSave">
        
        <template #form1>
            <FormApplicationC />
        </template>
        <template #form2>
            <FormExistence />
        </template>
        <template #form3>
            <FormToolsC />
        </template>
    </Dialog3>
</template>