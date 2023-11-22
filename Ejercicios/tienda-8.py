articulo = input("Digite el artículo: ")
costo = float(input("Digite el costo básico: "))

if costo<=30:
    impuesto = 0
elif costo<=60:
    impuesto = 0.3
elif costo <=400:
    impuesto = 0.4
elif costo>400:
    impuesto = 0.5

if costo > 30:  
    costo+=costo*impuesto

print("El costo por el artículo ", articulo, " es: ", costo)