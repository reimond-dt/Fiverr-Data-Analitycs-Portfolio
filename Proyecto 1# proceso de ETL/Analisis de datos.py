import pandas as pd
import mysql.connector 

config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'proyecto_ventas',
    'port': 3306
}

conexion = mysql.connector.connect(**config)
query = """
SELECT venta_id, nombre, ciudad, segmento, categoria, producto, cantidad, fecha, precio_unitario, 
coste_unitario, descuento_pct, precio_lista FROM productos JOIN ventas 
ON productos.producto_id = ventas.producto_id
JOIN clientes
ON clientes.cliente_id = ventas.cliente_id
"""
df = pd.read_sql(query, conexion)
df_sucio = df.info()
df["fecha"] = pd.to_datetime(df['fecha'])
productos_anteriores = df["producto"].unique()
categorias_anteriores = df["categoria"].unique()
df["producto"] = (df["producto"].str.replace("Auriculares inalÃ¡mbricos", "Auriculares inalambricos")
.str.replace("RatÃ³n inalÃ¡mbrico", "Raton inalambrico")
.str.replace("Teclado mecÃ¡nico", "Teclado mecanico")
.str.replace("Botella tÃ©rmica", "Botella termica")
.str.replace("Silla ergonÃ³mica", "Silla ergonomica")
.str.replace("Juego de sÃ¡banas", "Juego de sabanas")
.str.replace("LÃ¡mpara de escritorio", "Lampara de escritorio")
)
df["categoria"] = df["categoria"].str.replace("TecnologÃ­a", "Tecnologia")
df = df[df["cantidad"] >= 1]

df.to_excel("analisis de ventas 2024 a 2025", index=False)