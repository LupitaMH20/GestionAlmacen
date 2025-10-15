<script setup lang="ts">
import {ref, defineExpose} from 'vue'
import { FormField, FormItem, FormLabel, FormControl } from '../../ui/form'
import Input from '../../ui/input/Input.vue'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../../ui/select'
import { TypePositionC } from '../../data/TypePositionC'

const id_Collaborator = ref('')
const name = ref('')
const last_name = ref('')
const position = ref('')
const company = ref('')
const props = defineProps<{
    companies: Array<{id_Company: string, name: string}>
}>()

const submitForm = () => {
    const data = {
        id_Collaborator: id_Collaborator.value,
        name: name.value,
        last_name: last_name.value,
        position: position.value,
        company: company.value
    }
    return data
}

defineExpose({submitForm})
</script>

<template>
    <form>
        <FormField name="Collaboratorname">
            <FormItem>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">ID *</FormLabel>
                    <FormControl>
                        <Input v-model="id_Collaborator" placeholder="Ingrese el ID" class="w-75 text-12 font-sans font-light" />
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Nombre *</FormLabel>
                    <FormControl>
                        <Input v-model="name" placeholder="Ingrese el nombre" class="w-75 text-12 font-sans font-light" />
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Apellido *</FormLabel>
                    <FormControl>
                        <Input v-model="last_name" placeholder="Ingrese el apellido" class="w-75 text-12 font-sans font-light" />
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Puesto *</FormLabel>
                    <Select v-model="position">
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
                    <Select v-model="company">
                        <SelectTrigger class="w-75">
                            <SelectValue placeholder="Seleccione la empresa" class="text-12 font-sans font-light" />
                        </SelectTrigger>
                        <SelectContent>
                            <SelectItem v-for="company in props.companies" :key="company.id_Company" :value="company.id_Company"
                                class="w-75">
                                {{ company.name }}
                            </SelectItem>
                        </SelectContent>
                    </Select>
                </div>
            </FormItem>
        </FormField>
    </form>
</template>