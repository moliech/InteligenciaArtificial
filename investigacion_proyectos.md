# Investigación de Proyectos de Inteligencia Artificial

**Asignatura:** Inteligencia Artificial (Semestre 6)  
**Institución:** COTECNOVA  
**Docente:** Jhon James Cano Sánchez  
**Actividad:** Actividad Independiente - Clase 1 (Exploración del Banco de Proyectos)

---

## Introducción
El presente documento contiene el análisis e investigación preliminar de tres (3) propuestas de proyectos de Inteligencia Artificial elegidas para el curso. Cada idea aborda un problema real mediante el uso de Python, combinando herramientas de recomendación, análisis de documentos legales y procesamiento de texto, redactadas en un lenguaje claro y accesible.

---

## Proyecto 1: "Cerebro D&D para Principiantes" (Asistente Recomendador y Creador de Personajes)

* **¿Qué problema resuelve?:**  
  Crear una ficha de personaje en el juego de rol *Dungeons & Dragons* por primera vez es muy difícil para los principiantes porque el libro de reglas contiene demasiada información. Este sistema ayuda a los nuevos jugadores guiándolos paso a paso: valida que el personaje cumpla las reglas del juego y le recomienda qué raza, clase, poderes y habilidades elegir según el tipo de héroe que el usuario quiera crear (por ejemplo: "quiero un personaje sigiloso pero que también lance hechizos").

* **¿Qué tipo de datos se necesitarían?:**  
  Una base de datos en formato sencillo (archivos de texto o tablas en Python) que contenga la información oficial del reglamento básico de Dungeons & Dragons (lista de razas, clases de personajes, hechizos y habilidades), junto con las respuestas o preferencias del usuario.

* **¿Qué modelo de IA podría ser adecuado?:**  
  Un **Sistema de Reglas Lógicas** (para comprobar que no se violen las reglas del juego) combinado con un **Algoritmo Recomendador por Similitud** en Python, que compara lo que el usuario quiere jugar con las mejores opciones disponibles.

---

## Proyecto 2: Consultor Inteligente de Normativa en Salud (Colombia)

* **¿Qué problema resuelve?:**  
  En el sistema de salud de Colombia, las leyes, decretos y resoluciones cambian constantemente (como las reglas de facturación RIPS, autorización de medicamentos en MIPRES, cobros del Plan de Beneficios en Salud - PBS o manuales de glosas). Esto confunde a médicos, auditores y hospitales sobre qué norma aplicaba en una fecha específica del pasado. Este sistema permite hacer preguntas en lenguaje común y saber exactamente qué norma estaba vigente en determinado momento del tiempo.

* **¿Qué tipo de datos se necesitarían?:**  
  Los textos de los decretos, resoluciones y circulares emitidos por el Ministerio de Salud de Colombia, organizados con sus fechas de publicación, fecha de vigencia y el tema al que corresponden (ej. facturación, medicamentos o autorizaciones).

* **¿Qué modelo de IA podría ser adecuado?:**  
  Un modelo de **Búsqueda Semántica y Clasificación de Textos** en Python (utilizando técnicas de Procesamiento de Lenguaje Natural o NLP), que analiza la pregunta del usuario, filtra por la fecha requerida y encuentra los artículos legales exactos que responden a la consulta.

---

## Proyecto 3: Tutor Inteligente de Idiomas Interpretativo y Adaptativo (Lectura y Escritura)

* **¿Qué problema resuelve?:**  
  Los traductores como Google Translate traducen palabras sueltas o frases de forma literal, sin enseñar la intención real del texto. Este tutor virtual en Python ayuda a las personas a practicar lectura y escritura en inglés, evaluando si el estudiante entendió el mensaje completo en lugar de palabra por palabra, y creando un plan de estudio que se adapta a las dudas frecuentes del alumno.

* **¿Qué tipo de datos se necesitarían?:**  
  Una colección de lecturas y párrafos etiquetados por su nivel de dificultad (desde nivel principiante hasta avanzado), junto con un registro de los errores de interpretación y vocabulario que va cometiendo el estudiante durante sus prácticas.

* **¿Qué modelo de IA podría ser adecuado?:**  
  Un **Clasificador de Texto y Lenguaje Natural (NLP)** en Python que analiza la redacción del usuario, identifica qué tan precisa fue su interpretación y sugiere automáticamente lecturas o ejercicios para reforzar sus puntos débiles.

---

## Conclusión y Selección Propuesta para la Clase 2
Las tres opciones resuelven problemas prácticos, son fáciles de comprender por cualquier persona y se pueden desarrollar completamente desde cero en Python durante el semestre. La propuesta del **Consultor de Normativa en Salud** destaca especialmente por su gran impacto en el contexto real colombiano y su utilidad para el sector público y privado.
