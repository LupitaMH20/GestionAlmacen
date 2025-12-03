<script setup lang="ts">
import { ref, watch, defineExpose } from 'vue'
import axios from 'axios'
import { FormField, FormItem, FormLabel, FormControl } from '../../ui/form'
import Input from '../../ui/input/Input.vue'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../../ui/select'
import { TypePositionC } from '../../data/TypePositionC'
import { id } from 'zod/locales'

const props = defineProps<{
    collaborator: {
        id_Collaborator: string,
        name: string,
        last_name: string,
        address: string,
        phone: string,
        position: string,
        company_name: string
    },
    company: Array<{
        id_Company: string,
        name: string
    }>
}>()

const id_Collaborator = ref(props.collaborator.id_Collaborator || '')
const name = ref(props.collaborator.name || '')
const last_name = ref(props.collaborator.last_name || '')
const position = ref(props.collaborator.position || '')
const company = ref(props.collaborator.company_name || '')
const address = ref(props.collaborator.address || '')
const phone = ref(props.collaborator.phone || '')

watch(() => props.collaborator, (newCollaborator) => {
    id_Collaborator.value = newCollaborator.id_Collaborator
    name.value = newCollaborator.name
    last_name.value = newCollaborator.last_name
    position.value = newCollaborator.position
    address.value = newCollaborator.address
    phone.value = newCollaborator.phone
    const found = props.company.find(
        c => c.name === newCollaborator.company_name
    )
    company.value = found ? found.id_Company : ''
}, { immediate: true })

const submitForm = () => {
    const data: any = {
        id_Collaborator: props.collaborator.id_Collaborator,
        name: name.value,
        last_name: last_name.value,
        position: position.value,
        address: address.value,
        phone: phone.value,
        company: company.value
    }
    return data
}
defineExpose({ submitForm })
</script>

<template>
    <form>
        <FormField name="Collaboratorname">
            <FormItem>
                <div class="flex justify-center p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">ID *</FormLabel>
                    <FormControl>
                        <Input v-model="props.collaborator.id_Collaborator" placeholder="ID"
                            class="w-50 text-12 font-sans font-light" disabled />
                    </FormControl>
                </div>
                <div class="flex p-1.5">
                    <div class="p-1.5">
                        <FormLabel class="text-24 font-sans font-bold p-1.5">Nombre *</FormLabel>
                        <FormControl>
                            <Input v-model="name" placeholder="nombre" class="w-50 text-12 font-sans font-light" />
                        </FormControl>
                    </div>
                    <div class="p-1.5">
                        <FormLabel class="text-24 font-sans font-bold p-1.5">Apellido *</FormLabel>
                        <FormControl>
                            <Input v-model="last_name" placeholder="apellido"
                                class="w-50 text-12 font-sans font-light" />
                        </FormControl>
                    </div>
                </div>
                <div class="flex p-1.5">
                    <div class="p-1.5">
                        <FormLabel class="text-24 font-sans font-bold p-1.5">Puesto *</FormLabel>
                        <Select v-model="position">
                            <SelectTrigger class="w-50">
                                <SelectValue placeholder="Seleccione el puesto" class="text-12 font-sans font-light" />
                            </SelectTrigger>
                            <SelectContent>
                                <SelectItem v-for="position in TypePositionC" :key="position.value"
                                    :value="position.value" class="w-50">
                                    {{ position.label }}
                                </SelectItem>
                            </SelectContent>
                        </Select>
                    </div>
                    <div class="p-1.5">
                        <FormLabel class="text-24 font-sans font-bold p-1.5">Empresa *</FormLabel>
                        <Select v-model="company">
                            <SelectTrigger class="w-50">
                                <SelectValue placeholder="Seleccione el empresa" class="text-12 font-sans font-light" />
                            </SelectTrigger>
                            <SelectContent>
                                <SelectItem v-for="com in props.company" :key="com.id_Company" :value="com.id_Company"
                                    class="w-50">
                                    {{ com.name }}
                                </SelectItem>
                            </SelectContent>
                        </Select>
                    </div>
                </div>
                <div class="flex p-1.5">
                    <div class="p-1.5">
                        <FormLabel class="text-24 font-sans font-bold p-1.5">Dirección *</FormLabel>
                        <FormControl>
                            <Input v-model="address" placeholder="Ingrese la dirección"
                                class="w-50 text-12 font-sans font-light" />
                        </FormControl>
                    </div>
                    <div class="p-1.5">
                        <FormLabel class="text-24 font-sans font-bold p-1.5">Telefono *</FormLabel>
                        <FormControl>
                            <Input v-model="phone" placeholder="Ingrese el telefono"
                                class="w-50 text-12 font-sans font-light" />
                        </FormControl>
                    </div>
                </div>
            </FormItem>
        </FormField>
    </form>
</template>