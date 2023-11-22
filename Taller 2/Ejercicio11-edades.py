fechaNacimiento = int(input("Ingrese su año de nacimiento: "))
fechaActual = int(input("Ingrese el año actual: "))

if fechaActual < fechaNacimiento:
    print("El año actual no puede ser inferior al de nacimiento")

edad = fechaActual-fechaNacimiento

if edad<1 or edad>99:
    print("Edad invalida")
    print(edad)