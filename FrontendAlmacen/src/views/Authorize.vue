<script setup lang="ts">
import ProcessCard from '../components/Elements/Card.vue';
import { ref, computed } from 'vue'; 
interface ProcessData {
    id: number;
    title: string;
    currentStatus: 'Presolicitud' | 'Solicitud' | 'Autorizada' | 'Surtir' | 'Terminada';
    date: string;
    detailsUrl: string;
    type: 'Consumible' | 'Herramienta' | 'Consumo personal'; 
}
const allProcesses = ref<ProcessData[]>([
    { id: 101, title: 'Consumo personal', currentStatus: 'Autorizada', date: '2025-10-10', detailsUrl: '/process/101',type:'Consumo personal'},
    { id: 102, title: 'Herramienta', currentStatus: 'Presolicitud', date: '2025-10-12', detailsUrl: '/process/102',type:'Herramienta'},
    { id: 103, title: 'Consumibles', currentStatus: 'Surtir', date: '2025-10-05', detailsUrl: '/process/103',type:'Consumible'},
    { id: 104, title: 'Consumo personal', currentStatus: 'Presolicitud', date: '2025-10-01', detailsUrl: '/process/104',type:'Consumo personal' },
    { id: 105, title: 'Herramienta', currentStatus: 'Autorizada', date: '2025-10-02', detailsUrl: '/process/105', type:'Herramienta'},
    { id: 106, title: 'Consumible', currentStatus: 'Surtir', date: '2025-10-03', detailsUrl: '/process/106',type:'Consumible' },
]);
const filterByTypeAndStatus = (type: ProcessData['type']) => {
    return allProcesses.value.filter(p => 
        (p.currentStatus === 'Autorizada') &&
        p.type === type
    );
};

const consumibles = computed(() => filterByTypeAndStatus('Consumible'));
const herramienta = computed(() => filterByTypeAndStatus('Herramienta'));
const consumoPersonal = computed(() => filterByTypeAndStatus('Consumo personal'));

</script>

<template>
    <div class="p-6">

        <div class="grid grid-cols-3 gap-6">

            <section class="bg-gray-50 p-3 rounded-lg min-h-[500px]">
                <h2 class="text-xl font-bold mb-4 border-b pb-2 text-blue-700 whitespace-nowrap">
                    Consumibles ({{ consumibles.length }})
                </h2>
                
                <div class="flex flex-col space-y-3">
                    <ProcessCard 
                        v-for="proc in consumibles" 
                        :key="proc.id" 
                        :process="proc" 
                    />
                    <p v-if="!consumibles.length" class="text-gray-500 text-sm italic mt-4">No hay solicitudes de consumibles.</p>
                </div>
            </section>

            <section class="bg-gray-50 p-3 rounded-lg min-h-[500px]">
                <h2 class="text-xl font-bold mb-4 border-b pb-2 text-orange-700 whitespace-nowrap">
                    Herramienta ({{ herramienta.length }})
                </h2>
                
                <div class="flex flex-col space-y-3">
                    <ProcessCard 
                        v-for="proc in herramienta" 
                        :key="proc.id" 
                        :process="proc" 
                    />
                    <p v-if="!herramienta.length" class="text-gray-500 text-sm italic mt-4">No hay solicitudes de herramienta.</p>
                </div>
            </section>

            <section class="bg-gray-50 p-3 rounded-lg min-h-[500px]">
                <h2 class="text-xl font-bold mb-4 border-b pb-2 text-purple-700 whitespace-nowrap">
                    Consumo personal ({{ consumoPersonal.length }})
                </h2>
                
                <div class="flex flex-col space-y-3">
                    <ProcessCard 
                        v-for="proc in consumoPersonal" 
                        :key="proc.id" 
                        :process="proc" 
                    />
                    <p v-if="!consumoPersonal.length" class="text-gray-500 text-sm italic mt-4">No hay solicitudes de consumo personal.</p>
                </div>
            </section>

        </div>
    </div>
</template>