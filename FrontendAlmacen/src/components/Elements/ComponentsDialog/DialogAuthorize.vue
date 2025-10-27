<script setup lang="ts">
const props = defineProps<{
    authorization?: {
        authorize?: string;
        comment?: string;
        authorized_datetime?: string;
      };
}>();
</script>

<template>
    <div class="flex justify-center text-[24px] font-bold">Autorizado</div>
    <div><strong>Autorizado por:</strong>{{ props.authorization?.authorize || '—' }}</div>
    <div><strong>Comemtario:</strong>{{ props.authorization?.comment || '—' }}</div>
    <div><strong>Fecha de autorizada:</strong>{{ props.authorization?.authorized_datetime || '—' }}</div>
</template>