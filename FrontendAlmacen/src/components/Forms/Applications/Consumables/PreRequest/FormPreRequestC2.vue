<script setup lang="ts">
import { FormField, FormItem, FormLabel, FormControl } from '../../../../ui/form'
import Input from '../../../../ui/input/Input.vue';
import Textarea from '../../../../ui/textarea/Textarea.vue';

const props = defineModel('props', { type: Object, required: true })
</script>

<template>
    <form>
        <FormField name="Consumablename3">
            <FormItem>
                <div class="p-1.5">
                    <Label class="text-24 font-sans font-bold p-1.5">ID del producto*</Label>
                    <FormControl>
                        <Input v-model="props.article" type="text" placeholder="ID de producto"
                            class="w-50 font-sans text-12 font-light" />
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Cantidad *</FormLabel>
                    <FormControl>
                        <Input v-model="props.amount" type="number" placeholder="Ingrese la cantidad"
                            class="w-50 font-sans text-12 font-light" />
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Orden de taller *</FormLabel>
                    <FormControl>
                        <Input v-model="props.order_workshop" type="text" placeholder="Ingrese la orden de taller"
                            class="w-50 font-sans text-12 font-light" />
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5"> Descripción</FormLabel>
                    <FormControl>
                        <Textarea v-model="props.description" type="text" placeholder="Ingrese una descripción"
                            class="w-50 font-sans text-12 font-light my-3 h-25"></Textarea>
                    </FormControl>
                </div>
            </FormItem>
        </FormField>
    </form>
</template>