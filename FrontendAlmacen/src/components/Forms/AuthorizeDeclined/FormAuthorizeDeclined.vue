<script setup lang="ts">
import { FormField, FormItem, FormLabel, FormControl } from '../../ui/form/index.ts'
import Textarea from '../../ui/textarea/Textarea.vue';

const comment = defineModel<string>('comment', { required: true })

</script>

<template>
    <form>
        <FormField name="ArthorizedDeclined">
            <FormItem>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5"> Comentario </FormLabel>
                    <FormControl>
                        <Textarea v-model="comment" type="text" placeholder="Ingrese una comentario"
                            class="w-75 font-sans text-12 font-light my-3 h-25"></Textarea>
                    </FormControl>
                </div>
            </FormItem>
        </FormField>
    </form>
</template>