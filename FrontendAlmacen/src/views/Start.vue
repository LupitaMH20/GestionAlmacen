<script setup lang="ts">
import ProcessCard from '../components/Elements/Card.vue';
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';
import Input from '../components/ui/input/Input.vue'
import Button from '../components/ui/button/Button.vue'
import { Search } from 'lucide-vue-next'
import PreRequestC from '../components/Forms/Applications/Consumables/PreRequest/PreRequest.vue'
import PreRequestCo from '../components/Forms/Applications/PersonalConsumption/PreRequest/PreRequest.vue'
import PreRequestT from '../components/Forms/Applications/Tools/PreRequest/PreRequest.vue'
import { Card, CardContent } from '../components/ui/card';

interface Companies { id_Company: string; name: string }
interface Users { id_user: string; name: string; last_name: string };
interface Collaborators { id_Collaborator: string; name: string; last_name: string };
const searchQuery = ref('');
const selectedType = ref('All')
const displayedProcesses = ref<any[]>([]);

interface ProcessData {
    id_PreRequest: number | string;
    title: string;
    article: string;
    currentStatus: 'Presolicitud' | 'Solicitud' | 'Autorizada' | 'Surtir' | 'Terminada' | 'Cambios_Devoluciones';
    date: string;
    time: string;
    type?: string;
    applicant?: string;
    collaborator?: string;
    applicantName?: Users;
    collaboratorName?: Collaborators;
    description?: string
    amount?: number
    status?: string
    order_workshop?: string
    store?: string
    requestingCompany?: string
    supplierCompany?: string
    requestingCompanyName?: Companies
    supplierCompanyName?: Companies

    position?: string;
}

const allProcesses = ref<ProcessData[]>([]);

const loadProcesses = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/prerequest/');

        const formatDate = (datetime: string) => {
            if (!datetime) return 'Sin fecha';
            const date = new Date(datetime);
            const dia = date.getDate().toString().padStart(2, '0');
            const meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'];
            const mes = meses[date.getMonth()];
            const año = date.getFullYear();
            return `${dia}/${mes}/${año}`;
        };
        allProcesses.value = response.data.map((item: any) => {
            const reqCompanyObj = item.requestingCompany;
            const supCompanyObj = item.supplierCompany;
            const userObj = item.applicant;
            const collabObj = item.collaborator;

            console.log('Procesando item:', userObj);
            return {
                id_PreRequest: item.id_PreRequest,
                title: item.type || 'Sin tipo',
                article: item.article || 'Sin producto',
                currentStatus: item.status === 'prerequest' ? 'Presolicitud' :
                    item.status === 'request' ? 'Solicitud' :
                        item.status === 'authorization' ? 'Autorizada' :
                            item.status === 'deliverie' ? 'Surtir' :
                                item.status === 'deliverie' ? 'Terminada' :
                                    item.status === 'return_exchange' ? 'Cambios_Devoluciones' :
                                        'decline',
                date: formatDate(item.requested_datetime),
                time: new Date(item.requested_datetime).toLocaleTimeString('es-MX', { hour: '2-digit', minute: '2-digit', hour12: true }),
                type: item.type,
                applicant: userObj?.id_user,
                applicantName: userObj,
                collaborator: collabObj?.id_Collaborator,
                collaboratorName: collabObj,
                description: item.description,
                amount: item.amount,
                status: item.status,
                order_workshop: item.order_workshop,
                store: item.store,
                requestingCompany: reqCompanyObj?.id_Company,
                supplierCompany: supCompanyObj?.id_Company,
                requestingCompanyName: reqCompanyObj,
                supplierCompanyName: supCompanyObj,
                position: item.request?.position,
            };
        });
        displayedProcesses.value = [...allProcesses.value];
        console.log('Procesos cargados:', allProcesses.value);
    } catch (error) {
        console.error('Error al cargar procesos:', error);
    }
};

