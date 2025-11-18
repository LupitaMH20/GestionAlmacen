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
        articleName?: Article;
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
            id_acceptance: number;
            user?: Users | null;
            userName?: Users;
            article?: Article | null;
            articleName?: Article;
            date?: string;
            time?: string;

            requestactions?: {
                id_RequestActions: number;
                action: 'authorized' | 'declined';
                comment: string;
                requestactions_datetime: string;
                user: Users | null;
                userName?: Users;
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
}>();
</script>

<template>
    <template v-if="props.Request.status === 'request'">
        <div class="pt-4 space-y-2 text-sm border-t">
            <h4 class="flex justify-center text-[24px] font-bold">Solicitud</h4>
            <div><strong>ID de la Solicitud:</strong> {{ props.Request.acceptance?.id_acceptance || '—' }}</div>
            <div><strong>Aprobado por:</strong>ID: {{ props.Request.acceptance?.user?.id_user || '—' }} Nombre: {{
                props.Request.acceptance?.userName?.name }}</div>
            <div><strong>Articulo:</strong> ID: {{ props.Request.acceptance?.article?.id_mainarticle || '—' }} Nombre: {{
                props.Request.acceptance?.articleName?.name }}</div>
            <div><strong>Creacion:</strong> Fecha: {{ props.Request.acceptance?.date|| '—' }} Hora: {{
                props.Request.acceptance?.time }}</div>
        </div>
    </template>
</template>