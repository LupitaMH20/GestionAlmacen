<script setup lang="ts">
// Creacion de request
import CreateApplicationCP from '../../Forms/Applications/PersonalConsumption/Request/CreatePersonalConsumption.vue';
import CreateApplicationCO from '../../Forms/Applications/Consumables/Request/CreateConsumable.vue';
import CreateApplicationT from '../../Forms/Applications/Tools/Request/CreateTools.vue';

//create authorized
import Authorized from '../../Forms/AuthorizeDeclined/CreateAuthorize.vue';
import Decline from '../../Forms/AuthorizeDeclined/CreateDecline.vue';

const props = defineProps<{
    Request: {
        id_Request: string | number;
        type?: string;
        status?: string | null;
        acceptance: {
            id_acceptance: number;
        } | null
        user: {id_user:string};
        article?: string;
        amount?: number;
    }
}>();

const emit = defineEmits(['createPrecess']);

const validRequestType = ['Consumable', 'Tool', 'PersonalConsumption'];
</script>

<template>
    <div v-if="props.Request.status === 'prerequest'">
        <component :is="props.Request.type === 'Consumable' ? CreateApplicationCO
            : props.Request.type === 'Tool' ? CreateApplicationT
                : props.Request.type === 'PersonalConsumption' ? CreateApplicationCP
                    : null" :Request="props.Request" @createRequest="emit('createPrecess')" />
    </div>
    <div v-else-if="props.Request.status === 'request'">
        <div class="flex justify-center gap-2" v-if="validRequestType.includes(props.Request.type || '')">
            <Authorized :Request="props.Request" @createAuthorized="emit('createPrecess')" />
            <!-- <Decline :Request="props.Request" @createDecline="emit('createPrecess')"/> -->
        </div>
    </div>
</template>