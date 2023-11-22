"""
Escribir un programa que cree un diccionario simulando una cesta de la compra
el programa debe preguntar el artículo y su precio y añadir el par al diccionario,
hasta que el usuario decida terminar
después se debe mostrar por pantalla la lista de la compra y el coste total
con el siguiente formato:
producto1 -> 1000
producto2 -> 1000
producto3 -> 1000
coste total -> 3000
"""

cesta = {}
continuar = True
while continuar:
    item = input('Introduce un artículo: ')
    precio = float(input('Introduce el precio de ' + item + ': '))
    cesta[item] = precio
    continuar = input('¿Quieres añadir artículos a la lista (1 = Sí /2 = No)? ') == "1"
costo = 0
print('Lista de la compra')
for item, precio in cesta.items():
    print(item, " -> ", precio)
    costo += precio
print('Coste total: ', costo)