from django.core.management.base import BaseCommand
import csv
from apps.MagicTool.models import Cobro  # Asegúrate de que la ruta sea correcta 

class Command(BaseCommand):
    help = 'Importa cobros desde un archivo CSV'

    def add_arguments(self, parser):
        parser.add_argument('archivo_csv', type=str)

    def handle(self, *args, **options):
        archivo = options['archivo_csv']
        with open(archivo, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Cobro.objects.create(
                    id_credito=row['idCredito'],
                    monto_exigible=row['montoExigible'],
                    monto_cobro=row['montoCobrar'],
                    monto_cobrado=row['montoCobrado'],
                    id_respuesta_banco=row['idRespuestaBanco'],
                    id_banco=row['idBanco'],
                    id_lista_cobro=row['idListaCobro'],
                )
        self.stdout.write(self.style.SUCCESS('Importación completada'))
