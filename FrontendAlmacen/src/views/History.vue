<script setup lang="ts">
import { ref, computed, onMounted, inject, Ref } from 'vue';
import axios from 'axios';
import { Card, CardContent } from '../components/ui/card';
import { Search, FileText } from 'lucide-vue-next';
import { Input } from '../components/ui/input';

// --- 1. INTERFACES ---
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
    date: string;
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

// --- 2. ESTADO Y USUARIO ---
const allProcesses = ref<ProcessData[]>([]);
const loading = ref(false);
const loggedInUser = inject<Ref<LoggedInUserType | null>>('loggedInUser');

// Filtros
const filterStatus = ref('archived'); // Default: Archivadas
const filterType = ref('All');
const filterCompany = ref('All');
const searchQuery = ref('');

// --- 3. FORMATO DE DINERO ---
const formatCurrency = (value: number) => {
    return new Intl.NumberFormat('es-MX', { style: 'currency', currency: 'MXN', minimumFractionDigits: 2 }).format(value);
};

// --- 4. LISTA DE EMPRESAS ÚNICAS ---
const uniqueCompanies = computed(() => {
    const companies = new Map();
    allProcesses.value.forEach(p => {
        if (p.requestingCompany && p.requestingCompanyName) {
            companies.set(p.requestingCompany, p.requestingCompanyName.name);
        }
    });
    return Array.from(companies, ([id, name]) => ({ id, name }));
});

// --- 5. FILTRADO PRINCIPAL (SEGURIDAD + FILTROS) ---
const filteredProcesses = computed(() => {
    // A. SEGURIDAD: Si no hay usuario o no es Contador/Director/Admin, tabla vacía.
    if (!loggedInUser?.value) return [];
    
    const position = loggedInUser.value.position.toLowerCase();
    const rolesPermitidos = ['counter', 'director']; // Ajusta a tus nombres de roles exactos
    
    if (!rolesPermitidos.includes(position) && !loggedInUser.value.admin) {
        return []; 
    }

    // B. FILTROS DE LA INTERFAZ
    return allProcesses.value.filter(item => {
        // 1. Etapa
        const matchStatus = filterStatus.value === 'All' || item.currentStatus === filterStatus.value;
        // 2. Tipo
        const matchType = filterType.value === 'All' || item.type === filterType.value;
        // 3. Empresa
        const matchCompany = filterCompany.value === 'All' || item.requestingCompany == filterCompany.value;
        // 4. Buscador
        const query = searchQuery.value.toLowerCase();
        const matchSearch = !query || 
            item.title.toLowerCase().includes(query) ||
            item.article.toLowerCase().includes(query) ||
            item.id_Request.toString().includes(query) ||
            (item.userName?.name + ' ' + item.userName?.last_name).toLowerCase().includes(query);

        return matchStatus && matchType && matchCompany && matchSearch;
    });
});

// --- 6. TOTALES ---
const totalFilteredMoney = computed(() => {
    return filteredProcesses.value.reduce((sum, item) => sum + (item.totalValue || 0), 0);
});

