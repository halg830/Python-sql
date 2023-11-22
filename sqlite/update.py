import sqlite3
cnx = sqlite3.connect("mi_bd.db")
cursor = cnx.cursor()
cursor.execute("UPDATE persona SET nombre = 'Lina Maria' WHERE nombre = 'Lina Estrada'")
cursor.execute("UPDATE persona SET edad = 26 WHERE nombre = 'Juan Garcia'")
cnx.commit()
cnx.close()