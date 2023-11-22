import sqlite3
cnx = sqlite3.connect("tienda.db")
cursorbd = cnx.cursor()
# Grupos
cursorbd.execute("INSERT INTO grupos (idgrupos, nombre) VALUES (1, 'Electrónicos')")
cursorbd.execute("INSERT INTO grupos (idgrupos, nombre) VALUES (2, 'Ropa')")
cursorbd.execute("INSERT INTO grupos (idgrupos, nombre) VALUES (3, 'Hogar')")
cursorbd.execute("INSERT INTO grupos (idgrupos, nombre) VALUES (4, 'Deportes')")
cursorbd.execute("INSERT INTO grupos (idgrupos, nombre) VALUES (5, 'Juguetes')")

# Productos
cursorbd.execute("INSERT INTO productos (idproductos, nombre, precio, grupos_idgrupos) VALUES (1, 'Smartphone', 699.99, 1)")
cursorbd.execute("INSERT INTO productos (idproductos, nombre, precio, grupos_idgrupos) VALUES (2, 'Camisa', 29.99, 2)")
cursorbd.execute("INSERT INTO productos (idproductos, nombre, precio, grupos_idgrupos) VALUES (3, 'Aspiradora', 149.99, 3)")
cursorbd.execute("INSERT INTO productos (idproductos, nombre, precio, grupos_idgrupos) VALUES (4, 'Raqueta de tenis', 59.99, 4)")
cursorbd.execute("INSERT INTO productos (idproductos, nombre, precio, grupos_idgrupos) VALUES (5, 'Muñeca', 19.99, 5)")


# Ventas
cursorbd.execute("INSERT INTO Ventas (idventas, fecha, productos_idproductos) VALUES (1, '2023-01-01', 1)")
cursorbd.execute("INSERT INTO Ventas (idventas, fecha, productos_idproductos) VALUES (2, '2023-01-02', 2)")
cursorbd.execute("INSERT INTO Ventas (idventas, fecha, productos_idproductos) VALUES (3, '2023-01-03', 3)")
cursorbd.execute("INSERT INTO Ventas (idventas, fecha, productos_idproductos) VALUES (4, '2023-01-04', 4)")
cursorbd.execute("INSERT INTO Ventas (idventas, fecha, productos_idproductos) VALUES (5, '2023-01-05', 5)")


# Vendedores
cursorbd.execute("INSERT INTO vendedores (idvendedores, nombres, fecha_nac, ciudad, estado_civil, salario, ventas_idventas) VALUES (1, 'Juan Pérez', '1990-05-15', 'Ciudad A', 'Casado', 3000.00, 1)")
cursorbd.execute("INSERT INTO vendedores (idvendedores, nombres, fecha_nac, ciudad, estado_civil, salario, ventas_idventas) VALUES (2, 'Ana Gómez', '1985-08-22', 'Ciudad B', 'Soltero', 2500.00, 2)")
cursorbd.execute("INSERT INTO vendedores (idvendedores, nombres, fecha_nac, ciudad, estado_civil, salario, ventas_idventas) VALUES (3, 'Carlos López', '1992-03-10', 'Ciudad C', 'Casado', 2800.00, 3)")
cursorbd.execute("INSERT INTO vendedores (idvendedores, nombres, fecha_nac, ciudad, estado_civil, salario, ventas_idventas) VALUES (4, 'María Rodriguez', '1988-11-30', 'Ciudad A', 'Soltero', 2600.00, 4)")
cursorbd.execute("INSERT INTO vendedores (idvendedores, nombres, fecha_nac, ciudad, estado_civil, salario, ventas_idventas) VALUES (5, 'Pedro Martínez', '1995-07-05', 'Ciudad B', 'Casado', 3200.00, 5)")

cnx.commit()
cnx.close()