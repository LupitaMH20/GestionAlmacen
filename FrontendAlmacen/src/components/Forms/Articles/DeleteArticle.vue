<script setup lang="ts">
import { AlertDialog, AlertDialogAction, AlertDialogCancel, AlertDialogContent, AlertDialogDescription, AlertDialogFooter, 
        AlertDialogHeader, AlertDialogTitle, AlertDialogTrigger} from '../../ui/alert-dialog'
import { Trash, Trash2, Ban } from 'lucide-vue-next';
</script>

<template>
  <AlertDialog>
    <AlertDialogTrigger><Trash class="w-6 h-6"/></AlertDialogTrigger>
    <AlertDialogContent>
      <AlertDialogHeader>
        <AlertDialogTitle>Eliminar Producto</AlertDialogTitle>
        <AlertDialogDescription> 
            Realmente desea eliminar este producto? 
            Una vez eliminado no se encontrara su registro 
        </AlertDialogDescription>
      </AlertDialogHeader>
      <AlertDialogFooter>
        <AlertDialogCancel class="bg-whiite text-black hover:bg-black hover:text-white border border-write"><Ban class="w-6 h-6"/>Cancel</AlertDialogCancel>
        <AlertDialogAction class="bg-whiite text-black hover:bg-black hover:text-white border border-write"><Trash2 class="w-6 h-6"/> Eliminar</AlertDialogAction>
      </AlertDialogFooter>
    </AlertDialogContent>
  </AlertDialog>
</template>