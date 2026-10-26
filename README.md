# MCD-UdeG
## Programacion_I
Bienvenido al repositorio de la asignatura **Programación I**, correspondiente a la **Maestría en Ciencia de Datos**. Este espacio reúne los materiales, ejercicios y proyectos orientados al aprendizaje del lenguaje Python y al desarrollo de soluciones computacionales aplicadas al análisis de datos.
Durante el curso se abordarán los fundamentos de programación, el manejo de variables y estructuras de control, la manipulación de cadenas y archivos, las estructuras de datos, la programación orientada a objetos, las expresiones regulares, los servicios web y la integración con bases de datos SQL.
Asimismo, se utilizarán herramientas para la depuración y prueba de programas, así como **Git y GitHub** para el control de versiones y el desarrollo colaborativo.

## Objetivo
Desarrollar las habilidades necesarias para diseñar, implementar, depurar y documentar programas en Python, integrando buenas prácticas de programación y herramientas de colaboración.

## Contenido general
1. Arquitectura y fundamentos de Python.
2. Variables, tipos de datos y estructuras de control.
3. Manipulación de cadenas.
4. Lectura y escritura de archivos.
5. Estructuras de datos.
6. Expresiones regulares.
7. Programación orientada a objetos.
8. Sockets y servicios web.
9. Bases de datos SQL.
10. Depuración y pruebas de código.
11. Control de versiones con Git y GitHub.

## Recursos del repositorio
En este repositorio se publicarán ejemplos, prácticas, actividades y proyectos desarrollados durante el curso.

---

# Desafíos - Programación I
**Maestría en Ciencia de los Datos | CUCEA — Universidad de Guadalajara**

Este repositorio contiene la solución modular e interactiva para los desafíos de la asignatura Programación I, desarrollados en Python dentro de un entorno de Visual Studio.

## Tabla de Contenidos
- [Descripción General](#descripción-general)
- [Desafío 1: Validador de Palíndromos](#desafío-1-validador-de-palíndromos)
- [Desafío 2: Generador de Histograma por Intervalos](#desafío-2-generador-de-histograma-por-intervalos)
- [Requisitos e Instalación](#requisitos-e-instalación)
- [Instrucciones de Ejecución](#instrucciones-de-ejecución)
- [Criterios de Calidad y Robustez](#criterios-de-calidad-y-robustez)

---

## Descripción General

El propósito de estos desafíos es poner en práctica fundamentos esenciales de Python para la manipulación de cadenas de texto, control de flujo, funciones personalizadas y estructuras de datos nativas sin recurrir a librerías de terceros.

---

## Desafío 1: Validador de Palíndromos

### Descripción
Un **palíndromo** es una palabra o frase que se lee igual de izquierda a derecha que de derecha a izquierda, ignorando espacios, signos de puntuación, tildes y mayúsculas. El programa solicita una entrada al usuario y determina de manera automatizada si cumple con esta propiedad.

### Lógica de Solución
1. **Normalización del texto**: Conversión a minúsculas (`.lower()`) y remoción de espacios intermedios (`.replace(' ', '')`).
2. **Remoción de acentos**: Implementación de la función auxiliar `eliminar_acentos()`, la cual mapea las vocales acentuadas (`á`, `é`, `í`, `ó`, `ú`, `ü`) a sus equivalentes simples usando un diccionario de sustitución.
3. **Validación de entradas**:
   - Inspección mediante `.isalpha()` para asegurar que la entrada contenga únicamente letras, descartando números o símbolos.
   - Verificación de longitud (`len(palabra) > 1`) para evitar palabras de un solo carácter o entradas vacías.
4. **Comprobación del palíndromo**: Comparación directa de la cadena limpia contra su versión invertida utilizando *slicing* (`palabra == palabra[::-1]`).
5. **Ciclo de consulta interactivo**: Bucle `while` que permite realizar múltiples validaciones continuas mediante confirmación explícita de usuario (`S/N`).

### Ejemplo de Uso
```
Ingresa una palabra o frase para verificar si es un palíndromo: solos
La palabra o frase es un palíndromo
----------------------------------------
¿Quiere ingresar otra palabra (S/N)?: n
¡Hasta luego!
```

---

## Desafío 2: Generador de Histograma

### Descripción
Generación gráfica en consola de un histograma de frecuencias basado en una lista de valores numéricos, agrupando los datos en rangos de intervalo continuos mediante barras representadas por asteriscos (*).

### Lógica de Solución
1. **Detección de límites:** Cálculo del límite inferior (minimo) y superior (maximo) ajustados al tamaño del intervalo (ancho_barra) mediante división entera (//).
2. **Clasificación en rangos:** Recorrido iterativo de los intervalos semiabiertos [actual, siguiente) para contar cuántos elementos de la lista caen en cada segmento.
3. **Impresión alineada:** Formateo numérico en consola para mostrar el intervalo y la barra visual ('*' * frecuencia).

### Ejemplo de Uso
```
Valores analizados: [4.2, 8.7, 2.5, 6.0, 0.4, 5.5, 4.8, 2.1, 4.0, 9.1, 5.9, 1.2]

--- Histograma (Intervalos de tamaño 2) ---
 Intervalo  | Frecuencia
------------------------------
[  0 -   2) | **
[  2 -   4) | **
[  4 -   6) | *****
[  6 -   8) | *
[  8 -  10) | **
```
---

## Requisitos e Instalación
- Python 3.10 o superior.
- Entorno de ejecución de Jupyter Notebook, Google Colab o VS Code.
- Módulos de la biblioteca estándar de Python (no requiere instalaciones externas con pip).

... by Julia Dominguez