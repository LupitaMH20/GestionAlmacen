<script setup lang="ts">
import Dialog1 from '../../Elements/Dialog1.vue'
import FormCompanyU from './FormCompanyU.vue';
import {Building, NotebookPen} from 'lucide-vue-next'

const handleCancel=()=>{

}

const handleSave=()=>{

}

</script>

<template>
    <Dialog1 
        title="Actualizar Empresa"
        :iconP="NotebookPen"
        :iconT="Building"
        @cancel="handleCancel"
        @save="handleSave">
        
        <template #forms>
            <FormCompanyU />
        </template>
    </Dialog1>
</template>