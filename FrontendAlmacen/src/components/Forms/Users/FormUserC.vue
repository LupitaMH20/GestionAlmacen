<script setup lang="ts">
import {ref, defineExpose} from 'vue'
import { FormField, FormItem, FormLabel, FormControl } from '../../ui/form/index.ts'
import Input from '../../ui/input/Input.vue'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../../ui/select/index.ts'
import { TypePosition } from '../../data/TypePosition.ts'
import Checkbox from '../../ui/checkbox/Checkbox.vue'

const id_user = ref('')
const name = ref('')
const last_name = ref('')
const position = ref('')
const password = ref('')
const admin = ref(false)

const submitForm = () => {
  const data = {
    id_user: id_user.value,
    name: name.value,
    last_name: last_name.value,
    position: position.value,
    password: password.value,
    admin: admin.value
  }
  return data  
}
defineExpose({submitForm})

</script>

<template>
    <form>
        <FormField name="Username">
          <FormItem>
            <div class="p-1.5">
              <FormLabel class="text-24 font-sans font-bold p-1.5">ID del Usuario *</FormLabel>
              <FormControl>
                <Input v-model="id_user" placeholder="Ingrese el ID del usuario" class="w-75 text-12 font-sans font-light" />
              </FormControl>
            </div>
            <div class="p-1.5">
              <FormLabel class="text-24 font-sans font-bold p-1.5">Nombre *</FormLabel>
              <FormControl>
                <Input v-model="name" placeholder="Ingrese el nombre" class="w-75 text-12 font-sans font-light" />
              </FormControl>
            </div>
            <div class="p-1.5">
              <FormLabel class="text-24 font-sans font-bold p-1.5">Puesto *</FormLabel>
              <Select v-model="position">
                <SelectTrigger class="w-75">
                  <SelectValue placeholder="Seleccione el puesto" class="text-12 font-sans font-light" />
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
                <Input v-model="password" type="password" placeholder="Ingrese la contraseña" class="w-75 text-12 font-sans font-light" />
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