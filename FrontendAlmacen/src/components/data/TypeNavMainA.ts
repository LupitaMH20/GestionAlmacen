import {NotebookPen, BookCheck, BookmarkCheck, BookOpenCheck, User, UserCog, Building2, PanelLeftOpen,
    FileChartColumnIncreasing, ChartNoAxesCombined, Hammer, ArrowLeftRight, Boxes, LayoutDashboard, 
    BookOpen, BookOpenText} from "lucide-vue-next"
    
export const navMainA = [
    {
        title: "Dashboard",
        routerName: "start",
        icon: LayoutDashboard,
        isActive: true,
    },
    {
        title: "Modulos",
        icon: Boxes,
        routerName: "modules",
        isActive: true,
        items: [
            {
                title: "PreSolicitudes",
                routerName: "preApplication",
                icon: BookOpenText,
                isActive: true,
            },
            {
                title: "Solicitudes",
                routerName: "application",
                icon: NotebookPen,
                isActive: true,
            },
            {
                title: "Autorizadas",
                routerName: "authorize",
                icon: BookCheck,
                isActive: true,
            },
            {
                title: "Entregadas",
                routerName: "supply",
                icon: BookOpenCheck,
                isActive: true,
            },
            {
                title: "Archivadas",
                routerName: "archived",
                icon: BookmarkCheck,
                isActive: true,
            }
        ]
    },
    {
        title: "Registros",
        icon: PanelLeftOpen,
        isActive: true,
        items: [
            {
                title: "Usuarios",
                routerName: "user",
                icon: User,
                isActive: true
            },
            {
                title: "Colaboradores",
                routerName: "collaborator",
                icon: UserCog,
                isActive: true,
            },
            {
                title: "Empresa",
                routerName: "company",
                icon: Building2,
                isActive: true,
            },
            {
                title: "Articulos",
                routerName: "articles",
                icon: Hammer,
                isActive: true,
            },
        ]
    },
    {
        title: "Reportes",
        icon: BookOpen,
        isActive: true,
        items: [
            {
                title: "Reportes",
                routerName: "report",
                icon: ChartNoAxesCombined,
                isActive: true,
            },
            {
                title: "Historial",
                routerName: "history",
                icon: FileChartColumnIncreasing,
                isActive: true,
            }
        ]
    }
]