const prerequest = computed(() =>
    displayedProcesses.value.filter(p => p.currentStatus === 'Presolicitud')
);

const applicant = computed(() =>
    displayedProcesses.value.filter(p => p.currentStatus === 'Solicitud')
);

const autorizadas = computed(() =>
    displayedProcesses.value.filter(p => p.currentStatus === 'Autorizada')
);

const SurtirsTerminadas = computed(() =>
    displayedProcesses.value.filter(p => p.currentStatus === 'Surtir' || p.currentStatus === 'Terminada')
);

const searchProcess = () => {
    const query = searchQuery.value.toLowerCase().trim();
    const type = selectedType.value;
    
    let filteredByType = [];
    if (type === 'All') {
        filteredByType = [...allProcesses.value];
    } else {
        filteredByType = allProcesses.value.filter(proc => proc.title === type);
    }
    
    if (!query) {
        displayedProcesses.value = filteredByType;
        return;
    }
    
    displayedProcesses.value = filteredByType.filter(proc => {
        const inId = proc.id_PreRequest.toString().includes(query);
        const inTitle = proc.title.toLowerCase().includes(query);
        const inArticle = proc.article.toLowerCase().includes(query);
        const inApplicant = (
            proc.applicantName?.name.toLowerCase() + ' ' + 
            proc.applicantName?.last_name.toLowerCase()
        ).includes(query);
        const inDescription = proc.description?.toLowerCase().includes(query) || false;
        return inId || inTitle || inArticle || inApplicant || inDescription;
    });
}
onMounted(() => {
    loadProcesses();
});
</script>

