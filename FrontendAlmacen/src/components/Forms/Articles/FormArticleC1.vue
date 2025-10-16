<script setup lang="ts">
import { FormField, FormItem, FormLabel, FormControl } from '../../ui/form'
import Input from '../../ui/input/Input.vue';

const props = defineModel('props', {type: Object, required:true})
</script>

<template>
    <form>
        <FormField name="Articlename">
            <FormItem>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">ID Producto Principal *</FormLabel>
                    <FormControl>
                        <Input v-model="props.id_mainarticle" type="text" placeholder="Ingrese el idProductoPrincipal" class="w-50 font-sans text-12 font-light" />
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">ID Producto Alternativo *</FormLabel>
                    <FormControl>
                        <Input v-model="props.id_alternativearticle " type="text" placeholder="Ingrese el idProductoAlternatico" class="w-50 font-sans text-12 font-light" />
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Nombre del Producto *
                    </FormLabel>
                    <FormControl>
                        <Input v-model="props.name" type="text" placeholder="Ingrese el nombre" class="w-50 font-sans text-12 font-light" />
                    </FormControl>
                </div>
            </FormItem>
        </FormField>
    </form>
</template>