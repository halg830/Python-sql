print("Tarifa por hora")
valor = int(input())
print("Horas del día")
h = int(input())

# tarifa=valor*h
if h > 40:
    sal = valor * h
    bon = sal * 0.2
    print('El valor a pagar es: ', sal+bon)
else:
    sal=valor*h
    print('El valor a pagar es: ', sal)