<script setup lang="ts">
// Creacion de request
import CreateApplicationCP from '../../Forms/Applications/PersonalConsumption/Request/CreatePersonalConsumption.vue';
import CreateApplicationCO from '../../Forms/Applications/Consumables/Request/CreateConsumable.vue';
import CreateApplicationT from '../../Forms/Applications/Tools/Request/CreateTools.vue';

//create authorized y declined
import Authorized from '../../Forms/AuthorizeDeclined/CreateAuthorize.vue';
import Decline from '../../Forms/AuthorizeDeclined/CreateDecline.vue';

//create de supply
import CreateSupply from '../../Forms/Supply/CreateSupply.vue';

interface Companies { id_Company: string; name: string };
interface Users { id_user: string; name: string; };
interface Collaborators { id_Collaborator: string; name: string; last_name: string };
interface Article { id_mainarticle: string, name: string }

const props = defineProps<{
    Request: {
        id_Request: string | number;
        user?: Users | null;
        userName?: Users;
        collaborator?: string;
        collaboratorName?: Collaborators;
        type?: string;
        article?: string;
        articleName?: Article;
        description?: string;
        amount?: number;
        status?: string;
        order_workshop?: string;
        store?: string;
        requestingCompany?: string;
        supplierCompany?: string;
        requestingCompanyName?: Companies;
        supplierCompanyName?: Companies;
        date?: string;
        time?: string;
        acceptance?: {
            id_acceptance: number;
            user?: Users | null;
            userName?: Users;
            article?: Article | null;
            articleName?: Article;
            date?: string;
            time?: string;
            requestactions?: {
                id_RequestActions: number;
                action: 'authorized' | 'declined';
                comment: string;
                requestactions_datetime: string;
                user: Users | null;
                date?: string;
                time?: string;
            } | null;
        } | null;
    };
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
    <div v-else-if="props.Request.status === 'request' || props.Request.status === 'declined'">
        <div class="flex justify-center gap-2" v-if="validRequestType.includes(props.Request.type || '')">
            <Authorized :Request="props.Request" @createAuthorized="emit('createPrecess')" />
            <Decline :Request="props.Request" @createAuthorized="emit('createPrecess')" />
        </div>
    </div>
    <div v-else-if="props.Request.status === 'authorized'">
        <CreateSupply :Request="props.Request" @supplyCreated="emit('createPrecess')" />
    </div>
</template>