import csv
import os

def leer_datos(ruta_archivo):
    """Lee un archivo CSV y convierte cada fila en una lista de diccionarios."""
    datos = []
    with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            datos.append({
                "id": int(fila["id"]),
                "titulo": fila["titulo"],
                "nivel": fila["nivel"],
                "palabras": int(fila["palabras"]),
                "dificultad": float(fila["dificultad"])
            })
    return datos

def mostrar_resumen(datos):
    """Muestra la cantidad total de registros y estadísticas básicas de los datos."""
    total_registros = len(datos)

    # Extraer listas con los valores numéricos
    lista_palabras = [item["palabras"] for item in datos]
    lista_dificultad = [item["dificultad"] for item in datos]

    # Calcular estadísticas
    promedio_palabras = sum(lista_palabras) / total_registros
    max_dificultad = max(lista_dificultad)
    min_dificultad = min(lista_dificultad)

    # Impresión de resultados
    print("=== RESUMEN DEL DATASET DE INGLÉS ===")
    print(f"Total de registros: {total_registros}")
    print(f"Promedio de palabras por texto: {promedio_palabras:.1f} palabras")
    print(f"Dificultad máxima registrada: {max_dificultad}")
    print(f"Dificultad mínima registrada: {min_dificultad}")

# --- Programa principal ---
if __name__ == "__main__":
    # Buscar el archivo de datos tanto desde la raíz como dentro de src/
    posibles_rutas = [
        os.path.join("data", "lecturas_ingles.csv"),
        os.path.join("..", "data", "lecturas_ingles.csv"),
        "lecturas_ingles.csv"
    ]
    
    ruta_encontrada = None
    for ruta in posibles_rutas:
        if os.path.exists(ruta):
            ruta_encontrada = ruta
            break
            
    if ruta_encontrada:
        datos_ingles = leer_datos(ruta_encontrada)
        mostrar_resumen(datos_ingles)
    else:
        print("Error: No se encontró el archivo de datos lecturas_ingles.csv en data/")