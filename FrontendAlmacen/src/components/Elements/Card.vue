<script setup lang="ts">
import { defineProps, onMounted, ref, computed } from 'vue';
import { Card, CardContent, CardHeader, CardTitle, CardFooter } from '../ui/card';
import Dialog from './Dialog.vue';
import { Eye, FileText } from 'lucide-vue-next'

interface Companies { id_Company: string; name: string };
interface Users { id_user: string; name: string; };
interface Collaborators { id_Collaborator: string; name: string; last_name: string };
interface Article { id_mainarticle: string, name: string }

const process = defineProps<{
    id_Request: number | string;
    position?: string;
    title: string;
    article: string;
    currentStatus: 'prerequest' | 'request' | 'authorized' | 'declined' | 'supply' | 'finished' | 'archived' | 'returnExchange';
    date: string;
    time: string;
    type?: string;
    user?: Users;
    userName?: Users;
    collaborator?: string;
    collaboratorName?: Collaborators;
    description?: string;
    amount?: number;
    status?: string;
    order_workshop?: string;
    store?: string;
    requestingCompany?: string;
    supplierCompany?: string;
    requestingCompanyName?: Companies;
    supplierCompanyName?: Companies;
    acceptance?: {
        id_acceptance: number;
        user?: Users;
        userName?: Users;
        article?: Article;
        articleName?: Article;
        date?: string;
        time?: string;
        requestactions?: {
            id_RequestActions: number;
            action: 'authorized' | 'declined';
            comment: string;
            requestactions_datetime: string;
            user: Users;
            date?: string;
            time?: string;
            supply?: {
                id_supply: number;
                user?: Users;
                userName?: Users;
                collaborator?: string;
                collaboratorName?: Collaborators;
                comment?: string;
                date?: string;
                time?: string;
            } | null
        } | null;
    } | null;
}>();

const isDialogOpen = ref(false)
const emit = defineEmits(['card']);

const displayDateInfo = computed(() => {
    if ((process.currentStatus === 'supply') && 
        process.acceptance?.requestactions?.supply?.date) {
        return {
            label: 'Surtido',
            date: process.acceptance.requestactions.supply.date,
            time: process.acceptance.requestactions.supply.time
        };
    }
    if ((process.currentStatus === 'authorized' || process.currentStatus === 'declined') && 
        process.acceptance?.requestactions?.date) {
        return {
            label: process.currentStatus === 'authorized' ? 'Autorización' : 'Rechazo',
            date: process.acceptance.requestactions.date,
            time: process.acceptance.requestactions.time
        };
    }
    if (process.currentStatus === 'request' && process.acceptance?.date) {
        return {
            label: 'Solicitud',
            date: process.acceptance.date,
            time: process.acceptance.time
        };
    }
    return {
        label: 'Creación',
        date: process.date,
        time: process.time
    };
});
</script>

<template>
    <Card class="flex flex-col h-[35vh] w-full shadow-lg hover:shadow-xl transition-shadow duration-300">
        <CardHeader>
            <CardTitle class="text-24 font-lingh">{{ process.title }} (ID: {{ process.id_Request }})</CardTitle>
            <p>Producto: {{ process.article }}</p>
            <div v-if="process.currentStatus === 'declined'" class="flex justify-end text-center ">
                <span class="font-bold text-red-600 bg-red-100 px-3 py-1 rounded-full text-xs uppercase">
                    Rechazada
                </span>
            </div>
        </CardHeader>

        <CardContent class="flex flex-col space-y-3 flex-grow">
            <div class="border-t pt-2 ">
                <p class="text-sm text-gray-500">Creación</p>
                <p class="text-sm text-gray-500">Fecha: {{ displayDateInfo.date }} </p>
                <p class="text-sm text-gray-500">Hora: {{ displayDateInfo.time }} </p>
            </div>
        </CardContent>

        <CardFooter class="flex justify-end ">
            <Dialog v-model="isDialogOpen" :title="`Detalles de ${process.title}`" titleButton="Detalles" :iconP="Eye"
                :iconT="FileText" :Request="process" @dialog="emit('card')">
            </Dialog>
        </CardFooter>
    </Card>
</template>