Creado por Dario Joaquin Castillo Ocaña(Kah banda), 
Maria Jose carvajal Carrera y Ana Cristina 




Introducción
Este manual tiene como objetivo proporcionar una guía detallada sobre el uso de la aplicación para la conversión de Autómatas Finitos No Deterministas (AFN) a Autómatas Finitos Deterministas (AFD). Se explican sus funcionalidades, la interfaz gráfica, la API y el proceso de transformación y minimización de autómatas
La aplicación ofrece un conjunto de herramientas diseñadas para facilitar el trabajo con autómatas finitos, entre las que se incluyen:
Creación de autómatas: Permite definir estados, transiciones, símbolos de entrada y estados de aceptación.
Edición de autómatas: Modificación dinámica de estados y transiciones a través de la interfaz gráfica.
Conversión de AFN a AFD: Aplicación del algoritmo de determinación para transformar un autómata no determinista en su equivalente determinista.
Minimización de AFD: Reducción del número de estados del autómata determinista para optimizar su representación.
Visualización interactiva: Representación gráfica en tiempo real de los autómatas y sus transformaciones.
El programa va dirigido a Estudiantes de teoría de autómatas y lenguajes formales. Profesores que necesiten una herramienta visual para enseñar el concepto de conversión de AFN a AFD.
Conceptos Clave
¿Qué son los autómatas?
Autómata Finito No Determinista (AFN o NFA)
Un AFN es un modelo computacional que representa un conjunto de estados y transiciones en el que, para una misma entrada en un estado dado, pueden existir múltiples transiciones posibles hacia diferentes estados. Además, un AFN puede incluir transiciones vacías (ε-transiciones), lo que significa que puede cambiar de estado sin necesidad de consumir un símbolo de entrada. Aunque los AFN pueden parecer más potentes que los AFD, ambos tienen la misma capacidad expresiva en términos de los lenguajes que pueden reconocer.


Autómata Finito Determinista (AFD o DFA)
Un AFD es un tipo especial de autómata en el que, para cada estado y símbolo de entrada, existe una única transición posible a otro estado. A diferencia de los AFN, los AFD no permiten transiciones vacías ni múltiples caminos para un mismo símbolo. Aunque los AFD pueden ser más grandes que sus equivalentes AFN, son más fáciles de implementar en sistemas computacionales debido a su comportamiento predecible.
Ambos tipos de autómatas, tanto los AFN como los AFD, se describen formalmente mediante una estructura llamada quíntupla, definida como :
M = (Q, Σ, δ, q₀, F)
Q: Conjunto de estados del autómata.
Σ(sigma): Alfabeto de entrada, es decir, los símbolos que el autómata puede procesar.
δ(delta): Función de transición, que define cómo el autómata se mueve entre estados:
En un AFD, δ es una función total que asigna exactamente un estado para cada combinación de estado y símbolo.
En un AFN, δ puede asignar un conjunto de posibles estados, incluyendo transiciones epsilon (ε), que no consumen ningún símbolo de entrada.
q₀: Estado inicial desde donde comienza la ejecución.
F: Conjunto de estados de aceptación o finales.

Minimización 
Proceso de reducir el número de estados del autómata sin cambiar el lenguaje que reconoce. Esto se hace para obtener una versión más eficiente del autómata, útil en aplicaciones como el reconocimiento de patrones y la implementación de lenguajes formales.

Conversión 
Requisitos del sistema
Para garantizar un correcto funcionamiento de la aplicación de conversión de NFA a DFA, es importante cumplir con los siguientes requisitos de hardware y software.


Hardware Necesario
La aplicación es liviana y puede ejecutarse en la mayoría de los equipos modernos, pero se recomienda lo siguiente para un rendimiento óptimo:
Procesador: Intel Core i3 (10ª generación) o superior / AMD Ryzen 3 o superior.
Memoria RAM: Mínimo 4 GB (se recomiendan 8 GB para un mejor rendimiento).
Almacenamiento: Al menos 500 MB de espacio libre en disco para la instalación y almacenamiento de archivos temporales.
Pantalla: Resolución mínima de 1280x720 (HD), recomendada 1920x1080 (Full HD).
Conexión a Internet: Opcional, pero útil para la descarga de dependencias y actualizaciones.
Software de Base o Dependencias
Para ejecutar la aplicación, es necesario contar con los siguientes programas y paquetes:
Sistema Operativo:
Windows 10/11 (64 bits)
macOS 10.15 o superior
Distribuciones Linux (Ubuntu 20.04+, Debian 10+, Fedora 35+)
Entorno de Desarrollo:
Python 3.7+ (Se recomienda 3.9 o superior para compatibilidad y seguridad).
Dependencias de la Aplicación:
Flask (para ejecutar el servidor web).
Autómata-lib (para el procesamiento y conversión de autómatas).
Cytoscape.js (para la interfaz gráfica interactiva).
Bootstrap (para diseño responsivo de la interfaz web).
Herramientas Opcionales:
Un entorno virtual de Python (venv o virtualenv) para aislar la aplicación.
Un navegador web actualizado (Google Chrome, Firefox, Edge).




Arquitectura del software

La aplicación de conversión de NFA a DFA está basada en una arquitectura cliente-servidor, utilizando Flask como backend para el procesamiento de autómatas y Cytoscape.js para la visualización en el frontend.
 Diagramas de la Estructura General
A continuación, se presenta un diagrama de alto nivel que muestra los principales componentes de la aplicación y sus interacciones.
Diagrama General de la Arquitectura:

+---------------------------+
|         Cliente           |
|  (Interfaz Web con JS)    |
|   - Cytoscape.js          |
|   - HTML/CSS + Bootstrap  |
+------------+--------------+
             |
             | HTTP Requests (API REST)
             v
+---------------------------+
|         Servidor          |
|      (Flask - Python)     |
|   - Controladores (views) |
|   - Lógica de conversión  |
|   - API para peticiones   |
+------------+--------------+
             |
             v
+---------------------------+
|      Módulo de Cálculo    |
|  (Automata-lib en Python) |
|  - Procesamiento de NFA   |
|  - Conversión a DFA       |
|  - Minimización de DFA    |
+---------------------------+


 Componentes y Módulos
La aplicación se divide en varios módulos funcionales para mejorar la mantenibilidad y escalabilidad del código.
Módulos Principales:
Interfaz de Usuario (Frontend)
      Cytoscape.js: Biblioteca para la visualización y edición de autómatas.
      HTML/CSS + Bootstrap: Estructura visual y estilos responsivos.
      JavaScript: Comunicación con la API para procesar los autómatas en el servidor.
Backend (Flask - Python)
      Servidor Flask: Maneja las peticiones de la interfaz y gestiona la API.
      Rutas y Controladores: Define los endpoints (/convert, /) para recibir datos y procesarlos.
      Conversión de Autómatas: Lógica para transformar NFA en DFA utilizando automata-lib.
Módulo de Procesamiento (Automata-lib)
      Carga y Validación del NFA: Comprueba que los datos del autómata sean correctos.
      Conversión de NFA a DFA: Usa algoritmos estándar de teoría de autómatas.
      Minimización del DFA: Reduce el número de estados del autómata resultante.
