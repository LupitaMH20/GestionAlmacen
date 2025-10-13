<script setup lang="ts">
import type { LucideIcon } from "lucide-vue-next"
import { ChevronRight } from "lucide-vue-next"
import { SidebarGroup, SidebarMenu, SidebarMenuButton, SidebarMenuItem, SidebarMenuSub, SidebarMenuSubButton, SidebarMenuSubItem } from "../ui/sidebar"


defineProps<{
    items: {
        title: string
        icon?: LucideIcon
        isActive?: boolean
        url: string
    }[]
}>()
</script>

<template>
    <SidebarGroup class="p-0">
        <SidebarMenu>
                <SidebarMenuItem v-for="item in items" :key="item.title">
                    <router-link :to="item.url" as-child>
                        <SidebarMenuButton :tooltip="item.title" :data-active="item.isActive" undefined >
                        <component :is="item.icon" v-if="item.icon"/>
                        <span class="font-lingh">{{ item.title }}</span>   
                        <ChevronRight class="ml-auto w-4 h-4" /> 
                        </SidebarMenuButton>
                    </router-link>
                </SidebarMenuItem>
        </SidebarMenu>
    </SidebarGroup>
</template>