<script setup lang="ts">
import { useSlots, defineEmits } from 'vue';
import { Dialog, DialogContent, DialogFooter, DialogTrigger, DialogTitle } from '../ui/dialog';
import Button from '../ui/button/Button.vue';
import { LucideIcon } from 'lucide-vue-next';
import { Ban, Save } from 'lucide-vue-next';

const props = defineProps<{
    title: string;
    iconP: LucideIcon;
    iconT: LucideIcon;
}>();

const emit = defineEmits(['save', 'cancel']);

const IconComponent = (icon: LucideIcon) => icon;
const slots = useSlots();
</script>

<template>
    <Dialog>
        <DialogTrigger>
            <Button variant="outline">
                <component :is="IconComponent(props.iconP)" class="w-10 h-10 " />
            </Button>
        </DialogTrigger>
        <DialogContent class="sm:max-w-[370px]">
            <DialogTitle>
                <component :is="IconComponent(props.iconT)" class=" w-10 h-10 gap-4" />
            </DialogTitle>
                <div>
                    <div >
                        <label class="text-[24px] font-sans font-bold p-0 text-center">{{ title}}</label>
                    </div>
                    <div>
                        <slot name="forms"></slot>
                    </div>
                </div>
            <DialogFooter class="flex justify-self-center gap-20">
                <Button @click="$emit('cancel')" class="bg-whiite text-black hover:bg-black hover:text-white border border-write">
                    <Ban class="w-4 h-4 mr-3 " /> Cancelar
                </Button>
                <Button type="submit" @click="$emit('save')" class="bg-whiite text-black hover:bg-black hover:text-white border border-write">
                    <Save class="w-4 h-4 mr-3" /> Guardar
                </Button>
            </DialogFooter>
        </DialogContent>
    </Dialog>
</template>