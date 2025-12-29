<script setup lang="ts">
import { useSlots} from 'vue';
import { Dialog, DialogContent, DialogFooter, DialogTrigger, DialogTitle } from '../ui/dialog';
import Button from '../ui/button/Button.vue';
import { LucideIcon } from 'lucide-vue-next';
import { Ban, Save } from 'lucide-vue-next';

const props = defineProps<{
    title: string;
    titleButton: string;
    iconP: LucideIcon;
    iconT: LucideIcon;
}>();

const open = defineModel<boolean>()
const emit = defineEmits(['save', 'cancel']);

const IconComponent = (icon: LucideIcon) => icon;
</script>

<template>
    <Dialog v-model:open="open">
        <DialogTrigger>
            <Button variant="outline" class="flex items-center gap-2">
                <component :is="IconComponent(props.iconP)" class="w-10 h-10 " />
                <span>{{ titleButton }}</span>
            </Button>
        </DialogTrigger>
        <DialogContent class="w-full">
            <DialogTitle>
                <div class="flex">
                    <component :is="IconComponent(props.iconT)" class=" w-10 h-10 gap-4" />
                    <label class="flex justify-center text-[24px] font-sans font-bold p-5 text-center">{{ title }}</label>
                </div>
            </DialogTitle>
            <div class="flex justify-center">
                <slot name="forms"></slot>
            </div>
            <DialogFooter class="flex justify-self-center gap-20">
                <slot name="actions-extra"></slot>
                <Button @click="$emit('cancel')"
                    class="bg-white text-black hover:bg-black hover:text-white border border-write">
                    <Ban class="w-4 h-4 mr-3 " /> Cerrar
                </Button>
                <Button type="submit" @click="$emit('save')"
                    class="bg-white text-black hover:bg-black hover:text-white border border-write">
                    <Save class="w-4 h-4 mr-3" /> Guardar
                </Button>
            </DialogFooter>
        </DialogContent>
    </Dialog>
</template>