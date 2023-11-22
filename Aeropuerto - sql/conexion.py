import sqlite3
cnx = sqlite3.connect("aeropuerto.db")
#CURSOR para comunicarse con la base de datos
cursorbd = cnx.cursor()
cursorbd.execute("INSERT INTO clientes (id, nombres, apellidos, direccion, celular) VALUES (1, 'Juan', 'Perez', 'Calle 123', '555-1234')")
cursorbd.execute("INSERT INTO clientes (id, nombres, apellidos, direccion, celular) VALUES (2, 'Ana', 'Gomez', 'Avenida 456', '555-5678')")
cursorbd.execute("INSERT INTO clientes (id, nombres, apellidos, direccion, celular) VALUES (3, 'Carlos', 'Lopez', 'Carrera 789', '555-9876')")
cursorbd.execute("INSERT INTO clientes (id, nombres, apellidos, direccion, celular) VALUES (4, 'Maria', 'Rodriguez', 'Pasaje 321', '555-5432')")
cursorbd.execute("INSERT INTO clientes (id, nombres, apellidos, direccion, celular) VALUES (5, 'Pedro', 'Martinez', 'Plaza 654', '555-8765')")

cursorbd.execute("INSERT INTO aeropuerto (codigo, nombres, localidad, pais) VALUES (1, 'Aeropuerto Internacional A', 'Ciudad A', 'Pais A')")
cursorbd.execute("INSERT INTO aeropuerto (codigo, nombres, localidad, pais) VALUES (2, 'Aeropuerto Internacional B', 'Ciudad B', 'Pais B')")
cursorbd.execute("INSERT INTO aeropuerto (codigo, nombres, localidad, pais) VALUES (3, 'Aeropuerto Internacional C', 'Ciudad C', 'Pais C')")
cursorbd.execute("INSERT INTO aeropuerto (codigo, nombres, localidad, pais) VALUES (4, 'Aeropuerto Internacional D', 'Ciudad D', 'Pais D')")
cursorbd.execute("INSERT INTO aeropuerto (codigo, nombres, localidad, pais) VALUES (5, 'Aeropuerto Internacional E', 'Ciudad E', 'Pais E')")

cursorbd.execute("INSERT INTO aviones (codigo, nombres, num_plazas) VALUES (1, 'Boeing 747', 500)")
cursorbd.execute("INSERT INTO aviones (codigo, nombres, num_plazas) VALUES (2, 'Airbus A380', 550)")
cursorbd.execute("INSERT INTO aviones (codigo, nombres, num_plazas) VALUES (3, 'Boeing 737', 200)")
cursorbd.execute("INSERT INTO aviones (codigo, nombres, num_plazas) VALUES (4, 'Airbus A320', 180)")
cursorbd.execute("INSERT INTO aviones (codigo, nombres, num_plazas) VALUES (5, 'Boeing 777', 350)")

cursorbd.execute("INSERT INTO tarjetas_credito (codigo, cliente_id) VALUES ('1234567890123456', 1)")
cursorbd.execute("INSERT INTO tarjetas_credito (codigo, cliente_id) VALUES ('9876543210987654', 2)")
cursorbd.execute("INSERT INTO tarjetas_credito (codigo, cliente_id) VALUES ('1111222233334444', 3)")
cursorbd.execute("INSERT INTO tarjetas_credito (codigo, cliente_id) VALUES ('5555666677778888', 4)")
cursorbd.execute("INSERT INTO tarjetas_credito (codigo, cliente_id) VALUES ('9999888877776666', 5)")

