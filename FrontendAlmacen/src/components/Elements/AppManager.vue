<script setup lang="ts">
import { Sidebar, SidebarContent, SidebarFooter, SidebarHeader, SidebarRail, useSidebar } from "../ui/sidebar"
import type { SidebarProps } from "../ui/sidebar"
import { navMainE } from '../data/TypeNavMainE.ts'
import NavMain from "./NavMain.vue"
import NavUser from "./NavUser.vue"
import { computed, inject } from "vue"
import type { Ref } from 'vue'

interface User {
    id_user: string;
    name: string;
    position: string;
    admin: boolean;
}
const props = withDefaults(defineProps<SidebarProps>(), {
    collapsible: "icon",
})

const loggedInUser = inject<Ref<User | null>>('loggedInUser');

const sidebar = useSidebar()
const showHeaderText = computed(() => sidebar.state.value !== 'collapsed')
</script>

<template>
    <Sidebar v-bind="props">
        <SidebarHeader>
            <label v-show="showHeaderText" class="text-[16px] font-sans">Administrador</label>
        </SidebarHeader>

        <SidebarContent>
            <NavMain class="font-sans font-light text-[12px]" :items="navMainE" />
        </SidebarContent>

        <SidebarFooter>
            <NavUser class="font-sans text-[12px]" :user="loggedInUser" />
        </SidebarFooter>

        <SidebarRail />
    </Sidebar>
</template>
