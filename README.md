# Repositorio de Inteligencia Artificial

**Asignatura:** Inteligencia Artificial (Semestre 6)  
**Institución:** Corporación de Estudios Tecnológicos del Norte del Valle (COTECNOVA)  
**Estudiante:** Jhon Esteban Molina Echavarria  
**Docente:** Jhon James Cano Sánchez  
**Repositorio Oficial de Referencia:** [Clase2.md (Profesor James Cano)](https://github.com/jamescanos/InteligenciaArtificial/blob/master/Clase2.md)

---

## 📌 Entregables de la Clase 2 (Actividades 10, 11, 12 y 13)

### 🔵 Actividad 10 y 11: Definición y Estructura del Proyecto Final

* **Nombre del Proyecto:** Tutor Inteligente de Idiomas Interpretativo y Adaptativo (Lectura y Escritura en Inglés)
* **Compañero de Grupo:** Heiber Lozano Mercado *(Nota: Se creará un repositorio grupal dedicado al iniciar el desarrollo del proyecto)*.
* **Problemática:** Los estudiantes de inglés suelen traducir literalmente palabra por palabra sin comprender el sentido global del texto, o no cuentan con un plan de estudio adaptado a sus fallas frecuentes.
* **Objetivo:** Desarrollar un sistema interactivo en Python que evalúe la comprensión lectora, determine el nivel real del estudiante (A1, A2, B1) y sugiera lecturas adaptadas a sus necesidades.
* **Datos a utilizar:** Dataset estructurado en CSV (`lecturas_ingles.csv`) con lecturas en inglés, niveles de dificultad, número de palabras y categorías gramaticales.
* **Tecnologías:** Python (Listas, Diccionarios, Funciones, Manejo de Archivos CSV y Análisis Estadístico).
* **Documentación previa:** [`investigacion_proyectos.md`](./investigacion_proyectos.md)

---

### 🟢 Actividad 12: Actividad en Clase (Gestión de Cultivos)

* **Enunciado:** Desarrollar un programa que gestione información de cultivos en Cartago usando listas, diccionarios y funciones integradas.
* **Archivo de código:** [`gestion_cultivos.py`](./gestion_cultivos.py)
* **Funciones desarrolladas:**
  1. `calcular_rendimiento(cultivo)`: Retorna la producción por hectárea.
  2. `mostrar_cultivos(lista_cultivos)`: Imprime cada cultivo y su rendimiento formateado.
  3. `cultivo_mayor_rendimiento(lista_cultivos)`: Determina y retorna el cultivo de mayor rendimiento.

---

### 🔴 Actividad 13: Actividad Independiente (Procesamiento de Datos del Proyecto)

* **Enunciado:** Crear un archivo de datos real (`CSV` o `JSON`) enfocado en el proyecto final y un script `cargar_datos.py` que procese la información y muestre estadísticas clave.
* **Archivos entregados:**
  * **Dataset del Proyecto:** [`lecturas_ingles.csv`](./lecturas_ingles.csv)
  * **Script de Análisis:** [`cargar_datos.py`](./cargar_datos.py)
* **Funciones desarrolladas:**
  1. `leer_datos(ruta_archivo)`: Carga el archivo CSV y lo convierte en una lista de diccionarios.
  2. `mostrar_resumen(datos)`: Muestra la cantidad total de registros y tres estadísticas básicas (promedio de palabras, dificultad máxima y dificultad mínima).

---

## 📂 Índice General de Archivos del Repositorio

| Clase | Archivo / Entregable | Descripción |
| :--- | :--- | :--- |
| **Clase 1** | [`analisis_datos.py`](./analisis_datos.py) | Script básico con variables y condicionales `if/else`. |
| **Clase 1** | [`investigacion_proyectos.md`](./investigacion_proyectos.md) | Investigación preliminar de 3 propuestas de proyectos de IA. |
| **Clase 2** | [`gestion_cultivos.py`](./gestion_cultivos.py) | **Actividad 12:** Ejercicio integrador con listas, diccionarios y funciones. |
| **Clase 2** | [`lecturas_ingles.csv`](./lecturas_ingles.csv) | **Actividad 13 (Dataset):** Datos del proyecto del Tutor de Inglés. |
| **Clase 2** | [`cargar_datos.py`](./cargar_datos.py) | **Actividad 13 (Script):** Carga y resumen estadístico del dataset. |

---

## 🛠️ Cómo ejecutar los scripts
```bash
# Ejecutar Actividad 12
python gestion_cultivos.py

# Ejecutar Actividad 13
python cargar_datos.py
```
