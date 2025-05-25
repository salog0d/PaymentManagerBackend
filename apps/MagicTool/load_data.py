import os
import django
import csv


from MagicTool.models import Cobro

def cargar_csv(archivo_csv):
    """
    Carga datos desde un archivo CSV a la base de datos
    """
    contador = 0
    errores = 0
    
    print(f"Cargando archivo: {archivo_csv}")
    
    with open(archivo_csv, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            try:
                # Crear cobro
                Cobro.objects.create(
                    id_credito=row["credito"],
                    monto_exigible=float(row['montoExigible']),
                    monto_cobro=float(row['montoCobrar']),
                    monto_cobrado=float(row['montoCobrado']),
                    id_respuesta_banco=row["respuesta_banco"],
                    id_banco=row["banco"],
                    id_lista_cobro=row["lista_cobro"],
                )
                
                contador += 1
                if contador % 100 == 0:
                    print(f"Procesados: {contador}")
                    
            except Exception as e:
                errores += 1
                print(f"Error en fila {contador + errores}: {e}")
    
    print(f"\n=== COMPLETADO ===")
    print(f"Registros cargados: {contador}")
    print(f"Errores: {errores}")

# USO: Cambia la ruta por tu archivo CSV
if __name__ == "__main__":
    archivo = "resources/250_muestras.csv"  # <- CAMBIA ESTA RUTA
    cargar_csv(archivo)