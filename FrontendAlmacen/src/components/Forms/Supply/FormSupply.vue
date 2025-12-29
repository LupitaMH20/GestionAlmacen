<script setup lang="ts">
import { FormField, FormItem, FormLabel, FormControl } from '../../ui/form';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../../ui/select'
import { Textarea } from '../../ui/textarea';
import { Label } from '../../ui/label';
import { Input } from '../../ui/input';
import { computed, ref, watch } from 'vue';
import { Eye, X, UploadCloud, CloudUpload } from 'lucide-vue-next';

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

// Helper function to process the selected file
const processFile = (file: File) => {
    // Validate file type
    if (file.type !== 'application/pdf') {
        alert('Por favor, seleccione solo archivos PDF');
        return;
    }
    
    selectedFile.value = file;
    
    // Create preview URL
    if (pdfPreviewUrl.value) {
        URL.revokeObjectURL(pdfPreviewUrl.value);
    }
    pdfPreviewUrl.value = URL.createObjectURL(file);

    // Sync the file input element for consistency, e.g., for form submissions
    const fileInput = document.querySelector('#file-upload') as HTMLInputElement;
    if (fileInput) {
        try {
            const dataTransfer = new DataTransfer();
            dataTransfer.items.add(file);
            fileInput.files = dataTransfer.files;
        } catch (e) {
            console.error("This browser does not support creating a DataTransfer object.", e);
        }
    }
};

const handleFileChange = (event: Event) => {
    const target = event.target as HTMLInputElement;
    if (target.files && target.files[0]) {
        processFile(target.files[0]);
    }
};

const handleDrop = (event: DragEvent) => {
    const files = event.dataTransfer?.files;
    if (files && files[0]) {
        processFile(files[0]);
    }
};

const viewPdfInNewTab = () => {
    if (pdfPreviewUrl.value) {
        window.open(pdfPreviewUrl.value, '_blank');
    }
};

const removeFile = () => {
    selectedFile.value = null;
    if (pdfPreviewUrl.value) {
        URL.revokeObjectURL(pdfPreviewUrl.value);
        pdfPreviewUrl.value = null;
    }
    
    // Reset file input
    const fileInput = document.querySelector('#file-upload') as HTMLInputElement;
    if (fileInput) {
        fileInput.value = '';
    }
};

// Cleanup on unmount
watch(() => selectedFile.value, (newVal) => {
    if (!newVal && pdfPreviewUrl.value) {
        URL.revokeObjectURL(pdfPreviewUrl.value);
        pdfPreviewUrl.value = null;
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

        <div class="flex flex-col gap-2">
            <Label>Documento (Evidencia PDF)</Label>

            <!-- Conditional UI for file upload -->
            <div class="w-full">
                <!-- Show this when NO file is selected -->
                <div v-if="!selectedFile">
                    <label for="file-upload"
                        @dragover.prevent
                        @drop.prevent="handleDrop"
                        class="relative flex flex-col items-center justify-center w-full p-6 border-2 border-dashed rounded-lg cursor-pointer text-gray-500 hover:text-blue-600 hover:border-blue-500 transition-colors">
                        <UploadCloud class="w-10 h-10" />
                        <span class="mt-2 text-sm font-medium">Haz clic o arrastra para subir un archivo</span>
                        <span class="mt-1 text-xs">Solo se permiten archivos PDF</span>
                        <Input id="file-upload" type="file" class="sr-only" accept="application/pdf"
                            @change="handleFileChange" />
                    </label>
                </div>

                <!-- Show this WHEN a file IS selected -->
                <div v-else
                    class="p-3 bg-gray-50 rounded-md border border-gray-200 transition-all">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-3 overflow-hidden">
                            <CloudUpload class="w-8 h-8 text-red-600 flex-shrink-0" />
                            <div class="flex flex-col overflow-hidden">
                                <span class="text-sm font-semibold text-gray-800 truncate" :title="selectedFile.name">
                                    {{ selectedFile.name }}
                                </span>
                                <span class="text-xs text-gray-500">
                                    {{ (selectedFile.size / 1024).toFixed(2) }} KB
                                </span>
                            </div>
                        </div>
                        <div class="flex items-center gap-2 flex-shrink-0 ml-4">
                            <button type="button" @click="viewPdfInNewTab" title="Ver PDF"
                                class="p-2 text-gray-600 bg-gray-200 rounded-full hover:bg-green-200 hover:text-green-800 transition-colors">
                                <Eye class="w-4 h-4" />
                            </button>
                            <button type="button" @click="removeFile" title="Quitar archivo"
                                class="p-2 text-gray-600 bg-gray-200 rounded-full hover:bg-red-200 hover:text-red-800 transition-colors">
                                <X class="w-4 h-4" />
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>