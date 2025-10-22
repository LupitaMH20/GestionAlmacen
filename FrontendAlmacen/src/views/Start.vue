<script setup lang="ts">
import ProcessCard from '../components/Elements/Card.vue';
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';
import Input from '../components/ui/input/Input.vue'
import Button from '../components/ui/button/Button.vue'
import { Search } from 'lucide-vue-next'
import CreateApplicationC from '../components/Forms/Applications/PersonalConsumption/CreatePersonalConsumption.vue';
import CreateApplicationCO from '../components/Forms/Applications/Consumables/CreateConsumable.vue';
import CreateApplicationT from '../components/Forms/Applications/Tools/CreateTools.vue';
import PreRequestC from '../components/Forms/Applications/Consumables/PreRequest.vue'
import PreRequestCo from '../components/Forms/Applications/PersonalConsumption/PreRequest.vue'
import PreRequestT from '../components/Forms/Applications/Tools/PreRequest.vue'

interface ProcessData {
    id: number;
    title: string;
    currentStatus: 'Presolicitud' | 'Solicitud' | 'Autorizada' | 'Surtir' | 'Terminada';
    date: string;
    detailsUrl: string;
}

const allProcesses = ref<ProcessData[]>([]);

const loadProcesses = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/prerequest/');
        allProcesses.value = response.data.map((item: any) => ({
            id: item.id,
            title: item.type || 'Sin tipo',
            currentStatus: item.status === 'prerequest' ? 'Presolicitud' :
                item.status === 'request' ? 'Solicitud' :
                    item.status === 'authorized' ? 'Autorizada' :
                        item.status === 'supply' ? 'Surtir' : 'Terminada',
            date: item.created_at || 'Sin fecha',
            detailsUrl: `/process/${item.id}`,
        }));
        console.log('Procesos cargados:', allProcesses.value);
    } catch (error) {
        console.error('Error al cargar procesos:', error);
    }
};

const prerequest = computed(() =>
    allProcesses.value.filter(p => p.currentStatus === 'Presolicitud')
);

const applicant  = computed(() =>
    allProcesses.value.filter(p => p.currentStatus === 'Solicitud')
);

const autorizadas = computed(() =>
    allProcesses.value.filter(p => p.currentStatus === 'Autorizada')
);

const SurtirsTerminadas = computed(() =>
    allProcesses.value.filter(p => p.currentStatus === 'Surtir' || p.currentStatus === 'Terminada')
);
onMounted(() => {
    loadProcesses();
});
</script>

<template>
    <div class="p-6">
        <div class="flex justify-between items-center w-full mb-2">
            <div class="flex gap-2">
                <Input placeholder="Buscar colaborador" class="w-75 text-12 font-sans font-light" />
                <Button class="bg-white text-black hover:bg-black hover:text-white border border-gray-300">
                    <Search /> Buscar
                </Button>
            </div>
            <select
                class="border border-gray-300 rounded-md text-base font-normal px-3 py-1 focus:outline-none focus:ring-2 focus:bg-white">
                <option>Consumo Personal</option>
                <option>Consumibles</option>
                <option>Herramientas</option>
            </select>
        </div>
        <div class="flex justify-between items-center w-full mb-2 ">
            <label>Pre Solicitudes</label>
            <div class="flex justify-between items-center p-5 gap-4 ">
                <PreRequestC @createPreRequest="loadProcesses"/>
                <PreRequestCo @createPreRequest="loadProcesses"/>
                <PreRequestT @createPreRequest="loadProcesses"/>
            </div>

        </div>
        <div class="grid grid-cols-5 gap-6 pt-5">

            <section class="bg-gray-50 p-3 rounded-lg min-h-[500px]">
                <h2 class="text-xl font-bold mb-4 border-b pb-2 text-blue-700 whitespace-nowrap">
                    Presolicitudes ({{ prerequest.length }})
                </h2>
                <div class="flex flex-col space-y-3">
                    <ProcessCard v-for="proc in prerequest" :key="proc.id" :process="proc" />
                    <p v-if="!prerequest.length" class="text-gray-500 text-sm italic mt-4">Sin elementos en esta
                        etapa.</p>
                </div>
            </section>

            <section class="bg-gray-50 p-3 rounded-lg min-h-[500px]">
                <h2 class="text-xl font-bold mb-4 border-b pb-2 text-blue-700 whitespace-nowrap">
                    Solicitud ({{ applicant.length }})
                </h2>
                <CreateApplicationC />
                <CreateApplicationCO />
                <CreateApplicationT />
                <div class="flex flex-col space-y-3">
                    <ProcessCard v-for="proc in applicant" :key="proc.id" :process="proc" />
                    <p v-if="!applicant.length" class="text-gray-500 text-sm italic mt-4">Sin elementos en esta
                        etapa.</p>
                </div>
            </section>

            <section class="bg-gray-50 p-3 rounded-lg min-h-[520px]">
                <h2 class="text-xl font-bold mb-4 border-b pb-2 text-indigo-700 whitespace-nowrap">
                    Autorizadas ({{ autorizadas.length }})
                </h2>

                <div class="flex flex-col space-y-3">
                    <ProcessCard v-for="proc in autorizadas" :key="proc.id" :process="proc" />
                    <p v-if="!autorizadas.length" class="text-gray-500 text-sm italic mt-4">Sin elementos en esta etapa.
                    </p>
                </div>
            </section>

            <section class="bg-gray-50 p-3 rounded-lg min-h-[500px]">
                <h2 class="text-xl font-bold mb-4 border-b pb-2 text-green-700 whitespace-nowrap">
                    Surtir ({{SurtirsTerminadas.filter(p => p.currentStatus === 'Surtir').length}})
                </h2>

                <div class="flex flex-col space-y-3">
                    <ProcessCard v-for="proc in SurtirsTerminadas.filter(p => p.currentStatus === 'Surtir')"
                        :key="proc.id" :process="proc" />
                    <p v-if="!SurtirsTerminadas.filter(p => p.currentStatus === 'Surtir').length"
                        class="text-gray-500 text-sm italic mt-4">Sin elementos en esta etapa.</p>
                </div>
            </section>

            <section class="bg-gray-50 p-3 rounded-lg min-h-[500px]">
                <h2 class="text-xl font-bold mb-4 border-b pb-2 text-gray-700 whitespace-nowrap">
                    Terminadas ({{SurtirsTerminadas.filter(p => p.currentStatus === 'Terminada').length}})
                </h2>

                <div class="flex flex-col space-y-3">
                    <ProcessCard v-for="proc in SurtirsTerminadas.filter(p => p.currentStatus === 'Terminada')"
                        :key="proc.id" :process="proc" />
                    <p v-if="!SurtirsTerminadas.filter(p => p.currentStatus === 'Terminada').length"
                        class="text-gray-500 text-sm italic mt-4">Sin elementos en esta etapa.</p>
                </div>
            </section>
        </div>
    </div>
</template>