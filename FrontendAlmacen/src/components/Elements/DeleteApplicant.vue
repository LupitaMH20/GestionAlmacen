<script setup lang="ts">
import { AlertDialog, AlertDialogAction, AlertDialogCancel, AlertDialogContent, AlertDialogDescription, AlertDialogFooter, 
        AlertDialogHeader, AlertDialogTitle, AlertDialogTrigger} from '../ui/alert-dialog'
import { Trash, Trash2, Ban } from 'lucide-vue-next';
</script>

<template>
  <AlertDialog>
    <AlertDialogTrigger>
      <div class="flex items-center gap-2">
        <Trash class="w-6 h-6"/>
      </div>
    </AlertDialogTrigger>
    <AlertDialogContent>
      <AlertDialogHeader>
        <AlertDialogTitle>Desea Cancelar la solicitud</AlertDialogTitle>
        <AlertDialogDescription> 
            Realmente desea cancelar la solicitud? 
            Una vez cancelada ya no segura su proceso
        </AlertDialogDescription>
      </AlertDialogHeader>
      <AlertDialogFooter>
        <AlertDialogCancel class="bg-whiite text-black hover:bg-black hover:text-white border border-write"><Ban class="w-6 h-6"/>Cancel</AlertDialogCancel>
        <AlertDialogAction class="bg-whiite text-black hover:bg-black hover:text-white border border-write"><Trash2 class="w-6 h-6"/> Eliminar</AlertDialogAction>
      </AlertDialogFooter>
    </AlertDialogContent>
  </AlertDialog>
</template>