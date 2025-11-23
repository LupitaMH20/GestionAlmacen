from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db.models import Max
from django.db.models.functions import Now
from application.models import Request
import datetime

class Command(BaseCommand):
    help = 'Archiva solicitudes antiguas con corte exacto a la medianoche'

    def add_arguments(self, parser):
        parser.add_argument(
            '--days',
            type=int,
            default=1,
            help='Archivar solicitudes de hace N días (default: 1 = ayer)'
        )
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Simular sin hacer cambios en la BD'
        )

    def handle(self, *args, **kwargs):
        days_ago = kwargs['days']
        dry_run = kwargs['dry_run']
        
        system_now = timezone.now()

        last_req = Request.objects.aggregate(latest=Max('request_datetime'))
        latest_db_time = last_req['latest']

        if latest_db_time:
            self.stdout.write(f" Último registro en BD: {latest_db_time}")
            
            if system_now < latest_db_time:
                time_diff = latest_db_time - system_now
                self.stdout.write(self.style.ERROR(
                    f"\n{'='*70}\n"
                    f"❌ ERROR CRÍTICO: VIAJE AL PASADO DETECTADO\n"
                    f"\n🛑 PROCESO CANCELADO - Corrige el reloj del servidor\n"
                    f"{'='*70}\n"
                ))
                return
            
            time_ahead = system_now - latest_db_time
            if time_ahead > datetime.timedelta(days=365):
                self.stdout.write(self.style.ERROR(
                    f"\n{'='*70}\n"
                    f"❌ ERROR CRÍTICO: VIAJE AL FUTURO DETECTADO\n"
                    f"\n🛑 PROCESO CANCELADO - Verifica la configuración del servidor\n"
                    f"{'='*70}\n"
                ))
                return
            
            self.stdout.write(self.style.SUCCESS(" Verificación temporal: OK\n"))
        else:
            self.stdout.write(self.style.WARNING(" No hay registros en la base de datos\n"))

        start_of_today = system_now.replace(hour=0, minute=0, second=0, microsecond=0)
        
        target_date = system_now.date() - datetime.timedelta(days=days_ago)
        
        limit_past = system_now.date() - datetime.timedelta(days=60)

        requests_to_archive = Request.objects.filter(
            status='supply',
            acceptance__requestactions__supply__supply_datetime__lt=start_of_today,
            acceptance__requestactions__supply__supply_datetime__date__gte=limit_past,
            acceptance__requestactions__supply__supply_datetime__date__lte=target_date
        ).select_related(
            'user',
            'acceptance__requestactions__supply'
        )

        count = requests_to_archive.count()

        if count > 0:
            self.stdout.write("📦 Solicitudes que se archivarán:\n")
            for req in requests_to_archive[:100]:
                supply = req.acceptance.requestactions.supply
                self.stdout.write(
                    f"  • Request #{req.id_Request}: "
                    f"Surtido el {supply.supply_datetime.strftime('%Y-%m-%d %H:%M:%S')}"
                )
            
            if count > 10:
                self.stdout.write(f"  ... y {count - 10} más\n")
            
            if dry_run:
                self.stdout.write(self.style.WARNING(
                    f"\n DRY RUN: Se archivarían {count} solicitudes (sin cambios en BD)\n"
                ))
            else:
                self.stdout.write(self.style.WARNING(
                    f"\n  ¿Estás seguro de archivar {count} solicitudes?\n"
                ))
                rows = requests_to_archive.update(
                    status='archived',
                    archived_datetime=Now()
                )
                
                self.stdout.write(self.style.SUCCESS(
                    f"\n{'='*70}\n"
                    f" ÉXITO: {rows} solicitudes archivadas\n"
                    f"{'='*70}\n"
                    f"Fecha de archivado: {system_now}\n"
                    f"Solicitudes procesadas: {rows}\n"
                ))
        else:
            self.stdout.write(self.style.WARNING(
                f"\n{'='*70}\n"
                f"  No hay solicitudes para archivar\n"
            ))
        
        stats = {
            'prerequest': Request.objects.filter(status='prerequest').count(),
            'request': Request.objects.filter(status='request').count(),
            'authorized': Request.objects.filter(status='authorized').count(),
            'declined': Request.objects.filter(status='declined').count(),
            'supply': Request.objects.filter(status='supply').count(),
            'archived': Request.objects.filter(status='archived').count(),
        }
        
        for status, count in stats.items():
            self.stdout.write(f"  {status.capitalize():12} : {count:5} solicitudes")
        
        self.stdout.write(f"\n{'='*70}\n")