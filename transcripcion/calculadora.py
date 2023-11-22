numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese un número: "))

print("¿Qué operación desea hacer?")
print("a -> sumar")
print("b -> restar")
print("c -> multiplicar")
print("d -> dividir")

operacion = input("Elija una opción: ")
if operacion == "a":
    suma = numero1 +numero2
    print("El resultado es: ", suma)
elif operacion=="b":
    suma = numero1 - numero2
    print("El resultado es: ", suma)
elif operacion=="c":
    suma = numero1 * numero2
    print("El resultado es: ", suma)
elif operacion=="d":
    suma = numero1 / numero2
    print("El resultado es: ", suma)
else:
    print("Digito la opción equivocada")