import numpy as np

#Ejercicios

lista_de_listas=[ [-44,12], 
                  [12.0,51], 
                  [1300, -5.0]]
a = np.array(lista_de_listas)

print("Matriz original")
print(a)


# Restarle 5 a la fila 2 de la matriz
#IMPLEMENTAR
print("Restar 5 a fila 1")
a[1,:]=a[1,:]-5
print(a)

# Multiplicar por 2 toda la matriz
#IMPLEMENTAR
print("Multiplicar por 2 todo")
a=a*2
print(a)

# Dividir por -5 las dos primeras filas de la matriz
#IMPLEMENTAR
print("Dividir por -5")
a[0:2,:]=a[0:2,:]/5
print(a)


#Imprimir la ultima fila de la matriz
print("Ultima fila")
ultima_fila=a[2] # IMPLEMENTAR
print(ultima_fila)
