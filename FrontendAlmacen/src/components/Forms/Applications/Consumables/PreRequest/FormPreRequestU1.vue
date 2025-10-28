<script setup lang="ts">
import { FormField, FormItem, FormLabel, FormControl, FormDescription } from '../../../../ui/form';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../../../../ui/select'

const props = defineModel('props', { type: Object, required: true })
const props2 = defineProps<{
    companies: Array<{ id_Company: string, name: string }>
    users: Array<{ id_user: string, name: string }>
}>()

</script>
<template>
    <form>
        <FormField name="Consumablename1">
            <FormItem>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Empresa Solicitante *</FormLabel>
                    <Select v-model="props.requestingCompany">
                        <SelectTrigger class="w-50">
                            <SelectValue v-model="props.requestingCompany" class="text-12 font-sans font-light" />
                        </SelectTrigger>
                        <SelectContent>
                            <SelectItem v-for="company in props2.companies" :key="company.id_Company"
                                :value="company.id_Company">
                                {{ company.name }}
                            </SelectItem>
                        </SelectContent>
                    </Select>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Empresa Proveedora *</FormLabel>
                    <Select v-model="props.supplierCompany">
                        <SelectTrigger class="w-50">
                            <SelectValue v-model="props.supplierCompany" class="text-12 font-sans font-light" />
                        </SelectTrigger>
                        <SelectContent>
                            <SelectItem v-for="company in props2.companies" :key="company.id_Company"
                                :value="company.id_Company">
                                {{ company.name }}
                            </SelectItem>
                        </SelectContent>
                    </Select>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Solicitante</FormLabel>
                    <Select v-model="props.applicant">
                        <SelectTrigger class="w-50">
                            <SelectValue v-model="props.applicant" class="text-12 font-sans font-light" />
                        </SelectTrigger>
                        <SelectContent>
                            <SelectItem v-for="user in props2.users" :key="user.id_user" :value="user.id_user">
                                {{ user.name }} ({{ user.id_user }})
                            </SelectItem>
                        </SelectContent>
                    </Select>
                </div>
            </FormItem>
        </FormField>
    </form>
</template>