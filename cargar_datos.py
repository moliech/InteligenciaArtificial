import csv

def leer_datos(ruta_archivo):
    """Lee un archivo csv y convierte cada fila en una lista de diccionarios."""
    datos = []
    with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            datos.append({
                "id": int(fila["id"]),
                "titulo": fila["titulo"],
                "nivel": fila["nivel"],
                "palabras":int(fila["palabras"]),
                "dificultad":float(fila["dificultad"])
            })
    return datos

def mostrar_resumen(datos):
    """Muestra la cantidad total de registros y estadisticas básicas de los datos."""
    total_registros = len(datos)

    #Extraer listas con los valores numericos
    lista_palabras = [item["palabras"] for item in datos]
    lista_dificultad = [item["dificultad"] for item in datos]

    #Calcular estadisticas
    promedio_palabras = sum(lista_palabras) / total_registros
    max_dificultad = max(lista_dificultad)
    min_dificultad = min(lista_dificultad)

    #Impresion de resultados
    print("===RESUMEN DEL DATASET DE INGLES===")
    print(f"Total de registros: {total_registros}")
    print(f"Promedio de palabras por texto: {promedio_palabras:.1f} palabras")
    print(f"Dificultad máxima registrada: {max_dificultad}")
    print(f"Dificultad mínima registrada: {min_dificultad}")

# ---Programa principal---
if __name__ == "__main__":
    #1. Cargar el dataset desde el archivo CSV
    datos_ingles = leer_datos("lecturas_ingles.csv")

    #2. Mostrar estadísticas básicas del dataset
    mostrar_resumen(datos_ingles)