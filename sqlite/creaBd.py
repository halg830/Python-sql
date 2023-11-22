import sqlite3
con = sqlite3.connect("mi_bd.db")
cursor = con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS persona (nombre TEXT, edad INTEGER)")
con.commit()
con.close()