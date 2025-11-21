<script setup lang="ts">
import { defineEmits, defineModel } from 'vue';
import { Dialog, DialogContent, DialogFooter, DialogTrigger, DialogTitle } from '../ui/dialog';
import Button from '../ui/button/Button.vue';
import { LucideIcon, Ban, Save } from 'lucide-vue-next';

//Son las rutas de lo que se mostrara en el dialog
import DialogPreRequest from './ComponentsDialog/DialogPreRequest.vue';
import DialogRequest from './ComponentsDialog/DialogRequest.vue';
import DialogAuthorize from './ComponentsDialog/DialogAuthorize.vue';
import DialogDeclined from './ComponentsDialog/DialogDeclined.vue';
import DialogSupply from './ComponentsDialog/DialogSupply.vue';
import DialogReturnExchange from './ComponentsDialog/DialogReturnExchange.vue';

// rutas para crear el estado de la solicitud
import CreateProcess from './ComponentsDialog/CreateProcess.vue';

//rutas para editar y eliminar los procesos de la solicitud
import UpdateDelete from './ComponentsDialog/UpdateDelete.vue';

interface Companies { id_Company: string; name: string };
interface Users { id_user: string; name: string; };
interface Collaborators { id_Collaborator: string; name: string; last_name: string };
interface Article { id_mainarticle: string, name: string }

const props = defineProps<{
  title: string;
  titleButton: string;
  iconP: LucideIcon;
  iconT: LucideIcon;
  Request: {
    id_Request: number | string;
    title: string;
    article: string;
    articleName?: Article;
    currentStatus: 'prerequest' | 'request' | 'authorized' | 'declined' | 'supply' | 'finished' | 'archived';
    date: string;
    time: string;
    type?: string;
    user?: string;
    collaborator?: string;
    userName?: Users;
    collaboratorName?: Collaborators;
    description?: string;
    amount?: number;
    status?: string;
    order_workshop?: string;
    store?: string;
    requestingCompany?: string;
    supplierCompany?: string;
    requestingCompanyName?: Companies;
    supplierCompanyName?: Companies;
    unitPrice?: number;
    totalValue?: number;
    acceptance?: {
      id_acceptance: number;
      user?: string;
      userName?: Users;
      article?: string;
      articleName?: Article;
      date?: string;
      time?: string;
      requestactions?: {
        id_RequestActions: number;
        action: 'authorized' | 'declined';
        comment: string;
        requestactions_datetime: string;
        user: Users;
        date?: string;
        time?: string;
        supply?: {
          id_supply: number;
          user?: Users;
          userName?: Users;
          collaborator?: string;
          collaboratorName?: Collaborators;
          comment?: string;
          date?: string;
          time?: string;
        } | null
      } | null;
    } | null;
  }
}>();


const open = defineModel<boolean>();
const emit = defineEmits(['dialog']);

const IconComponent = (icon: LucideIcon) => icon;
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
          <UpdateDelete :Request="props.Request" @update="emit('dialog')" />
        </div>
      </DialogTitle>

      <div class="flex flex-col gap-4 overflow-y-auto max-h-[60vh] p-1">
        <DialogPreRequest v-if="props.Request" :Request="props.Request" />
        <DialogRequest v-if="props.Request.acceptance" :acceptance="props.Request.acceptance" />
        <DialogAuthorize
          v-if="props.Request.acceptance?.requestactions && props.Request.acceptance.requestactions.action === 'authorized'"
          :requestactions="props.Request.acceptance.requestactions" />
        <DialogDeclined
          v-if="props.Request.acceptance?.requestactions && props.Request.acceptance.requestactions.action === 'declined'"
          :requestactions="props.Request.acceptance.requestactions" />
        <DialogSupply v-if="props.Request.acceptance?.requestactions?.supply"
          :supply="props.Request.acceptance.requestactions.supply" />
        <!-- <DialogReturnExchange v-if="props.Request.request?.deliverie?.return_exchange" :return_exchange="props.Request.request.deliverie.return_exchange" /> -->
      </div>

      <DialogFooter class="flex justify-between mt-5 pt-3 border-t">
        <Button  variant="secondary"
          @click="open = false" class="flex items-center gap-2">
          <Ban class="w-4 h-4" />cerrar
        </Button>

        <CreateProcess :Request="props.Request" @createPrecess="emit('dialog')" />
      </DialogFooter>
    </DialogContent>
  </Dialog>
</template>