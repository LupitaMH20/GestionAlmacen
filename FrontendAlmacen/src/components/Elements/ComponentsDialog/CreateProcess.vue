<script setup lang="ts">
// Creacion de request
import CreateApplicationC from '../../Forms/Applications/PersonalConsumption/Request/CreatePersonalConsumption.vue';
import CreateApplicationCO from '../../Forms/Applications/Consumables/Request/CreateConsumable.vue';
import CreateApplicationT from '../../Forms/Applications/Tools/Request/CreateTools.vue';

//create authorized
import Authorized from '../../Forms/AuthorizeDeclined/CreateAuthorize.vue';
import Decline from '../../Forms/AuthorizeDeclined/CreateDecline.vue';

const props = defineProps<{
    Request: {
        id_Request: string | number;
        type?: string;
        status?: string;
        acceptance: {
            id_acceptance: number;
        } | null
        user: {id_user:string};
    }
}>();

const emit = defineEmits(['createPrecess']);

const validRequestType = ['Consumable', 'Tools', 'PersonalConsumption'];
</script>

<template>
    <div v-if="props.Request.status === 'prerequest'">
        <component :is="props.Request.type === 'Consumable' ? CreateApplicationCO
            : props.Request.type === 'Tool' ? CreateApplicationT
                : props.Request.type === 'PersonalConsumption' ? CreateApplicationC
                    : null" :Request="props.Request" @updateRequest="emit('createPrecess')" />
    </div>
    <div v-else-if="props.Request.status === 'request'">
        <div class="flex justify-center gap-2" v-if="validRequestType.includes(props.Request.type || '')">
            <Authorized :Request="props.Request" @createAuthorized="emit('createPrecess')" />
            <!-- <Decline :Request="props.Request" @createDecline="emit('createPrecess')"/> -->
        </div>
    </div>
</template>