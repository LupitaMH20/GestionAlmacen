<script setup lang="ts">
import Dialog1 from '../../Elements/Dialog1.vue';
import FormUserC from './FormUserC.vue';
import { UserPlus } from 'lucide-vue-next';
import axios from 'axios'
import { ref } from 'vue'

const formRef = ref<any>(null)
const isDialogisOpen = ref(false)
const emit = defineEmits(['userCreated'])

const handleCancel = () => {
    isDialogisOpen.value=false
  console.log("Acción de Cancelar");
}

const apiSaveUser  = async (data: any) => {
  try {
    await axios.post('http://127.0.0.1:8000/api/users/', data)
    console.log('Usuario guardado correctamente', data)
    isDialogisOpen.value=false
    emit('userCreated')
  } catch (error) {
    console.log('Error al guardar usuario', error)
  }
}

const handleSave = () => {
  if (formRef.value) {
    const data = formRef.value.submitForm()
    if(data){
        apiSaveUser(data)
    }
  } else {
    console.log("No hay datos del formulario")
  }
}
</script>

<template>
  <Dialog1 
      title="Registro de Usuario" 
      :iconP="UserPlus" 
      :iconT="UserPlus"
      @cancel="handleCancel"
      @save="handleSave"
      v-model:open="isDialogisOpen">
      <template #forms>
          <FormUserC ref="formRef" />
      </template>
  </Dialog1>
</template>
