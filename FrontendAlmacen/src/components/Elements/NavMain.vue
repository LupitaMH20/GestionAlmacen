<script setup lang="ts">
import type { LucideIcon } from "lucide-vue-next"
import { ChevronRight } from "lucide-vue-next"
import { SidebarGroup, SidebarMenu, SidebarMenuButton, SidebarMenuItem, SidebarMenuSub, SidebarMenuSubButton, SidebarMenuSubItem } from "../ui/sidebar"
import { Collapsible, CollapsibleContent, CollapsibleTrigger } from "../ui/collapsible"

defineProps<{
    items: {
        title: string
        routerName: string
        icon?: LucideIcon
        isActive?: boolean
        items?: {
            title: string
            routerName: string
            icon?: LucideIcon
            isActive?: boolean
        }[]
    }[]
}>()
</script>

<template>
    <SidebarGroup class="p-0">
        <SidebarMenu>
            <SidebarMenuItem v-for="item in items" :key="item.title">
                <template v-if="!item.items || item.items.length === 0">
                    <SidebarMenuButton as-child :tooltip="item.title">
                        <router-link :to="item.routerName" class="flex items-center gap-2 w-full">
                            <component :is="item.icon" v-if="item.icon" />
                            <span>{{ item.title }}</span>
                        </router-link>
                    </SidebarMenuButton>
                </template>

                <template v-else>
                    <Collapsible as-child :default-open="item.isActive" class="group/collapsible">
                        <div>
                            <CollapsibleTrigger as-child>
                                <SidebarMenuButton :tooltip="item.title">
                                    <component :is="item.icon" v-if="item.icon" />
                                    <span>{{ item.title }}</span>
                                    <ChevronRight
                                        class="ml-auto w-4 h-4 transition-transform duration-200 group-data-[state=open]/collapsible:rotate-90" />
                                </SidebarMenuButton>
                            </CollapsibleTrigger>

                            <CollapsibleContent>
                                <SidebarMenuSub>
                                    <SidebarMenuSubItem v-for="subItem in item.items" :key="subItem.title">
                                        <SidebarMenuSubButton as-child>
                                            <router-link :to="subItem.routerName" class="flex items-center gap-2">
                                                <component :is="subItem.icon" v-if="subItem.icon" />
                                                <span>{{ subItem.title }}</span>
                                            </router-link>
                                        </SidebarMenuSubButton>
                                    </SidebarMenuSubItem>
                                </SidebarMenuSub>
                            </CollapsibleContent>
                        </div>
                    </Collapsible>
                </template>
            </SidebarMenuItem>
        </SidebarMenu>
    </SidebarGroup>
</template>