<script setup lang="ts">
import AppManager from "../Elements/AppManager.vue";
import { Breadcrumb, BreadcrumbItem, BreadcrumbLink, BreadcrumbList, BreadcrumbSeparator} from "../../components/ui/breadcrumb"
import { Separator } from "../../components/ui/separator"
import { SidebarInset, SidebarProvider, SidebarTrigger} from "../../components/ui/sidebar"
</script>

<template>
    <SidebarProvider>
        <AppManager />
        <SidebarInset>
            <header
                class="flex h-16 shrink-0 items-center gap-2 transition-[width,height] ease-linear group-has-[[data-collapsible=icon]]/sidebar-wrapper:h-12">
                <div class="flex items-center gap-2 px-4">
                    <SidebarTrigger class="-ml-1" />
                    <Separator orientation="vertical" class="mr-2 h-4" />
                    <Breadcrumb>
                        <BreadcrumbList>
                            <BreadcrumbItem class="hidden md:block">
                                <BreadcrumbLink class="text-2xl" href="/">
                                    Consumo Interno
                                </BreadcrumbLink>
                            </BreadcrumbItem>
                            <BreadcrumbSeparator class="hidden md:block" />
                        </BreadcrumbList>
                    </Breadcrumb>
                </div>
            </header>
            <div class="flex flex-1 flex-col gap-4 p-4 pt-0">
                <router-view />
            </div>
        </SidebarInset>
    </SidebarProvider>
</template>