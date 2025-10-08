<script setup lang="ts">
import type { LucideIcon } from "lucide-vue-next"
import { ChevronRight } from "lucide-vue-next"
import { Collapsible, CollapsibleContent, CollapsibleTrigger } from "../ui/collapsible"
import { SidebarGroup, SidebarMenu, SidebarMenuButton, SidebarMenuItem, SidebarMenuSub, SidebarMenuSubButton, SidebarMenuSubItem } from "../ui/sidebar"
import { navMainA } from '../data/TypeNavMainA';

defineProps<{
    items: {
        title: string
        icon?: LucideIcon
        isActive?: boolean
        items?: {
            title: string
            url: string
            icon?: LucideIcon
        }[]
    }[]
}>()
</script>

<template>
    <SidebarGroup>
        <SidebarMenu>
            <Collapsible v-for="item in items" :key="item.title" as-child :default-open="item.isActive"
                class="group/collapsible">
                <SidebarMenuItem>
                    <CollapsibleTrigger as-child>
                        <SidebarMenuButton :tooltip="item.title">
                            <component :is="item.icon" v-if="item.icon" />
                            <span>{{ item.title }}</span>
                            <ChevronRight class="ml-auto" />
                        </SidebarMenuButton>
                    </CollapsibleTrigger>
                    <CollapsibleContent>
                        <SidebarMenuSub>
                            <SidebarMenuSubItem v-for="subItem in item.items" :key="subItem.title">
                                <SidebarMenuSubButton as-child>
                                    <router-link v-for="item in navMainA" :key="item.title" :to="item.url"
                                        class="flex items-center p-2 rounded-lg hover:bg-gray-100">
                                        <component :is="item.icon" class="w-5 h-5 mr-3" />
                                        <span>{{ item.title }}</span>
                                    </router-link>
                                </SidebarMenuSubButton>
                            </SidebarMenuSubItem>
                        </SidebarMenuSub>
                    </CollapsibleContent>
                </SidebarMenuItem>
            </Collapsible>
        </SidebarMenu>
    </SidebarGroup>
</template>