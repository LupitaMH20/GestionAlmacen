<script setup lang="ts">
import { Sidebar, SidebarContent, SidebarFooter, SidebarHeader, SidebarRail, useSidebar } from "../ui/sidebar"
import type { SidebarProps } from "../ui/sidebar"
import { navMainS } from "../data/TypeNavMainS.ts"
import NavMain from "./NavMain.vue"
import NavUser from "./NavUser.vue"
import { computed } from "vue"

const props = withDefaults(defineProps<SidebarProps>(), {
    collapsible: "icon",
})

const data = {
    user: {
        name: "",
        last_name: "",
        position: "Encargado"
    }
}

const sidebar = useSidebar()
const showHeaderText = computed(() => sidebar.state.value !== 'collapsed')
</script>

<template>
  <Sidebar v-bind="props">
    <SidebarHeader>
      <!-- Aquí usamos la computed -->
      <label v-show="showHeaderText" class="text-[16px] font-sans">Personal</label>
    </SidebarHeader>

    <SidebarContent>
      <NavMain class="text-[16px] font-sans"n :items="navMainS" />
    </SidebarContent>

    <SidebarFooter>
      <NavUser class="text-[16px] font-sans" :user="data.user" />
    </SidebarFooter>

    <SidebarRail />
  </Sidebar>
</template>
