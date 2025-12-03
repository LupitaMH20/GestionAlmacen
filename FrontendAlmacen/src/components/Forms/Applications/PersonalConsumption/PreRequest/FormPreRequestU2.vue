<script setup lang="ts">
import { FormField, FormItem, FormLabel, FormControl } from '../../../../ui/form'
import Input from '../../../../ui/input/Input.vue';
import Textarea from '../../../../ui/textarea/Textarea.vue';

// Usar defineModel correctamente para v-model bidireccional
const modelValue = defineModel<{
    article: string;
    amount: number;
    description: string;
    [key: string]: any;
}>({ required: true });
</script>

<template>
    <form>
        <FormField name="Consumablename3">
            <FormItem>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">ID del Producto *</FormLabel>
                    <FormControl>
                        <Input v-model="modelValue.article" type="text" class="w-50 font-sans text-12 font-light" />
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Cantidad *</FormLabel>
                    <FormControl>
                        <!-- Usamos v-model.number para asegurar que sea numérico -->
                        <Input v-model.number="modelValue.amount" type="number" class="w-50 font-sans text-12 font-light" />
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5"> Descripción</FormLabel>
                    <FormControl>
                        <Textarea v-model="modelValue.description" type="text" class="w-50 font-sans text-12 font-light my-3 h-25"></Textarea>
                    </FormControl>
                </div>
            </FormItem>
        </FormField>
    </form>
</template>