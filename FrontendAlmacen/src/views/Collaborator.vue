<script setup lang="ts">
import { Table, TableBody, TableCaption, TableCell, TableHead, TableHeader, TableRow } from '../components/ui/table'
import CreateCollaborator from '../components/Forms/Collaborators/CreateCollaborator.vue';
import UpdateCollaborator from '../components/Forms/Collaborators/UpdateCollaborator.vue';
import DeleteCollaborator from '../components/Forms/Collaborators/DeleteCollaborator.vue';

</script>

<template>
    <div class="flex justify-between items-center w-full text-black font-sans font-bold text-3xl">
        Colaboradores
        <CreateCollaborator />
    </div>
    <Table>
        <TableCaption>Colaboradores registrados.</TableCaption>
        <TableHeader>
            <TableRow>
                <TableHead class="w-[100px]"> ID </TableHead>
                <TableHead>Nombre</TableHead>
                <TableHead>Apellido</TableHead>
                <TableHead>Puesto</TableHead>
                <TableHead class="text-right"> Opciones </TableHead>
            </TableRow>
        </TableHeader>
        <TableBody>
            <TableRow>
                <TableCell class="font-medium"> INV001 </TableCell>
                <TableCell>Heriberto</TableCell>
                <TableCell>XXXXX</TableCell>
                <TableCell>Contador</TableCell>
                <TableCell class="text-right">
                    <div class="flex justify-end item-center gap-20">
                        <UpdateCollaborator />
                        <DeleteCollaborator />
                    </div>
                </TableCell>
            </TableRow>
        </TableBody>
    </Table>
</template>