import { House, NotebookPen, BookCheck, BookmarkCheck, BookOpenCheck,
    User, UserCog, Building2, FileChartColumnIncreasing, ChartNoAxesCombined} from "lucide-vue-next"
    // HardHat, ToolCase, PencilRuler
export const navMainA = [
    {
        title: "Inicio",
        url: "/start",
        icon: House,
        isActive: true,
    },
    {
        title: "Solicitudes",
        url: "/application",
        icon: NotebookPen
    },
    {
        title: "Autorizadas",
        url: "/authorize",
        icon: BookCheck
    },
    {
        title: "Surtir",
        url: "/supply",
        icon: BookOpenCheck
    },
    {
        title: "Entregas",
        url: "/deliveries",
        icon: BookmarkCheck
    },
    {
        title: "Usuarios",
        url: "/user",
        icon: User,
        isActive: true,
    },
    {
        title: "Empresa",
        url: "/Company",
        icon: Building2,
        isActive: true,
    },
    {
        title: "Colaboradores",
        url: "/collaborator",
        icon: UserCog,
        isActive: true,
    },
    {
        title: "Reportes",
        url: "/report",
        icon: ChartNoAxesCombined,
        isActive: true,
    },
    {
        title: "Historial",
        url: "/record",
        icon: FileChartColumnIncreasing,
        isActive: true,
    },
]