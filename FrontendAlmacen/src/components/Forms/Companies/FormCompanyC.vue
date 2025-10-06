<script setup lang="ts">
import { FormControl, FormField, FormItem, FormLabel } from "../../ui/form";
import Input from "../../ui/input/Input.vue";
</script>

<template>
    <form class="pt-5">
        <FormField name="Companycreate">
            <FormItem>
                <FormLabel class="text-24 font-sans font-bold p-1.5">Nombre *</FormLabel>
                <FormControl>
                    <Input placeholder="Ingrese el nombre de la empresa" class="w-75 text-12 font-sans font-light" />
                </FormControl>
                <FormLabel class="text-24 font-sans font-bold p-1.5">Dirección *</FormLabel>
                <FormControl>
                    <Input placeholder="Ingrese la dirección de la empresa" class="w-75 text-12 font-sans font-light" />
                </FormControl>
            </FormItem>
        </FormField>
    </form>
</template>