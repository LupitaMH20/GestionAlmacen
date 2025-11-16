<script setup lang="ts">
import { FormField, FormItem, FormLabel, FormControl } from '../../../../ui/form'
import Input from '../../../../ui/input/Input.vue';
import Textarea from '../../../../ui/textarea/Textarea.vue';
import { NumberField } from '../../../../ui/number-field'

const props = defineModel('props', { type: Object, required: true })

</script>

<template>
    <form>
        <FormField name="Consumablename3">
            <FormItem>
                <div class="p-1.5">
                    <NumberField>
                        <Label class="text-24 font-sans font-bold p-1.5">ID del Producto * </Label>
                        <FormControl>
                            <Input type="text" v-model="props.article" class="w-50 font-sans text-12 font-light" />
                        </FormControl>
                    </NumberField>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5"> Cantidad </FormLabel>
                    <FormControl>
                        <Input type="text" v-model="props.amount" class="w-50 font-sans text-12 font-light"></Input>
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Orden de taller *</FormLabel>
                    <FormControl>
                        <Input type="text" v-model="props.order_workshop" class="w-50 font-sans text-12 font-light" />
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5"> Descripción</FormLabel>
                    <FormControl>
                        <Textarea type="text" v-model="props.description" class="w-50 font-sans text-12 font-light my-3 h-25"></Textarea>
                    </FormControl>
                </div>
            </FormItem>
        </FormField>
    </form>
</template>