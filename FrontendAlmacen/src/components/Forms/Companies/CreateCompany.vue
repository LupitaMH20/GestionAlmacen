<script setup lang="ts">
import Dialog1 from '../../Elements/Dialog1.vue';
import FormCompanyC from './FormCompanyC.vue';
import {Building2, Building} from 'lucide-vue-next'

const handleCancel=()=>{

}

const handleSave=()=>{

}
</script>

<template>
    <Dialog1
        title="Registro de empresa"
        :iconP="Building2"
        :iconT="Building"
        @cancel="handleCancel"
        @save="handleSave">
        
        <template #forms>
            <FormCompanyC />
        </template>
    </Dialog1>
</template>