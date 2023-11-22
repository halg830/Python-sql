nombre = input("Su nombre por favor: ")
altura = float(input("Digite su estatura en decimal(ejemplo: 1.55(metros)): "))
estatura = altura
peso = float(input("Digite su peso (kilogramos):"))
imc = peso /estatura**2

if imc>=0 and imc<=15.99:
    print (nombre,"Estas...Extremadamente delgado", imc)
elif imc>=16.00 and imc<=18.49:
    print(nombre, "Estas...Delgado",imc)
elif imc>=18.50 and imc<=24.99:
    print(nombre ,"Estas..en el peso adecuado", imc )
elif imc>=25.00 and imc<=29.99:
    print(nombre, "Estas...en sobrepeso", imc)
elif imc>=30.00 and imc <=34.99:
    print(nombre, "Estas...en obesidad", imc)