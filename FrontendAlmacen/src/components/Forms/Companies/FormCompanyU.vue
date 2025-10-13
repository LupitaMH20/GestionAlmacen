<script setup lang="ts">
import {ref, watch,defineExpose, defineProps} from 'vue' 
import { FormControl, FormField, FormItem, FormLabel } from "../../ui/form";
import Input from "../../ui/input/Input.vue";

const props =defineProps<{
    company:{
        id_Company: string,
        name: string,
        address: string
    }
}>()

const id_Company = ref (props.company.id_Company || '')
const name = ref(props.company.name || '')
const address = ref(props.company.address || '')

watch(() => props.company, (newCompany)=>{
    id_Company.value = newCompany.id_Company
    name.value = newCompany.name
    address.value = newCompany.address
},{immediate:true})

const submitForm = () => {
    const data: any ={
        id_Company: id_Company.value,
        name: name.value,
        address: address.value
    }
    return data
}

defineExpose({submitForm})
</script>

<template>
    <form class="pt-5">
        <FormField name="Companyupdate">
            <FormItem>
                <FormLabel class="text-24 font-sans font-bold p-1.5">Nombre *</FormLabel>
                <FormControl>
                    <Input v-model="name" placeholder="nombre" class="w-75 text-12 font-sans font-light" />
                </FormControl>
                <FormLabel class="text-24 font-sans font-bold p-1.5">Dirección *</FormLabel>
                <FormControl>
                    <Input v-model="address" placeholder="dirección" class="w-75 text-12 font-sans  font-light" />
                </FormControl>
            </FormItem>
        </FormField>
    </form>
</template>