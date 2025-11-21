<script setup lang="ts">
import ProcessCard from '../components/Elements/Card.vue';
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';
import PreRequestC from '../components/Forms/Applications/Consumables/PreRequest/PreRequest.vue'
import PreRequestCP from '../components/Forms/Applications/PersonalConsumption/PreRequest/PreRequest.vue'
import PreRequestT from '../components/Forms/Applications/Tools/PreRequest/PreRequest.vue'
import { Card, CardContent } from '../components/ui/card';

interface Companies { id_Company: string; name: string }
interface Users { id_user: string; name: string; last_name: string };
interface Collaborators { id_Collaborator: string; name: string; last_name: string };
interface Article { id_mainarticle: string; name: string };

interface ProcessData {
    id_Request: number | string;
    title: string;
    article: string;
    articleName?: Article;
    currentStatus: 'prerequest' | 'request' | 'authorized' | 'declined' | 'supply' | 'finished' | 'archived';
    date: string;
    time: string;
    type?: string;
    user?: string;
    collaborator?: string;
    userName?: Users;
    collaboratorName?: Collaborators;
    description?: string;
    amount?: number;
    status?: string;
    order_workshop?: string;
    store?: string;
    requestingCompany?: string;
    supplierCompany?: string;
    requestingCompanyName?: Companies;
    supplierCompanyName?: Companies;
    unitPrice?: number;
    totalValue?: number;
    acceptance?: {
        id_acceptance: number;
        user?: string;
        userName?: Users;
        article?: string;
        articleName?: Article;
        date?: string;
        time?: string;
        requestactions?: {
            id_RequestActions: number;
            action: 'authorized' | 'declined';
            comment: string;
            requestactions_datetime: string;
            user: Users;
            date?: string;
            time?: string;
            supply?: {
                id_supply: number;
                user?: Users;
                userName?: Users;
                collaborator?: string;
                collaboratorName?: Collaborators;
                comment?: string;
                date?: string;
                time?: string;
            } | null
        } | null;
    } | null;
}

const searchQuery = ref('');
const selectedType = ref('All')
const displayedProcesses = ref<ProcessData[]>([]);
const allProcesses = ref<ProcessData[]>([]);

const formatCurrency = (value: number) => {
    return new Intl.NumberFormat('es-MX', {
        style: 'currency',
        currency: 'MXN',
        minimumFractionDigits: 2
    }).format(value);
};

const calculateTotalMoney = (list: ProcessData[]) => {
    const total = list.reduce((acc, item) => {
        const value = item.totalValue || 0;
        return acc + value;
    }, 0);
    return total;
};

