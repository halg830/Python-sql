import numpy as np
#vectores propuestos
vector1 = np.array([5, 13, 1, -9])
vector2 = np.array([-2, -6, 4, -8])
matriz1 = np.array(([[1, -2, 5], [2, 5, -8], [2, 1, 0]]))
matriz2 = np.array(([[-1, 7, 3], [-8, 2, -10], [-2, 2, 5]]))
#Realizar operaciones con los vextores propuestos

#Suma de matrices
print("Matriz 1: ")
print(matriz1)
print("Matriz 2:")
print(matriz2)
print("La suma de las matrices es: ")
print(matriz1+matriz2)

#Resta de matrices
print("La resta entre matriz 2 y la matriz 1 es: ")
print(matriz2-matriz1)

#Suma de matriz y escalar
print('el escalar de la suma de las matrices es: ')
print(10*(matriz1+matriz2))

#Suma de vector y escalar
print("El vector 1 es: ")
print(vector1)
print("El vector 2 es: ")
print(vector2)
print("La suma de los vectores es: ")
vs = vector1+vector2
print(vs)
print("El escalar del resultado es: ")
print(vs*10)

#Tranpuesta de una matriz
print("Matriz 1: ")
print(matriz1)
print("La traspuesta de la matriz 1 es: ")
print(matriz1.T)

#Multiplicación de un escalar y un vector
print("La multiplicación del vector 1 y el vector 2 es: ")
mv = vector1*vector2
print(mv)
print("El escalar del resultado es: ")
print(10*mv)

#Multiplicación de un escalar y una matriz
print("La multiplicación entre la matriz 2 y la matriz 1 es: ")
mm = matriz2*matriz1
print(mm)
print("El escalar del resultado es: ")
print(mm*10)

#Multiplicación de vectores
print("La multiplicación entre vectores 1 y 2 es: ")
mv = np.dot(vector1,vector2)
print(mv)

#Multiplicación de matrices
print("La multiplicación entre las matrices 1 y 2 es: ")
mm = np.dot(matriz1, matriz2)
print(mm)

#Operadores con matrices
#add() esto es suma
print("Matriz 1: ")
print(matriz1)
print("Matriz 2: ")
print(matriz2)
print("La operación add en las matrices es: ")
addm = np.add(matriz1, matriz2)
print(addm)

#Subtract() esto es resta
print("El resultado de la operación dot es: ")
sm = np.subtract(matriz1, matriz2)
print(sm)

#Multiply() esto es multiplicar el elemento a elemento
print("El resultado de la operación multiply es: ")
mulm = np.multiply(matriz1, matriz2)
print(mulm)

#dot() multiplicar por un valor(numero)
print("El resultado de la operación es: ")
dm = np.dot(matriz2,5)

#divide() dividir dos matrices elemento a elemento
print('el resultado de la operación divide es: ')
pm = np.divide(matriz1,matriz2)
print(pm)

#mod() dividir dos matrices y obtener el resto de la división , elemento a elemento
print("El resultado de la operación mod es: ")
modm = np.mod(matriz2,matriz1)
print(modm)

#divmod() Dividir dos arrays y obtener el cociente y el resto de la división
print("El resultado de la operación divmod es: ")
divm = np.divmod(matriz1,matriz2)
print(divm)

#negative() Cambiar el signo a lso valores de un array.
print("El resultado de la operación negativa es: ")
negm = np.negative(matriz1)
print(negm)

#sqrt() Calcular la raíz cuadrada, elemento a elemento.
print("El resultado de la operación sqrt es: ")
rm = np.sqrt(matriz2)
print(rm)








