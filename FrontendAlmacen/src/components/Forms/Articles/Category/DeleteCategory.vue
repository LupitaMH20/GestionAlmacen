<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios';
import {
    AlertDialog, AlertDialogAction, AlertDialogCancel, AlertDialogContent, AlertDialogDescription, AlertDialogFooter,
    AlertDialogHeader, AlertDialogTitle, AlertDialogTrigger
} from '../../../ui/alert-dialog'
import { Trash, Trash2, Ban } from 'lucide-vue-next';

const props = defineProps<{ id_Category: number }>()
const emit = defineEmits(['disableArticle'])
const isLoading = ref(false)

const CategoryDisabled = async (data: any) => {
    try {
        isLoading.value = true
        await axios.patch(`http://127.0.0.1:8000/api/category/${props.id_Category}/`, {
            active: false
        })
        emit('disableArticle', props.id_Category)
    } catch (error) {
        console.log('No se deshabilito el colaborador')
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
                <AlertDialogTitle>Ocultar Categoria</AlertDialogTitle>
                <AlertDialogDescription>
                    ¿Realmente desea ocultar esta categoria?
                    Una vez desactivado, no se encontrara en la lista de activos
                </AlertDialogDescription>
            </AlertDialogHeader>
            <AlertDialogFooter>
                <AlertDialogCancel class="bg-whiite text-black hover:bg-black hover:text-white border border-write">
                    <Ban class="w-6 h-6" />Cancel
                </AlertDialogCancel>
                <AlertDialogAction class="bg-whiite text-black hover:bg-black hover:text-white border border-write"
                    @click.prevent="CategoryDisabled">
                    <Trash2 class="w-6 h-6" /> Desactivar
                </AlertDialogAction>
            </AlertDialogFooter>
        </AlertDialogContent>
    </AlertDialog>
</template>