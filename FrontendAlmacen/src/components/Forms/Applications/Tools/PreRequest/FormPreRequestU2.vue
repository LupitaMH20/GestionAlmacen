<script setup lang="ts">
import { FormField, FormItem, FormLabel, FormControl } from '../../../../ui/form'
import Input from '../../../../ui/input/Input.vue';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../../../../ui/select'
import Textarea from '../../../../ui/textarea/Textarea.vue';
import { TypeStore } from '../../../../data/TypeStore';

const props = defineModel('props', {type:Object, required:true})
</script>

<template>
    <form>
        <FormField name="Consumablename3">
            <FormItem>
                <div class="p-1.5">
                    <Label class="text-24 font-sans font-bold p-1.5">Nombre ó ID *</Label>
                    <FormControl>
                        <Input v-model="props.article" type="text" class="w-50 font-sans text-12 font-light" />
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Cantidad *</FormLabel>
                    <FormControl>
                        <Input v-model="props.amount" type="number" class="w-50 font-sans text-12 font-light" />
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Almacen *</FormLabel>
                    <Select v-model="props.store">
                        <SelectTrigger class="w-50">
                            <SelectValue v-model="props.store" class="text-12 font-sans font-light" />
                        </SelectTrigger>
                        <SelectContent>
                            <SelectItem v-for="store in TypeStore" :key="store.value" :value="store.value">
                                {{ store.label }}
                            </SelectItem>
                        </SelectContent>
                    </Select>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5"> Descripción</FormLabel>
                    <FormControl>
                        <Textarea v-model="props.description" type="text" class="w-50 font-sans text-12 font-light my-3 h-25"></Textarea>
                    </FormControl>
                </div>
            </FormItem>
        </FormField>
    </form>
</template>