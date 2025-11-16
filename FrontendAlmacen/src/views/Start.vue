<script setup lang="ts">
import ProcessCard from '../components/Elements/Card.vue';
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';
import Input from '../components/ui/input/Input.vue'
import Button from '../components/ui/button/Button.vue'
import { Search } from 'lucide-vue-next'
import PreRequestC from '../components/Forms/Applications/Consumables/PreRequest/PreRequest.vue'
import PreRequestCP from '../components/Forms/Applications/PersonalConsumption/PreRequest/PreRequest.vue'
import PreRequestT from '../components/Forms/Applications/Tools/PreRequest/PreRequest.vue'
import { Card, CardContent } from '../components/ui/card';

interface Companies { id_Company: string; name: string }
interface Users { id_user: string; name: string; last_name: string };
interface Collaborators { id_Collaborator: string; name: string; last_name: string };
interface Article {id_mainarticle: string, name:string}

const searchQuery = ref('');
const selectedType = ref('All')
const displayedProcesses = ref<any[]>([]);

interface ProcessData {
    id_Request: number | string;
    title: string;
    article: string;
    currentStatus: 'prerequest' | 'request' | 'authorized' | 'declined' | 'supply' | 'finished' | 'archived';
    date: string;
    time: string;
    type?: string;
    user?: string;
    collaborator?: string;
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

    id_acceptance?: string | number;
    articleName?: Article;
}

const allProcesses = ref<ProcessData[]>([]);

const loadProcesses = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/request/');

        const formatDate = (datetime: string) => {
            if (!datetime) return 'Sin fecha';
            const date = new Date(datetime);
            const dia = date.getDate().toString().padStart(2, '0');
            const meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'];
            const mes = meses[date.getMonth()];
            const año = date.getFullYear();
            return `${dia}/${mes}/${año}`;
        };

        const typeMap: Record<string, string> = {
            "Consumable": 'Consumibles',
            "Tool": 'Herramientas',
            "PersonalConsumption": 'Consumo Personal',
        };

        allProcesses.value = response.data.map((item: any) => {
            const reqCompanyObj = item.requestingCompany;
            const supCompanyObj = item.supplierCompany;
            const userObj = item.user;
            const collabObj = item.collaborator;
            const acceptanceObj = item.acceptance;

            const originalType = item.type;
            const translatedTitle = typeMap[originalType] || originalType || 'Sin tipo';

            console.log('Procesando item:', userObj);
            return {
                id_Request: item.id_Request,
                title: translatedTitle,
                article: item.article || 'Sin producto',
                currentStatus: item.status,
                date: formatDate(item.request_datetime),
                time: new Date(item.request_datetime).toLocaleTimeString('es-MX', { hour: '2-digit', minute: '2-digit', hour12: true }),
                type: originalType,
                user: userObj.id_user,
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

                acceptance: acceptanceObj
            };
        });
        displayedProcesses.value = [...allProcesses.value];
        console.log('Procesos cargados:', allProcesses.value);
    } catch (error) {
        console.error('Error al cargar procesos:', error);
    }
};

const prerequest = computed(() =>
    displayedProcesses.value.filter(p => p.currentStatus === 'prerequest')
);

const request = computed(() =>
    displayedProcesses.value.filter(p => p.currentStatus === 'request')
);

const authorized = computed(() =>
    displayedProcesses.value.filter(p => p.currentStatus === 'authorized')
);

const declined = computed(() =>
    displayedProcesses.value.filter(p => p.currentStatus === 'declined')
);

const supplyFinished = computed(() =>
    displayedProcesses.value.filter(p => p.currentStatus === 'supply' || p.currentStatus === 'finished')
);

const archived = computed(() =>
    displayedProcesses.value.filter(p => p.currentStatus === 'archived')
);

const searchProcess = () => {
    const query = searchQuery.value.toLowerCase().trim();
    const type = selectedType.value;

    let filteredByType = [];
    if (type === 'All') {
        filteredByType = [...allProcesses.value];
    } else {
        filteredByType = allProcesses.value.filter(proc => proc.title === type);
    }

    if (!query) {
        displayedProcesses.value = filteredByType;
        return;
    }

    displayedProcesses.value = filteredByType.filter(proc => {
        const inId = proc.id_Request.toString().includes(query);
        const inTitle = proc.title.toLowerCase().includes(query);
        const inArticle = proc.article.toLowerCase().includes(query);
        const inrequest = (
            proc.userName?.name.toLowerCase() + ' ' +
            proc.userName?.last_name.toLowerCase()
        ).includes(query);
        const inDescription = proc.description?.toLowerCase().includes(query) || false;
        return inId || inTitle || inArticle || inrequest || inDescription;
    });
}
onMounted(() => {
    loadProcesses();
});
</script>

