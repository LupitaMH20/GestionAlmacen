<script setup lang="ts">
interface Companies { id_Company: string; name: string };
interface Users { id_user: string; name: string };
interface Collaborators { id_Collaborator: string; name: string; last_name: string };
interface Article { id_mainarticle: string; name: string }

const props = defineProps<{
    Request: {
        id_Request: number | string;
        title: string;
        article?: string;
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
}>();

const formatStatus = (status: string) => {
    const lower = status.toLowerCase();
    if (lower.includes('prerequest')) return 'PreSolicitud';
    if (lower.includes('request')) return 'Solicitud';
    if (lower.includes('authorized')) return 'Autorizar';
    if (lower.includes('decline')) return 'Rechazar';
    if (lower.includes('supply')) return 'Surtir';
    if (lower.includes('return_exchange')) return 'Devoluciones o Cambios';
    return status;
};

const formatStore = (store: string) => {
    const lower = store.toLowerCase();
    if (lower.includes('handtoolstorage')) return 'Almacén de herramienta manual';
    if (lower.includes('powertoolstorage')) return 'Almacén de herramienta eléctrica';
    if (lower.includes('ppestorage')) return 'Almacén de EPP, (Equipo de protección personal)';
    return store;
};

const formatType = (type: string) => {
    if (!type) return '';
    const lower = type.toLowerCase();
    if (lower.includes('consumable')) return 'Consumibles';
    if (lower.includes('tool')) return 'Herramienta';
    if (lower.includes('personalconsumption')) return 'Consumo Personal';
    return type;
};
</script>

<template>
    <div class="space-y-2 text-sm">
        <h4 class="flex justify-center text-[24px] font-bold">PreSolicitud</h4>
        <div><strong>Solicito:</strong> {{ props.Request.userName?.name || '—' }} </div>
        <div v-if="props.Request.collaborator"><strong>Colaborador:</strong> {{ props.Request.collaboratorName?.name ||
            '—' }} {{
                props.Request.collaboratorName?.last_name || '' }} </div>
        <div><strong>Tipo:</strong> {{ formatType(props.Request.type || '') || '—' }}</div>
        <div><strong>Articulo:</strong> ID: {{ props.Request.article || '—' }}
            Nombre: {{ props.Request.articleName?.name || props.Request?.articleName?.name || '—' }}
        </div>
        <div><strong>Descripción:</strong> {{ props.Request.description || '—' }}</div>
        <div><strong>Cantidad:</strong> {{ props.Request.amount || '—' }}</div>
        <div><strong>Estatus:</strong> {{ formatStatus(props.Request.status || '') || '—' }}</div>
        <div v-if="props.Request.order_workshop"><strong>Orden/Taller:</strong> {{ props.Request.order_workshop || '—'
        }}</div>
        <div v-if="props.Request.store"><strong>Almacén:</strong> {{ formatStore(props.Request.store || '') || '—' }}
        </div>
        <div v-if="props.Request.requestingCompany"><strong>Empresa Solicitante: </strong> {{
            props.Request.requestingCompanyName?.name || '—' }}</div>
        <div v-if="props.Request.supplierCompany"><strong>Empresa Proveedora: </strong>{{
            props.Request.supplierCompanyName?.name || '—' }}</div>
        <div v-if="props.Request.date"><strong>Creación: </strong>Fecha: {{ props.Request.date || '—' }} Hora: {{
            props.Request.time || '—' }}</div>
    </div>
</template>