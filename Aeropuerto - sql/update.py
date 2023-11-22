import sqlite3
cnx = sqlite3.connect("aeropuerto.db")
cursorbd = cnx.cursor()
cursorbd.execute("UPDATE clientes SET nombres = 'Juan Modificado' WHERE id = 1")
cursorbd.execute("UPDATE aeropuerto SET nombres = 'Aeropuerto Internacional A Modificado' WHERE codigo = 1")
cursorbd.execute("UPDATE aviones SET nombres = 'Boeing 747 Modificado' WHERE codigo = 1")
cursorbd.execute("UPDATE tarjetas_credito SET codigo = '1111222233334444 Modificado' WHERE cliente_id = 3")
cursorbd.execute("UPDATE tarjeta_embarque SET numero_asiento = '11A' WHERE codigo = 1")
cursorbd.execute("UPDATE vuelos SET hora_salida = 11 WHERE codigo = 1")
cursorbd.execute("UPDATE reservas SET num_plazas = 3 WHERE codigo = 1")
cursorbd.execute("UPDATE plazas SET disponible = 0 WHERE codigo = 1")

cnx.commit()
cnx.close()