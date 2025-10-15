<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios';
import Dialog1 from '../../Elements/Dialog1.vue';
import FormCollaboratorU from './FormCollaboratorU.vue';
import { UserPen, NotebookPen } from 'lucide-vue-next'

const props = defineProps<{
    collaborator: {
        id_Collaborator: string,
        name: string,
        last_name: string,
        position: string,
        company: string
    },
    company: Array<{
        id_Company: string,
        name: string
    }>
}>()

const formRef = ref<any>(null)
const isDialogisOpen = ref(false)
const emit = defineEmits(['updateCollaborator'])

const handleCancel = () => {
    console.log("Acción de Cancelar");
    isDialogisOpen.value = false
}

const apiUpdateCollaborator = async (data: any) => {
    try {
        console.log('Enviando PATCH a la API con datos:', data);
        await axios.patch(`http://127.0.0.1:8000/api/collaborator/${props.collaborator.id_Collaborator}/`, data)
        console.log('colaborador actualizado',data);
        isDialogisOpen.value = false
        emit('updateCollaborator')
    } catch (error) {
        console.log('No se pudo actualizar el colaborador', error)
    }
}

const handleSave = () => {
    if (formRef.value) {
        const data = formRef.value.submitForm()
        if (data) {
            apiUpdateCollaborator(data)
        }else {
            console.log("Advertencia: submitForm() devolvió datos nulos/vacíos.");
        }
    } else {
        console.log('No continen nada el formulario')
    }
}
</script>

<template>
    <Dialog1 title="Actualizar colaborador" :iconP="NotebookPen" :iconT="UserPen" @cancel="handleCancel"
        @save="handleSave" v-model:open="isDialogisOpen">

        <template #forms>
            <FormCollaboratorU ref="formRef" :collaborator="props.collaborator" :company="props.company" />
        </template>
    </Dialog1>
</template>