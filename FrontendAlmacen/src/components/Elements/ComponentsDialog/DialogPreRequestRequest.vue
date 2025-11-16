<script setup lang="ts">
interface Companies { id_Company: string; name: string };
interface Users { id_user: string; name: string };
interface Collaborators { id_Collaborator: string; name: string; last_name: string };
interface Article { id_mainarticle: string; name: string }

const props = defineProps<{
    Request: {
        id_Request: string | number;
        user?: Users | null;
        userName?: Users;
        collaborator?: string;
        collaboratorName?: Collaborators;
        type?: string;
        article?: string;
        description?: string;
        amount?: number;
        status?: string;
        order_workshop?: string;
        store?: string;
        requestingCompany?: string;
        supplierCompany?: string;
        requestingCompanyName?: Companies;
        supplierCompanyName?: Companies;
        date?: string;
        time?: string;

        acceptance?: {
            id_acceptance?: string | number;
            user?: string;
            userName?: Users;
            article?: string;
            articleName?: Article;
            date?: string;
            time?: string;
        } | null
    }
}>();

const formatStatus = (status: string) => {
    const lower = status.toLowerCase();
    if (lower.includes('prerequest')) return 'PreSolicitud';
    if (lower.includes('request')) return 'Solicitud';
    if (lower.includes('authorization')) return 'Atorizar';
    if (lower.includes('decline')) return 'Rechazar';
    if (lower.includes('deliverie')) return 'Surtir';
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
        <div><strong>ID de la PreSolicitud</strong> {{ props.Request.id_Request }} </div>
        <div><strong>Solicitante:</strong> ID: {{ props.Request.user || '—' }} Nombre: {{
            props.Request.userName?.name || '—' }} </div>
        <div v-if="props.Request.collaborator"><strong>Colaborador:</strong> ID: {{ props.Request.collaborator ||
            '—' }} Nombre: {{ props.Request.collaboratorName?.name || '—' }} {{
                props.Request.collaboratorName?.last_name || '' }} </div>
        <div><strong>Tipo:</strong> {{ formatType(props.Request.type || '') || '—' }}</div>
        <div><strong>Artículo:</strong> {{ props.Request.article || '—' }}</div>
        <div><strong>Descripción:</strong> {{ props.Request.description || '—' }}</div>
        <div><strong>Cantidad:</strong> {{ props.Request.amount || '—' }}</div>
        <div><strong>Estatus:</strong> {{ formatStatus(props.Request.status || '') || '—' }}</div>
        <div v-if="props.Request.order_workshop"><strong>Orden/Taller:</strong> {{ props.Request.order_workshop ||
            '—' }}</div>
        <div v-if="props.Request.store"><strong>Almacén:</strong> {{ formatStore(props.Request.store || '') || '—'
        }}</div>
        <div v-if="props.Request.requestingCompany"><strong>Empresa Solicitante: </strong>ID: {{
            props.Request.requestingCompany || '—' }} Empresa: {{
                props.Request.requestingCompanyName?.name || '—' }}</div>
        <div v-if="props.Request.supplierCompany"><strong>Empresa Proveedora: </strong>ID: {{
            props.Request.supplierCompany || '—' }} Empresa: {{
                props.Request.supplierCompanyName?.name || '—' }}</div>
        <div v-if="props.Request.date"><strong>Creación: </strong>Fecha: {{ props.Request.date || '—' }} Hora: {{
            props.Request.time || '—' }}</div>
    </div>

    <template v-if="props.Request.acceptance">
        <div class="pt-4 space-y-2 text-sm border-t">
            <h4 class="flex justify-center text-[24px] font-bold">Solicitud</h4>
            <div><strong>ID de la Solicitud:</strong> {{ props.Request.acceptance.id_acceptance || '—' }}</div>
            <div><strong>Aprobado por:</strong>ID: {{ props.Request.acceptance.user || '—' }} Nombre: {{
                props.Request.acceptance.userName?.name }}</div>
            <div><strong>Articulo:</strong> ID: {{ props.Request.acceptance.article || '—' }} Nombre: {{
                props.Request.acceptance.articleName?.id_mainarticle }}</div>
            <div><strong>Creacion:</strong> Fecha: {{ props.Request.acceptance.date || '—' }} Hora: {{
                props.Request.acceptance.time }}</div>
        </div>
    </template>
</template>