<script setup lang="ts">
import { Table, TableBody, TableCaption, TableCell, TableHead, TableHeader, TableRow } from '../components/ui/table'
import ArticleCreate from '../components/Forms/Articles/CreateArticle.vue';
import ArticleUpdate from '../components/Forms/Articles/UpdateArticle.vue';
import DeleteArticle from '../components/Forms/Articles/DeleteArticle.vue';
</script>

<template>
    <div class="flex justify-between items-center w-full text-black font-sans font-bold text-3xl">
        Articulos
        <ArticleCreate />
    </div>
    <Table>
        <TableCaption>Articulos registrados.</TableCaption>
        <TableHeader>
            <TableRow>
                <TableHead class="w-[100px]"> ID Principal</TableHead>
                <TableHead class="w-[100px]"> ID Alternativo</TableHead>
                <TableHead>Nombre</TableHead>
                <TableHead>Stock</TableHead>
                <TableHead>Precio</TableHead>
                <TableHead>Descripción</TableHead>
                <TableHead class="text-right"> Opciones </TableHead>
            </TableRow>
        </TableHeader>
        <TableBody>
            <TableRow>
                <TableCell class="font-medium"> INV001 </TableCell>
                <TableCell class="font-medium"> INV002 </TableCell>
                <TableCell>Aceite de Motor</TableCell>
                <TableCell>5</TableCell>
                <TableCell>$150</TableCell>
                <TableCell>Uso para el motor</TableCell>
                <TableCell class="text-right">
                    <div class="flex justify-end item-center gap-20">
                        <ArticleUpdate />
                        <DeleteArticle />
                    </div>
                </TableCell>
            </TableRow>
        </TableBody>
    </Table>
</template>