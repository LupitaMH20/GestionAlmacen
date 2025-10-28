<script setup lang="ts">
// rutas para editar y eliminar la presolicitud de Consumables
import UpdatePreRequestC from '../../Forms/Applications/Consumables/PreRequest/UpdatePreRequest.vue'
import DeletePreRequestC from '../../Forms/Applications/Consumables/PreRequest/DeletePreRequest.vue'

// rutas para editar y eliminar la presolicitud de PersonalConsumption
import UpdatePreRequestPC from '../../Forms/Applications/PersonalConsumption/PreRequest/UpdatePreRequest.vue'
import DeletePreRequestPC from '../../Forms/Applications/PersonalConsumption/PreRequest/DeletePreRequest.vue'

//rutas para editar y eliminar la presolicitud de Tools
import UpdatePreRequestT from '../../Forms/Applications/Tools/PreRequest/UpdatePreRequest.vue'
import DeletePreRequestT from '../../Forms/Applications/Tools/PreRequest/DeletePreRequest.vue'

const props = defineProps<{
    preRequest: {
        id_PreRequest: string | number;
        type?: string;
        status?: string;
    }
}>();

const emit = defineEmits(['updatePreRequest'])
</script>
<template>
    <!-- Para editar o eliminar la prerequest -->
    <div v-if="props.preRequest?.status === 'prerequest'">
        <div v-if="props.preRequest.type === 'Consumible'" class="flex justify-end gap-2">
            <UpdatePreRequestC :preRequest="props.preRequest" @updatePreRequest="emit('updatePreRequest')" />
            <DeletePreRequestC :id_PreRequest="props.preRequest.id_PreRequest"
                @deletePreRequest="emit('updatePreRequest')" />
        </div>
        <div v-else-if="props.preRequest.type === 'ConsumoPersonal'" class="flex justify-end gap-2">
            <UpdatePreRequestPC :preRequest="props.preRequest" @updatePreRequest="emit('updatePreRequest')" />
            <DeletePreRequestPC :id_PreRequest="props.preRequest.id_PreRequest"
                @deletePreRequest="emit('updatePreRequest')" />
        </div>
        <div v-else-if="props.preRequest.type === 'Herramienta'" class="flex justify-end gap-2">
            <UpdatePreRequestT :preRequest="props.preRequest" @updatePreRequest="emit('updatePreRequest')" />
            <DeletePreRequestT :id_PreRequest="props.preRequest.id_PreRequest"
                @deletePreRequest="emit('updatePreRequest')" />
        </div>
    </div>
    <!-- Para editar o eliminar la request -->
    <div v-if="props.preRequest?.status === 'request'" class="flex justify-end gap-2">

    </div>
    <!-- Para editar o eliminar la authorization -->
    <div v-if="props.preRequest?.status === 'authorization'" class="flex justify-end gap-2">

    </div>
    <!-- Para editar o eliminar la rechazar -->
    <div v-if="props.preRequest?.status === 'decline'" class="flex justify-end gap-2">

    </div>
    <!-- Para editar o eliminar la deliverie -->
    <div v-if="props.preRequest?.status === 'deliverie'" class="flex justify-end gap-2">

    </div>
    <!-- Para editar o eliminar la return_change -->
    <div v-if="props.preRequest?.status === 'return_exchange'" class="flex justify-end gap-2">

    </div>
</template>