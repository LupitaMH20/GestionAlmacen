<script setup lang="ts">
import { FormField, FormItem, FormLabel } from '../../../../ui/form';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../../../../ui/select'

// Usar defineModel correctamente para v-model bidireccional
const modelValue = defineModel<{
    requestingCompany: string | number;
    supplierCompany: string | number;
    collaborator: string | number;
    [key: string]: any;
}>({ required: true });

const props = defineProps<{
    companies: Array<{ id_Company: string | number, name: string }>
    collaborator: Array<{ id_Collaborator: string | number, name: string }>
}>();

</script>
<template>
    <form>
        <FormField name="requestingCompany">
            <FormItem>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Empresa Solicitante *</FormLabel>
                    <Select v-model="modelValue.requestingCompany">
                        <SelectTrigger class="w-50">
                            <SelectValue placeholder="Seleccione empresa" class="text-12 font-sans font-light" />
                        </SelectTrigger>
                        <SelectContent>
                            <SelectItem v-for="company in props.companies" :key="company.id_Company"
                                :value="company.id_Company">
                                {{ company.name }}
                            </SelectItem>
                        </SelectContent>
                    </Select>
                </div>
                
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Empresa Proveedora *</FormLabel>
                    <Select v-model="modelValue.supplierCompany">
                        <SelectTrigger class="w-50">
                            <SelectValue placeholder="Seleccione empresa" class="text-12 font-sans font-light" />
                        </SelectTrigger>
                        <SelectContent>
                            <SelectItem v-for="company in props.companies" :key="company.id_Company"
                                :value="company.id_Company">
                                {{ company.name }}
                            </SelectItem>
                        </SelectContent>
                    </Select>
                </div>

                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Colaborador *</FormLabel>
                    <Select v-model="modelValue.collaborator">
                        <SelectTrigger class="w-50">
                            <SelectValue placeholder="Seleccione colaborador" class="text-12 font-sans font-light" />
                        </SelectTrigger>
                        <SelectContent>
                            <SelectItem v-for="collab in props.collaborator" :key="collab.id_Collaborator" 
                                :value="collab.id_Collaborator">
                                {{ collab.name }}
                            </SelectItem>
                        </SelectContent>
                    </Select>
                </div>
            </FormItem>
        </FormField>
    </form>
</template>