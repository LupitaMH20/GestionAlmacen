import { House, NotebookPen, BookCheck, BookmarkCheck, BookOpenCheck} from "lucide-vue-next"
    
export const navMainS = [
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
]