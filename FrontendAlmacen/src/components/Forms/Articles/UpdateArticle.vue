<script setup lang="ts">
import Dialog2 from '../../Elements/Dialog2.vue';
import { NotebookPen, FileSpreadsheet, PackageOpen } from 'lucide-vue-next';
import FormArticleU1 from './FormArticleU1.vue';
import FormArticleU2 from './FormArticleU2.vue';

const handleCancel = () => {
    console.log("Acción de Cancelar");
};

const handleSave = () => {
    console.log("Datos guardados!");
};
</script>

<template>
    <Dialog2 
        title="Actualizar producto" 
        :iconP="NotebookPen" 
        :iconT="NotebookPen" 
        recordof="Producto"
        :IconOf="PackageOpen" 
        description="Descripción" 
        :IconD="FileSpreadsheet"
        @cancel="handleCancel"
        @save="handleSave"
    >
        <template #form1>
            <FormArticleU1 />
        </template>
        <template #form2>
            <FormArticleU2/>
        </template>
    </Dialog2>
</template>