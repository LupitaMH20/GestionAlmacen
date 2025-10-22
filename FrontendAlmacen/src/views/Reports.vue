<script setup lang="ts">

import UpdateApplicationC from '../components/Forms/Applications/PersonalConsumption/UpdatePersonalConsumption.vue';
import DeleteApplicationC from '../components/Forms/Applications/PersonalConsumption/DeletePersonal consumption.vue'

import UpdateApplicationCO from '../components/Forms/Applications/Consumables/UpdateConsumable.vue';
import DeleteApplicationCO from '../components/Forms/Applications/Consumables/DeleteConsumable.vue';

import UpdateApplicationT from '../components/Forms/Applications/Tools/UpdateTools.vue';
import DeleteApplicationT from '../components/Forms/Applications/Tools/DeleteTools.vue';
import CreateAuthorize from '../components/Forms/Authorize/CreateAuthorize.vue'
import CreateDecline from '../components/Forms/Decline/CreateDecline.vue';
import PreRequest from '../components/Forms/Applications/Consumables/PreRequest.vue';

</script>

<template>
    <label>Consumo Personal solicitud</label>
    <div class="grid grid-cols-3 grid-rows-1 gap-1">
        <div>
            <UpdateApplicationC />
        </div>
        <div>
            <DeleteApplicationC /> 
        </div>
    </div>
    <label>Consumibles solicitud</label>
    <div class="grid grid-cols-3 grid-rows-1 gap-1">
        <div>
            <CreateApplicationCO/>
        </div>
        <div>
            <UpdateApplicationCO />
        </div>
        <div>
            <DeleteApplicationCO />
        </div>
    </div>
    <label>Herramientas solicitudes</label>
    <div class="grid grid-cols-3 grid-rows-1 gap-1">
        <div>
            <CreateApplicationT/>
        </div>
        <div>
            <UpdateApplicationT />
        </div>
        <div>
            <DeleteApplicationT />
        </div>
    </div>
    <label>Autorizar</label>
    <CreateAuthorize />
    <label>Rechazar</label>
    <CreateDecline />
</template>