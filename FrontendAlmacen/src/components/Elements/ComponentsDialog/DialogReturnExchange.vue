<script setup lang="ts">
const props = defineProps<{
    return_exchange?: {
        returnenby?: string;
        receivedby?: string;
        deliverycompany?: string;
        receivingcompany?: string;
        reason?: string;
        type?: string;
        return_datetime?: string;
    };
}>();
</script>

<template>
    <h4 class="flex justify-center text-[24px] font-bold">Cambios o Devoluciones</h4>
    <div><strong>Persona que devolvio:</strong>{{ props.return_exchange?.returnenby || '—' }}</div>
    <div><strong>Persona que recibe:</strong>{{ props.return_exchange?.receivedby || '—' }}</div>
    <div><strong>Empresa que devolvio:</strong>{{ props.return_exchange?.deliverycompany || '—' }}</div>
    <div><strong>Empresa que recibe:</strong>{{ props.return_exchange?.receivingcompany || '—' }}</div>
    <div><strong>Razón:</strong>{{ props.return_exchange?.reason || '—' }}</div>
    <div><strong>Tipo:</strong>{{ props.return_exchange?.type || '—' }}</div>
    <div><strong>Fecha que se surtio:</strong>{{ props.return_exchange?.return_datetime || '—' }}</div>
</template>