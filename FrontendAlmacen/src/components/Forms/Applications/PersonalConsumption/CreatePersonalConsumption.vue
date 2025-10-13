<script setup lang="ts">
import Dialog3 from '../../../Elements/Dialog3.vue';
import FormApplicationC from '../../../Elements/FormApplicationC.vue';
import FormExistence from '../../../Elements/FormExistence.vue';
import FormPersonalConsumptionC from './FormPersonalConsumptionC.vue';
import { Building2, Hammer, Notebook, Users2} from 'lucide-vue-next';

const handleCancel = () => {
    console.log("Acción de Cancelar");
};

const handleSave = () => {
    console.log("Datos guardados!");
};
</script>

<template>
    <Dialog3 
        title="Solicitud de Consumo Personal" 
        :iconP="Users2" 
        :iconT="Users2"
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
            <FormPersonalConsumptionC />
        </template>
    </Dialog3>
</template>