<script setup lang="ts">
import ProcessCard from '../components/Elements/Card.vue';
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';

interface ProcessData {
    id: number;
    title: string;
    currentStatus: 'Presolicitud' | 'Solicitud' | 'Autorizada' | 'Surtir' | 'Terminada';
    date: string;
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

    return {
        id: item.id_PreRequest,
        title: item.type ?? item.article ?? 'Sin título',
        currentStatus: statusMap[item.status] ?? 'Presolicitud',
        date: new Date(item.requested_datetime).toLocaleDateString(),
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
        <div class="grid grid-cols-3 gap-6">
            <section class="bg-gray-50 p-3 rounded-lg min-h-[500px]">
                <h2 class="text-xl font-bold mb-4 border-b pb-2 text-blue-700">
                    Consumibles ({{ consumibles.length }})
                </h2>
                <div class="flex flex-col space-y-3">
                    <ProcessCard v-for="proc in consumibles" :key="proc.id" :process="proc"/>
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
                    <ProcessCard v-for="proc in herramienta" :key="proc.id" :process="proc"/>
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
                    <ProcessCard v-for="proc in consumoPersonal" :key="proc.id" :process="proc"/>
                    <p v-if="!consumoPersonal.length" class="text-gray-500 text-sm italic mt-4">
                        No hay solicitudes de consumo personal.
                    </p>
                </div>
            </section>
        </div>
    </div>
</template>
