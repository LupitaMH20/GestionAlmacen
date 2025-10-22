<script setup lang="ts">
import { FormField, FormItem, FormLabel, FormControl, FormDescription } from '../../../ui/form';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../../../ui/select'
import { TypeCompany } from '../../../data/TypeCompany';

import { ref, onMounted } from 'vue';
interface applicant {
    value: string;
    label: string;
}

const applicants = ref<applicant[]>([]);
const selectedApplicant = ref<string>('');


onMounted(() => {
    // loadApplicants();
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