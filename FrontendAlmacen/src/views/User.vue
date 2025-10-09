<script setup lang="ts">
import { Table, TableBody, TableCaption, TableCell, TableHead, TableHeader, TableRow } from '../components/ui/table'
import CreateUser from '../components/Forms/Users/CreateUser.vue'
import UpdateUser from '../components/Forms/Users/UpdateUser.vue'
import DeleteUser from '../components/Forms/Users/DeleteUser.vue'
</script>

<template>
    <div class="flex justify-between items-center w-full text-black font-sans font-bold text-3xl">
        Usuarios
        <CreateUser />
    </div>
    <Table>
        <TableCaption>Usuarios registrados.</TableCaption>
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
                <TableCell>Josue</TableCell>
                <TableCell>Medina</TableCell>
                <TableCell>Director</TableCell>
                <TableCell class="text-right">
                    <div class="flex justify-end item-center gap-20">
                        <UpdateUser />
                        <DeleteUser />
                    </div>
                </TableCell>
            </TableRow>
        </TableBody>
    </Table>
</template>