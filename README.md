# Repositorio de Inteligencia Artificial

**Asignatura:** Inteligencia Artificial (Semestre 6)  
**Institución:** Corporación de Estudios Tecnológicos del Norte del Valle (COTECNOVA)  

---

## 📌 Descripción del Proyecto Final
* **Nombre:** Tutor Inteligente de Idiomas Interpretativo y Adaptativo (Lectura y Escritura en Inglés)
* **Objetivo:** Desarrollar un sistema de apoyo en Python para el aprendizaje del idioma inglés, evaluando la comprensión lectora y adaptando ejercicios según el nivel y progreso del estudiante.

---

## 📂 Contenido del Repositorio por Clases

### 📘 Clase 1: Introducción a la Inteligencia Artificial y Python Básico

#### 1. Actividad en Clase
* **Enunciado:** Crear un primer script en Python para afianzar el uso de variables, tipos de datos y estructuras condicionales simples (`if` / `else`).
* **Archivo de código:** [`analisis_datos.py`](./analisis_datos.py)

#### 2. Actividad Independiente
* **Enunciado:** Investigar y redactar tres (3) propuestas de proyectos de Inteligencia Artificial aplicables a problemáticas reales, definiendo el problema a resolver, los datos requeridos y el tipo de modelo de IA sugerido.
* **Archivo de documentación:** [`investigacion_proyectos.md`](./investigacion_proyectos.md)

---

### 📙 Clase 2: Estructuras de Datos y Funciones en Python

#### 1. Actividad en Clase
* **Enunciado:** Desarrollar un programa integrador que gestione información de cultivos en Cartago usando listas, diccionarios y funciones. El script define datos de al menos 5 cultivos con sus hectáreas y toneladas producidas, e incluye funciones para:
  * `calcular_rendimiento(cultivo)`: Retorna las toneladas por hectárea.
  * `mostrar_cultivos(lista_cultivos)`: Imprime el listado de cultivos y su rendimiento formateado.
  * `cultivo_mayor_rendimiento(lista_cultivos)`: Identifica y retorna el nombre del cultivo con mayor rendimiento.
* **Archivo de código:** [`gestion_cultivos.py`](./gestion_cultivos.py)

#### 2. Actividad Independiente
* **Enunciado:** Aplicar el procesamiento de datos estructurados en Python orientándolo al proyecto final (**Tutor de Inglés**). Se crea un archivo de datos en formato CSV con textos/ejercicios en inglés y un script en Python que implementa:
  * `leer_datos(ruta_archivo)`: Lee el archivo CSV y lo convierte en una lista de diccionarios.
  * `mostrar_resumen(datos)`: Calcula e imprime la cantidad total de registros y tres estadísticas básicas (promedio de palabras, dificultad máxima y dificultad mínima).
* **Archivos entregados:**
  * **Dataset CSV:** [`lecturas_ingles.csv`](./lecturas_ingles.csv)
  * **Script de Análisis:** [`cargar_datos.py`](./cargar_datos.py)

---

## 🛠️ Requisitos de Ejecución
* Python 3.8 o superior.
* Para ejecutar cualquiera de los scripts:
  ```bash
  python <nombre_del_script>.py
  ```
