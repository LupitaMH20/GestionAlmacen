<script setup lang="ts">
// 1. IMPORTA 'inject' y 'useRouter'
import { ShieldUser, LogOut, ChevronsUpDown } from 'lucide-vue-next'
import { DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuLabel, DropdownMenuTrigger } from "../ui/dropdown-menu"
import { SidebarMenu, SidebarMenuButton, SidebarMenuItem, useSidebar } from "../ui/sidebar"
import { Avatar, AvatarFallback } from '../ui/avatar'
import { inject } from 'vue'
import { useRouter } from 'vue-router'

interface User {
  id_user: string;
  name: string;
  position: string;
  admin: boolean;
}

const positionMap: Record<string, string> = {
    "director": "Director",
    "counter": "Contador",
    "managerJom": "Encargado de JOM",
    "managerNs": "Encargado de NARANJA STORE",
    "managerPrintek": "Encargado PRINTEK",
    "managerHefesto": "Encargado HEFESTO",
    "managerBlackWorkshop": "Encargado BLACK GARAGE",
    "applicant": "Solicitante",
    "deliberystaff": "Personal de entrega"
}

defineProps<{
  user: User | null | undefined
}>()

const { isMobile } = useSidebar()
const logoutAction = inject<Function>('logoutAction')
const router = useRouter()

const handleLogout = () => {
  if (logoutAction) {
    logoutAction()
  }
  router.push('/login')
}
</script>

<template>
  <SidebarMenu v-if="user">
    <SidebarMenuItem>
      <DropdownMenu>
        <DropdownMenuTrigger as-child>
          <SidebarMenuButton
            size="lg"
            class="data-[state=open]:bg-sidebar-accent data-[state=open]:text-sidebar-accent-foreground"
          >
            <Avatar class="h-8 w-8 rounded-lg">
              <AvatarFallback class="rounded-lg">
                <ShieldUser class="size-10" />
              </AvatarFallback>
            </Avatar>
            <div class="grid flex-1 text-left text-sm leading-tight">
              <span class="truncate font-sean">{{ user.name }} </span>
            </div>
            <ChevronsUpDown class="ml-auto size-4" />
          </SidebarMenuButton>
        </DropdownMenuTrigger>

        <DropdownMenuContent
          class="w-[--reka-dropdown-menu-trigger-width] min-w-56 rounded-lg"
          :side="isMobile ? 'bottom' : 'right'"
          align="end"
          :side-offset="4"
        >
          <DropdownMenuLabel class="p-0 font-sans">
            <div class="flex items-center gap-2 px-1 py-1.5 text-left text-sm">
              <Avatar class="h-8 w-8 rounded-lg">
                <AvatarFallback class="rounded-lg">
                  <ShieldUser class="size-6" />
                </AvatarFallback>
              </Avatar>
              <div class="grid flex-1 text-left text-sm leading-tight">
                <span class="truncate font-sans-bold">{{ user.name }} </span>
                <span class="truncate text-xs">{{ positionMap[user.position] || user.position }}</span>
              </div>
            </div>
          </DropdownMenuLabel>

          <DropdownMenuItem @click="handleLogout">
            <LogOut /> Log out
          </DropdownMenuItem>
        </DropdownMenuContent>
      </DropdownMenu>
    </SidebarMenuItem>
  </SidebarMenu>
</template>