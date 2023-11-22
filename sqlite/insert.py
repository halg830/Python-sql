import sqlite3
cnx = sqlite3.connect("mi_bd.db")
cursordb = cnx.cursor()
cursordb.execute("insert into persona values ('Juan Garcia', 25)")
cursordb.execute("insert into persona values ('Lina Estrada', 47)")
cursordb.execute("insert into persona values ('Raul Castro', 53)")
cnx.commit()
cnx.close()