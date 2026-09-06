import csv
import os

def cargar_datos_ingles(ruta_csv):
   """Lee el archivo CSV de lecturas de ingles"""
   lecturas = []
   with open(ruta_csv, mode='r', encoding='utf-8') as archivo:
        lector=csv.DictReader(archivo)
        for fila in lector:
            lectura = {
                'id': int(fila['id']),
                'titulo': fila['titulo'],
                'nivel': fila['nivel'],
                'palabras': int(fila['palabras']),
                'dificultad': float(fila['dificultad'])
            }
            lecturas.append(lectura)
        return lecturas

def calcular_estadisticas_ingles(lecturas):
    """Calcula estadisticas de las lecturas de ingles"""
    total_lecturas=len(lecturas)
    if total_lecturas==0:
        return{}


    palabras = [l["palabras"]for l in lecturas]
    dificultades = [l["dificultad"]for l in lecturas]

    promedio_palabras=sum(palabras)/total_lecturas
    max_dificultad=max(dificultades)
    min_dificultad=min(dificultades)
    promedio_dificultad=sum(dificultades)/total_lecturas

    #conteo de lecturas por nivel
    conteo_nivel={}
    for l in lecturas:
        nivel=l["nivel"]
        conteo_nivel[nivel]=conteo_nivel.get(nivel,0)+1

    return {
        'total_lecturas': total_lecturas,
        'promedio_palabras': promedio_palabras,
        'max_dificultad': max_dificultad,
        'min_dificultad': min_dificultad,
        'promedio_dificultad': promedio_dificultad,
        'conteo_nivel': conteo_nivel
    }

def generar_informe_ingles(estadisticas, ruta_salida):
    """Genera automaticamente el informe en formato Markdown"""

    #Crea la carpeta de salida si no existe
    if directorio := os.path.dirname(ruta_salida):
        os.makedirs(directorio, exist_ok=True)

    with open(ruta_salida, mode='w', encoding='utf-8')as f:
        f.write("# 📚 Informe del Proyecto: Tutor Inteligente de Inglés\n\n")
        f.write("## 📝 Descripción del Dataset\n")
        f.write("Este dataset contiene lecturas clasificadas según el nivel del estudiante (A1, A2, B1), ")
        f.write("evaluando la extensión del texto en palabras y su nivel de dificultad para adaptar la enseñanza.\n\n")
        
        f.write("## 📊 Tabla de Estadísticas Calculadas\n\n")
        f.write("| Métrica | Valor Calculado |\n")
        f.write("|---|---|\n")
        f.write(f"| **Total de Lecturas Evaluadas** | {estadisticas['total_lecturas']} lecturas |\n")
        f.write(f"| **Promedio de Palabras por Texto** | {estadisticas['promedio_palabras']:.2f} palabras |\n")
        f.write(f"| **Dificultad Léxica Máxima** | {estadisticas['max_dificultad']:.2f} / 5.0 |\n")
        f.write(f"| **Dificultad Léxica Mínima** | {estadisticas['min_dificultad']:.2f} / 5.0 |\n")
        f.write(f"| **Promedio General de Dificultad** | {estadisticas['promedio_dificultad']:.2f} / 5.0 |\n\n")
        f.write("### 🎯 Distribución por Nivel\n")
        for nivel, cantidad in estadisticas['conteo_nivel'].items():
            f.write(f"- **Nivel {nivel}**: {cantidad} lectura(s)\n")
        f.write("\n")
        f.write("## 💡 Interpretación de Resultados para la Enseñanza del Inglés\n")
        f.write("- **Diagnóstico y Nivelación**: La brecha entre la dificultad mínima y la máxima permite a la IA ubicar al estudiante en la lección ideal.\n")
        f.write("- **Dosificación de Lectura**: El promedio de palabras ayuda a estimar el tiempo de lectura para enfocar al estudiante en la comprensión de ideas globales y no en la traducción literal palabra por palabra.\n") 


if __name__ == "__main__":
    ruta_csv = "data/lecturas_ingles.csv"
    ruta_salida = "informes/informe_ingles.md"

    lecturas = cargar_datos_ingles(ruta_csv)
    estadisticas = calcular_estadisticas_ingles(lecturas)
    generar_informe_ingles(estadisticas, ruta_salida)

    print(f"✅ ¡Análisis completado con éxito! Se ha generado el informe '{ruta_salida}'.")