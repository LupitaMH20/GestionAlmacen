<script setup lang="ts">
import { defineProps } from 'vue';
import { Card, CardContent, CardHeader, CardTitle, CardFooter } from '../ui/card';
import Button from '../ui/button/Button.vue';
import { ArrowRight, FileText, CheckCircle, Clock } from 'lucide-vue-next';
import Dialog from './Dialog.vue';

interface ProcessData {
    id: number;
    title: string;
    currentStatus: 'Presolicitud' | 'Solicitud' | 'Autorizada' | 'Surtir' | 'Terminada';
    date: string;
    detailsUrl: string;
}

const props = defineProps<{
    process: ProcessData;
}>();

const getStatusColor = (status: string) => {
    switch (status) {
        case 'Presolicitud':
            return 'bg-blue-100 text-blue-800';
        case 'Solicitud':
            return 'bg-yellow-100 text-yellow-800';
        case 'Autorizada':
            return 'bg-indigo-100 text-indigo-800';
        case 'Entregada':
            return 'bg-green-100 text-green-800';
        case 'Terminada':
            return 'bg-gray-100 text-gray-800';
        default:
            return 'bg-gray-200 text-gray-700';
    }
};

const getStatusIcon = (status: string) => {
    switch (status) {
        case 'Presolicitud':
        case 'Solicitud':
            return FileText;
        case 'Autorizada':
        case 'Entregada':
        case 'Terminada':
            return CheckCircle;
        default:
            return Clock;
    }
};
</script>

<template>
    <Card class="flex flex-col h-full shadow-lg hover:shadow-xl transition-shadow duration-300">
        <CardHeader>
            <CardTitle class="text-xl font-bold">{{ process.title }} (ID: {{ process.id }})</CardTitle>
        </CardHeader>

        <CardContent class="flex flex-col space-y-3 flex-grow">

            <div
                :class="['p-2 rounded-lg font-semibold text-sm inline-flex items-center', getStatusColor(process.currentStatus)]">
                <component :is="getStatusIcon(process.currentStatus)" class="w-4 h-4 mr-2" />
                <span>Estatus: {{ process.currentStatus }}</span>
            </div>

            <div class="border-t pt-2 mt-2">
                <p class="text-sm text-gray-500">Fecha de Creación: {{ process.date }}</p>
            </div>
        </CardContent>

        <CardFooter class="pt-4">
            <!-- <Dialog></Dialog> -->
             
        </CardFooter>
    </Card>
</template>