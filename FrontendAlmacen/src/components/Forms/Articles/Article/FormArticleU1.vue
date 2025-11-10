<script setup lang="ts">
import { FormField, FormItem, FormLabel, FormControl } from '../../../ui/form'
import Input from '../../../ui/input/Input.vue';

const props = defineModel('props', { type: Object, required: true })
</script>

<template>
    <form>
        <FormField name="Articlename">
            <FormItem>
                <div class="p-1.5">
                    <FormLabel>ID Producto Principal *</FormLabel>
                    <FormControl>
                        <Input v-model="props.id_mainarticle" type="text" disabled />
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel>ID Producto Alternativo *</FormLabel>
                    <FormControl>
                        <Input v-model="props.alternativearticle" type="text" disabled />
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel>Nombre del Producto *</FormLabel>
                    <FormControl>
                        <Input v-model="props.name" type="text" placeholder="Ingrese el nombre"/>
                    </FormControl>
                </div>
            </FormItem>
        </FormField>
    </form>
</template>
