import sqlite3
cnx = sqlite3.connect("mi_bd.db")
cursor = cnx.cursor()
cursor.execute("SELECT * FROM persona")
result = cursor.fetchall()
print(result)
for registro in result:
    print("Nombre: ", registro[0], "Edad: ", registro[1])

cursor = cnx.cursor()
cursor.execute("SELECT edad FROM persona WHERE nombre = 'Juan Garcia'")
result = cursor.fetchone()
print("Edad de Juan: ", result[0])