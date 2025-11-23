<script setup lang="ts">
import { useSlots, defineEmits } from 'vue';
import { Tabs, TabsList, TabsTrigger, TabsContent } from '../ui/tabs'
import { Dialog, DialogContent, DialogFooter, DialogTrigger, DialogTitle } from '../ui/dialog';
import Button from '../ui/button/Button.vue';
import { LucideIcon } from 'lucide-vue-next';
import { Ban, Save } from 'lucide-vue-next';

const props = defineProps<{
    title: string;
    titleButton: string;
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
            <Button variant="outline" class="flex items-center gap-2">
                <component :is="IconComponent(props.iconP)" class="w-10 h-10 " />
                <span>{{ titleButton }}</span>
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
                        <TabsList class="h-30 flex flex-col space-y-3 items-start mt-4">
                            <TabsTrigger class="w-full justify-start font-sans text-[16px] py-3 px-4" value="article">
                                <component :is="IconComponent(props.IconOf)" class="w-6 h-6 mr-3" />{{ recordof }}
                            </TabsTrigger>

                            <TabsTrigger class="w-full justify-start font-sans text-[16px] py-3 px-4"
                                value="description">
                                <component :is="IconComponent(props.IconD)" class="w-6 h-6 mr-3" />{{ description }}
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
                <Button @click="$emit('cancel')"
                    class="bg-whiite text-black hover:bg-black hover:text-white border border-write">
                    <Ban class="w-4 h-4 mr-3 " /> Cerrar
                </Button>
                <Button type="submit" @click="$emit('save')"
                    class="bg-whiite text-black hover:bg-black hover:text-white border border-write">
                    <Save class="w-4 h-4 mr-3" /> Guardar
                </Button>
            </DialogFooter>
        </DialogContent>
    </Dialog>
</template>