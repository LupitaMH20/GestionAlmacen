<script setup lang="ts">
import { icons } from 'lucide-vue-next';
import { Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle, DialogTrigger } from '../ui/dialog'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '../ui/tabs'
import { LucideIcon, Save, Ban } from 'lucide-vue-next';
import { useSlots, defineEmits } from 'vue';
import Button from '../ui/button/Button.vue';

const props = defineProps<{
    title: string;
    iconP: LucideIcon;
    iconT: LucideIcon;
    recordof: string;
    iconOf: LucideIcon;
    existence: string;
    iconE: LucideIcon;
    description: string;
    iconD: LucideIcon;
}>()

const emits = defineEmits(['save', 'cancel'])
const IconComponent = (icon: LucideIcon) => icon

const slots = useSlots();
</script>

<template>
    <Dialog>
        <DialogTrigger>
            <Button variant="outline">
                <component :is="IconComponent(props.iconP)" />
            </Button>
        </DialogTrigger>
        <DialogContent class="sm-max-w-[500px]">
            <DialogHeader>
                <DialogTitle>
                    <component :is="IconComponent(props.iconT)" />
                </DialogTitle>
                <DialogDescription>
                    <Tabs default-value="account">
                        <div class="grid grid-cols-2 grid-rows-1 gap-4">
                            <div>
                                <label class="text-[24px] font-sans font-bold p-0 text-center text-black">{{ title.split('')[0] }}</label>
                                <label class="text-[24px] font-sans font-bold p-0 text-center  text-black">{{ title.split('').slice(1).join('') }}</label>
                                <TabsList class="h-45 flex flex-col space-y-3 items-start  mt-3">
                                    <TabsTrigger class="  w-full justify-start font-sans text-[14px] py-3 px-4 text-black" value="article">
                                        <component :is="IconComponent(props.iconOf)" class="w-10 h-10 gap-3" />{{ recordof }}
                                    </TabsTrigger>
                                    <TabsTrigger class="w-full justify-start font-sans text-[14px] py-3 px-4" value="existence">
                                        <component :is="IconComponent(props.iconE)" class="w-10 h-10 gap-3" />{{ existence }}
                                    </TabsTrigger>
                                    <TabsTrigger class="w-full justify-start font-sans text-[14px] py-3 px-4" value="description">
                                        <component :is="IconComponent(props.iconD)" class="w-10 h-10 gap-3" />{{ description }}
                                    </TabsTrigger>
                                </TabsList>
                            </div>
                            <div>
                                <TabsContent value="article">
                                    <slot name="form1"></slot>
                                </TabsContent>
                                <TabsContent value="existence">
                                    <slot name="form2"></slot>
                                </TabsContent>
                                <TabsContent value="description">
                                    <slot name="form3"></slot>
                                </TabsContent>
                            </div>
                        </div>
                    </Tabs>
                </DialogDescription>
            </DialogHeader>
            <DialogFooter class="flex justify-self-center gap-20">
                <Button @click="$emit('cancel')"
                    class="bg-whiite text-black hover:bg-black hover:text-white border border-write">
                    <Ban class="w-4 h-4 mr-3 " /> Cancelar
                </Button>
                <Button type="submit" @click="$emit('save')"
                    class="bg-whiite text-black hover:bg-black hover:text-white border border-write">
                    <Save class="w-4 h-4 mr-3" /> Guardar
                </Button>
            </DialogFooter>
        </DialogContent>
    </Dialog>
</template>