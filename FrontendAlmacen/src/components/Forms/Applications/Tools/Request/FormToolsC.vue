<script setup lang="ts">
import { FormField, FormItem, FormLabel, FormControl } from '../../../../ui/form/index.ts'
import Input from '../../../../ui/input/Input.vue'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../../../../ui/select/index.ts'
import { TypeStore } from '../../../../data/TypeStore.ts'
import Textarea from '../../../../ui/textarea/Textarea.vue'

</script>

<template>
    <form>
        <FormField name="Username">
            <FormItem>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Nombre ó ID *</FormLabel>
                    <FormControl>
                        <Input placeholder="Ingrese el nombre o el ID" class="w-50 text-12 font-sans font-light" />
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Almacén *</FormLabel>
                    <Select>
                        <SelectTrigger class="w-50">
                            <SelectValue placeholder="Seleccione el tipo de almacén" class="text-12 font-sans font-light" />
                        </SelectTrigger>
                        <SelectContent>
                            <SelectItem v-for="store in TypeStore" :key="store.value" :value="store.value"
                                class="w-50">
                                {{ store.label }}
                            </SelectItem>
                        </SelectContent>
                    </Select>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5"> Descripción</FormLabel>
                    <FormControl>
                        <Textarea type="text" placeholder="Ingrese una descripción" class="w-50 font-sans text-12 font-light my-3 h-25"></Textarea>
                    </FormControl>
                </div>
            </FormItem>
        </FormField>
    </form>
</template>