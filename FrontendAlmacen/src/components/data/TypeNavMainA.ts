import { House, NotebookPen, BookCheck, BookmarkCheck, BookOpenCheck,
    User, UserCog, Building2, FileChartColumnIncreasing, ChartNoAxesCombined} from "lucide-vue-next"
    // HardHat, ToolCase, PencilRuler
export const navMainA = [
    {
        title: "Inicio",
        url: "#",
        icon: House,
        isActive: true,
    },
    {
        title: "Soliciitudes",
        url: "#",
        icon: NotebookPen
    },
    {
        title: "Autorizadas",
        url: "#",
        icon: BookCheck
    },
    {
        title: "Surtir",
        url: "#",
        icon: BookOpenCheck
    },
    {
        title: "Entregas",
        url: "#",
        icon: BookmarkCheck
    },
    {
        title: "Usuarios",
        url: "#",
        icon: User,
        isActive: true,
    },
    {
        title: "Empresa",
        url: "#",
        icon: Building2,
        isActive: true,
    },
    {
        title: "Colaboradores",
        url: "#",
        icon: UserCog,
        isActive: true,
    },
    {
        title: "Reportes",
        url: "#",
        icon: ChartNoAxesCombined,
        isActive: true,
    },
    {
        title: "Historial",
        url: "#",
        icon: FileChartColumnIncreasing,
        isActive: true,
    },
]