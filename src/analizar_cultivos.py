import csv
import os

def leer_cultivos(ruta_archivo):
    """Lee un archivo CSV de cultivos y retorna una lista de diccionarios."""
    cultivos=[]
    try:
        with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
            lector=csv.DictReader(archivo)
            for fila in lector:
                cultivo={
                    "nombre": fila["nombre"],
                    "hectareas": float(fila["hectareas"]),
                    "produccion_toneladas": float(fila["produccion_toneladas"])
                }
                cultivos.append(cultivo)
            return cultivos

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta '{ruta_archivo}'")
        return []
    except Exception as e:
        print(f"Error inesperado al procesar el archivo: {e}")
        return []

def calcular_estadisticas(cultivos):
    """Calcula estadísticas integrales sobre la lista de diccionarios de cultivos."""
    if not cultivos:
        return None

    # Calcular estadísticas
    total_hectareas=sum(c["hectareas"] for c in cultivos)
    total_produccion=sum(c["produccion_toneladas"] for c in cultivos)
    promedio_rendimiento=total_produccion/total_hectareas if total_hectareas>0 else 0

    #Obtener el cultivo con mayor y menor producción
    mayor=max(cultivos, key=lambda c: c["produccion_toneladas"])
    menor=min(cultivos, key=lambda c: c["produccion_toneladas"])

    return{
        "total_hectareas": total_hectareas,
        "total_produccion": total_produccion,
        "promedio_rendimiento": promedio_rendimiento,
        "cultivo_mayor": mayor["nombre"],
        "produccion_mayor": mayor["produccion_toneladas"],
        "cultivo_menor": menor["nombre"],
        "produccion_menor": menor["produccion_toneladas"]
    }

def generar_informe(estadisticas, ruta_salida):
    """Generar un archivo de informe en formato Markdown (.md) con los resultados"""
    if not estadisticas:
        print("No hay estadísticas para generar el informe.")
        return

    with open (ruta_salida, mode="w", encoding="utf-8") as archivo:
        archivo.write("# Informe de Cultivos en Cartago\n\n")
        archivo.write("Este informe ha sido generado automáticamente a partir del archivo de datos CSV.\n\n")
        archivo.write("## Resumen Estadístico\n\n")
        archivo.write(f"- **Total de hectáreas cultivadas:** {estadisticas['total_hectareas']:.2f} ha\n")
        archivo.write(f"- **Total de producción:** {estadisticas['total_produccion']:.2f} toneladas\n")
        archivo.write(f"- **Promedio de rendimiento general:** {estadisticas['promedio_rendimiento']:.2f} ton/ha\n\n")
        archivo.write("## Hallazgos Principales\n\n")
        archivo.write(f"- **Mayor producción:** {estadisticas['cultivo_mayor']} ({estadisticas['produccion_mayor']:.2f} toneladas)\n")
        archivo.write(f"- **Menor producción:** {estadisticas['cultivo_menor']} ({estadisticas['produccion_menor']:.2f} toneladas)\n")

        print(f"Informe generado exitosamente en: '{ruta_salida}'")

# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    #Definir rutas probables para ubicar el dataset de cultivos
    posibles_rutas=[
        os.path.join("data", "cultivos.csv"),
        os.path.join("..", "data", "cultivos.csv"),
        "cultivos.csv"
    ]

    ruta_encontrada=None
    for ruta in posibles_rutas:
        if os.path.exists(ruta):
            ruta_encontrada=ruta
            break

    if ruta_encontrada:
        #1. Leer los datos del csv con try-except
        cultivos=leer_cultivos(ruta_encontrada)

        #2. Calcular estadísticas
        stats=calcular_estadisticas(cultivos)

        #3. Generar informe en formato Markdown
        generar_informe(stats, "informe_cultivos.md")
    else:
        print("Error: No se encontró el archivo de datos 'data/cultivos.csv'.")