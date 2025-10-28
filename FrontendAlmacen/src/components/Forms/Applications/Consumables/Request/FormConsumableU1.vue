<script setup lang="ts">
import { FormField, FormItem, FormLabel, FormControl, FormDescription } from '../../../../ui/form';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../../../../ui/select'
import Input from '../../../../ui/input/Input.vue';
import { TypeCompany } from '../../../../data/TypeCompany';

import { ref, onMounted } from 'vue';
interface Manager {
    value: string;
    label: string;
}

const Managers = ref<Manager[]>([]);
const selectedManager = ref<string>('');

const loadManagers = async () => {
    
};

onMounted(() => {
    loadManagers();
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
                            <SelectValue placeholder="Empresa" class="text-12 font-sans font-light" />
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
                            <SelectValue placeholder="Empresa" class="text-12 font-sans font-light" />
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
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Encargado *</FormLabel>
                    <Select v-model="selectedManager">
                        <SelectTrigger class="w-50">
                            <SelectValue placeholder="Seleccionar " class="text-12 font-sans font-light" />
                        </SelectTrigger>
                        <SelectContent>
                            <SelectItem v-for="Manager in Managers" :key="Manager.value" :value="Manager.value"
                                class="w-50">
                                {{ Manager.label }}
                            </SelectItem>
                        </SelectContent>
                    </Select>
                </div>
            </FormItem>
        </FormField>
    </form>
</template>