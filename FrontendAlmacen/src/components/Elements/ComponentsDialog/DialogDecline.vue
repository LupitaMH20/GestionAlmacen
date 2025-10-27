<script setup lang="ts">
const props = defineProps<{
    decline?: {
        decline?: string;
        comment?: string;
        datetime?: string;
      };
}>();
</script>

<template>
    <h4 class="flex justify-center text-[24px] font-bold">Rechazado</h4>
    <div><strong>Rechazado por:</strong>{{ props.decline?.decline || '—' }}</div>
    <div><strong>Comemtario:</strong>{{ props.decline?.comment || '—' }}</div>
    <div><strong>Fecha de rechazo:</strong>{{ props.decline?.datetime || '—' }}</div>
</template>