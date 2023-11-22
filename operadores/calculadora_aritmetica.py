a=int(input('Digite el primer número: '))
b=int(input('Digite el segundo número: '))
o=str(input('Digite la operación que desea realizar: \n s: suma \n r: resta \n m: multiplicación \n d: división \n %: modulo \n e: exponente \n c: cociente \n'))

if o=="s":
    r=a+b
elif o=="r":
    r=a-b
elif o=="m":
    r=a*b
elif o=="d":
    r=a/b
elif o=="%":
    r=a%b
elif o=="e":
    r=a**b
elif o=="c":
    r=a//b

print('El resultado de la operación es: ',r)