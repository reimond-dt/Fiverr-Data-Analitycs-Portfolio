#Importamos las librerias para poder hacer las limpiezas, transformaciones y conexiones 
import pandas as pd
import mysql.connector 

#Pones los datos para ingresar en la Base de Datos
#Los parametros de conexion son del local

config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'proyecto_ventas',
    'port': 3306
}

conexion = mysql.connector.connect(**config)

#Iniciamos la consulta para extraer de la Base de Datos una tabla con informacion para limpiar y transformarla para
#no obtener errores o tener texto sucios para cuando la pasemos al Power BI

query = """
SELECT venta_id, nombre, ciudad, segmento, categoria, producto, cantidad, fecha, precio_unitario, 
coste_unitario, descuento_pct, precio_lista FROM productos JOIN ventas 
ON productos.producto_id = ventas.producto_id
JOIN clientes
ON clientes.cliente_id = ventas.cliente_id
"""

#Conectamos la consulta y la conexion de Mysql para asi obtener la tabla entera que necesitamos

df = pd.read_sql(query, conexion)
#Información de la tabla antes de limpiarla y transformarla
df_sucio = df.info()
print(df_sucio)
#Transformamos la columna fecha a un tipo de dato de tiempo para poder hacer analisis de tiempo
df["fecha"] = pd.to_datetime(df['fecha'])
#Informacion de antes de limpiar los productos y categorias de nuestro dataframe 
productos_anteriores = df["producto"].unique()
categorias_anteriores = df["categoria"].unique()
#Limpieza de texto
df["producto"] = (df["producto"].str.replace("Auriculares inalÃ¡mbricos", "Auriculares inalambricos")
.str.replace("RatÃ³n inalÃ¡mbrico", "Raton inalambrico")
.str.replace("Teclado mecÃ¡nico", "Teclado mecanico")
.str.replace("Botella tÃ©rmica", "Botella termica")
.str.replace("Silla ergonÃ³mica", "Silla ergonomica")
.str.replace("Juego de sÃ¡banas", "Juego de sabanas")
.str.replace("LÃ¡mpara de escritorio", "Lampara de escritorio")
)
df["categoria"] = df["categoria"].str.replace("TecnologÃ­a", "Tecnologia")
#Aqui se detecto que habian 0  y negativos en las cantidades por lo cual nuestro cliente nos pidio 
#que no teniamos que aceptar esos 0 y negativos para los calculos
df = df[df["cantidad"] >= 1]
#Aqui como ya hicimos la limpieza y la transformación ya podemos extrar el Dataframe a Excel 
#df.to_excel("analisis de ventas 2024 a 2025.xlsx", index=False)