<script setup lang="ts">
interface Users { id_user: string; name: string };

const props = defineProps<{
    requestactions?: {
        id_RequestActions: number;
        action: 'authorized' | 'declined';
        comment: string;
        requestactions_datetime: string;
        user: Users;
        date?: string;
        time?: string;
    } | null;
}>();
</script>

<template>
    <template v-if="props.requestactions?.action === 'authorized'">
        <div class="space-y-2 text-sm">
            <h4 class="flex justify-center text-[24px] font-bold">Autorizado</h4>
            <div><strong>Id de Autorizado</strong>{{ props.requestactions?.id_RequestActions }}</div>
            <div><strong>Autorizado por:</strong>{{ props.requestactions?.user.id_user || '—' }} Nombre: {{
                props.requestactions?.user.name || '—' }}</div>
            <div><strong>Comemtario:</strong>{{ props.requestactions?.comment || '—' }}</div>
            <div><strong>Fecha de autorizada:</strong>Fecha: {{ props.requestactions?.date || '—' }} Hora: {{
                props.requestactions?.time }}</div>
        </div>
    </template>

    <template v-if="props.requestactions?.action === 'declined'">
        <div class="space-y-2 text-sm">
            <h4 class="flex justify-center text-[24px] font-bold">Rechazado</h4>
            <div><strong>Id de Rechazado</strong>{{ props.requestactions?.id_RequestActions }}</div>
            <div><strong>Autorizado por:</strong>{{ props.requestactions?.user.id_user || '—' }} Nombre: {{
                props.requestactions?.user.name || '—' }}</div>
            <div><strong>Comemtario:</strong>{{ props.requestactions?.comment || '—' }}</div>
            <div><strong>Fecha de rechazo:</strong>Fecha: {{ props.requestactions?.date || '—' }} Hora: {{
                props.requestactions?.time }}</div>
        </div>
    </template>
</template>