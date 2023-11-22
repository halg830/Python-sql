largo = float(input("Digite el largo en metros: "))
ancho = float(input("Digite el ancho en metros: "))
precio = float(input("Digite el precio por metro cuadrado: "))

descuento = 0.1

mCuadrado = largo*ancho
total=mCuadrado*precio

if mCuadrado>400:
    total-=total*descuento

print("El precio del terreno es: ", total)