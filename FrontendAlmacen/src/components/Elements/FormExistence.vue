<script setup lang="ts">
import { FormField, FormItem, FormLabel, FormControl, FormDescription } from '../ui/form';
import Input from '../ui/input/Input.vue';


</script>

<template>
    <form>
        <FormField name="Existence">
            <FormItem>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Nombre ó ID *</FormLabel>
                    <FormControl>
                        <Input placeholder="Ingrese el nombre" class="w-50 font-sans text-12 font-light" />
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Stock *</FormLabel>
                    <FormControl>
                        <Input placeholder="Cantidad" class="w-50 font-sans text-12 font-light" />
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Cantidad *</FormLabel>
                    <FormControl>
                        <Input placeholder="Ingrese la cantidad" class="w-50 font-sans text-12 font-light" />
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Existencia </FormLabel>
                </div>
            </FormItem>
        </FormField>
    </form>
</template>