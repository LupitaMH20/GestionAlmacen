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
import { Card, CardHeader, CardTitle, CardContent } from '../components/ui/card';
import { time } from 'console';

interface ProcessData {
    id: number;
    title: string;
    article: string;
    currentStatus: 'Presolicitud' | 'Solicitud' | 'Autorizada' | 'Surtir' | 'Terminada';
    date: string;
    time : string;
    detailsUrl: string;
}

const allProcesses = ref<ProcessData[]>([]);

const loadProcesses = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/prerequest/');

        const formatDate = (datetime: string) => {
            if (!datetime) return 'Sin fecha';
            const date = new Date(datetime);
            const dia = date.getDate().toString().padStart(2, '0');
            const meses = [ 'Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic' ];
            const mes = meses[date.getMonth()];
            const año = date.getFullYear();
            return `${dia}/${mes}/${año}`;
        };

        allProcesses.value = response.data.map((item: any) => ({
            id: item.id_PreRequest,
            title: item.type || 'Sin tipo',
            article: item.article || 'Sin producto',
            currentStatus: item.status === 'prerequest' ? 'Presolicitud' :
                item.status === 'request' ? 'Solicitud' :
                    item.status === 'authorized' ? 'Autorizada' :
                        item.status === 'supply' ? 'Surtir' : 'Terminada',
            date: formatDate(item.requested_datetime),
            time: new Date(item.requested_datetime).toLocaleTimeString('es-MX', {hour:'2-digit', minute:'2-digit', hour12:true}),
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

const applicant = computed(() =>
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
                <Input placeholder="Buscar" class="w-75 text-12 font-sans font-light" />
                <Button class="bg-white text-black hover:bg-black hover:text-white border border-gray-300">
                    <Search /> Buscar
                </Button>
            </div>
            <div class="flex gap-5 text-{12px}">
                <p>Buscar por: </p>
                <select
                    class="border border-gray-300 rounded-md text-base font-normal px-3 py-1 focus:outline-none focus:ring-2 focus:bg-white">
                    <option>Consumo Personal</option>
                    <option>Consumibles</option>
                    <option>Herramientas</option>
                </select>
            </div>
        </div>

        <div class="flex justify-between items-center w-full mb-2 ">
            <div></div>
            <div class="p-3">
                <label class="flex text-{14 px} justify-end">Registro de nuevas: PreSolicitudes</label>
                <div class="flex justify-between items-center p-2 gap-4 ">
                    <PreRequestC @createPreRequest="loadProcesses" />
                    <PreRequestCo @createPreRequest="loadProcesses" />
                    <PreRequestT @createPreRequest="loadProcesses" />
                </div>
            </div>
        </div>

        <Card class="flex flex-col h-full shadow-lg hover:shadow-xl transition-shadow duration-300">
            <CardContent>
                <div class="grid grid-cols-6 gap-6 ">
                    <section class="bg-gray-50 p-3 rounded-lg min-h-[500px]">
                        <h2 class="text-xl font-bold mb-4 border-b pb-2 text-blue-400 whitespace-nowrap">
                            Presolicitudes ({{ prerequest.length }})
                        </h2>
                        <div class="flex flex-col space-y-3">
                            <ProcessCard v-for="proc in prerequest" :key="proc.id" :process="proc" />
                            <p v-if="!prerequest.length" class="text-gray-500 text-sm italic mt-4">Sin elementos en esta
                                etapa.</p>
                        </div>
                    </section>

                    <section class="bg-gray-50 p-3 rounded-lg min-h-[500px]">
                        <h2 class="text-xl font-bold mb-4 border-b pb-2 text-indigo-500 whitespace-nowrap">
                            Solicitud ({{ applicant.length }})
                        </h2>
                        <!-- <CreateApplicationC />
                <CreateApplicationCO />
                <CreateApplicationT /> -->
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
                            <p v-if="!autorizadas.length" class="text-gray-500 text-sm italic mt-4">Sin elementos en
                                esta etapa.
                            </p>
                        </div>
                    </section>

                    <section class="bg-gray-50 p-3 rounded-lg min-h-[500px]">
                        <h2 class="text-xl font-bold mb-4 border-b pb-2 text-green-600 whitespace-nowrap">
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
                    <section class="bg-gray-50 p-3 rounded-lg min-h-[500px]">
                        <h2 class="text-xl font-bold mb-4 border-b pb-2 text-gray-500 whitespace-nowrap">
                            Archivada ({{SurtirsTerminadas.filter(p => p.currentStatus === 'Surtir').length}})
                        </h2>

                        <div class="flex flex-col space-y-3">
                            <ProcessCard v-for="proc in SurtirsTerminadas.filter(p => p.currentStatus === 'Surtir')"
                                :key="proc.id" :process="proc" />
                            <p v-if="!SurtirsTerminadas.filter(p => p.currentStatus === 'Surtir').length"
                                class="text-gray-500 text-sm italic mt-4">Sin elementos en esta etapa.</p>
                        </div>
                    </section>
                </div>
            </CardContent>
        </Card>
    </div>
</template>