<template>
    <div class="p-6">
        <div class="flex justify-between items-center w-full mb-2">
            <div class="flex gap-2">
                <Input v-model="searchQuery" placeholder="Buscar" class="w-75 text-12 font-sans font-light"
                    @input="searchProcess" />
                <Button @click="searchProcess"
                    class="bg-white text-black hover:bg-black hover:text-white border border-gray-300">
                    <Search /> Buscar
                </Button>
            </div>
            <div class="flex gap-5 text-{12px}">
                <p>Buscar por: </p>
                <select v-model="selectedType" @change="searchProcess"
                    class="border border-gray-300 rounded-md text-base font-normal px-3 py-1 focus:outline-none focus:ring-2 focus:bg-white">
                    <option value="All"> Todos </option>
                    <option value="ConsumoPersonal"> Consumo Personal </option>
                    <option value="Consumible"> Consumibles </option>
                    <option value="Herramienta"> Herramientas </option>
                </select>
            </div>
        </div>

        <div class="flex justify-between items-center w-full mb-2 ">
            <div></div>
            <div class="p-3">
                <label class="flex text-{14 px} justify-end">Registro de nuevas: PreSolicitudes</label>
                <div class="flex justify-between items-center p-2 gap-4 ">
                    <PreRequestC @createPreRequest="loadProcesses" />
                    <PreRequestCo @createPreRequest="loadProcesses" />
                    <PreRequestT @createPreRequest="loadProcesses" />
                </div>
            </div>
        </div>

        <Card class="flex flex-col shadow-lg hover:shadow-xl transition-shadow duration-300">
            <CardContent>
                <div class="grid grid-cols-6 h-[65vh] w-full overflow-x-auto gap-50">
                    <section class="bg-gray-50 p-3 rounded-lg min-h-[698vh] min-w-[28vh]">
                        <h2 class="text-xl font-bold mb-4 border-b pb-2 text-blue-400 whitespace-nowrap">
                            Presolicitudes ({{ prerequest.length }})
                        </h2>
                        <div class="flex flex-col space-y-3">
                            <ProcessCard v-for="proc in prerequest" :key="proc.id_PreRequest" v-bind="proc"
                                @updatePreRequest="loadProcesses" />
                            <p v-if="!prerequest.length" class="text-gray-500 text-sm italic mt-4">Sin elementos en esta
                                etapa.</p>
                        </div>
                    </section>

                    <section class="bg-gray-50 p-3 rounded-lg min-h-[698vh] min-w-[28vh]">
                        <h2 class="text-xl font-bold mb-4 border-b pb-2 text-indigo-500 whitespace-nowrap">
                            Solicitud ({{ applicant.length }})
                        </h2>
                        <div class="flex flex-col space-y-3">
                            <ProcessCard v-for="proc in applicant" :key="proc.id_PreRequest" v-bind="proc" />
                            <p v-if="!applicant.length" class="text-gray-500 text-sm italic mt-4">Sin elementos en esta
                                etapa.</p>
                        </div>
                    </section>

                    <section class="bg-gray-50 p-3 rounded-lg min-h-[698vh] min-w-[28vh]">
                        <h2 class="text-xl font-bold mb-4 border-b pb-2 text-indigo-700 whitespace-nowrap">
                            Autorizadas ({{ autorizadas.length }})
                        </h2>

                        <div class="flex flex-col space-y-3">
                            <ProcessCard v-for="proc in autorizadas" :key="proc.id_PreRequest" v-bind="proc" />
                            <p v-if="!autorizadas.length" class="text-gray-500 text-sm italic mt-4">Sin elementos en
                                esta etapa.
                            </p>
                        </div>
                    </section>

                    <section class="bg-gray-50 p-3 rounded-lg min-h-[698vh] min-w-[28vh]">
                        <h2 class="text-xl font-bold mb-4 border-b pb-2 text-green-600 whitespace-nowrap">
                            Surtir ({{SurtirsTerminadas.filter(p => p.currentStatus === 'Surtir').length}})
                        </h2>

                        <div class="flex flex-col space-y-3">
                            <ProcessCard v-for="proc in SurtirsTerminadas.filter(p => p.currentStatus === 'Surtir')"
                                :key="proc.id_PreRequest" v-bind="proc" />
                            <p v-if="!SurtirsTerminadas.filter(p => p.currentStatus === 'Surtir').length"
                                class="text-gray-500 text-sm italic mt-4">Sin elementos en esta etapa.</p>
                        </div>
                    </section>

                    <section class="bg-gray-50 p-3 rounded-lg min-h-[698vh] min-w-[28vh]">
                        <h2 class="text-xl font-bold mb-4 border-b pb-2 text-gray-700 whitespace-nowrap">
                            Terminadas ({{SurtirsTerminadas.filter(p => p.currentStatus === 'Terminada').length}})
                        </h2>

                        <div class="flex flex-col space-y-3">
                            <ProcessCard v-for="proc in SurtirsTerminadas.filter(p => p.currentStatus === 'Terminada')"
                                :key="proc.id_PreRequest" v-bind="proc" />
                            <p v-if="!SurtirsTerminadas.filter(p => p.currentStatus === 'Terminada').length"
                                class="text-gray-500 text-sm italic mt-4">Sin elementos en esta etapa.</p>
                        </div>
                    </section>

                    <section class="bg-gray-50 p-3 rounded-lg min-h-[500px] min-w-[28vh]">
                        <h2 class="text-xl font-bold mb-4 border-b pb-2 text-gray-500 whitespace-nowrap">
                            Archivada ({{SurtirsTerminadas.filter(p => p.currentStatus === 'Surtir').length}})
                        </h2>

                        <div class="flex flex-col space-y-3">
                            <ProcessCard v-for="proc in SurtirsTerminadas.filter(p => p.currentStatus === 'Surtir')"
                                :key="proc.id_PreRequest" v-bind="proc" />
                            <p v-if="!SurtirsTerminadas.filter(p => p.currentStatus === 'Surtir').length"
                                class="text-gray-500 text-sm italic mt-4">Sin elementos en esta etapa.</p>
                        </div>
                    </section>
                </div>
            </CardContent>
        </Card>
    </div>
</template>