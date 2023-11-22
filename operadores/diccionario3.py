"""
3. Escribir un programa que guarde en un diccionario los precios de los productos de 
la tabla, pregunte al usuario por un producto, una cantidad de ese producto y muestre
por pantalla el precio de la cantidad de productos comprado. Si el producto no está
en el diccionario debe mostrar un mensaje informando de ello.
"""

productos = {'Pantalla': 1500, 'Teclado': 9400, 'Mouse': 3600, 'Impresora': 978000,
             'Dvd': 12000, 'Memoria': 35000, 'SCANER': 40000}
producto = input('¿Qué producto quiere?').title()
unidad = float(input('¿Cuántas unidades?'))
if producto in productos:
    print(unidad, 'unidades de', producto, 'valen', productos[producto]*unidad, '$')
else:
    print("Lo siento, en producto", producto, "no esta diosponible.")