import sqlite3
cnx=sqlite3.connect("tienda.db")
cursorbd=cnx.cursor()
cursorbd.execute("DELETE FROM grupos WHERE idgrupos = 1")
cursorbd.execute("DELETE FROM productos WHERE idproductos = 1")
cursorbd.execute("DELETE FROM Ventas WHERE idventas = 1")
cursorbd.execute("DELETE FROM vendedores WHERE idvendedores = 1")

cnx.commit()