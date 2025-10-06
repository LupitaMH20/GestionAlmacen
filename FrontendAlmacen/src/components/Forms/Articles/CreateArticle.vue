<script setup lang="ts">
import Dialog2 from '../../Elements/Dialog2.vue';
import { Plus, ArchiveRestore, FileSpreadsheet, PackageOpen } from 'lucide-vue-next';
import FormArticleC1 from './FormArticleC1.vue';
import FormArticleC2 from './FormArticleC2.vue';

const handleCancel = () => {
    console.log("Acción de Cancelar");
};

const handleSave = () => {
    console.log("Datos guardados!");
};
</script>

<template>
    <Dialog2 
        title="Registro de producto" 
        :iconP="Plus" 
        :iconT="ArchiveRestore" 
        recordof="Producto"
        :IconOf="PackageOpen" 
        description="Descripción" 
        :IconD="FileSpreadsheet"
        @cancel="handleCancel"
        @save="handleSave"
    >
        <template #form1>
            <FormArticleC1 />
        </template>
        <template #form2>
            <FormArticleC2/>
        </template>
    </Dialog2>
</template>