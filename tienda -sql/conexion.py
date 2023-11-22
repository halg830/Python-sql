import sqlite3
cnx = sqlite3.connect("tienda.db")
cursorbd = cnx.cursor()
cursorbd.execute("""CREATE TABLE IF NOT EXISTS grupos
                 (idgrupos INTEGER PRIMARY KEY NOT NULL,
                 nombre TEXT NOT NULL)
                 """)
cursorbd.execute("""CREATE TABLE IF NOT EXISTS productos
                 (idproductos INTEGER PRIMARY KEY NOT NULL,
                 nombre TEXT NOT NULL,
                 precio DECIMAL NOT NULL,
                 grupos_idgrupos INTEGER NOT NULL, 
                 FOREIGN KEY (grupos_idgrupos) REFERENCES grupos(idgrupos))
                 """)
cursorbd.execute("""CREATE TABLE IF NOT EXISTS Ventas
                 (idventas INTEGER PRIMARY KEY NOT NULL,
                 fecha DATE NOT NULL,
                 productos_idproductos INTEGER NOT NULL, 
                 FOREIGN KEY (productos_idproductos) REFERENCES productos(idproductos))
                 """)
cursorbd.execute("""CREATE TABLE IF NOT EXISTS vendedores
                 (idvendedores INTEGER PRIMARY KEY NOT NULL,
                 nombres TEXT NOT NULL,
                 fecha_nac DATE NOT NULL,
                 ciudad TEXT NOT NULL,
                 estado_civil TEXT NOT NULL,
                 salario DECIMAL NOT NULL,
                 ventas_idventas INTEGER NOT NULL,
                 FOREIGN KEY (ventas_idventas) REFERENCES ventas(idventas))
                 """)
cnx.commit()
cnx.close()