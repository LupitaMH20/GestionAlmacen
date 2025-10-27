<script setup lang="ts">
const props = defineProps<{
    deliverie?: {
        persondelivery?: string;
        personreceives?: string;
        companydelivery?: string;
        companyreceives?: string;
        comment?: string;
        photo?: string;
        document?: string;
        deliverie_datetime?: string;
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
</template>