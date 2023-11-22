import mysql.connector
from cnxclass import ConexionSG

conexion = ConexionSG.get_conexion("mydb")
cursor = conexion.cursor()
cursor.execute("""INSERT INTO productos
                  (codigo, nombre, cantidad, precio, categoria_codigo) VALUES
                  (1, 'Producto1', 5, 3.99, 333)""")
cursor.execute("""INSERT INTO productos
                  (codigo, nombre, cantidad, precio, categoria_codigo) VALUES
                  (2, 'Producto2', 10, 7.99, 333)""")
cursor.execute("""INSERT INTO productos
                  (codigo, nombre, cantidad, precio, categoria_codigo) VALUES
                  (3, 'Producto3', 10, 7.99, 334)""")
cursor.execute("""INSERT INTO productos
                  (codigo, nombre, cantidad, precio, categoria_codigo) VALUES
                  (4, 'Producto4', 10, 7.99, 334)""")
cursor.execute("""INSERT INTO productos
                  (codigo, nombre, cantidad, precio, categoria_codigo) VALUES
                  (5, 'Producto5', 10, 7.99, 335)""")
cursor.execute("""INSERT INTO productos
                  (codigo, nombre, cantidad, precio, categoria_codigo) VALUES
                  (6, 'Producto6', 10, 7.99, 335)""")
cursor.execute("""INSERT INTO productos
                  (codigo, nombre, cantidad, precio, categoria_codigo) VALUES
                  (7, 'Producto7', 10, 7.99, 336)""")
cursor.execute("""INSERT INTO productos
                  (codigo, nombre, cantidad, precio, categoria_codigo) VALUES
                  (8, 'Producto8', 10, 7.99, 336)""")
cursor.execute("""INSERT INTO productos
                  (codigo, nombre, cantidad, precio, categoria_codigo) VALUES
                  (9, 'Producto9', 10, 7.99, 337)""")
cursor.execute("""INSERT INTO productos
                  (codigo, nombre, cantidad, precio, categoria_codigo) VALUES
                  (10, 'Producto10', 10, 7.99, 337)""")

conexion.commit()