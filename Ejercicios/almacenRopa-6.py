cant = int(input("Digite la cantidad de trajes: "))
precioUnidad = float(input("Digite el precio por unidad: "))
modelo = input("Digite el modelo: ")

descuento = 0.17

total=cant*precioUnidad

if cant >=3:
    total-=total*descuento

print("El total es: ", total)
