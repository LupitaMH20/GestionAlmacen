import { House, NotebookPen, BookCheck, BookmarkCheck, BookOpenCheck,
    User, UserCog, Building2, FileChartColumnIncreasing, ChartNoAxesCombined, Hammer, ArrowLeftRight} from "lucide-vue-next"
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
    {
        title: "Usuarios",
        url: "/user",
        icon: User,
        isActive: true,
        
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