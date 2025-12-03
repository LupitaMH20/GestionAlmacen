<script setup lang="ts">
import { ref, computed, onMounted, inject, Ref } from 'vue';
import axios from 'axios';
import { Card, CardContent } from '../components/ui/card';
import { Search, FileText, Download } from 'lucide-vue-next';
import { PdfService } from '../components/Forms/pdf/pdfService';
import { Input } from '../components/ui/input';
import ApexCharts from 'vue3-apexcharts';
import type { ApexOptions } from 'apexcharts';

interface Companies { id_Company: string; name: string }
interface Users { id_user: string; name: string; last_name: string };
interface Collaborators { id_Collaborator: string; name: string; last_name: string };
interface Article { id_mainarticle: string; name: string };

interface LoggedInUserType {
    id_user: string;
    name: string;
    position: string;
    admin: boolean;
}

interface ProcessData {
    id_Request: number | string;
    title: string;
    article: string;
    articleName?: { name: string };
    currentStatus: string;
    statusLabel: string;
    date: string;  // YYYY-MM-DD
    time: string;
    type: string;
    user?: any;
    userName?: Users;
    collaboratorName?: Collaborators;
    description?: string;
    amount?: number;
    unitPrice?: number;
    totalValue?: number;
    requestingCompany?: string;
    requestingCompanyName?: Companies;
    supplierCompanyName?: Companies;
}

const allProcesses = ref<ProcessData[]>([]);
const loading = ref(false);
const loggedInUser = inject<Ref<LoggedInUserType | null>>('loggedInUser');

const filterStatus = ref('archived');
const filterType = ref('All');
const filterCompany = ref('All');
const filterUser = ref('All');
const searchQuery = ref('');

// Formato dinero
const formatCurrency = (value: number) =>
    new Intl.NumberFormat('es-MX', {
        style: 'currency',
        currency: 'MXN',
        minimumFractionDigits: 2
    }).format(value);

// Empresas únicas
const uniqueCompanies = computed(() => {
    const companies = new Map<string, string>();
    allProcesses.value.forEach(p => {
        if (p.requestingCompany && p.requestingCompanyName) {
            companies.set(p.requestingCompany, p.requestingCompanyName.name);
        }
    });
    return Array.from(companies, ([id, name]) => ({ id, name }));
});

// Usuarios únicos (solicitantes)
const uniqueUsers = computed(() => {
    const users = new Map<string, string>();
    allProcesses.value.forEach(p => {
        if (p.userName) {
            const full = `${p.userName.name} ${p.userName.last_name || ''}`.trim();
            users.set(p.userName.id_user, full);
        }
    });
    return Array.from(users, ([id, name]) => ({ id, name }));
});

// Filtrado principal
const filteredProcesses = computed(() => {
    if (!loggedInUser?.value) return [];

    const position = loggedInUser.value.position.toLowerCase();
    const rolesPermitidos = ['counter', 'director'];

    if (!rolesPermitidos.includes(position) && !loggedInUser.value.admin) {
        return [];
    }

    return allProcesses.value.filter(item => {
        const matchStatus = filterStatus.value === 'All' || item.currentStatus === filterStatus.value;
        const matchType = filterType.value === 'All' || item.type === filterType.value;
        const matchCompany = filterCompany.value === 'All' || item.requestingCompany == filterCompany.value;
        const matchUser =
            filterUser.value === 'All' ||
            (item.userName && item.userName.id_user === filterUser.value);

        const query = searchQuery.value.toLowerCase();
        const fullUser = item.userName
            ? `${item.userName.name} ${item.userName.last_name || ''}`.toLowerCase()
            : '';

        const matchSearch =
            !query ||
            item.title.toLowerCase().includes(query) ||
            item.article.toLowerCase().includes(query) ||
            item.id_Request.toString().includes(query) ||
            fullUser.includes(query);

        return matchStatus && matchType && matchCompany && matchUser && matchSearch;
    });
});

