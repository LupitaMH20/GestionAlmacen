<script setup lang="ts">
import { FormField, FormItem, FormLabel, FormControl } from '../../ui/form';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../../ui/select'
import { Textarea } from '../../ui/textarea';
import { Label } from '../../ui/label';
import { Input } from '../../ui/input';
import { computed, ref, watch } from 'vue';
import { Eye, X } from 'lucide-vue-next';

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

const pdfPreviewUrl = ref<string | null>(null);
const showPreview = ref(false);

const handleFileChange = (event: Event) => {
    const target = event.target as HTMLInputElement;
    if (target.files && target.files[0]) {
        const file = target.files[0];
        
        // Validate file type
        if (file.type !== 'application/pdf') {
            alert('Por favor, seleccione solo archivos PDF');
            target.value = '';
            selectedFile.value = null;
            return;
        }
        
        selectedFile.value = file;
        
        // Create preview URL
        if (pdfPreviewUrl.value) {
            URL.revokeObjectURL(pdfPreviewUrl.value);
        }
        pdfPreviewUrl.value = URL.createObjectURL(file);
    } else {
        selectedFile.value = null;
        if (pdfPreviewUrl.value) {
            URL.revokeObjectURL(pdfPreviewUrl.value);
            pdfPreviewUrl.value = null;
        }
    }
};

const togglePreview = () => {
    showPreview.value = !showPreview.value;
};

const removeFile = () => {
    selectedFile.value = null;
    if (pdfPreviewUrl.value) {
        URL.revokeObjectURL(pdfPreviewUrl.value);
        pdfPreviewUrl.value = null;
    }
    showPreview.value = false;
    
    // Reset file input
    const fileInput = document.querySelector('input[type="file"]') as HTMLInputElement;
    if (fileInput) {
        fileInput.value = '';
    }
};

// Cleanup on unmount
watch(() => selectedFile.value, (newVal) => {
    if (!newVal && pdfPreviewUrl.value) {
        URL.revokeObjectURL(pdfPreviewUrl.value);
        pdfPreviewUrl.value = null;
        showPreview.value = false;
    }
});
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

        <div class="flex flex-col gap-3">
            <Label>Documento (Evidencia PDF)</Label>
            <Input type="file" 
                accept="application/pdf"
                @change="handleFileChange"
                class="file:text-white file:bg-blue-600 file:hover:bg-blue-700 file:rounded-md" />
            
            <!-- File info and preview controls -->
            <div v-if="selectedFile" class="mt-2 p-3 bg-gray-50 rounded-md border border-gray-200">
                <div class="flex items-center justify-between">
                    <div class="flex items-center gap-2">
                        <span class="text-sm font-medium text-gray-700">{{ selectedFile.name }}</span>
                        <span class="text-xs text-gray-500">({{ (selectedFile.size / 1024).toFixed(2) }} KB)</span>
                    </div>
                    <div class="flex gap-2">
                        <button 
                            type="button"
                            @click="togglePreview"
                            class="px-3 py-1 text-sm bg-green-600 text-white rounded hover:bg-green-700 transition-colors flex items-center gap-1">
                            <Eye class="w-4 h-4" />
                            {{ showPreview ? 'Ocultar' : 'Vista Previa' }}
                        </button>
                        <button 
                            type="button"
                            @click="removeFile"
                            class="px-3 py-1 text-sm bg-red-600 text-white rounded hover:bg-red-700 transition-colors flex items-center gap-1">
                            <X class="w-4 h-4" />
                            Quitar
                        </button>
                    </div>
                </div>
                
                <!-- PDF Preview -->
                <div v-if="showPreview && pdfPreviewUrl" class="mt-3">
                    <iframe 
                        :src="pdfPreviewUrl" 
                        class="w-full h-96 border border-gray-300 rounded"
                        title="Vista previa del PDF">
                    </iframe>
                </div>
            </div>
        </div>
    </div>
</template>