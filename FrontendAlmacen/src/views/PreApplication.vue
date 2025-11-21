<script setup lang="ts">
import ProcessCard from '../components/Elements/Card.vue';
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';
import { Card, CardHeader, CardTitle, CardContent } from '../components/ui/card';

interface Companies { id_Company: string; name: string };
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
}
const processes = ref<ProcessData[]>([]);

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

        processes.value = response.data.map((item: any) => {
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
    } catch (error) {
        console.error('Error al cargar procesos:', error);
    }
};

const filterByTypeAndStatus = (type: ProcessData['type']) =>
    processes.value.filter(p => (p.currentStatus === 'prerequest' || p.currentStatus === 'declined') && p.type === type);

const Consumable = computed(() => filterByTypeAndStatus('Consumable'));
const Tool = computed(() => filterByTypeAndStatus('Tool'));
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
                            <span class="text-sm text-gray-500 font-normal mt-1">
                                Total: {{ formatCurrency(calculateTotalMoney(Consumable)) }}
                            </span>
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
                            Herramienta ({{ Tool.length }})
                            <span class="text-sm text-gray-500 font-normal mt-1">
                                Total: {{ formatCurrency(calculateTotalMoney(Tool)) }}
                            </span>
                        </h2>
                        <div class="flex flex-col space-y-3">
                            <ProcessCard v-for="proc in Tool" :key="proc.id_Request" v-bind="proc"
                                @updateRequest="loadProcesses" />
                            <p v-if="!Tool.length" class="text-gray-500 text-sm italic mt-4">
                                No hay solicitudes de Herramienta.
                            </p>
                        </div>
                    </section>

                    <section class="bg-gray-50 overflow-y-auto p-3 rounded-lg min-h-[500px]">
                        <h2 class="text-xl font-bold mb-4 border-b pb-2 text-purple-700">
                            ConsumoPersonal ({{ PersonalConsumption.length }})
                            <span class="text-sm text-gray-500 font-normal mt-1">
                                Total: {{ formatCurrency(calculateTotalMoney(PersonalConsumption)) }}
                            </span>
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