<script setup lang="ts">
import { FormField, FormItem, FormLabel, FormControl } from '../../ui/form'
import Input from '../../ui/input/Input.vue'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../../ui/select'
import { TypePositionC } from '../../data/TypePositionC'
import { TypeCompany } from '../../data/TypeCompany'
</script>

<template>
    <form>
        <FormField name="Collaboratorname">
            <FormItem>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Nombre *</FormLabel>
                    <FormControl>
                        <Input placeholder="Ingrese el nombre" class="w-75 text-12 font-sans font-light" />
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Apellido *</FormLabel>
                    <FormControl>
                        <Input placeholder="Ingrese el apellido" class="w-75 text-12 font-sans font-light" />
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Puesto *</FormLabel>
                    <Select>
                        <SelectTrigger class="w-75">
                            <SelectValue placeholder="Seleccione el puesto" class="text-12 font-sans font-light" />
                        </SelectTrigger>
                        <SelectContent>
                            <SelectItem v-for="position in TypePositionC" :key="position.value" :value="position.value"
                                class="w-75">
                                {{ position.label }}
                            </SelectItem>
                        </SelectContent>
                    </Select>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Empresa *</FormLabel>
                    <Select>
                        <SelectTrigger class="w-75">
                            <SelectValue placeholder="Seleccione el puesto" class="text-12 font-sans font-light" />
                        </SelectTrigger>
                        <SelectContent>
                            <SelectItem v-for="company in TypeCompany" :key="company.value" :value="company.value"
                                class="w-75">
                                {{ company.label }}
                            </SelectItem>
                        </SelectContent>
                    </Select>
                </div>
            </FormItem>
        </FormField>
    </form>
</template>