// --- 7. CARGA DE DATOS ---
const loadProcesses = async () => {
    loading.value = true;
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/request/');

        const typeMap: Record<string, string> = {
            "Consumable": 'Consumibles',
            "Tool": 'Herramientas',
            "PersonalConsumption": 'Consumo Personal',
        };
        
        const statusMap: Record<string, string> = {
            'prerequest': 'Pre-Solicitud',
            'request': 'Solicitud',
            'authorized': 'Autorizada',
            'declined': 'Rechazada',
            'supply': 'Surtida',
            'finished': 'Terminada',
            'archived': 'Archivada',
            'returnExchange': 'Devolución'
        };

        allProcesses.value = response.data.map((item: any) => {
            const unitPrice = Number(item.article_price) || 0;
            const amount = Number(item.amount) || 0;
            
            // Formato de fecha simple para tabla
            const dateObj = new Date(item.request_datetime);
            const dateStr = dateObj.toLocaleDateString('es-MX');
            const timeStr = dateObj.toLocaleTimeString('es-MX', { hour: '2-digit', minute: '2-digit' });

            return {
                id_Request: item.id_Request,
                title: typeMap[item.type] || item.type,
                type: item.type,
                article: item.article,
                // Asegúrate de que tu backend envíe article_obj o article_name
                articleName: item.article_obj || { name: item.article_name || '---' },
                
                currentStatus: item.status,
                statusLabel: statusMap[item.status] || item.status,

                date: dateStr,
                time: timeStr,
                
                amount: amount,
                unitPrice: unitPrice,
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
        console.error("Error cargando historial", error);
    } finally {
        loading.value = false;
    }
};

onMounted(() => {
    loadProcesses();
});
</script>

<template>
    <div class="p-6 space-y-6">
        
        <div class="flex items-center gap-2 mb-4">
            <FileText class="w-8 h-8 text-blue-600"/> 
            <div>
                <h1 class="text-3xl font-bold text-gray-800">Historial de Solicitudes</h1>
            </div>
        </div>

        <div class="flex flex-col lg:flex-row justify-between items-stretch w-full gap-4">
            
            <div class="bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col gap-4 min-w-[280px]">
                <div class="flex flex-col gap-1">
                    <label class="text-xs font-bold text-gray-500 uppercase">1. Etapa</label>
                    <select v-model="filterStatus" class="h-10 rounded-md border border-gray-300 px-3 text-sm focus:ring-2 focus:ring-blue-500 bg-white">
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
                    <select v-model="filterType" class="h-10 rounded-md border border-gray-300 px-3 text-sm focus:ring-2 focus:ring-blue-500 bg-white">
                        <option value="All">Todos los tipos</option>
                        <option value="Consumable">Consumibles</option>
                        <option value="Tool">Herramientas</option>
                        <option value="PersonalConsumption">Consumo Personal</option>
                    </select>
                </div>

                <div class="flex flex-col gap-1">
                    <label class="text-xs font-bold text-gray-500 uppercase">3. Empresa Solicitante</label>
                    <select v-model="filterCompany" class="h-10 rounded-md border border-gray-300 px-3 text-sm focus:ring-2 focus:ring-blue-500 bg-white">
                        <option value="All">Todas las empresas</option>
                        <option v-for="comp in uniqueCompanies" :key="comp.id" :value="comp.id">
                            {{ comp.name }}
                        </option>
                    </select>
                </div>
            </div>

            <Card class="bg-green-50 border-green-200 shadow-sm min-w-[280px] flex items-center justify-center">
                <CardContent class="p-6 flex flex-col items-center w-full">
                    <span class="text-sm font-medium text-green-600 uppercase tracking-wider mb-1">Importe Total</span>
                    <span class="text-4xl font-bold text-green-700 mb-1">
                        {{ formatCurrency(totalFilteredMoney) }}
                    </span>
                    <span class="text-xs font-semibold text-green-600 bg-green-100 px-2 py-1 rounded-full">
                        {{ filteredProcesses.length }} registros encontrados
                    </span>
                </CardContent>
            </Card>
        </div>

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
                            <th class="px-4 py-3">Empresa</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="item in filteredProcesses" :key="item.id_Request" class="border-b hover:bg-gray-50 transition-colors">
                            <td class="px-4 py-3 font-medium text-gray-900">#{{ item.id_Request }}</td>
                            <td class="px-4 py-3">
                                <span class="px-2 py-1 rounded-full text-xs font-semibold inline-block min-w-[80px] text-center"
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
                                {{ item.date }} <span class="text-xs text-gray-400 block">{{ item.time }}</span>
                            </td>
                            <td class="px-4 py-3">{{ item.title }}</td>
                            <td class="px-4 py-3">
                                <div class="font-medium text-gray-900">{{ item.articleName?.name || item.article }}</div>
                                <div v-if="item.articleName" class="text-xs text-gray-400">ID: {{ item.article }}</div>
                            </td>
                            <td class="px-4 py-3 text-right font-medium">{{ item.amount }}</td>
                            <td class="px-4 py-3 text-right text-gray-500">{{ formatCurrency(item.unitPrice || 0) }}</td>
                            <td class="px-4 py-3 text-right font-bold text-green-600">{{ formatCurrency(item.totalValue || 0) }}</td>
                            <td class="px-4 py-3">
                                <div class="font-medium">{{ item.userName?.name }} {{ item.userName?.last_name }}</div>
                                <div class="text-xs text-gray-400">{{ item.collaboratorName?.name }}</div>
                            </td>
                            <td class="px-4 py-3 text-gray-500">
                                {{ item.requestingCompanyName?.name || '—' }}
                            </td>
                        </tr>
                        <tr v-if="filteredProcesses.length === 0">
                            <td colspan="10" class="px-4 py-12 text-center text-gray-500">
                                <div class="flex flex-col items-center gap-2">
                                    <Search class="w-8 h-8 text-gray-300"/>
                                    <p>No se encontraron registros con los filtros seleccionados.</p>
                                    <p v-if="!loggedInUser" class="text-xs text-red-400">Verifica que hayas iniciado sesión.</p>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>