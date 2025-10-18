<script setup lang="ts">
import Dialog2 from '../../../Elements/Dialog2.vue';
import FormApplicationU from '../../../Elements/FormAppicationU.vue';
import FormToolsU from './FormToolsU.vue';
import { Building2, Hammer, Notebook} from 'lucide-vue-next';

const handleCancel = () => {
    console.log("Acción de Cancelar");
};

const handleSave = () => {
    console.log("Datos guardados!");
};
</script>

<template>
    <Dialog2 
        title="Actualizar la solicitud herramientas" 
        titleButton="Actualizar"
        :iconP="Hammer" 
        :iconT="Hammer" 
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
            <FormToolsU />
        </template>
    </Dialog2>
</template>