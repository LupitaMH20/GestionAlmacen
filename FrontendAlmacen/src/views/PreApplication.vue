<script setup lang="ts">
import ProcessCard from '../components/Elements/Card.vue';
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';
import { Card, CardHeader, CardTitle, CardContent } from '../components/ui/card';

interface Companies { id_Company: string; name: string };
interface Users { id_user: string; name: string; last_name: string };
interface Collaborators { id_Collaborator: string; name: string; last_name: string };

interface ProcessData {
    id_Request: number;
    title: string;
    article: string;
    currentStatus: 'prerequest' | 'request' | 'authorized' | 'declined' | 'supply' | 'finished' | 'archived';
    date: string;
    time: string;
    type?: string;
    user?: string
    collaborator?: string
    userName?: Users;
    collaboratorName?: Collaborators;
    description?: string
    amount?: number
    status?: string
    order_workshop?: string
    store?: string
    requestingCompany?: string
    supplierCompany?: string
    requestingCompanyName?: Companies
    supplierCompanyName?: Companies
}
const processes = ref<ProcessData[]>([]);

const loadProcesses = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/request/');
        
        const typeMap: Record<string, string> = {
            "Consumable": 'Consumibles',
            "Tool": 'Herramientas',
            "PersonalConsumption": 'Consumo Personal',
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
        processes.value = response.data.map((item: any) => {
            const reqCompanyObj = item.requestingCompany;
            const supCompanyObj = item.supplierCompany;
            const userObj = item.user;
            const collabObj = item.collaborator;

            return {
                id_Request: item.id_Request,
                title: typeMap[item.type] || item.type || 'Sin tipo',
                article: item.article || 'Sin producto',
                currentStatus: item.status,
                date: formatDate(item.request_datetime),
                time: new Date(item.request_datetime).toLocaleTimeString('es-MX', { hour: '2-digit', minute: '2-digit', hour12: true }),
                type: item.type,
                user: userObj?.id_user,
                userName: userObj,
                collaborator: collabObj?.id_Collaborator,
                collaboratorName: collabObj,
                description: item.description,
                amount: item.amount,
                status: item.status,
                order_workshop: item.order_workshop,
                store: item.store,
                requestingCompany: reqCompanyObj?.id_Company,
                supplierCompany: supCompanyObj?.id_Company,
                requestingCompanyName: reqCompanyObj,
                supplierCompanyName: supCompanyObj,
                request: item.request
            };
        });
        console.log('Procesos cargados:', processes.value);
    } catch (error) {
        console.error('Error al cargar procesos:', error);
    }
};

const filterByTypeAndStatus = (type: ProcessData['type']) =>
    processes.value.filter(p => p.currentStatus === 'prerequest' && p.type === type);

const Consumable = computed(() => filterByTypeAndStatus('Consumable'));
const Tools = computed(() => filterByTypeAndStatus('Tools'));
const PersonalConsumption = computed(() => filterByTypeAndStatus('PersonalConsumption'));

onMounted(() => { loadProcesses() });
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
                <div class="grid grid-cols-3 gap-6 h-[65vh] overflow-hidden">

                    <section class="bg-gray-50 overflow-y-auto p-3 rounded-lg min-h-[500px]">
                        <h2 class="text-xl font-bold mb-4 border-b pb-2 text-blue-700">
                            Consumible ({{ Consumable.length }})
                        </h2>
                        <div class="flex flex-col space-y-3">
                            <ProcessCard v-for="proc in Consumable" :key="proc.id_Request" v-bind="proc"
                                @updateRequest="loadProcesses" />
                            <p v-if="!Consumable.length" class="text-gray-500 text-sm italic mt-4">
                                No hay solicitudes de Consumible.
                            </p>
                        </div>
                    </section>

                    <section class="bg-gray-50 overflow-y-auto p-3 rounded-lg min-h-[500px]">
                        <h2 class="text-xl font-bold mb-4 border-b pb-2 text-orange-700">
                            Herramienta ({{ Tools.length }})
                        </h2>
                        <div class="flex flex-col space-y-3">
                            <ProcessCard v-for="proc in Tools" :key="proc.id_Request" v-bind="proc"
                                @updateRequest="loadProcesses" />
                            <p v-if="!Tools.length" class="text-gray-500 text-sm italic mt-4">
                                No hay solicitudes de Herramienta.
                            </p>
                        </div>
                    </section>

                    <section class="bg-gray-50 overflow-y-auto p-3 rounded-lg min-h-[500px]">
                        <h2 class="text-xl font-bold mb-4 border-b pb-2 text-purple-700">
                            ConsumoPersonal ({{ PersonalConsumption.length }})
                        </h2>
                        <div class="flex flex-col space-y-3">
                            <ProcessCard v-for="proc in PersonalConsumption" :key="proc.id_Request" v-bind="proc"
                                @updateRequest="loadProcesses" />
                            <p v-if="!PersonalConsumption.length" class="text-gray-500 text-sm italic mt-4">
                                No hay solicitudes de ConsumoPersonal.
                            </p>
                        </div>
                    </section>
                </div>
            </CardContent>
        </Card>
    </div>
</template>