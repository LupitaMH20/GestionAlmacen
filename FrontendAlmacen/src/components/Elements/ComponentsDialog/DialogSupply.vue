<!-- <script setup lang="ts">
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
    <h4 class="flex justify-center text-[24px] font-bold">Surtir</h4>
    <div><strong>Persona que entrega:</strong>{{ props.deliverie?.persondelivery || '—' }}</div>
    <div><strong>Persona que recibe:</strong>{{ props.deliverie?.personreceives || '—' }}</div>
    <div><strong>Empresa que entrega:</strong>{{ props.deliverie?.companydelivery || '—' }}</div>
    <div><strong>Empresa que recibe:</strong>{{ props.deliverie?.companyreceives || '—' }}</div>
    <div><strong>Comentario:</strong>{{ props.deliverie?.comment || '—' }}</div>
    <div v-if="props.deliverie?.photo"><strong>Foto:</strong>{{ props.deliverie.photo || '—' }}</div>
    <div v-if="props.deliverie?.document"><strong>Documento:</strong>{{ props.deliverie.document || '—' }}</div>
    <div><strong>Fecha que se surtio:</strong>{{ props.deliverie?.deliverie_datetime || '—' }}</div>
</template> -->