# Repositorio de Inteligencia Artificial

**Asignatura:** Inteligencia Artificial (Semestre 6)  
**Institución:** Corporación de Estudios Tecnológicos del Norte del Valle (COTECNOVA)  
**Estudiante:** Jhon Esteban Molina Echavarria  
**Compañero de Proyecto:** Heiber Lozano Mercado  
**Docente:** Jhon James Cano Sánchez  
**Repositorio Oficial de Referencia:** [Clase2.md (Profesor James Cano)](https://github.com/jamescanos/InteligenciaArtificial/blob/master/Clase2.md)

---

## 📌 Entregables del Curso por Clases

### 🔵 Clase 1: Fundamentos e Investigación de Proyectos

* **Script básico:** [`src/analisis_datos.py`](./src/analisis_datos.py) - Script básico con variables y condicionales `if/else`.
* **Investigación de Proyectos:** [`investigacion_proyectos.md`](./investigacion_proyectos.md) - Análisis preliminar de 3 propuestas de proyectos de IA y selección del *Tutor Inteligente de Idiomas*.

---

### 🟢 Clase 2: Docker, Estructuras de Datos y Carga Real

* **Actividad 10 y 11 (Definición y Estructura del Proyecto Final):**
  * **Nombre del Proyecto:** Tutor Inteligente de Idiomas Interpretativo y Adaptativo (Lectura y Escritura en Inglés)
  * **Compañero de Grupo:** Heiber Lozano Mercado *(Nota: Se creará un repositorio grupal dedicado al iniciar el desarrollo del avance del primer corte)*.
  * **Problemática:** Los estudiantes de inglés suelen traducir literalmente palabra por palabra sin comprender el sentido global del texto, o no cuentan con un plan de estudio adaptado a sus fallas frecuentes.
  * **Objetivo:** Desarrollar un sistema interactivo en Python que evalúe la comprensión lectora, determine el nivel real del estudiante (A1, A2, B1) y sugiera lecturas adaptadas a sus necesidades.
  * **Datos a utilizar:** Dataset estructurado en CSV (`data/lecturas_ingles.csv`) con lecturas en inglés, niveles de dificultad, número de palabras y categorías.
  * **Tecnologías:** Python, Docker (`Dockerfile`, `docker-compose.yml`), Listas, Diccionarios y Funciones.

* **Actividad 12 (Actividad en Clase - Gestión de Cultivos):**
  * **Enunciado:** Desarrollar un programa que gestione información de cultivos en Cartago usando listas, diccionarios y funciones integradas.
  * **Archivo de código:** [`src/gestion_cultivos.py`](./src/gestion_cultivos.py)
  * **Funciones desarrolladas:**
    1. `calcular_rendimiento(cultivo)`: Retorna la producción por hectárea.
    2. `mostrar_cultivos(lista_cultivos)`: Imprime cada cultivo y su rendimiento formateado.
    3. `cultivo_mayor_rendimiento(lista_cultivos)`: Determina y retorna el cultivo de mayor rendimiento.

* **Actividad 13 (Actividad Independiente - Procesamiento de Datos del Proyecto):**
  * **Enunciado:** Crear un archivo de datos real (`CSV` o `JSON`) enfocado en el proyecto final y un script `cargar_datos.py` que procese la información y muestre estadísticas clave.
  * **Archivos entregados:**
    * **Dataset del Proyecto:** [`data/lecturas_ingles.csv`](./data/lecturas_ingles.csv)
    * **Script de Análisis:** [`src/cargar_datos.py`](./src/cargar_datos.py)
  * **Funciones desarrolladas:**
    1. `leer_datos(ruta_archivo)`: Carga el archivo CSV y lo convierte en una lista de diccionarios.
    2. `mostrar_resumen(datos)`: Muestra la cantidad total de registros y tres estadísticas básicas (promedio de palabras, dificultad máxima y dificultad mínima).

---

### 🔴 Clase 3: Manejo de Archivos e Informes Estadísticos

* **Actividad en Clase (Procesamiento CSV de Cultivos e Informe Markdown):**
  * **Enunciado:** Crear un programa que lea un archivo CSV de cultivos, procese los datos y genere un informe automático en formato Markdown.
  * **Dataset:** [`data/cultivos.csv`](./data/cultivos.csv)
  * **Script:** [`src/analizar_cultivos.py`](./src/analizar_cultivos.py) - Lee el archivo con `csv.DictReader` y genera automáticamente [`informe_cultivos.md`](./informe_cultivos.md).

* **Actividad Independiente (Análisis del Proyecto de Inglés e Informe Markdown):**
  * **Enunciado:** Aplicar el manejo de archivos y estructuras de datos al proyecto personal del Tutor de Inglés, calculando 5 estadísticas y generando un informe en Markdown.
  * **Dataset del Proyecto:** [`data/lecturas_ingles.csv`](./data/lecturas_ingles.csv)
  * **Script de Análisis:** [`src/analisis_proyecto.py`](./src/analisis_proyecto.py) - Procesa los datos con `csv.DictReader`, convierte valores numéricos, calcula 5 estadísticas clave (total lecturas, promedio palabras, dificultad mínima/máxima, promedio general de dificultad y distribución por nivel) y genera el informe estructurado.
  * **Informe Generado:** [`informes/informe_ingles.md`](./informes/informe_ingles.md)

---

## 📂 Índice General de Archivos del Repositorio

| Clase | Archivo / Entregable | Descripción |
| :--- | :--- | :--- |
| **Clase 1** | [`src/analisis_datos.py`](./src/analisis_datos.py) | Script básico con variables y condicionales `if/else`. |
| **Clase 1** | [`investigacion_proyectos.md`](./investigacion_proyectos.md) | Investigación preliminar de 3 propuestas de proyectos de IA. |
| **Clase 2** | [`src/gestion_cultivos.py`](./src/gestion_cultivos.py) | **Actividad 12:** Ejercicio integrador con listas, diccionarios y funciones. |
| **Clase 2** | [`data/lecturas_ingles.csv`](./data/lecturas_ingles.csv) | **Actividad 13 (Dataset):** Datos iniciales del proyecto del Tutor de Inglés. |
| **Clase 2** | [`src/cargar_datos.py`](./src/cargar_datos.py) | **Actividad 13 (Script):** Carga y resumen estadístico del dataset. |
| **Clase 3** | [`data/cultivos.csv`](./data/cultivos.csv) | **Clase 3 (Dataset):** Datos de cultivos para generación de informe. |
| **Clase 3** | [`src/analizar_cultivos.py`](./src/analizar_cultivos.py) | **Clase 3 (Script):** Procesamiento de CSV de cultivos y generación de `informe_cultivos.md`. |
| **Clase 3** | [`src/analisis_proyecto.py`](./src/analisis_proyecto.py) | **Clase 3 Independiente (Script):** Procesamiento de lecturas de inglés y 5 estadísticas. |
| **Clase 3** | [`informes/informe_ingles.md`](./informes/informe_ingles.md) | **Clase 3 Independiente (Informe):** Informe generado en Markdown con estadísticas del proyecto. |

---

## 🛠️ Cómo ejecutar los scripts

```bash
# Ejecutar Actividad 12 (Clase 2)
python src/gestion_cultivos.py

# Ejecutar Actividad 13 (Clase 2)
python src/cargar_datos.py

# Ejecutar Actividad en Clase (Clase 3)
python src/analizar_cultivos.py

# Ejecutar Actividad Independiente del Proyecto (Clase 3)
python src/analisis_proyecto.py
```

### Ejecución en Docker:
```bash
# Levantar contenedor
docker compose up -d

# Ejecutar script de análisis dentro del contenedor
docker exec -it ia-python python src/analisis_proyecto.py
```
