import sqlite3
cnx=sqlite3.connect("mi_bd.db")
cursor=cnx.cursor()
cursor.execute("DELETE FROM persona WHERE nombre = 'Raul Castro'")
cnx.commit()