const loadProcesses = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/request/');
        console.log('🔍 Primera respuesta del backend:', response.data[0]);

        const formatDate = (datetime: string) => {
            if (!datetime) return 'Sin fecha';
            const date = new Date(datetime);
            const dia = date.getDate().toString().padStart(2, '0');
            const meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'];
            const mes = meses[date.getMonth()];
            const año = date.getFullYear();
            return `${dia}/${mes}/${año}`;
        };

        const formatTime = (datetime: string) => {
            if (!datetime) return 'Sin hora';
            const date = new Date(datetime);
            return date.toLocaleTimeString('es-MX', {
                hour: '2-digit',
                minute: '2-digit',
                hour12: true
            });
        };

        const typeMap: Record<string, string> = {
            "Consumable": 'Consumibles',
            "Tool": 'Herramientas',
            "PersonalConsumption": 'Consumo Personal',
        };

        allProcesses.value = response.data.map((item: any) => {
            const unitPrice = parseFloat(item.article_price) || 0;
            const amount = parseFloat(item.amount) || 0;
            const totalValue = unitPrice * amount;

            const reqCompanyObj = item.requestingCompany;
            const supCompanyObj = item.supplierCompany;
            const userObj = item.user;
            const collabObj = item.collaborator;
            const acceptanceObj = item.acceptance;

            let acceptance = null;
            if (acceptanceObj) {
                const requestActionsObj = acceptanceObj.requestactions;
                let requestactions = null;
                if (requestActionsObj) {
                    const supplyObj = requestActionsObj.supply;
                    let supply = null;
                    if (supplyObj) {
                        supply = {
                            id_supply: supplyObj.id_supply,
                            user: supplyObj.user,
                            userName: supplyObj.user,
                            collaborator: supplyObj.collaborator?.id_Collaborator || supplyObj.collaborator,
                            collaboratorName: supplyObj.collaborator,
                            comment: supplyObj.comment,
                            date: formatDate(supplyObj.supply_datetime),
                            time: formatTime(supplyObj.supply_datetime)
                        };
                    }

                    requestactions = {
                        id_RequestActions: requestActionsObj.id_RequestActions,
                        action: requestActionsObj.action,
                        comment: requestActionsObj.comment,
                        requestactions_datetime: requestActionsObj.requestactions_datetime,
                        user: requestActionsObj.user,
                        userName: requestActionsObj.user,
                        date: formatDate(requestActionsObj.requestactions_datetime),
                        time: formatTime(requestActionsObj.requestactions_datetime),
                        supply: supply
                    };
                }

                acceptance = {
                    id_acceptance: acceptanceObj.id_acceptance,
                    user: acceptanceObj.user,
                    userName: acceptanceObj.user,
                    article: acceptanceObj.article?.id_mainarticle || acceptanceObj.article,
                    articleName: acceptanceObj.article,
                    date: formatDate(acceptanceObj.acceptance_datetime),
                    time: formatTime(acceptanceObj.acceptance_datetime),
                    requestactions: requestactions
                };
            }

            const processData = {
                id_Request: item.id_Request,
                title: typeMap[item.type] || 'Sin tipo',
                article: item.article,
                articleName: item.article_obj,
                currentStatus: item.status || 'solicitud',
                date: formatDate(item.request_datetime),
                time: formatTime(item.request_datetime),
                type: item.type,
                user: userObj,
                userName: userObj,
                collaborator: collabObj?.id_Collaborator,
                collaboratorName: collabObj,
                description: item.description,
                amount: amount,
                unitPrice: unitPrice,
                totalValue: totalValue,
                status: item.status,
                order_workshop: item.order_workshop,
                store: item.store,
                requestingCompany: reqCompanyObj?.id_Company,
                supplierCompany: supCompanyObj?.id_Company,
                requestingCompanyName: reqCompanyObj,
                supplierCompanyName: supCompanyObj,
                acceptance: acceptance
            };
            console.log('ProcessData construido:', {
                id: processData.id_Request,
                articleId: processData.article,
                articleName: processData.articleName
            });

            return processData;
        });

        displayedProcesses.value = [...allProcesses.value];
        console.log('Total procesos cargados:', allProcesses.value.length);
        const conNombre = allProcesses.value.filter(p => p.articleName?.name).length;
        console.log(`Procesos con nombre de artículo: ${conNombre}/${allProcesses.value.length}`);
        
    } catch (error) {
        console.error('Error al cargar procesos:', error);
    }
};

const prerequestDeclined = computed(() =>
    displayedProcesses.value.filter(p => p.currentStatus === 'prerequest' || p.currentStatus === 'declined')
);

const request = computed(() =>
    displayedProcesses.value.filter(p => p.currentStatus === 'request')
);

const authorized = computed(() =>
    displayedProcesses.value.filter(p => p.currentStatus === 'authorized')
);

