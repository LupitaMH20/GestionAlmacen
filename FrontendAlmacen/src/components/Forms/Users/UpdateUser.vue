<script setup lang="ts">
import {ref} from 'vue'
import axios from 'axios';
import Dialog1 from '../../Elements/Dialog1.vue';
import FormUserU from './FormUserU.vue';
import { UserPen, NotebookPen } from 'lucide-vue-next'

const props = defineProps<{
    user: {
        id_user: string,
        name: string,
        last_name: string,
        position: string,
        admin: boolean
    }
}>()
const formRef = ref<any>(null)
const isDialogOpen = ref(false)
const emit = defineEmits(['updateUser'])

const handleCancel = () => {
    isDialogOpen.value = false
    console.log("Acción de Cancelar");
}

const apiUpdateUser = async (data: any) => {
    try{
        await axios.patch(`http://127.0.0.1:8000/api/users/${props.user.id_user}/`, data)
        console.log("Datos actualizados!", data);
        isDialogOpen.value = false 
        emit('updateUser')
    }catch(error){
        console.log("No se puede actualizar el usuario ", error);
    }
    
}

const handleSave = () => {
    if(formRef.value){
        const data = formRef.value.submitForm()
        if(data){
            apiUpdateUser(data)
        }
    }else{
        console.log("No contiene nada el formulario")
    }
}

</script>

<template>
    <Dialog1
        title="Actualizar usuario"
        :iconP="NotebookPen"
        :iconT="UserPen"
        @cancel="handleCancel"
        @save="handleSave"
        v-model:open="isDialogOpen">
        
        <template #forms>
            <FormUserU ref="formRef" :user="props.user"/>
        </template>
    </Dialog1>
</template>