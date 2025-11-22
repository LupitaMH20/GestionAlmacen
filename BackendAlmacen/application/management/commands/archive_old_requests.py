from django.core.management.base import BaseCommand
from django.utils import timezone
from application.models import Request

class Command(BaseCommand):
    help = 'Archiva automáticamente las solicitudes surtidas el día anterior'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        today_date = now.date()

        print(f"--- Iniciando proceso de archivado: {now} ---")
        
        requests_to_archive = Request.objects.filter(
            status='supply',
            acceptance__requestactions__supply__supply_datetime__date__lt=today_date
        )

        count = requests_to_archive.count()

        if count > 0:
            for req in requests_to_archive:
                req.status = 'archived'
                req.archived_datetime = now
                req.save(update_fields=['status', 'archived_datetime'])
            
            self.stdout.write(self.style.SUCCESS(f'Se archivaron {count} solicitudes correctamente.'))
        else:
            self.stdout.write(self.style.WARNING('No hay solicitudes antiguas para archivar hoy.'))