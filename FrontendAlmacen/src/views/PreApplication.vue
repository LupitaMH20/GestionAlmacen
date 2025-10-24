<script setup lang="ts">
import ProcessCard from '../components/Elements/Card.vue';
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';
import { Card, CardHeader, CardTitle, CardContent } from '../components/ui/card';

interface ProcessData {
    id: number;
    title: string;
    currentStatus: 'Presolicitud' | 'Solicitud' | 'Autorizada' | 'Surtir' | 'Terminada';
    date: string;
    time: string;
    detailsUrl: string;
    type: 'Consumible' | 'Herramienta' | 'Consumo personal';
}
const processes = ref<ProcessData[]>([]);

const mapProcess = (item: any): ProcessData => {
    const statusMap: Record<string, ProcessData['currentStatus']> = {
        prerequest: 'Presolicitud',
        request: 'Solicitud',
        authorized: 'Autorizada',
        supply: 'Surtir',
        finished: 'Terminada',
    };
    const typeMap: Record<string, ProcessData['type']> = {
        Consumible: 'Consumible',
        Herramienta: 'Herramienta',
        ConsumoPersonal: 'Consumo personal',
    };

    const formatDate = (datetime: string) => {
        if (!datetime) return 'Sin fecha';
        const date = new Date(datetime);
        const dia = date.getDate().toString().padStart(2, '0');
        const meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'];
        const mes = meses[date.getMonth()];
        const año = date.getFullYear();
        return `${dia}/${mes}/${año}`;
    };

    return {
        id: item.id_PreRequest,
        title: item.type ?? item.article ?? 'Sin título',
        currentStatus: statusMap[item.status] ?? 'Presolicitud',
        date: formatDate(item.requested_datetime),
        time: new Date(item.requested_datetime).toLocaleTimeString('es-MX', { hour: '2-digit', minute: '2-digit', hour12: true }),
        detailsUrl: `/process/${item.id_PreRequest}`,
        type: typeMap[item.type] ?? 'Consumible'
    };
};
const loadProcess = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/prerequest/');
        processes.value = response.data.map(mapProcess);
    } catch (error) {
        console.error('Error al cargar los procesos:', error);
    }
};
const filterByTypeAndStatus = (type: ProcessData['type']) =>
    processes.value.filter(p => p.currentStatus === 'Presolicitud' && p.type === type);

const consumibles = computed(() => filterByTypeAndStatus('Consumible'));
const herramienta = computed(() => filterByTypeAndStatus('Herramienta'));
const consumoPersonal = computed(() => filterByTypeAndStatus('Consumo personal'));

onMounted(loadProcess);
</script>

<template>
    <div class="p-6">
        <Card class="flex flex-col h-full shadow-lg hover:shadow-xl transition-shadow duration-300">
            <CardHeader>
                <CardTitle
                    class="flex justify-center text-4xl font-sans font-bold text-blue-400 bg-gray-50 p-3 rounded-lg">
                    PreSolicitudes
                </CardTitle>
            </CardHeader>
            <CardContent>
                <div class="grid grid-cols-3 gap-6">
                    <section class="bg-gray-50 p-3 rounded-lg min-h-[500px]">
                        <h2 class="text-xl font-bold mb-4 border-b pb-2 text-blue-700">
                            Consumibles ({{ consumibles.length }})
                        </h2>
                        <div class="flex flex-col space-y-3">
                            <ProcessCard v-for="proc in consumibles" :key="proc.id" :process="proc" />
                            <p v-if="!consumibles.length" class="text-gray-500 text-sm italic mt-4">
                                No hay solicitudes de consumibles.
                            </p>
                        </div>
                    </section>

                    <section class="bg-gray-50 p-3 rounded-lg min-h-[500px]">
                        <h2 class="text-xl font-bold mb-4 border-b pb-2 text-orange-700">
                            Herramienta ({{ herramienta.length }})
                        </h2>
                        <div class="flex flex-col space-y-3">
                            <ProcessCard v-for="proc in herramienta" :key="proc.id" :process="proc" />
                            <p v-if="!herramienta.length" class="text-gray-500 text-sm italic mt-4">
                                No hay solicitudes de herramienta.
                            </p>
                        </div>
                    </section>

                    <section class="bg-gray-50 p-3 rounded-lg min-h-[500px]">
                        <h2 class="text-xl font-bold mb-4 border-b pb-2 text-purple-700">
                            Consumo personal ({{ consumoPersonal.length }})
                        </h2>
                        <div class="flex flex-col space-y-3">
                            <ProcessCard v-for="proc in consumoPersonal" :key="proc.id" :process="proc" />
                            <p v-if="!consumoPersonal.length" class="text-gray-500 text-sm italic mt-4">
                                No hay solicitudes de consumo personal.
                            </p>
                        </div>
                    </section>
                </div>
            </CardContent>
        </Card>
    </div>
</template>