// Total filtrado
const totalFilteredMoney = computed(() =>
    filteredProcesses.value.reduce((sum, item) => sum + (item.totalValue || 0), 0)
);

// Datos mensuales
const monthlyData = computed(() => {
    const months = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'];
    const dataByMonth: Record<string, number> = {};
    months.forEach(m => (dataByMonth[m] = 0));

    filteredProcesses.value.forEach(item => {
        const d = new Date(item.date); // 'YYYY-MM-DD'
        if (isNaN(d.getTime())) return;
        const idx = d.getMonth();
        const mName = months[idx] ?? 'Ene';
        dataByMonth[mName] += item.totalValue || 0;
    });

    return months.map(m => ({ month: m, total: dataByMonth[m] }));
});

// Opciones ApexCharts tipadas
const chartOptions = computed<ApexOptions>(() => ({
    chart: {
        toolbar: { show: false }
    },
    xaxis: {
        categories: monthlyData.value.map(m => m.month),
    },
    dataLabels: { enabled: false },
    stroke: {
        curve: 'smooth'  // tipo literal válido
    },
    yaxis: {
        labels: {
            formatter: (val: number) => `$${(val / 1000).toFixed(0)}k`,
        },
    },
    tooltip: {
        y: {
            formatter: (val: number) => formatCurrency(val),
        },
    },
}));

const chartSeries = computed(() => [
    {
        name: 'Importe total',
        data: monthlyData.value.map(m => m.total),
    },
]);

// Carga datos
const loadProcesses = async () => {
    loading.value = true;
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/request/');

        const typeMap: Record<string, string> = {
            Consumable: 'Consumibles',
            Tool: 'Herramientas',
            PersonalConsumption: 'Consumo Personal',
        };

        const statusMap: Record<string, string> = {
            prerequest: 'Pre-Solicitud',
            request: 'Solicitud',
            authorized: 'Autorizada',
            declined: 'Rechazada',
            supply: 'Surtida',
            finished: 'Terminada',
            archived: 'Archivada',
            returnExchange: 'Devolución',
        };

        allProcesses.value = response.data.map((item: any): ProcessData => {
            const unitPrice = Number(item.article_price) || 0;
            const amount = Number(item.amount) || 0;

            const dateObj = new Date(item.request_datetime);
            const dateStr = dateObj.toISOString().slice(0, 10); // YYYY-MM-DD
            const timeStr = dateObj.toLocaleTimeString('es-MX', { hour: '2-digit', minute: '2-digit' });

            return {
                id_Request: item.id_Request,
                title: typeMap[item.type] || item.type,
                type: item.type,
                article: item.article,
                articleName: item.article_obj || { name: item.article_name || '---' },

                currentStatus: item.status,
                statusLabel: statusMap[item.status] || item.status,

                date: dateStr,
                time: timeStr,

                amount,
                unitPrice,
                totalValue: unitPrice * amount,

                description: item.description,
                userName: item.user,
                collaboratorName: item.collaborator,
                requestingCompany: item.requestingCompany?.id_Company,
                requestingCompanyName: item.requestingCompany,
                supplierCompanyName: item.supplierCompany,
            };
        });
    } catch (error) {
        console.error('Error cargando historial', error);
    } finally {
        loading.value = false;
    }
};



const handleDownloadPdf = async (id: number | string) => {
    try {
        await PdfService.downloadQuotePdf(id);
    } catch (error) {
        alert('Error al descargar el PDF');
    }
};

const handleDownloadBulkPdf = async () => {
    if (filteredProcesses.value.length === 0) return;
    
    try {
        const ids = filteredProcesses.value.map(p => p.id_Request);
        await PdfService.downloadBulkQuotePdf(ids);
    } catch (error) {
        alert('Error al descargar el reporte masivo');
    }
};

onMounted(() => {
    loadProcesses();
});
</script>

