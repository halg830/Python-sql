import mysql.connector

conexion = mysql.connector.connect(host='localhost',
                                   database='mydb',
                                   user='root',
                                   password='1234')
if conexion.is_connected():
    print ("Conexion exitosa a la base de datos")

conexion.close()