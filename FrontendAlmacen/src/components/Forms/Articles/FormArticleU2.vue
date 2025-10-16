<script setup lang="ts">
import { FormField, FormItem, FormLabel, FormControl } from '../../ui/form'
import Input from '../../ui/input/Input.vue';
import Textarea from '../../ui/textarea/Textarea.vue';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../../ui/select'

const props = defineModel('props', { type: Object, required: true })
const props2 = defineProps<{ companies: Array<{id_Company:string, name:string}> }>()
</script>

<template>
    <form>
        <FormField name="articlename">
            <FormItem>
                <div class="p-1.5">
                    <FormLabel>Cantidad *</FormLabel>
                    <FormControl>
                        <Input v-model="props.stock" type="number"/>
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel>Precio *</FormLabel>
                    <FormControl>
                        <Input v-model="props.price" type="number"/>
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel>Descripción</FormLabel>
                    <FormControl>
                        <Textarea v-model="props.description"/>
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel>Categoria *</FormLabel>
                    <FormControl>
                        <Input v-model="props.category" type="text"/>
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel>Empresa *</FormLabel>
                    <Select v-model=" props2.companies">
                        <SelectTrigger>
                            <SelectValue placeholder="Seleccione la empresa" />
                        </SelectTrigger>
                        <SelectContent>
                            <SelectItem v-for="company in props2.companies" :key="company.id_Company" :value="company.id_Company">
                                {{ company.name }}
                            </SelectItem>
                        </SelectContent>
                    </Select>
                </div>
            </FormItem>
        </FormField>
    </form>
</template>
