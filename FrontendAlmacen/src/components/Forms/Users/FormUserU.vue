<script setup lang="ts">
import { ref, watch, defineExpose, defineProps } from 'vue'
import { FormField, FormItem, FormLabel, FormControl } from '../../ui/form'
import Input from '../../ui/input/Input.vue'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../../ui/select/index.ts'
import { TypePosition } from '../../data/TypePosition.ts'
import Checkbox from '../../ui/checkbox/Checkbox.vue'

const props = defineProps<{
    user: {
        id_user: string
        name: string
        last_name: string
        position: string
        admin: boolean
        password?: string
    }
}>()

const id_user = ref(props.user.id_user || '')
const name = ref(props.user.name || '')
const last_name = ref(props.user.last_name || '')
const position = ref(props.user.position || '')
const admin = ref(props.user.admin || false)
const password = ref('')

watch(() => props.user, (newUser) => {
    id_user.value = newUser.id_user
    name.value = newUser.name
    last_name.value = newUser.last_name
    position.value = newUser.position
    admin.value = newUser.admin
}, { immediate: true })

const submitForm = () => {
    const data: any = {
        id_user: id_user.value,
        name: name.value,
        last_name: last_name.value,
        position: position.value,
        admin: admin.value
    }
    if (password.value) {
        data.password = password.value
    }
    return data
}
defineExpose({ submitForm })
</script>

<template>
    <form>
        <FormField name="UsernameUpdate">
            <FormItem>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">ID del Usuario *</FormLabel>
                    <FormControl>
                        <Input v-model="id_user" placeholder="Ingrese el ID del usuario"
                            class="w-75 text-12 font-sans font-light" readonly />
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Nombre *</FormLabel>
                    <FormControl>
                        <Input v-model="name" class="w-75 text-12 font-sans font-light"/>
                    </FormControl>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Puesto *</FormLabel>
                    <Select v-model="position">
                        <SelectTrigger class="w-75">
                            <SelectValue  class="text-12 font-sans font-light" />
                        </SelectTrigger>
                        <SelectContent>
                            <SelectItem v-for="position in TypePosition" :key="position.value" :value="position.value"
                                class="w-75">
                                {{ position.label }}
                            </SelectItem>
                        </SelectContent>
                    </Select>
                </div>
                <div class="p-1.5">
                    <FormLabel class="text-24 font-sans font-bold p-1.5">Contraseña *</FormLabel>
                    <FormControl>
                        <Input type="password" v-model="password" class="w-75 text-12 font-sans font-light" />
                    </FormControl>
                </div>
                <div class="p-1.5 flex justify-self-center gap-1.5">
                    <Checkbox id="Administrador" v-model="admin"></Checkbox>
                    <FormLabel for="Administrador" class="text-12 font-sans font-bold">Administrador</FormLabel>
                </div>
            </FormItem>
        </FormField>
    </form>
</template>