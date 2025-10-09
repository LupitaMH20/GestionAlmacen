<script setup lang="ts">
import { Table, TableBody, TableCaption, TableCell, TableHead, TableHeader, TableRow } from '../components/ui/table'
import CreateCompany from '../components/Forms/Companies/CreateCompany.vue';
import UpdateCompany from '../components/Forms/Companies/UpdateCompany.vue';
import DeleteCompany from '../components/Forms/Companies/DeleteCompany.vue';
</script>

<template>
    <div class="flex justify-between items-center w-full text-black font-sans font-bold text-3xl">
        Empresas
        <CreateCompany />
    </div>
    <Table>
        <TableCaption>Empresas registradas.</TableCaption>
        <TableHeader>
            <TableRow>
                <TableHead class="w-[100px]"> ID </TableHead>
                <TableHead>Nombre</TableHead>
                <TableHead>Dirección</TableHead>
                <TableHead class="text-right"> Opciones </TableHead>
            </TableRow>
        </TableHeader>
        <TableBody>
            <TableRow>
                <TableCell class="font-medium"> INV001 </TableCell>
                <TableCell>Refaccionaria JOM</TableCell>
                <TableCell>Calle Fray Servando T. de M. Ote 211, Alto 99070 Fresnillo, Zac.</TableCell>
                <TableCell class="text-right">
                    <div class="flex justify-end item-center gap-20">
                        <UpdateCompany />
                        <DeleteCompany />
                    </div>
                </TableCell>
            </TableRow>
        </TableBody>
    </Table>
</template>