<template>
    <div class="p-6 space-y-6">
        <div class="flex items-center gap-2 mb-4">
            <FileText class="w-8 h-8 text-blue-600" />
            <div>
                <h1 class="text-3xl font-bold text-gray-800">Reportes de Solicitudes</h1>
            </div>
            <div class="ml-auto">
                <button @click="handleDownloadBulkPdf" 
                        class="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded-md flex items-center gap-2 transition-colors"
                        :disabled="filteredProcesses.length === 0">
                    <Download class="w-4 h-4" />
                    Descargar Reporte PDF
                </button>
            </div>
        </div>

        <div class="flex flex-col lg:flex-row justify-between items-stretch w-full gap-4">
            <div class="bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col gap-4 min-w-[280px]">
                <div class="flex flex-col gap-1">
                    <label class="text-xs font-bold text-gray-500 uppercase">1. Etapa</label>
                    <select v-model="filterStatus"
                        class="h-10 rounded-md border border-gray-300 px-3 text-sm focus:ring-2 focus:ring-blue-500 bg-white">
                        <option value="All">Todas las etapas</option>
                        <option value="archived">Archivadas (Default)</option>
                        <option value="finished">Terminadas</option>
                        <option value="supply">Surtidas</option>
                        <option value="authorized">Autorizadas</option>
                        <option value="declined">Rechazadas</option>
                        <option value="request">Solicitud</option>
                        <option value="prerequest">Pre-Solicitud</option>
                    </select>
                </div>

                <div class="flex flex-col gap-1">
                    <label class="text-xs font-bold text-gray-500 uppercase">2. Tipo</label>
                    <select v-model="filterType"
                        class="h-10 rounded-md border border-gray-300 px-3 text-sm focus:ring-2 focus:ring-blue-500 bg-white">
                        <option value="All">Todos los tipos</option>
                        <option value="Consumable">Consumibles</option>
                        <option value="Tool">Herramientas</option>
                        <option value="PersonalConsumption">Consumo Personal</option>
                    </select>
                </div>

                <div class="flex flex-col gap-1">
                    <label class="text-xs font-bold text-gray-500 uppercase">3. Empresa Solicitante</label>
                    <select v-model="filterCompany"
                        class="h-10 rounded-md border border-gray-300 px-3 text-sm focus:ring-2 focus:ring-blue-500 bg-white">
                        <option value="All">Todas las empresas</option>
                        <option v-for="comp in uniqueCompanies" :key="comp.id" :value="comp.id">
                            {{ comp.name }}
                        </option>
                    </select>
                </div>

                <div class="flex flex-col gap-1">
                    <label class="text-xs font-bold text-gray-500 uppercase">4. Solicitante</label>
                    <select v-model="filterUser"
                        class="h-10 rounded-md border border-gray-300 px-3 text-sm focus:ring-2 focus:ring-blue-500 bg-white">
                        <option value="All">Todos</option>
                        <option v-for="u in uniqueUsers" :key="u.id" :value="u.id">
                            {{ u.name }}
                        </option>
                    </select>
                </div>

                <div class="flex flex-col gap-1">
                    <label class="text-xs font-bold text-gray-500 uppercase">5. Buscar</label>
                    <div class="relative">
                        <Search class="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-gray-400" />
                        <Input v-model="searchQuery" placeholder="ID, solicitante, artículo..."
                            class="pl-10 h-10 text-sm" />
                    </div>
                </div>
            </div>

            <Card class="bg-green-50 border-green-200 shadow-sm min-w-[280px] flex items-center justify-center">
                <CardContent class="p-6 flex flex-col items-center w-full">
                    <span class="text-sm font-medium text-green-600 uppercase tracking-wider mb-1">
                        Importe Total
                    </span>
                    <span class="text-4xl font-bold text-green-700 mb-1">
                        {{ formatCurrency(totalFilteredMoney) }}
                    </span>
                    <span class="text-xs font-semibold text-green-600 bg-green-100 px-2 py-1 rounded-full">
                        {{ filteredProcesses.length }} registros encontrados
                    </span>
                </CardContent>
            </Card>
        </div>

        <Card class="shadow-sm">
            <CardContent class="p-4">
                <h2 class="text-lg font-semibold mb-1">Importes por mes</h2>
                <p class="text-xs text-gray-500 mb-4">
                    Suma de importes de las solicitudes filtradas, agrupadas por mes.
                </p>
                <ApexCharts type="line" height="280" :options="chartOptions" :series="chartSeries" />
            </CardContent>
        </Card>

        <!-- Tabla (igual que antes) -->
        <div class="rounded-md border bg-white shadow-sm overflow-hidden">
            <div class="overflow-x-auto">
                <table class="w-full text-sm text-left">
                    <thead class="text-xs text-gray-700 uppercase bg-gray-100 border-b">
                        <tr>
                            <th class="px-4 py-3">ID</th>
                            <th class="px-4 py-3">Estado</th>
                            <th class="px-4 py-3">Fecha</th>
                            <th class="px-4 py-3">Tipo</th>
                            <th class="px-4 py-3">Artículo</th>
                            <th class="px-4 py-3 text-right">Cant.</th>
                            <th class="px-4 py-3 text-right">Precio U.</th>
                            <th class="px-4 py-3 text-right">Total</th>
                            <th class="px-4 py-3">Solicitante</th>
                            <th class="px-4 py-3">Solicitante</th> 
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="item in filteredProcesses" :key="item.id_Request"
                            class="border-b hover:bg-gray-50 transition-colors">
                            <td class="px-4 py-3 font-medium text-gray-900">#{{ item.id_Request }}</td>
                            <td class="px-4 py-3">
                                <span
                                    class="px-2 py-1 rounded-full text-xs font-semibold inline-block min-w-[80px] text-center"
                                    :class="{
                                        'bg-gray-200 text-gray-800': item.currentStatus === 'archived',
                                        'bg-green-100 text-green-800': item.currentStatus === 'supply' || item.currentStatus === 'finished',
                                        'bg-red-100 text-red-800': item.currentStatus === 'declined',
                                        'bg-blue-100 text-blue-800': item.currentStatus === 'request' || item.currentStatus === 'authorized',
                                        'bg-yellow-100 text-yellow-800': item.currentStatus === 'prerequest',
                                    }">
                                    {{ item.statusLabel }}
                                </span>
                            </td>
                            <td class="px-4 py-3 text-gray-500 whitespace-nowrap">
                                {{ item.date }}
                                <span class="text-xs text-gray-400 block">{{ item.time }}</span>
                            </td>
                            <td class="px-4 py-3">{{ item.title }}</td>
                            <td class="px-4 py-3">
                                <div class="font-medium text-gray-900">
                                    {{ item.articleName?.name || item.article }}
                                </div>
                                <div v-if="item.articleName" class="text-xs text-gray-400">
                                    ID: {{ item.article }}
                                </div>
                            </td>
                            <td class="px-4 py-3 text-right font-medium">{{ item.amount }}</td>
                            <td class="px-4 py-3 text-right text-gray-500">
                                {{ formatCurrency(item.unitPrice || 0) }}
                            </td>
                            <td class="px-4 py-3 text-right font-bold text-green-600">
                                {{ formatCurrency(item.totalValue || 0) }}
                            </td>
                            <td class="px-4 py-3">
                                <div class="font-medium">
                                    {{ item.userName?.name }} {{ item.userName?.last_name }}
                                </div>
                            </td>
                            <td class="px-4 py-3 text-gray-500">
                                {{ item.requestingCompanyName?.name || '—' }}
                            </td>
                        </tr>

                        <tr v-if="filteredProcesses.length === 0">
                            <td colspan="10" class="px-4 py-12 text-center text-gray-500">
                                <div class="flex flex-col items-center gap-2">
                                    <Search class="w-8 h-8 text-gray-300" />
                                    <p>No se encontraron registros con los filtros seleccionados.</p>
                                    <p v-if="!loggedInUser" class="text-xs text-red-400">
                                        Verifica que hayas iniciado sesión.
                                    </p>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>