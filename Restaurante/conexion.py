import sqlite3
cnx = sqlite3.connect("restaurante.db")
#CURSOR para comunicarse con la base de datos
cursorbd = cnx.cursor()
cursorbd.execute("""CREATE TABLE IF NOT EXISTS cargos
                 (id INTEGER PRIMARY KEY NOT NULL,
                 nombre TEXT NOT NULL)
                 """)
cursorbd.execute("""CREATE TABLE IF NOT EXISTS almacen
                 (id INTEGER PRIMARY KEY NOT NULL,
                 nombres TEXT NOT NULL,
                 descripcion TEXT NOT NULL)
                 """)
cursorbd.execute("""CREATE TABLE IF NOT EXISTS pedido
                 (id INTEGER PRIMARY KEY NOT NULL,
                 fecha DATE NOT NULL,
                 mesa TEXT NOT NULL,
                 valor FLOAT NOT NULL,
                 estado TEXT NOT NULL)
                 """)
cursorbd.execute("""CREATE TABLE IF NOT EXISTS recetas
                 (id INTEGER PRIMARY KEY NOT NULL,
                 descripcion TEXT NOT NULL,
                 fecha_creacion DATE NOT NULL)
                 """)
cursorbd.execute("""CREATE TABLE IF NOT EXISTS ingredientes
                 (codigo TEXT PRIMARY KEY NOT NULL,
                 nombre TEXT NOT NULL,
                 unidad_medida FLOAT NOT NULL,
                 presentacion TEXT NOT NULL,
                 costo FLOAT NOT NULL)
                 """)
cursorbd.execute("""CREATE TABLE IF NOT EXISTS empleados
                 (identificacion TEXT PRIMARY KEY NOT NULL,
                 nombres TEXT NOT NULL,
                 apellidos TEXT NOT NULL,
                 direccion TEXT NOT NULL,
                 telefono_fijo TEXT,
                 telefono_movil TEXT NOT NULL,
                 tiempo_servicio FLOAT NOT NULL,
                 especialidad TEXT NOT NULL,
                 cargos INT NOT NULL,
                 FOREIGN KEY (cargos) REFERENCES cargos(id))
                 """)
cursorbd.execute("""CREATE TABLE IF NOT EXISTS cocineros_ayudantes
                 (id INTEGER PRIMARY KEY NOT NULL,
                 cocinero TEXT NOT NULL,
                 ayudante TEXT NOT NULL,
                 FOREIGN KEY (cocinero) REFERENCES empleados(identificacion),
                 FOREIGN KEY (ayudante) REFERENCES empleados(identificacion))
                 """)
cursorbd.execute("""CREATE TABLE IF NOT EXISTS platos
                 (id INTEGER PRIMARY KEY NOT NULL,
                 nombre TEXT NOT NULL,
                 costo FLOAT NOT NULL,
                 tipo_plato TEXT NOT NULL,
                 descripcion TEXT NOT NULL,
                 recetas INTEGER NOT NULL,
                 FOREIGN KEY (recetas) REFERENCES recetas(id))
                 """)
cursorbd.execute("""CREATE TABLE IF NOT EXISTS detalle_pedido
                 (id TEXT PRIMARY KEY NOT NULL,
                 cantidad FLOAT NOT NULL,
                 valor_unitario FLOAT NOT NULL,
                 pedido INTEGER NOT NULL,
                 platos INTEGER NOT NULL,
                 FOREIGN KEY (pedido) REFERENCES pedido(id),
                 FOREIGN KEY (platos) REFERENCES platos(id))
                 """)
cursorbd.execute("""CREATE TABLE IF NOT EXISTS preparaciones
                 (id INTEGER PRIMARY KEY NOT NULL,
                 observacion TEXT NOT NULL,
                 empleados TEXT NOT NULL,
                 platos INTEGER NOT NULL,
                 FOREIGN KEY (empleados) REFERENCES empleados(identificacion),
                 FOREIGN KEY (platos) REFERENCES platos(id))
                 """)
cursorbd.execute("""CREATE TABLE IF NOT EXISTS distribucion_estantes
                 (id INTEGER PRIMARY KEY NOT NULL,
                 codigo_estante TEXT NOT NULL,
                 nombre TEXT NOT NULL,
                 almacen INTEGER NOT NULL,
                 FOREIGN KEY (almacen) REFERENCES almacen(id))
                 """)
cursorbd.execute("""CREATE TABLE IF NOT EXISTS inventario
                 (id INTEGER PRIMARY KEY NOT NULL,
                 cantidad FLOAT NOT NULL,
                 estado TEXT NOT NULL,
                 distribuciones_estantes INTEGER NOT NULL,
                 ingredientes TEXT NOT NULL,
                 FOREIGN KEY (distribuciones_estantes) REFERENCES distribuciones_estantes(id),
                 FOREIGN KEY (ingredientes) REFERENCES ingredientes(codigo))
                 """)
cursorbd.execute("""CREATE TABLE IF NOT EXISTS detalle_receta
                 (id INTEGER PRIMARY KEY NOT NULL,
                 cantidad FLOAT NOT NULL,
                 recetas INTEGER NOT NULL,
                 ingredientes TEXT NOT NULL,
                 FOREIGN KEY (recetas) REFERENCES recetas(id),
                 FOREIGN KEY (ingredientes) REFERENCES ingredientes(codigo))
                 """)
cnx.commit()
cnx.close()