const supply = computed(() =>
    displayedProcesses.value.filter(p => p.currentStatus === 'supply')
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
                    <PreRequestT @createPreRequest="loadProcesses" />
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
                <div class="grid grid-cols-5 h-[65vh] w-full overflow-x-auto gap-50">
                    <section class="bg-gray-50 p-3 rounded-lg h-full min-w-[34vh]">
                        <h2 class="text-xl font-bold mb-4 border-b pb-2 text-blue-400 whitespace-nowrap">
                            <div class="flex flex-col">
                                <span>Presolicitudes ({{ prerequestDeclined.length }})</span>
                                <span class="text-sm text-gray-500 font-normal mt-1">
                                    Total: {{ formatCurrency(calculateTotalMoney(prerequestDeclined)) }}
                                </span>
                            </div>
                        </h2>
                        <div class="flex flex-col space-y-3">
                            <ProcessCard v-for="proc in prerequestDeclined" :key="proc.id_Request" v-bind="proc"
                                @card="loadProcesses" />
                            <p v-if="!prerequestDeclined.length" class="text-gray-500 text-sm italic mt-4">Sin elementos
                                en esta etapa.</p>
                        </div>
                    </section>

                    <section class="bg-gray-50 p-3 rounded-lg h-full min-w-[34vh]">
                        <h2 class="text-xl font-bold mb-4 border-b pb-2 text-indigo-500 whitespace-nowrap">
                            <div class="flex flex-col">
                                <span>Solicitud ({{ request.length }})</span>
                                <span class="text-sm text-gray-500 font-normal mt-1">
                                    Total: {{ formatCurrency(calculateTotalMoney(request)) }}
                                </span>
                            </div>
                        </h2>
                        <div class="flex flex-col space-y-3">
                            <ProcessCard v-for="proc in request" :key="proc.id_Request" v-bind="proc"
                                @card="loadProcesses" />
                            <p v-if="!request.length" class="text-gray-500 text-sm italic mt-4">Sin elementos en esta
                                etapa.</p>
                        </div>
                    </section>

                    <section class="bg-gray-50 p-3 rounded-lg h-full min-w-[34vh]">
                        <h2 class="text-xl font-bold mb-4 border-b pb-2 text-indigo-700 whitespace-nowrap">
                            <div class="flex flex-col">
                                <span>Autorizadas ({{ authorized.length }})</span>
                                <span class="text-sm text-gray-500 font-normal mt-1">
                                    Total: {{ formatCurrency(calculateTotalMoney(authorized)) }}
                                </span>
                            </div>
                        </h2>

                        <div class="flex flex-col space-y-3">
                            <ProcessCard v-for="proc in authorized" :key="proc.id_Request" v-bind="proc" />
                            <p v-if="!authorized.length" class="text-gray-500 text-sm italic mt-4">Sin elementos en esta
                                etapa.</p>
                        </div>
                    </section>

                    <section class="bg-gray-50 p-3 rounded-lg h-full min-w-[34vh]">
                        <h2 class="text-xl font-bold mb-4 border-b pb-2 text-green-600 whitespace-nowrap">
                            <div class="flex flex-col">
                                <span>Entregadas ({{ supply.length }})</span>
                                <span class="text-sm text-gray-500 font-normal mt-1">
                                    Total: {{ formatCurrency(calculateTotalMoney(supply)) }}
                                </span>
                            </div>
                        </h2>

                        <div class="flex flex-col space-y-3">
                            <ProcessCard v-for="proc in supply" :key="proc.id_Request" v-bind="proc" />
                            <p v-if="!supply.length" class="text-gray-500 text-sm italic mt-4">Sin elementos en esta
                                etapa.</p>
                        </div>
                    </section>

                    <section class="bg-gray-50 p-3 rounded-lg h-full min-w-[34vh]">
                        <h2 class="text-xl font-bold mb-4 border-b pb-2 text-gray-500 whitespace-nowrap">
                            <div class="flex flex-col">
                                <span>Archivada ({{ archived.length }})</span>
                                <span class="text-sm text-gray-500 font-normal mt-1">
                                    Total: {{ formatCurrency(calculateTotalMoney(archived)) }}
                                </span>
                            </div>
                        </h2>

                        <div class="flex flex-col space-y-3">
                            <ProcessCard v-for="proc in archived" :key="proc.id_Request" v-bind="proc" />
                            <p v-if="!archived.length" class="text-gray-500 text-sm italic mt-4">Sin elementos en esta
                                etapa.</p>
                        </div>
                    </section>
                </div>
            </CardContent>
        </Card>
    </div>
</template>