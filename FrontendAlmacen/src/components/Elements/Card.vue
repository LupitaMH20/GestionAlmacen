<script setup lang="ts">
import { defineProps } from 'vue';
import { Card, CardContent, CardHeader, CardTitle, CardFooter } from '../ui/card';

interface ProcessData {
    id: number;
    title: string;
    article: string;
    currentStatus: 'Presolicitud' | 'Solicitud' | 'Autorizada' | 'Surtir' | 'Terminada';
    date: string;
    time: string;
    detailsUrl: string;
}

const props = defineProps<{
    process: ProcessData;
}>();
</script>

<template>
    <Card class="flex flex-col h-full shadow-lg hover:shadow-xl transition-shadow duration-300">
        <CardHeader>
            <CardTitle class="text-24 font-linght">{{ process.title }} (ID: {{ process.id }})</CardTitle>
            <p>Producto: {{ process.article }}</p>
        </CardHeader>

        <CardContent class="flex flex-col space-y-3 flex-grow">
            <div class="border-t pt-2 mt-2">
                <p class="text-sm text-gray-500">Creación</p>
                <p class="text-sm text-gray-500">Fecha: {{ process.date }} </p>
                <p class="text-sm text-gray-500">Hora: {{ process.time }} </p>
            </div>
        </CardContent>

        <CardFooter class="pt-4">
            <!-- <Dialog></Dialog> -->
             
        </CardFooter>
    </Card>
</template>