<script setup lang="ts">
import { FormField, FormItem, FormLabel, FormControl } from '../../ui/form'
import Input from '../../ui/input/Input.vue';
</script>

<template>
    <form>
        <FormField name="Articlename">
            <FormItem>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">ID Producto Principal *</FormLabel>
                    <FormControl>
                        <Input type="text" placeholder="idProductoPrincipal" class="w-50 font-sans text-12 font-light" />
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">ID Producto Alternativo *</FormLabel>
                    <FormControl>
                        <Input type="text" placeholder="idProductoAlternativo" class="w-50 font-sans text-12 font-light" />
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Nombre del Producto *
                    </FormLabel>
                    <FormControl>
                        <Input type="text" placeholder="Ingrese el nombre" class="w-50 font-sans text-12 font-light" />
                    </FormControl>
                </div>
            </FormItem>
        </FormField>
    </form>
</template>