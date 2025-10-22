<script setup lang="ts">
import { FormField, FormItem, FormLabel, FormControl } from '../../ui/form'
import Textarea from '../../ui/textarea/Textarea.vue';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../../ui/select/index.ts'
import { TypeAuthorize } from '../../data/TypeAuthorize.ts'
import { ref, onMounted } from 'vue';
interface manager {
    value: string;
    label: string;
}

const managers = ref<manager[]>([]);
const selectedmanager = ref<string>('');

</script>

<template>
    <form>
        <FormField name="Articlename1">
            <FormItem>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Puesto *</FormLabel>
                    <Select>
                        <SelectTrigger class="w-75">
                            <SelectValue placeholder="Seleccione el puesto" class="text-12 font-sans font-light" />
                        </SelectTrigger>
                        <SelectContent>
                            <SelectItem v-for="authorize in TypeAuthorize" :key="authorize.value" :value="authorize.value"
                                class="w-75">
                                {{ authorize.label }}
                            </SelectItem>
                        </SelectContent>
                    </Select>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Nombre *</FormLabel>
                    <Select v-model="selectedmanager">
                        <SelectTrigger class="w-75">
                            <SelectValue placeholder="Nombre" class="text-12 font-sans font-light" />
                        </SelectTrigger>
                        <SelectContent>
                            <SelectItem v-for="manager in managers" :key="manager.value" :value="manager.value"
                                class="w-75">
                                {{ manager.label }}
                            </SelectItem>
                        </SelectContent>
                    </Select>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5"> Comentario </FormLabel>
                    <FormControl>
                        <Textarea type="text" placeholder="Ingrese una comentario" class="w-75 font-sans text-12 font-light"></Textarea>
                    </FormControl>
                </div>
            </FormItem>
        </FormField>
    </form>
</template>