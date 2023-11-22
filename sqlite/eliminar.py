import sqlite3

bd=sqlite3.connect("mi_bd.db")
cursor=bd.cursor()
nombre=input("\nNombre: ")
sentencia="DELETE FROM persona WHERE nombre =?"
cursor.execute(sentencia, (nombre,))
bd.commit()
bd.close()
print("Eliminado correctamente")