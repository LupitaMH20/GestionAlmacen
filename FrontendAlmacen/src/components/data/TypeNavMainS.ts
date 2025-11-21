import { NotebookPen, BookCheck, BookmarkCheck, BookOpenCheck, ArrowLeftRight, Boxes, LayoutDashboard, BookOpenText} from "lucide-vue-next"
    
export const navMainS = [
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
        ]
    },
]