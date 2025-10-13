<script setup lang="ts">
import {ref, defineExpose} from 'vue'
import { FormControl, FormField, FormItem, FormLabel } from "../../ui/form";
import Input from "../../ui/input/Input.vue";

const name = ref('')
const address = ref('')

const submitForm = () => {
    const data = {
        name: name.value,
        address: address.value
    }
    return data
}

defineExpose({submitForm})
</script>

<template>
    <form class="pt-5">
        <FormField name="Companycreate">
            <FormItem>
                <FormLabel class="text-24 font-sans font-bold p-1.5">Nombre *</FormLabel>
                <FormControl>
                    <Input v-model="name" placeholder="Ingrese el nombre de la empresa" class="w-75 text-12 font-sans font-light" />
                </FormControl>
                <FormLabel class="text-24 font-sans font-bold p-1.5">Dirección *</FormLabel>
                <FormControl>
                    <Input v-model="address" placeholder="Ingrese la dirección de la empresa" class="w-75 text-12 font-sans font-light" />
                </FormControl>
            </FormItem>
        </FormField>
    </form>
</template>