<script setup lang="ts">
import { FormField, FormItem, FormLabel, FormControl } from '../../../ui/form'
import Input from '../../../ui/input/Input.vue';
import Textarea from '../../../ui/textarea/Textarea.vue';
import { NumberField, NumberFieldContent, NumberFieldDecrement, NumberFieldInput, NumberFieldIncrement } from '../../../ui/number-field'

</script>

<template>
    <form>
        <FormField name="Consumablename3">
            <FormItem>
                <div class="p-1.5">
                    <NumberField>
                        <Label class="text-24 font-sans font-bold p-1.5">Nombre ó ID *</Label>
                        <FormControl>
                        <Input type="text" placeholder="Nombre ó ID" class="w-50 font-sans text-12 font-light" />
                    </FormControl>
                    </NumberField>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Orden de taller *</FormLabel>
                    <FormControl>
                        <Input type="text" placeholder="Orden de taller" class="w-50 font-sans text-12 font-light" />
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5"> Descripción</FormLabel>
                    <FormControl>
                        <Textarea type="text" placeholder="Descripción" class="w-50 font-sans text-12 font-light"></Textarea>
                    </FormControl>
                </div>
            </FormItem>
        </FormField>
    </form>
</template>