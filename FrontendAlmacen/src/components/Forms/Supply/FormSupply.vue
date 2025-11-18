<script setup lang="ts">
import { FormField, FormItem, FormLabel, FormControl } from '../../ui/form';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../../ui/select'
import { Textarea } from '../../ui/textarea';
import { Label } from '../../ui/label';
import { Input } from '../../ui/input';
import { computed } from 'vue';

interface Collaborator {
    id_Collaborator: string;
    name: string;
    last_name: string;
}

const props = defineProps<{
    collaboratorsList: Collaborator[];
    requestType?: string;
}>();

const collaboratorId = defineModel<string | null>('collaboratorId');
const comment = defineModel<string>('comment');
const selectedFile = defineModel<File | null>('selectedFile');
const showDocumentUpload = computed(() => {
    return props.requestType === 'Tool';
});

const handleFileChange = (event: Event) => {
    const target = event.target as HTMLInputElement;
    if (target.files && target.files[0]) {
        selectedFile.value = target.files[0];
    } else {
        selectedFile.value = null;
    }
};
</script>

<template>
    <div class="grid gap-6 py-4">
        <div class="flex flex-col gap-3">
            <Label>Recibe (Colaborador)</Label>
            <Select v-model="collaboratorId">
                <SelectTrigger class="w-75">
                    <SelectValue placeholder="Seleccione un colaborador..."/>
                </SelectTrigger >
                <SelectContent>
                    <SelectItem v-for="colab in props.collaboratorsList" :key="colab.id_Collaborator"
                        :value="colab.id_Collaborator">
                        {{ colab.name }} {{ colab.last_name }}
                    </SelectItem>
                </SelectContent>
            </Select>
        </div>

        <div class="flex flex-col gap-3">
            <Label>Comentario</Label>
            <Textarea v-model="comment" placeholder="Detalles de la entrega..." class="w-75 font-sans text-12 font-light my-3 h-25" :rows="4" />
        </div>

        <div v-if="showDocumentUpload" class="flex flex-col gap-3">
            <Label>Documento (Evidencia)</Label>
            <Input type="file" @change="handleFileChange"
                class="file:text-white file:bg-blue-600 file:hover:bg-blue-700 file:rounded-md" />
        </div>
    </div>
</template>