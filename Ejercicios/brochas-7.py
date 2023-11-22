cantBrochas = int(input("Digite la cantidad de brochas: "))
precioBrochas = float(input("Digite el precio unitario de la brocha: "))
cantRodillos = int(input("Digite la cantidad de rodillos: "))
precioRodillos = float(input("Digite el precio unitario del rodillo: "))
cantSellador = int(input("Digite la cantidad de selladores: "))
precioSellador = float(input("Digite el precio unitario del sellador: "))
print("Eliga el método de pago: \n a-Crédito \n b-Contado")
tipoPago = input("Digite una opción: ")

descuentoBrochas = 0.2
descuentoRodillos = 0.15
descuentoContado = 0.07

totalBrochas = cantBrochas*precioBrochas
totalRodillos = cantRodillos*precioRodillos
totalSellador = cantSellador*precioSellador

totalBrochas -=totalBrochas*descuentoBrochas
totalRodillos -=totalRodillos*descuentoRodillos

total = totalBrochas+totalRodillos+totalSellador

if tipoPago == "a": 
    print("El total de la orden es: ",total)
elif tipoPago == "b":
    total-=total*descuentoContado
    print("El total de la orden es: ", total)
elif tipoPago != "a" or tipoPago != "b":
    print("Tipo de pago incorrecto")

