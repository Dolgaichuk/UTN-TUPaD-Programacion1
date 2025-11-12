# UTN Programación 1 - Trabajo Práctico Integrador (TPI)
## Sistema de Gestión de Datos de Países

### Descripción del Programa
Este proyecto es una aplicación de consola desarrollada en **Python 3.x** para la **Gestión de Datos de Países**. El objetivo es afianzar el uso de estructuras de datos (listas, diccionarios), modularización con funciones, manejo de archivos CSV, y técnicas de filtrado, ordenamiento y estadísticas, tal como se abordó en Programación I.

El sistema cumple con las funcionalidades mínimas requeridas en la consigna:
1. Persistencia de datos mediante **lectura desde CSV**.
2. Operaciones de consulta, incluyendo **búsqueda** y **filtrado por múltiples criterios**.
3. **Ordenamiento** ascendente/descendente por diferentes campos.
4. Generación de **estadísticas** clave.
5. **Validación de entradas** y manejo básico de errores.

###  Integrantes
La participación de los integrantes se detalla a continuación:

| Rol | Nombre y Apellido | Comision |
| **PROGRAMADOR**| Tadeo Dolgaichuk | Comision 7 |
| **PROGRAMADOR** | Sebastian Dolgaichuk | Comision 4  |

---

### Requisitos de Ejecución
Para correr la aplicación, solo necesitas tener instalado **Python 3.14**. No se requieren librerías externas adicionales más allá de los módulos estándar (`csv` y `os`).

### Instrucciones de Uso

Sigue estos pasos para ejecutar y probar el sistema:

1.  **Clonar el Repositorio:**
    Abre tu terminal y descarga el proyecto:
    ```bash
    git clone (https://github.com/Tadeee07/UTN-TUPaDProgramacion1-.git)
                (https://github.com/Dolgaichuk/UTN-TUPaD-Programacion1/blob/main/TPI%20Integrador%20II/Dolgaichuk%20TPI%20II.py
    ```

2.  **Verificar Archivos:**
    Asegúrate de que los archivos se encuentren en el mismo directorio:
    * `Integrador.py` (el código fuente Python)
    * `paises.csv` (el dataset base)

3.  **Ejecución:**
    Ejecuta el script de Python desde la terminal
   

4.  **Interacción:**
    El programa mostrará un **Menú Principal**. Selecciona la opción deseada (del 1 al 7) y sigue las indicaciones de la consola.

> **IMPORTANTE:** Para cumplir con la persistencia de datos, debes seleccionar la opción **7. Guardar y salir** antes de finalizar el programa. Los cambios realizados (países agregados o datos actualizados) se guardarán en el archivo `paises.csv`.



###  Ejemplos de Entradas y Salidas
El `README.md` debe incluir ejemplos de entradas y salidas para demostrar la funcionalidad:

| Funcionalidad | Entrada del Usuario | Salida del Programa |
| **Agregar País** (Opción 1) | Nombre: Atlantis, Continente: Desconocido, Población: 1000, Superficie: 500 | País 'Atlantis' agregado correctamente. |
| **Filtrar por Rango** (Opción 4) | Opción: 2 (Población) | Muestra una lista de países entre el rango de población especificado. |
| **Validación** | Población: `texto` | Entrada inválida. Por favor, ingresa un número entero. |
| **Mostrar Estadísticas** (Opción 6) | Opción: 6 | Muestra País con mayor/menor población, promedios y desglose por continente. |