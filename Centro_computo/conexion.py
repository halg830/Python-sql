import sqlite3
cnx = sqlite3.connect("centro_computo.db")
#CURSOR para comunicarse con la base de datos
cursorbd = cnx.cursor()
cursorbd.execute("""CREATE TABLE IF NOT EXISTS centro_computo
                 (id INTEGER PRIMARY KEY NOT NULL,
                 responsable TEXT NOT NULL,
                 direccion TEXT NOT NULL)
                 """)
cursorbd.execute("""CREATE TABLE IF NOT EXISTS usuarios
                 (identificacion TEXT PRIMARY KEY NOT NULL,
                 nombres TEXT NOT NULL,
                 apellidos TEXT NOT NULL,
                 direccion TEXT NOT NULL,
                 telefono TEXT NOT NULL)
                 """)
cursorbd.execute("""CREATE TABLE IF NOT EXISTS equipos
                 (codigo TEXT PRIMARY KEY NOT NULL,
                 marca TEXT NOT NULL,
                 modelo TEXT NOT NULL,
                 ram INTEGER NOT NULL,
                 disco INTEGER NOT NULL)
                 """)
cursorbd.execute("""CREATE TABLE IF NOT EXISTS personal_tecnico
                 (identificacion TEXT PRIMARY KEY NOT NULL,
                 nombres TEXT NOT NULL,
                 apellidos TEXT NOT NULL,
                 direccion TEXT NOT NULL,
                 telefono TEXT NOT NULL,
                 centro_computo INTEGER NOT NULL,
                 FOREIGN KEY (centro_computo) REFERENCES centro_computo(codigo))
                 """)
cursorbd.execute("""CREATE TABLE IF NOT EXISTS soporte_tecnico
                 (id INTEGER PRIMARY KEY NOT NULL,
                 fecha_recepcion DATE NOT NULL,
                 fecha_entrega DATE NOT NULL,
                 diagnostico TEXT NOT NULL,
                 observaciones TEXT NOT NULL,
                 equipos TEXT NOT NULL,
                 personal_tecnico TEXT NOT NULL,
                 FOREIGN KEY (equipos) REFERENCES equipos(codigo),
                 FOREIGN KEY (personal_tecnico) REFERENCES personal_tecnico(identificacion))
                 """)
cursorbd.execute("""CREATE TABLE IF NOT EXISTS cuentas
                 (id INTEGER PRIMARY KEY NOT NULL,
                 nombre TEXT NOT NULL,
                 password TEXT NOT NULL,
                 fecha_creacion DATE NOT NULL,
                 fecha_activa DATE NOT NULL,
                 fecha_inactiva DATE NOT NULL,
                 estado TEXT NOT NULL,
                 equipos TEXT NOT NULL,
                 usuarios TEXT NOT NULL,
                 FOREIGN KEY (equipos) REFERENCES equipos(codigo),
                 FOREIGN KEY (usuarios) REFERENCES usuarios(identificacion))
                 """)
cnx.commit()
cnx.close()