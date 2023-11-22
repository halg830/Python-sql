"""
1. Escribir un programa que almacene el diccionario las notas
de una asignatura {'Nota1': 3.5, 'Nota2': 4.3, 'Nota3': 3.7}
y después muestre por pantalla cada una de las notas en el formato 
la <notas> tiene un valor de <valor>, donde <notas> es cada una de 
las notas del curso, y <valor< son los valores para cada nota.
Al final debe mostrar también el primedio total del curso.
"""

notas = {'Nota1': 3.5, 'Nota2': 4.3, 'Nota3': 3.7}
valor = 0
for asignatura, creditos in notas.items():
    print(asignatura, 'tiene', creditos, 'creditos')
    valor += creditos / 3
print('promedio de las notas: ', valor)