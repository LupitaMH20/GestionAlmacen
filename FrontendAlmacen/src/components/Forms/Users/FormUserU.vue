<script setup lang="ts">
import { FormField, FormItem, FormLabel, FormControl } from '../../ui/form'
import Input from '../../ui/input/Input.vue'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../../ui/select/index.ts'
import { TypePosition } from '../../data/TypePosition.ts'

</script>
<template>
    <form>
        <FormField name="UsernameUpdate">
            <FormItem>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Nombre *</FormLabel>
                    <FormControl>
                        <Input placeholder="Josue" class="w-75 text-12 font-sans font-light" />
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Apellido *</FormLabel>
                    <FormControl>
                        <Input placeholder="Medina" class="w-75 text-12 font-sans font-light" />
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Puesto *</FormLabel>
                    <Select>
                        <SelectTrigger class="w-75">
                            <SelectValue placeholder="Director" class="text-12 font-sans font-light" />
                        </SelectTrigger>
                        <SelectContent>
                            <SelectItem v-for="position in TypePosition" :key="position.value" :value="position.value"
                                class="w-75">
                                {{ position.label }}
                            </SelectItem>
                        </SelectContent>
                    </Select>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Contraseña *</FormLabel>
                    <FormControl>
                        <Input type="password" placeholder="XXXXXXXXXX" class="w-75 text-12 font-sans font-light" />
                    </FormControl>
                </div>
            </FormItem>
        </FormField>
    </form>
</template>