<script setup lang="ts">
import { Tabs, TabsList, TabsTrigger, TabsContent } from '../ui/tabs'
import { LucideIcon } from 'lucide-vue-next';
import { Box, Axe } from 'lucide-vue-next';
import ViewsArticle from '../../components/Forms/Articles/Article/ViewsArticle.vue'
import ViewsCategory from '../../components/Forms/Articles/Category/ViewsCategory.vue'

</script>

<template>
    <Tabs default-value="article" class="w-full">
        <TabsList class="grid w-full grid-cols-2">
            <TabsTrigger value="article" class="flex items-center gap-2">
                <Axe class="w-5 h-5" /> Artículos
            </TabsTrigger>
            <TabsTrigger value="category" class="flex items-center gap-2">
                <Box class="w-5 h-5" /> Categorías
            </TabsTrigger>
        </TabsList>

        <TabsContent value="article" class="p-4">
            <ViewsArticle />
        </TabsContent>

        <TabsContent value="category" class="p-4">
            <ViewsCategory />
        </TabsContent>
    </Tabs>
</template>