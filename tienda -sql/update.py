import sqlite3
cnx = sqlite3.connect("tienda.db")
cursor = cnx.cursor()
cursor.execute("UPDATE grupos SET nombre = 'Raul' WHERE nombre = 'Ropa'")
cursor.execute("UPDATE productos SET precio = '10.2' WHERE nombre = 'Camisa'")
cursor.execute("UPDATE Ventas SET fecha = '2023-02-01' WHERE idventas = 1")
cursor.execute("UPDATE vendedores SET salario = 3500.00 WHERE idvendedores = 1")

cnx.commit()
cnx.close()