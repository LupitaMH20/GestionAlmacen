<script setup lang="ts">
import axios from 'axios';
import DeleteApplicant from '../../../../Elements/DeleteApplicant.vue'

const emit = defineEmits(['deletePreRequest']);
const props = defineProps<{
    id_Request: number | string;
}>();

const handelDelete = async() => {
    try{
    await axios.delete(`http://127.0.0.1:8000/api/prerequest/${props.id_Request}/`)
    console.log('Presolicitud eliminada con exito');
    emit('deletePreRequest');
    } catch (error) {
        console.log('Error al eliminar la presolicitud')
    }
};
</script>

<template>
    <DeleteApplicant @deletePreRequest="handelDelete"/>
</template>