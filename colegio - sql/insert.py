import sqlite3
cnx = sqlite3.connect("colegio.db")
cursorbd = cnx.cursor()
# decanos
cursorbd.execute("INSERT INTO decanos (cedula, nombres, apellidos, celular) VALUES ('123456789', 'John', 'Doe', '555-1234')")
cursorbd.execute("INSERT INTO decanos (cedula, nombres, apellidos, celular) VALUES ('987654321', 'Jane', 'Smith', '555-5678')")
cursorbd.execute("INSERT INTO decanos (cedula, nombres, apellidos, celular) VALUES ('111222333', 'Robert', 'Johnson', '555-9876')")
cursorbd.execute("INSERT INTO decanos (cedula, nombres, apellidos, celular) VALUES ('444555666', 'Alice', 'Williams', '555-5432')")
cursorbd.execute("INSERT INTO decanos (cedula, nombres, apellidos, celular) VALUES ('777888999', 'David', 'Brown', '555-8765')")

# estudiantes
cursorbd.execute("INSERT INTO estudiantes (id, nombres, apellidos, direccion) VALUES (001, 'Michael', 'Jordan', '123 Main St')")
cursorbd.execute("INSERT INTO estudiantes (id, nombres, apellidos, direccion) VALUES (002, 'LeBron', 'James', '456 Oak St')")
cursorbd.execute("INSERT INTO estudiantes (id, nombres, apellidos, direccion) VALUES (003, 'Kobe', 'Bryant', '789 Pine St')")
cursorbd.execute("INSERT INTO estudiantes (id, nombres, apellidos, direccion) VALUES (004, 'Stephen', 'Curry', '321 Elm St')")
cursorbd.execute("INSERT INTO estudiantes (id, nombres, apellidos, direccion) VALUES (005, 'Kevin', 'Durant', '654 Birch St')")

# Asignaturas
cursorbd.execute("INSERT INTO asignaturas (codigo, nombres, num_creditos) VALUES ('A001', 'Mathematics', 3)")
cursorbd.execute("INSERT INTO asignaturas (codigo, nombres, num_creditos) VALUES ('A002', 'Physics', 4)")
cursorbd.execute("INSERT INTO asignaturas (codigo, nombres, num_creditos) VALUES ('A003', 'Chemistry', 3)")
cursorbd.execute("INSERT INTO asignaturas (codigo, nombres, num_creditos) VALUES ('A004', 'Computer Science', 4)")
cursorbd.execute("INSERT INTO asignaturas (codigo, nombres, num_creditos) VALUES ('A005', 'English', 3)")

# Facultades
cursorbd.execute("INSERT INTO falcultades (numero, nombres, ubicacion, decanos_cedula) VALUES (1, 'Engineering', 'Building A', '123456789')")
cursorbd.execute("INSERT INTO falcultades (numero, nombres, ubicacion, decanos_cedula) VALUES (2, 'Science', 'Building B', '987654321')")
cursorbd.execute("INSERT INTO falcultades (numero, nombres, ubicacion, decanos_cedula) VALUES (3, 'Arts', 'Building C', '111222333')")
cursorbd.execute("INSERT INTO falcultades (numero, nombres, ubicacion, decanos_cedula) VALUES (4, 'Business', 'Building D', '444555666')")
cursorbd.execute("INSERT INTO falcultades (numero, nombres, ubicacion, decanos_cedula) VALUES (5, 'Social Sciences', 'Building E', '777888999')")

# Docentes
cursorbd.execute("INSERT INTO docentes (cedula, nombres, apellidos, titulo, facultades_numero) VALUES ('111111111', 'Professor', 'One', 'Ph.D.', 1)")
cursorbd.execute("INSERT INTO docentes (cedula, nombres, apellidos, titulo, facultades_numero) VALUES ('222222222', 'Professor', 'Two', 'Ph.D.', 2)")
cursorbd.execute("INSERT INTO docentes (cedula, nombres, apellidos, titulo, facultades_numero) VALUES ('333333333', 'Professor', 'Three', 'Ph.D.', 3)")
cursorbd.execute("INSERT INTO docentes (cedula, nombres, apellidos, titulo, facultades_numero) VALUES ('444444444', 'Professor', 'Four', 'Ph.D.', 4)")
cursorbd.execute("INSERT INTO docentes (cedula, nombres, apellidos, titulo, facultades_numero) VALUES ('555555555', 'Professor', 'Five', 'Ph.D.', 5)")

#Cursos
cursorbd.execute("INSERT INTO cursos (id, docentes_cedula, asignaturas_codigo) VALUES (1, '111111111', 'A001')")
cursorbd.execute("INSERT INTO cursos (id, docentes_cedula, asignaturas_codigo) VALUES (2, '222222222', 'A002')")
cursorbd.execute("INSERT INTO cursos (id, docentes_cedula, asignaturas_codigo) VALUES (3, '333333333', 'A003')")
cursorbd.execute("INSERT INTO cursos (id, docentes_cedula, asignaturas_codigo) VALUES (4, '444444444', 'A004')")
cursorbd.execute("INSERT INTO cursos (id, docentes_cedula, asignaturas_codigo) VALUES (5, '555555555', 'A005')")

# Inscripciones
cursorbd.execute("INSERT INTO inscripciones (id, periodo, estudiantes_id, asignaturas_codigo) VALUES (1, '2023-01', 'E001', 'A001')")
cursorbd.execute("INSERT INTO inscripciones (id, periodo, estudiantes_id, asignaturas_codigo) VALUES (2, '2023-01', 'E002', 'A002')")
cursorbd.execute("INSERT INTO inscripciones (id, periodo, estudiantes_id, asignaturas_codigo) VALUES (3, '2023-01', 'E003', 'A003')")
cursorbd.execute("INSERT INTO inscripciones (id, periodo, estudiantes_id, asignaturas_codigo) VALUES (4, '2023-01', 'E004', 'A004')")
cursorbd.execute("INSERT INTO inscripciones (id, periodo, estudiantes_id, asignaturas_codigo) VALUES (5, '2023-01', 'E005', 'A005')")


cnx.commit()
cnx.close()