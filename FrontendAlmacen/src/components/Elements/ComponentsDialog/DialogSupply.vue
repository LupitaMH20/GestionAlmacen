<script setup lang="ts">
interface Users { id_user: string; name: string };
interface Collaborators { id_Collaborator: string; name: string; last_name: string };

const props = defineProps<{
    supply?: {
        id_supply: number;
        user?: Users;
        userName?: Users;
        collaborator?: string;
        collaboratorName?: Collaborators;
        comment?: string;
        date?: string;
        time?: string;
    } | null;
}>();
</script>

<template>
    <div v-if="props.supply" class="pt-4 space-y-2 text-sm border-t">
        <h4 class="flex justify-center text-[24px] font-bold">Surtido</h4>
        <div><strong>Persona que entrego:</strong> {{ props.supply.userName?.name || props.supply.userName?.name || '—' }} </div>
        <div><strong>Persona que recibe:</strong> {{ props.supply.collaboratorName?.name || '—' }} {{ props.supply.collaboratorName?.last_name || '' }} </div>
        <div><strong>Comentario:</strong> {{ props.supply.comment || '—' }}</div>
        <div><strong>Fecha de surtido:</strong> 
            Fecha: {{ props.supply.date || '—' }} 
            Hora: {{ props.supply.time || '—' }}
        </div>
    </div>
</template>