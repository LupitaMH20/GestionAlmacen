<script setup lang="ts">
import { ref, defineExpose } from 'vue';
import { FormField, FormItem, FormLabel, FormControl } from '../../../ui/form'
import Input from '../../../ui/input/Input.vue';

const props = defineModel('props', { type: Object, required: true })
</script>

<template>
    <form>
        <FormField name="category">
            <FormItem>
                <div class="flex p-1.5">
                    <FormLabel class="text-24 font-sans font-bold">Ingerese la categoria</FormLabel>
                    <FormControl>
                        <Input v-model="props.name" class="text-12 font-sans font-light" type="text" placeholder="Ingrese la categorias"></Input>
                    </FormControl>
                </div>
            </FormItem>
        </FormField>
    </form>
</template>