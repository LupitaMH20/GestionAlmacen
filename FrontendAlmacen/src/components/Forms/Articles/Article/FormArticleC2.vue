<script setup lang="ts">
import { FormField, FormItem, FormLabel, FormControl } from '../../../ui/form'
import Input from '../../../ui/input/Input.vue';
import Textarea from '../../../ui/textarea/Textarea.vue';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../../../ui/select'

const props = defineModel('props', { type: Object, required: true })
const props2 = defineProps<{
    companies: Array<{ id_Company: string, name: string }>
    category: Array<{ id_Category: string, name: string }>
}>()
</script>

<template>
    <form>
        <FormField name="Articlename1">
            <FormItem>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Cantidad *</FormLabel>
                    <FormControl>
                        <Input v-model="props.stock" type="number" placeholder="Ingrese la cantidad"
                            class="w-50 font-sans text-12 font-light" />
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Precio *</FormLabel>
                    <FormControl>
                        <Input v-model="props.price" type="number" placeholder="Ingrese el precio"
                            class="w-50 font-sans text-12 font-light" />
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5"> Descripción</FormLabel>
                    <FormControl>
                        <Textarea v-model="props.description" type="text" placeholder="Ingrese una descripción"
                            class="w-50 font-sans text-12 font-light my-3 h-25"></Textarea>
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Categoria *</FormLabel>
                    <Select v-model="props.category">
                        <SelectTrigger class="w-49">
                            <SelectValue placeholder="Seleccione la categoria" class="text-12 font-sans font-light" />
                        </SelectTrigger>
                        <SelectContent>
                            <template v-if="props2.category && props2.category.length > 0">
                                <SelectItem v-for="categories in props2.category" :key="categories.id_Category"
                                    :value="categories.id_Category" class="w-75">
                                    {{ categories.name }}
                                </SelectItem>
                            </template>
                            <template v-else>
                                <div class="p-2 text-center text-sm text-gray-500">
                                    No hay categorías registradas
                                </div>
                            </template>
                        </SelectContent>
                    </Select>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Empresa *</FormLabel>
                    <Select v-model="props.company">
                        <SelectTrigger class="w-49">
                            <SelectValue placeholder="Seleccione la empresa" class="text-12 font-sans font-light" />
                        </SelectTrigger>
                        <SelectContent>
                            <SelectItem v-for="company in props2.companies" :key="company.id_Company"
                                :value="company.id_Company" class="w-75">
                                {{ company.name }}
                            </SelectItem>
                        </SelectContent>
                    </Select>
                </div>
            </FormItem>
        </FormField>
    </form>
</template>