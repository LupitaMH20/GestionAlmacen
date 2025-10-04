<script setup lang="ts">
import { Sidebar, SidebarContent, SidebarFooter, SidebarHeader, SidebarRail, useSidebar } from "@/components/ui/sidebar"
import type { SidebarProps } from "@/components/ui/sidebar"
import { navMainA } from '../data/TypeNavMainA.ts'
import NavMain from "./NavMain.vue"
import NavUser from "./NavUser.vue"
import { computed } from "vue"

const props = withDefaults(defineProps<SidebarProps>(), {
    collapsible: "icon",
})

const data = {
    user: {
        name: "Josue",
        last_name: "Medina",
        position: "Director"
    }
}

const sidebar = useSidebar()
const showHeaderText = computed(() => sidebar.state.value !== 'collapsed')
</script>

<template>
  <Sidebar v-bind="props">
    <SidebarHeader>
      <!-- Aquí usamos la computed -->
      <label v-show="showHeaderText" class="text-[16px] font-sans">Administrador</label>
    </SidebarHeader>

    <SidebarContent>
      <NavMain class="font-sans text-[12px]" :items="navMainA" />
    </SidebarContent>

    <SidebarFooter>
      <NavUser class="font-sans text-[12px]" :user="data.user" />
    </SidebarFooter>

    <SidebarRail />
  </Sidebar>
</template>
