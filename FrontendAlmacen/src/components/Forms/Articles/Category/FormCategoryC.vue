<script setup lang="ts">
import { ref, defineExpose } from 'vue';
import { FormField, FormItem, FormLabel, FormControl } from '../../../ui/form'
import Input from '../../../ui/input/Input.vue';

const name = ref('')

const submitForm = () => {
    const data = {
        name: name.value   
    }
    return data
}

defineExpose({submitForm})
</script>

<template>
    <form>
        <FormField name="category">
            <FormItem>
                <div class="flex flex-col gap-2 p-1.5">
                    <FormLabel class="text-24 font-sans font-bold">Ingerese la nueva categoria</FormLabel>
                    <FormControl>
                        <Input v-model="name" class="text-12 font-sans font-light" type="text" placeholder="Ingrese la categoria"></Input>
                    </FormControl>
                </div>
            </FormItem>
        </FormField>
    </form>
</template>