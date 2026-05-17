# Analizador Léxico SQL a Python (ANTLR4)

Este proyecto es un Analizador Léxico (Lexer) desarrollado como parte de la materia de Programación de Sistemas. El sistema es capaz de reconocer, clasificar y validar un subconjunto extenso del lenguaje SQL, incluyendo estándares de SQL Server 2022.

## Características
- Soporte Extenso: Reconocimiento de comandos DML, DDL, DCL, funciones de ventana (Window Functions), CTEs y más.
- Manejo de Errores: Implementación de un `LexerErrorListener` que reporta la ubicación exacta (línea y columna) de símbolos desconocidos.
- Clasificación Eficiente: Los tokens se categorizan dinámicamente utilizando el catálogo generado por ANTLR4.
- Filtro de Ruido: Ignora automáticamente espacios en blanco y comentarios (tanto de una línea `--` como de bloque `/* ... */`).

## Estructura del Proyecto
El repositorio contiene los siguientes archivos esenciales:

| Archivo | Descripción |
| **`SQL.g4`** | Gramática léxica original donde se definen los tokens. |
| **`main.py`** | Script principal para ejecutar el análisis sobre archivos `.sql`. |
| **`SQLLexer.py`** | Lexer generado automáticamente por ANTLR4. |
| **`consulta_valida.sql`** | Archivo de prueba con sintaxis SQL correcta. |
| **`consulta_errores.sql`** | Archivo de prueba con errores léxicos intencionales. |

## Instalación y Requisitos

Para ejecutar este proyecto, necesitas tener instalado Python 3.x y la librería de ejecución de ANTLR4.

1. Instala la dependencia necesaria:
   pip install antlr4-python3-runtime==4.13.1
