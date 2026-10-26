# NovaStore — Análisis de ventas
## 1. Descripción del proyecto

NovaStore es un caso práctico ficticio de análisis de datos comerciales. El objetivo es analizar los datos de ventas de la empresa para comprender su rendimiento, identificar tendencias y comparar los resultados entre ciudades y categorías de productos.

## 2. Objetivo de negocio

El análisis busca responder preguntas como:

- ¿Qué ciudades y categorías generan más ingresos?
- ¿Cómo evolucionan los ingresos a lo largo del tiempo?
- ¿Cómo se comparan los márgenes brutos entre ciudades?
- ¿Qué ciudades podrían necesitar una revisión de su rendimiento?

## 3. Herramientas utilizadas

- **MySQL:** consulta y extracción de datos mediante SQL y JOIN.
- **Python:** conexión con la base de datos y procesamiento de la información.
- **Pandas:** limpieza y transformación de los datos.
- **Power BI:** creación de dashboards, indicadores y medidas DAX.

## 4. Proceso de trabajo

1. Extracción de datos relacionados de las tablas de ventas, clientes y productos.
2. Inspección del conjunto de datos original.
3. Conversión de fechas y corrección de textos con problemas de codificación.
4. Identificación y exclusión de registros con cantidades inferiores a 1, según el criterio definido para este análisis.
5. Exportación de los datos preparados a Excel.
6. Desarrollo de un informe interactivo en Power BI para analizar los ingresos, los márgenes y la evolución temporal.

## 5. Resultados del procesamiento

- Registros originales de ventas: 3.172.
- Registros después de la limpieza: 3.164.
- Registros excluidos por cantidad inferior a 1: 8.
- Columnas del conjunto de datos final: 12.

## 6. Dashboard de Power BI

El informe contiene tres páginas:

- **Rendimiento de ventas:** ingresos, costes, ganancias brutas y márgenes.
- **Evolución de ingresos:** comparación interanual, variación porcentual e ingresos acumulados del año.
- **Comparación entre ciudades:** participación en los ingresos, comparación de márgenes y clasificación de prioridades.

## 7. Archivos del proyecto

- Consulta SQL utilizada para extraer los datos.
- Código Python para la preparación de los datos.
- Archivo Excel con los datos procesados.
- Capturas de evidencia del proceso y del informe de Power BI.
- Archivo de Power BI.

## 8. Limitaciones

NovaStore es una empresa ficticia y los resultados corresponden a un conjunto de datos de práctica. Las conclusiones y recomendaciones deben interpretarse dentro de ese contexto.

## 9. Autoría

Proyecto personal de práctica orientado al análisis de datos comerciales mediante SQL, Python, Pandas y Power BI.