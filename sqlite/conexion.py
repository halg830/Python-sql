import sqlite3
cnx = sqlite3.connect("mibd.bd")
#CURSOR para comunicarse con la base de datos
cursorbd = cnx.cursor()
# cursorbd.execute("CREATE TABLE IF NOT EXISTS persona(nombre TEXT, apellido TEXT, edad INTEGER)")
cursorbd.execute("""CREATE TABLE IF NOT EXISTS persona
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 nombre TEXT NOT NULL,
                 apellido TEXT NOT NULL,
                 edad INTEGER CHECK (edad>0))
                 """)
cnx.commit()
cnx.close()