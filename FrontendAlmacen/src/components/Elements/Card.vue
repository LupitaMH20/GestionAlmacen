<script setup lang="ts">
import { defineProps, onMounted, ref } from 'vue';
import { Card, CardContent, CardHeader, CardTitle, CardFooter } from '../ui/card';
import Dialog from './Dialog.vue';
import { Eye, FileText } from 'lucide-vue-next'

interface Companies{id_Company: string; name: string };
interface Users { id_user: string; name: string; };
interface Collaborators { id_Collaborator: string; name: string; last_name: string };

const process = defineProps <{
    id_Request: number | string
    position?: string
    title: string
    article: string
    currentStatus: 'prerequest' | 'request' | 'authorized' | 'declined' | 'supply' | 'finished' | 'archived' | 'returnExchange';
    date: string
    time: string
    type?: string
    user?: string
    userName?: Users
    collaborator?: string
    collaboratorName?: Collaborators
    description?: string
    amount?: number
    status?: string
    order_workshop?: string
    store?: string
    requestingCompany?: string
    supplierCompany?: string
    requestingCompanyName?: Companies
    supplierCompanyName?: Companies
}>();

const isDialogOpen = ref(false)
const emit = defineEmits(['card']);
</script>

<template>
    <Card class="flex flex-col h-[35vh] w-full shadow-lg hover:shadow-xl transition-shadow duration-300">
        <CardHeader>
            <CardTitle class="text-24 font-lingh">{{ process.title }} (ID: {{ process.id_Request }})</CardTitle>
            <p>Producto: {{ process.article }}</p>
        </CardHeader>

        <CardContent class="flex flex-col space-y-3 flex-grow">
            <div class="border-t pt-2 mt-2">
                <p class="text-sm text-gray-500">Creación</p>
                <p class="text-sm text-gray-500">Fecha: {{ process.date }} </p>
                <p class="text-sm text-gray-500">Hora: {{ process.time }} </p>
            </div>
        </CardContent>

        <CardFooter class="flex justify-end ">
            <Dialog v-model="isDialogOpen" :title="`Detalles de ${process.title}`" titleButton="Detalles" :iconP="Eye"
                :iconT="FileText" :Request="process" @dialog="emit('card')">
            </Dialog>
        </CardFooter>
    </Card>
</template>