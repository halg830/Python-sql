a=7; b=2 #asignar
#Esto usa el valor de x para sumarle el valor que le digamos, en este caso b
print("Operadores de asignación")
x=a; x+=b;  print("x+=", x)  # 9 sumar
x=a; x-=b;  print("x-=", x)  # 5 restar
x=a; x*=b;  print("x*=", x)  # 14 multiplicar
x=a; x/=b;  print("x/=", x)  # 3.5 dividir
x=a; x%=b;  print("x%=", x)  # 1 residuo
x=a; x//=b; print("x//=", x) # 3 cociente (por el que uno multiplica)
x=a; x**=b; print("x**=", x) # 49 potencia
x=a; x&=b;  print("x&=", x)  # 2 
x=a; x|=b;  print("x|=", x)  # 7
x=a; x^=b; print("x^=", x)   # 5
x=a; x>>=b; print("x>>=", x) # 1
x=a; x<<=b; print("x<<=", x) # 28