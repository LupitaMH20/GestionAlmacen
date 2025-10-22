<script setup lang="ts">
import { defineEmits, defineModel } from 'vue';
import { Dialog, DialogContent, DialogFooter, DialogTrigger, DialogTitle } from '../ui/dialog';
import Button from '../ui/button/Button.vue';
import { LucideIcon, Ban, Save } from 'lucide-vue-next';
import CreateConsumable from '../Forms/Applications/Consumables/CreateConsumable.vue';

const props = defineProps<{
  title: string;
  titleButton: string;
  iconP: LucideIcon;
  iconT: LucideIcon;
  preRequest: {
    applicant: string;
    collaborator: string;
    type: string;
    article: string;
    description: string;
    amount: number;
    status: string;
    order_workshop: string;
    store: string;
    requestingCompany: string;
    supplierCompany: string;
  };
}>();

const open = defineModel<boolean>();
const emit = defineEmits(['request']);

const IconComponent = (icon: LucideIcon) => icon;
</script>

<template>
  <Dialog v-model:open="open">
    <DialogTrigger>
      <Button variant="outline" class="flex items-center gap-2">
        <component :is="IconComponent(props.iconP)" class="w-10 h-10" />
        <span>{{ titleButton }}</span>
      </Button>
    </DialogTrigger>
    <DialogContent class="sm:max-w-[420px] bg-white rounded-xl shadow-lg">
      <DialogTitle class="flex items-center gap-3 border-b pb-2">
        <component :is="IconComponent(props.iconT)" class="w-8 h-8 text-gray-700" />
        <span class="text-lg font-semibold">{{ title }}</span>
      </DialogTitle>
      <div class="mt-4 space-y-2 text-sm font-sans">
        <div><strong>Solicitante:</strong> {{ props.preRequest.applicant || '—' }}</div>
        <div><strong>Colaborador:</strong> {{ props.preRequest.collaborator || '—' }}</div>
        <div><strong>Tipo:</strong> {{ props.preRequest.type || '—' }}</div>
        <div><strong>Artículo:</strong> {{ props.preRequest.article || '—' }}</div>
        <div><strong>Descripción:</strong> {{ props.preRequest.description || '—' }}</div>
        <div><strong>Cantidad:</strong> {{ props.preRequest.amount || '—' }}</div>
        <div><strong>Estatus:</strong> {{ props.preRequest.status || '—' }}</div>
        <div><strong>Orden/Taller:</strong> {{ props.preRequest.order_workshop || '—' }}</div>
        <div><strong>Almacén:</strong> {{ props.preRequest.store || '—' }}</div>
        <div><strong>Empresa Solicitante:</strong> {{ props.preRequest.requestingCompany || '—' }}</div>
        <div><strong>Empresa Proveedora:</strong> {{ props.preRequest.supplierCompany || '—' }}</div>
      </div>
      <DialogFooter class="flex justify-between mt-5 pt-3 border-t">
        
        <CreateConsumable/>
      </DialogFooter>
    </DialogContent>
  </Dialog>
</template>
