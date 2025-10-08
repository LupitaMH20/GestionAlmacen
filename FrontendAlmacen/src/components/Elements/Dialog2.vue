<script setup lang="ts">
import { useSlots, defineEmits } from 'vue';
import { Tabs, TabsList, TabsTrigger, TabsContent } from '../ui/tabs'
import { Dialog, DialogContent, DialogFooter, DialogTrigger, DialogTitle } from '../ui/dialog';
import Button from '../ui/button/Button.vue';
import { LucideIcon } from 'lucide-vue-next';
import { Ban, Save } from 'lucide-vue-next';

const props = defineProps<{
    title: string;
    iconP: LucideIcon;
    iconT: LucideIcon;
    recordof: string;
    IconOf: LucideIcon;
    description: string;
    IconD: LucideIcon;
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
        <DialogContent class="sm:max-w-[500px]">
            <DialogTitle>
                <component :is="IconComponent(props.iconT)" class="w-10 h-10 gap-4" />
            </DialogTitle>
            <Tabs default-value="account">
                <div class="grid grid-cols-2 grid-rows-1 gap-4">
                    <div>
                        <label class="text-[24px] font-sans font-bold p-0 text-center">{{ title.split('')[0] }}</label>
                        <label class="text-[24px] font-sans font-bold p-0 text-center">{{ title.split('').slice(1).join('')
                            }}</label>
                        <TabsList class="grid grid-cols-1 grid-rows-2 space-y-4 items-start">
                            <TabsTrigger class="font-sans text-[16px] p-0" value="article">
                                <component :is="IconComponent(props.IconOf)" class="w-10 h-10 gap-3" />{{ recordof }}
                            </TabsTrigger>
                            <TabsTrigger class="font-sans text-[16px] p-0" value="description">
                                <component :is="IconComponent(props.IconD)" class="w-10 h-10 gap-3" />{{ description }}
                            </TabsTrigger>
                        </TabsList>
                    </div>
                    <div>
                        <TabsContent value="article">
                            <slot name="form1"></slot>
                        </TabsContent>
                        <TabsContent value="description">
                            <slot name="form2"></slot>
                        </TabsContent>
                    </div>
                </div>
            </Tabs>
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