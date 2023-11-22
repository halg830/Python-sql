import numpy as np

#vectores y matrices propuestos 
vector1 = np.array([5, 13, 1, -9])
vector2 = np.array([-2, -6, 4, -8])
matriz1 = np.array(([[1, -2,5], [2, 5,-8], [2, 1,0]]))
matriz2 = np.array(([[-1, 7,3], [-8, 2,-10], [-2, 2,5]]))

#Realizar operaciones con los vectores y matrices propuestos

#Suma de matrices
print("Suma matriz: ", matriz1+matriz2)

#Resta de matrices
print("Resta matrices: ", matriz1-matriz2)

#Suma de matriz y escalar
escalar = 5
print("Suma matriz y escalar: ", matriz1+escalar)

#Suma de vector y escalar
print("Suma de vector y escalar: ", vector1+escalar)

#Transpuesta de una matriz
print("Transpuesta matriz: ", matriz1.T)

#Multiplicación de un escalar y un vector
print("Multi escalar y vector: ", escalar*vector1)

#Multiplicación de un escalar y una matriz
print("Multi escalar y matriz: ", escalar*matriz1)

#Multiplicación de vectores
print("Multi vectores: ", vector1*vector2)

#Multiplicación de matrices
print("Multi matrices: ", matriz1*matriz2)

##Operaciones con matrices

#add() esto es suma
add = np.add(matriz1, matriz2)
print("add: ", add)

#subtract() esto es resta
subtract = np.subtract(matriz1, matriz2)
print("Subtract: ", subtract)

#multiply() esto es multiplicar elemento a elemento
multiply = np.multiply(matriz1, matriz2)
print("multiply: ", multiply)

#dot() multiplicar por un valor (numero)
dot = np.dot(matriz1, matriz2)
print("dot: ", dot)

#divide() dividir dos matrices elemento a elemento
print("divide: ", np.divide(matriz1, matriz2))

#mod() Dividir dos matrices y obtener el resto de la división, elemento a elemento.
print("mod: ", np.mod(matriz1, matriz2))

#divmod() Dividir dos arrays y obtener el cociente y el resto de la división, elemento a elemento.
print("divmod: ", np.divmod(matriz1, matriz2))

#negative() Cambiar el signo a los valores de un array.
print("negative: ", np.negative(matriz1, matriz2))

#sqrt() Calcular la raíz cuadrada, elemento a elemento.
print("sqrt: ", np.sqrt(matriz1))
  