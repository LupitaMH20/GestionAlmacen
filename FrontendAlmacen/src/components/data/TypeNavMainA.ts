import {NotebookPen, BookCheck, BookmarkCheck, BookOpenCheck, User, UserCog, Building2, PanelLeftOpen,
    FileChartColumnIncreasing, ChartNoAxesCombined, Hammer, ArrowLeftRight, Boxes, LayoutDashboard, 
    BookOpen, BookOpenText} from "lucide-vue-next"
    
export const navMainA = [
    {
        title: "Dashboard",
        url: "/start",
        icon: LayoutDashboard,
        isActive: true,
    },
    {
        title: "Modulos",
        icon: Boxes,
        isActive: true,
        url: "#",
        items: [
            {
                title: "PreSolicitudes",
                url: "/preApplication",
                icon: BookOpenText,
                isActive: true,
            },
            {
                title: "Solicitudes",
                url: "/application",
                icon: NotebookPen,
                isActive: true,
            },
            {
                title: "Autorizadas",
                url: "/authorize",
                icon: BookCheck,
                isActive: true,
            },
            {
                title: "Surtir",
                url: "/supply",
                icon: BookOpenCheck,
                isActive: true,
            },
            {
                title: "Terminadas",
                url: "/finished",
                icon: BookmarkCheck,
                isActive: true,
            },
            {
                title: "Devoluciones",
                url: "/returns",
                icon: ArrowLeftRight,
                isActive: true,
            },
        ]
    },
    {
        title: "Registros",
        icon: PanelLeftOpen,
        isActive: true,
        url: "#",
        items: [
            {
                title: "Usuarios",
                url: "/user",
                icon: User,
                isActive: true
            },
            {
                title: "Colaboradores",
                url: "/collaborator",
                icon: UserCog,
                isActive: true,
            },
            {
                title: "Empresa",
                url: "/company",
                icon: Building2,
                isActive: true,
            },
            {
                title: "Articulos",
                url: "/articles",
                icon: Hammer,
                isActive: true,
            },
        ]
    },
    {
        title: "Reportes",
        icon: BookOpen,
        isActive: true,
        url: "#",
        items: [
            {
                title: "Reportes",
                url: "/report",
                icon: ChartNoAxesCombined,
                isActive: true,
            },
            {
                title: "Historial",
                url: "/history",
                icon: FileChartColumnIncreasing,
                isActive: true,
            }
        ]
    }
]