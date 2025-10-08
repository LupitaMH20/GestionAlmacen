<script setup lang="ts">
import { FormField, FormItem, FormLabel, FormControl, FormDescription } from '../ui/form';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../ui/select'
import Input from '../ui/input/Input.vue';
import { TypeCompany } from '../data/TypeCompany';


import { ref, onMounted } from 'vue';
interface applicant {
    value: string;
    label: string;
}

const applicants = ref<applicant[]>([]);
const selectedApplicant = ref<string>('');

const loadApplicants = async () => {
    applicants.value = [
        { value: 'USR001', label: 'Rocio Pérez (Producción)' },
        { value: 'USR002', label: 'María Gómez (Almacén)' },
        { value: 'USR003', label: 'Luis Castro (Ventas)' },
    ];
};

interface collaborator {
    value: string;
    label: string;
}

const collaborators = ref<collaborator[]>([]);
const selectedcollaborator = ref<string>('');

const loadcollaborators = async () => {
    collaborators.value = [
        { value: 'USR001', label: 'Rocio Pérez (Producción)' },
        { value: 'USR002', label: 'María Gómez (Almacén)' },
        { value: 'USR003', label: 'Luis Castro (Ventas)' },
    ];
};

onMounted(() => {
    loadApplicants();
});

</script>

<template>
    <form>
        <FormField name="Consumablename1">
            <FormItem>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Empresa Solicitante *</FormLabel>
                    <Select>
                        <SelectTrigger class="w-50">
                            <SelectValue placeholder="Seleccionar empresa" class="text-12 font-sans font-light" />
                        </SelectTrigger>
                        <SelectContent>
                            <SelectItem v-for="company in TypeCompany" :key="company.value" :value="company.value"
                                class="w-50">
                                {{ company.label }}
                            </SelectItem>
                        </SelectContent>
                    </Select>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Empresa Proveedora *</FormLabel>
                    <Select>
                        <SelectTrigger class="w-50">
                            <SelectValue placeholder="Seleccionar empresa" class="text-12 font-sans font-light" />
                        </SelectTrigger>
                        <SelectContent>
                            <SelectItem v-for="company in TypeCompany" :key="company.value" :value="company.value"
                                class="w-50">
                                {{ company.label }}
                            </SelectItem>
                        </SelectContent>
                    </Select>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Colaborador *</FormLabel>
                    <Select v-model="selectedcollaborator">
                        <SelectTrigger class="w-50">
                            <SelectValue placeholder="Seleccionar " class="text-12 font-sans font-light" />
                        </SelectTrigger>
                        <SelectContent>
                            <SelectItem v-for="collaborator in collaborators" :key="collaborator.value" :value="collaborator.value"
                                class="w-50">
                                {{ collaborator.label }}
                            </SelectItem>
                        </SelectContent>
                    </Select>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Solicitante *</FormLabel>
                    <Select v-model="selectedApplicant">
                        <SelectTrigger class="w-50">
                            <SelectValue placeholder="Seleccionar solicitante" class="text-12 font-sans font-light" />
                        </SelectTrigger>
                        <SelectContent>
                            <SelectItem v-for="applicant in applicants" :key="applicant.value" :value="applicant.value"
                                class="w-50">
                                {{ applicant.label }}
                            </SelectItem>
                        </SelectContent>
                    </Select>
                </div>  
            </FormItem>
        </FormField>
    </form>
</template>