"""
5. Escribir un programa que cree un diccionario de listado
de clientes. El programa debe preguntar el cliente y su ciudad
de origen y añadir la dupla al diccionario, hasta que el usuario
decida temrinar. Después se mostrar por pantalla la lista de 
clientes, con el siguiente formato. Probar con la tabla adjunta y 
adjuntar al trabajo imagen de la impresión en pantalla.
producto1 -> 1000
producto2 -> 1000
producto3 -> 1000
coste total -> 3000
"""

clientes = {}
continuar = True
while continuar:
    cliente = input('Introduce el nombre del cliente: ')
    ciudad = input('Introduce la ciudad ' + cliente + ': ')
    clientes[cliente] = ciudad
    continuar = input('¿Quieres añadir otro cliente a la lista? (1 = Sí /2 = No)? ') == "1"

print('Lista de clientes')
for cliente, ciudad in clientes.items():
    print(cliente, 'esta en la ciudad de', ciudad)