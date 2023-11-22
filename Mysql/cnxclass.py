import mysql.connector
class ConexionSG:
    __conexion = None

    @staticmethod
    def get_conexion(bd):
        if ConexionSG.__conexion == None:
            ConexionSG.__conexion = mysql.connector.connect(host='localhost',
                                                  database=bd,
                                                  user='root',
                                                  password='1234')
        return ConexionSG.__conexion