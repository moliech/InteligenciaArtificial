# 🤖 Repositorio Académico: Inteligencia Artificial (Semestre 6)

**Institución:** COTECNOVA  
**Docente:** Jhon James Cano Sánchez  
**Integrantes del Proyecto Independiente:**  
- **Jhon Esteban Molina Echavarría**  
- **Heiber Lozano Mercado**  

---

## 📌 Estructura del Repositorio

\InteligenciaArtificial/
├── Dockerfile                  # Entorno Docker con Python 3.12-slim
├── docker-compose.yml          # Servicio Docker e integración de volúmenes
├── requirements.txt            # Dependencias (numpy, pandas, matplotlib, scikit-learn, jupyter)
├── README.md                   # Documentación principal del repositorio
├── data/                       # Archivos de datos (.csv)
│   ├── cultivos.csv            # Dataset de práctica en clase
│   └── lecturas_ingles.csv     # Dataset del proyecto (Tutor de Inglés)
├── src/                        # Scripts en Python
│   ├── main.py                 # Script de prueba inicial (Clase 2)
│   ├── gestion_cultivos.py     # Práctica de Listas, Diccionarios y Funciones (Clase 2)
│   ├── analizar_cultivos.py    # Práctica de Lectura de CSV e Informes (Clase 3)
│   ├── cargar_datos.py         # Carga inicial de datos del proyecto (Clase 2)
│   └── analisis_proyecto.py    # Procesamiento e informe del proyecto (Clase 3)
└── informes/                   # Informes generados automáticamente en Markdown
    └── informe_ingles.md       # Informe de estadísticas del Tutor de Inglés
\
---

## 💻 1. Trabajo en Clase (Actividades Guiadas)

Ejercicios prácticos desarrollados durante las sesiones presenciales de la asignatura para comprender los fundamentos de Python, estructuras de datos y Docker:

* **Clase 1: Configuración de Herramientas**:
  - Configuración de WSL 2, Ubuntu, Docker Desktop y entorno de desarrollo en VS Code.
* **Clase 2: Fundamentos de Python y Dockerization**:
  - Creación del contenedor Docker \ia-python\ basado en \python:3.12-slim\.
  - Script \src/gestion_cultivos.py\: Manejo de listas de diccionarios, cálculo de rendimiento de cultivos y funciones.
* **Clase 3: Manejo de Archivos e Informes**:
  - Lectura del archivo \data/cultivos.csv\ utilizando el módulo \csv.DictReader\.
  - Script \src/analizar_cultivos.py\ para calcular estadísticas y generar automáticamente \informe_cultivos.md\.

---

## 🚀 2. Trabajo Independiente (Proyecto de IA)

**Nombre del Proyecto:** Tutor Inteligente de Idiomas (Lectura y Comprensión en Inglés)  
**Equipo de Trabajo:** Jhon Esteban Molina Echavarría & Heiber Lozano Mercado  

### 🎯 Descripción del Proyecto
Un sistema inteligente de soporte educativo diseñado para evaluar la extensión y dificultad léxica de lecturas en inglés (clasificadas en niveles A1, A2, B1, B2). El objetivo es ubicar al estudiante en el nivel de lectura óptimo y dosificar el contenido para fomentar la comprensión de ideas globales en lugar de la traducción literal.

### 📅 Entregas del Proyecto Independiente

* **Entrega Clase 1 - Exploración del Banco de Proyectos**:
  - Selección e investigación del *Tutor Inteligente de Idiomas* en el documento \investigacion_proyectos.md\.
* **Entrega Clase 2 - Carga de Datos Reales**:
  - Definición del dataset \data/lecturas_ingles.csv\ y creación del script de lectura \src/cargar_datos.py\.
* **Entrega Clase 3 - Procesamiento y Generación de Informe**:
  - Script \src/analisis_proyecto.py\: Lee los datos con \csv.DictReader\, convierte valores numéricos y calcula 5 estadísticas clave (total lecturas, promedio palabras, dificultad min/max, promedio dificultad y distribución por nivel).
  - Generación automática del informe estructurado en \informes/informe_ingles.md\.

---

## 🛠️ Instrucciones de Ejecución

1. **Levantar el contenedor de Docker**:
   \\ash
   docker compose up -d
   \2. **Ejecutar el análisis del proyecto independiente**:
   \\ash
   python3 src/analisis_proyecto.py
   \3. **Revisar el informe generado**:
   Verificar la creación del archivo \informes/informe_ingles.md\.
