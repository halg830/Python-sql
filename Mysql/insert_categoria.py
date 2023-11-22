import mysql.connector
from cnxclass import ConexionSG

conexion = ConexionSG.get_conexion("mydb")
cursor = conexion.cursor()
cursor.execute ("""INSERT INTO categoria
                   (codigo, nombre) VALUES
                   (333, 'Infantil')""")
cursor.execute("""INSERT INTO categoria
                  (codigo, nombre) VALUES
                  (334, 'Adultos')""")
cursor.execute("""INSERT INTO categoria
                  (codigo, nombre) VALUES
                  (335, 'Ficción')""")
cursor.execute("""INSERT INTO categoria
                  (codigo, nombre) VALUES
                  (336, 'No ficción')""")
cursor.execute("""INSERT INTO categoria
                  (codigo, nombre) VALUES
                  (337, 'Romance')""")
conexion.commit()