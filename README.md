# Repositorio de Inteligencia Artificial

**Asignatura:** Inteligencia Artificial (Semestre 6)  
**Institución:** Corporación de Estudios Tecnológicos del Norte del Valle (COTECNOVA)  
**Estudiante:** Jhon Esteban Molina Echavarria  
**Docente:** Jhon James Cano Sánchez  
**Repositorio Oficial:** [github.com/moliech/InteligenciaArtificial](https://github.com/moliech/InteligenciaArtificial)

---

## 📌 Entregables del Curso por Clases

### 📘 Clase 1: Introducción a la IA y Fundamentos de Python
* **Actividad en Clase:** [`src/analisis_datos.py`](./src/analisis_datos.py) - Script básico de variables y condicionales `if/else`.
* **Actividad Independiente:** [`investigacion_proyectos.md`](./investigacion_proyectos.md) - Investigación preliminar de 3 propuestas de proyectos de IA.

---

### 📙 Clase 2: Estructuras de Datos y Funciones
* **Actividad 12 (En Clase):** [`src/gestion_cultivos.py`](./src/gestion_cultivos.py) - Ejercicio integrador con listas de diccionarios, cálculo de rendimientos y cultivo con mayor rendimiento.
* **Actividad 13 (Independiente):** 
  * Dataset del proyecto: [`data/lecturas_ingles.csv`](./data/lecturas_ingles.csv)
  * Script de Carga y Resumen: [`src/cargar_datos.py`](./src/cargar_datos.py)

---

### 📗 Clase 3: Manejo de Archivos, Excepciones e Informes Automáticos
* **Actividad en Clase:**
  * Dataset CSV: [`data/cultivos.csv`](./data/cultivos.csv)
  * Script de Procesamiento con `try-except`: [`src/analizar_cultivos.py`](./src/analizar_cultivos.py)
  * Informe Automático Generado: [`informe_cultivos.md`](./informe_cultivos.md)

---

## 📂 Estructura General del Repositorio

```text
InteligenciaArtificial/
├── .dockerignore                  # Exclusiones para construcciones de Docker
├── .gitignore                     # Exclusiones para el control de versiones de Git
├── Dockerfile                     # Configuración de imagen contenedora de Python
├── docker-compose.yml             # Orquestación de servicios para el entorno
├── README.md                      # Documentación principal del repositorio
├── informe_cultivos.md            # Informe generado automáticamente por Clase 3
├── investigacion_proyectos.md     # Documento de investigación de proyectos (Clase 1)
├── requirements.txt               # Dependencias principales del proyecto
├── data/                          # Almacenamiento de archivos de datos (CSV/JSON)
│   ├── cultivos.csv
│   └── lecturas_ingles.csv
└── src/                           # Código fuente en Python
    ├── analisis_datos.py
    ├── analizar_cultivos.py
    ├── cargar_datos.py
    ├── gestion_cultivos.py
    └── main.py
```

---

## 🛠️ Cómo ejecutar los scripts
```bash
# Ejecutar Actividad Clase 2 (Gestión de cultivos en memoria)
python3 src/gestion_cultivos.py

# Ejecutar Actividad Clase 2 (Carga de dataset de inglés)
python3 src/cargar_datos.py

# Ejecutar Actividad Clase 3 (Análisis de CSV e Informe automático en Markdown)
python3 src/analizar_cultivos.py
```
