cantGalones = float(input("Ingrese la cantidad de galones: "))
precioLitro = float(input("Ingrese el precio por litro: "))

galon = 3.785411784

precioGalon = galon*cantGalones/precioLitro

print("El precio en galones es: ", precioGalon)
