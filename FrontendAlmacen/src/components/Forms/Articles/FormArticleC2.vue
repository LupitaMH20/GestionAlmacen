<script setup lang="ts">
import { FormField, FormItem, FormLabel, FormControl } from '../../ui/form'
import Input from '../../ui/input/Input.vue';
import Textarea from '../../ui/textarea/Textarea.vue';
import { NumberField, NumberFieldContent, NumberFieldDecrement, NumberFieldInput, NumberFieldIncrement } from '../../ui/number-field'

</script>

<template>
    <form>
        <FormField name="Articlename1">
            <FormItem>
                <div class="p-1.5">
                    <NumberField>
                        <Label class="text-24 font-sans font-bold p-1.5">Cantidad *</Label>
                        <NumberFieldContent>
                            <NumberFieldDecrement />
                            <NumberFieldInput class="w-50 font-sans text-12 font-light" />
                            <NumberFieldIncrement />
                        </NumberFieldContent>
                    </NumberField>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Precio *</FormLabel>
                    <FormControl>
                        <Input type="number" placeholder="Ingrese el precio" class="w-50 font-sans text-12 font-light" />
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5"> Descripción</FormLabel>
                    <FormControl>
                        <Textarea type="text" placeholder="Ingrese una descripción" class="w-50 font-sans text-12 font-light"></Textarea>
                    </FormControl>
                </div>
            </FormItem>
        </FormField>
    </form>
</template>