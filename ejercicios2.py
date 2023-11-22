import numpy as np

lista_de_listas=[ [-44,12], 
                  [12.0,51], 
                  [1300, -5.0]]
a = np.array(lista_de_listas)

print("Matriz original")
print(a)

# Más ejercicios

# Calcular la suma de los elementos de a utilizando dos fors anidados
print("for anidados")
suma = 0
for sub in a:
    for elemento in sub:
        suma+=elemento
#IMPLEMENTAR
print(suma)

# Calcular la suma de los elementos de a utilizando np.sum
#IMPLEMENTAR
print("sumar np")
sumar = np.sum(a)

# Calcular el promedio de los elementos de las primeras dos filas de a utilizando dos fors anidados
print("promedio for anidados")
promedio=0
#IMPLEMENTAR
rows = 2
columns = len(a[0])

for i in range(rows):
    for j in range(columns):
        promedio+=a[i][j]

promedio/=rows*columns
print(promedio)

# Calcular el promedio de los elementos de las primeras dos filas de utilizando slices y np.mean
#IMPLEMENTAR
print("promedio con np")
npPromedio = np.mean(a[:2])
print(npPromedio)