cursorbd.execute("INSERT INTO tarjeta_embarque (codigo, numero_asiento, fila, columna, planta, cliente_id) VALUES (1, '10A', '10', 'A', 'Superior', 1)")
cursorbd.execute("INSERT INTO tarjeta_embarque (codigo, numero_asiento, fila, columna, planta, cliente_id) VALUES (2, '15B', '15', 'B', 'Inferior', 2)")
cursorbd.execute("INSERT INTO tarjeta_embarque (codigo, numero_asiento, fila, columna, planta, cliente_id) VALUES (3, '20C', '20', 'C', 'Superior', 3)")
cursorbd.execute("INSERT INTO tarjeta_embarque (codigo, numero_asiento, fila, columna, planta, cliente_id) VALUES (4, '25D', '25', 'D', 'Inferior', 4)")
cursorbd.execute("INSERT INTO tarjeta_embarque (codigo, numero_asiento, fila, columna, planta, cliente_id) VALUES (5, '30E', '30', 'E', 'Superior', 5)")

cursorbd.execute("INSERT INTO vuelos (codigo, fecha, hora_salida, hora_llegada, aviones_codigo, aeropuerto_codigo) VALUES (1, '2023-01-01', 10, 15, 1, 1)")
cursorbd.execute("INSERT INTO vuelos (codigo, fecha, hora_salida, hora_llegada, aviones_codigo, aeropuerto_codigo) VALUES (2, '2023-01-02', 12, 17, 2, 2)")
cursorbd.execute("INSERT INTO vuelos (codigo, fecha, hora_salida, hora_llegada, aviones_codigo, aeropuerto_codigo) VALUES (3, '2023-01-03', 14, 19, 3, 3)")
cursorbd.execute("INSERT INTO vuelos (codigo, fecha, hora_salida, hora_llegada, aviones_codigo, aeropuerto_codigo) VALUES (4, '2023-01-04', 16, 21, 4, 4)")
cursorbd.execute("INSERT INTO vuelos (codigo, fecha, hora_salida, hora_llegada, aviones_codigo, aeropuerto_codigo) VALUES (5, '2023-01-05', 18, 23, 5, 5)")

cursorbd.execute("INSERT INTO reservas (codigo, fecha, num_plazas, clientes_id, vuelos_codigo) VALUES (1, '2023-01-01', 2, 1, 1)")
cursorbd.execute("INSERT INTO reservas (codigo, fecha, num_plazas, clientes_id, vuelos_codigo) VALUES (2, '2023-01-02', 1, 2, 2)")
cursorbd.execute("INSERT INTO reservas (codigo, fecha, num_plazas, clientes_id, vuelos_codigo) VALUES (3, '2023-01-03', 3, 3, 3)")
cursorbd.execute("INSERT INTO reservas (codigo, fecha, num_plazas, clientes_id, vuelos_codigo) VALUES (4, '2023-01-04', 2, 4, 4)")
cursorbd.execute("INSERT INTO reservas (codigo, fecha, num_plazas, clientes_id, vuelos_codigo) VALUES (5, '2023-01-05', 1, 5, 5)")

cursorbd.execute("INSERT INTO plazas (codigo, numero, columna, fila, planta, disponible, tarjeta_embarque, aviones_codigo) VALUES (1, '10', 'A', '10', 'Superior', 1, 1, 1)")
cursorbd.execute("INSERT INTO plazas (codigo, numero, columna, fila, planta, disponible, tarjeta_embarque, aviones_codigo) VALUES (2, '15', 'B', '15', 'Inferior', 1, 2, 2)")
cursorbd.execute("INSERT INTO plazas (codigo, numero, columna, fila, planta, disponible, tarjeta_embarque, aviones_codigo) VALUES (3, '20', 'C', '20', 'Superior', 1, 3, 3)")
cursorbd.execute("INSERT INTO plazas (codigo, numero, columna, fila, planta, disponible, tarjeta_embarque, aviones_codigo) VALUES (4, '25', 'D', '25', 'Inferior', 1, 4, 4)")
cursorbd.execute("INSERT INTO plazas (codigo, numero, columna, fila, planta, disponible, tarjeta_embarque, aviones_codigo) VALUES (5, '30', 'E', '30', 'Superior', 1, 5, 5)")

cnx.commit()
cnx.close()