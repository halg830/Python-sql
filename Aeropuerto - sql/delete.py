import sqlite3
cnx=sqlite3.connect("aeropuerto.db")
cursorbd=cnx.cursor()
cursorbd.execute("DELETE FROM clientes WHERE id = 1")
cursorbd.execute("DELETE FROM aeropuerto WHERE codigo = 1")
cursorbd.execute("DELETE FROM aviones WHERE codigo = 1")
cursorbd.execute("DELETE FROM tarjetas_credito WHERE cliente_id = 3")
cursorbd.execute("DELETE FROM tarjeta_embarque WHERE codigo = 1")
cursorbd.execute("DELETE FROM vuelos WHERE codigo = 1")
cursorbd.execute("DELETE FROM reservas WHERE codigo = 1")
cursorbd.execute("DELETE FROM plazas WHERE codigo = 1")

cnx.commit()