<script setup lang="ts">
interface Users { id_user: string; name: string };
interface Article { id_mainarticle: string; name: string }

const props = defineProps<{
    acceptance?: {
        id_acceptance: number;
        user?: string;
        userName?: Users;
        article?: string;
        articleName?: Article;
        date?: string;
        time?: string;
    };
}>();
</script>

<template v-if="props.acceptance">
    <div class="pt-4 space-y-2 text-sm border-t">
        <h4 class="flex justify-center text-[24px] font-bold">Solicitud</h4>
        <div><strong>Aprobado por:</strong> {{ props.acceptance?.userName?.name }}</div>
        <div><strong>Articulo:</strong> ID: {{ props.acceptance?.articleName?.id_mainarticle || '—' }} Nombre: {{
            props.acceptance?.articleName?.name }}</div>
        <div><strong>Creacion:</strong> Fecha: {{ props.acceptance?.date || '—' }} Hora: {{ props.acceptance?.time }}
        </div>
    </div>
</template>