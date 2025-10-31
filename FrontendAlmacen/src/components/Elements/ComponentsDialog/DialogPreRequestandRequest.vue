<script setup lang="ts">
interface Companies { id_Company: string; name: string };
interface Users { id_user: string; name: string};
interface Collaborators { id_Collaborator: string; name: string; last_name: string };

const props = defineProps<{
    preRequest: {
        id_PreRequest: string | number;
        applicant?: string;
        applicantName?: Users;
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

        request?: {
            id_Request?: string | number;
            position?: string;
            request_datetime?: string;
        }
    }
}>();

const formatType = (type: string) => {
    const lower = type.toLowerCase();
    if (lower.includes('prerequest')) return 'PreSolicitud';
    if (lower.includes('request')) return 'Solicitud';
    if (lower.includes('authorization')) return 'Atorizar';
    if (lower.includes('decline')) return 'Rechazar';
    if (lower.includes('deliverie')) return 'Surtir';
    if (lower.includes('return_exchange')) return 'Devoluciones o Cambios';
    return type;
};

const formatStore = (store: string) => {
    const lower = store.toLowerCase();
    if (lower.includes('handtoolstorage')) return 'Almacén de herramienta manual';
    if (lower.includes('powertoolstorage')) return 'Almacén de herramienta eléctrica';
    if (lower.includes('ppestorage')) return 'Almacén de EPP, (Equipo de protección personal)';
};
</script>

<template>
    <div class="space-y-2 text-sm">
        <h4 class="flex justify-center text-[24px] font-bold">PreSolicitud</h4>
        <div><strong>ID de la PreSolicitud</strong> {{ props.preRequest.id_PreRequest }} </div>
        <div><strong>Solicitante:</strong> ID: {{ props.preRequest.applicant || '—' }} Nombre: {{ props.preRequest.applicantName?.name || '—' }} </div>
        <div v-if="props.preRequest.collaborator"><strong>Colaborador:</strong> ID: {{ props.preRequest.collaborator || '—' }} Nombre: {{ props.preRequest.collaboratorName?.name || '—' }} {{ props.preRequest.collaboratorName?.last_name || '' }} </div>
        <div><strong>Tipo:</strong> {{ props.preRequest.type || '—' }}</div>
        <div><strong>Artículo:</strong> {{ props.preRequest.article || '—' }}</div>
        <div><strong>Descripción:</strong> {{ props.preRequest.description || '—' }}</div>
        <div><strong>Cantidad:</strong> {{ props.preRequest.amount || '—' }}</div>
        <div><strong>Estatus:</strong> {{ formatType(props.preRequest.status || '') || '—' }}</div>
        <div v-if="props.preRequest.order_workshop"><strong>Orden/Taller:</strong> {{ props.preRequest.order_workshop ||
            '—' }}</div>
        <div v-if="props.preRequest.store"><strong>Almacén:</strong> {{ formatStore(props.preRequest.store || '') || '—'
        }}</div>
        <div v-if="props.preRequest.requestingCompany"><strong>Empresa Solicitante: </strong>ID: {{
            props.preRequest.requestingCompany || '—' }} Empresa: {{
                props.preRequest.requestingCompanyName?.name || '—' }}</div>
        <div v-if="props.preRequest.supplierCompany"><strong>Empresa Proveedora: </strong>ID: {{
            props.preRequest.supplierCompany || '—' }} Empresa: {{
                props.preRequest.supplierCompanyName?.name || '—' }}</div>
        <div v-if="props.preRequest.date"><strong>Creación: </strong>Fecha: {{ props.preRequest.date || '—' }} Hora: {{
            props.preRequest.time || '—' }}</div>
    </div>

    <template v-if="props.preRequest.request">
        <div class="pt-4 space-y-2 text-sm border-t">
            <h4 class="flex justify-center text-[24px] font-bold">Solicitud</h4>
            <div><strong>ID de la Solicitud:</strong> {{ props.preRequest.request.id_Request || '—' }}</div>
            <div><strong>Cargo:</strong> {{ props.preRequest.request.position || '—' }}</div>
            <div><strong>Fecha de Solicitud:</strong> {{ props.preRequest.request.request_datetime || '—' }}</div>
        </div>
    </template>
</template>