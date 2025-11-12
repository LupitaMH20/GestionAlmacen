<script setup lang="ts">
// rutas para editar y eliminar la presolicitud de Consumables
import UpdatePreRequestC from '../../Forms/Applications/Consumables/PreRequest/UpdatePreRequest.vue'
import DeletePreRequestC from '../../Forms/Applications/Consumables/PreRequest/DeletePreRequest.vue'

// rutas para editar y eliminar la presolicitud de PersonalConsumption
// import UpdateRequestPC from '../../Forms/Applications/PersonalConsumption/Request/UpdateRequest.vue'
// import DeleteRequestPC from '../../Forms/Applications/PersonalConsumption/Request/DeleteRequest.vue'

// //rutas para editar y eliminar la presolicitud de Tools
// import UpdateRequestT from '../../Forms/Applications/Tools/Request/UpdateRequest.vue'
// import DeleteRequestT from '../../Forms/Applications/Tools/Request/DeleteRequest.vue'

const props = defineProps<{
    Request: {
        id_Request: string | number;
        type?: string;
        status?: string;
    }
}>();

const emit = defineEmits(['updateRequest'])
</script>
<template>
    <!-- Para editar o eliminar la Request -->
    <div v-if="props.Request?.status === 'prerequest'">
        <div v-if="props.Request.type === 'Consumable'" class="flex justify-end gap-2">
            <UpdatePreRequestC :Request="props.Request" @updateRequest="emit('updateRequest')" />
            <DeletePreRequestC :id_Request="props.Request.id_Request"
                @deleteRequest="emit('updateRequest')" />
        </div>
        <div v-else-if="props.Request.type === 'ConsumoPersonal'" class="flex justify-end gap-2">
            <UpdateRequestPC :Request="props.Request" @updateRequest="emit('updateRequest')" />
            <DeleteRequestPC :id_Request="props.Request.id_Request"
                @deleteRequest="emit('updateRequest')" />
        </div>
        <div v-else-if="props.Request.type === 'Herramienta'" class="flex justify-end gap-2">
            <UpdateRequestT :Request="props.Request" @updateRequest="emit('updateRequest')" />
            <DeleteRequestT :id_Request="props.Request.id_Request"
                @deleteRequest="emit('updateRequest')" />
        </div>
    </div>
    <!-- Para editar o eliminar la request -->
    <div v-if="props.Request?.status === 'request'" class="flex justify-end gap-2">

    </div>
    <!-- Para editar o eliminar la authorization -->
    <div v-if="props.Request?.status === 'authorization'" class="flex justify-end gap-2">

    </div>
    <!-- Para editar o eliminar la rechazar -->
    <div v-if="props.Request?.status === 'decline'" class="flex justify-end gap-2">

    </div>
    <!-- Para editar o eliminar la deliverie -->
    <div v-if="props.Request?.status === 'deliverie'" class="flex justify-end gap-2">

    </div>
    <!-- Para editar o eliminar la return_change -->
    <div v-if="props.Request?.status === 'return_exchange'" class="flex justify-end gap-2">

    </div>
</template>