<template>
    <div class="p-6">
        <div class="flex justify-between items-center w-full mb-2">
            <div class="p-3">
                <label class="flex text-{14 px}">Registro de nuevas: PreSolicitudes</label>
                <div class="flex justify-between items-center p-2 gap-4 ">
                    <PreRequestC @createPreRequest="loadProcesses" />
                    <PreRequestCP @createPreRequest="loadProcesses" />
                    <!-- <PreRequestT @createPreRequest="loadProcesses" /> -->
                </div>
            </div>
            <div class="flex gap-5 text-{12px}">
                <p>Buscar por: </p>
                <select v-model="selectedType" @change="searchProcess"
                    class="border border-gray-300 rounded-md text-base font-normal px-3 py-1 focus:outline-none focus:ring-2 focus:bg-white">
                    <option value="All"> Todos </option>
                    <option value="Consumo Personal"> Consumo Personal </option>
                    <option value="Consumibles"> Consumibles </option>
                    <option value="Herramientas"> Herramientas </option>
                </select>
            </div>
        </div>

        <div class="flex justify-between items-center w-full mb-2 ">

        </div>

        <Card class="flex flex-col shadow-lg hover:shadow-xl transition-shadow duration-300">
            <CardContent>
                <div class="grid grid-cols-6 h-[65vh] w-full overflow-x-auto gap-50">
                    <section class="bg-gray-50 p-3 rounded-lg min-h-[698vh] min-w-[28vh]">
                        <h2 class="text-xl font-bold mb-4 border-b pb-2 text-blue-400 whitespace-nowrap">
                            Presolicitudes ({{ prerequest.length }})
                        </h2>
                        <div class="flex flex-col space-y-3">
                            <ProcessCard v-for="proc in prerequest" :key="proc.id_Request" v-bind="proc"
                                @card="loadProcesses" />
                            <p v-if="!prerequest.length" class="text-gray-500 text-sm italic mt-4">Sin elementos en esta
                                etapa.</p>
                        </div>
                    </section>

                    <section class="bg-gray-50 p-3 rounded-lg min-h-[698vh] min-w-[28vh]">
                        <h2 class="text-xl font-bold mb-4 border-b pb-2 text-indigo-500 whitespace-nowrap">
                            Solicitud ({{ request.length }})
                        </h2>
                        <div class="flex flex-col space-y-3">
                            <ProcessCard v-for="proc in request" :key="proc.id_Request" v-bind="proc" />
                            <p v-if="!request.length" class="text-gray-500 text-sm italic mt-4">Sin elementos en esta
                                etapa.</p>
                        </div>
                    </section>

                    <section class="bg-gray-50 p-3 rounded-lg min-h-[698vh] min-w-[28vh]">
                        <h2 class="text-xl font-bold mb-4 border-b pb-2 text-indigo-700 whitespace-nowrap">
                            Autorizadas ({{ authorized.length }})
                        </h2>

                        <div class="flex flex-col space-y-3">
                            <ProcessCard v-for="proc in authorized" :key="proc.id_Request" v-bind="proc" />
                            <p v-if="!authorized.length" class="text-gray-500 text-sm italic mt-4">Sin elementos en
                                esta etapa.
                            </p>
                        </div>
                    </section>

                    <section class="bg-gray-50 p-3 rounded-lg min-h-[698vh] min-w-[28vh]">
                        <h2 class="text-xl font-bold mb-4 border-b pb-2 text-green-600 whitespace-nowrap">
                            Surtir ({{supplyFinished.filter(p => p.currentStatus === 'supply').length}})
                        </h2>

                        <div class="flex flex-col space-y-3">
                            <ProcessCard v-for="proc in supplyFinished.filter(p => p.currentStatus === 'supply')"
                                :key="proc.id_Request" v-bind="proc" />
                            <p v-if="!supplyFinished.filter(p => p.currentStatus === 'supply').length"
                                class="text-gray-500 text-sm italic mt-4">Sin elementos en esta etapa.</p>
                        </div>
                    </section>

                    <section class="bg-gray-50 p-3 rounded-lg min-h-[698vh] min-w-[28vh]">
                        <h2 class="text-xl font-bold mb-4 border-b pb-2 text-gray-700 whitespace-nowrap">
                            Terminadas ({{supplyFinished.filter(p => p.currentStatus === 'finished').length}})
                        </h2>

                        <div class="flex flex-col space-y-3">
                            <ProcessCard v-for="proc in supplyFinished.filter(p => p.currentStatus === 'finished')"
                                :key="proc.id_Request" v-bind="proc" />
                            <p v-if="!supplyFinished.filter(p => p.currentStatus === 'finished').length"
                                class="text-gray-500 text-sm italic mt-4">Sin elementos en esta etapa.</p>
                        </div>
                    </section>

                    <section class="bg-gray-50 p-3 rounded-lg min-h-[500px] min-w-[28vh]">
                        <h2 class="text-xl font-bold mb-4 border-b pb-2 text-gray-500 whitespace-nowrap">
                            Archivada ({{ archived.length }})
                        </h2>

                        <div class="flex flex-col space-y-3">
                            <ProcessCard v-for="proc in archived" :key="proc.id_Request" v-bind="proc" />
                            <p v-if="!archived.values" class="text-gray-500 text-sm italic mt-4">Sin elementos en esta
                                etapa.</p>
                        </div>
                    </section>
                </div>
            </CardContent>
        </Card>
    </div>
</template>