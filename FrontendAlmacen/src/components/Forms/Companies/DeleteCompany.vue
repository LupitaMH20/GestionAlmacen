<script setup lang="ts">
import {ref} from 'vue'
import axios from 'axios';
import { AlertDialog, AlertDialogAction, AlertDialogCancel, AlertDialogContent, AlertDialogDescription, AlertDialogFooter, 
        AlertDialogHeader, AlertDialogTitle, AlertDialogTrigger} from '../../ui/alert-dialog'
import { Trash, Trash2, Ban } from 'lucide-vue-next';

const props = defineProps<{id_Company:string}>()
const emit =defineEmits(['disablecompany'])
const isLoading = ref(false)

const companyDisabled = async(data: any) =>{
  try{
    isLoading.value=true
    await axios.patch(`http://127.0.0.1:8000/api/companies/${props.id_Company}/`, {
      active: false
    })
    emit('disablecompany', props.id_Company)
  }catch(error){
    console.log('No se deshabilito la empresa')
  } finally{
    isLoading.value = false 
  }
}
</script>

<template>
  <AlertDialog>
    <AlertDialogTrigger><Trash class="w-6 h-6"/></AlertDialogTrigger>
    <AlertDialogContent>
      <AlertDialogHeader>
        <AlertDialogTitle>Ocultar Empresa</AlertDialogTitle>
        <AlertDialogDescription> 
            ¿Realmente desea ocultar esta empresa? 
            Una vez desactivado, no se encontrara en la lista de activos 
        </AlertDialogDescription>
      </AlertDialogHeader>
      <AlertDialogFooter>
        <AlertDialogCancel class="bg-whiite text-black hover:bg-black hover:text-white border border-write">
          <Ban class="w-6 h-6"/>Cancel
        </AlertDialogCancel>
        <AlertDialogAction class="bg-whiite text-black hover:bg-black hover:text-white border border-write"
          @click.prevent="companyDisabled">
          <Trash2 class="w-6 h-6"/> Desactivar
        </AlertDialogAction>
      </AlertDialogFooter>
    </AlertDialogContent>
  </AlertDialog>
</template>