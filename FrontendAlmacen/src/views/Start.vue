<script setup lang="ts">
import ProcessCard from '../components/Elements/Card.vue';
import { ref, computed } from 'vue'; 

interface ProcessData {
    id: number;
    title: string;
    currentStatus: 'Presolicitud' | 'Solicitud' | 'Autorizada' | 'Surtir' | 'Terminada';
    date: string;
    detailsUrl: string;
}

const allProcesses = ref<ProcessData[]>([
    { id: 101, title: 'Consumo personal', currentStatus: 'Autorizada', date: '2025-10-10', detailsUrl: '/process/101',},
    { id: 102, title: 'Herramienta', currentStatus: 'Presolicitud', date: '2025-10-12', detailsUrl: '/process/102',},
    { id: 103, title: 'Consumibles', currentStatus: 'Surtir', date: '2025-10-05', detailsUrl: '/process/103',},
    { id: 104, title: 'Consumo personal', currentStatus: 'Presolicitud', date: '2025-10-01', detailsUrl: '/process/104' },
    { id: 105, title: 'Herramienta', currentStatus: 'Autorizada', date: '2025-10-02', detailsUrl: '/process/105' },
    { id: 106, title: 'Consumible', currentStatus: 'Surtir', date: '2025-10-03', detailsUrl: '/process/106' },
]);

const presolicitud = computed(() => 
    allProcesses.value.filter(p => p.currentStatus === 'Presolicitud' || p.currentStatus === 'Solicitud')
);

const autorizadas = computed(() => 
    allProcesses.value.filter(p => p.currentStatus === 'Autorizada')
);

const SurtirsTerminadas = computed(() => 
    allProcesses.value.filter(p => p.currentStatus === 'Surtir' || p.currentStatus === 'Terminada')
);
</script>

<template>
    <div class="p-6">        
        <div class="grid grid-cols-4 gap-6">

            <section class="bg-gray-50 p-3 rounded-lg min-h-[500px]">
                <h2 class="text-xl font-bold mb-4 border-b pb-2 text-blue-700 whitespace-nowrap">
                    Presolicitudes / Solicitud ({{ presolicitud.length }})
                </h2>
                
                <div class="flex flex-col space-y-3">
                    <ProcessCard 
                        v-for="proc in presolicitud" 
                        :key="proc.id" 
                        :process="proc" 
                    />
                    <p v-if="!presolicitud.length" class="text-gray-500 text-sm italic mt-4">Sin elementos en esta etapa.</p>
                </div>
            </section>

            <section class="bg-gray-50 p-3 rounded-lg min-h-[520px]">
                <h2 class="text-xl font-bold mb-4 border-b pb-2 text-indigo-700 whitespace-nowrap">
                    Autorizadas ({{ autorizadas.length }})
                </h2>
                
                <div class="flex flex-col space-y-3">
                    <ProcessCard 
                        v-for="proc in autorizadas" 
                        :key="proc.id" 
                        :process="proc" 
                    />
                    <p v-if="!autorizadas.length" class="text-gray-500 text-sm italic mt-4">Sin elementos en esta etapa.</p>
                </div>
            </section>

            <section class="bg-gray-50 p-3 rounded-lg min-h-[500px]">
                <h2 class="text-xl font-bold mb-4 border-b pb-2 text-green-700 whitespace-nowrap">
                    Surtir ({{ SurtirsTerminadas.filter(p => p.currentStatus === 'Surtir').length }})
                </h2>
                
                <div class="flex flex-col space-y-3">
                    <ProcessCard 
                        v-for="proc in SurtirsTerminadas.filter(p => p.currentStatus === 'Surtir')" 
                        :key="proc.id" 
                        :process="proc" 
                    />
                    <p v-if="!SurtirsTerminadas.filter(p => p.currentStatus === 'Surtir').length" class="text-gray-500 text-sm italic mt-4">Sin elementos en esta etapa.</p>
                </div>
            </section>

            <section class="bg-gray-50 p-3 rounded-lg min-h-[500px]">
                <h2 class="text-xl font-bold mb-4 border-b pb-2 text-gray-700 whitespace-nowrap">
                    Terminadas ({{ SurtirsTerminadas.filter(p => p.currentStatus === 'Terminada').length }})
                </h2>
                
                <div class="flex flex-col space-y-3">
                    <ProcessCard 
                        v-for="proc in SurtirsTerminadas.filter(p => p.currentStatus === 'Terminada')" 
                        :key="proc.id" 
                        :process="proc" 
                    />
                    <p v-if="!SurtirsTerminadas.filter(p => p.currentStatus === 'Terminada').length" class="text-gray-500 text-sm italic mt-4">Sin elementos en esta etapa.</p>
                </div>
            </section>
        </div>
    </div>
</template>