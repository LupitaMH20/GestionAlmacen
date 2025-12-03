<script setup lang="ts">
import { ref, watch } from 'vue';
import { FormField, FormItem, FormLabel, FormControl } from '../../../ui/form'
import Input from '../../../ui/input/Input.vue';

const props = defineProps<{
    id_Category: string | number,
    name: string
}>()

const name = ref(props.name || '')

watch(() => props.name, (newCategory) => {
    name.value = newCategory
}, { immediate: true })

const submitForm = () => {
    const data = {
        id_Category: props.id_Category,
        name: name.value   
    }
    return data
}
defineExpose({ submitForm })
</script>

<template>
    <form>
        <FormField name="category">
            <FormItem>
                <div class="flex p-1.5">
                    <FormLabel class="text-24 font-sans font-bold">Ingerese la categoria</FormLabel>
                    <FormControl>
                        <Input v-model="name" class="text-12 font-sans font-light" type="text" placeholder="Ingrese la categorias"></Input>
                    </FormControl>
                </div>
            </FormItem>
        </FormField>
    </form>
</template>