<script setup lang="ts">
import { ref } from 'vue'
import {
  AlertDialog, AlertDialogAction, AlertDialogCancel, AlertDialogContent,
  AlertDialogDescription, AlertDialogFooter, AlertDialogHeader,
  AlertDialogTitle, AlertDialogTrigger
} from '../../ui/alert-dialog'
import { Trash, Trash2, Ban } from 'lucide-vue-next'
import axios from 'axios'

const props = defineProps<{ id_user: string }>()
const emit = defineEmits(['userDisabled'])

const isLoading = ref(false)
const disabledUser = async () => {
  try {
    isLoading.value = true
    await axios.patch(`http://127.0.0.1:8000/api/users/${props.id_user}/`, {
      active: false
    })
    emit('userDisabled', props.id_user)
  } catch (error) {
    console.error('Error al desactivar usuario', error)
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <AlertDialog>
    <AlertDialogTrigger>
      <div class="flex items-center gap-2">
        <Trash class="w-6 h-6" />
        <span>Ocultar</span>
      </div>
    </AlertDialogTrigger>

    <AlertDialogContent>
      <AlertDialogHeader>
        <AlertDialogTitle>Ocultar Usuario</AlertDialogTitle>
        <AlertDialogDescription>
          ¿Realmente desea ocultar este usuario?
          Una vez desactivado, no aparecerá en la lista de activos.
        </AlertDialogDescription>
      </AlertDialogHeader>

      <AlertDialogFooter class="flex gap-2">
        <AlertDialogCancel
          class="bg-white text-black hover:bg-black hover:text-white border border-gray-300 px-4 py-2 flex items-center gap-1">
          <Ban class="w-5 h-5" /> Cerrar
        </AlertDialogCancel>

        <AlertDialogAction class="bg-whiite text-black hover:bg-black hover:text-white border border-write"
          @click.prevent="disabledUser">
          <Trash2 class="w-5 h-5" /> Desactivar
        </AlertDialogAction>
      </AlertDialogFooter>
    </AlertDialogContent>
  </AlertDialog>
</template>
