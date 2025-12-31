<script setup lang="ts">
import { ref, computed, inject, Ref } from 'vue';
import { Card, CardContent, CardHeader, CardTitle, CardFooter } from '../ui/card';
import Dialog from './Dialog.vue';
import { Eye, FileText } from 'lucide-vue-next';
import axios from 'axios';

interface Companies { id_Company: string; name: string };
interface Users { id_user: string; name: string; last_name: string };
interface Collaborators { id_Collaborator: string; name: string; last_name: string };
interface Article { id_mainarticle: string; name: string };

interface LoggedInUserType {
    id_user: string;
    name: string;
    position: string;
    admin: boolean;
}

const process = defineProps<{
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
                payment_status?: string;
                date?: string;
                time?: string;
            } | null
        } | null;
    } | null;
}>();

const isDialogOpen = ref(false)
const emit = defineEmits(['card', 'update-request']);

const loggedInUser = inject<Ref<LoggedInUserType | null>>('loggedInUser');

const paymentStatus = ref(process.acceptance?.requestactions?.supply?.payment_status || 'unpaid');

const canPerformActions = computed(() => {
    if (!loggedInUser?.value) return false;
    const position = loggedInUser.value.position.toLowerCase();
    // 'applicant' and 'deliberystaff' cannot perform these actions
    return position !== 'applicant' && position !== 'deliberystaff';
});

const displayDateInfo = computed(() => {
    if ((process.currentStatus === 'supply') &&
        process.acceptance?.requestactions?.supply?.date) {
        return {
            label: 'Surtido',
            date: process.acceptance.requestactions.supply.date,
            time: process.acceptance.requestactions.supply.time
        };
    }
    if ((process.currentStatus === 'authorized' || process.currentStatus === 'declined') &&
        process.acceptance?.requestactions?.date) {
        return {
            label: process.currentStatus === 'authorized' ? 'Autorización' : 'Rechazo',
            date: process.acceptance.requestactions.date,
            time: process.acceptance.requestactions.time
        };
    }
    if (process.currentStatus === 'request' && process.acceptance?.date) {
        return {
            label: 'Solicitud',
            date: process.acceptance.date,
            time: process.acceptance.time
        };
    }
    return {
        label: 'Creación',
        date: process.date,
        time: process.time
    };
});

const formatCurrency = (value: number) => {
    return new Intl.NumberFormat('es-MX', {
        style: 'currency',
        currency: 'MXN',
        minimumFractionDigits: 2
    }).format(value);
};

const showPaymentStatus = computed(() => {
    return (process.type === 'PersonalConsumption') && process.currentStatus === 'supply';
});

const updatePaymentStatus = async (newStatus: string) => {
    try {
        const token = sessionStorage.getItem('token');
        if (!token) {
            alert('Sesión expirada. Por favor, inicie sesión nuevamente.');
            return;
        }

        const supplyId = process.acceptance?.requestactions?.supply?.id_supply;
        if (!supplyId) {
            alert('Error: No se encontró el ID del suministro.');
            return;
        }

        const config = {
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        };

        await axios.patch(`http://127.0.0.1:8000/api/supply/${supplyId}/`, {
            payment_status: newStatus
        }, config);

        paymentStatus.value = newStatus;
        alert(`Estado de pago actualizado a: ${newStatus === 'paid' ? 'Pagado' : 'No Pagado'}`);
        emit('update-request');
    } catch (error) {
        console.error('Error al actualizar estado de pago:', error);
        alert('Error al actualizar el estado de pago.');
    }
};

const archiveRequest = async () => {
    if (!confirm('¿Estás seguro de que deseas archivar esta solicitud manualmente?')) return;

    try {
        const token = sessionStorage.getItem('token');
        if (!token) {
            alert('Sesión expirada. Por favor, inicie sesión nuevamente.');
            return;
        }

        const config = {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        };

        await axios.post(`http://127.0.0.1:8000/api/request/${process.id_Request}/archive/`, {}, config);

        alert('Solicitud archivada exitosamente.');
        emit('update-request');
    } catch (error) {
        console.error('Error al archivar solicitud:', error);
        alert('Error al archivar la solicitud, falta el pago.');
    }
};
</script>

<template>
    <Card class="flex flex-col h-full w-full shadow-lg hover:shadow-xl transition-shadow duration-300">
        <CardHeader>
            <CardTitle class="text-lg font-semibold">{{ process.title }} (ID: {{ process.id_Request }})</CardTitle>
            <p class="text-sm">Producto: {{ process.article }}</p>

            <p v-if="process.totalValue && process.totalValue > 0" class="text-sm font-bold text-green-600">
                Total: {{ formatCurrency(process.totalValue) }}
            </p>

            <div v-if="process.currentStatus === 'declined'" class="flex justify-end text-center">
                <span class="font-bold text-red-600 bg-red-100 px-3 py-1 rounded-full text-xs uppercase">
                    Rechazada
                </span>
            </div>

            <!-- Payment Status Badge and Select for PersonalConsumption -->
            <div v-if="showPaymentStatus" class="mt-2 flex items-center gap-2">
                <span v-if="paymentStatus === 'unpaid'"
                    class="font-bold text-red-600 bg-red-100 px-3 py-1 rounded-full text-xs uppercase">
                    No Pagada
                </span>
                <span v-else class="font-bold text-green-600 bg-green-100 px-3 py-1 rounded-full text-xs uppercase">
                    Pagada
                </span>
                <select v-model="paymentStatus" @change="updatePaymentStatus(paymentStatus)"
                    :disabled="!canPerformActions"
                    class="ml-2 px-2 py-1 text-xs border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500">
                    <option value="unpaid">No Pagada</option>
                    <option value="paid">Pagada</option>
                </select>
            </div>
        </CardHeader>

        <CardContent class="flex flex-col space-y-3 flex-grow">
            <div class="border-t pt-2">
                <p class="text-sm text-gray-500">{{ displayDateInfo.label }}</p>
                <p class="text-sm text-gray-500">Fecha: {{ displayDateInfo.date }}</p>
                <p class="text-sm text-gray-500">Hora: {{ displayDateInfo.time }}</p>
            </div>
        </CardContent>

        <CardFooter class="flex justify-end gap-2">
            <button v-if="canPerformActions && process.currentStatus === 'supply'" @click="archiveRequest"
                class="px-3 py-2 bg-yellow-500 text-white rounded hover:bg-yellow-600 transition-colors text-sm font-semibold shadow-sm">
                Archivar
            </button>
            <Dialog v-model="isDialogOpen" :title="`Detalles de ${process.title}`" titleButton="Detalles" :iconP="Eye"
                :iconT="FileText" :Request="process" @dialog="emit('update-request')" />
        </CardFooter>
    </Card>
</template>