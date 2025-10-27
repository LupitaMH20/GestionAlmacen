<script setup lang="ts">
import { defineEmits, defineModel, onMounted } from 'vue';
import { Dialog, DialogContent, DialogFooter, DialogTrigger, DialogTitle } from '../ui/dialog';
import Button from '../ui/button/Button.vue';
import { LucideIcon, Ban, Save } from 'lucide-vue-next';

//Son las rutas de lo que se mostrara en el dialog
import DialogPreRequestandRequest from './ComponentsDialog/DialogPreRequestandRequest.vue';
import DialogAuthorize from './ComponentsDialog/DialogAuthorize.vue';
import DialogDecline from './ComponentsDialog/DialogDecline.vue';
import DialogDeliverie from './ComponentsDialog/DialogDeliverie.vue';
import DialogReturnExchange from './ComponentsDialog/DialogReturnExchange.vue';

// rutas para crear una soliciud
import CreateApplicationC from '../Forms/Applications/PersonalConsumption/CreatePersonalConsumption.vue';
import CreateApplicationCO from '../Forms/Applications/Consumables/CreateConsumable.vue';
import CreateApplicationT from '../Forms/Applications/Tools/CreateTools.vue';

// rutas para editar y eliminar la presolicitud
import UpdatePreRequest from '../Forms/Applications/Consumables/UpdatePreRequest.vue'
import DeletePreRequest from '../Forms/Applications/Consumables/DeletePreRequest.vue'

interface Companies { id_Company: string; name: string };

const props = defineProps<{
  title: string;
  titleButton: string;
  iconP: LucideIcon;
  iconT: LucideIcon;
  preRequest: {
    applicant?: string;
    collaborator?: string;
    type?: string;
    article?: string;
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

    request?: {
      position?: string;
      request_datetime?: string;

      authorization?: {
        authorize?: string;
        comment?: string;
        authorized_datetime?: string;
      };

      decline?: {
        decline?: string;
        comment?: string;
        datetime?: string;
      };

      deliverie?: {
        persondelivery?: string;
        personreceives?: string;
        companydelivery?: string;
        companyreceives?: string;
        comment?: string;
        photo?: string;
        document?: string;
        deliverie_datetime?: string;

        return_exchange?: {
          returnenby?: string;
          receivedby?: string;
          deliverycompany?: string;
          receivingcompany?: string;
          reason?: string;
          return_datetime?: string;
        };
      };
    };
  };
}>();

const open = defineModel<boolean>();
const emit = defineEmits(['request']);

const IconComponent = (icon: LucideIcon) => icon;
onMounted(() => {
  console.log("Datos recibidos", props.preRequest)
})
</script>

<template>
  <Dialog v-model:open="open" class="w-[50vh]">
    <DialogTrigger>
      <Button variant="outline" class="flex items-center gap-2">
        <component :is="IconComponent(props.iconP)" class="w-10 h-10" />
        <span>{{ titleButton }}</span>
      </Button>
    </DialogTrigger>
    <DialogContent class="sm:max-w-[550px] bg-white rounded-xl shadow-lg">
      <DialogTitle class="flex items-center gap-15 border-b pb-2">
        <div class="flex items-center gap-3 pb-2">
          <component :is="IconComponent(props.iconT)" class="w-8 h-8 text-gray-700" />
          <span class="text-lg font-semibold">{{ title }}</span>
        </div>

        <div>
          <!-- Para editar o eliminar la prerequest -->
          <div v-if="props.preRequest?.status === 'prerequest'" class="flex justify-end gap-2">
            <UpdatePreRequest :preRequest="props.preRequest" />
            <DeletePreRequest :preRequest="props.preRequest" />
          </div>
          <!-- Para editar o eliminar la request -->
          <div v-if="props.preRequest?.status === 'request'" class="flex justify-end gap-2">
            <UpdatePreRequest :preRequest="props.preRequest" />
            <DeletePreRequest :preRequest="props.preRequest" />
          </div>
          <!-- Para editar o eliminar la authorization -->
          <div v-if="props.preRequest?.status === 'authorization'" class="flex justify-end gap-2">
            <UpdatePreRequest :preRequest="props.preRequest" />
            <DeletePreRequest :preRequest="props.preRequest" />
          </div>
          <!-- Para editar o eliminar la rechazar -->
          <div v-if="props.preRequest?.status === 'decline'" class="flex justify-end gap-2">
            <UpdatePreRequest :preRequest="props.preRequest" />
            <DeletePreRequest :preRequest="props.preRequest" />
          </div>
          <!-- Para editar o eliminar la deliverie -->
          <div v-if="props.preRequest?.status === 'deliverie'" class="flex justify-end gap-2">
            <UpdatePreRequest :preRequest="props.preRequest" />
            <DeletePreRequest :preRequest="props.preRequest" />
          </div>
          <!-- Para editar o eliminar la return_change -->
          <div v-if="props.preRequest?.status === 'return_exchange'" class="flex justify-end gap-2">
            <UpdatePreRequest :preRequest="props.preRequest" />
            <DeletePreRequest :preRequest="props.preRequest" />
          </div>
        </div>
      </DialogTitle>

      <DialogPreRequestandRequest v-if="props.preRequest" :preRequest="props.preRequest" />
      <DialogAuthorize v-if="props.preRequest.request?.authorization" :authorization="props.preRequest.request.authorization" />
      <DialogDecline v-if="props.preRequest.request?.decline" :decline="props.preRequest.request.decline" />
      <DialogDeliverie v-if="props.preRequest.request?.deliverie" :deliverie="props.preRequest.request.deliverie" />
      <DialogReturnExchange v-if="props.preRequest.request?.deliverie?.return_exchange" :return_exchange="props.preRequest.request.deliverie.return_exchange" />

      <DialogFooter class="flex justify-between mt-5 pt-3 border-t">
        <Button variant="secondary" @click="open = false" class="flex items-center gap-2">
          <Ban class="w-4 h-4" />Cancelar
        </Button>

        <component :is="props.preRequest.type === 'Consumible' ? CreateApplicationCO
          : props.preRequest.type === 'Herramienta' ? CreateApplicationT
            : props.preRequest.type === 'ConsumoPersonal' ? CreateApplicationC
              : null" />
      </DialogFooter>
    </DialogContent>
  </Dialog>
</template>