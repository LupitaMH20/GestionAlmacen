<script setup lang="ts">
import {ref, watch, defineExpose} from 'vue'
import axios from 'axios'
import { FormField, FormItem, FormLabel, FormControl } from '../../ui/form'
import Input from '../../ui/input/Input.vue'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../../ui/select'
import { TypePositionC } from '../../data/TypePositionC'

const props = defineProps<{
    collaborator:{
        name: string,
        last_name: string,
        position: string,
        company: string
    },
    company:Array<{
        id_Company: string,
        name: string
    }>
}>()

const name = ref(props.collaborator.name || '')
const last_name = ref(props.collaborator.last_name || '')
const position = ref(props.collaborator.position || '')
const company = ref(props.collaborator.company || '')

watch(() => props.collaborator,(newCollaborator)=>{
    name.value = newCollaborator.name
    last_name.value = newCollaborator.last_name
    position.value = newCollaborator.position
    company.value = newCollaborator.company
}, {immediate:true})

const submitForm = () =>{
    const data: any ={
        name:name.value,
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
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Nombre *</FormLabel>
                    <FormControl>
                        <Input v-model="name" placeholder="nombre" class="w-75 text-12 font-sans font-light" disabled/>
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Apellido *</FormLabel>
                    <FormControl>
                        <Input v-model="last_name" placeholder="apellido" class="w-75 text-12 font-sans font-light" disabled/>
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
                            <SelectValue placeholder="Seleccione el empresa" class="text-12 font-sans font-light" />
                        </SelectTrigger>
                        <SelectContent>
                            <SelectItem v-for="company in props.company" :key="company.id_Company" :value="company.id_Company"
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