<script setup lang="ts">
interface Users { id_user: string; name: string };

const props = defineProps<{
    requestactions?: {
        id_RequestActions: number;
        action: 'authorized' | 'declined';
        comment: string;
        requestactions_datetime: string;
        user: Users | null;
        date?: string;
        time?: string;
    } | null;
}>();
</script>

<template>
    <div class="pt-4 space-y-2 text-sm border-t ">
        <h4 class="flex justify-center text-[24px] font-bold">Autorizado</h4>
        <div><strong>Autorizado por: </strong> {{ props.requestactions?.user?.name || '—' }}</div>
        <div><strong>Comemtario: </strong>{{ props.requestactions?.comment || '—' }}</div>
        <div><strong>Fecha de autorizada: </strong>Fecha: {{ props.requestactions?.date || '—' }} Hora: {{
            props.requestactions?.time }}</div>
    </div>
</template>