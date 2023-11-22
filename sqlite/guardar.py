import sqlite3

bd = sqlite3.connect("mi_bd.db")
cursor = bd.cursor()
nombre= input("\nNombre: ")
edad=input("\nEdad: ")
sentencia = "INSERT INTO persona(nombre, edad) VALUES (?,?)"
cursor.execute(sentencia, [nombre, edad])
bd.commit()
bd.close()
print("Guardado correctamente")