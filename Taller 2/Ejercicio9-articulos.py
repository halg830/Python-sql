articulos = [
  {
    "nombre": "producto1",
    "clave": "01",
    "precio bruto": 5000,
  },
  {
    "nombre": "producto2",
    "clave": "02",
    "precio bruto": 6000,
  },
  {
    "nombre": "producto3",
    "clave": "01",
    "precio bruto": 4500,
  },
  {
    "nombre": "producto4",
    "clave": "02",
    "precio bruto": 5500,
  },
  {
    "nombre": "producto5",
    "clave": "01",
    "precio bruto": 4800,
  },
  {
    "nombre": "producto6",
    "clave": "02",
    "precio bruto": 5200,
  },
  {
    "nombre": "producto7",
    "clave": "01",
    "precio bruto": 5300,
  },
  {
    "nombre": "producto8",
    "clave": "02",
    "precio bruto": 4700,
  },
  {
    "nombre": "producto9",
    "clave": "01",
    "precio bruto": 4900,
  },
  {
    "nombre": "producto10",
    "clave": "02",
    "precio bruto": 5800,
  }
]

descuentos = {
    "01": 0.1,
    "02": 0.2
}

for art in articulos:
    art["precio neto"] = art["precio bruto"] - art["precio bruto"] * descuentos[art["clave"]]

    print("-------------------------")
    print(f"Nombre: {art['nombre']}")
    print(f"Clave: {art['clave']}")
    print(f"Precio bruto: {art['precio bruto']}")
    print(f"Precio neto: {art['precio neto']}")
    print("-------------------------")