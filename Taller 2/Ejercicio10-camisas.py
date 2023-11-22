cant = int(input("Ingrese la cantidad de camisas: "))
precio = int(input("Ingrese el precio: "))

descuentos = {
    "mayor3": 0.2,
    "menos3": 0.1
}

if cant >= 3:
    total = precio - precio*descuentos["mayor3"]
else:
    total = precio -precio*descuentos["menos3"]

print(total)