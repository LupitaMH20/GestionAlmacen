<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios';
import Dialog1 from '../../Elements/Dialog1.vue'
import FormCompanyU from './FormCompanyU.vue';
import { Building, NotebookPen } from 'lucide-vue-next'

const props = defineProps<{
    company: {
        id_Company: string,
        name: string,
        address: string
    }
}>()

const formRef = ref<any>(null)
const isDialogisOpen = ref(false)
const emit = defineEmits(['UpdateCompany'])

const handleCancel = () => {
    isDialogisOpen.value = false
    console.log('Accion cancelada')
}

const apiSaveCompany = async (data: any) => {
    try {
        await axios.patch(`http://127.0.0.1:8000/api/companies/${props.company.id_Company}/`, data);
        console.log('Error al actualizarse la empresa', data);
        isDialogisOpen.value = false
        emit('UpdateCompany')
    } catch (error) {
        console.log('Error al actualizara la empresa')
    }
}

const handleSave = () => {
    if (formRef.value) {
        const data = formRef.value.submitForm()
        if (data) {
            apiSaveCompany(data)
        }
    } else {
        console.log("No contiene nada el formulario")
    }
}

</script>

<template>
    <Dialog1 
        title="Actualizar Empresa" 
        titleButton="Actualizar"
        :iconP="NotebookPen" 
        :iconT="Building" 
        @cancel="handleCancel"
        @save="handleSave"
        v-model:open="isDialogisOpen">

        <template #forms>
            <FormCompanyU ref="formRef" :company="props.company" />
        </template>
    </Dialog1>
</template>