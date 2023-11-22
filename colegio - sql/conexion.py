import sqlite3
cnx = sqlite3.connect("colegio.db")
#CURSOR para comunicarse con la base de datos
cursorbd = cnx.cursor()
cursorbd.execute("""CREATE TABLE IF NOT EXISTS decanos
                 (cedula TEXT PRIMARY KEY NOT NULL,
                 nombres TEXT NOT NULL,
                 apellidos TEXT NOT NULL,
                 celular TEXT NOT NULL)
                 """)
cursorbd.execute("""CREATE TABLE IF NOT EXISTS estudiantes
                 (id INTEGER PRIMARY KEY NOT NULL,
                 nombres TEXT NOT NULL,
                 apellidos TEXT NOT NULL,
                 direccion TEXT NOT NULL)
                 """)
cursorbd.execute("""CREATE TABLE IF NOT EXISTS asignaturas
                 (codigo TEXT PRIMARY KEY NOT NULL,
                 nombres TEXT NOT NULL,
                 num_creditos INTEGER NOT NULL)
                 """)
cursorbd.execute("""CREATE TABLE IF NOT EXISTS falcultades
                 (numero INTEGER PRIMARY KEY NOT NULL,
                 nombres TEXT NOT NULL,
                 ubicacion TEXT NOT NULL,
                 decanos_cedula TEXT NOT NULL,
                 FOREIGN KEY (decanos_cedula) REFERENCES decanos(cedula))
                 """)
cursorbd.execute("""CREATE TABLE IF NOT EXISTS docentes
                 (cedula TEXT PRIMARY KEY NOT NULL,
                 nombres TEXT NOT NULL,
                 apellidos TEXT NOT NULL,
                 titulo TEXT NOT NULL,
                 facultades_numero TEXT NOT NULL,
                 FOREIGN KEY (facultades_numero) REFERENCES facultades(numero))
                 """)
cursorbd.execute("""CREATE TABLE IF NOT EXISTS cursos
                 (id INTEGER PRIMARY KEY NOT NULL,
                 docentes_cedula TEXT NOT NULL,
                 asignaturas_codigo TEXT NOT NULL,
                 FOREIGN KEY (docentes_cedula) REFERENCES docentes(cedula),
                 FOREIGN KEY (asignaturas_codigo) REFERENCES asignaturas(numero))
                 """)
cursorbd.execute("""CREATE TABLE IF NOT EXISTS inscripciones
                 (id INTEGER PRIMARY KEY NOT NULL,
                 periodo TEXT NOT NULL,
                 estudiantes_id INTEGER NOT NULL,
                 asignaturas_codigo TEXT NOT NULL,
                 FOREIGN KEY (estudiantes_id) REFERENCES estudiantes(id),
                 FOREIGN KEY (asignaturas_codigo) REFERENCES asignaturas(numero))
                 """)
cnx.commit()
cnx.close()